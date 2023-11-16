TruTraks API Python Script

Overview
This Python script connects to the TruTraks API to retrieve vehicle tracking data and exports it to a CSV file. The purpose of this script is to facilitate the extraction of TruTraks tracking information into a format compatible with Power BI for further analysis.

Note: This script is a work in progress. While it successfully connects to the TruTraks API and pulls the required data into a CSV file, there is an ongoing effort to enhance its functionality. Specifically, the script currently lacks a graceful stopping mechanism. To terminate the script, it is necessary to manually kill the terminal process. Further updates will address this limitation and provide a more user-friendly stop mechanism.

Features
Data Retrieval: Connects to the TruTraks API to fetch real-time tracking data.
CSV Export: Transforms the retrieved data into a CSV format, making it compatible with Power BI.
Easy Integration: Designed for seamless integration with Power BI for comprehensive data analysis.
