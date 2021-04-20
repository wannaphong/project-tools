import glob, os

def readcode(file):
    with open(file, 'r', encoding='utf-8-sig') as f:
        return f.read()

list_filecode = list(glob.glob('./source/*.*'))
#print(list_filecode)
list_code = [readcode(i) for i in list_filecode]
files = """
""".splitlines()
#files = [i.strip() for i in files]
#print(files)
import html
dict_code = [{'file':os.path.basename(i),'code':html.escape(j),'num':'2.2.'+str(list_code.index(j)+1)} for i,j in zip(list_filecode, list_code)]# if os.path.basename(i) in files]
#print(dict_code)
def get_data():
    return dict_code