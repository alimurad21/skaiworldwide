# SKAI Worldwide Documentation

This repository contains the standardized documentation for SKAI Worldwide's products and services, built using Sphinx and reStructuredText (RST).

## Features

- Modern, responsive documentation theme matching SKAI Worldwide's branding
- Support for both RST and Markdown files
- Cross-referencing between documents
- Code syntax highlighting
- Search functionality
- Mobile-friendly design

## Structure

```
docs/
├── _static/          # Static files (CSS, images)
├── _templates/       # Custom templates
├── products/         # Product documentation
├── services/         # Service documentation
├── resources/        # Additional resources
└── index.rst         # Main documentation index
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd skai-docs
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Building the Documentation

1. Navigate to the docs directory:
   ```bash
   cd docs
   ```

2. Build the HTML documentation:
   ```bash
   make html
   ```

3. View the documentation:
   Open `_build/html/index.html` in your web browser.

## Adding New Documentation

### Adding a New Product

1. Create a new RST file in the `docs/products/` directory
2. Add the file to the appropriate toctree in `index.rst`
3. Follow the existing documentation structure

Example:
```rst
New Product
==========

Overview
--------

[Product description]

Features
--------

* Feature 1
* Feature 2
```

### Adding a New Service

1. Create a new RST file in the `docs/services/` directory
2. Add the file to the appropriate toctree in `index.rst`
3. Follow the existing documentation structure

## Customizing the Theme

The documentation theme can be customized by modifying:

- `docs/_static/custom.css` - Custom CSS styles
- `docs/config.py` - Sphinx configuration
- `docs/_templates/` - Custom HTML templates

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

Copyright © 2024 SKAI Worldwide Co., Ltd. All Rights Reserved.
