# Course: CS6507
# Laboratory: Assignment 1
# Date of creation: 2021/03/05
# Author: Amit Somnath Sambrekar
# Number: 120220153
# Description: Write a Python program that prints all pairs of matching records (records of two individuals,
#one from each list, that match up in terms of district, year, quarter, volume and page number).

import re

# Extracting and filtering the data from the text file. 
def filtering_data(files):

    details = (re.sub(r"[\s]*", "", files))
    lines_spaces =(re.split("Marriageof",details))
    remove_space = [elem for elem in lines_spaces if elem.strip()]
    imp_details =[]
    imp_details.clear()
    district_name = []

    for details in remove_space:
        district_name.clear()
        names = re.findall('^[A-Z]+', details)
        digits = re.findall('[0-9]+', details)
        district = re.findall('(?<=RegArea).*(?=ReturnsYear)', details)
        district_str = ''.join(district)
        district_name.append(district_str)
        names.extend(digits)
        names[2:2] = district_name
        imp_details.append(names)
    return imp_details

# Function to match the strings from the two given files...
def find_matches(nfile,mrfile):
    count_f = 0
    for det in nfile:
        count_f += 1
        details_female = ''.join(det[1:])
        count_m =0
        for detm in mrfile:
            count_m += 1
            details_male = ''.join(detm[1:])
            # Using finditer to find possible match
            for exact_match in re.finditer(details_female, details_male):
                # Printing the values from the possibe match.
                print(" Possible match!\n",male_names[count_m - 1], "and", female_names[count_f - 1], "in", det[2], "in", det[1])
                print(" Quarter =", det[4],", Volume =", det[5],", Page =", det[6],"\n")
 

if __name__ == '__main__':
    
    with open('mary_roche.txt','r') as file1:
        female_file = file1.read()
        # Extracting the names from the file.
        nameRegex = re.compile(r'Marriage of ([a-zA-Z\s]+(?=\n))',re.DOTALL)
        female_names = nameRegex.findall(female_file)

    with open('nicholas.txt','r') as file2:
        male_file = file2.read()
        # Extracting the names from the file.
        nameRegex = re.compile(r'Marriage of ([a-zA-Z\s]+(?=\n))',re.DOTALL)
        male_names = nameRegex.findall(male_file)
    try:
        male_details=filtering_data(male_file)
        female_details=filtering_data(female_file)
        find_matches(female_details,male_details)

    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        print("Press Enter to Exit!")
        input()