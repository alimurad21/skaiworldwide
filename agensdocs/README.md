# AgensDocs

This repository contains the documentation for AgensGraph, built using Sphinx and various extensions to create a modern, interactive documentation website.

## Features

- Modern documentation theme using `sphinx-rtd-theme`
- Support for Markdown files using `myst-parser`
- Automatic type hints documentation with `sphinx-autodoc-typehints`
- Code block copy button functionality with `sphinx-copybutton`
- Tabbed content support with `sphinx-tabs`

## Project Structure

```
agensdocs/
├── docs/                    # Documentation source files
│   ├── _static/            # Static files (CSS, images, etc.)
│   ├── _template/          # Custom templates
│   ├── build/              # Build output directory
│   ├── conf.py            # Sphinx configuration
│   ├── index.rst          # Main documentation entry point
│   ├── index.js           # JavaScript files
│   ├── Makefile           # Build automation for Unix-like systems
│   └── make.bat           # Build automation for Windows
├── venv/                   # Python virtual environment
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agensdocs
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Building the Documentation

To build the documentation locally:

1. Navigate to the `docs` directory:
   ```bash
   cd docs
   ```

2. Build the documentation:
   ```bash
   make html
   ```

3. The built documentation will be available in `docs/_build/html/`. Open `index.html` in your web browser to view it.

## Development

- Source files are located in the `docs` directory
- Configuration is in `docs/conf.py`
- The main documentation structure is defined in `docs/index.rst`

## Contributing

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes
4. Submit a pull request

## License

[Add appropriate license information here]

## Contact

[Add contact information here] 