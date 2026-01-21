import setuptools as st

meta = {
    "name": "ptk-blinkfix",
    "version": "1.0.0",
    "author": "Ahmet Altin",
    "author_email": "me@ahmetaltin.com",
    "description": "Blinking cursor fix for Python prompt_toolkit apps",
    "long_description": open("README.md", "r", encoding="utf-8").read(),
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/ahmetaltin/ptk-blinkfix",
    "packages": st.find_packages(),
    "python_requires": ">=3.7",
    "install_requires": ["prompt_toolkit>=3.0.0"],
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
}

if __name__ == "__main__":
    st.setup(**meta)
