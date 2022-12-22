import csv
import time
import stdiomask
import pandas as pd
import datetime
import os
item=[]
price=[]
def ciusine(cuisinefile):
    df=pd.read_csv("Menu.csv")
    filename=f"{df['Cuisine'][cuisinefile-1]}.csv"
    df1=pd.read_csv(filename)
    file=open(filename)
    read=csv.reader(file)
    length=len(list(read))
    print(f"||____________________________{df['Cuisine'][cuisinefile-1]}___________________________________||")  
    print("Sr.                           Items                                  Rate  ")
    print("---------------------------------------------------------------------------")
    for i in range(length-1):
        element=f"{i+1}.                           {df1['Items'][i]} {df1['Price'][i]}"
        print(element)
    selectitem=int(input("Enter the serial number agaists the Item You want to Select: "))
    selecteditem=selectitem-1
    item.append(df1['Items'][selecteditem])
    price.append(df1['Price'][selecteditem])
    os.system('cls')
    return bill(cuisinefile)

def menu():
    print("||____________________________Menu______________________________________||\nSr.                           Cuisine                                     \n--------------------------------------------------------------------------\n1.                            Gujarati                                    \n2.                            Punjabi                                     \n3.                            Chinese                                     \n4.                            FastFood                                    \n5.                            Mexican                                     \n6.                            Italian                                     \n7.                            Bevrages                                    \n8.                            Indian Bread                                \n9.                            Rice & Biryani                              \n10.                           Desersts                                    \n____________________________________________________________________________\n")
    sr=int(input("Enter the serial number agaists the Cuisin You want to Select: "))
    os.system('cls')
    return ciusine(sr)

def feedbackform():
    print("___________________________________________________________________________________")
    customername=input("Enter Your Name: ")
    customernumver=int(input("Enter Your Mobile Number: "))
    food=int(input("How was the Food Quality?\n1(Poor)\n2(Okay)\n3(Good)\n4(Very Good)\n5(Excellent)\nYour revview: "))
    sevies=int(input("How was the Service?\n1(Poor)\n2(Okay)\n3(Good)\n4(Very Good)\n5(Excellent)\nYour revview: "))
    ambience=int(input("How is the Ambience?\n1(Poor)\n2(Okay)\n3(Good)\n4(Very Good)\n5(Excellent)\nYour revview: "))
    overall=int(input("How is your overall review?\n1(Poor)\n2(Okay)\n3(Good)\n4(Very Good)\n5(Excellent)\nYour revview: "))
    with open("review.csv","a",newline="") as revenuefile:
        Writer=csv.writer(revenuefile)
        Writer.writerow([customername,customernumver,f"{food}*",f"{sevies}*",f"{ambience}*",f"{overall}*"])
    revenuefile.close()
    os.system('cls')
    return exit("Thankyou for payment and Feedback! Enjoy your rest of the day!\n____________________________________________________________________________\n")

def revenu(exitkey1):
    revenufile=pd.read_csv("revenue.csv")
    revenuefile1=open("revenue.csv")
    readfile=csv.reader(revenuefile1)
    filelength=len(list(readfile))
    print("________________________________________________________________________________________")
    monthreveue=int(input("Enter the month number: "))
    yearrevenue=int(input("Enter the year number: "))
    print("________________________________________________________________________________________")
    print("Date          Time      Amount")
    for i in range(filelength-1):
        if revenufile['Month'][i]==monthreveue and revenufile['Year'][i]==yearrevenue:
            print(f"{revenufile['Date'][i]}  {revenufile['Time'][i]}  {revenufile['Amount'][i]}")
    print("________________________________________________________________________________________\n")
    if exitkey1==1:
        Exit1=input("Press Enter to go back to index:")
        os.system('cls')
        ownerindex()
    elif exitkey1==2:
        Exit1=input("Press Enter to go back to index:")
        os.system('cls')
        managerindex()
    return mymain()

