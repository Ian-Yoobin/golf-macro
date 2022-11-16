import time
import selenium
from tkinter import * 
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

root =Tk()
root.geometry("600x400")
root.title("Auto Booking")
root.resizable(False,False)



def btn1press():
    btn.config(text=ent.get())
    global id
    id=ent.get()

def btn2press():
    btn2.config(text=ent2.get())
    global pw
    pw=ent2.get() 


def start():
    driver = webdriver.Chrome()
    url='https://city-of-burnaby-golf.book.teeitup.com/login'
    driver.get(url)
    driver.maximize_window()
    action =ActionChains(driver)
    time.sleep(1)
    action.send_keys(id).perform()

    driver.find_element(By.ID,'txtPassword').click()
    action.send_keys(pw).perform()

    time.sleep(100)  

ent=Entry(root)
ent.pack()

ent2=Entry(root)
ent2.pack()

btn=Button(root)
btn.config(text="ID save")
btn.config(width=20)
btn.config(command=btn1press)
btn.pack()

btn2=Button(root)
btn2.config(text="Password save")
btn2.config(width=20)
btn2.config(command=btn2press)
btn2.pack()

btn3=Button(root)
btn3.config(text="Start")
btn3.config(width=10)
btn3.config(command=start)
btn3.pack()

root.mainloop()

