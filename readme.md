# Walkman Chanikya to UTF-8 Converter

NCERT Hindi books are encoded in Walkman Chanikya font. This script converts the
text to UTF-8 encoding.

Steps to convert:

- pdf -> word (Using google drive api)
- process word file (Using python-docx)

Google drive api is used to convert pdf to word. The script uses the google
drive api, that is required to be enabled in the google cloud console

Processing assumes that the hindi text is in "Arial" font in docx, as it is the
default fallback (used by GDrive) when converting walkman pdf to docx.

> [!NOTE]
> If you don't have a google cloud account, you can manually convert the pdf to
> docx using google drive and then run the script. *requires modification in the
> main.py

## Google Cloud Console steps

- Enable Google Drive API
- Create a service account (or use existing)
- Download the credentials json file
- Copy it to project root and rename to `credentials.json`

## Usage

- Copy all pdfs to `input` folder

```bash
python main.py
```

or

```bash
python3 main.py
```
