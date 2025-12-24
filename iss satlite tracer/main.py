import requests
import smtplib
from datetime import datetime
import time

MY_LAT=15.364708 # Your latitude
MY_LONG=75.123955 # Your longitude
my_email="prithvikalakeri659@gmail.com"
password="*************" #to get password go to gmail -> security -> complete 2 factor authentication
                            # search for app password and create new password

def iss_is_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    )


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow().hour  # IMPORTANT: use UTC

    return time_now >= sunset or time_now <= sunrise


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="prithvikalakerihere@gmail.com",
            msg="Subject:Satellite Above!\n\nLook up! The ISS is overhead."
        )


# BONUS: run every 60 seconds
while True:
    if iss_is_overhead() and is_night():
        send_email()
    time.sleep(60)



