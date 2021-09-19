#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import sys, re, os

#setting into dictionary
def setting_into_dictionary(fd):
    pattern_value = re.compile("\"(.*?)\"")
    pattern_key = re.compile("^(.*):")
    dictionary = {}
    for i, line in enumerate(fd):
        value = re.search(pattern_value,line)[1]
        key = re.search(pattern_key, line)[1]
        dictionary[key] = value
    return (dictionary)

def render_f():
    if len(sys.argv) != 2:
        print("usage : render.py [files]")
        sys.exit(0)

    file_n = sys.argv[1]

    try:
        dictionary_setting = {}
        with open('setting.py', 'r') as setting_fd:
            dictionary_setting = setting_into_dictionary(setting_fd)

        #Create or open file html to write new entry
        new_line = ""
        if re.match("\w+.template", file_n):
            file = re.findall('\w+.', file_n)[0]
            with open(file+'html', "w+") as f, open(file_n, "r") as fd:
                for i, line in enumerate(fd):

                    key_to_place = re.search('\{(.*?)\}', line)[1]
                    if key_to_place in dictionary_setting:
                        new_line += re.sub('\{(.*?)\}', dictionary_setting[key_to_place],line)
                    else:
                        print('missing argument in setting for : '+ key_to_place)
                        new_line += line

                f.write(new_line)
    except FileNotFoundError as e:
        print("file {} not found".format(e.filename))
        sys.exit(0)
    except PermissionError as e:
        print("Permission denied in reading for {}".format(e.filename))
        sys.exit(0)
    except Exception as e:
        print("An error {}.".format(e))
        sys.exit(0)
    #create dictionary

    """
    # (?P<name>{name}) regexp find string
    # \{(.*?)\} find all caracter between {}
    list key word in template file
    with open(file_n, 'r') as fd:
        #open and read template file find {} value
        for i , line in enumerate(fd):
            for match in re.finditer('(?<=\{).+?(?=\})', line):
        content = fd.read()
        print(content)
        content_new = re.sub("(?P<name>{name})", "samuel", content)
        print(content_new)


        """

if __name__ == '__main__':
    render_f()
