import os
import sys
import re

# 判断一个unicode是否是汉字
def is_chinese(uchar):
    if '\u4e00' <= uchar<='\u9fff':
        return True
    else:
        return False

# 判断一个unicode是否是数字
def is_number(uchar):
    if '\u0030' <= uchar <='\u0039':
        return True
    else:
        return False

# 判断一个unicode是否是英文字母
def is_alphabet(uchar):
    if ('\u0041' <= uchar<='\u005a') or ('\u0061' <= uchar<='\u007a'):
        return True
    else:
        return False
def is_symbol(uchar):
    if ('\u0020' <= uchar <= '\u002F') or ('\u003A' <= uchar <= '\u0040') or ('\u005B' <= uchar <='\u0060') or ('\u007B'<= uchar <='\u007E'):
        return True
    else:
        return False

def is_pureLongNumAlpha(ustr):
    module = "[0-9a-z]{10,}"
    if re.sub(module, "", ustr) == "":
        return ""
    else:
        return ustr

# 判断是否非汉字，数字和英文字符and symbol
def is_other(uchar):
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar) or is_symbol(uchar)):
        return True
    else:
        return False

def strQ2B(ustring):
    ss = []
    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
                inside_code -= 65248
            rstring += chr(inside_code)
        ss.append(rstring)
    return "".join(ss)

def deleteSpecialCharacters(ustring):
    ss = []
    for s in ustring:
        rstring = ""
        for uchar in s:
            if is_other(uchar):
                pass
            else:
                ss.append(uchar)
    return "".join(ss)

def filterSymbols(ustring):
    pattern = '[\"\'\\\+`<\.!/_,#\$%^\*()~&;:\|\?<>@\[\]{}\-_=]+'
#line = re.sub("\W","",line)
    return re.sub(pattern, "", ustring)

'''
    delete some long numbers
'''
def filterLongNums(ustr):
    module = "[\d]{5,}"
    return re.sub(module, "", ustr)

def transform(filename, savefile):
    sf = open(savefile, "w")
    with open(filename, "r") as f:
        lines = f.readlines()
        if filename == "positive":
            for line in lines:
                contents = line.split('\t')
                line = strQ2B(contents[0])
                line = deleteSpecialCharacters(line)
                line = filterSymbols(line)
                line = line.lower()
                line = filterLongNums(line)
                line = is_pureLongNumAlpha(line)
                sf.write(line + "\t" +contents[1])
        else:
            for line in lines:
                line = strQ2B(line)
                line = deleteSpecialCharacters(line)
                line = filterSymbols(line)
                line = line.lower()
                line = filterLongNums(line)
                line = is_pureLongNumAlpha(line)
                sf.write(line + "\n")

if __name__ == '__main__':
    filename = sys.argv[1]
    savefile = sys.argv[2]
    transform(filename, savefile)
