#Capture Pattern
service = int(input("ป้อนหมายเลขเพื่อใช้บริการ : "))

match service:
    case 1 : 
        print("ถอนเงิน")
    case 2 : 
        print("ฝากเงิน")
    case 3 : 
        print("เปิดบัญชี")
    case service :
        print(f"ไม่มีบริการหมายเลข {service} ในระบบ โปรดทำรายการใหม่อีกครั้ง")