import re

file = open("input.txt", "r")
text = file.read()
file.close()

emails = re.findall(r'\S+@\S+\.\S+', text)

print("Email addresses found:")

for email in emails:
    print(email)

print("Total emails:", len(emails))

# OUTPUT
Email addresses found:
abc@gmail.com
xyz@yahoo.com.
student123@college.edu.
Total emails: 3
