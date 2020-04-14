#SMTP: Simple Mail Transfer Protocol

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import openpyxl

wb = openpyxl.load_workbook("result.xlsx")
sheet = wb.active
print("불러오기 성공")

for i in range(52,68):
    email = sheet['B' + str(i)].value
    result = sheet['C' + str(i)].value

    msg = MIMEMultipart()
    msg['Subject']='대흥동 이제마가 전해드리는 당신의 체질 결과.'

    if result == '태양인':
        text = MIMEText('안녕하세요! 코알라 유니브의 대흥동이제마 입니다. \n\n 코알라 해커톤을 통해 탄생한 온라인 이제마가 당신의 체질을 태양인으로 판별했습니다. \n\n 데이터 수집에 참여해주심에 감사하며 태양인에 해당하는 몇가지 도움될만한 정보(첨부파일참고)를 보내드립니다 :)')
        fp = open('taeyang_1.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(text)
        msg.attach(img)
    elif result == '소양인':
        text = MIMEText('안녕하세요! 코알라 유니브의 대흥동이제마 입니다. \n\n 코알라 해커톤을 통해 탄생한 온라인 이제마가 당신의 체질을 소양인으로 판별했습니다. \n\n 데이터 수집에 참여해주심에 감사하며 소양인에 해당하는 몇가지 도움될만한 정보(첨부파일참고)를 보내드립니다 :)')
        fp = open('soyang_1.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(text)
        msg.attach(img)
        fp = open('soyang_2.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
    elif result == '태음인':
        text = MIMEText('안녕하세요! 코알라 유니브의 대흥동이제마 입니다. \n\n코알라 해커톤을 통해 탄생한 온라인 이제마가 당신의 체질을 태음인으로 판별했습니다. \n\n 데이터 수집에 참여해주심에 감사하며 태음인에 해당하는 몇가지 도움될만한 정보(첨부파일참고)를 보내드립니다 :)')
        msg.attach(text)
        fp = open('taeum_1.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
        fp = open('taeum_2.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
    elif  result == '소음인':
        text = MIMEText('안녕하세요! 코알라 유니브의 대흥동이제마 입니다. \n\n 코알라 해커톤을 통해 탄생한 온라인 이제마가 당신의 체질을 소음인으로 판별했습니다. \n\n 데이터 수집에 참여해주심에 감사하며 소음인에 해당하는 몇가지 도움될만한 정보(첨부파일참고)를 보내드립니다 :)')
        msg.attach(text)
        fp = open('soum_1.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)


    # MIMEText: 메일을 보낼 때 메세지의 제목과 본문을 설정하기 위한 모듈

    #세션 생성
    s =smtplib.SMTP('64.233.184.108')

    #TLS 보안 시작
    s.starttls()

    #로그인 인증
    s.login('jeesoo8516@gmail.com','*****')


    #메일 보내기
    s.sendmail('jeesoo8516@gmail.com',email, msg.as_string())
    print(i, '번째', email, '에게 전송완료\n')

#세션 종료
s.quit()
