import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Sir, Please take a Break of 20 sec...",
            message="If you find yourself gazing at screens all day, "
                    "Basically, every 20 minutes spent using a screen;"
                    " you should try to look away at something that is "
                    "20 feet away from you for a total of 20 seconds.",
            # app_icon="C:\Users\Srijan Samridh\Desktop\Python\Notification Reminder App\icon.ico",
            app_name="Eye Alert!",
            timeout=2
        )
        # time.sleep(20*60)
        time.sleep(6)
