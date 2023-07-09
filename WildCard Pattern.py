#WildCard Pattern (default case)
# 1-> ถอนเงิน , 2->ฝากเงิน , 3->เปิดบัญชี , อื่นๆ -> หมายเลขไม่ถูกต้อง
service = int(input("ป้อนหมายเลขเพื่อใช้บริการ : "))

match service:
    case 1 : 
        print("ถอนเงิน")
    case 2 : 
        print("ฝากเงิน")
    case 3 : 
        print("เปิดบัญชี")
    case _ :
        print("หมายเลขไม่ถูกต้อง")