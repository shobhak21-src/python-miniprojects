password=input("enter password")
special_chars="@#$!%*?"

if not (len(password)>8):
    print("invalid password! must contain minimum of 8 characters")
else:
    has_upper=any(char.isupper() for char in password)
    has_lower=any(char.islower()for char in password)
    has_special= any(char in special_chars for char in password)
    has_digit = any(char.isdigit() for char in password)

if has_upper and has_lower and has_digit and has_special:
    print("strong password! all conditions met.")
else:
    print("weak password! please include:")
    if not has_upper:
      print("at least one uppercase letter")
    if not has_lower:
      print("at least one lowercase letter")
    if not has_special:
      print("at least one special character (@#$!%*?)")
    if not has_digit:
      print("at least one digit (0-9)")