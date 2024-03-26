# Hardware Info (hwinfo)

This is a Windows-only Python tool for gathering hardware information from a system using the Win32 Provider and Windows Management Instrumentation (WMI). It provides details such as CPU, memory, disk, and network information.

### Requirements
[>= Python 3.12.0](https://www.python.org/)

---
### Setup

`# pip install -r requirements.txt`

---
### Building

`# pyinstaller --noconfirm --onefile --console --name "hwinfo" --clean --hide-console "hide-early" --add-data "src/modules;modules" --add-data "src/utils.py;." "src/main.py"`

---
### Running

`# .\dist\hwinfo.exe`