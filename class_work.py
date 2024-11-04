import re 

file_object = open ('social_media_users.csv')

text_from_file = file_object.read()

emails = re.findall('[a-z]+@[a-z]{4,}\.com',text_from_file)
print(emails)



