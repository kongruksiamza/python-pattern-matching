#Guard 
# สอบได้ 100 คะแนน -> คะแนนเต็ม
# สอบได้ 50 คะแนน -> สอบผ่าน
# สอบได้ 51-99 -> สอบผ่าน

score = int(input("ป้อนคะแนนสอบ : "))

match score:
    case 100 :
        print("คะแนนเต็ม")
    case 50 :
        print("สอบผ่าน")
    case score if score>50 and score<100:
        print("สอบผ่าน")
    case _ :
        print("ไม่ผ่านเกณฑ์การสอบวัดผล")
        