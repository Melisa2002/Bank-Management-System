#WONG KAH YING
#TP064640


def generate_id(det):
    with open("generateid.txt","r") as fh:
        rec = fh.readline()
        all_rec = rec.strip().split(":")
    first = ""
    if det == "admin":
        first = "AMY"
        old_id = all_rec[0][3:]
    elif det == "customer":
        first = "CMY"
        old_id = all_rec[1][3:]
    else :
        first = "TSC"
        old_id = all_rec[2][3:]
    next_id = int(old_id)+1
    if len(str(next_id)) == 1 :
        new_id = first+"0000"+str(next_id)
    elif len(str(next_id)) == 2 :
        new_id = first+"000"+str(next_id)
    elif len(str(next_id)) == 3 :
        new_id = first+"00"+str(next_id)
    elif len(str(next_id)) == 4 :
        new_id = first+"0"+str(next_id)
    elif len(str(next_id)) == 5 :
        new_id = first+str(next_id) 

    if det == "admin":
        all_rec[0] = new_id
    elif det == "customer" :
        all_rec[1] = new_id
    else :
        all_rec[2] = new_id
    line=":".join(all_rec)
    with open("generateid.txt","w") as fh1:
        fh1.write(line)
    return new_id

def acc_num_trans():
    with open("generateid.txt","r") as fh :
        fh_line = fh.readline()
        all_rec = fh_line.strip().split(":")
        new_acc_nmb = int(all_rec[3]) + 1
        all_rec[3] = str(new_acc_nmb)
    new_line = ":".join(all_rec)
    with open("generateid.txt","w") as fh1 :
        fh1.write(new_line)
    return str(new_acc_nmb)

def check_phonenum():
    all_ph = []
    with open("cusdetails.txt","r") as fh:
        for i in fh :
            fh_line = i.strip().split(":")
            all_ph.append(fh_line[2])
    length = len(all_ph)
    while True:
        num=-1
        phone_number = input ("Enter Phone Number(Must 10 digits):")
        for i in range(0,length):
            if phone_number == all_ph[i] :
                print ("The phone number is exist,try another one.")
                num = i
                break
        if num <0:
            return phone_number

def create_admin():
    print("*"*47)
    while True :
        id = generate_id("admin")
        password = id
        while True :
            print("PLEASE BE CAUTION:NAME ARE NOT ALLOWED TO EDIT !!!!")
            name = input("Enter new admin name:")
            if not name.isalpha():
                print("Only words are allowed!")
            else:
                break
        
        account = "2"
        new_admin = id+":"+password+":"+name+":"+account+"\n"
        with open("id&pass.txt","a") as fh:
            fh.write(new_admin)
        print("=========Successfully create admin account=========\n")
        print("\tNew ID:",id)
        print("\tPassword:",password)
        print("\tHolder name:",name)
        print("\tAccount : Admin ")
        print("===================================================\n")
        ans = input("Enter Y to continue register account.....otherwise exit to interface:")
        if ans == "Y":
            True 
        else :
            break

def birth_day():
    while True:
        print("Example:")
        print("Year:2000 Month:12 Day:12")
        birth_yr = input ("Birthday Year:")
        birth_mon =input ("Birthday Month:")
        birth_dt = input ("Birthday Day:")    
        if birth_yr.isnumeric() and birth_mon.isnumeric() and birth_dt.isnumeric():
            try:
                dt = datetime.date(int(birth_yr),int(birth_mon),int(birth_dt))
                dt1 =str(dt.strftime("%Y%m%d"))   
                return dt1
            except ValueError:
                print("Invalid Date")
        else:
            print("Invalid Format!")

def display_all_user():
    print("\n\n"+"ALL USER ACCOUNT".center(80))
    print("="*80)
    print("|"+"USER ID".center(20)+"|"+"PASSWORD".center(20)+"|"+"USERNAME".center(20)+"|"+"ACCOUNT TYPE".center(15)+"|")
    print("-"*80)
    with open("id&pass.txt","r") as fh :
        for line in fh:
            all_rec=line.strip().split(":")
            print("|"+all_rec[0].center(20)+"|"+all_rec[1].center(20)+"|"+all_rec[2].center(20)+"|"+all_rec[3].center(15)+"|")
    print("-"*80+"\n\n\n")

