# A simple wrapper for OpenAI's chat API

## Requirements:

* Python modules specified in `requirements.txt`
* glow (optional, for markdown rendering)

## API key

Please use your own OpenAI API key.

You can either set the environment variables 
`OPENAI_API_KEY` and `OPENAI_ORGANIZATION`,
or explicitly set `openai.api_key` and `openai.organization`
in api.py

## Usage

Simply, just type
```bash
python main.py
```

For installation, use

```bash
pyinstaller -F main.py
```

The executable will appear in `dist/`. It's recommended that you create
a new venv to minimize binary size.


