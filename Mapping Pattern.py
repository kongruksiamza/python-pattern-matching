#Mapping Pattern
product={"name":"เมาส์","price":1500,"category":"อุปกรณ์ไอที"}

match product:
    case {"category":"แฟชั่น"}:
        print("ได้รับส่วนลด 50%")
    case _ :
        print("สินค้าดังกล่าวไม่มีส่วนลด")