def create_cus():
    print("*"*47)
    while True :
        id = generate_id("customer")
        acc_id = acc_num_trans()
        password = id
        while True :
            print("PLEASE BE CAUTION:NAME ARE NOT ALLOWED TO EDIT !!!!")
            name = str(input("Enter new customer name:"))
            if not name.isalpha():
                print("Only words are allowed!!!")
            else:
                break
        account = "3"
        while True:
            ph = check_phonenum()
            if ph.isnumeric() and len(ph)== 10 :
                break
            else :
                print("Only number are allowed!!!")
        dt = birth_day()
        while True :
            cus_type = str(input("Saving account(SA)/Current account(CA):"))
            if cus_type == "SA" or cus_type == "CA" :
                break
            else:
                print("Only SA and CA are allowed!!!!!")
        while True :
            money = input("Enter the deposit:RM")
            if cus_type =="SA":
                if not money.isnumeric() :
                    print("Only numbers are allowed!!!!")
                else:
                    if int(money)>=100 :
                        break
                    else:
                        print("Minimum Deposit Must Be RM100.")
            else :
                if not money.isnumeric() :
                    print("Only numbers are allowed!!!!")
                else:
                    if int(money)>=500 :
                        break
                    else:
                        print("Minimum Deposit Must Be RM500.")
        cus_det = id+":"+name+":"+str(ph)+":"+dt+":"+cus_type+":"+str(money)+":"+acc_id+"\n"
        with open("cusdetails.txt","a") as fh:
            fh.write(cus_det)

        new_customer = id+":"+password+":"+name+":"+account+"\n"
        with open("id&pass.txt","a") as fh1:
            fh1.write(new_customer)

        trans_id = generate_id("transaction")
        tdy = datetime.date.today()
        tdy_dt = tdy.strftime("%Y%m%d")
        stm = id+":"+trans_id+":"+str(tdy_dt)+":"+"Deposit"+":"+"+"+str(money)+":"+"Balance"+":"+str(money)+"\n"

        with open("statement.txt","a") as fh2:
            fh2.write(stm)
        
        print("=========Successfully create customer account=========\n")
        print("\tNew ID:"+id)
        print("\tPassword:"+password)
        print("\tAccount Number:"+acc_id)
        print("\tHolder name:"+name)
        print("\tPhone number:"+ph)
        print("\tBirthday:"+dt)
        print("\tCustomer Account Type:"+cus_type)
        print("\tBalance:RM"+money)
        print("======================================================\n")
        ans = input("Enter Y to continue register account.....otherwise exit to interface:")
        if ans == "Y":
            True
        else :
            break

def display_cus():
    print("-"*109)
    print("|"+"Customer ID".center(15)+"|"+"Username".center(20)+"|"+"Phone Number".center(20)+"|"+"Birthday".center(10)+"|"+"Type".center(6)+"|"+"Balance".center(10)+"|"+"Account Number".center(20)+"|")
    print("-"*109)
    with open("cusdetails.txt","r") as fh :
        for line in fh:
            all_rec= line.strip().split(":")
            print("|"+all_rec[0].center(15)+"|"+all_rec[1].center(20)+"|"+all_rec[2].center(20)+"|"+all_rec[3].center(10)+"|"+all_rec[4].center(6)+"|"+all_rec[5].center(10)+"|"+all_rec[6].center(20)+"|")
            print("-"*109)
    print("\n")

