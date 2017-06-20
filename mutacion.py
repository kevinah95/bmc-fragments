def insert_sequence(str1, str2, index):
    str1_split1 = str1[:index]
    str1_split2 = str1[index:]
    new_string = str1_split1 + str2 + str1_split2
    return new_string


print(insert_sequence('CCGG', 'AT', 2))