def bill(cuisine_name):
    total1=0
    print("___________________________________________________________________________")
    print("|||________________________________BILL_________________________________|||\n")
    i=0
    n=len(item)
    print("------------------------------------------------")
    print("sr.","  ","Item","                              ","Rs")
    print("------------------------------------------------")
    while i<n: 
        print((i+1),"    ",item[i],"  ",price[i],"Rs")
        i+=1
    print("------------------------------------------------")
    for ele in range(0,len(price)):
        total1=total1 + price[ele]
    total2=total1*0.025
    total=total1+(2*total2)
    print("Bill Amount: ",total1,"Rs")
    print("CGST 2.5%:   ",total2,"Rs")
    print("SGST 2.5%:   ",total2,"Rs")
    print("------------------------------------------------\n")
    print("Total Amount:",total,"Rs")
    print("------------------------------------------------\n")
    print("1. Payment")
    print("2. Select another item from different cuisine")
    print("3. Select another item from same cuisine")
    print("4. Delete all items")
    print("5. Delete last item")
    print("6. cancel order")
    print("____________________________________________________________________________\n")
    sr9=int(input("Select an option: "))
    if sr9==1:
        date=datetime.date.today()
        Time=time.localtime()
        currenttime=time.strftime("%H:%M:%S",Time)
        with open("revenue.csv","a",newline="") as revenuefile:
            Writer=csv.writer(revenuefile)
            Writer.writerow([date,currenttime,total,date.day,date.month,date.year,(2*total2)])
        revenuefile.close()
        os.system('cls')
        print("Do You like to fill feedback form?\n1. Yes\n2. No")
        userchoice=int(input("Enetr your choice: "))
        if userchoice==1:
            os.system('cls')
            print(feedbackform())
        else:
            os.system('cls')
            exit("Thankyou for payment! Enjoy your rest of the day!\n____________________________________________________________________________\n")
    elif sr9==2:
        os.system('cls')
        var9=menu()
    elif sr9==3:
        os.system('cls')
        var9=ciusine(cuisine_name)
    elif sr9==4:
        os.system('cls')
        item.clear()
        price.clear()
        var9=menu()
    elif sr9==5:
        os.system('cls')
        item.pop()
        price.pop()
        var9=bill(cuisine_name)
    elif sr9==6:
        os.system('cls')
        print("Thankyou for visit! Enjoy Rest of Your Day")
        print("____________________________________________________________________________\n")
        var9=mymain()
    else:
        print("Invalid select! Please Try Again.")
        print("____________________________________________________________________________\n")  
        var9=bill()

    return var9

def managerattendence():
    with open("managerattendence.csv","a",newline="") as employfile:
        Writer=csv.writer(employfile)
        attend=input("For present press 'p' anf for absent press 'n'")
        print("____________________________________________________________________________\n")
        date=datetime.date.today()
        if attend=="p":
            Writer.writerow([date,"Present",date.month,date.year])
        elif attend=="n":
            Writer.writerow([date,"Absent",date.month,date.year])
    employfile.close()
    print("____________________________________________________________________________\n")
    print("Attendence marked successfully!")
    Exit2=input("Press Enter to o back to index:")
    os.system('cls')
    return ownerindex()

def jobapplication():
    print("____________________________________________________________________________")
    print("        Welcome to restaurant\n____________________________________________________________________________\nEnter folowwing details For appling for Job:-")
    name=input("Enter Your Name: ")
    qualification=input("Enterr your Qualification: ")
    email=input("Enter email: ")
    jobfor=int(input("1. Senior-Chef\n2. Assistant-Chef\n3. Waiter\n"))
    if jobfor==1:
        jobf="Senior-Chef"
    elif jobfor==2:
        jobf="Assistant-Chef"
    elif jobfor==3:
        jobf="Waiter"
    with open("Job.csv","a",newline="") as revenuefile:
        Writer=csv.writer(revenuefile)
        Writer.writerow([name,qualification,email,jobf])
    revenuefile.close()
    print("You have succesfully applied for job!")
    Exit3=input("Press Enter to Exit:")
    os.system('cls')
    return exit()

