import Login
# import Registration

print("""1 - Login
2 - Registration""")
choice = input()

if choice == "1"\
    or choice == "Login"\
    or choice == "login":
  Login.doLogin()
elif choice == "2"\
    or choice == "Registration"\
    or choice == "registration":
  # doRegistration()
  pass
else:
  print("incorrect input")