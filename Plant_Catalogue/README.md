## Plant Catalogue System

A command-line application to manage your plant collection.

### Features
- Add and manage plants (name, family, image path, birthdate)
- Search plants by name or family
- Generate plant collection reports in CSV format
- Keep track of plant growth and watering
- QR code scanning for quick plant access

### Setup
1. Copy `config.example.ini` to `config.ini` and update settings
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python src/main.py`

### Commands

#### Basic Plant Management
- List all plants
  ```
  python src/main.py list
  ```

- Add a new plant
  ```
  python src/main.py add-plant --name "Venus Flytrap" --family "Droseraceae" --image "path/to/image.jpg" --age-months 6
  ```

- Edit a specific plant
  ```
  python src/main.py edit-plant --id 3 --name "Changed" --family "Changed_Family"
  ```

- Search for plants
  ```
  python src/main.py search-plant --query "Venus"
  ```

#### Growth Tracking
- Add leaf record to track growth
  ```
  python src/main.py add-leaf --id 3
  ```

- Show leaf statistics for a specific plant
  ```
  python src/main.py leaf-stats --id 2
  ```

- Generate CSV of all leaf statistics
  ```
  python src/main.py leaf-stats
  ```

#### Watering Management
- Record watering for a plant
  ```
  python src/main.py water --id 3
  ```

- Show watering information
  ```
  python src/main.py water-info --id 3
  ```

#### Image & QR Code Features
- Show image of a specific plant
  ```
  python src/main.py show-image --id 2
  ```
/Users/michieldevogelaere/Vives/Vakken/Sem1/Programming_In_Python/Archive/Plants_/venv
- List all QR codes
  ```
  python src/main.py list-qr
  ```

- Scan QR code and interact with plant
  ```
  python src/main.py scan
  ```

#### Reports & Data
- Generate plant report
  ```
  python src/main.py report
  ```

- Perform database migrations
  ```
  python src/main.py migrate
  ```

- Get help on commands
  ```
  python src/main.py -h
  ```

### Project Structure
```
plant_catalogue/
├── src/
│   ├── main.py
│   ├── models/
│   │   └── plant.py
│   ├── database/
│   │   ├── db_manager.py
│   │   └── queries.py
│   ├── utils/
│   │   ├── image_handler.py
│   │   ├── image_viewer.py
│   │   ├── plantdata_processor.py
│   │   ├── qr_handler.py
│   │   └── report_generator.py
│   └── cli/
│       └── argument_parser.py
├── data/
│   ├── images/
│   ├── reports/
│   ├── qr_codes/
│   └── plants.db
├── config.example.ini
├── README.md
└── requirements.txt
```
