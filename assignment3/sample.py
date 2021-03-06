
from email.parser import Parser
import os


def email_between(suspects):

    for root, dirs, files in os.walk(os.getcwd()):  
        for file in files: 
            with open(os.path.join(root, file), "r",errors='ignore') as email_file:
                email = Parser().parse(email_file)
                from_raw_details =(email['from'])
                from_details = from_raw_details
                for _, val in red_flags.items():
                        for det in val:
                            if det == from_details: 
                                to_raw = (email['to']).split() .
                                to_new = [s.replace(',', '') for s in to_raw]
                                for _, names in red_flags.items():
                                    try:
                                        for values  in names:
                                            if values in to_new:
                                                to_details_raw = (email['to']).split()
                                                to_details = [s.replace(',', '') for s in to_details_raw]
                                                if len(to_details) <= 20 : 
                                                    print("Path of the email: ",email_file)
                                                    print(email)
                                            else:
                                                if names in to_new:
                                                    print("Path of the email: ",email_file)
                                                    print(email)
                                    except:
                                        pass                                   
                            else:
                                pass

if __name__ == '__main__':    
    # Suspects dictionary
    red_flags = {"lay-k": ["kenneth.lay@enron.com", "klay@enron.com"],
    "skilling-j": ["skilling@enron.com", "jeff.skilling@enron.com"]}
    suspects = red_flags
    email_between(suspects)