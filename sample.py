import os, shutil
# shutil ---> folder jo files he unko move krne me help krega

folders={
    'videos':['.mp4','.mkv'],
    'audios':['.mp3', '..wav'],
    'images':['.jpg', '.png'],
    'docs':['.txt', '.pdf', '.xlsx', '.xls', '.zip', '.rar'],
    'software' : ['.exe']
}

def rename():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, folder)) == True:
            os.rename(os.path.join(directory, folder), os.path.join(directory, folder.lower()))



def moveFiles(ext, file_name):
    find=False
    for folderName in folders:
        if "." + ext in folders[folderName]:
            # print('found', folderName)
            if folderName not in os.listdir(directory):
                os.mkdir(os.path.join(directory, folderName))
            # shutil.move(source, destination)
            shutil.move(os.path.join(directory, file_name), os.path.join(directory, folderName))
            find= True
            break
    if find == False:
        if Other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory, Other_name))
        shutil.move(os.path.join(directory, file_name), os.path.join(directory, Other_name))

  


# print(folders)
# for folderName in folders:
#     print(folderName, folders[folderName])

directory= r'G:\Pictures'
Other_name= input('Enter the other name')
rename()

allFiles= os.listdir(directory)
lenght= len(allFiles)
count = 1 
# print(allFiles)
for fileName in allFiles:
    if os.path.isfile(os.path.join(directory, fileName)) == True:
        # print('yes')
        moveFiles(fileName.split('.')[-1], fileName)
        print(f'Total Files : {lenght} | Done : {count} | Left : {lenght-count}')
    count=count+1