def cus_statement(cus):
    while True:
        print("*"*40)
        print("DATE FORMAT MUST BE YYYYMMDD")
        start_dt = input ("Enter Start Date:")
        end_dt = input("Enter End date:")
        if len(start_dt) != 8 or len(end_dt) != 8 or not start_dt.isnumeric() or not end_dt.isnumeric():
            print("MUST FOLLOW THE DATE FORMAT!!!!!")
        else :
            try:
                start_dt =datetime.date(int(start_dt[:4]),int(start_dt[4:6]),int(start_dt[6:8]))
                end_dt = datetime.date(int(end_dt[:4]),int(end_dt[4:6]),int(end_dt[6:8]))
                start_dt = int(start_dt.strftime("%Y%m%d"))
                end_dt = int(end_dt.strftime("%Y%m%d"))
                break
            except:
                print("Invalid Date")
    with open ("cusdetails.txt","r") as fh:
        for i in fh:
            fh_line = i.strip().split(":")
            if cus[0]== fh_line[0] :
                acctyp = fh_line[4]
                bal = fh_line[5]
                accid = fh_line[6]
                break

    print("*"*40)
    print("\n\n\t\t\t\t=========Account Report of",fh_line[1],"==========")
    print("User ID:",cus[0])
    print("Statement Date :",start_dt,"-",end_dt,"\t\t\t\t\t","Account Type:"+acctyp)
    print("Account Number:",accid)
    print("Current Balance:RM",bal)
    print("-"*111)
    print("|"+"Transaction ID".center(20)+"|"+"Date".center(20)+"|"+"Transact".center(20)+"|"+"Transaction Amount(RM)".center(30)+"|"+"Balance(RM)".center(15)+"|")
    print("-"*111)
    dep_mny = 0
    with_mny = 0
    with open("statement.txt","r") as fh:
        for line in fh :
            all_rec =line.strip().split(":")
            if cus[0] == all_rec[0] and  int(all_rec[2])>=start_dt and int(all_rec[2])<= end_dt:
                print("|"+all_rec[1].center(20)+"|"+all_rec[2].center(20)+"|"+all_rec[3].center(20)+"|"+all_rec[4].center(30)+"|"+all_rec[6].center(15)+"|")
                if all_rec[3] == "Deposit":
                    dep_mny = dep_mny + int(all_rec[4][1:])
                else:
                    with_mny = with_mny +int(all_rec[4][1:])
    print("-"*111)
    print("Total deposit money :RM",dep_mny)
    print("Total Withdraw money :RM",with_mny)
    print("-"*111)
    print("*"*111)


def interface_statement():
    while True :
        print("*"*50)
        print("1 :Display All customer statement")
        print("2 :Display certain customer statement")
        print("3 :Exit")
        ans = input ("Enter Number:")
        if ans == "1" :
            while True:
                print("*"*40)
                print("DATE FORMAT MUST BE YYYYMMDD")
                start_dt = input ("Enter Start Date:")
                end_dt = input("Enter End date:")
                if len(start_dt) != 8 or len(end_dt) != 8 or not start_dt.isnumeric() or not end_dt.isnumeric():
                    print("MUST FOLLOW THE DATE FORMAT!!!!!")
                else :
                    try:
                        start_dt =datetime.date(int(start_dt[:4]),int(start_dt[4:6]),int(start_dt[6:8]))
                        end_dt = datetime.date(int(end_dt[:4]),int(end_dt[4:6]),int(end_dt[6:8]))
                        start_dt = int(start_dt.strftime("%Y%m%d"))
                        end_dt = int(end_dt.strftime("%Y%m%d"))
                        break
                    except:
                        print("Invalid Date")
            print("*"*40)
            print("=========Statement of all customer==========".center(112))
            print("Date:",start_dt,"-",end_dt)
            print("-"*112)
            print("|"+"User ID".center(10)+"|"+"Transaction ID".center(20)+"|"+"Date".center(20)+"|"+"Transaction".center(20)+"|"+"Transact money(RM)".center(20)+"|"+"Balance(RM)".center(15)+"|")
            print("-"*112)
                
            with open ("statement.txt","r") as fh :
                for line in fh :
                    all_rec=line.strip().split(":")
                    if int(all_rec[2]) >= start_dt and int(all_rec[2]) <= end_dt :
                        print("|"+all_rec[0].center(10)+"|"+all_rec[1].center(20)+"|"+all_rec[2].center(20)+"|"+all_rec[3].center(20)+"|"+all_rec[4].center(20)+"|"+all_rec[6].center(15)+"|")
            print("-"*112)
        elif ans == "2" :
            while True :
                valid = 0
                user_id = input("Enter customer ID:")
                with open ("cusdetails.txt","r") as fh1 :
                    for line in fh1 :
                        all_rec=line.strip().split(":")
                        if user_id == all_rec[0] :
                            cus_statement(all_rec)
                            valid = 1
                            break
                    
                if valid == 0 :
                    print("Invalid User ID")
                else:
                    break
        elif ans == "3":
            return
        else :
            print("Invalid number.")

