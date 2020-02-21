---
title: "Digital forensics Notes"
date: 2020-03-20 08:00:00
updated: 2020-03-25 10:09:33
tags: ["Notes","Study"]
---

Prescribed textbook: André Årnes, Digital Forensic, Wiley; 1 edition (July 24, 2017)

Session 1: Introduction of Digital Forensics

1. Introduction - Andre Arnes
   1. History
   2. Locard's Exchange Principle
   3. Crime Reconstruction
   4. Ivestigations
   5. Evidence Dynamics
   6. Layers of Abstraction
   7. Metadata
   8. Online Bank Fraud
      1. Modus Operandi
      2. The SpyEye Case
2. The Digital Forensics Process - Anders O. Flaglien
   1. Principles of a Forensics Process
   2. Finding the Digital Evidence
   3. The Identification Phase
      1. Preparations and Deployment of Tools and Resources
      2. The First Responder
      3. At the Scene of the Incident
      4. Dealing with Live and Dead Systems
      5. Chain of Custody
   4. The Collection Phase
      1. Sources of Digital Evidence
      2. Systems Physically Tied to a Location
      3. Multiple Evidence Sources
      4. Reconstruction
      5. Evidence Integrity
      6. Dual-Tool Verification
      7. Remote Acquisition
      8. External Competency and Forensics Cooperation
   5. The Examination Phase
      1. Initial Data Source Examination and Preprocessing
      2. Forensic File Formats and Structures
      3. Data Reduction and Filtering
      4. Timestamps
      5. Compression, Encryption and Obfuscation
      6. Data and File Carving
      7. Automation
   6. The Analysis Phase
      1. Layers of Abstraction
      2. Evidence Types
      3. String and Keyword Searches
      4. Anti-Forensics
         1. Computer Media Wiping
         2. Analysis of Encrypted and Obfuscated Data
      5. Automated Analysis
      6. Timelining of Events
      7. Graphs and Visual Representaitons
      8. Link Analysis
   7. The Presentation Phase
      1. The Final Reports
      2. Presentation of Evidence and Work Conducted
      3. The Chain of Custody Circle Closes

Session 2-4: Traditional Digital Forensics Investigation

1. Cybercrime Law - Inger Marie Sunde
   1. The International Legal Framework of Cybercrime Law
      1. The International Involved in Criminal Activity and in Crime-Prevention Initiatives
      2. The National Legal System Versus the International legal Framework
      3. Fundamental Rights Relating to Cybercrime Law - The ECHR
         1. The ECtHR as a Driving Force for Development of Human Rights
         2. The Right to Bring a Case before the ECtHR
         3. A Special Note on Transborder Search and the rule of Law
         4. The Connection between Fundamental Rights and the Rule of Law
         5. The Principle of Legality in the Context of Crime
         6. The Principle of Legality in the Context of a Criminal Investigation
         7. The Positive Obligation of the Nation State
         8. The Right to Fair Trial
         9. A Special Note on Evidence Rules in Different Legal Systems
         10. Possible Outcomes of a Violation of Fundamental Rights
      4. Special Legal Framework: The Cybercrime Convention
      5. Interpretation of Cybercrime Law
         1. Interpretation of Substantive Criminal Law
         2. Application of Old Criminal Provisions to New Modes of Conduct
         3. Interpretation of Procedural Procedural Provisions Authorizing Coersive Measures
   2. Digital Crime - Substantive Criminal Law
       1. General Conditions for Criminal Liability
       2. Real-Life Modus Operandi
       3. Offenses against the Confidentiality, Integrity, and Availability of Computer Data and Systems
           1. Illegal Access and Illegal Interception
           2. Data and System Interference
           3. Misuse of Devices
       4. Computer-Related Offenses
       5. Content-Related Offenses
       6. Offenses Related to Infringements of Copyright and Related Rights
       7. Racist and Xenophobic Speech
   3. Investigation Methods for Collecting Digital Evidence
      1. The Digital Forensic Process in the Context of Criminal Procedure
      2. Computer Data That Are Publicly Available
         1. Transborder Access to Stored Computer Data Where Publicly Available
         2. Online Undercover Operations
      3. Scope and Safeguards fo the Investigation Methods
         1. Suspicion-Based Investigation Methods
         2. The Scope of the Investigation Methods
         3. Conditions and Safeguards
         4. Considerations Relating to Third Parties
      4. Search and Seizure
         1. Main Rules
         2. Special Issues
      5. Production Order
      6. Expedited Preservation and Partial Disclosure of Traffic Data
         1. Real-Time Investigation Methods
   4. International Cooperation in Order to Collect Digital Evidence
      1. Narowing the Focus
      2. A Special Note on Transborder Access to Digital Evidence
      3. Mutual Legal Assistance
         1. Basic Principles and Formal steps of the procedure
         2. International Police Cooperation and Joint Investigation
