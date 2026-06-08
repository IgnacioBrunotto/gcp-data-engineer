import argparse
from google.cloud import storage


def main():
    parser = argparse.ArgumentParser(
        description="Create a GCP Storage Bucket"
    )

    parser.add_argument(
        "bucket_name",
        type=str,
        help="Name of the bucket to create"
    )

    parser.add_argument(
        "--project",
        required=True,
        help="Google Cloud Project ID"
    )

    parser.add_argument(
        "--location",
        default="us-central1",
        help="Bucket location (default: us-central1)"
    )

    args = parser.parse_args()

    print(f"Bucket name received: {args.bucket_name}")
    print(f"Project: {args.project}")
    print(f"Location: {args.location}")

    # Crear cliente para el proyecto especificado
    storage_client = storage.Client(
        project=args.project
    )

    bucket = storage_client.bucket(args.bucket_name)
    bucket.storage_class = "STANDARD"

    new_bucket = storage_client.create_bucket(
        bucket,
        location=args.location
    )

    print(
        f"Bucket '{new_bucket.name}' created "
        f"in project '{args.project}' "
        f"at location '{new_bucket.location}' "
        f"with class '{new_bucket.storage_class}'"
    )


if __name__ == "__main__":
    main()
 