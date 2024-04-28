# WebApp Creator Tool
Provides you a graphical user interface to create webapps in a simple way.

## Install - Windows
- Make sure you have Python 3.10 or greater installed
- Clone this repository to your system and open a Powershell terminal inside of it
- Use `pip install -r requirements.txt` to install all requirements
- Run `python main.py` to run WebApp Creator

## Supported languages
The default software language is english, but it supports more languages. To change the software language, edit the `preferences.json` file and set the language value to your language code.

Currently, the interface supports:
```
ptbr - Brazilian Portuguese
eng  - English
hiin - Hindi
zhcn - Mandarin
rus  - Russian
es   - Spanish
ar   - Arabian
jp   - Japanese
kr   - Korean
du   - Dutch
```

Most of the translations were made with artificial intelligence. If you are a native speaker and would like to improve it, feel free to open an issue.

### Example of how to load brazilian portuguese language:
- Edit preferences.json:
  `{ "language": "ptbr" }`
- Save and restart WebApp Creator

## TODO:
- Firefox currently not working
- Manual icon choose not implemented yet
- Some code cleaning

## This app is Windows only
If you would like to use a WebApp Creator in Linux, use [this](https://github.com/linuxmint/webapp-manager) alternative.
