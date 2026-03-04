accountData = {}
while True:
  print("請選擇操作選項(a 註冊,b 登入,c 退出)?",end=" ")
  enter = input()
  if enter == "a":
    print("\n請輸入帳號 :",end=" ")
    account = input()
    if account in accountData:
      print("帳號已存在，請重新輸入!\n")
      continue
    else:
      print("\n請輸入密碼 :",end=" ")
      password = input()
      print("註冊成功!\n")
      accountData[account] = password
      # print(accountData)
  elif enter == "b":
    print("\n請輸入帳號 :",end=" ")
    account = input()
    print("\n請輸入密碼 :",end=" ")
    password = input()
    if account in accountData and password == accountData[account]:
      print("登入成功!\n")
    else:
      print("帳號或密碼錯誤!\n")
      continue
  elif enter == "c":
    print("退出系統!")
    break
  else:
    print("無效的選項!\n")
    continue