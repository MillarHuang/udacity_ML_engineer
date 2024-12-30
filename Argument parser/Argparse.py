import argparse
"""
Run "python Argparse.py --help" will return the description of the usage of this script in command line with argument parser.
The help message specified in each argument will be shown as description for each argument usage
"""
def parse_arguments():
    """
    Parses command-line arguments for the script.
    Returns:
        args: Parsed arguments as a namespace.
    """
    parser = argparse.ArgumentParser(description="A script for processing data.")

    # Add arguments
    parser.add_argument(
        "--input_file", 
        type=str, 
        required=True, 
        help="Path to the input file."
    )
    parser.add_argument(
        "--output_file", 
        type=str, 
        required=False, #If this argument is not a required argument, should also specified a default value
        default="output.csv", 
        help="Path to save the output file (default: output.csv)."
    )
    parser.add_argument(
        "--verbose", 
        action="store_true", # if --verbose is provided in the command-line input, the value assigned to it will be True. Otherwise if --verbose is not provided, its default value will be False
        help="Enable verbose mode for logging."
    )
    parser.add_argument(
        "--num_epochs", 
        type=int, 
        default=10, 
        help="Number of epochs to run the training (default: 10)."
    )

    # Parse the arguments
    args = parser.parse_args()
    return args

# Example Usage
if __name__ == "__main__":
    args = parse_arguments()
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")
    print(f"Verbose mode: {'ON' if args.verbose else 'OFF'}")
    print(f"Number of epochs: {args.num_epochs}")
