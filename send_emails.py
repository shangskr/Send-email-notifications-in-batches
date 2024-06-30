import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 从环境变量中获取邮箱服务器设置
smtp_server = os.getenv('SMTP_SERVER')
sender_email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
port = 587  # SMTP服务器端口

# 读取包含邮箱地址的文件
def read_email_addresses(file_path):
    with open(file_path, 'r') as file:
        email_addresses = [line.strip() for line in file]
    return email_addresses

# 发送邮件
def send_email(receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # 启动安全模式
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f'邮件已发送到 {receiver_email}')
    except Exception as e:
        print(f'无法发送邮件到 {receiver_email}. 错误: {e}')

# 主函数
def main():
    email_file = 'email_addresses.txt'  # 包含邮箱地址的文件路径
    subject = '你的邮件标题'  # 邮件标题
    body = '这是你的邮件内容'  # 邮件内容

    email_addresses = read_email_addresses(email_file)
    for email in email_addresses:
        send_email(email, subject, body)

if __name__ == '__main__':
    main()