def jobapproval():
    jobfile=pd.read_csv("Job.csv")
    jobfile1=open("Job.csv")
    jobread1=csv.reader(jobfile1)
    joblength=len(list(jobread1))
    if joblength>1:
        print("_______________________________________________________________________")
        print("    Name          Applied for")
        print("_______________________________________________________________________")
        for i in range(joblength-1):
            print(f"{i+1}. {jobfile['Name'][i]}   {jobfile['Appling For'][i]}")
        applicantno=int(input("Enter your choice: "))
        print("Applicant's Name: ",jobfile['Name'][applicantno-1])
        print("Qualification: ",jobfile['Qualification'][applicantno-1])
        print("Applied For: ",jobfile['Appling For'][applicantno-1])
        print("Email: ",jobfile['email'][applicantno-1])
        approv=int(input("1. Aprove\n2. Reject\nEnter Your decision: "))
        if approv==1:
            newsalary=int(input("Enter salary of new employee: "))
            newpassword=int(input("Enter password of new employee: "))
            with open("employsalary.csv","a",newline="") as revenuefile:
                Writer=csv.writer(revenuefile)
                Writer.writerow([jobfile['Name'][applicantno-1],jobfile['Appling For'][applicantno-1],newsalary,newpassword])
            revenuefile.close()
            newemployee=f"{jobfile['Name'][applicantno-1]}.csv"
            with open(newemployee,"a",newline="") as newfile1:
                Writer=csv.writer(newfile1)
                Writer.writerow(["Date","Attendence","Month","Year"])
            newfile1.close()
            namenew=['Name']
            qualification=['Qualification']
            applied=['Appling For']
            email=['email']
            for row in range(joblength-1):
                if jobfile['Name'][row]!=jobfile['Name'][applicantno-1]:
                    namenew.append(jobfile['Name'][row])
                    qualification.append(jobfile['Qualification'][row])
                    applied.append(jobfile['Appling For'][row])
                    email.append(jobfile['email'][row])
            with open("Job.csv","w",newline="") as employfile1:
                Writer=csv.writer(employfile1)
                for i in range(len(namenew)):
                    Writer.writerow([namenew[i],qualification[i],applied[i],email[i]])
            print("Approval mail is sended to New employee with His new password!\n\nNew Employeee recordes are logged in the restaurant database!\n_______________________________________________________________________")
        elif approv==2:
            namenew=['Name']
            qualification=['Qualification']
            applied=['Appling For']
            email=['email']
            for row in range(joblength-1):
                if jobfile['Name'][row]!=jobfile['Name'][applicantno-1]:
                    namenew.append(jobfile['Name'][row])
                    qualification.append(jobfile['Qualification'][row])
                    applied.append(jobfile['Appling For'][row])
                    email.append(jobfile['email'][row])
            with open("Job.csv","w",newline="") as employfile1:
                Writer=csv.writer(employfile1)
                for i in range(len(namenew)):
                    Writer.writerow([namenew[i],qualification[i],applied[i],email[i]])
            print("Rejection mail is sended to this applicant!\n_______________________________________________________________________\n")
        nextstep=int(input("1. Check Another Job applications\n2. Back to index\nEnter your choice: "))
        if nextstep==1:
            os.system('cls')
            jobapproval()
        elif nextstep==2:
            os.system('cls')
            ownerindex()
    else:
        print("No new Job applications!")
        print("Press Enter to go back to index:")
        os.system('cls')
        ownerindex()
    return ownerindex()

def salarymanager():
    managersalaryfile=pd.read_csv("managerattendence.csv")
    print("__________________________________________________________________")
    print("Designation:    ","Manager")
    print("Current Salary: ",managersalaryfile['salary'][0])
    print("__________________________________________________________________\n")
    managersalaryfile.loc[0, "salary"]=int(input("Enter New salary: "))
    managersalaryfile.to_csv("managerattendence.csv",index=False)
    Exit4=input("Salary Updated Successfully!\nPressEnter to go back to index:")
    os.system('cls')
    return ownerindex()

def monthlyprofit():
    revenufile=pd.read_csv("revenue.csv")
    expencefile=pd.read_csv("expence.csv")
    managerfile=pd.read_csv("managerattendence.csv")
    employfile=pd.read_csv("employsalary.csv")
    employeesalary=0
    employfile1=open("employsalary.csv")
    employread1=csv.reader(employfile1)
    employlength1=len(list(employread1))
    for i in range(employlength1-1):
        employeesalary+=employfile['Salary'][i]
    managersal=managerfile['salary'][0]
    querymonth=int(input("Enter the month: "))
    queryyear=int(input("Enter the year: "))
    expencefile1=open("expence.csv")
    expenceread1=csv.reader(expencefile1)
    expencelength1=len(list(expenceread1))
    for j in range(expencelength1-1):
        if expencefile['Month'][j]==querymonth and expencefile['Year'][j]==queryyear:
            maintance=expencefile['Maintance'][j]
            grossary=expencefile['Grossary'][j]
            electricbill=expencefile['Electricity'][j]
            other=expencefile['Extra'][j]
    revenuefile1=open("revenue.csv")
    revenueread1=csv.reader(revenuefile1)
    revenuelength1=len(list(revenueread1))
    income=0
    tax=0
    for k in range(revenuelength1-1):
        if revenufile['Month'][k]==querymonth and revenufile['Year'][k]==queryyear:
            income+=revenufile['Amount'][k]
            tax+=revenufile['Tax'][k]
    print(f"__________________________________________________________________________\nExpence:-\n__________________________________________________________________________\n\nEmployees Salary: {employeesalary}\nManager Salary:   {managersal}\nMaintance:        {maintance}\nGrossaryExpence:  {grossary}\nElectricityBill:  {electricbill}\nTax:              {tax}\nExtraExpences:    {other}\n\n")
    totalexpence=employeesalary+managersal+maintance+grossary+electricbill+other+tax
    print(f"__________________________________________________________________________\nTotal Income:  {income}\nTotal Expence: {totalexpence}\n__________________________________________________________________________\n\nNet Profit:    {income-totalexpence}\n__________________________________________________________________________\n")
    Exit5=input("Press Enter to go back to index:")
    os.system('cls')
    return ownerindex()

