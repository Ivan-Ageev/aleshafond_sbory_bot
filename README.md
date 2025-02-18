# **Telegram Bot for Monitoring Charity Fund Statuses**

🤖 This Python script is designed to monitor the status of children's fundraising campaigns on the **Alyosha Foundation** website and send notifications via Telegram when a campaign is closed. It uses web scraping, asynchronous programming, and a scheduler to periodically check for updates.

---

## **Features**

- **Web Scraping:** Fetches data from the Alyosha Foundation website to track the status of fundraising campaigns for children.  
- **Telegram Notifications:** Sends real-time notifications to a specified Telegram chat when a campaign is closed.  
- **Scheduled Checks:** Automatically checks the website every minute for updates.  
- **Avoids Duplicates:** Keeps track of processed campaigns to avoid sending duplicate notifications.  

---

## **How It Works**

1. **Web Scraping:**  
   - The script uses `BeautifulSoup` to parse the Alyosha Foundation's "Children" page (`https://aleshafond.ru/children`).  
   - It extracts the names of children and the status of their fundraising campaigns.  

2. **Notification Logic:**  
   - If a campaign is marked as "Сбор закрыт" (Collection Closed), the script sends a notification to a specified Telegram chat.  
   - The script ensures that each child is only notified once by storing processed names in a set.  

3. **Scheduling:**  
   - The script uses `APScheduler` to run the check every minute.  

---

## **Setup Instructions**

### **1. Install Dependencies**
Make sure you have the required Python libraries installed:
```bash
pip install beautifulsoup4 requests python-telegram-bot apscheduler
```

### **2. Configure the Script**
- Replace the `TOKEN` variable with your Telegram bot token.  
- Replace the `CHAT_ID` variable with the ID of the Telegram chat where notifications should be sent.  

### **3. Run the Script**
Execute the script using Python:
```bash
python script_name.py
```

---

## **Code Structure**

### **Key Functions**
- **`send_notification(name, message)`**:  
  Sends a notification to the specified Telegram chat.  
  - `name`: The name of the child.  
  - `message`: The status message (e.g., "Сбор закрыт").  

- **`check_funds()`**:  
  Scrapes the Alyosha Foundation website, checks the status of each child's campaign, and sends notifications if a campaign is closed.  

- **`main()`**:  
  Wrapper function to run `check_funds()` asynchronously.  

- **`check_statuses()`**:  
  Calls `main()` using `asyncio.run()` to handle asynchronous execution.  

### **Scheduler**
- The script uses `BlockingScheduler` from `APScheduler` to run `check_statuses()` every minute.  

---

## **Environment Variables**
- **`TOKEN`**: Your Telegram bot token.  
- **`CHAT_ID`**: The ID of the Telegram chat where notifications will be sent.  

---

## **Example Notification**
When a campaign is closed, the bot sends a message in the following format:
```
Иван Иванов | Сбор закрыт
```

---

## **Dependencies**
- `beautifulsoup4`: For parsing HTML content.  
- `requests`: For making HTTP requests to the Alyosha Foundation website.  
- `python-telegram-bot`: For sending notifications via Telegram.  
- `apscheduler`: For scheduling periodic checks.  

---

## **License**
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).  

---
