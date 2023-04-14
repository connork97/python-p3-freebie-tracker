#!/usr/bin/env python3

# from sqlalchemy import create_engine

from models import Company, Dev, Freebie
import ipdb;

if __name__ == '__main__':
    # engine = create_engine('sqlite:///freebies.db')

    print("Running debug.py...")

    print("--------------------")
    print("--------------------")
    print("--------------------")

    # ----- COMPANY CLASS -----
    print("Running Company Methods:")

    print("--------------------")
    print("--------------------")
    print("--------------------")

    print("Dropping companies table...")
    Company.drop_table()

    print("--------------------")

    print("Creating companies table...")
    Company.create_table()

    print("--------------------")

    print("Creating company instances...")
    mlb = Company.create("MLB", 1905)
    nba = Company.create("NBA", 1969)
    nhl = Company.create("NGL", 1960)
    monsanto = Company.create("Monsanto", 1940)

    print("--------------------")

    print("Updating companies...")
    nhl.name = "NHL"
    nhl.update()

    print("Deleting following companies...")
    monsanto.delete()    

    print("--------------------")

    print("Searching for oldest company...")
    Company.oldest_company()

    print("--------------------")
    print("--------------------")
    print("--------------------")

    print("Running Dev Methods:")

    print("--------------------")
    print("--------------------")
    print("--------------------")

    print("Dropping devs table...")
    Dev.drop_table()

    print("--------------------")

    print("Creating devs table...")
    Dev.create_table()

    print("--------------------")

    print("Saving new devs and saving to database...")
    connor = Dev.create("Connor")
    wally = Dev.create("Bill")
    the_rock = Dev.create("Dwayne")
    bill = Dev.create("Wally")

    print("--------------------")

    print("Updating dev names...")
    wally.name = "Wally"
    wally.update()
    bill.name = "Bill"
    bill.update()
    
    print("--------------------")

    print("Deleting dev rows...")
    the_rock.delete()

    print("--------------------")
    print("--------------------")
    print("--------------------")

    print("Running Freebie Methods:")

    print("--------------------")
    print("--------------------")
    print("--------------------")

    print("Dropping freebies table...")    
    Freebie.drop_table()

    print("--------------------")

    print("Creating freebies table...")
    Freebie.create_table()

    print("--------------------")

    print("Creating and saving freebies...")
    ugly_sweater = Freebie.create("Ugly Sweater", 1, 2, 3)
    mlb_jersey = Freebie.create("Mike Trout jersey", 50, 1, 1)
    basketball = Freebie.create("Basketball", 20, 2, 3)
    hockey_puck = Freebie.create("Hockey Puck", 15, 3, 2)
    sticker = Freebie.create("Sticker", 2, 2, 1)

    print("--------------------")

    print("Updating freebies...")

    mlb_jersey.value = 100
    mlb_jersey.update()

    print("--------------------")

    print("Deleting bad freebies...")
    ugly_sweater.delete()

    print("--------------------")

    print("Finding company related to selected freebie...")
    mlb_jersey_company = mlb_jersey.company()
    basketball_company = basketball.company()
    sticker_company = sticker.company()
    hockey_puck_company = hockey_puck.company()

    print("--------------------")

    print("Finding dev related to selected freebie...")

    mlb_jersey_dev = mlb_jersey.dev()

    ipdb.set_trace()
    
    # print("Dropping companies table...")
    # Company.drop_table()
    
    # print("--------------------")

    # print("Creating companies table...")
    # Company.create_table()
    
    # print("--------------------")
    
    # print("Creating company 'test'...")
    # test = Company.create("test", 2000)
    # print("--------------------")
    # print("Creating company 'test1'...")
    # test1 = Company.create("test1", 2001)
    # print("--------------------")    
    # print("Creating company 'test2'...")
    # test2 = Company.create("test2", 2002)
    # print("--------------------")   
    # print("Creating company 'test3'...")
    # test3 = Company.create("test3", 2003)
    # print("--------------------")
    
    # print("Updating 'test' to 'tester'...")
    # test.name = "tester"
    # test.update()
    
    # print("--------------------")

    # print("Finding company 'test' freebies...")
    # test.freebies()

    # print("--------------------")

    # print("Finding company 'test' devs...")
    # test.devs()

    # print("--------------------")
    
    # print("Deleting 'test2'...")
    # test2.delete()
    
    # print("--------------------")

    # print("Returning oldest company...")
    # Company.oldest_company()



    # DEV CLASS

    # print("Dropping 'devs' table...")
    # Dev.drop_table()

    # print("--------------------")

    # print("Creating 'devs' table...")
    # Dev.create_table()

    # print("--------------------")

    # print("Creating new_dev instance 'connor' and saving to database...")
    # connor = Dev.create("Connor")
    # print("--------------------")
    # print("Creating new_dev instance 'simon' and saving to database...")
    # simon = Dev.create("Simon")
    # print("Creating new_dev instance 'will (be deleted)' and saving to database...")
    # will = Dev.create("Will")
    # print("--------------------")
    # print("Creating new_dev instance 'steve' and saving to database...")
    # steve = Dev.create("Steve")

    # print("--------------------")

    # print("Updated dev 'Steve' to 'Stephen'...")
    # steve.name = "Stephen"
    # steve.update()
    
    # print("--------------------")

    # print("Deleting 'will' from database...")
    # will.delete()


    # # FREEBIES TABLE

    # print("Dropping 'freebies' table...")
    # Freebie.drop_table()

    # print("--------------------")

    # print("Creating 'freebies' table...")
    # Freebie.create_table()

    # print("--------------------")

    # print("Creating Freebie instance 'goodies' and saving to database...")
    # goodies = Freebie.create("goodies", 100.00, 1, 1)
    # print("Creating Freebie instance 'tasty_food' and saving to database...")
    # tasty_food = Freebie.create("tasty food", 14.99, 1, 2)
    # print("Creating Freebie instance 'stickers' and saving to database...")
    # stickers = Freebie.create("stickers", 2.50, 2, 1)
    # print("Creating Freebie instance 'bad_freebie' and saving to database...")
    # bad_freebie = Freebie.create("bad freebie", 0.01, 1, 1)

    # print("--------------------")

    # print("Updating freebies...")
    # print("Original goodies value: ", goodies.value)
    # goodies.value = 1000.00
    # goodies.update()
    # print("Updated goodies value: ", goodies.value)

    # print("--------------------")

    # print("Deleting 'bad_freebie'...")
    # bad_freebie.delete()

