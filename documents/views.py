from django.shortcuts import redirect, render

from .forms import DocumentUploadForm
from .services.ingestion import ingest_document


def upload_document(request):

    if request.method == "POST":

        form = DocumentUploadForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            document = form.save()

            ingest_document(document)
            return redirect(
                "documents:upload_success"
            )


    else:

        form = DocumentUploadForm()

    return render(
        request,
        "documents/upload.html",
        {
            "form": form,
        },
    )
    
    
def upload_success(request):

    return render(
        request,
        "documents/success.html",
    )