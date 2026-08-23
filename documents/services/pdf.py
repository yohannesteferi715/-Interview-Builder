import fitz


def extract_pdf_pages(file_path):

    pdf = fitz.open(file_path)

    pages = []

    try:

        for page_number, page in enumerate(pdf):

            text = page.get_text("text").strip()

            if not text:
                continue

            pages.append(
                {
                    "page": page_number + 1,
                    "text": text,
                }
            )

    finally:
        pdf.close()

    return pages