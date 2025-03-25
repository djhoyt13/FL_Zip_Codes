# Florida Zip Code Distance Calculator

This project calculates zip codes within a specified radius of a target zip code in Florida. It uses geopy for accurate distance calculations and provides the results in a CSV format.

## Project Structure

The project consists of three main Python files:

- `func.py`: Contains utility functions for coordinate handling and distance calculations
- `main.py`: Contains the main program logic and configuration
- `run.py`: Entry point script to execute the program

## Dependencies

- geopy: For calculating geodesic distances between coordinates
- Python 3.x

## Functions

### `func.py`

The module contains three main functions:

1. `load_coordinates(filename: str) -> Dict[str, Tuple[float, float]]`
   - Loads coordinate data from a JSON file
   - Returns a dictionary mapping zip codes to their coordinates
   - Handles file not found and JSON parsing errors

2. `find_zipcodes_in_radius(coordinates: Dict[str, Tuple[float, float]], target_zipcode: str, radius_miles: float) -> List[Dict]`
   - Finds all zip codes within the specified radius of the target zip code
   - Returns a sorted list of dictionaries containing zip code, distance, and coordinates
   - Results are sorted by zip code numerically

3. `save_to_csv(results: List[Dict], filename: str)`
   - Saves the results to a CSV file
   - Includes zip code, distance, latitude, and longitude columns

### `main.py`

Contains the main program configuration and execution logic:
- Default target zip code: "33621"
- Default radius: 75 miles
- Input file: "florida_coordinates.json"
- Output file: Generated based on target zip code and radius

## Usage

1. Ensure you have the required dependencies installed:
   ```bash
   pip install geopy
   ```

2. Place your Florida coordinates JSON file in the project directory

3. Run the program:
   ```bash
   python run.py
   ```

The program will:
- Load the coordinates from the JSON file
- Find all zip codes within the specified radius
- Save the results to a CSV file
- Display a preview of the first 5 results

## Output Format

The CSV output includes the following columns:
- zipcode: The zip code
- distance: Distance from target zip code in miles
- latitude: Latitude coordinate
- longitude: Longitude coordinate

## Error Handling

The program includes error handling for:
- Missing input files
- Invalid JSON data
- Target zip code not found in coordinates
- Empty results
