import os



root=os.getcwd()

if(root.endswith("versions")):

	upload_folder_path=os.path.join(os.getcwd(), "..", "..", "VersionsRecord", "file")
else:

	upload_folder_path=os.path.join(os.getcwd(),"file")

print("config "+os.name+" "+"path: "+os.getcwd()+" "+"root: "+root)