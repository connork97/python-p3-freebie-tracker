# lib/models.py

# ! Class.class_method
# ! Class#instance_method

# Relationships:
#   Company has_many Freebies
#   Company has_many Devs through Freebies

#   Dev has_many Freebies
#   Dev has_many Companies through Freebies

#   Freebie belongs_to Company
#   Freebie belongs_to Dev

# Therefore there is a Many to Many Relationship
#   between the Company and Dev

import sqlite3

CONN = sqlite3.connect('./freebies.db')
CURSOR = CONN.cursor()


class Company():

    def __init__(self, name, founding_year, id=None):
        self.name = name
        self.founding_year = founding_year
        self.id = id

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and len(name) > 0:
            self._name = name
        else:
            print("Improper name...")
            raise Exception()
        
    def get_founding_year(self):
        return self._founding_year
    
    def set_founding_year(self, founding_year):
        if founding_year > 0:
            self._founding_year = founding_year
        else:
            print("Improper founding year...")
            raise Exception()
        
    # def get_id(self):
    #     return self.id
    
    # def set_id(self, id):
    #     if id > 0:
    #         self._id = id
    #     else:
    #         print("Improper ID...")
    #         raise Exception()
        
    # id = property(get_id, set_id)
    
    name = property(get_name, set_name)
    founding_year = property(get_founding_year, set_founding_year)

    # ? ORM Table Methods
    @classmethod
    def create_table(cls):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY,
                name TEXT,
                founding_year INTEGER
            )
        """
        companies_table = CURSOR.execute(create_table_sql)
        print("companies table: ==> ", companies_table)

    @classmethod
    def drop_table(cls):
        drop_table_sql = """
            DROP TABLE IF EXISTS companies
        """
        dropped_companies_table = CURSOR.execute(drop_table_sql)
        print("Dropped companies table: ==> ", dropped_companies_table)

    @classmethod
    def new_from_companies_db(cls, row):
        company_inst = cls(name=row[1], founding_year=row[2], id=row[0])
        print(f"Selected company instance is {company_inst.name} ==> {company_inst}")
        return company_inst

    def save(self):
        save_company_sql = """
            INSERT INTO companies (name, founding_year)
            VALUES(?, ?)
        """
        saved_company = CURSOR.execute(save_company_sql, (self.name, self.founding_year))
        CONN.commit()
        self.id = CURSOR.lastrowid

        print(f"{self.name} row ==> ", saved_company)

    @classmethod
    def create(cls, name, founding_year, id=None):
        new_company_inst = cls(name, founding_year, id)
        new_company_inst.save()
        print(f"{name} instance ==>", new_company_inst)
        return new_company_inst

    # ? Optional Useful Methods
    def update(self):
        update_company_sql = """
            UPDATE companies
            SET name = ?,
                founding_year = ?
            WHERE id = ?
        """
        updated_company = CURSOR.execute(update_company_sql, (self.name, self.founding_year, self.id))
        CONN.commit()
        print("Updated company: ==> ", updated_company)

    def delete(self):
        delete_company_sql = """
            DELETE FROM companies
            WHERE id = ?
        """
        deleted_company = CURSOR.execute(delete_company_sql, (self.id,))
        CONN.commit()

        print(f"{self.name} has been deleted ==>", deleted_company)

    # ? Relationship Methods
    def freebies(self):
        # Returns all the FREEBIE Instances associated with THIS Company
        pass

    def devs(self):
        # Returns all the DEV Instances associated with THIS Company
        pass

    # ? Aggregate Methods
    def give_freebie(self, dev, item_name, value):
        pass

    @classmethod
    def oldest_company(cls):
        # Returns the COMPANY Instance of the oldest company
        # ! Should not use any python searching, it will all be done in SQL
        oldest_company_sql = """
            SELECT * FROM companies
            ORDER BY founding_year
            LIMIT 1
        """
        oldest_company_row = CURSOR.execute(oldest_company_sql).fetchone()
        print(f"The oldest company is ==> {oldest_company_row}")
        return cls.new_from_companies_db(oldest_company_row)

# ! ================================


class Dev():

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and len(name) > 0:
            self._name = name
        else:
            raise Exception("Improper name...")

    name = property(get_name, set_name)


    # ? ORM Table Methods
    @classmethod
    def create_table(cls):
        create_devs_sql = """
            CREATE TABLE IF NOT EXISTS devs (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        devs_table = CURSOR.execute(create_devs_sql)
        print("Devs table ==>", devs_table)

    @classmethod
    def drop_table(cls):
        drop_devs_sql = """
            DROP TABLE IF EXISTS devs
        """
        dropped_devs_table = CURSOR.execute(drop_devs_sql)
        print("Dropped devs table ==>", dropped_devs_table)

    @classmethod
    def new_from_devs_db(cls, row):
        dev_inst = cls(name=row[1], id=row[0])
        print(f"Selected company instance is {dev_inst.name} ==> {dev_inst}")
        return dev_inst

    def save(self):
        save_dev_sql = """
            INSERT INTO devs (name)
            VALUES (?)
        """
        saved_dev = CURSOR.execute(save_dev_sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid

        print(f"Saved dev {self.name} ==> {saved_dev}")
        print("SELF.ID", self.id)

    @classmethod
    def create(cls, name, id=None):
        new_dev_inst = cls(name, id)
        new_dev_inst.save()
        print("New dev instance ==>", new_dev_inst)
        return new_dev_inst

    # ? Optional Useful Methods
    def update(self):
        update_dev_sql = """
            UPDATE devs
            SET name = ?
            WHERE id = ?
        """
        updated_dev = CURSOR.execute(update_dev_sql, (self.name, self.id))
        CONN.commit()
        print(f"{self.name} has been updated. ==> {updated_dev}")

    def delete(self):
        delete_dev_sql = """
            DELETE FROM devs
            WHERE id = ?
        """
        deleted_dev = CURSOR.execute(delete_dev_sql, (self.id,))
        CONN.commit()
        print(f"{self.name} has been deleted ==> {deleted_dev}")

    # ? Relationship Methods
    def companies(self):
        pass

    def freebies(self):
        pass

    # ? Aggregate Methods
    def recieved_one(self, item_name):
        # Returns a BOOLEAN of whether or not THIS Dev has recieved
        pass

    def give_away(self, other_dev, freebie):
        # Gives this Freebie instance to other_dev
        #
        pass

# ! ================================


class Freebie():

    # initializes with a: item_name, value, both belongs_to associations, id of None on init
    def __init__(self, item_name, value, company_id, dev_id, id=None):
        self.item_name = item_name
        self.value = value
        self.company_id = company_id
        self.dev_id = dev_id
        self.id = id

    def get_item_name(self):
        return self._item_name
    
    def set_item_name(self, item_name):
        if type(item_name) == str and len(item_name) > 0:
            self._item_name = item_name
        else:
            raise Exception("Improper item_name for freebie.")
        

    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if value > 0:
            self._value = value
        else:
            raise Exception("Improper value for freebie.")

    item_name = property(get_item_name, set_item_name)
    value = property(get_value, set_value)
        

    # ? ORM Table Methods
    @classmethod
    def create_table(cls):
        create_freebies_sql = """
            CREATE TABLE IF NOT EXISTS freebies (
                id INTEGER PRIMARY KEY,
                item_name TEXT,
                value INTEGER,
                company_id INTEGER,
                dev_id INTEGER
            )
        """
        created_freebies_table = CURSOR.execute(create_freebies_sql)
        print(f"freebies table created ==> {created_freebies_table}")

    @classmethod
    def drop_table(cls):
        drop_freebies_sql = """
            DROP TABLE IF EXISTS freebies
        """
        dropped_freebie_table = CURSOR.execute(drop_freebies_sql)
        print(f"Freebies table dropped ==> {dropped_freebie_table}")

    @classmethod
    def new_from_freebies_db(cls, row):
        freebie_inst = cls(item_name=row[1], value=row[2], company_id=row[3], dev_id=row[4], id=row[0])
        print(f"Selected company instance is {freebie_inst.item_name} ==> {freebie_inst}")
        return freebie_inst

    def save(self):
        save_freebie_row_sql = """
            INSERT INTO freebies (item_name, value, company_id, dev_id)
            VALUES (?, ?, ?, ?)
        """
        saved_freebie = CURSOR.execute(save_freebie_row_sql, (self.item_name, self.value, self.company_id, self.dev_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        print(f"Saved {self.item_name} freebie ==> {saved_freebie}")

    @classmethod
    def create(cls, item_name, value, company_id, dev_id):
        new_freebie_inst = cls(item_name, value, company_id, dev_id)
        new_freebie_inst.save()
        return new_freebie_inst

    # ? Optional Useful Methods
    def update(self):
        update_freebie_sql = """
            UPDATE freebies
            SET item_name = ?,
                value = ?,
                company_id = ?,
                dev_id = ?
            WHERE id = ?
        """
        updated_freebie = CURSOR.execute(update_freebie_sql, (self.item_name, self.value, self.company_id, self.dev_id, self.id))
        CONN.commit()
        print(f"{self.item_name} freebie row has been updated ==> {updated_freebie}")

    def delete(self):
        delete_freebie_sql = """
            DELETE FROM freebies
            WHERE id = ?
        """
        deleted_freebie = CURSOR.execute(delete_freebie_sql, (self.id,))
        CONN.commit()
        print(f"{self.item_name} freebie has been deleted ==> {deleted_freebie}")


    # ? Relationship Methods
    def company(self):
        freebie_company_sql = """
            SELECT * FROM companies
            WHERE id = ?
            LIMIT 1
        """
        related_company = CURSOR.execute(freebie_company_sql, (self.company_id,)).fetchone()
        related_comp_inst = Company.new_from_companies_db(related_company)
        print(f"{related_comp_inst.name} instance ==> {related_comp_inst}")
        return related_comp_inst


    def dev(self):
        freebie_dev_sql = """
            SELECT * FROM devs
            WHERE id = ?
            LIMIT 1
        """
        related_dev = CURSOR.execute(freebie_dev_sql, (self.dev_id,)).fetchone()
        related_dev_inst = Dev.new_from_devs_db(related_dev)
        print(f"{related_dev_inst.name} instance ==> {related_dev_inst}")
        return related_dev_inst

    def print_details(self):
        # Returns a String formatted like:
        #   {dev name} owns a {freebie item_name} from {company name}
        print(Freebie.dev.name)
        pass




























































# # lib/models.py

# # ! Class.class_method
# # ! Class#instance_method

# # Relationships:
# #   Company has_many Freebies
# #   Company has_many Devs through Freebies

# #   Dev has_many Freebies
# #   Dev has_many Companies through Freebies

# #   Freebie belongs_to Company
# #   Freebie belongs_to Dev

# # Therefore there is a Many to Many Relationship
# #   between the Company and Dev

# import sqlite3

# CONN = sqlite3.connect('./freebies.db')
# CURSOR = CONN.cursor()


# class Company():

#     def __init__(self, name, founding_year, id=None):
#         self.name = name
#         self.founding_year = founding_year
#         self.id = id

#     # ? ORM Table Methods
#     @classmethod
#     def create_table(cls):
#         create_sql = """
#             CREATE TABLE IF NOT EXISTS companies (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 founding_year INTEGER
#             )
#         """
#         companies_table = CURSOR.execute(create_sql)
#         CONN.commit()

#         print(companies_table)
#         return companies_table

#     @classmethod
#     def drop_table(cls):
#         drop_sql = """
#             DROP TABLE IF EXISTS companies
#         """
#         dropped_companies_table = CURSOR.execute(drop_sql)
#         CONN.commit()

#         print(dropped_companies_table)
#         return dropped_companies_table

#     def save(self):
#         save_sql = """
#             INSERT INTO companies (name, founding_year)
#             VALUES (?, ?)
#         """
#         CURSOR.execute(save_sql, (self.name, self.founding_year))
#         CONN.commit()

#         self.id = CURSOR.lastrowid

#     @classmethod
#     def create(cls, name, founding_year, id=None):
#         new_company = cls(name, founding_year, id)
#         new_company.save()

#         print(new_company)
#         return new_company


#     # ? Optional Useful Methods
#     def update(self):
#         update_sql = """
#             UPDATE companies
#             SET name = ?,
#                 founding_year = ?
#             WHERE id = ?
#         """
#         updated_company = CURSOR.execute(update_sql, (self.name, self.founding_year, self.id))
#         CONN.commit()
#         print(updated_company)
#         return updated_company


#     def delete(self):
#         delete_sql = """
#             DELETE FROM companies
#             WHERE id = ?
#         """
#         deleted_row = CURSOR.execute(delete_sql, (self.id,))
#         CONN.commit()
#         print(deleted_row)
#         return deleted_row

#     # ? Relationship Methods
#     def freebies(self):
#         # Returns all the FREEBIE Instances associated with THIS Company
#         company_freebies_sql = """
#             SELECT * FROM freebies
#             WHERE company_id = ?
#         """
#         company_freebies = CURSOR.execute(company_freebies_sql, (self.id, )).fetchall()
        
#         print(company_freebies)
#         return company_freebies
        

#     def devs(self):
#         # Returns all the DEV Instances associated with THIS Company

#         company_devs_sql = """
#             SELECT devs.id, devs.name FROM devs
#             JOIN freebies
#             ON devs.id = freebies.dev_id
#             WHERE (freebies.company_id) = (?)
#         """

#         company_devs = CURSOR.execute(company_devs_sql, (self.id, ))
#         print(company_devs)
#         for dev in company_devs:
#             print(dev)


#     # ? Aggregate Methods
#     def give_freebie(self, dev, item_name, value):
#         pass

#     @classmethod
#     def oldest_company(cls):
#         # Returns the COMPANY Instance of the oldest company
#         # ! Should not use any python searching, it will all be done in SQL
#         oldest_comp_sql = """
#             SELECT * FROM companies
#             ORDER BY founding_year DESC
#             LIMIT 1
#         """

#         oldest_company = CURSOR.execute(oldest_comp_sql).fetchone()
#         print(oldest_company)
#         return oldest_company
    


# # ! ================================


# class Dev():

#     def __init__(self, name, id=None):
#         self.name = name
#         self.id = id

#     # ? ORM Table Methods
#     @classmethod
#     def create_table(cls):
#         create_sql = """
#             CREATE TABLE IF NOT EXISTS devs (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT
#             )
#         """
#         devs_table = CURSOR.execute(create_sql)
#         CONN.commit()
#         print(devs_table)
#         return devs_table

#     @classmethod
#     def drop_table(cls):
#         drop_sql = """
#             DROP TABLE IF EXISTS devs
#         """
#         dropped_devs_table = CURSOR.execute(drop_sql)
#         CONN.commit()
#         print(dropped_devs_table)
#         return dropped_devs_table

#     def save(self):
#         save_sql = """
#             INSERT INTO devs (name)
#             VALUES (?)
#         """
#         new_dev = CURSOR.execute(save_sql, (self.name,))
#         CONN.commit()
#         self.id = CURSOR.lastrowid

#         # print(new_dev)
#         return new_dev

#     @classmethod
#     def create(cls, name, id=None):
#         new_dev_inst = cls(name, id)
#         new_dev_inst.save()

#         print(new_dev_inst)
#         return new_dev_inst

#     # ? Optional Useful Methods
#     def update(self):
#         update_sql = """
#             UPDATE devs
#             SET name = ?
#             WHERE id = ?
#         """
#         updated_dev = CURSOR.execute(update_sql, (self.name, self.id))
#         CONN.commit()

#         print(updated_dev)
#         return updated_dev

#     def delete(self):
#         delete_sql = """
#             DELETE FROM devs
#             WHERE id = ?
#         """
#         deleted_dev = CURSOR.execute(delete_sql, (self.id,))
#         CONN.commit()

#         print(deleted_dev)
#         return deleted_dev

#     # ? Relationship Methods
#     def companies(self):
#         pass

#     def freebies(self):
#         pass

#     # ? Aggregate Methods
#     def recieved_one(self, item_name):
#         # Returns a BOOLEAN of whether or not THIS Dev has recieved
#         pass

#     def give_away(self, other_dev, freebie):
#         # Gives this Freebie instance to other_dev
#         #
#         pass

# # ! ================================


# class Freebie():

#     # initializes with a: item_name, value, both belongs_to associations, id of None on init
#     def __init__(self, name, value, company_id, dev_id, id=None):
#         self.name = name
#         self.value = value
#         self.company_id = company_id
#         self.dev_id = dev_id
#         self.id = id

#     # ? ORM Table Methods
#     @classmethod
#     def create_table(cls):
#         create_sql = """
#             CREATE TABLE IF NOT EXISTS freebies (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 value REAL,
#                 company_id INTEGER,
#                 dev_id INTEGER
#             )
#         """
#         freebies_table = CURSOR.execute(create_sql)
#         CONN.commit()

#         print(freebies_table)
#         return freebies_table

#     @classmethod
#     def drop_table(cls):
#         drop_sql = """
#             DROP TABLE IF EXISTS freebies
#         """
#         dropped_table = CURSOR.execute(drop_sql)
#         CONN.commit()

#         print(dropped_table)
#         return dropped_table

#     def save(self):
#         save_sql = """
#             INSERT INTO freebies (name, value, company_id, dev_id)
#             VALUES (?, ?, ?, ?)
#         """
#         new_freebie_inst = CURSOR.execute(save_sql, (self.name, self.value, self.company_id, self.dev_id))
#         CONN.commit()
#         self.id = CURSOR.lastrowid

#         print(new_freebie_inst)
#         return new_freebie_inst

#     @classmethod
#     def create(cls, name, value, company_id, dev_id, id=None):
#         new_freebie_inst = cls(name, value, company_id, dev_id, id)
#         new_freebie_inst.save()

#         print(new_freebie_inst)
#         return new_freebie_inst

#     # ? Optional Useful Methods
#     def update(self):
#         update_sql = """
#             UPDATE freebies
#             SET name = ?,
#                 value = ?,
#                 company_id = ?,
#                 dev_id = ?
#             WHERE id = ?
#         """
#         updated_freebie = CURSOR.execute(update_sql, (self.name, self.value, self.company_id, self.dev_id, self.id))
#         CONN.commit()

#         print(updated_freebie)
#         return updated_freebie


#     def delete(self):
#         delete_sql = """
#             DELETE FROM freebies
#             WHERE id = ?
#         """
#         deleted_freebie = CURSOR.execute(delete_sql, (self.id,))
#         CONN.commit()

#         print(deleted_freebie)
#         return deleted_freebie

#     # ? Relationship Methods
#     def company(self):
#         pass

#     def dev(self):
#         pass

#     def print_details(self):
#         # Returns a String formatted like:
#         #   {dev name} owns a {freebie item_name} from {company name}
#         pass