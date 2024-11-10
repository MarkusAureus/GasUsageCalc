# GasUsage Calculator

[Slovak version/Slovenská verzia](README_SK.md)

A simple desktop application for calculating gas consumption that converts cubic meters (m³) to kilowatt-hours (kWh) and then calculates the price in euros.

![GasUsage Calculator Screenshot](/images/background.png)

## Features

- Conversion from cubic meters (m³) to kilowatt-hours (kWh)
- Price calculation in euros based on current rate
- User-friendly interface
- Option to clear entered values

## Technical Specifications

- Language: Python 3.x
- GUI Framework: Tkinter
- Conversion factor: 40 * 1.02264 / 3.6
- Rate per kWh: 0.0292 €

## Installation

1. Make sure you have Python 3.x installed
2. Download all files from the repository
3. Create an `images` folder and place the `background.png` file in it

## Running the Application

```bash
python gas_calculator.py
```

## Usage

1. Enter the consumption value in cubic meters (m³)
2. Click the "Result" button to calculate
3. The application will display:
   - Converted value in kWh
   - Price in euros
4. Use the "Clear" button to reset all values

## Project Structure

```
GasUsage-Calculator/
├── gas_calculator.py
├── README.md
├── README_SK.md
├── images/
│   └── background.png
└── LICENSE
│   
└── thumbnail.jpg
```

## Author

Marek Kožuch

## License

This project is open-source software distributed under the MIT License. This means:
- You can freely use, modify, and distribute the software
- The software is available free of charge
- The only requirement is to preserve the copyright and license information

## Development Notes

- Application is designed exclusively for PC (desktop computers and laptops)
- Application uses a fixed window size (602x400 pixels)
- User interface is optimized for readability using Roboto and Helvetica fonts
- Input validations implemented for safe usage
