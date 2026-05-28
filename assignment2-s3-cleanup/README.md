# AWS Lambda S3 Bucket Cleanup

## 📌 Overview
This project demonstrates how to use an AWS Lambda function with **Boto3** to automatically clean up old files in an S3 bucket.  
Objects older than **30 days** are deleted, while newer files remain untouched.

---

## ⚙️ Prerequisites
- AWS account with access to S3 and Lambda.
- IAM role with permissions:
  - `s3:ListBucket`
  - `s3:DeleteObject`
- Python 3.9 or 3.10 runtime for Lambda.
- An S3 bucket with test files uploaded.

---

## 🛠 Steps Taken

### 1. S3 Bucket Setup
- Created a new bucket: `lambda-s3-cleanup-demo`.

#### Creating bucket
![S3 Bucket creation](screenshots/s3-new-bucket-creation-process.png)

### Data uploaded to bucket
- Uploaded multiple files (PDFs, text files).
- Verified that all files show **Last modified** timestamps at upload time.
![S3 Bucket Data Uploaded](screenshots/s3-lambda-bucket-contents.png)

### 2. IAM Role Setup
- Created IAM role named **Lambda-S3-Cleanup**.
![Lambda IAM role creation](screenshots/s3-iam-role-name.png)

- Trusted entity: **Lambda**.
![Lambda IAM role creation](screenshots/s3-iam-role-trusted.png)

- Attached policy: **AmazonS3FullAccess** (for simplicity; in production, restrict to only required actions).
![Lambda IAM role permission](screenshots/s3-iam-role-permissions.png)

- IAM Role created successfully
![Lambda IAM role permission](screenshots/s3-iam-role-dashboard.png)


### 3. Lambda Function Creation
- Created Lambda function named **S3CleanupFunction**.
- Runtime: Python 3.9.
![Lambda Function creation](screenshots/s3-lambda-creation.png)

- Timeout: **30 seconds**.
- Memory: 128 MB.

![Lambda Function creation](screenshots/s3-lambda-timeout.png)


- Execution role: **Lambda-S3-Cleanup**.
![Lambda Function creation](screenshots/s3-lambda-execution-role-add.png)

### 4. Lambda Function Code
Code has been added.

![Lambda Function creation](screenshots/s3-lambda-function-add.png)

### 5. Lambda Function Test Code
Create lambda test case as below.

![Lambda Function test-case creation](screenshots/s3-lambda-testcase-create.png)


### 6. Lambda Function Test Result

Executed the code and the result should be as below.

![Lambda Function test-case creation](screenshots/s3-lambda-test-result.png)


