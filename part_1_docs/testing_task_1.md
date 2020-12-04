### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card): # colon sign for else clause is missing, so the subsequent keyword will not catch anything missed by the preceding conditions.  the assignment operator is confused with comparison operator, where the card.value property is not being checked for a value, but rather assigned one before the logic is checked.
    if card.value = 1:
      return True
    else
      return False
   

  dif highest_card(self, card1 card2):  # spelling for function keyword is incorrect, and comma seperating parameter variables is missing.  statement should be indeneted and returning 'card' in the conditional statement, as opposed to the named object instances (card1, card2), would also prevent the test from running properly.
    if card1.value > card2.value:
    return card
  else:
    return card2
  


def cards_total(self, cards): # Function header isn't indented. 'total' variable has no value and needs to return string version of object.
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
