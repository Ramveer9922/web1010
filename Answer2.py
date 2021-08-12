import requests
page=int(input("Enter the page Number : "))

if page==1:
     r=requests.get(" https://reqres.in/api/users?page=1")
     data=requests.get("https://reqres.in/api/page=3")
     count=0
     for i in data:
         if id==id:
              count+=1
     print("Total Number of User in page 1 :",count)
     print("\n",r.text)

    
elif page==2:
     r=requests.get(" https://reqres.in/api/users?page=2")
     data=requests.get("https://reqres.in/api/page=3")
     count=0
     for i in data:
         if id==id:
              count+=1
     print("Total Number of User in page 2 :",count)
     print("\n",r.text)
     

elif page==3:
     r=requests.get(" https://reqres.in/api/users?page=3")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 3 :",count)
     print("\n",r.text)


elif page==4:
     r=requests.get(" https://reqres.in/api/users?page=4")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 4 :",count)
     print("\n",r.text)


elif page==5:
     r=requests.get(" https://reqres.in/api/users?page=5")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 5 :",count)
     print("\n",r.text)


elif page==6:
     r=requests.get(" https://reqres.in/api/users?page=6")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 6 :",count)
     print("\n",r.text)


elif page==7:
     r=requests.get(" https://reqres.in/api/users?page=7")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 7 :",count)
     print("\n",r.text)

elif page==8:
     r=requests.get(" https://reqres.in/api/users?page=8")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 8 :",count)
     print("\n",r.text)


elif page==9:
     r=requests.get(" https://reqres.in/api/users?page=9")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 9 :",count)
     print("\n",r.text)  


elif page==10:
     r=requests.get(" https://reqres.in/api/users?page=10")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 10 :",count)
     print("\n",r.text)


elif page==11:
     r=requests.get(" https://reqres.in/api/users?page=11")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 11 :",count)
     print("\n",r.text)  


elif page==12:
     r=requests.get(" https://reqres.in/api/users?page=12")
     count=0
     for i in r:
          if id=="id":
               count+=1
     print("Total Number of User in page 12 :",count) 
     print("\n",r.text)

else:
    print("End page")