import boto3
import os

s3 = boto3.client('s3')

def list_buckets():
    response = s3.list_buckets()
    print("\nYour Buckets:")
    for bucket in response['Buckets']:
        print(f"  • {bucket['Name']}")

def create_bucket(bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created.")

def upload_file(bucket_name, file_path):
    filename = os.path.basename(file_path)
    s3.upload_file(file_path, bucket_name, filename)
    print(f"Uploaded '{filename}' to '{bucket_name}'.")

def download_file(bucket_name, filename, destination):
    s3.download_file(bucket_name, filename, destination)
    print(f"Downloaded '{filename}' to '{destination}'.")

def delete_object(bucket_name, filename):
    s3.delete_object(Bucket=bucket_name, Key=filename)
    print(f"Deleted '{filename}' from '{bucket_name}'.")

if __name__ == "__main__":
    while True:
        print("\n--- S3 Manager ---")
        print("1. List Buckets")
        print("2. Create Bucket")
        print("3. Upload File")
        print("4. Download File")
        print("5. Delete Object")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            list_buckets()

        elif choice == '2':
            bucket = input("Bucket name: ")
            create_bucket(bucket)

        elif choice == '3':
            bucket = input("Bucket name: ")
            path = input("Path to file: ")
            upload_file(bucket, path)

        elif choice == '4':
            bucket = input("Bucket name: ")
            filename = input("File to download: ")
            destination = input("Download to (path): ")
            download_file(bucket, filename, destination)

        elif choice == '5':
            bucket = input("Bucket name: ")
            filename = input("File to delete: ")
            delete_object(bucket, filename)

        elif choice == '6':
            break

        else:
            print("Invalid choice.")

