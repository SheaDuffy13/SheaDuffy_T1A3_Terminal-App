import pytest
# from passwordWordList import wordList

# def test_passwordGenerator():
#     newPassword = passwordGenerator()
#     passwordContainsRandomWords = False

#     for word in wordList:
#         if word in newPassword:
#             passwordContainsRandomWords = True
    
#     assert passwordContainsRandomWords == True
#--------------------------------------------------------

# from SomeOtherFile import addNum
# The above would import a function like this: 
# def addNum(num1, num2):
#   return num1 + num2
#
# def test_ExampleThrowingError():
#     result = addNum(1,1)
#     assert result == 2
#--------------------------------------------------------


# class Food:
#     def __init__(self, name, isHealthy):
#         self.name = name
#         self.isHealthy = isHealthy

# testFoodData = [
#     {'name':'Apple', 'isHealthy':True},
#     {'name':'Gummy Snake', 'isHealthy':False}
# ]

# @pytest.mark.parametrize('foodData',testFoodData)
# def test_FoodCreation(foodData):
#     newFood = Food(foodData.get('name'), foodData.get('isHealthy'))
#     assert newFood.name != ''
#     assert newFood.isHealthy == True or newFood.isHealthy == False
#--------------------------------------------------------
def test_WillFail():
    assert "hello" == "world"

def test_WillPass():
    assert "hello" == "hello"

test_WillFail()
test_WillPass()
#--------------------------------------------------------
from classes import randloot
def test_randloot():
    randlootSet = randloot()
    assert randlootSet in chest_items

from classes import loot
def test_loot():
    pass
