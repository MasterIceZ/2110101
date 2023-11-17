class Card:
 card_list = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
 suit_list = ["club", "diamond", "heart", "spade"]

 def __init__(self, value, suit):
  self.value = value
  self.suit = suit

 def __str__(self):
  return "({} {})".format(self.value, self.suit)
 
 def get_next(self):
  this_value_index = self.card_list.index(self.value)
  this_suit_index = self.suit_list.index(self.suit)

  this_suit_index += 1
  if this_suit_index == 4:
   this_suit_index = 0
   this_value_index += 1
  if this_value_index == 13:
   this_value_index = 0
  return (self.card_list[this_value_index], self.suit_list[this_suit_index])

 def next1(self):
  return Card(*self.get_next())

 def next2(self):
  self.value, self.suit = self.get_next()

n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].next1())
print("----------")
for i in range(n):
 print(cards[i])
print("----------")
for i in range(n):
 cards[i].next2()
 cards[i].next2()
 print(cards[i])