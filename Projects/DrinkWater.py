#Drink Water Notification

import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "***Drink Water Now and Stretch your body!!!",
            message = "Drink atleast 4L fluid in a day.",
            app_icon = "E:\Python\glass.ico",
            timeout = 5
        )
        time.sleep(3600)