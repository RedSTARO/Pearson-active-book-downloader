import os
import re
import fitz
import combain2pdf as t
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
           " AppleWebKit/537.36 (KHTML, like Gecko) "
           "Chrome/74.0.3729.169 Safari/537.36"}

# 替换文件名字符

print('Welcome to use this tool,this tool can help you download pearson active book easily.\n'
      'First,you should get a link which can download any page of book by using developer tool of your browser.\n'
      'Like this :\n'
      'If your link is "https://resources.pearsonactivelearn.com/r00/r0090/r009023/r00902341/current/OPS/images/9781292244778-001.jpg"\n'
      'Then,after deal,you should input link like this "https://resources.pearsonactivelearn.com/r00/r0090/r009023/r00902341/current/OPS/images/9781292244778"\n'
      'Easily understand,isn\'t ?\n'
      'Now  enjoy this tool!\n'
      '(This tool writen by RedSTAR.This tool will open source in Github.)\n' )

def new_name(title):
    # '/ \ : * ? " < > |'
    rstr = r"[\/\\\:\*\?\"\<\>\|\%\=\@\!\@\#\$\%\%\^\&\*\(\)\-\+\|\`\~]"
    new_doc_name = re.sub(rstr, "_", title)  # 替换为下划线
    return new_doc_name


# 获取文件扩展名
def get_file_extension(filename):
    arr = os.path.splitext(filename)
    return arr[len(arr) - 1]


img_path = ".\download\\"
doc = fitz.open()

for i in range(1,1001):
    num = str(i).rjust(3,'0')
    print(f"Continuous files downloader for pearson active book:task {num}")
    in_url = input("Please input link with out 001.jpg: ") + f"{str(num)}.jpg"
    print(in_url)

    doc_name = in_url.rsplit('/', 1)[1]
    doc_name = new_name(doc_name)
    doc_file = get_file_extension(doc_name)
    if len(doc_name) > 250:
        doc_name = "The file has been renamed,because original file namois too long. Now name:" + str(doc_file)
    try:
        response = requests.get(str(in_url), headers=headers)
        r = response.content
        if response.status_code != 200:
            print(f"Get {doc_name} failed.Download finish. Packing into pdf...")
            num_pdf = int(num)
            break
        else:
            with open(".\download\\" + str(doc_name), "wb") as f:
                print("Code:" + str(response.status_code))
                f.write(r)
    except requests.exceptions.ConnectionError:
        print(f"Download {doc_name} failed！Please confirm your input.")
    if response.status_code == 200:
        print(f"Download {doc_name} success！File is saved in path \"download\". \n")

t.img2pdf(doc_name.split('_')[0],num_pdf)
