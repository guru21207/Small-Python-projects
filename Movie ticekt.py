Default=200
Gender=input("Enter your gender(M/F): ").upper()
num=int(input("Enter the number of tickets: "))
if(Gender=="M"):
    print(f"Ticket price:{Default*num}")
elif(Gender=="F"):
    print(f"Ticket price:{(Default-50)*num}")
else:
    print(f"Your Input {Gender} is invalid")
