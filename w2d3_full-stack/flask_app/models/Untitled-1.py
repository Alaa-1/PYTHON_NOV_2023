class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


class Quote:
    def __init__(self, data):
        self.id = data["id"]
        self.quote_body = data["quote_body"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]


one_user_quote = {
    "created_at": "2023, 11, 23, 10, 29, 50",
    "email": "a@a.com",
    "first_name": "Jane",
    "id": 5,
    "last_name": "Kimbel",
    "quote_body": "Don't comment bad code – rewrite it",
    "quotes.created_at": "2023, 11, 23, 10, 32, 29",
    "quotes.id": 1,
    "quotes.updated_at": "2023, 11, 23, 10, 32, 29",
    "updated_at": "2023, 11, 23, 10, 29, 50",
    "user_id": 5,
}

data = {
    "id": one_user_quote["id"],
    "first_name": one_user_quote["first_name"],
    "last_name": one_user_quote["last_name"],
    "email": one_user_quote["email"],
    "created_at": one_user_quote["created_at"],
    "updated_at": one_user_quote["updated_at"],
}

quote_dict = {
    "id": one_user_quote["quotes.id"],
    "quote_body": one_user_quote["quote_body"],
    "created_at": one_user_quote["quotes.created_at"],
    "updated_at": one_user_quote["quotes.updated_at"],
    "user_id": one_user_quote["user_id"],
}

quotes = []
# instances
user1 = User(data)
quote1 = Quote(quote_dict)
quote2 = Quote(quote_dict)
# add the quotes to the list
quotes.append(quote1)
quotes.append(quote2)


user1.all_quotes = quotes

print(user1.all_quotes)
