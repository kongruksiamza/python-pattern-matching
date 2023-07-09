#OR Pattern | 
# 0-5 -> 0,2,4 คู่ , 1,3,5 -> คี่
number = int(input("ป้อนตัวเลข (0-11): "))

match number:
    case 0|2|4|6|8|10:
        print("เลขคู่")
    case 1|3|5|7|9|11: 
        print("เลขคี่")