def yearlyprofit():
    revenufile=pd.read_csv("revenue.csv")
    expencefile=pd.read_csv("expence.csv")
    managerfile=pd.read_csv("managerattendence.csv")
    employfile=pd.read_csv("employsalary.csv")
    employeesalary=0
    employfile1=open("employsalary.csv")
    employread1=csv.reader(employfile1)
    employlength1=len(list(employread1))
    for i in range(employlength1-1):
        employeesalary+=employfile['Salary'][i]
    managersal=managerfile['salary'][0]
    queryyear=int(input("Enter the year: "))
    expencefile1=open("expence.csv")
    expenceread1=csv.reader(expencefile1)
    expencelength1=len(list(expenceread1))
    maintance,grossary,electricbill,other=0,0,0,0
    for j in range(expencelength1-1):
        if expencefile['Year'][j]==queryyear:
            maintance+=expencefile['Maintance'][j]
            grossary+=expencefile['Grossary'][j]
            electricbill+=expencefile['Electricity'][j]
            other+=expencefile['Extra'][j]
    revenuefile1=open("revenue.csv")
    revenueread1=csv.reader(revenuefile1)
    revenuelength1=len(list(revenueread1))
    income=0
    tax=0
    for k in range(revenuelength1-1):
        if revenufile['Year'][k]==queryyear:
            income+=revenufile['Amount'][k]
            tax+=revenufile['Tax'][k]
    print(f"__________________________________________________________________________\nExpence:-\n__________________________________________________________________________\n\nEmployees Salary: {employeesalary*12}\nManager Salary:   {managersal*12}\nMaintance:        {maintance}\nGrossaryExpence:  {grossary}\nElectricityBill:  {electricbill}\nTax:              {tax}\nExtraExpences:    {other}\n\n")
    totalexpence=(employeesalary*12)+(managersal*12)+maintance+grossary+electricbill+other+tax
    print(f"__________________________________________________________________________\nTotal Income:  {income}\nTotal Expence: {totalexpence}\n__________________________________________________________________________\n\nNet Profit:    {income-totalexpence}\n__________________________________________________________________________\n")
    Exit6=input("Press Enter to go back to index:")
    os.system('cls')
    return ownerindex()

def attendence():
    df2=pd.read_csv("employsalary.csv")
    file1=open("employsalary.csv")
    read1=csv.reader(file1)
    length1=len(list(read1))
    print("____________________________________________________________________________")
    for i in range(length1-1):
        element=f"{i+1}. {df2['Name'][i]}"
        print(element)
    print(f"{length1}. Index")
    print(f"{length1+1}. Exit")
    print("____________________________________________________________________________\n")
    employenumber=int(input("Select one whoes attendence you want to fill: "))
    print("____________________________________________________________________________\n")
    if employenumber<length1:
        employfilename=f"{df2['Name'][employenumber-1]}.csv"
        with open(employfilename,"a",newline="") as employfile:
            Writer=csv.writer(employfile)
            attend=input("For present press 'p' anf for absent press 'n'")
            print("____________________________________________________________________________\n")
            date=datetime.date.today()
            if attend=="p":
                Writer.writerow([date,"Present",date.month,date.year])
            elif attend=="n":
                Writer.writerow([date,"Absent",date.month,date.year])
        employfile.close()
        print("____________________________________________________________________________\n")
        print("1. Enter attendence of other employ\n2. Back to index\n3. Exit")
        Mchoice=int(input("Enter Your choice"))
        if Mchoice==1:
            os.system('cls')
            attendence()
        elif Mchoice==2:
            os.system('cls')
            managerindex()
        elif Mchoice==3:
            os.system('cls')
            exit()
    elif employenumber==length1:
        os.system('cls')
        managerindex()
    elif employenumber==(length1+1):
        os.system('cls')
        exit()
    return attendence()

def employsalary():
    salaryfile=pd.read_csv("employsalary.csv")
    salaryfile1=open("employsalary.csv")
    readsalaryfile=csv.reader(salaryfile1)
    salaryfilelength=len(list(readsalaryfile))
    for i in range(salaryfilelength-1):
        print(f"{i+1}. {salaryfile['Name'][i]}({salaryfile['Designation'][i]})")
    print(f"{salaryfilelength}. Back to index")
    print("________________________________________________________________")
    choice1=int(input("Enter the number whose salary you want to change: "))
    print("________________________________________________________________\n")
    if choice1<salaryfilelength:
        print("Name:           ",salaryfile['Name'][choice1-1])
        print("Designation:    ",salaryfile['Designation'][choice1-1])
        print("Current Salary: ",salaryfile['Salary'][choice1-1])
        salaryfile.loc[choice1-1, "Salary"]=int(input("Enter New salary: "))
        salaryfile.to_csv("employsalary.csv",index=False)
        print("________________________________________________________________")
        Exit7=input("Salary Updated Successfully!\nPress Enter to back to index:")
        os.system('cls')
        managerindex()
    else:
        os.system('cls')
        managerindex()

