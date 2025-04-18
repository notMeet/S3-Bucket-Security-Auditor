import boto3
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/scan")
def scan_buckets():
    s3 = boto3.client("s3")
    public_buckets = []

    buckets = s3.list_buckets()["Buckets"]
    for bucket in buckets:
        name = bucket["Name"]
        try:
            acl = s3.get_bucket_acl(Bucket=name)
            for grant in acl["Grants"]:
                grantee = grant.get("Grantee", {})
                if grantee.get("URI", "") == "http://acs.amazonaws.com/groups/global/AllUsers":
                    public_buckets.append({
                        "Bucket": name,
                        "Permission": grant["Permission"]
                    })
        except Exception as e:
            print(f"Could not check {name}: {e}")

    return {"public_buckets": public_buckets}
