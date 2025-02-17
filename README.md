Weather Notification System

Overview
This repository contains scripts for fetching weather data and sending notifications via email. It supports both Python and PowerShell implementations, allowing flexibility based on user preference.

Features
- Fetch Weather Data: Retrieves real-time weather information from an external API.
- Email Notifications: Sends weather updates via email to a predefined recipient.
- Cross-Platform: Available in both Python and PowerShell versions.

Prerequisites
- Python Requirements:
  - Python 3.x
  - Install dependencies using:
    ```bash
    pip install requests
    ```
- PowerShell Requirements:
  - Ensure PowerShell execution policy allows script execution.
  - Microsoft Outlook must be installed for email functionality.

Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/rBigChill/Weather.git
   ```
2. Update the script with your API key and email credentials.
3. Ensure required dependencies are installed.

Usage
- Python Script:
  ```bash
  python emailWeather.py
  ```
- PowerShell Script:
  ```powershell
  .\Email-Weather.ps1
  ```

Future Improvements
- Support for multiple weather data sources.
- Additional notification methods (SMS, push notifications).
- Enhanced logging and error handling.

License
This project is open-source and available for modification and distribution.
