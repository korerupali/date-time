#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''Show Current date-time'''
import tkinter as tk
#import datetime for the time recognizing part
from datetime import datetime

#function to get the current time and update the value every 1sec
def update_label():
    
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label.config(text=current_date_time)
    # Schedule the next update
    window.after(1000, update_label) 
    # Update every 1000 milliseconds (1 second)


window = tk.Tk()
window.geometry("400x60")
window.title('Date&Time')

label = tk.Label(window, text ='rupali', font=("Helvetica",30))
label.pack()

update_label()
window.mainloop()


# In[ ]:




