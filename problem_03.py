def string_test(a):
    b={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in a:
        if c.isupper():
           b["UPPER_CASE"]+=1
        elif c.islower():
           b["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", a)
    print ("No. of Upper case characters : ", b["UPPER_CASE"])
    print ("No. of Lower case Characters : ", b["LOWER_CASE"])

string_test('The quick Brown Fox')
print(string_test)