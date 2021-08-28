import mimetypes
import glob
import os
import datetime
from datetime import date
from datetime import datetime as dtime
abs_path="E:/Desktop/"

mimetypes.init()
image_ext=list()
image_files=list()


#determines if script will continue to run or not
now=dtime.today().strftime('%d/%m/%Y %H:%M:%S')

try: fhand=open('timestamp.txt')
except:
	fhand=open('timestamp.txt','w')
	fhand.write(now)
	print('timestamp.txt missing. Creating new timestamp file........')
	print('Closing Script')
	exit()
for line in fhand:
    timestamp=line
    break
timestamp_date=timestamp.split()[0].split('/')
timestamp_time=timestamp.split()[1].split(':')
now_date=now.split()[0].split('/')
now_time=now.split()[1].split(':')
print('timestamp_date:',timestamp_date)
print('timestamp_time:',timestamp_time)
print('now_date:',now_date)
print('now_time:',now_time)

fhand.close()


#condition for running script
if timestamp_date==now_date: #script is already done this day
    print('Script: Already Done Earlier')
    exit()
elif int(now_time[0])<=5: #script will ony start past 5AM
    print('Script: Not Yet')
    exit()
print('\nScript: Starting.....')
#rewrite timestamp text if line passes here
fhand=open('timestamp.txt','w')
fhand.write(now)
print('Timestamp Updated.....')

#retrieve date
now=date.today()
date=now.strftime("%d %m %Y").split()
first_day=datetime.date(int(date[2]),int(date[1]),1).weekday()

#determine folder number name based on week number
first_week=7-first_day
if int(date[0])<=first_week:folder_number="1"
elif int(date[0])<=first_week+7:folder_number='2'
elif int(date[0])<=first_week+14:folder_number='3'
elif int(date[0])<=first_week+21:folder_number='4'
elif int(date[0])<=first_week+28:folder_number='5'
elif int(date[0])<=first_week+35:folder_number='6'


#make list of all image extensions
for ext in mimetypes.types_map:
    if mimetypes.types_map[ext].split('/')[0]=='image':
        image_ext.append(ext)

#find all images on current directory
for ext in image_ext:
    for file in glob.glob(abs_path+'*'+ext):
        image_files.append(file)
print('\nTransferred Files:\n',image_files)

#transfer all files to new folder
file_folder=abs_path+"images/"+now.strftime("%b")+'(Week_'+folder_number+')/'
os.makedirs(os.path.dirname(file_folder),exist_ok=True)
for file in image_files:
    file=file.split('\\')[1]
    count=1
    copied_file=file
    while(os.path.isfile(file_folder+copied_file)): #rename file to prevent overwr
        copied_file=file
        copied_file=copied_file.split('.')
        filename=copied_file[0]
        ext=copied_file[1]
        filename=filename+'_'+str(count)
        count=count+1
        copied_file=filename+'.'+ext
    os.rename(abs_path+file,file_folder+copied_file)
print('\n\n........SUCCESS........\n......CLOSING SCRIPT......\n')


