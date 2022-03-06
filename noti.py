from plyer import notification
import time

while True:
	notification.notify(title = "BT-CANBNK",
		message = "An amount of INR 40000.00 has been DEBITED to your account XXXX0094 on 24/02/2022. Total Available balance 14,785.45 -Canara bank", 
		timeout = 7)
	time.sleep(10)

input()