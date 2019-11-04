from boto3.session import Session

class SagemakerClient:

    def __init__(self):
        self.client = Session(profile_name="default").client("sagemaker", region_name="us-west-2")

    def create_model(self, model_data_url):

        model_params = {
            "ExecutionRoleArn": "arn:aws:iam::562998738767:role/dev-sagemaker", 
            "ModelName": "sample-model4",
            "PrimaryContainer": {
                "Image": "562998738767.dkr.ecr.us-west-2.amazonaws.com/test-sagemaker:latest",
                "ModelDataUrl": model_data_url
            }
        }

        self.client.create_model(**model_params)


if __name__ == '__main__':

    training_job_name = "sample-training18"

    client = Session(profile_name="default").client("sagemaker", region_name="us-west-2")
    model_data_url = client.describe_training_job(TrainingJobName=training_job_name)['ModelArtifacts']['S3ModelArtifacts']

    SagemakerClient().create_model(model_data_url)
