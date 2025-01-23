<H1>ML IDS WEB APP</H1>
<H2>Screenshots of our Project</H2>

![image copy](https://github.com/user-attachments/assets/baddc6c8-f91a-4af9-a53c-14e7ad50f4d3)
Fig 1: ML IDS WEB APP HOME PAGE

![image](https://github.com/user-attachments/assets/2a037131-9873-43f5-a94e-d7599938416e)
Fig 2.1: Packet data CSV file input demo image 1

![image (1)](https://github.com/user-attachments/assets/e7933380-4eb1-4562-b7d5-920bf4a6e2eb)
Fig 2.2: Packet data CSV file input demo image 2

![image (2)](https://github.com/user-attachments/assets/9e0fc529-706c-4e49-a2db-03c0c6bf9e9f)
Fig 3.1: ML IDS WebApp demo Image 1 (The above Data displays a Count VS Timestamp graph of anomalous data captured by our machine learning algorithm.)

![image (3)](https://github.com/user-attachments/assets/ed3f11a9-2630-4439-b611-67e4c445fadb)
Fig 3.2: ML IDS WebApp demo Image 2 (The above picture displays A Confusion Matrix Graph of our ML Algorithm along with the analysis report given below.)

<h2>ABOUT OUR PROJECT</h2>
Our project revolves around developing a robust Network Intrusion Detection System (NIDS) employing a multifaceted approach leveraging various technologies and methodologies prevalent in the field of cybersecurity and data analysis.<br><br>

<b>Cybersecurity Landscape</b>
We delved into the extensive realm of cybersecurity, understanding the evolving threat landscape, and the critical necessity for efficient intrusion detection systems. This involved examining the historical context of cyber threats, their evolution, and the increasingly sophisticated methods employed by malicious entities.

<b>Tools and Platforms:</b>
Utilizing virtual machines, specifically Kali Linux and Metasploitable, we simulated network environments to mimic real-world scenarios. These environments facilitated the analysis of attack vectors, vulnerabilities, and various intrusion attempts.

<b>Data Capture and Analysis:</b>
Tools like Wireshark and Zeek (formerly known as Bro) were instrumental in capturing and analyzing network traffic. They provided deep packet inspection capabilities, allowing us to dissect network packets, identify anomalies, and scrutinize communication patterns.

<b>Machine Learning in Intrusion Detection:</b>
Leveraging machine learning concepts, particularly logistical regression, we aimed to develop an anomaly detection mechanism. This involved training models on labeled datasets to identify patterns and anomalies within network traffic.

<b>Web Interface and Data Presentation:</b>
To democratize access to our system, we integrated the analyzed data into a user-friendly web interface. Combining Python for backend analysis, HTML, CSS, and JS modules for frontend design, we created a dynamic website. This platform allowed users to upload CSV files and receive comprehensive analyses and graphical representations of the data, making complex findings easily accessible.

This amalgamation of tools, technologies, and methodologies culminated in a sophisticated Network Intrusion Detection System designed to proactively detect, analyze, and mitigate potential security breaches.

<h2>Environment Setup</h2>

The project required specific software and operating systems for conducting simulated attacks, capturing network traffic, and analyzing data.

<h3>Operating Systems Used:</h3>
  Kali Linux: Employed for launching attacks using tools like Hydra.
  Metasploitable: Utilized to simulate vulnerable systems for attack scenarios.
  Ubuntu: Used as an additional environment for specific functionalities.

<h2>Attack Simulation</h2>

<b>Brute Force Password Cracking</b>
-Tool Used: Hydra on Kali Linux.
<b>Procedure:</b>
  - Hydra was configured to launch a brute force password cracking attack on target systems.
  - Specific configurations and parameters were set to execute the attack and record the network traffic.

<b>FTP Attack Using Metasploit</b>
- Tool Used: Metasploitable on Ubuntu.
- <b>Procedure:</b>
  - Utilized Metasploit to perform an FTP attack on simulated vulnerable systems.
  - The attack was conducted with predefined settings to generate relevant network traffic data.

<b>DNS Attack</b>
- <b>Procedure:</b>
  - A DNS attack was simulated to capture diverse network behaviors and traffic patterns.
  - Wireshark was employed to capture the resultant network packets.

<h2>Packet Capture and Segregation</h2>

<b>Wireshark for Packet Capture</b>
- <b>Capture Process:</b>
  - Wireshark was employed to capture network packets during the simulated attacks.
  - Captured data was exported in pcap file format for further analysis.

<b>Zui for Packet Segregation</b>
- <b>Tool Used:</b> Zui (Zed User Interface).
- <b>Segregation Process:</b>
  - Imported pcap files into Zui for packet segregation and analysis.
  - Facilitated filtering and sorting of captured packets for data organization.

<h2>Data Preprocessing</h2>

<b>Merging and Cleaning</b>

- <b>Steps Taken:</b>
  - Combined the segregated pcap files into a unified dataset for comprehensive analysis.
  - Removed columns with zero values to enhance data quality and relevance.

<b>Data Classification</b>
- <b>Anomaly Identification:</b>
  - Classified data into anomalous and non-anomalous categories based on predefined parameters.
  - Graphical representations were generated to visualize the distribution of anomalous and non-anomalous data points.

<h2>Machine Learning Model Application</h2>
- <b>Algorithm Used:</b> Logistic Regression.

- <b>Steps:</b>
  - Split the dataset into training and testing subsets for machine learning applications.
  - Applied logistic regression for anomaly detection and calculated its accuracy.
