# AWS Lambda Automation Assignments – HeroVired Training

## 📌 Overview
This repository contains four AWS Lambda automation assignments completed as part of the **HeroVired training program**.  
Each assignment demonstrates practical use of **AWS Lambda** with **Boto3** to automate infrastructure tasks, integrate with AWS services, and enforce operational efficiency.

---

## 📂 Repository Structure

```
aws-lambda-automation/
├── assignment1-ec2-instance-management/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
├── assignment2-s3-cleanup/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
├── assignment4-ebs-snapshot-cleanup/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
├── assignment6-billing-alerts/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
└── README.md 
```

---

## 📝 Assignments Summary

### 1. [EC2 Instance Management](ca://s?q=Explain_Assignment1_EC2_Instance_Management)
- **Objective:** Automate start/stop of EC2 instances using Lambda.  
- **Key Steps:**  
  - Created IAM role with EC2 permissions.  
  - Deployed Lambda function to manage EC2 lifecycle.  
  - Tested with manual triggers and EventBridge scheduling.  
- **Outcome:** Automated EC2 instance management with cost savings.

---

### 2. [S3 Bucket Cleanup](ca://s?q=Explain_Assignment2_S3_Cleanup)
- **Objective:** Delete files older than 30 days in an S3 bucket.  
- **Key Steps:**  
  - Created IAM role with S3 permissions.  
  - Deployed Lambda function to scan and delete old objects.  
  - Verified via CloudWatch Logs.  
- **Outcome:** Automated cleanup of aged S3 objects to optimize storage.

---

### 3. [EBS Snapshot and Cleanup](ca://s?q=Explain_Assignment4_EBS_Snapshot_Cleanup)
- **Objective:** Automate snapshot creation for EBS volumes and delete snapshots older than 30 days.  
- **Key Steps:**  
  - Created IAM role with EC2 snapshot permissions.  
  - Deployed Lambda function to create and clean snapshots.  
  - Verified via EC2 console and CloudWatch Logs.  
- **Outcome:** Reliable backup automation with cost control.

---

### 4. [Billing Alert via SNS](ca://s?q=Explain_Assignment6_Billing_Alert)
- **Objective:** Monitor AWS billing and send alerts when charges exceed a threshold.  
- **Key Steps:**  
  - Created SNS topic and confirmed email subscription.  
  - Created IAM role with CloudWatch + SNS permissions.  
  - Deployed Lambda function to fetch billing metrics and publish alerts.  
  - Tested with manual invocation and verified email alerts.  
- **Outcome:** Proactive billing monitoring with daily automation via EventBridge.

---

## 🧑‍🏫 Training Context
These assignments were conducted under the guidance of the **HeroVired trainer**, focusing on:
- Practical AWS Lambda use cases.  
- Integration with core AWS services (EC2, S3, EBS, CloudWatch, SNS).  
- Infrastructure automation and cost optimization.  
- Hands‑on learning with IAM roles, policies, and event triggers.  

---

## ✅ Outcomes
- Gained hands‑on experience with AWS Lambda and Boto3.  
- Built automation workflows for compute, storage, backup, and billing.  
- Learned IAM best practices for least‑privilege access.  
- Implemented monitoring and alerting for proactive cloud management.  

---

## 📸 Documentation
Each assignment folder contains:
- **README.md** → Detailed explanation of objectives, steps, and outcomes.  
- **lambda_function.py** → Python code using Boto3.  
- **screenshots/** → Visual proof of setup, configuration, and test results.  


---

## 🏷️ Credits
Assignments completed by **Prashanth Shetty** under **HeroVired AWS Lambda training program**.  
Trainer guidance ensured structured learning and practical application of cloud automation concepts.
