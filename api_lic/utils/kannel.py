#!/usr/bin/env python3

import cgi
from urllib.parse import urlencode, unquote, quote_plus
import requests
import re
from api_lic import model,settings
from falcon_rest.logger import log


def unprefix(s):
    if s[0:2] == '+1' and len(s) == 12:
        return s[2:]
    return s

class KannelException(Exception):
    pass


class SmsSender():
    def __init__(self, username, password, charset="utf-8", coding=1, send_url="http://localhost:13013/cgi-bin/sendsms"):
        self.un = username
        self.pw = password
        self.charset = charset
        self.coding = coding
        self.send_url = send_url
        self.buffer = []

    def send(self, src, dest, message, buffer=False):

        # if this message should be bufferred,
        # then stash it until self.flush is called
        if buffer:
            self.buffer.append((src, dest, message))
            return True

        # strip any junk from the destination -- the exact
        # characters allowed vary wildy between installations
        # and networks, so we'll play it safe here
        dest = re.compile('\D').sub("", dest)

        # urlencode to make special chars
        # safe to embed in the kannel url
        msg_enc = quote_plus(message)

        # send the sms to kannel via a very
        # unpleasent-looking HTTP GET request
        # (which is a flagrant violation of the
        # HTTP spec - this should be POST!)
        try:
            url = '{}?username={}&password={}&charset={}&coding={}&to={}&' \
                  'from={}&text={}'.format(self.send_url, self.un, self.pw, self.charset, self.coding,
                                               dest, src, msg_enc)
            log.debug('kannel send {}'.format(url))
            response = requests.get(url, timeout = (2, 4))
            if response.status_code != 202:
                raise KannelException(response.content.decode('utf-8'))
        except Exception as e:
            raise KannelException(e)

        # for now, just return a boolean to show whether
        # kannel accepted the sms or not. todo: raise an
        # exception with the error message upon failure
        return response.content.decode('utf-8').startswith("0: Accepted")

    def flush(self):
        # send any buffered messages. no magic here...
        # (the SmsApplication library removes duplicates)
        for tuple in self.buffer:
            src,dest, msg = tuple
            self.send(src,dest, msg, False)


# if this is invoked directly, test things out by listening
# for incomming SMSs, and relaying them to a test number.
# obviously, for this to work, the kannel user + password
# must be correct (see /etc/kannel/kannel.conf)
if __name__ == "__main__":
    sender = SmsSender(username="denovo", password="xyoo5Ichex")
    sender.send('0301','0302', "Test message по русски")
    #sender.send('0301','8901891597', "Test message по русски")



