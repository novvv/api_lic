from falcon_rest.contrib.mailer import Mailer as _Mailer
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders

class Mailer(_Mailer):
    def send(self, addr_from, addr_to, addr_cc=None):
        if self.content_html:
            msg = MIMEMultipart('alternative')
            msg.attach(MIMEText(self.content_text, 'plain', 'utf-8'))
            msg.attach(MIMEText(self.content_html, 'html', 'utf-8'))
        else:
            msg = MIMEText(self.content_text)
        att_num = 0
        if hasattr(self,'attachments'):
            for typ, data in self.attachments:
                subtype = 'octet-stream'
                if typ in ('csv','xls'):
                    subtype = 'vnd.ms-excel'
                attachment = MIMEApplication(data, subtype)
                # attachment.set_payload(fp.read())
                encoders.encode_base64(attachment)
                attachment.add_header("Content-Disposition", "attachment", filename='attachment' + str(att_num) + '.' + typ)
                msg.attach(attachment)

        msg['Subject'] = self.subject
        msg['To'] = addr_to

        msg['From'] = addr_from

        if addr_cc:
            msg['Cc'] = addr_cc

        result = self.smtp.sendmail(addr_from, addr_to, msg.as_string())
        self.smtp.quit()
        return result

    def get_content(self):
        import re
        def cleanhtml(raw_html):
            cleanr = re.compile('<.*?>')
            raw_html = raw_html.replace('\r', '').replace('\n', '').replace('\t', '')
            cleantext = re.sub(cleanr, '', raw_html)
            return cleantext

        if self.content_html:
            return cleanhtml(self.content_html)
        else:
            return self.content_text
