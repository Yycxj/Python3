import re #shell awk封装
import sys


class XAwk():
    def __init__(self,string):
        self.string: str = string 

    def re_line_awk(self,keyword,*re_index,re_split=",",strip=False):
        split_keyword: str = ""
        if isinstance (keyword, list):
            split_keyword = "|".join(keyword)
        elif isinstance (keyword, str):
            split_keyword = keyword
        else:
            print(f"re_line_awk keyword type:{type(keyword)} not support")
            sys.exit(2)

        line_cut = re.split(split_keyword, self, string)

        line_re_list: list = []
        for i in re_index:
            if i == 0:
                if strip:
                    line_re_list.append(self.string.strip())
                else:
                    line_re_list.append(self.string)
            else:
                if strip:
                    line_re_list.append(line_cut[i-1].strip())
                else:
                    line_re_list.append(line_cut[i-1])

        new_line = re_split.join(line_re_list)

        return(XAwk(new_line))

    def get(self):
        return self.string

    def re_line_grep(self, *key_word):
        key_word_str: str = "|".join(key_word)
        matched = re.search(key_word_str, self.string)

        if matched:
            return True
        else:
            return False 


def re_line_grep(s, key_word):
    searched = re.search(key_word, s)
    return searched


def re_file_grep(f_path, *s_key)     -> list:
    matched = ()
    key_word: str = "|".join(s_key)
    f_open = open(f_path)
    for line in f_open.readlines():
        match = re_line_grep(line, key_word)