# Sagemaker bring your Docker

## Using your Docker
1. docker build -t test-sagemaker .
2. docker tag test-sagemaker:latest 123.dkr.ecr.us-west-2.amazonaws.com/test-sagemaker:latest
3. docker push 123.dkr.ecr.us-west-2.amazonaws.com/test-sagemaker:latest
4. python submit_training_job.py
5. python create_model.py
6. python submit_transform_job.py
