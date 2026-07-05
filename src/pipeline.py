"""
NBA Career Performance Analytics Engine
Author: Michael Stephen Curbeam Jr.
Description: An optimized, modular data pipeline that automates the ETL 
             processing of historical athlete career data.
"""

def open_file(filename="players_regular_season_career.txt"):
    """Safely opens a data file for reading."""
    try:
        return open(filename, "r")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

def read_file():
    """Ingests and parses data fields from the raw source file using pipe-delimiters."""
    file_handle = open_file()
    if not file_handle:
        return []
    
    parsed_data = []
    for line in file_handle:
        parsed_data.append(line.rstrip().split("|"))
    file_handle.close()
    return parsed_data

def calculate_efficiency():
    """Transforms raw metrics into a standardized career efficiency calculation matrix."""
    dataset = read_file()
    if not dataset:
        return []

    efficiency_collection = []

    for index, row in enumerate(dataset):
        # Skip the header metadata layer
        if index == 0:
            continue

        try:
            # Defensive variable extraction mapping from data row indexes
            games_played = int(row[4])
            if games_played == 0:
                continue  # Prevent mathematical ZeroDivisionError anomalies

            points    = int(row[6])
            rebounds  = int(row[9])
            assists   = int(row[10])
            steals    = int(row[11])
            blocks    = int(row[12])
            turnovers = int(row[13])
            
            fg_attempts = int(row[15])
            fg_made     = int(row[16])
            ft_attempts = int(row[17])
            ft_made     = int(row[18])
            
            player_name = f"{row[1]} {row[2]}"

            # NBA efficiency standard logic formulation
            positive_metrics = points + rebounds + assists + steals + blocks
            negative_metrics = (fg_attempts - fg_made) + (ft_attempts - ft_made) + turnovers
            efficiency = (positive_metrics - negative_metrics) / games_played

            efficiency_collection.append([player_name, efficiency])
        except (ValueError, IndexError):
            # Skip rows with malformed or missing columns defensively
            continue

    return efficiency_collection

def write_out_file(collections):
    """Sorts datasets efficiently and loads the top 50 records into a structured output file."""
    if not collections:
        return ""

    # Algorithmic optimization: Sort directly by efficiency score in O(N log N) time complexity
    collections.sort(key=lambda player: player[1], reverse=True)
    
    # Isolate top 50 elite statistical records
    top_fifty = collections[:50]

    output_filename = "top50.txt"
    with open(output_filename, "w") as file_handle:
        for player in top_fifty:
            # Format output data rows dynamically
            file_handle.write(f"{player[0]},{player[1]:.2f}\n")

    # Read back generated file contents for analytical confirmation
    with open(output_filename, "r") as file_handle:
        generated_report = file_handle.read()
    
    return generated_report

def main():
    print("=== NBA Performance Analytics Pipeline Initialized ===")
    
    # Execute extraction & transformation pipeline steps
    efficiency_data = calculate_efficiency()
    
    if efficiency_data:
        # Load structured analytical output
        report_output = write_out_file(efficiency_data)
        print("\n=== Top 50 Performance Report Generated Successfully ===")
        print(report_output[:300] + "...\n[Report Truncated for CLI View]")
    else:
        print("Pipeline Execution Halted: No input data recovered.")
        
    print("\nFinished")

if __name__ == "__main__":
    main()