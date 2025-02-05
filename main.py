import string 
import random 
if __name__ == "__main__":
    s1=string.ascii_lowercase 
    s2=string.ascii_uppercase
    print(s1,s2)
    s3=string.digits
    print(s3)
    lst=[]
    lst.append(s1)
    lst.append(s2)
    lst.append(s3)
    pas= " ".join(lst)
 
    ip=int(input("Enter the lenth of password you want: "))
    password=""
    for i in range(ip):
        
        #for j in range(ip):
         
        password=password+random.choice(pas)
    print(f"your automatically genrated password is {password}")
    