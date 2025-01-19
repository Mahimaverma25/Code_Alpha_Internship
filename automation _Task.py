import os
import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup
import schedule
import time

# Organize files
def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            folder_name = os.path.join(directory, file_extension)
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            shutil.move(file_path, os.path.join(folder_name, filename))
            print(f"Moved {filename} to {folder_name}")

# Send email
def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, password):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Scrape stock price
def get_stock_price(stock_symbol):
    url = f"https://finance.yahoo.com/quote/{stock_symbol}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve data.")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    price_tag = soup.find('span', {'data-reactid': '32'})
    if price_tag:
        price = price_tag.text
        print(f"The current price of {stock_symbol} is {price}")
        return price
    else:
        print("Stock price not found.")
        return None

# Scheduled task example
def task_to_run():
    print("This task is running...")

schedule.every(5).seconds.do(task_to_run)

# Main function
def main():
    print("Task Automation Script Running...")

    # Organize files
    organize_files('/path/to/your/directory')
    
    # Send email
    send_email(
        sender_email="your_email@example.com", 
        receiver_email="receiver_email@example.com", 
        subject="Automated Email", 
        body="This is an automated message sent by a Python script.",
        smtp_server="smtp.gmail.com", 
        smtp_port=465, 
        password="your_email_password"
    )
    
    # Get stock price
    get_stock_price("AAPL")
    
    # Run scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

