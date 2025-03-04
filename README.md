
# Automated Tests for Banking Project  

This repository contains automated tests for the Banking Project ([GlobalSQA](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login)) using **Python**, **Playwright** and **Pytest**.

## 🛠️ Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone <repo-url>
   cd <repo-folder>
  
2. **Install dependencies**  

   pip install -r requirements.txt

3. **Run Playwright installation (if not installed)**  

   playwright install


## 🚀 Running the Tests  

To execute all tests, run:  

pytest --headed --html=report.html --self-contained-html

This will generate an **HTML report (`report.html`)** for test results.

## 🏗️ Testing Approach  

### ✅ **Page Object Model (POM) Implementation**  
The project follows the **Page Object Model (POM)**, which enhances **scalability, maintainability, and reusability** of test cases. Each page is represented as a separate class containing reusable methods.

### 📌 **Test Cases Covered**  

1. **Login as Manager**  
   - Navigate to the banking portal.  
   - Login as Manager
  
1. **Add a Customer**    
   - Login as Manager.  
   - Enter customer data.
   - Add customer  

1. **Create Account**  
   - Login as Manager.  
   - Select a customer from the dropdown.  
   - Select currecny for the account.
   - Create account  

2. **Deposit Money**  
   - Login as a customer.  
   - Deposit a certain amount.  
   - Verify.  

3. **Withdraw Money**  
   - Login as a customer.  
   - Withdraw an amount.  
   - Ensure balance updates correctly.  

## 📁 Project Structure  

```
📂 tests/
   ├── test_Add_Customer.py
   ├── test_Create_Accout.py
   ├── test_Deposit.py
   ├── test_Login.py
   ├── test_Withdraw.py
📂 pages/
   ├── Login_Page.py
   ├── Customer_Page.py
   ├── Manager_Page.py
```

## ⚡ Technologies Used  
- **Python** 🐍  
- **Playwright** 🎭  
- **Pytest** 🧪  
- **Page Object Model (POM)**  
 
