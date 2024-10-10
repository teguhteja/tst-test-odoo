

# TST Test Odoo

This repository contains customizations and extensions for the Odoo ERP system. The customizations are aimed at enhancing the functionality of the Point of Sale (POS) module.

## Table of Contents

- [TST Test Odoo](#tst-test-odoo)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)
    - [TTM Material Module](#ttm-material-module)
      - [API Endpoints](#api-endpoints)
    - [POS Customizations Module](#pos-customizations-module)
  - [Contributing](#contributing)
  - [License](#license)


## Project Structure

The project is organized as follows:

```sh
tst-test-odoo/
├──ttm_material/ 
│    ├── init.py 
│    ├── manifest.py 
│    ├── controllers/ 
│    │      └── material_controller.py 
│    ├── models/ 
│    │      └── material.py 
│    └── views/ 
│       └── material_views.xml 
│
├── pos_customizations/
│   ├── __init__.py
│   ├── __manifest__.py
│   ├── static/
│   │   └── src/
│   │       └── js/
│   │           └── pos_customizations.js
│   └── views/
│       └── pos_customizations_templates.xml
└── README.md
```


The project is organized as follows:

- **ttm_material/**: Module for managing materials.
  - **controllers/**: Contains HTTP request handling.
    - **material_controller.py**: Routes for CRUD operations on materials.
  - **models/**: Definitions for data models.
    - **material.py**: Defines the `material` model.
  - **views/**: XML files defining views.
    - **material_views.xml**: Views for the `material` model.
  - **__init__.py**: Module initialization.
  - **__manifest__.py**: Metadata for the module.

- **pos_customizations/**: Module for POS customizations.
  - **__init__.py**: Module initialization.
  - **__manifest__.py**: Metadata for the module.
  - **static/src/js/**: JavaScript files for POS customization.
    - **pos_customizations.js**: Custom JavaScript for POS behavior.
  - **views/**: XML files for custom views and templates.
    - **pos_customizations_templates.xml**: POS template customizations.

## Installation

To install the modules, follow these steps:

1. **Clone the repositories**:
    ```bash
    git clone https://github.com/teguhteja/tst-test-odoo.git
    ```

2. **Navigate to the Odoo addons directory**:
    ```bash
    cd /path/to/your/odoo/addons
    ```

3. **Update the module list**:
    ```bash
    odoo-bin -c your_odoo.conf -u ttm_material -u pos_customizations -d your_database
    ```

4. **Install the modules**:
    - Go to the Odoo Apps menu.
    - Search for `TTM Material` and `POS Customizations`.
    - Click `Install` for each module.

## Usage

### TTM Material Module

Manage materials through the Odoo interface or via API endpoints:

#### API Endpoints

- **List Materials**: `GET /materials`
- **Create Material**: `POST /materials/create`
- **Update Material**: `POST /materials/update/<int:material_id>`
- **Delete Material**: `POST /materials/delete/<int:material_id>`

### POS Customizations Module

Customize POS behavior with updated numpad buttons:

- The "Price" and "Discount" buttons will be disabled.
- Numpad buttons show values like +10,000, +50,000, +100,000.

To use:

1. Open the POS module in Odoo.
2. Start a new session to see the updated numpad buttons.

## Contributing

Contributions are welcome! Follow these steps:

1. **Fork the repositories**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make changes** and **commit**.
4. **Push changes** and **create a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
