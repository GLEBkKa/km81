file = open("data/info.file.csv")
data = file.read()
result = data.splitlines()
sofia = dict()
keys_str = lines[0].split(",")
value_str = lines[1].split(",")
for i,p in zip(keys_str,value_str) :
    sofia[i] = p


file.close()