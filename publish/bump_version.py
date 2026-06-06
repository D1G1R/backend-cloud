import sys
import os

if len(sys.argv) > 1:
    new_version = sys.argv[1]
    # Kök dizindeki VERSION dosyasının yolunu belirliyoruz
    version_file_path = os.path.join(os.path.dirname(__file__), "..", "VERSION")

    with open(version_file_path, "w") as f:
        f.write(new_version)
    print(f"Versiyon güncellendi: {new_version}")
else:
    print("Versiyon numarası sağlanmadı!")
