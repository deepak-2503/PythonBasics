# A spam comment is defined as a text containing following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams
text = input("Enter or paste message which you want to know is scam or not: ").lower()
if("make a lot of money" in text or "buy now" in text or "subscribe this" in text or "click this" in text):
    print("This is spam 🚫 comment")
else:
    print("✅ This is safe comment")    
    
