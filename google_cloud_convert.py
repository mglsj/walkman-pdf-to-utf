from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
from google.oauth2.service_account import Credentials
import io

# Path to your Google Cloud service account credentials JSON file
SERVICE_ACCOUNT_FILE = "credentials.json"

# Scopes for Google Drive API
SCOPES = ["https://www.googleapis.com/auth/drive"]

# Authenticate using service account
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build("drive", "v3", credentials=credentials)


def convert_pdf_to_google_doc(input_file_path, output_file_path):
    try:
        # Step 1: Upload the PDF and convert it to Google Doc format
        media = MediaIoBaseUpload(
            io.FileIO(input_file_path, "rb"), mimetype="application/pdf", resumable=True
        )
        converted_file = (
            drive_service.files()
            .create(
                media_body=media,
                fields="id",  # We retrieve only the file ID for temporary use
                body={
                    "mimeType": "application/vnd.google-apps.document"
                },  # Conversion to Google Doc
            )
            .execute()
        )

        file_id = converted_file.get("id")

        # Step 2: Export the converted Google Doc to a Word document
        request = drive_service.files().export_media(
            fileId=file_id,
            mimeType="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
        download_path = output_file_path
        with io.FileIO(download_path, "wb") as file:
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Download progress: {int(status.progress() * 100)}%")
        print(f"Converted file downloaded successfully: {download_path}")

        # Step 3: Delete the temporary file from Google Drive
        drive_service.files().delete(fileId=file_id).execute()
        print("Temporary file deleted from Google Drive.")

    except Exception as e:
        print(f"An error occurred: {e}")