def super_interface(usr_name):
    while True:
        print("\n"+"="*47+"\n")
        print("WELCOME TO SUPERACCOUNT INTERFACE :",usr_name)
        print("\n\t-----------MENU-----------\n")
        print("1 : Create admin account")
        print("2 : Display all user account")
        print("3 : Create Customer account")
        print("4 : Show Account Statement")
        print("5 : Show Customer Details")
        print("6 : Exit")
        ans = input("Enter the number:")
        if ans == "1":
            create_admin()
        elif ans == "2":
            display_all_user()
        elif ans == "3":
            create_cus()
        elif ans == "4":
            interface_statement()
        elif ans == "5":
            display_cus()
        elif ans =="6":
            print("Successfully logout account!!!!!")
            break
        else:
            print("Invalid number,Please try again.")

def admin_edit():
    cus_det = []
    valid = 0
    with open("cusdetails.txt","r")as fh:
        for line in fh :
            line_det = line.strip().split(":")
            cus_det.append(line_det)
    print("*"*47)
    length = len(cus_det)
    num = -1
    print("="*50)
    id = input("Enter customer id :")
    for i in range (0,length):
        if id == cus_det[i][0] :
            print("User Name :"+cus_det[i][1])
            num = i
            valid = 1
            break
    if valid == 0 :
        print("Invalid id!")
    
    while valid == 1:
        print("*"*20+"EDIT DETAILS"+"*"*20)
        print("\t\t1 :Change password")
        print("\t\t2 :Change phone number")
        print("\t\t3 :Exit")
        ans= str(input("Enter the number of service:"))
        if ans == "1":
            chg_pass(cus_det[i])
        elif ans == "2":
            print("Old Phone Number:"+cus_det[num][2])
            while True:
                new_ph = check_phonenum()
                if new_ph.isnumeric() and len(new_ph) == 10:
                    print("Succesfully Edit details.")
                    break
                else :
                    print("Invalid phone number.")
            cus_det[num][2] = new_ph
            with open("cusdetails.txt","w") as fh1:
                for i in range (0,length):
                    join_back = ":".join(cus_det[i])+"\n"
                    fh1.write(join_back)
        elif ans == "3":
            return
        else:
            print("Invalid number.")
                
def chg_pass(det):
    all_det = []
    ind=-1
    with open("id&pass.txt","r") as fh:
        for line in fh :
            file_line=line.strip().split(":")
            all_det.append(file_line)
    length = len(all_det)
    while True :
        new_pass = input("Enter New Password:")
        re_enter= input("Enter New Password again:")
        if re_enter == new_pass and new_pass.isidentifier():
            break
        else:
            print("Wrong confirmation Password.Password must included number and word!!!!")
    for i in range (0,length):
        if det[0]== all_det[i][0] :
            ind =i
            break
    if ind >= 0:
        all_det[ind][1]=new_pass
        with open("id&pass.txt","w") as fh1:
            for i in range(0,length):
                new_line=":".join(all_det[i])+"\n"
                fh1.write(new_line)
        print("Successfully change password!!!")
        return new_pass

def adm_interface(usr):
    while True:
        print("="*37)
        print("WELCOME TO ADMIN MENU:",usr[2])
        print("\n===============M E N U ==============\n")
        print("1 :Create New Customer account")
        print("2 :Display customer details")
        print("3 :Edit customer password and phone number")
        print("4 :Change Password")
        print("5 :Customer Statement")
        print("6 :Exit")
        ans = input("Enter number :")
        if ans == "1" :
            create_cus()
        elif ans == "2" :
            display_cus()
        elif ans == "3" :
            admin_edit()
        elif ans == "4" :
            chg_pass(usr)
        elif ans == "5":
            interface_statement()
        elif ans == "6" :
            print("Successfully logout account.")
            break
        else :
            print("Invalid number.Please enter number again")

