"""
KrishiMitra — Language Setup Script
Run this ONCE before starting the app to download Tamil and Hindi translation packages.
Usage: python setup_languages.py
"""

import argostranslate.package

LANGUAGES = ["ta", "hi"]  # Tamil and Hindi

print("🌍 Updating Argos Translate package index...")
argostranslate.package.update_package_index()

available_packages = argostranslate.package.get_available_packages()

for pkg in available_packages:
    if pkg.from_code == "en" and pkg.to_code in LANGUAGES:
        print(f"📥 Downloading: English → {pkg.to_code} ({pkg.to_name})...")
        download_path = pkg.download()
        argostranslate.package.install_from_path(download_path)
        print(f"✅ Installed: English → {pkg.to_name}")

print("\n🎉 Language setup complete! You can now run: streamlit run app.py")
