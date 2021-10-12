1. Replace over the script MFA_NUMBER and USERNAME with yours

2. source the script

3. have already configured your MFA device manager

4. Run "$aws configure" and set your default aws_access_key_id, aws_secret_access_key, region and output type you will use

5. run the script with a single paramter as your mfa token

If everything is working as expected, you will receive an output like:

{
  "Credentials": {
    "AccessKeyId": "ASIAXXXXXXXXXXXXX",
    "SecretAccessKey": "Or8XXXXXXXXXXXXXXXXXXXXXX",
    "SessionToken": "IQoJb3JpZ2luX2VjEIv/////////(...)",
    "Expiration": "2021-10-12T22:49:04+00:00"
  }
}

The aws session will live only on your terminal where you run this script.

The token by default has an 1d period
