# pdfff

PDF Form Filler

## Setup

```bash
virtualenv -p python3 pyenv
pyenv/bin/pip install -e .
mkdir test
pyenv/bin/pdfff
```

## Building a Windows executable

This assumes that you are running on Linux and building an executable via Wine.

```bash
wine pip.exe install pyinstaller
wine pip.exe install -e .
wine pyinstaller.exe pdfff.spec
```
