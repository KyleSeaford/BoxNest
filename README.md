# BoxNest

## Overview

BoxNest is a powerful storage management solution designed to streamline the organization, tracking, and retrieval of stored items. With its intuitive interface and robust features, BoxNest ensures that users can effortlessly manage their stored boxes, enhancing efficiency and minimizing the hassle associated with storage management.

## Features

- **Easy Box Management:** Add, find, and remove boxes with a few simple commands.
- **Detailed Database:** Keep track of each box's location, size, and owner.
- **Print Box Labels:** Automatically generate and print box ID stickers.
- **Backup and Log:** Automatic backups triggered by runtime or database size, with detailed logs.

## Installation

1. Clone the repository:

```bash
  git clone https://github.com/KyleSeaford/BoxNest-public.git
```
2. Navigate to the project directory:
 
```bash
  cd BoxNest-public
```

3. Install the required dependencies:
   
  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. Run the program:
  ```bash
  python BoxNest.py
```
2. Follow the on-screen instructions to manage your boxes.

## Backup and Log
- Automatic backups are triggered after 2 hours of runtime or if the database rows exceed 30.
- Detailed logs can be found in the `BoxNest.log` file.
- Backup files are stored in the `backup+log` directory within the program files.

## Acknowledgements
Special thanks to contributors and supporters who have helped make BoxNest better.
##                               

#### Organized to Perfection. By Kyle Seaford.
