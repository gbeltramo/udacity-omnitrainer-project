# Setup

Make sure you have a terminal open in the starter kit folder.

## Create virtual environment and install dependencies

In the terminal, run:
```bash
uv sync --dev
```

## Install the app in edit mode
We install our app in edit mode so edits we do in the files are reflected
immediately in the installed app:

```bash
uv pip install -e .
```

## Set the virtual environment as interpreter for the project

In VS Code, hit Shift+Crtl+P (or Shift+Command+P on Mac) then select `Python:
Select Interpreter`.

Go to `Enter Interpreter Path` and then enter `.venv/bin/python`.

This will help you with syntax highlighting and other things.

## Configure credentials

Open a terminal at the root of the repo, and copy the `env.example` file to
`.env`:

```bash
cp env.example .env
```

then open .env and fill your API credential in GEMINI_API_KEY, as well as
make up a USER_API_KEY (anything works). You can use for example
`my-api-key`.

**NOTE**: this is obviously not secure, but it is here to remind you that a
real production app will need to have some authentication measure!
