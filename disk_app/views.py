from django.shortcuts import render
from django.http import HttpResponse
from .yadisk_api import get_public_resource
import zipfile
from io import BytesIO
import requests


def index(request):
    data = None
    items = []
    error = None

    if request.method == "POST" and "public_key" in request.POST:
        public_key = request.POST.get("public_key")

        if public_key:
            result = get_public_resource(public_key)
            print("API Response:", result)

            if "error" in result:
                error = result["error"]
            else:
                data = result
                raw_items = data.get("items", [])

                for item in raw_items:
                    mime_type = item.get("mime_type", "")
                    item["is_image"] = mime_type.startswith("image/")
                    item["is_video"] = mime_type.startswith("video/")
                    item["is_other"] = not (item["is_image"] or item["is_video"])
                    items.append(item)

            print("Processed Items:", items)
        else:
            error = "Пожалуйста, введите публичный ключ."

    return render(request, 'index.html', {"items": items, "error": error})


def download_selected_files(request):
    if request.method == "POST":
        selected_files = request.POST.getlist("selected_files")

        if not selected_files:
            return HttpResponse("Файлы не выбраны", status=400)

        buffer = BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zip_file:
            for file_url in selected_files:
                response = requests.get(file_url)
                if response.status_code == 200:
                    filename = file_url.split("/")[-1]
                    zip_file.writestr(filename, response.content)
                else:
                    return HttpResponse(f"Не удалось загрузить файл: {file_url}", status=400)

        buffer.seek(0)
        response = HttpResponse(buffer, content_type="application/zip")
        response["Content-Disposition"] = 'attachment; filename="selected_files.zip"'
        return response
