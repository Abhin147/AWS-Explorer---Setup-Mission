import boto3


def main():
    # Get the list of AWS regions supported by the EC2 service
    regions = boto3.session.Session().get_available_regions("ec2")

    print("AWS Regions:")
    print("-" * 40)

    for region in regions:
        print(region)

    print("-" * 40)
    print(f"Total regions: {len(regions)}")

    print()
    print('"submitted_by": "abhinjgomez@mulearn"')


if __name__ == "__main__":
    main()