class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Begg_for_master_toad")
user_2 = User("002", "Big Chungus")



# Social Media account test
print(f"Your number: {user_1.id}\n"
      f"Name: {user_1.username}\n"
      f"Followers: {user_1.followers}\n"
      f"Following: {user_1.following}\n")

print(f"Your number: {user_2.id}\n"
      f"Name: {user_2.username}\n"
      f"Followers: {user_2.followers}\n"
      f"Following: {user_2.following}\n")
