from geopy.distance import geodesic
import json
import csv
from typing import Dict, List, Tuple

def load_coordinates(filename: str) -> Dict[str, Tuple[float, float]]:
    """
    Load coordinates from JSON file.
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not parse {filename}")
        return {}

def find_zipcodes_in_radius(
    coordinates: Dict[str, Tuple[float, float]], 
    target_zipcode: str, 
    radius_miles: float
) -> List[Dict]:
    """
    Find all zipcodes within specified radius of target zipcode.
    """
    if target_zipcode not in coordinates:
        print(f"Error: Target zipcode {target_zipcode} not found in coordinates data")
        return []
    
    target_coords = coordinates[target_zipcode]
    nearby_zipcodes = []
    
    for zipcode, coords in coordinates.items():
        distance = geodesic(target_coords, coords).miles
        
        if distance <= radius_miles:
            nearby_zipcodes.append({
                'zipcode': zipcode,
                'distance': round(distance, 2),
                'latitude': coords[0],
                'longitude': coords[1]
            })
    
    # Sort results by zipcode numerically
    nearby_zipcodes.sort(key=lambda x: x['zipcode'])
    return nearby_zipcodes

def save_to_csv(results: List[Dict], filename: str):
    """
    Save results to CSV file.
    """
    if not results:
        return
    
    fieldnames = ['zipcode', 'distance', 'latitude', 'longitude']
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results) 