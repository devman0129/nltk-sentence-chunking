import sys
import os

from langchain.text_splitter import NLTKTextSplitter

def get_file_content(file_path, file_name):
    try:
        with open(file_path+"/"+file_name, "r") as file:
            content = file.read()
            return content 
    except FileNotFoundError:
        print("File not found. Please check the file name and path.")
        sys.exit()

    except PermissionError:
        print("Permission denied. Please check the file permissions.")
        sys.exit()

    except Exception as e:
        print("An error occurred while reading the file:", str(e))
        sys.exit()

text = get_file_content("downloads", "test.txt")
text_splitter = NLTKTextSplitter(chunk_size=600, chunk_overlap=150)
docs = text_splitter.split_text(text)

print(len(docs))
for doc in docs:
    print("--------------------------------------")
    print(doc)