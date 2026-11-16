from pathlib import Path
import json


def import_document(file_path):
    path = Path(file_path)

    if path.suffix.lower() != ".txt":
        raise ValueError("This first prototype supports TXT files only.")

    text = path.read_text(encoding="utf-8")

    if not text.strip():
        raise ValueError("The document is empty.")

    document = {
        "document_id": "DOC-001",
        "source_filename": path.name,
        "original_text": text,
        "processing_status": "awaiting_extraction",
    }

    output_folder = Path("data")
    output_folder.mkdir(exist_ok=True)

    output_path = output_folder / "DOC-001.json"
    output_path.write_text(
        json.dumps(document, indent=2),
        encoding="utf-8",
    )

    return document


if __name__ == "__main__":
    try:
        document = import_document("sample_record.txt")
        print(f"Imported: {document['source_filename']}")
        print(f"Status: {document['processing_status']}")
        print("Saved document to data/DOC-001.json")
    except (OSError, ValueError) as error:
        print(f"Import failed: {error}")