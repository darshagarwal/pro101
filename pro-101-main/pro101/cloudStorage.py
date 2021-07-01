import os
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token= access_token
    
    def upload_File(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root, files in os.walk(file_from):
            for name in files:
                file_name=os.path.join(root, name)
            dbx.files_upload(file_name.read(),file_to,mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token='sl.Azxl99MqkyLgxhx2hs_JFsGYP7-MRZ-y4gcQAujqji_3blv5u-iCpxE066ISobXopwetdr0aH0qtsAYkmNhbSMOlVwvqJAgnuLYbTlNMIxZlkcaEjSN8B7UM3rw7kkxAFPHZ9kmkD104'
    transferData = TransferData(access_token)

    file_from=input("Enter the folder pat to transfer:")
    file_to='/test_dropbox'
    file=''
    for files in os.walk(file_from):
        file=files
    print(file)

    transferData.upload_File(file,file_to)
    print("file has sucessfully moved")

main()