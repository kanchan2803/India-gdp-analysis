import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


global df
df=pd.read_csv("gdp.csv")
#---------------------------------------------
#Function to display the main menu.
#---------------------------------------------
def MainMenu():
    ans='y'
    while ans=='y' or ans=='Y':
        opt=""
        print()
        print("==============================================================================")
        print("               Gross State Domestic Product (GSDP) of India                   ")
        print("******************************************************************************")
        print('''Welcome to GSDP analyser For India.
             \n GSDP is the sum of all value added by industries 
             \n within each state or union territory and serves as a counterpart
             \n to the national gross domestic product (GDP)''')
        print("\n")
        print('''The following program analyses the latest available
             \n gross state domestic product GSDP figures for all Indian States and
             \n Union Territories at current prices in crores (units of 10 million) or
             \n lakh crores(units of 1 trillion)of the Indian rupees.
             \n [No data is available for the union territories of Dadra and Nagar Haveli
             \n and Daman and Diu, Ladakh and Lakshadweep.]''')
        print("\n")
        print('''Choose the way you would prefer to analyse data for the following years
             (2011-12 to 2020-21):''')
        print("1-Data Visualisation\n")
        print("2-Analysis\n")
        print("3-Manipulation\n")
        print("4-Exit")
        print("===============================================")
        opt=input("Enter your choice: ")
        if opt=='1':
            visuals()
        elif opt=='2':
            analysis()
        elif opt=='3':
            manipulation()
        elif opt=='4':
            my_chance=input("Do you really want to exit?(y/n)")
            if my_chance=="y" or my_chance=="Y":
                print("Thank you. Exiting now......")
                sys.exit()
        else:
            print("\nInvalid choice. Try again")
            continue
    else:
        ans=input("Do you want to continue(y/n)")


#------------------------------------------------
#Function for Data Visualization.
#------------------------------------------------
def visuals():
    df=pd.read_csv("gdp.csv")
    while True:
        print("V I S U A L   M E N U")
        print("=====================")
        print("1-Line Chart of a Particular Year")
        print("2-Bar Chart for different Years")
        print("3-Histogram for a Year")
        print("4-Line Chart Average GDP Year wise")
        print("5-Back to Main Menu")
        print("==================================")
        choice=int(input("Enter your choice: "))
        if choice==1:
            year=input("Enter Year of GDP(2011-12 to 2020-21)")
            df1=df.sort_values(by=[year],ascending=False)
            n=int(input("Enter number of top states/UTs (1-36) : "))
            print(df1.head(n))
            df1.plot(x ='State/ UTs', y=year, kind = 'line',rot=30)
            plt.xlabel("State/UT Name-->", color='b',fontsize=12)
            plt.ylabel("GSDP (in Crore)->", color='b',fontsize=12)
            plt.title("Top "+str(n)+" Indian State(s) GDP Analysis",color='r',fontsize=16) 
            plt.show()
        elif choice==2:
            year=eval(input("Enter Year of GDP as list like['2011-12','2012-13']: "))
            n=int(input("Enter number of states (1-36) : "))
            print(df.head(n))
            df1=df.head(n)
            df1.plot(x='State/ UTs',y=year,kind='bar',rot=30)
            plt.xlabel("State/UT Name-->", color='r',fontsize=12)
            plt.ylabel("GSDP (in Crore)->", color='r',fontsize=12)
            plt.title("Top"+str(n)+" Indian State(s) GDP Analysis",color='g',fontsize=16) 
            plt.show()
        elif choice==3:
            year=input("Enter Year of GDP(2011-12 to 2020-21) ")
            df.hist(column=year,color='pink',edgecolor='black')
            plt.xlabel("GSDP (in Crore)->", color='r',fontsize=12)
            plt.ylabel("No. of States", color='r',fontsize=12)
            plt.title("Indian State(s) GDP Analysis of \nYear-"+year,color='g',fontsize=16) 
            plt.show()
        elif choice==4:
            s1=df.mean()
            mylabel=s1.index
            plt.plot(mylabel,s1.values,linewidth=2,color='g',marker='*',ms=10)
            plt.xlabel("Year-->", color='b',fontsize=10)
            plt.ylabel("GSDP (in Crore) of India ->", color='b',fontsize=12)
            plt.title("Indian GDP Rate Analysis 2011-12 to 2020-21", color='r',fontsize=16) 
            plt.grid()
            plt.show()    
        else:
            break

