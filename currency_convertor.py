def currency_convertor(amount):
 with open('file1') as f:
  lines=f.readlines()
 currency_dic={}
 for line in lines:
     parsed=line.split("\t")
     currency_dic[parsed[0]]=parsed[2]
 print("Enter the currency in wiht you ant to convert: \n")
 [print(item) for item in currency_dic.keys()]
 currency=input("")
 print(f"your amount {amount} is equal to {amount*float(currency_dic[currency])} {currency} ")
    
    
    
    
    
amount=int(input("Enter the amount to convert: "))  
currency_convertor(amount)