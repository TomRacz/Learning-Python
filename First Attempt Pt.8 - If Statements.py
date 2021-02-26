is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male nor tall")
if is_male and is_tall:
    print("You are a tall man")
elif is_male and not (is_tall):
    print("You are a short guy")
elif not (is_male) and is_tall:
    print("You are a tall lady")
else:
    print("You are either female or short")
