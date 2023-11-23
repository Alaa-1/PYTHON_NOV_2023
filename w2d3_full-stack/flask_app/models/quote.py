from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models import user

DATABASE = "users_schema"


class Quote:
    def __init__(self, data):
        self.id = data["id"]
        self.quote_body = data["quote_body"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    # C R U D
    # * CREATE A QUOTE
    @classmethod
    def create_quote(cls, data):
        query = """
                    INSERT INTO quotes (quote_body, user_id)
                    VALUES(%(quote_body)s, %(user_id)s);
                """

        result = connectToMySQL(DATABASE).query_db(query, data)

        print(result)
