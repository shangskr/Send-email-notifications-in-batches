# Email Sender via GitHub Actions

这是一个使用 GitHub Actions 自动发送电子邮件的项目示例。通过将接收者的电子邮件地址存储在文本文件中，并使用 Python 脚本读取这些地址并发送邮件。


## 使用步骤

### 1. 克隆项目
### 2. 修改 email_addresses.txt 文件，每行写一个接收者的邮箱地址
### 3. 设置 GitHub Secrets
- 在 GitHub 仓库的 Settings -> Secrets and variables -> Actions 中添加以下 Secrets：
- SMTP_SERVER: 你的 SMTP 服务器地址
- EMAIL: 你的邮箱地址
- PASSWORD: 你的邮箱密码（SMTP服务应用码）
### 4. 修改邮件内容
- 在 send_emails.py 文件中修改邮件的标题和内容：
- subject = '你的邮件标题'  # 邮件标题
- body = '这是你的邮件内容'  # 邮件内容
### 5. 在send_emails.py 文件内容下
- 你可以修改SMTP服务器端口
- 从环境变量中获取邮箱服务器设置
- smtp_server = os.getenv('SMTP_SERVER')
- sender_email = os.getenv('EMAIL')
- password = os.getenv('PASSWORD')
- port = 587  # SMTP服务器端口