def managersalary():
    print("____________________________________________________________________")
    monthofattendence=int(input("Enter the month: "))
    yearofattendence=int(input("Enter the year: "))
    print("____________________________________________________________________")
    manageratt=pd.read_csv("managerattendence.csv")
    efile=open("managerattendence.csv")
    eread=csv.reader(efile)
    length=len(list(eread))
    msalary=manageratt['salary'][0]
    attend=0
    for i in range(length-1):
        if manageratt['Month'][i]==monthofattendence and manageratt['Year'][i]==yearofattendence:
            if  manageratt['Attendence'][i]=="Absent":
                attend+=1
    print("Your salary is: ",msalary,"Rs")
    print(f"You took {attend} leaves in this month:")
    print("____________________________________________________________________\n\n")
    if attend>2:
        print(f"you took {attend-2} leaves extra")
        print(f"So according to restaurant policy you will be impose penalty of {(attend-2)*(0.02*msalary)}Rs")
        print(f"Salary credited in your account this month is :{msalary-((attend-2)*(0.02*msalary))}")
        Exit8=input("____________________________________________________________________\nPress Enter to go back to index:")
        os.system('cls')
    else:
        print(f"Salary credited in your account this month is :{msalary}")
        Exit8=input("____________________________________________________________________\nPress Enter to go back to index:")
        os.system('cls')
    return managerindex()

def leaveapplication():
    leaveappli=pd.read_csv("leaveapplication.csv")
    lafile=open("leaveapplication.csv")
    laread=csv.reader(lafile)
    lalength=len(list(laread))
    print("_________________________________________________________________________")
    if lalength>1:
        for i in range(lalength-1):
            print(f"{i+1}.  {leaveappli['Name'][i]}")
        applicatnnum=int(input("Enter Your Choice: "))
        print(f"{leaveappli['Name'][applicatnnum-1]} want leave from: {leaveappli['Day'][applicatnnum-1]}-{leaveappli['Month'][applicatnnum-1]}-{leaveappli['Year'][applicatnnum-1]} for {leaveappli['Days'][applicatnnum-1]} days Reason:{leaveappli['Reason'][applicatnnum-1]}")
        print("_________________________________________________________________________")
        approval=int(input("1. Approve\n2. Disapprove\nEnter your choice: "))
        if approval==1:
            with open("leaveapproval.csv","a",newline="") as employleave:
                Writer=csv.writer(employleave)
                Writer.writerow([leaveappli['Name'][applicatnnum-1],leaveappli['Day'][applicatnnum-1],leaveappli['Month'][applicatnnum-1],leaveappli['Year'][applicatnnum-1],leaveappli['Reason'][applicatnnum-1],"Approved"])
            employleave.close()
        elif approval==2:
            with open("leaveapproval.csv","a",newline="") as employleave:
                Writer=csv.writer(employleave)
                Writer.writerow([leaveappli['Name'][applicatnnum-1],leaveappli['Day'][applicatnnum-1],leaveappli['Month'][applicatnnum-1],leaveappli['Year'][applicatnnum-1],leaveappli['Reason'][applicatnnum-1],"Disaproved"])
            employleave.close()
        name=['Name']
        day=['Day']
        month=['Month']
        year=['Year']
        days=['Days']
        reason=['Reason']
        a_file=open("leaveapplication.csv")
        a_read=csv.reader(a_file)
        a_length=len(list(a_read))
        for row in range(a_length-1):
            if leaveappli['Name'][row]!=leaveappli['Name'][applicatnnum-1]:
                name.append(leaveappli['Name'][row])
                day.append(leaveappli['Day'][row])
                month.append(leaveappli['Month'][row])
                year.append(leaveappli['Year'][row])
                days.append(leaveappli['Days'][row])
                reason.append(leaveappli['Reason'][row])
        with open("leaveapplication.csv","w",newline="") as employfile1:
            Writer=csv.writer(employfile1)
            for i in range(len(reason)):
                Writer.writerow([name[i],day[i],month[i],year[i],days[i],reason[i]])
        print("_________________________________________________________________________")
        ret=int(input("1. Check another leave appllication\n2. Back to index\nEnter Your choice: "))
        if ret==1:
            os.system('cls')
            leaveapplication()
        elif ret==2:
            os.system('cls')
            managerindex()
    else:
        print("No applications!")
        Exit9=input("Press Enter to go back to index:")
        os.system('cls')
        managerindex()

def manageratten():
    print("________________________________________________________________")
    month_of_attendence=int(input("Enter the month: "))
    year_of_attendence=int(input("Enter the year: "))
    print("________________________________________________________________")
    employatt=pd.read_csv("managerattendence.csv")
    managerattfile=open("managerattendence.csv")
    mfileread=csv.reader(managerattfile)
    mfilelength=len(list(mfileread))
    print(f"Date       Attendence")
    for i in range(mfilelength-1):
        if employatt['Month'][i]==month_of_attendence and employatt['Year'][i]==year_of_attendence:
            printer=f"{employatt['Date'][i]}  {employatt['Attendence'][i]}"
            print(printer)
    Exit10=input("________________________________________________________________\nPress Enter to go back to index:")
    os.system('cls')
    return managerindex()

