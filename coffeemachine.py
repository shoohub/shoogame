#材料を定義する
ingredient = {"coffee":500, "suger":500, "milk":500}
#print(ingredient["coffee"])

#コーヒーを定義する
coffee_ingredient = {
   "latte": {"coffee":100 ,"suger":50 ,"milk":150 ,"price":250}
   ,"cappuccino": {"coffee":150 ,"suger":50 ,"milk":100 ,"price":200}
   ,"espresso": {"coffee":200 ,"suger":50 ,"milk":50 ,"price":150}
}

#コーヒーの種類を選ばせる
coffee_choice = input("what kind of coffee do you want?latte or cappuccino or espresso :")


#材料足りるかを判断する
def ingredient_compare(coffee_choice):
    #現在の材料状況をプリントする
    print(f"the report of ingredient : coffee is {ingredient['coffee']}, suger is {ingredient['suger']}, milk is {ingredient['milk']}")
    coffee_coffee = coffee_ingredient[coffee_choice]["coffee"]
    coffee_suger = coffee_ingredient[coffee_choice]["suger"]
    coffee_milk = coffee_ingredient[coffee_choice]["milk"]
    if coffee_coffee <= ingredient["coffee"] and coffee_suger <= ingredient["suger"] and coffee_milk <= ingredient["milk"]:
        return True
    else:
        return False
    


#お金足りるかを判断する
def coin_compare(coffee_choice):
    #お金を払う
    coin_5 = int(input("How many 5-yen coins do you have?"))
    coin_10 = int(input("How many 10-yen coins do you have?"))
    coin_100 = int(input("How many 100-yen coins do you have?"))
    user_coin = 5 * coin_5 + 10 * coin_10 + 100 * coin_100
    coffee_coin = coffee_ingredient[coffee_choice]["price"]

    if user_coin >= coffee_coin:
       return True
    else:
       return False       


#お金と原材料を判断し、コーヒーを販売する
def buy_coffee(coffee_choice):
    if ingredient_compare(coffee_choice) and coin_compare(coffee_choice):
        print(f"Here is your {coffee_choice}")
    else:
        print(f"It is {coffee_ingredient[coffee_choice]['price']},You're short on money.")


buy_coffee(coffee_choice)