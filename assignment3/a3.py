# Course: CS6507
# Laboratory: Assignment 3
# Date of creation: 2021/03/25
# Author: Amit Somnath Sambrekar
# Number: 120220153

# Importing packages needed for the assignment
from email.parser import Parser
import os


def email_between(suspects):
    result =[]
     # Iterating through all the directories fom the curent folder.
     ## Only folder to be present as per assignment: 'enron_email_corpus'
    for root, dirs, files in os.walk(os.getcwd()):  
        for file in files: 

            # Reading through email files in each folder present.
            with open(os.path.join(root, file), "r",errors='ignore') as email_file:

                # Calling email package to extract email objects
                email = Parser().parse(email_file)
                from_raw_details =(email['from'])
                from_details = from_raw_details

                # Checking for the suspects details in ''to' and 'from' fields in email.
                
                for _, val in red_flags.items():
                        for det in val:
                            if det == from_details: # Condition for 'from' field in the email.
                                to_raw = (email['to']).split() # Extracing value from the 'to' field.
                                to_new = [s.replace(',', '') for s in to_raw]
                                for _, names in red_flags.items():
                                    try:
                                        for values  in names:
                                            if values in to_new:
                                                to_details_raw = (email['to']).split()
                                                to_details = [s.replace(',', '') for s in to_details_raw]
                                                if len(to_details) <= 20 : # Condition for less <= 20 receipents
                                                    print("Path of the email: ",email_file)
                                                    result.append(email)
                                              
                                            else:
                                                if names in to_new: # If only one receipt is present.
                                                    print("Path of the email: ",email_file)
                                                    result.append(email)
                                                    
                                    except:
                                        pass                                   
                            else:
                                pass
    return result
if __name__ == '__main__':    
    # Suspects dictionary
    red_flags = {"lay-k": ["kenneth.lay@enron.com", "klay@enron.com"],
    "skilling-j": ["skilling@enron.com", "jeff.skilling@enron.com"]}
    suspects = red_flags
    print(email_between(suspects)) # Calling the main function