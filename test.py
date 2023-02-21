for file in dbutils.fs.ls("/"):
    print(file.path)