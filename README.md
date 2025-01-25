README.md:

# ClickHelper

**ClickHelper** is a Python-based utility tool designed to automate repetitive mouse-clicking tasks with user-defined intervals. It is ideal for situations where automated, periodic mouse clicks are needed, and it provides an easy way to manage and control the process.

---

## Features

- **Customizable Time Intervals**: Specify the time interval (in seconds) between mouse clicks.
- **Escape Key Control**: Exit the program by pressing the `Esc` key three times.
- **Click Counter**: Displays the total number of clicks performed during the session.
- **Cross-Platform Compatibility**: Works seamlessly on Windows (tested) and can be adapted for other platforms.
- **Executable Version**: Run without needing Python installed by using the provided executable file.

---

## Installation and Usage

### For Python Users

1. Clone the repository:
   ```bash
   git clone https://github.com/Akash-Dinkar-Bhujbal/ClickHelper.git
   cd ClickHelper
   ```
2. Install required dependencies:
   ```bash
   pip install pynput
   ```
3. Run the program:
   ```bash
   python main.py
   ```

### For Non-Python Users

1. Download the latest release from the [Releases](https://github.com/Akash-Dinkar-Bhujbal/ClickHelper/releases) page.
2. Extract the executable file and run it directly.

---

## How It Works

1. Start the program.
2. Enter the time interval (in seconds) between clicks when prompted.
3. The program will begin performing left mouse clicks at the specified interval.
4. To stop the program, press the `Esc` key three times.

---

## Repository Structure

```
ClickHelper/
├── V1/
│   ├── main.py           # Python script for the first version
├── V2/                   # Placeholder for future updates
├── README.md             # Project documentation
└── LICENSE               # License file
```

---

## Future Updates

- GUI for better user interaction.
- Support for right-click and double-click automation.
- Logging feature to track click history.
- Multilingual support.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built with [pynput](https://pypi.org/project/pynput/) for mouse and keyboard interaction.
- Inspired by the need for simple, customizable click automation.

---

## Disclaimer

This tool is provided "as is" without warranty of any kind. Use it responsibly and ensure it complies with the intended use cases and policies.
