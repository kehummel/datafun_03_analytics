"""
Process a JSON file to count astronauts by spacecraft and save the result.

JSON file is in the format where people is a list of dictionaries with keys "craft" and "name".

{
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        },
        {
            "craft": "ISS",
            "name": "Nikolai Chub"
        }
    ],
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from loguru import logger

#####################################
# Declare Global Variables
#####################################

# TODO: Replace with the names of your folders
FETCHED_DATA_DIR: str = "logs"
PROCESSED_DIR: str = "khummel_processed"

#####################################
# Define Functions
#####################################

# TODO: Add or replace this with a function that reads and processes your JSON file

def count_people_by_language(file_path: pathlib.Path) -> dict:
    """Count the number of astronauts on each spacecraft from a JSON file."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r') as file:

            # Use the json module load() function 
            # to read data file into a Python dictionary
            people_dictionary = json.load(file)  

            # initialize an empty dictionary to store the counts
            language_counts_dictionary = {}

    

            # For each person in the list, get the craft and count them
            for person_dictionary in people_dictionary:  

                # Get the craft from the person dictionary
                # If the key "craft" is not found, default to "Unknown"
                lang = person_dictionary.get("language", "Unknown")

                # Update the craft counts dictionary for that craft
                # If the craft is not in the dictionary, initialize it to 0
                # Add 1 to the count for the current craft
                language_counts_dictionary[lang] = language_counts_dictionary.get(lang, 0) + 1

            # Return the dictionary with counts of astronauts by spacecraft    
            return language_counts_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {} # return an empty dictionary in case of error

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""

    # TODO: Replace with path to your JSON data file
    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "name_lang.json")

    # TODO: Replace with path to your JSON processed file
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "number_of_languages.txt")
    
    # TODO: Call your new function to process YOUR JSON file
    # TODO: Create a new local variable to store the result of the function call
    craft_counts = count_people_by_language(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # TODO: Update the output to describe your results
        file.write("Number of people by Language:\n")
        for craft, count in craft_counts.items():
            file.write(f"{craft}: {count}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")