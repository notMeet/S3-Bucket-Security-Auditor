# S3-Bucket-Security-Auditor
CloudGuard S3 Auditor is a FastAPI-based application that scans AWS S3 buckets for public access to help secure data by identifying potential risks. The app is built using Python 3.10 and utilizes Boto3 to interact with AWS services. It is containerized with Docker for consistent deployment, and deployed on AWS ECS Fargate for serverless scaling. The app is automated using Terraform to manage cloud resources. Its primary objective is to ensure S3 buckets are properly secured by detecting and flagging any public access permissions.


## Technologies Used

#### Locally:

- Python 3.10: The core language used to build the application.
- FastAPI: A modern web framework for building RESTful APIs.
- Uvicorn: ASGI server to run the FastAPI application.
- Boto3: AWS SDK for Python, used to interact with AWS S3.
- Docker: To containerize the application for consistent deployment.
- AWS CLI: Configures AWS credentials and interacts with AWS services.

#### On the Cloud:

- Amazon S3: Used to store and manage data. The app scans S3 buckets for public access.
- Amazon ECR: Used to store Docker images for deployment.
- Amazon ECS Fargate: A serverless compute service for deploying containerized applications.
- IAM: Used for managing permissions and roles in AWS.
- Terraform: Automates the deployment of ECS clusters and other cloud resources.
