# Exercise 11: Solution + Shoutouts - Desktop Notification System | Python Tutorial - Day #99


from win10toast import ToastNotifier
import time

n = ToastNotifier()

t=18


time.sleep(t)
n.show_toast("HEY DIPAK , DRINK WATER", "You got notification", duration = 8,
 icon_path ="https://assets.materialup.com/uploads/9a462a9b-2856-446a-97af-717c10fe59f9/preview.png")


