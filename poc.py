## Write code here
import os
import shutil
import datetime



# Create directories if they don't exist
create_folder = r"C:\Users\Sindhu Barathi A\Downloads\THBS_TRANING\POC"

dir = os.path.join(create_folder, 'good_data')
if not os.path.exists(dir):
    print("Folder Created")
    os.mkdir(dir)

dir = os.path.join(create_folder, 'bad_data')
if not os.path.exists(dir):
    print("Folder Created")
    os.mkdir(dir)

good_dir = r'C:\Users\Sindhu Barathi A\Downloads\THBS_TRANING\POC\good_data'
bad_dir = r'C:\Users\Sindhu Barathi A\Downloads\THBS_TRANING\POC\bad_data'

#Giving the directory
Directory = r'C:\Users\Sindhu Barathi A\Downloads\THBS_TRANING\POC\RAW_DIR'

# Get today's date in the specified format
today = datetime.date.today().strftime('%d_%m_%Y')


for file_name in os.listdir(Directory):
    print(file_name)
    if file_name.startswith('poc') and file_name.endswith('.csv'):
        file_path = os.path.join(Directory, file_name)
        if os.stat(file_path).st_size > 0:
            temp1 = file_name[0:-4]
            temp2 = '.csv'
            new_name = temp1 + today + temp2
            print(new_name)
            new_file_path = os.path.join(good_dir, new_name)
            shutil.move(file_path, new_file_path)
        else:
            shutil.move(file_path, bad_dir)
