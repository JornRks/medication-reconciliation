def extract_medication(document):
    field_names = {
        "Medication": "name",
        "Dose": "dose",
        "Frequency": "frequency",
        "Status": "reported_status",
    }

    medication = {
        "name": None,
        "dose": None,
        "frequency": None,
        "reported_status": None,
        "source_document_id": document["document_id"],
        "source_filename": document["source_filename"],
        "review_status": "unreviewed",
    }

    for line in document["original_text"].splitlines():
        label, separator, value = line.partition(":")

        if separator and label.strip() in field_names:
            field = field_names[label.strip()]
            medication[field] = value.strip() or None

    if medication["name"] is None:
        raise ValueError("No medication name found.")

    medication["missing_fields"] = [
        field
        for field in ("dose", "frequency", "reported_status")
        if medication[field] is None
    ]

    return medication