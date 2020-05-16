import sqlite3
conn = sqlite3.connect('example120.db')
c = conn.cursor()
shopping_complete="0"
sql2='''CREATE TABLE complete_database
             (name VARCHAR, qty INTEGER, price INTEGER)'''
c.execute(sql2)

purchase=[( 'milk', '80', '27') ,

  ( 'apple', '45', '60') ,
( 'orange', '80', '60') ,
( 'chicken', '70', '100') ,
( 'onion', '100', '1000') ,
( 'ginger', '45', '40') ,
( 'curry Patta', '87', '20') ,
( 'bhindi', '50', '40') ,
( 'carrot', '60', '30') ,
( 'brinjal', '40', '22') ,
( 'papaya', '30', '37') ,
( 'cheese', '60', '70') ,
( 'bread', '90', '35') ,
( 'butter', '50', '40') ,
]
c.executemany('INSERT INTO complete_database VALUES (?,?,?)', purchase)    
while shopping_complete == "0":
    print("press 1 to add item")
    print("press 2 to view cart")
    print("press 3 to complete the bill")
    choice=input("Choose one option ")
    
    
    if choice == "1":
        
        sql1='''CREATE TABLE cart
             (name VARCHAR, qty INTEGER, price INTEGER)'''
        c.execute(sql1)
        complete="0"

        while complete == "0":
            name=input("enter the name of the product")
            qty=input("enter the quantity of the product")
            price=input("enter the price of the product")
            purchases = [(name, qty, price)]
            c.executemany('INSERT INTO cart VALUES (?,?,?)', purchases)
            sql3 = """DELETE FROM complete_database WHERE name = '""" + name + """'"""
            c.execute(sql3)
            a=['chicken', 'mushroom cream sauce', 'pasta', 'fromage blanc', 'herb & pepper', 'tomato sauce', 'olive oil', 'olive oil', 'shrimp', 'spaghetti', 'burgers', 'chocolate', 'burgers', 'tomatoes', 'ground beef', 'chicken', 'nan', 'olive oil', 'olive oil', 'shrimp', 'chocolate', 'chocolate', 'cooking oil', 'eggs', 'eggs', 'nan', 'nan', 'herb & pepper', 'fromage blanc', 'tomatoes', 'spaghetti', 'milk', 'milk', 'milk', 'shrimp', 'olive oil', 'shrimp', 'shrimp', 'tomatoes', 'ground beef', 'tomatoes', 'herb & pepper', 'mineral water', 'herb & pepper', 'spaghetti', 'olive oil', 'soup', 'nan', 'pepper', 'shrimp', 'spaghetti', 'mineral water', 'olive oil', 'shrimp', 'olive oil', 'olive oil', 'soup', 'spaghetti', 'mineral water', 'mineral water', 'olive oil', 'shrimp', 'pancakes', 'olive oil', 'tomatoes', 'spaghetti', 'burgers', 'chocolate', 'turkey', 'tomatoes', 'ground beef', 'nan', 'olive oil', 'olive oil', 'eggs', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'shrimp', 'shrimp', 'chocolate', 'chocolate', 'chocolate', 'shrimp', 'cooking oil', 'eggs', 'eggs', 'eggs', 'herb & pepper', 'frozen smoothie', 'tomatoes', 'milk', 'milk', 'mineral water', 'spaghetti', 'milk', 'milk', 'milk', 'milk', 'milk', 'milk', 'shrimp', 'shrimp', 'mineral water', 'olive oil', 'shrimp', 'shrimp', 'tomatoes', 'ground beef', 'tomatoes', 'herb & pepper', 'mineral water', 'spaghetti', 'mineral water', 'olive oil', 'soup', 'mineral water', 'pancakes', 'mineral water', 'pepper', 'shrimp', 'spaghetti', 'mineral water', 'mineral water', 'mineral water', 'shrimp', 'olive oil', 'olive oil', 'soup', 'spaghetti', 'mineral water', 'mineral water', 'pancakes', 'olive oil', 'tomatoes', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'shrimp', 'chocolate', 'shrimp', 'eggs', 'spaghetti', 'mineral water', 'spaghetti', 'spaghetti', 'olive oil', 'soup', 'spaghetti', 'shrimp', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti']
            b=['light cream', 'escalope', 'escalope', 'honey', 'ground beef', 'ground beef', 'light cream', 'whole wheat pasta', 'pasta', 'avocado', 'cake', 'burgers', 'turkey', 'cake', 'spaghetti', 'milk', 'chicken', 'chicken', 'spaghetti', 'chocolate', 'herb & pepper', 'soup', 'spaghetti', 'herb & pepper', 'spaghetti', 'mushroom cream sauce', 'pasta', 'french fries', 'nan', 'frozen vegetables', 'frozen vegetables', 'frozen vegetables', 'soup', 'tomatoes', 'mineral water', 'spaghetti', 'spaghetti', 'tomatoes', 'spaghetti', 'spaghetti', 'ground beef', 'milk', 'herb & pepper', 'nan', 'herb & pepper', 'milk', 'milk', 'tomato sauce', 'spaghetti', 'spaghetti', 'tomato sauce', 'spaghetti', 'nan', 'olive oil', 'soup', 'spaghetti', 'tomatoes', 'milk', 'soup', 'whole wheat pasta', 'nan', 'nan', 'olive oil', 'spaghetti', 'spaghetti', 'nan', 'nan', 'burgers', 'burgers', 'nan', 'nan', 'chicken', 'nan', 'spaghetti', 'chocolate', 'mineral water', 'spaghetti', 'milk', 'spaghetti', 'chocolate', 'chocolate', 'herb & pepper', 'nan', 'spaghetti', 'chocolate', 'spaghetti', 'milk', 'herb & pepper', 'spaghetti', 'nan', 'spaghetti', 'nan', 'mineral water', 'spaghetti', 'spaghetti', 'nan', 'olive oil', 'soup', 'spaghetti', 'nan', 'nan', 'tomatoes', 'mineral water', 'mineral water', 'spaghetti', 'spaghetti', 'spaghetti', 'tomatoes', 'spaghetti', 'nan', 'ground beef', 'nan', 'herb & pepper', 'herb & pepper', 'spaghetti', 'nan', 'nan', 'spaghetti', 'mineral water', 'spaghetti', 'spaghetti', 'spaghetti', 'nan', 'spaghetti', 'spaghetti', 'spaghetti', 'olive oil', 'nan', 'spaghetti', 'tomatoes', 'nan', 'nan', 'nan', 'olive oil', 'spaghetti', 'spaghetti', 'eggs', 'mineral water', 'spaghetti', 'mineral water', 'spaghetti', 'chocolate', 'spaghetti', 'chocolate', 'mineral water', 'frozen smoothie', 'ground beef', 'ground beef', 'mineral water', 'mineral water', 'mineral water', 'mineral water', 'spaghetti', 'tomatoes', 'mineral water', 'mineral water', 'pancakes', 'tomatoes', 'mineral water', 'tomatoes']
            for items in range(len(a)):
                
                if a[items]==name:
                    print("suggested dishes " + b[items] )
            import csv
            with open('Market_Basket_Optimisation.csv','a') as newFile:
              newFileWriter = csv.writer(newFile)
              newFileWriter.writerow(name)
            
            complete=input("if completed enter 1")

    if choice == "2":
        for row in c.execute("select * from cart;"):
            print(row[0])
            print(row[1])
            print(row[2])
        delete_choice=input("enter 1 if you want to delete item")
        sql = """DELETE FROM cart WHERE price = """ + delete_choice
        c.execute(sql)
    
    shopping_complete=input("if shopping completed enter 1")
  
   
    
conn.close()
