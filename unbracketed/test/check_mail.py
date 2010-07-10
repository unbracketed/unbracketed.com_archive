from django.core.mail import mail_admins

mail_admins( 'test', 'this is a test mail to all admins' )