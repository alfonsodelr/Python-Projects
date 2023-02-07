import re 

def main():
    txt = "sentence essay"
    reg = r"[a-zA-z]*e[a-zA-z]*|[a-zA-z]*E[a-zA-z]*"
    reg_1 = r"^[a-z][a-zA-Z\s]*\s$"
    split = r"\S+"
    testing = r"^s[a-z]*"

    split_arr = re.findall(split, txt)
    print(split_arr)
    filtered = []

    for i in range(0 , len(split_arr)):
        if(re.fullmatch(testing, split_arr[i])):
            filtered.append(split_arr[i])
    

    print(filtered)

main()