"""Connector and methods for accessing Amazon S3"""
import logging
import os
import boto3

class S3BucketConnector():
    """

    This is a class for interacting with S3 Buckets
    """
    def __init__(self, access_key: str, secret_key: str, endpoint_url: str, bucket: str):
        """
        Constructor for s3 bucket connector

        :param access_key is access key for accessing s3,
        :param secret_key is secret key for s3,
        :param endpoint_url is endpoint to s3,
        :param bucket is s3 bucket name
        """
        self._logger = logging.getLogger(__name__)
        self.endpoint_url = endpoint_url
        self.session = boto3.Session(aws_access_key_id = os.environ[access_key],
                                    aws_secret_access_key= os.environ[secret_key])
        self._s3 = self.session.resource(service_name='s3', endpoint_url=endpoint_url)
        self._bucket = self._s3.Bucket(bucket)

    def list_files_in_prefix(self, prefix: str):
        """
        listing all files with a prefix on the s3 bucket

        :param prefix: prefix on the S3 bucket that should be filtered

        :returns:
            files: list of all filenames containing the prefix in the key
        """
        files = [obj.key for obj in self._bucket.objects.filter(Prefix=prefix)]
        return files

    def read_csv_to_df(self):
        pass

    def write_df_to_s3(self):
        pass
