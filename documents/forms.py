from django import forms

from .models import Document


class DocumentUploadForm(forms.ModelForm):

    class Meta:
        model = Document

        fields = [
            "title",
            "file",
        ]

    def clean_file(self):

        file = self.cleaned_data["file"]

        if not file.name.lower().endswith(".pdf"):
            raise forms.ValidationError(
                "Only PDF files are allowed."
            )

        if file.size > 20 * 1024 * 1024:
            raise forms.ValidationError(
                "PDF must be smaller than 20 MB."
            )

        return file