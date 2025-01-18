Our project revolves around developing a robust Network Intrusion Detection System (NIDS) employing a multifaceted approach leveraging various technologies and methodologies prevalent in the field of cybersecurity and data analysis.

Cybersecurity Landscape
We delved into the extensive realm of cybersecurity, understanding the evolving threat landscape, and the critical necessity for efficient intrusion detection systems. This involved examining the historical context of cyber threats, their evolution, and the increasingly sophisticated methods employed by malicious entities.

 Tools and Platforms
Utilizing virtual machines, specifically Kali Linux and Metasploitable, we simulated network environments to mimic real-world scenarios. These environments facilitated the analysis of attack vectors, vulnerabilities, and various intrusion attempts.

Data Capture and Analysis
Tools like Wireshark and Zeek (formerly known as Bro) were instrumental in capturing and analyzing network traffic. They provided deep packet inspection capabilities, allowing us to dissect network packets, identify anomalies, and scrutinize communication patterns.

Machine Learning in Intrusion Detection
Leveraging machine learning concepts, particularly logistical regression, we aimed to develop an anomaly detection mechanism. This involved training models on labeled datasets to identify patterns and anomalies within network traffic.

Web Interface and Data Presentation
To democratize access to our system, we integrated the analyzed data into a user-friendly web interface. Combining Python for backend analysis, HTML, CSS, and JS modules for frontend design, we created a dynamic website. This platform allowed users to upload CSV files and receive comprehensive analyses and graphical representations of the data, making complex findings easily accessible.

This amalgamation of tools, technologies, and methodologies culminated in a sophisticated Network Intrusion Detection System designed to proactively detect, analyze, and mitigate potential security breaches.

Environment Setup

The project required specific software and operating systems for conducting simulated attacks, capturing network traffic, and analyzing data.

Operating Systems Used:
  Kali Linux: Employed for launching attacks using tools like Hydra.
  Metasploitable: Utilized to simulate vulnerable systems for attack scenarios.
  Ubuntu: Used as an additional environment for specific functionalities.

Attack Simulation

Brute Force Password Cracking
-Tool Used: Hydra on Kali Linux.
Procedure:
  - Hydra was configured to launch a brute force password cracking attack on target systems.
  - Specific configurations and parameters were set to execute the attack and record the network traffic.

FTP Attack Using Metasploit
- Tool Used: Metasploitable on Ubuntu.
- Procedure:
  - Utilized Metasploit to perform an FTP attack on simulated vulnerable systems.
  - The attack was conducted with predefined settings to generate relevant network traffic data.

DNS Attack
- Procedure:
  - A DNS attack was simulated to capture diverse network behaviors and traffic patterns.
  - Wireshark was employed to capture the resultant network packets.

Packet Capture and Segregation

Wireshark for Packet Capture
- Capture Process:
  - Wireshark was employed to capture network packets during the simulated attacks.
  - Captured data was exported in pcap file format for further analysis.

Zui for Packet Segregation
- Tool Used: Zui (Zed User Interface).
- Segregation Process:
  - Imported pcap files into Zui for packet segregation and analysis.
  - Facilitated filtering and sorting of captured packets for data organization.

Data Preprocessing

Merging and Cleaning
- Steps Taken:
  - Combined the segregated pcap files into a unified dataset for comprehensive analysis.
  - Removed columns with zero values to enhance data quality and relevance.

Data Classification
- Anomaly Identification:
  - Classified data into anomalous and non-anomalous categories based on predefined parameters.
  - Graphical representations were generated to visualize the distribution of anomalous and non-anomalous data points.

Machine Learning Model Application
- Algorithm Used: Logistic Regression.
- Steps:
  - Split the dataset into training and testing subsets for machine learning applications.
  - Applied logistic regression for anomaly detection and calculated its accuracy.