def with_draw(cus):
    cus_det = []
    acc_number = input ("Enter Account Number:")
    with open("cusdetails.txt","r") as fh:
        for line in fh :
            file_line=line.strip().split(":")
            cus_det.append(file_line)
    ind=-1
    length = len(cus_det)
    for i in range (0,length):
        if cus[0]== cus_det[i][0] and acc_number == cus_det[i][6]:
            ind =i
            break

    if ind== -1 :
        print("Invalid Account Number!")
        return
    pass_word = input("Enter the password :")
    if pass_word != cus[1] :
        print("Wrong Password is entered!")
        print("You can't withdraw money!!!")
        return

    mny = int(cus_det[ind][5])
    bal=mny
    print("="*30)
    print("Your Balance:RM"+cus_det[ind][5])
    if cus_det[ind][4] == "SA":
            while True:
                out_money=input("How much do you want to withdraw?:RM")
                if out_money.isnumeric() and out_money != "0" :
                    out_money=int(out_money)
                    amt = mny - out_money
                    if amt < 100:
                        print ("You cant withdraw money,your balance will less than RM100 after withdraw.")
                        break
                    else :
                        bal = amt
                        trans_id = generate_id("transaction")
                        tdy = datetime.date.today()
                        now = tdy.strftime("%Y%m%d")
                        stm = cus_det[ind][0]+":"+trans_id+":"+str(now)+":"+"WithDraw"+":"+"-"+str(out_money)+":"+"Balance"+":"+str(bal)+"\n"
                        with open("statement.txt","a") as fh2:
                            fh2.write(stm)
                        break
                else:
                    print("Only numbers are allowed!!!!") 
    else :
            while True:
                out_money=(input("How much do you want to withdraw?:RM"))
                if out_money.isnumeric() and out_money!="0":
                    out_money=int(out_money)
                    amt = mny - out_money
                    if amt < 500 :
                        print ("You can't withdraw money,Your balance will less than RM500 after withdraw. ")
                        break
                    else:
                        bal = amt
                        trans_id = generate_id("transaction")
                        tdy = datetime.date.today()
                        now = tdy.strftime("%Y%m%d")
                        stm = cus_det[ind][0]+":"+trans_id+":"+str(now)+":"+"WithDraw"+":"+"-"+str(out_money)+":"+"Balance"+":"+str(bal)+"\n"
                        with open("statement.txt","a") as fh2:
                            fh2.write(stm)
                        break
                else :
                    print("Only numbers are allowed")
    bal = str(bal)
    print("Now your Balance :RM",bal)
    if ind >= 0:
        cus_det[ind][5]=bal
        with open("cusdetails.txt","w") as fh1:
            for i in range(0,length):
                new_line=":".join(cus_det[i])+"\n"
                fh1.write(new_line)
    
def dep_money(det):
    cus_det = []
    with open("cusdetails.txt","r") as fh:
        for line in fh :
            file_line=line.strip().split(":")
            cus_det.append(file_line)
    ind=-1
    length = len(cus_det)
    acc_number = input ("Enter Account Number:")
    for i in range (0,length):
        if det[0]== cus_det[i][0] and acc_number == cus_det[i][6]:
            ind =i
            break
    if ind== -1 :
        print("Invalid Account Number!")
        return
    pass_word = input("Enter the password :")
    if pass_word != det[1] :
        print("Wrong Password is entered!")
        print("You can't Deposit Money!")
        return

    mny = int(cus_det[ind][5])
    if ind>=0 :
        print("*"*30)
        print("Your Balance:RM",mny)
        while True :
            in_mny= input("How much you want deposit?:RM")
            if not in_mny.isnumeric() or in_mny == "0" :
                print ("Only numbers are allowed!!")
            else:
                balance = mny + int(in_mny)
                print("Successfully deposit money")
                print("Balance :RM",balance)
                cus_det[ind][5]=str(balance)
                trans_id = generate_id("transaction")
                tdy = datetime.date.today()
                now = tdy.strftime("%Y%m%d")
                stm = cus_det[ind][0]+":"+trans_id+":"+str(now)+":"+"Deposit"+":"+"+"+in_mny+":"+"Balance"+":"+str(balance)+"\n"
                with open("statement.txt","a") as fh1:
                    fh1.write(stm)
                break
                
        with open("cusdetails.txt","w") as fh2:
            for i in range(0,length) :
                new_cus_det = ":".join(cus_det[i])+"\n"
                fh2.write(new_cus_det)

