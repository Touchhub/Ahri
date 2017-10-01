import time
user,passwd='alex','abc123'
def auth(auth_type):
	print("auth func:",auth_type)
	def outer_wrapper(func):
            def wrapper(*args,**kwargs):

                print("wrapper func args:",*args,**kwargs)
            username=input("Usesname:").strip()
            password=input("Password:").strip()
            if user==username and passwd==password:
                print("\033[32;1mUser has psss authentication\033[0m")
                res=func(*args,**kwargs) #from home
                print("---after authenticaion")
                return res
            else:
                exit("\033[31;1mInvalid username or password\033[0m")
                return wrapper
            return out_wrapper
def index():
    print("welcome to index page")
def home():
    print("welcome to home page")
def pps():
    print('welcome to pps page')

index()
@auth(auth_type=="local")
home()
@auth
pps()