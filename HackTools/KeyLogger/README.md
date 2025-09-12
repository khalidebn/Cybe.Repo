# KeyLogger

A simple Python keylogger script that records keyboard input and saves it to a text file. This script uses the `pynput` library to listen for keypress events and logs each keystroke to a file called `keyfile.txt`.

## Features

- Captures all keyboard input.
- Appends each keystroke to a log file.
- Minimal and easy to use.

## Requirements

- Python 3.x
- [`pynput`](https://pypi.org/project/pynput/) library

Install `pynput` using pip if you haven't already:

```bash
pip install pynput
```

## Usage

1. **Clone the repository or copy the script file** to your local machine.

2. **Run the script:**

   ```bash
   python keylogger.py
   ```

3. The script will start listening for keyboard events. Each key pressed will be saved to a file named `keyfile.txt` in the same directory.

## How It Works

- The script listens for keyboard input using the `pynput.keyboard.Listener`.
- Every key pressed is printed in the console and written to `keyfile.txt`.
- The script attempts to extract the character from the key event. If it fails (e.g., for special keys), it prints an error message.

## Disclaimer

This script is for educational purposes only. Using keyloggers without consent is illegal and unethical. Always obtain proper authorization before running such software.

## License

MIT
