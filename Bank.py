import streamlit as st
import pandas as pd
import numpy as np

st.title("Bank App")

class BankApp:
    def __init__(self, pin="1234"):
        self.balance = 0
        self.pin = pin
    def deposit(self):
        st.header("Deposit Money")

        amount = st.number_input("Enter deposit amount (₦):", min_value=0 )
        account_no = st.text_input("Enter your account number:") 

        if st.button("Deposit"):
            if amount <= 0:
                st.warning("please enter a valid amount")
            else:
                self.balance += amount
                st.success(f"₦{amount} deposited successfuly into account{account_no}")
                st.info(f"Current Balance: {self.balance}")

    def transfer(self):
        st.header("Transfer Money")


        bank = st.text_input("Enter bank name:")
        account_no = st.text_input("Enter the receipent account number:")
        amount = st.number_input("Enter transfer amount (₦):", min_value=0)
        if st.button("transfer"):
           if amount > self.balance:
            st.error("Insufficient fund")
        elif amount < 100:
            st.warning("Minimum transfer is ₦100.")
        elif pin != self.pin:
            st.error("Incorrecr PIN")
        else:
            self.balance += amount
            st.success(f"₦{amount} transfered successfully into account {account_no}")
            st.info(f"New balance:{self.balance}")
        
        
    def airtime(self):
        st.header("Buy Airtime")

        network = st.text_input("Enter your network:")
        amount = st.number_input("Enter amount(₦):", min_value=0)
        pin = st.number_input("Enter your pin:")
        if self.pin == pin:
            self.balance -= amount
            st.success(f"₦{amount} deducted successfully from account {account_no}")
            st.info(f"New balance: {self.balance}")
          
    def check_balance(self):
        st.header("Account Balance")
        st.info(f"Your account balnce is: ₦{self.balance}")

    def logout(self):
        st.info(f"You have been logout. Thank you for banking with us!")


st.title("Bank.py")

if "app" not in st.session_state:
    st.session_state.app = BankApp()

option = st.sidebar.selectbox("choose an option:", ["Deposit", "Transfer", "Airtime", "Check Balance", "Logout"])
if option == "Deposit":
    st.session_state.app.deposit()
elif option == "Transfer":
    st.session_state.app.transfer()
elif option == "Airtime":
    st.session_state.app.airtime()
elif option == "Check Balance":
    st.session_state.app.check_balance()
elif option == "Logout":
    st.session_state.app.logout()

        

