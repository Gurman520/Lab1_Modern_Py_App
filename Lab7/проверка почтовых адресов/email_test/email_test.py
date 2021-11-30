import email_app.email as email
import unittest


class EmailTest(unittest.TestCase):
    def test_nameEmail(self):
        for i in range(10):
            inp = "../проверка почтовых адресов/input/input0%d.txt" % (i)
            out = "../проверка почтовых адресов/output/output0%d.txt" % (i)
            fin = open(inp, 'r')
            fout = open(out, 'r')
            text_in = fin.read()
            text_out = fout.read()
            text_in = text_in.split()
            n = int(text_in[0])
            emails = []
            for i in range(1, n + 1):
                emails.append(text_in[i])
            filtered_emails = email.filter_mail(emails)
            assert str(filtered_emails) == text_out
