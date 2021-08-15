import requests
page=int(input("Enter the page Number : "))

if page==1:
     r=requests.get(" https://reqres.in/api/users?page=1")
     data=r.json()
     print("\n",data["data"])

    
elif page==2:
     r=requests.get(" https://reqres.in/api/users?page=2")
     data=requests.get("https://reqres.in/api/page=3")
     data=r.json()
     print("\n",data["data"])
     

elif page==3:
     r=requests.get(" https://reqres.in/api/users?page=3")
     data=r.json()
     print("\n",data["data"])


elif page==4:
     r=requests.get(" https://reqres.in/api/users?page=4")
     data=r.json()
     print("\n",data["data"])


elif page==5:
     r=requests.get(" https://reqres.in/api/users?page=5")
     data=r.json()
     print("\n",data["data"])


elif page==6:
     r=requests.get(" https://reqres.in/api/users?page=6")
     data=r.json()
     print("\n",data["data"])


elif page==7:
     r=requests.get(" https://reqres.in/api/users?page=7")
     data=r.json()
     print("\n",data["data"])

elif page==8:
     r=requests.get(" https://reqres.in/api/users?page=8")
     data=r.json()
     print("\n",data["data"])


elif page==9:
     r=requests.get(" https://reqres.in/api/users?page=9")
     data=r.json()
     print("\n",data["data"])


elif page==10:
     r=requests.get(" https://reqres.in/api/users?page=10")
     data=r.json()
     print("\n",data["data"])


elif page==11:
     r=requests.get(" https://reqres.in/api/users?page=11")
     data=r.json()
     print("\n",data["data"]) 


elif page==12:
     r=requests.get(" https://reqres.in/api/users?page=12")
     data=r.json()
     print("\n",data["data"])

else:
    print("End page")