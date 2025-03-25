from func import load_coordinates, find_zipcodes_in_radius, save_to_csv

def main():
    # Configuration
    TARGET_ZIPCODE = "33621"
    RADIUS_MILES = 75
    COORDINATES_FILE = "florida_coordinates.json"
    OUTPUT_FILE = f"zipcodes_within_{RADIUS_MILES}miles_of_{TARGET_ZIPCODE}.csv"
    
    # Load coordinates
    print(f"Loading coordinates from {COORDINATES_FILE}...")
    coordinates = load_coordinates(COORDINATES_FILE)
    
    if not coordinates:
        print("No coordinates data available. Exiting.")
        return
    
    print(f"\nSearching for zipcodes within {RADIUS_MILES} miles of {TARGET_ZIPCODE}...")
    nearby = find_zipcodes_in_radius(coordinates, TARGET_ZIPCODE, RADIUS_MILES)
    
    if not nearby:
        print("No zipcodes found within the specified radius.")
        return
    
    # Save results to CSV
    save_to_csv(nearby, OUTPUT_FILE)
    print(f"\nFound {len(nearby)} zipcodes within {RADIUS_MILES} miles of {TARGET_ZIPCODE}")
    print(f"Results saved to {OUTPUT_FILE}")
    
    # Print preview of results
    print("\nPreview of first 5 results (sorted by zipcode):")
    print("Zipcode  | Distance (miles) | Coordinates")
    print("-" * 50)
    
    for result in nearby[:5]:
        print(f"{result['zipcode']}    | {result['distance']:>14.2f} | ({result['latitude']}, {result['longitude']})")
    
    if len(nearby) > 5:
        print(f"... and {len(nearby) - 5} more zipcodes (see CSV file for complete list)")

if __name__ == "__main__":
    main()
