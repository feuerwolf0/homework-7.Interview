import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mailer:
    def __init__(self, email, password, header = None):
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.email = email
        self.password = password
        self.header = header

    def send_message(self, subject, to, message):
        self.subject = subject
        self.recipients = to
        self.message = message
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        server = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        server.ehlo()
        # secure our email with tls encryption
        server.starttls()
        # re-identify ourselves as an encrypted connection
        server.ehlo()
        server.login(self.email, self.password)
        server.sendmail(
            self.email,
            server,
            msg.as_string()
        )
        # close connection
        server.quit()

    def recieve_message(self):
        mailbox = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mailbox.login(self.email, self.password)
        mailbox.list()
        mailbox.select('inbox')
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mailbox.uid('search', None, criterion)

        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        result, data = mailbox.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        # close connection
        mailbox.logout()

        return email_message
    

def main():
    # Создаю мейлер
    mailer = Mailer(
        email='login@gmail.com',
        password='qwerty',
    )
    # Отрпавляю сообщение
    mailer.send_message(
        subject='Subject',
        to=['vasya@email.com', 'petya@email.com'],
        message='Just message'
    )
    # Получаю сообщение
    recieve_message = mailer.recieve_message()


if __name__ == '__main__':
    main()