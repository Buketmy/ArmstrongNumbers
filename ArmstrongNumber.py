number= int(input("Number:"))
str_number = str(number)
number_len:int = len(str_number)
count= 0
for i in range(number_len):
    count += int(str_number[i]) ** number_len
   
if  count == number:
    print("Armstrong Numbers")
        
else:
    print("Not Armstrong Number")
       