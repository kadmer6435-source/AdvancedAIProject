import os
import zipfile

# ZIP adı
zip_filename = "AdvancedAIProject.zip"

# Proje klasör yolu
project_folder = "AdvancedAIProject"

# ZIP oluştur
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_folder):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, project_folder)
            zipf.write(filepath, arcname)

print(f"ZIP dosyası oluşturuldu: {zip_filename}")
