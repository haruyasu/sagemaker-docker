from boto3.session import Session

class SagemakerClient:

    def __init__(self):
        self.client = Session(profile_name="default").client("sagemaker", region_name="us-west-2")

    def submit_transform_job(self):

        model_name = self.client.list_models(
            NameContains="sample-model",
            SortOrder='Descending',
            SortBy='CreationTime')["Models"][0]["ModelName"]

        transform_params = {
            "TransformJobName": "sample-transform2",
            "ModelName": model_name,
            "MaxConcurrentTransforms": 2,
            "MaxPayloadInMB": 50,
            "BatchStrategy": "MultiRecord",
            "TransformOutput": {
                "S3OutputPath": "s3://test-ubuntu-sagemaker/output-data-prediction/"
            },
            "TransformInput": {
                "DataSource": {
                    "S3DataSource": {
                        "S3DataType": "S3Prefix",
                        "S3Uri": "s3://test-ubuntu-sagemaker/input-data-prediction/"
                    }
                },
                "ContentType": "text/csv",
                "SplitType": "Line"
            },
            "TransformResources": {
                "InstanceType": "ml.c4.xlarge",
                "InstanceCount": 1
            }
        }

        self.client.create_transform_job(**transform_params)

if __name__ == '__main__':
    SagemakerClient().submit_transform_job()
