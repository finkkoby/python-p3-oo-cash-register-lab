#!/usr/bin/env python3

class CashRegister():
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []
  def add_item(self, title, price, quantity=1):
    self.items = self.items + ([title] * quantity)
    self.total += price * quantity
    self.last_transaction = dict(title = title, price = price, quantity = quantity)
  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * (self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  def void_last_transaction(self):
    target = self.last_transaction
    if target["quantity"] > 1:
      for item in self.items:
        if item == target["title"]:
          self.items.remove(item)
      self.total -= (target["quantity"] * target["price"])
    else:
      self.total -= target["price"]
      self.items.pop()