def addmonthyexpence():
    print("________________________________________________________________")
    expencemonth=int(input("Enter the month: "))
    expenceyear=int(input("Enter the year: "))
    maintanance=int(input("Enter maintaince: "))
    grossary=int(input("Enter Grossary expences: "))
    electricy=int(input("Enter electricity cost: "))
    other=int(input("Enter Extra Expences: "))
    print("________________________________________________________________")
    with open("expence.csv","a",newline="") as revenuefile:
        Writer=csv.writer(revenuefile)
        Writer.writerow([expencemonth,expenceyear,maintanance,grossary,electricy,other])
    revenuefile.close()
    Exit11=input("Record Saved Successfully!\nPress Enter to go back to index:")
    os.system('cls')
    return managerindex()

def adddish():
    print("________________________________________________________________________Sr.                           Cuisine                                     \n--------------------------------------------------------------------------\n1.                            Gujarati                                    \n2.                            Punjabi                                     \n3.                            Chinese                                     \n4.                            FastFood                                    \n5.                            Mexican                                     \n6.                            Italian                                     \n7.                            Bevrages                                    \n8.                            Indian Bread                                \n9.                            Rice & Biryani                              \n10.                           Desersts                                    \n____________________________________________________________________________\n")
    cuisinename=int(input("Enter the serial number agaists the Cuisin You want to Select: "))
    menu=pd.read_csv("Menu.csv")
    print("________________________________________________________________")
    print("Adding to ",menu['Cuisine'][cuisinename-1])
    print("________________________________________________________________")
    dish=input("Enter name of Dish: ")
    dishprice=int(input("Enter price od dish: "))
    dishlength=len(dish)
    space=(30-dishlength)*" "
    with open(f"{menu['Cuisine'][cuisinename-1]}.csv","a",newline="") as revenuefile:
        Writer=csv.writer(revenuefile)
        Writer.writerow([f"{dish}{space}",dishprice])
    revenuefile.close()
    Exit12=input("________________________________________________________________\nDish added Successfully!\nPress Enter to go back to index:")
    os.system('cls')
    return managerindex()

def reviewfeedback(exitkey2):
    reviewfile=pd.read_csv("review.csv")
    rfile=open("review.csv")
    rread=csv.reader(rfile)
    rlength=len(list(rread))
    print("__________________________________________________________________________________________________________")
    print(f"Customer's Name          Customer's Number  Food Rating  Service Rating  Ambience Rating  Overall Rating")
    for i in range(rlength-1):
        lenthname=len(reviewfile['Customers Name'][i])
        namespace=(25-lenthname)*" "
        print(f"{reviewfile['Customers Name'][i]}{namespace}    {reviewfile['Customers Number'][i]}         {reviewfile['Food Rating'][i]}              {reviewfile['Service Rating'][i]}               {reviewfile['Ambience Rating'][i]}              {reviewfile['Overall Rating'][i]}")
    print("__________________________________________________________________________________________________________")
    if exitkey2==1:
        Exit13=input("Press Enter to go back to index:")
        os.system('cls')
        ownerindex()
    elif exitkey2==2:
        Exit13=input("Press Enter to go back to index:")
        os.system('cls')
        managerindex()
    return mymain()

def employattendence(file_name):
    print("_____________________________________________________________________")
    monthofatten=int(input("Enter the month: "))
    yearofatten=int(input("Enter the year: "))
    employatt=pd.read_csv(f"{file_name}.csv")
    efile=open(f"{file_name}.csv")
    eread=csv.reader(efile)
    length=len(list(eread))
    print("_____________________________________________________________________")
    print(f"Date       Attendence")
    for i in range(length-1):
        if employatt['Month'][i]==monthofatten and employatt['Year'][i]==yearofatten:
            printer=f"{employatt['Date'][i]}  {employatt['Attendence'][i]}"
            print(printer)
    Exit14=input("_____________________________________________________________________\nPress Enter to go back to index:")
    os.system('cls')
    return employindex(file_name)

