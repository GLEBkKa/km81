print("\\n\n\\\\\n\\n\n",)
import os.path
print(os.path.exists("../main.py"))
file = open("data/kol.txt")
info = file.read()
print(type(info))
print(info)
file.close()