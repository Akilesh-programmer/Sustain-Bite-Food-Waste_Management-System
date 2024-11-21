import tkinter  as tk
from registration import supplier_register, restaurant_register
from login import supplier_login, restaurant_login

def main():
    root = tk.Tk()
    root.title("Sustain Bite")
    root.geometry("500x250")

    restaurant_login_button = tk.Button(root, text="Restaurant Login", height=1,
                                        font=("Arial", 20), width=16,
                                        command=restaurant_login)
    restaurant_register_button = tk.Button(root, text="Restaurant Register", 
                                           font=("Arial", 20), 
                                           width=16, 
                                           command=restaurant_register)

    supplier_login_button = tk.Button(root, text="Supplier Login", height=1, 
                                      font=("Arial", 20), width=16, 
                                      command=supplier_login)
    supplier_register_button = tk.Button(root, text="Supplier Register", 
                                         height=1, font=("Arial", 20), width=16,
                                           command=supplier_register)

    restaurant_login_button.pack()
    restaurant_register_button.pack()
    supplier_login_button.pack()
    supplier_register_button.pack()

    root.mainloop()
    


if __name__ == "__main__":
    main()