def esalary(emp_name):
    print("_____________________________________________________________________")
    monthofatten=int(input("Enter the month: "))
    yearofatten=int(input("Enter the year: "))
    print("_____________________________________________________________________")
    employatt=pd.read_csv(f"{emp_name}.csv")
    empsalary=pd.read_csv("employsalary.csv")
    salaryfile2=open("employsalary.csv")
    readsalaryfile2=csv.reader(salaryfile2)
    salaryfilelength2=len(list(readsalaryfile2))
    for i in range(salaryfilelength2-1):
        if empsalary['Name'][i]==emp_name:
            salary=empsalary['Salary'][i]
    efile=open(f"{emp_name}.csv")
    eread=csv.reader(efile)
    length=len(list(eread))
    attend=0
    for i in range(length-1):
        if employatt['Month'][i]==monthofatten and employatt['Year'][i]==yearofatten:
            if  employatt['Attendence'][i]=="Absent":
                attend+=1
    print("_____________________________________________________________________")
    print("Your salary is: ",salary,"Rs")
    print(f"You took {attend} leaves in this month:\n\n")
    if attend>2:
        print(f"you took {attend-2} leaves extra")
        print(f"So according to restaurant policy you will be impose penalty of {(attend-2)*(0.02*salary)}Rs")
        print(f"Salary credited in your account this month is :{salary-((attend-2)*(0.02*salary))}")
        print("_____________________________________________________________________")
    else:
        print(f"Salary credited in your account this month is :{salary}")
        print("_____________________________________________________________________")
    Exit15=input("Press Enter to back to index:")
    os.system('cls')
    return employindex(emp_name)

def leave(empname):
    print("__________________________________________________________________________________")
    print("______________________________Leave Application___________________________________\n")
    leavemonth=int(input("Enter the month of leave: "))
    leaveyear=int(input("Enter the year of leave: "))
    fromdate=int(input("Enter the day from you are on leave: "))
    daysofleave=int(input("Enter days of leave: "))
    leavereason=input("Enter the reason for leave(in one word): ")
    with open("leaveapplication.csv","a",newline="") as employleave:
        Writer=csv.writer(employleave)
        Writer.writerow([empname,fromdate,leavemonth,leaveyear,daysofleave,leavereason])
    employleave.close()
    print("___________________________________________________________________________________\n")
    Exit16=input("Your leave application is submitted successfully!\nYou will recive manager's responce in 1-2 Days\nPress Enter to go back to index:")
    os.system('cls')
    return employindex(empname)

def appleave(nameemp):
    leaveapp=pd.read_csv("leaveapproval.csv")
    afile=open("leaveapproval.csv")
    aread=csv.reader(afile)
    alength=len(list(aread))
    applist=0
    for i in range(alength-1):
        if leaveapp['Name'][i]==nameemp:
            applist+=1
    print("_____________________________________________________________________")
    if applist>0:
        for j in range(alength-1):
            if leaveapp['Name'][j]==nameemp:
                if  leaveapp['Approval'][j]=="Approved":
                    print("Congratulation! your leave has been Aproved")
                    print(f"{leaveapp['Day'][j]}-{leaveapp['Month'][j]}-{leaveapp['Year'][j]}   {leaveapp['Reason'][j]}   {leaveapp['Approval'][j]}\n\n")
                else:
                    print("Sorry! your leave has been Disaproved")
                    print(f"{leaveapp['Day'][j]}-{leaveapp['Month'][j]}-{leaveapp['Year'][j]}   {leaveapp['Reason'][j]}   {leaveapp['Approval'][j]}\n\n")
        print("_____________________________________________________________________")
        Exit17=input("Press Enter to mark Approvals as seen:")
        name=['Name']
        day=['Day']
        month=['Month']
        year=['Year']
        app=['Approval']
        with open("leaveapproval.csv",newline="") as employfile:
            reader1=csv.reader(employfile)
            rd=len(list(reader1))
            for row in range(rd-1):
                if leaveapp['Name'][row]!=nameemp:
                    name.append(leaveapp['Name'][row])
                    day.append(leaveapp['Day'][row])
                    month.append(leaveapp['Month'][row])
                    year.append(leaveapp['Year'][row])
                    app.append(leaveapp['Approval'][row])
        with open("leaveapproval.csv","w",newline="") as employfile1:
            Writer=csv.writer(employfile1)
            for k in range(len(app)):
                Writer.writerow([name[k],day[k],month[k],year[k],app[k]])
    else:
        Exit17=input("You Don't Have any pending aprovals to view!\n_____________________________________________________________________\nPressEnter to go bact to index:")
    os.system('cls')
    return employindex(nameemp)

def ownerindex():
    print("____________________________________________________________________________")
    print("                           Welcome sir!")
    print("____________________________________________________________________________\n")
    print("1. Mark Attendence of Manager")
    print("2. Salary of Manager")
    print("3. Check Revenue")
    print("4. Check profit by month")
    print("5. Check profit by year")
    print("6. Approval of job application of new employ")
    print("7. Review Customer Feedback")
    print("8. Exit")
    print("____________________________________________________________________________\n")
    ochoice=int(input("Please select one option: "))
    if ochoice==1:
        os.system('cls')
        managerattendence()
    elif ochoice==2:
        os.system('cls')
        salarymanager()
    elif ochoice==3:
        os.system('cls')
        revenu(1)
    elif ochoice==4:
        os.system('cls')
        monthlyprofit()
    elif ochoice==5:
        os.system('cls')
        yearlyprofit()
    elif ochoice==6:
        os.system('cls')
        jobapproval()
    elif ochoice==7:
        os.system('cls')
        reviewfeedback(1)
    elif ochoice==8:
        os.system('cls')
        exit()
    else:
        print("Wrong Input! PLease Try again.")
    return ownerindex()

