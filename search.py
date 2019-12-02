from time import sleep
import re
import pandas as pd


fl = open("data", "r")
data = fl.read()
str_data = data

df = pd.read_csv("processed_data.csv")
processed_data = df["words"].tolist()



def search_it(word):
    rs = []

    wd = word.replace('"', "").replace("OR", "").replace("AND", "")
    counter = str_data.count(wd)
    pos = 0
    tmp = []

    if '"' in word:
        for count in range(counter):
            indx = str_data.find(wd, pos)
            pos += indx + len(wd)
            if indx not in tmp:
                tmp.append(indx)

        for indx in tmp:
            curr_wd = str_data[indx: (indx + len(wd))]
            # prev word
            prev_indx = indx - 2
            while str_data[prev_indx] != " ":
                prev_indx -= 1
                try:
                    temp = str_data[prev_indx]
                except:
                    break
            # next word
            next_indx = indx + len(wd) + 1
            while str_data[next_indx] != " ":
                next_indx += 1
                try:
                    temp = str_data[next_indx]
                except:
                    break

            rs.append(str_data[prev_indx: next_indx].strip())

        if not rs:
            if wd in processed_data:
                rs.append("YES")
            else:
                rs.append("NO")

    elif "OR" in word:
        wds = word.split("OR")
        flag = False
        for wd0 in wds:
            wd = wd0.strip()
            if wd in str_data or wd in processed_data:
                flag = flag or True
            else:
                flag = flag or False

        if flag:
            rs.append("YES")
        else:
            rs.append("NO")


    elif "AND" in word:
        wds = word.split("AND")
        flag = True
        for wd0 in wds:
            wd = wd0.strip()
            if wd in str_data or wd in processed_data:
                flag = flag and True
            else:
                flag = flag and False

        if flag:
            rs.append("YES")
        else:
            rs.append("NO")

    else:
        if wd in processed_data:
            rs.append("YES")
        else:
            rs.append("NO")

    return rs


def main():

    print("Developed by SMBH ;))")
    sleep(.5)
    print("enter 0 to exit the app...")
    sleep(.3)
    print("otherwise")

    # input loop breaks on 0
    while True:
        tmp = input("Search : ")
        if tmp == "0":
            break
        else:
            rs = search_it(tmp)
            for result in rs:
                print(result)




if __name__ == "__main__":
    main()

