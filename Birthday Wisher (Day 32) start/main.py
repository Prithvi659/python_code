import datetime as dt
import pandas
import random
import smtplib

data_file=pandas.read_csv("birthdays.csv")

today=dt.datetime.now()
letters=[]
placeholder="[NAME]"
my_email="yourgmail@gmail.com"
password="*************"#to get password go to gmail -> security -> complete 2 factor authentication
                            # search for app password and create new password


for index,row in data_file.iterrows():
    data=(row["name"],row["year"],row["month"],row["day"],row["email"])

    if row["month"] == today.month and row["day"] == today.day:
        for i in range(1,4):
            with open(f"letter_templates/letter_{i}.txt") as file:
                letters.append(file.read())
        letter=random.choice(letters)
        new_letter=letter.replace(placeholder,row["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday\n\n{new_letter}")


































        # with open("letter_templates/letter_1.txt") as letter_1:
        #     content_1=letter_1.read()
        # with open("letter_templates/letter_2.txt") as letter_2:
        #     content_2 = letter_2.read()
        # with open("letter_templates/letter_3.txt") as letter_3:
        #     content_3 = letter_3.read()
        # letters.append(content_1)
        # letters.append(content_2)
        # letters.append(content_3)
        # letter=random.choice(letters)
        # print(letter)