def show_det(cus):
    cus_det = []
    with open("cusdetails.txt","r") as fh:
        for line in fh:
            file_line=line.strip().split(":")
            cus_det.append(file_line)
    length = len(cus_det)
    num =-1
    for i in range(0,length):
        if cus[0] == cus_det[i][0]:
            num = i
            break
    if num >= 0 :
        print("\n"+"*"*80)
        print("\t\t======A C C O U N T D E T A I L S ======\n")
        print("User ID:",cus_det[num][0])
        print("Account Number:",cus_det[num][6])
        print("User Name:",cus_det[num][1])
        print("Phone Number:",cus_det[num][2])
        print("Birthday:",cus_det[num][3])
        print("Account Type:",cus_det[num][4])
        print("Balance:RM",cus_det[num][5],"\n"+"*"*80)
        print("*"*80)

def chk_bal(cus):
    with open("cusdetails.txt","r") as fh:
        for line in fh :
            fh_line=line.strip().split(":")
            if cus[0]== fh_line[0] :
                print("Current Balance:RM",fh_line[5])
                break

def cus_interface(cus):
    print("="*37)
    if cus[1] == cus[0] :
        print("You need to change the default password!")
        cus[1]=chg_pass(cus)
    while True:
        print("\n\n\t  WELCOME TO USER INTERFACE:",cus[2])
        print("\n=================U S E R M E N U=================\n")
        print("1 :Withdraw money")
        print("2 :Deposit money")
        print("3 :Show account details")
        print("4 :Change Password")
        print("5 :Check Balance")
        print("6 :Bank Statement")
        print("7 :Logout account")
        ans = input("Enter the number:")
        if ans == "1":
            with_draw(cus)
        elif ans == "2":
            dep_money(cus)
        elif ans == "3":
            show_det(cus)
        elif ans == "4":
            cus[1]=chg_pass(cus)
        elif ans == "5":
            chk_bal(cus)
        elif ans == "6":
            cus_statement(cus)
        elif ans == "7":
            print("Successfully log out account")
            break
        else:
            print("Invalid number.Please try again.")

def login_interface():
    valid=0
    print("***********WELCOME TO MYBANK SYSTEM************")
    user_id = str(input("Enter the user id:"))
    user_pass = str(input ("Enter the password:"))
    with open("id&pass.txt","r") as fh :
        for line in fh:
            all_rec= line.strip().split(":")
            if user_id==all_rec[0] and user_pass==all_rec[1]:
                rec = all_rec
                valid = 1
                break
            

    if valid == 1:
        print("Successfully enter into account")
        return rec
    else :
        print("Invalid user id or password.")
        return "Invalid"


#MAIN LOGIC
#=============================================
import datetime
import os
os.chdir("C:\\Users\\kahyi\\Desktop\\Assignment\\python assignment\\assignmenttextfile")
while True :
    process = login_interface()
    if process == "Invalid":
        print ("Please try again")
    elif process[3] == "1" :
        super_interface(process[2])
    elif process[3] == "2" :
        adm_interface(process)
    else:
        cus_interface(process)

    print("Do you want to continue login?")
    ans = input("Enter y to EXIT,else continue login .....:")
    if ans == "y":
        print("THANKS FOR USING MYBANK SYSTEM.GOODBYE:)!!!!")
        break
        