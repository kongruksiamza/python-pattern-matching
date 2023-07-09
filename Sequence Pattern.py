#Sequence Pattern
list_number=[10,20,30]

match list_number:
    case []:
        print("ไม่มีข้อมูลใน List")
    case [10,20]:
        print("มีข้อมูล 2 รายการ")
    case [10,20,30]:
        print("มีข้อมูล 3 รายการ")