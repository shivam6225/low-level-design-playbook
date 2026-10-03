from userSR import User
from userRepoSR import UserRepo

user_obj = User("John", "", "20")
user_repo = UserRepo(user_obj.name, user_obj.email, "")

user_obj.get_user_info()
user_repo.save_to_db(user_obj)