#------------------------------------------------
#Function to analyse data from a dataframe.
#------------------------------------------------
def analysis():
    df=pd.read_csv("gdp.csv")
    while True:
        print("Data Frame Analysis")
        print("*******************")
        menu='''\n 1.Top record
         \n 2.Bottom records
         \n 3.To Display GDP of a particular year
         \n 4.To Display States with Maximum GSDP
         \n 5.To display Average GDP of India
         \n 6.To display Complete DataFrame
         \n 7.To Minimum, Maximum and Average GDP in a year" 
         \n 8.Back to Main Menu'''
        print(menu)
        print("==========================================")
        ch_an=int(input("Enter  your choice: "))
        if ch_an==1:
            n=int(input("Enter the number of records to be displayed: "))
            print("Top",n,"records from the dtaframe")
            print(df.head(n))
        elif ch_an==2:
            n=int(input("Enter the number of records to be displayed: "))
            print("Bottom",n,"records from the dtaframe")
            print(df.tail(n))
        elif ch_an==3:
            print("Name of the columns\n",df.columns)
            col=eval(input("Enter the year of GDP like ['State/ UTs','2011-12']: "))
            print(df.loc[:,col])
        elif ch_an==4:
            yr=input("Enter Year : ")
            print()
            print("State with Maximum GDP in the year-"+yr)
            print("----------------------------------------------")
            x=df[yr].max()
            print(df.loc[(df[yr]==x),['State/ UTs',yr]])
            print("----------------------------------------------\n")
        elif ch_an==5:
            print("Average GDP of India")
            print("-------------------------")
            print(df.mean())
            print("-------------------------")
        elif ch_an==6:
            print("Displaying Complete DataFrame")
            print("-------------------------")
            print(df)
            print("-------------------------")
        elif ch_an==7:
            yr=input("Enter Year : ")
            print("\nMaximum GDP:")
            print("-------------------------")
            x=df[yr].max()
            print(df.loc[(df[yr]==x),['State/ UTs',yr]])
            print("-------------------------")
            print("Minimum GDP:")
            print("-------------------------")
            y=df[yr].min()
            print(df.loc[(df[yr]==y),['State/ UTs',yr]])
            avg=df[yr].mean()
            print("------------------------------------------------------------")
            print("Average GDP in the Year-"+yr+" in India =",avg)
            print("------------------------------------------------------------")
        else:
            break


#------------------------------------------------
#Function to manipulate data in a dataframe.
#------------------------------------------------
def manipulation():
    df=pd.read_csv("gdp.csv")
    while True:
        print("\n\nManipulation Menu")
        print("*********************")
        print('''\n1. Insert a row\n
2. Insert a Column\n
3. Delete a Row\n
4. Delete a column\n
5. Back to Main Menu''')
        print("=====================")
        mch=int(input("Enter your choice: "))
        if mch==1:
            df1=pd.DataFrame()
            col=df.columns
            print(col)
            print(df.head(1))
            j=0
            lst=[]
            lst1=eval(input("Enter a list of values in the sequence of columns: "))
            print(lst1)
            s1=pd.Series(lst1,index=df.columns)
            df1=df.append(s1,ignore_index=True)
            print("New row inserted")
            print(df1)
            df1.to_csv("gdp.csv",index=False)
            df=pd.read_csv("gdp.csv")
        elif mch==2:
            n=len(df.index)
            yr=input("Enter Year of GDP : ")
            lst=[]
            for i in range(0,n):
                gdp=float(input("Enter GDP of "+df.loc[i,['State/ UTs']]+": "))
                lst.append(gdp)
            df[yr]=lst
            print(df)
            df.to_csv("gdp.csv",index=False)
            df=pd.read_csv("gdp.csv")
        elif mch==3:
            print("List of States-\n",df['State/ UTs'])
            n=int(input("Enter the index number of the State for row deletion :"))
            ch=input("Do you really want to delete  row of-\n"+str(df[(df.index==n)])+"(y/n)?")
            if ch=='y' or ch=='Y':
                df.drop(index=n,inplace=True)
                print(df)
                print("Row of index no- ",n,"deleted successfully!!!")
                df.to_csv("gdp.csv",index=False)
                df=pd.read_csv("gdp.csv")
        elif mch==4:
            print(df.columns)
            col=input("Enter column name to be deleted from the above")
            ch=input("Do you really want to delete  column(y/n)?")
            if ch=='y' or ch=='Y':
                del df[col]
                print("Column- ",col,"deleted successfully!!!")
                print(df)
                df.to_csv("gdp.csv",index=False)
                df=pd.read_csv("gdp.csv")
        else:
            break



        
#***************************************************
# Calling main program
#***************************************************
MainMenu()
