from boto3.session import Session

class SagemakerClient:

    def __init__(self):
        self.client = Session(profile_name="default").client("sagemaker", region_name="us-west-2")

    def submit_training_job(self):
        training_params = {
            "TrainingJobName": "sample-training15",
            "HyperParameters": {
                'objective': 'multiclass',
                'num_class': '3'
            },
            "AlgorithmSpecification": {
                'TrainingImage': "562998738767.dkr.ecr.us-west-2.amazonaws.com/test-sagemaker:latest",
                'TrainingInputMode': 'File'
            },
            "RoleArn": "arn:aws:iam::562998738767:role/dev-sagemaker",
            "InputDataConfig": [
                {
                    'ChannelName': 'training',
                    'DataSource': {
                        'S3DataSource': {
                            'S3DataType': 'S3Prefix',
                            'S3Uri': "s3://test-ubuntu-sagemaker/input-data/iris5.csv"
                        }
                    }
                }
            ],
            "OutputDataConfig": {
                'S3OutputPath': "s3://test-ubuntu-sagemaker/output-data/"
            },
            "ResourceConfig": {
                'InstanceType': 'ml.m4.xlarge',
                'InstanceCount': 1,
                'VolumeSizeInGB': 10
            },
            "StoppingCondition": {
                'MaxRuntimeInSeconds': 60 * 60
            }
        }
        response = self.client.create_training_job(**training_params)
        print(response)

if __name__ == '__main__':
    SagemakerClient().submit_training_job()
