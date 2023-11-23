from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import quote

from pprint import pprint

DATABASE = "users_schema"


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # self.all_quotes = []

    #! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results:
            one_user = cls(row)
            users.append(one_user)

        return users

    #! CREATE
    @classmethod
    def save(cls, data):
        query = """
                    INSERT INTO users(first_name, last_name, email)
                    VALUES (%(first_name)s,%(last_name)s,%(email)s);
                """

        result = connectToMySQL(DATABASE).query_db(query, data)
        # print(result)
        return result

    #! GET ONE BY ID
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        user = cls(result[0])

        return user

    #! UPDATE

    @classmethod
    def update(cls, data):
        update_query = """  
                            UPDATE users
                            SET first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s
                            WHERE id = %(id)s;

                        """
        result = connectToMySQL(DATABASE).query_db(update_query, data)
        print(f"====>Upadte result: ")
        return result

    #! DELETE
    # TODO

    #! Get One User with quotes
    # get one user with their quote
    @classmethod
    def one_user_quotes(cls, data):
        query = """
                    SELECT * from users
                    JOIN quotes
                    ON quotes.user_id = users.id
                    WHERE users.id = %(id)s;
                """

        results = connectToMySQL(DATABASE).query_db(query, data)
        this_user = cls(results[0])
        quotes = []
        for row in results:
            #! format the data here for the quote
            #! preapre the dict for the quote constructor

            quote_dict = {
                "id": row["quotes.id"],
                "quote_body": row["quote_body"],
                "created_at": row["quotes.created_at"],
                "updated_at": row["quotes.updated_at"],
                "user_id": row["user_id"],
            }
            #! now we need to import our Quote model to init it
            this_quote = quote.Quote(quote_dict)

            quotes.append(this_quote)

        this_user.all_quotes = quotes

        return this_user
