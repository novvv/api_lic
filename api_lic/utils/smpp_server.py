from api_lic.utils.smpplib import consts,smpp
from api_lic.utils.smpplib.server import Server
import logging
import sys
from falcon_rest.db.orm import generate_uuid_str

logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')

from pynput import keyboard


s=None
kannel=None

def dump_pdu(p):
    print(p.__class__.__name__)
    for k in p.params.keys():
        print(k,'=',getattr(p,k,None))

class SmppServer(Server):
    @staticmethod
    def authorization_handler(pdu, client, **kwargs):
        global kannel
        if pdu.system_id== 'Wcpittktdi' and pdu.password== 'Gapypafm':

            kannel=client
            return True
        elif pdu.system_id== 'client' and pdu.password== 'Gapypafm':
            return True
        else:
            return False
    @staticmethod
    def new_sms_handler(pdu, client, **kwargs):
        global kannel
        dump_pdu(pdu)
        if client == kannel:
            #here is inbound route
            answer_pdu=smpp.make_pdu('data_sm',
                                client=kannel,
                                message_payload=pdu.short_message.encode(),
                                source_addr=pdu.source_addr,
                                destination_addr=pdu.destination_addr,
                                esm_class=consts.SMPP_MSGMODE_FORWARD,
                                data_coding=consts.SMPP_ENCODING_DEFAULT,
                                dest_addr_ton=consts.SMPP_TON_INTL,
                                dest_addr_npi=consts.SMPP_NPI_ISDN,
                                source_addr_ton=consts.SMPP_TON_INTL,
                                source_addr_npi=consts.SMPP_NPI_ISDN,
                                service_type='VMA',
                                registered_delivery=0,
                                alert_on_message_delivery=None
                                )

            kannel.send_pdu(answer_pdu)

        else:
            #here is outbound route
            kannel.send_pdu(pdu)
        return generate_uuid_str()()

s=SmppServer()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char=='q':
            client = s.clients[0]
            p = smpp.make_pdu('enquire_link', client=client)
            client.send_pdu(p)
    except AttributeError:
        print('special key {0} pqressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

if __name__ == "__main__":

    s.set_authorization_handler(SmppServer.authorization_handler)
    s.set_new_sms_handler(SmppServer.new_sms_handler)
    s.up()
    print('start')
    key=''
    #while s.state == consts.SMPP_SERVER_STATE_OPEN and key !='q':
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    print('run')
    s.down()
    s.server_thread.join()
    print('bye')


