from email.parser import Parser
from email.policy import default

# If the e-mail headers are in a file, uncomment these two lines:
# with open("1_", 'rb') as fp:
#     headers = BytesParser(policy=default).parse(fp)
# headers = BytesParser(policy=default).parse(fp)
#  Or for parsing headers in a string (this is an uncommon operation), use:
# headers = Parser(policy=default).parsestr(
#         'From: Foo Bar <user@example.com>\n'
#         'To: <someone_else@example.com>\n'
#         'Subject: Test message\n'
#         '\n'
#         'Body would go here\n')

#  Now the header items can be accessed as a dictionary:
red_flags = {"lay-k": ["kenneth.lay@enron.com", "klay@enron.com"],
"skilling-j": ["skilling@enron.com", "jeff.skilling@enron.com"]}
import os
for root, dirs, files in os.walk('enron_email_corpus_2'):
    
    for file in files:
        # print(root)
        # print("files",file)
        with open(os.path.join(root, file), "r") as auto:
            headers = Parser().parse(auto)
            to =[]
            # print('To: %s' % headers['to'])
            # to_raw = (headers['to']).split()
            # to_new = [s.replace(',', '') for s in to_raw]
            from_raw =(headers['from'])
            from_ = from_raw
            for key, val in red_flags.items():
                try:
                    for i in val:
                        if i ==from_:
                            # print("from",i)
                            to_raw = (headers['to']).split()
                            # print("to_raw",to_raw)
                            to_new = [s.replace(',', '') for s in to_raw]
                            # print(to_new)
                            for k, v in red_flags.items():
                                try:
                                    for l in v:
                                        if l in to_new:
                                            print(file)
                                            # print("i",i)
                                            print('Date: %s' % headers['Date'])
                                            print('From: %s' % headers['from'])
                                            print('To:%s' % headers['To'])
                                            print('Subject: %s' % headers['subject'])
                                            # print(headers.get_payload())
                                except:
                                    if v in to_new:
                                        print("Random",i)
                                        print('Date: %s' % headers['Date'])
                                        print('From: %s' % headers['from'])
                                        print('To:%s' % headers['To'])
                                        print('Subject: %s' % headers['subject'])
                                        # print(headers.get_payload())
                                        
                        else:
                            pass
                except:
                    pass

            # print("to_new",to_new)
            
            # for k, v in red_flags.items():
            #     try:
            #         for i in v:
            #             # print("v",v)
            #             if i in to_new:
            #                 # print("i",i)
            #                 # print(k)
            #                 print(i)
            #                 print('Date: %s' % headers['Date'])
            #                 print('From: %s' % headers['from'])
            #                 print('To:',i)
            #                 print('Subject: %s' % headers['subject'])
                            
            #     except:
            #         if v in to_new:
            #             # print("k_",k)
            #                 print(i)
            #                 print('Date: %s' % headers['Date'])
            #                 print('From: %s' % headers['from'])
            #                 print('To:',i)
            #                 print('Subject: %s' % headers['subject'])

            

            # # You can also access the parts of the addresses:
            # print('Recipient username: {}'.format(headers['to'].addresses[0].username))
            # print('Sender name: {}'.format(headers['from'].addresses[0].username))

