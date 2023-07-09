#Class Pattern
class User:
    def __init__(self,username,type):
        self.username=username
        self.type=type

login=User("kong","manager")

match login:
    case User(username="admin",type="admin"):
        print("สวัสดีผู้ดูแลระบบ")
    case User(type="member"):
        print(f"สวัสดีสมาชิก : {login.username}")
    case User():
        print("ไม่มีข้อมูลในระบบ")