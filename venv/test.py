print("hello world")
var = "중국 " \
      "한국 "
varSplit = var.split()
print(varSplit[0])

print("-------------------")

string = "123456789"
listString = list(string)
listString[0] = '0'
string = ''.join(listString)
print(string)