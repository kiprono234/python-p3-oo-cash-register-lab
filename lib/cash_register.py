#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0  

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        self.total += price * quantity
        self.last_transaction_amount = price * quantity  

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount) / 100
            total_str = f"{self.total:.2f}".rstrip('0').rstrip('.')
            print(f"After the discount, the total comes to ${total_str}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0 




  