def managerindex():
    print("____________________________________________________________________________")
    print("                           Welcome Manager!")
    print("____________________________________________________________________________\n")
    print("1. Check Revenu")
    print("2. Mark Attendence of Employees")
    print("3. salary of Employees")
    print("4. Check Your Salary")
    print("5. Leave application of Employees ")
    print("6. check you own attendence")
    print("7. Enter Monthly Expences")
    print("8. Add Dish to Menu")
    print("9. Review Customer Feedback")
    print("10. Exit")
    print("____________________________________________________________________________\n")
    mchoice=int(input("Please select one option: "))
    print("____________________________________________________________________________\n")
    if mchoice==1:
        os.system('cls')
        revenu(2)
    elif mchoice==2:
        os.system('cls')
        attendence()
    elif mchoice==3:
        os.system('cls')
        employsalary()
    elif mchoice==4:
        os.system('cls')
        managersalary()
    elif mchoice==5:
        os.system('cls')
        leaveapplication()
    elif mchoice==6:
        os.system('cls')
        manageratten()
    elif mchoice==7:
        os.system('cls')
        addmonthyexpence()
    elif mchoice==8:
        os.system('cls')
        adddish()
    elif mchoice==9:
        os.system('cls')
        reviewfeedback(2)
    elif mchoice==10:
        os.system('cls')
        exit()
    else:
        print("Incorret Input")
        print("____________________________________________________________________________\n")
    return managerindex()

def employindex(name_e):
    print("_____________________________________________________________________")
    print("                  Welcome ",name_e,"\n")
    print("_____________________________________________________________________")
    print("1. Check Attendence\n2. Check salary\n3. Apply For leave\n4. Approval of leave\n5. Exit")
    echoice=int(input("Enter Your Chice: "))
    if echoice==1:
        os.system('cls')
        print(employattendence(name_e))
    elif echoice==2:
        os.system('cls')
        print(esalary(name_e))
    elif echoice==3:
        os.system('cls')
        print(leave(name_e))
    elif echoice==4:
        os.system('cls')
        print(appleave(name_e))
    elif echoice==5:
        os.system('cls')
        print(exit())
    else:
        print("Wrong Input! PLease Try again.")
    return employindex()

def owner():
    password=stdiomask.getpass("Enter your Password: ")
    print("---------------------------------------------------------------------------\n")
    if password=="12345678":
        os.system('cls')
        ownerindex()
    else:
        print("Wrong Password! Please Try again.")
        print("____________________________________________________________________________\n")
    return owner()

def manager():
    password=stdiomask.getpass("Enter your Password: ")
    print("---------------------------------------------------------------------------\n")
    if password=="12345678":
        os.system('cls')
        managerindex()
    else:
        print("Wrong Password! Please Try again.")
        print("____________________________________________________________________________\n")
    return manager()

def employ():
    print("____________________________________________________________________________")
    print("                      Welcome dear Employ!")
    print("____________________________________________________________________________\n")
    df2=pd.read_csv("employsalary.csv")
    file1=open("employsalary.csv")
    read1=csv.reader(file1)
    length1=len(list(read1))
    for i in range(length1-1):
        element=f"{i+1}. {df2['Name'][i]}"
        print(element)
    print("____________________________________________________________________________")
    ename=int(input("Enter your Choice: "))
    epassword=int(stdiomask.getpass("Enter your Password: "))
    if epassword==df2['Password'][ename-1]:
        os.system('cls')
        employindex(df2['Name'][ename-1])
    else:
        os.system('cls')
        print("Wrong password please try again!")
    return employ()

def mymain():
    print("---------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------")  
    print("                          Welcome to Restuarant                            ")
    print("---------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------")
    print("1. Customer")
    print("2. Owner")
    print("3. Manager")
    print("4. Employ")
    print("5. Apply for Job")
    print("6. Exit")
    print("---------------------------------------------------------------------------\n")
    Choice1=int(input("Select Any One: "))
    if Choice1==1:
        os.system('cls')
        menu()
    elif Choice1==2:
        os.system('cls')
        owner()
    elif Choice1==3:
        os.system('cls')
        manager()
    elif Choice1==4:
        os.system('cls')
        employ()
    elif Choice1==5:
        os.system('cls')
        jobapplication()
    elif Choice1==6:
        os.system('cls')
        exit("                     Thank You!")
    else:
        print("Wrong Input! please try again.")
        print("____________________________________________________________________________\n")
    return mymain()
print(mymain())