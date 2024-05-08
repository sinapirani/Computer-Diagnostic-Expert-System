
# Computer Diagnostic Expert System

Welcome to the Computer Diagnostic Expert System, a Python application designed to help diagnose and suggest solutions for common computer issues. This application utilizes the Experta framework, a powerful tool for developing expert systems with rules-based logic in Python.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the Computer Diagnostic Expert System, follow these steps to install the necessary environment and libraries:

1. Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the Experta library using pip:
   ```bash
   pip install experta
   ```

## Usage

To run the expert system, execute the following command in your terminal:

```bash
python diagnostic_system.py
```

Follow the on-screen prompts and answer yes/no questions to receive a diagnosis for the computer issue.

## How It Works

The system initiates by loading initial facts and rules:
- **Initial Facts**: Determines the starting point of the diagnosis, asking if the computer turns on.
- **Rules**: A set of conditions that guide the diagnostic process based on user inputs.

### Diagnostic Process

1. **Power Check**: Determines if the computer can turn on.
2. **Display Check**: Checks if the display outputs correctly.
3. **Boot Check**: Verifies if the system boots up to the operating system.
4. **Software Check**: Identifies any software-related issues that might cause crashes or errors.

Based on responses, the system uses rules to infer problems and suggest troubleshooting steps or solutions.

## Contributing

Interested in contributing? Great! You can contribute in several ways:
- Submit bugs and feature requests.
- Review the code and enhancements.
- Add more diagnostic rules and features.

Feel free to fork the repo and create pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for exploring the Computer Diagnostic Expert System. For any questions or support, please open an issue on this repository.
```
