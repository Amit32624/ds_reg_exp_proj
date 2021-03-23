from email.parser import Parser
import os
parser = Parser()
red_flags = {"lay-k": ["kenneth.lay@enron.com", "klay@enron.com"],"skilling-j": ["skilling@enron.com", "jeff.skilling@enron.com"]}
a=[]
for i in red_flags.values():
    print(red_flags.values())
    a.append(i)
flat_list = [item for sublist in a for item in sublist]
for root, dirs, files in os.walk('enron_email_corpus_2'):
     for file in files:
        print("files",file)
        with open(os.path.join(root, file), "r") as auto:
            email = parser.parsestr(auto.read())
            try:
                to_mail=email.get('To').split()
                print("to_mail",to_mail)
                to_mail_final=[s.replace(',', '') for s in to_mail]
                print("to_mail_final",to_mail_final)
                from_mail = email.get('From').split()
                from_mail_final = [s.replace(',', '') for s in from_mail]
                print("from_mail_final",from_mail_final)
                print(email.get_payload())

            except:
                to_mail = email.get('X-To').split()
                to_mail_final = [s.replace(',', '') for s in to_mail]
                to_mail_final_1 = [s.replace(':', '') for s in to_mail_final]
                from_mail = email.get('X-To').split()
                from_mail_final = [s.replace(',', '') for s in from_mail]
                from_mail_final_1 = [s.replace(':', '') for s in from_mail_final]
                print(from_mail_final_1,root,file)
                print(email.get_payload())

