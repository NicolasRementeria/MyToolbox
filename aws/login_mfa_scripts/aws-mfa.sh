nodq() { sed 's/"//g'; }

aws-mfa()
{
    unset AWS_SESSION_TOKEN

    mfa_token=$1

    result=$(aws --output json sts get-session-token --serial-number arn:aws:iam::MFA_NUMBER:mfa/USERNAME --token-code $mfa_token)
    echo "$result" | jq .

    export AWS_ACCESS_KEY_ID=$(echo "$result" | jq ".Credentials.AccessKeyId" | nodq)
    echo "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID"

    export AWS_SECRET_ACCESS_KEY=$(echo "$result" | jq ".Credentials.SecretAccessKey" | nodq)
    echo "AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY"

    export AWS_SESSION_TOKEN=$(echo "$result" | jq ".Credentials.SessionToken" | nodq)
    echo "AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN"

    unset AWS_SECURITY_TOKEN
    unset AWS_PROFILE
}
