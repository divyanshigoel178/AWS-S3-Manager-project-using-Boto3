import streamlit as st
import boto3
import os

# Set up session
session = boto3.Session()
s3 = session.client("s3")

st.title("🗂️ AWS S3 Bucket Manager - Dashboard")

# List all buckets
buckets_response = s3.list_buckets()
bucket_names = [b['Name'] for b in buckets_response['Buckets']]

bucket = st.selectbox("Select an S3 Bucket", bucket_names)

if bucket:
    st.subheader(f"📂 Contents of Bucket: `{bucket}`")
    objects = s3.list_objects_v2(Bucket=bucket)
    if 'Contents' in objects:
        for obj in objects['Contents']:
            st.write(f"📄 {obj['Key']} ({obj['Size']} bytes)")
    else:
        st.write("✅ Bucket is empty.")

    # Upload a file
    st.subheader("📤 Upload a File")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        s3.upload_fileobj(uploaded_file, bucket, uploaded_file.name)
        st.success(f"✅ File `{uploaded_file.name}` uploaded successfully!")

    # Delete a file
    st.subheader("🗑️ Delete a File")
    delete_filename = st.text_input("Enter filename to delete")
    if st.button("Delete File"):
        try:
            s3.delete_object(Bucket=bucket, Key=delete_filename)
            st.success(f"✅ `{delete_filename}` deleted successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
