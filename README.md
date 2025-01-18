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

Requirement Analysis

Project Scope
Our primary objective was to develop a comprehensive Network Intrusion Detection System (NIDS) capable of identifying and mitigating potential security breaches within network traffic. This system aimed to provide:

- Real-time monitoring of network activity.
- Detection of anomalous behavior or potential intrusions.
- Analysis of identified threats to provide actionable insights.
- User-friendly access to analyzed data through a web interface.

Functional Requirements
1. Data Collection and Analysis:
    - Capability to capture and analyze network packets using Wireshark and Zeek (Zui).
    - Parsing and preprocessing of captured data to extract meaningful information.

2. Anomaly Detection:
    - Implementation of machine learning algorithms, specifically logistical regression, for anomaly detection.
    - Training the model on labeled datasets to recognize normal and anomalous network behavior.

3. Web Interface:
    - Development of a dynamic web platform to visualize analyzed data.
    - User-friendly functionalities allowing users to access analyzed data through the web interface.

Non-functional Requirements
1. Performance:
    - Real-time or near-real-time analysis of network traffic for prompt threat identification.
    - Scalability to handle varying data volumes without compromising system performance.

2. Security:
    - Ensuring the security of the NIDS system against potential attacks or unauthorized access.

3. User Experience:
    - Intuitive interface design allowing easy interaction for users with varying technical expertise.


System Design Considerations
1. Technological Stack:
    - Selection of appropriate tools and technologies including Python, HTML, CSS, JavaScript, and machine learning libraries.
  
2. Data Handling and Storage:
    - Efficient data processing and storage mechanisms to handle large volumes of network traffic data.

3. Compatibility and Integration:
    - Compatibility of the system with various operating environments and browsers for the web interface.







Implementation Details:
Control Flow Diagram:




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







Results and Outputs:
Brute Force Attack

Fig. 1.1: Word list used for brute force attack mylist.txt

Fig. 1.2: Brute force attack using Hydra on Kali Linux










Ftp attack using metasploitable

Fig 2.1: Nmap scan on target machine ‘Metasploitable’

Fig. 2.2:  Extensive Scan of target machine using Nmap.


Fig. 2.2: FTP attack using Hydra on Kali Linux

Fig. 2.3.1 – Nmap scan image-1 for FTP Attack

Fig. 2.3.2 – Nmap scan image-2 for FTP Attack

Fig. 2.3.3 – Nmap scan confirmation screen for FTP Attack

DNS ATTACK

Fig. 3.4 – DNS Attack using Hydra

Fig. 3.5.1 – DNS Attack data capture using Nmap Image-1

Fig. 3.5.2 – DNS Attack data capture using Nmap Image-2


HTTP ATTACK

Fig. 4.1 - HTTP Attack Modules

Fig. 4.2 – HTTP Attack Execution

Fig. 4.3 – HTTP Attack confirmation Screen


USING ZUI:
NORMAL DATA

Fig 5.1 – normal.pcapng packet feature construction using Zui (Brim)
BRUTE FORCE:

Fig 5.2 – brute_force_ubuntu.pcapng  packet feature construction using Zui (Brim)


FTP ATTACKS:

Fig 5.3 – ftp_attack.pcapng packet feature construction using Zui (Brim)
DNS ATTACK:

Fig 5.4 – dns_attack.pcapng packet feature construction using Zui (Brim)



HTTP ATTACK:

Fig 5.5 – http_attack.pcapng packet feature construction using Zui (Brim)

OUR WEBPAGE:
-HOME PAGE

Fig 6.1 – ML IDS WebApp Demo (Home Page)

Fig. 6.2 – Packet Data CSV file input Demonstration Image-1

Fig. 6.3 - Packet Data CSV file input Demonstration Image-2

-




RESULT PAGE

Fig 7.1 – ML IDS WebApp Demo (Results Page) Image-1 
(The above picture displays A Count VS Timestamp graph of Anomalous Data Captured by our Machine Learning Algorithm.)


Fig 7.2 – ML IDS WebApp Demo (Results Page) Image-2 (The above picture displays A Confusion Matrix Graph of our ML Algorithm along with the Analysis Report given below.)
Conclusion

The culmination of this project signifies the successful development and implementation of a robust Network Intrusion Detection System (NIDS). Through the meticulous execution of simulated attacks, data capture, and machine learning algorithms, we have achieved significant milestones in enhancing network security. The key takeaways from our endeavors are outlined below:

Key Achievements:

1. Attack Simulation and Data Capture:
   - Successfully executed brute force password cracking attacks, FTP attacks, and DNS attacks on simulated systems using Kali Linux and Metasploitable.
   - Employed Wireshark to capture and export network traffic data in pcap format.

2. Packet Segregation and Preprocessing:
   - Utilized Zui for effective packet segregation and organization, facilitating a streamlined dataset.
   - Merged segregated pcap files and conducted data cleaning, removing irrelevant columns with zero values.

3. Anomaly Detection and Classification:
   - Developed a comprehensive classification model using logistic regression to distinguish between anomalous and non-anomalous network behaviors.
   - Visualized the classification results through graphical representations, providing insights into network anomalies.

4. Machine Learning Application:
   - Applied logistic regression on the preprocessed dataset, achieving a commendable accuracy rate in identifying anomalous network activities.

Significance of Findings:
Our project's findings hold significance in the realm of cybersecurity, contributing to the ongoing efforts to fortify network defenses. By successfully simulating and identifying network intrusions, we have laid the foundation for proactive threat detection and mitigation.

Future Scope
The project opens avenues for further exploration and enhancement. Future endeavors could focus on the following aspects:

1. Real-Time Implementation:
   - Transition the system into a real-time network monitoring tool for instantaneous threat detection and response.

2. Integration of Advanced Machine Learning Techniques:
   - Explore the integration of more advanced machine learning algorithms to further improve anomaly detection accuracy.

3. Automation of Data Entry:
   - Develop mechanisms to automate the entry of Wireshark and Zeek data into the system, reducing manual intervention.

4. Extensive Testing Scenarios:
   - Expand the scope of simulated attacks and testing scenarios to enhance the system's robustness and adaptability.

5. User Interface Enhancement:
   - Improve the user interface of Zui for more intuitive packet segregation and analysis.

6. Collaboration with Industry Standards:
   - Align the NIDS system with industry standards and best practices to ensure compatibility and effectiveness in diverse network environments.

Overall Reflection
In conclusion, our project has not only achieved its objectives but has also laid the groundwork for future advancements in network security. The integration of attack simulations, data analysis, and machine learning showcases the project's multidimensional approach to addressing the complex challenges of network intrusion detection.
This report stands as a testament to our commitment to advancing the field of cybersecurity and contributing to the collective efforts aimed at safeguarding digital ecosystems from potential threats.