2. Digital Forensic Readiness - Ausra Dilijonaite
   1. Definition
   2. Law Enforcement versus Enterprise Digital Forensic Readiness
   3. Why? A Rationale for Difital Forensic Readiness
      1. Cost
      2. Usefulness of Digital Evidence
         1. Existence of Digital Evidence
         2. Evidentiary Weight of Digital Evidence
   4. Frameworks, Standards, and Methodologies
      1. Standards
         1. ISO/IEC 27037
         2. ISO/IEC 17025
         3. NIST SP 800-86
      2. Guidelines
         1. IOCE Guidelines
         2. Scientific Working Group on Digital Evidence (SWGDE)
         3. ENFSI Guidelines
      3. Research
         1. Rowlingson's Ten-step Process
         2. Grobler et al.'s Forensic Readiness Framework
         3. Endicott-Popovsky et al.'s Forensic Readiness Framework
   5. Becoming "Digital Forensic" Ready
   6. Enterprise Digital Forensic Readiness
      1. Legal Aspects
      2. Policy, Processes, and Procedures
      3. People
      4. Technology: Digital Forensic Laboratory
      5. Technology: Tools and Infrastructure
      6. Outsourcing Digital Forensic Capabilities
   7. Considerations for Law Enforcement
3. Computer Forensics - Jeff Hamm
   1. Evidence Collection
      1. Data Acquisition
         1. Live Data
         2. Forensic
      2. Forensic Copy
   2. Examination
      1. Disk Structures
      2. File Systems
   3. Analysis
      1. Analysis Tools
      2. Timeline Analysis
      3. File Hashing
      4. Filtering
      5. Data Carving

Session 5: Network Forensics Investigation
Internet Forensics

1. 
2. 
3. 
4. 
5. Tracing Information on the Internet
   1. DNS and Reverse DNS
   2. Whois and Reverse Whois
   3. Ping and Port Scan
   4. Traceroute
   5. IP Geolocation
   6. Tracing BitTorrent Peers
   7. Bitcoin Unconfirmed Transaction Tracing
6. Collection Phase - Local Acquisition
   1. Server: Server Logs, Web Application Logs, Virtual Hosts
   2. Cloud Services
   3. Open Sources
7. Other Considerations
   1. APIs
   2. Integrity of Remote Artifacts
8. The Examination and Analysis Phases

Session 6: Live and Memory Forensics Investigation

Session 7: Mobile Forensics Investigation
Mobile and Embedded Forensics - Jens-Petter Sandvik

1. Introduction
   1. Embedded Systems and Consumer Electronics
   2. Mobile Phone
   3. Telecommunication Networks
   4. Mobile Devices and Embedded Systems as Evidence
   5. Malware and Security Considerations

Session 8-9: Practical Exercise
Educational Guide - Stefan Axelsson

Session 10: Big Data Forensics
Challenges in Digital Forensics - Katrin Franke and Andre Arnes

1. Computational Forensics
2. Automation and Standardization
3. Research Agenda
