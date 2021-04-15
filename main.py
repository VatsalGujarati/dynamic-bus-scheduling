import datetime
from time import strftime

import matplotlib.pyplot as plt;
import pandas as pd
import numpy as np

bus = input('bus no. :  ')
month = input('month :  ')


# data = int(input('1. time base\n2. station base\n3. exit\n'))
# df = pd.read_csv(r'C:\Users\VATSAL\Desktop\station-scet\input\106\{}\{}.csv'.format(data,month))
#
# column = df.columns
# column1=column.tolist()
# c=column1.pop(0)
#
# col_name=column[1]
#
#
# date=df[column[1]]
#
#
#
# sum2 = 0
# z=[]


#######################################################################################################################

df2 = pd.read_csv(r'C:\Users\VATSAL\Desktop\station-scet\input\106\1\{}.csv'.format(month))

col = df2.columns
col1 = col.tolist()
col2=df2.columns
c = col1.pop(0)

buses=np.zeros((13, 31))
sum1=0

for i in range(len(col1)):
    count_data=df2[col1[i]]
    # print(len(count_data))
    for j in range(len(count_data)):
        if (count_data[j] > 35):
            buses[j][i]=1
        elif (count_data[j] < 35):
            buses[j][i]=0
        else:
            buses[j][i]=0
# print(buses)
new = df2.to_numpy()

for i in range(len(col1)):
    # print(new.loc[i][1])
    for j in range(len(new)):
        new[j][i+1] = int(buses[j][i])

pd.DataFrame(new, columns=[col2]).to_csv(r'C:\Users\VATSAL\Desktop\station-scet\output\{}.csv'.format(month), index=False)

#############################################################################################################################



while (True):
    data = int(input('-----------------------------\n1. Time base\n2. Station base\n3. Event base\n4. exit\n'))

#--------------------------------------------------------------------------------------------------------------------

    if (data==1):
        df = pd.read_csv(r'C:\Users\VATSAL\Desktop\station-scet\input\106\{}\{}.csv'.format(data, month))

        column = df.columns
        column1 = column.tolist()
        c = column1.pop(0)
        col_name = column[1]
        date = df[column[1]]
        sum2 = 0
        z = []
        time = df.Time
        n = int(input('1. day wise analysis\n2. month wise analysis \n'))

        if (n==1) :
            val = input('enter date in mm/dd/yyyy formate : ')
            for i in range(len(column)):
                if (val == column[i]):
                    count = df[column[i]]
                    col_name = column[i]
            plt.plot(time, count,'-o')
            plt.title(col_name)
            plt.xlabel('Time')
            plt.ylabel('Count')
            # plt.legend(['this is xq'])
            plt.axhline(y=40, color='r', linestyle='--',  label = 'capacity')
            plt.xticks(rotation=45)
            plt.show()

        elif (n==2):
            for i in column1:
                a = df[i]
                # print(a)
                for j in a:
                    sum2 = sum2 + j
                    # print(sum2)
                z.append(sum2)
                sum2 = 0
            plt.plot(column1, z,'-o')
            plt.title(month)
            plt.xlabel('Date')
            plt.ylabel('Count')
            plt.axhline(y=460, color='r', linestyle='--',  label = 'capacity')
            plt.xticks(rotation=50)
            plt.show()

        else:
            print('enter valid choise !')

#------------------------------------------------------------------------------------------------------------------------

    elif (data==2):
        df = pd.read_csv(r'C:\Users\VATSAL\Desktop\station-scet\input\106\{}\{}.csv'.format(data, month))

        column = df.columns
        column1 = column.tolist()
        c = column1.pop(0)
        col_name = column[1]
        date = df[column[1]]
        sum2 = 0
        z = []
        a = []
        station = df.Station
        n = int(input('1. day wise analysis\n2. month wise analysis \n'))

        if (n == 1):
            val = input('enter date in mm/dd/yyyy formate : ')
            for i in range(len(column)):
                if (val == column[i]):
                    count = df[column[i]]
                    col_name = column[i]
            plt.plot(station, count,'-o')
            plt.title(col_name)
            plt.xlabel('Station')
            plt.ylabel('Count')
            # plt.legend(['this is xq'])
            plt.axhline(y=300, color='r', linestyle='--', label='capacity')
            plt.xticks(rotation=20)
            plt.show()

        elif (n == 2):
            for row in df.itertuples(index=False):
                a = np.asarray(row)
                a = np.delete(a, 0)
                # print(a)
                for i in range(len(a)):
                    sum2 = sum2 + int(a[i])
                z.append(sum2)
                sum2 = 0
            # print(z)

            # for i in column1:
            #     a = df[i]
            #     # print(a)
            #     for j in a:
            #         sum2 = sum2 + j
            #         # print(sum2)
            #     z.append(sum2)
            #     sum2 = 0

            plt.plot(station, z, '-o')
            plt.title(month)
            plt.xlabel('Date')
            plt.ylabel('Count')
            plt.axhline(y=8450, color='r', linestyle='--', label='capacity')
            plt.xticks(rotation=20)
            plt.show()

        else:
            print('enter valid choise !')

#-----------------------------------------------------------------------------------------------------------------------

    elif (data==3):
        df3 = pd.read_csv(r'C:\Users\VATSAL\Desktop\station-scet\input\106\3\event.csv', parse_dates=['Date'])
        df4 = pd.read_csv(r'C:\Users\VATSAL\Desktop\station-scet\input\106\1\{}.csv'.format(month))

        month_no=0
        if(month=='march'):
            month_no = 3
        elif(month=='april'):
            month_no = 4

        date = df3['Date'].dt.month == month_no
        d = df3.loc[date]
        events = d.Event
        sd = d['Date'].apply(lambda x: x.strftime('%m/%d/%Y'))
        spe_date = sd.tolist()

        column = df4.columns
        column1 = column.tolist()
        c = column1.pop(0)
        # print(column1)
        s = pd.to_datetime(column1)
        data_date = s.strftime('%m/%d/%Y')
        # print(ff.tolist())

        sum3 = 0
        event_count = []

        for i in range(len(data_date)):
            for j in range(len(spe_date)):
                if (spe_date[j] == data_date[i]):
                    # print(spe_date[j])
                    a = df4[column1[i]]
                    # print(a)
                    for k in a:
                        sum3 = sum3 + k
                        # print(sum2)
                    event_count.append(sum3)
                    sum3 = 0
        # print(event_count)
        plt.plot(events, event_count, '-o')
        plt.title(month)
        plt.xlabel('Events')
        plt.ylabel('Count')
        # plt.legend(['this is xq'])
        plt.axhline(y=460, color='r', linestyle='--', label='capacity')
        plt.xticks(rotation=10)
        plt.show()

#----------------------------------------------------------------------------------------------------------------------

    elif (data==4):
        break

    else:
        print('enter valid number !')
