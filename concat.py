import os
import logging

def concatenate_py_files(directory, output_file):
    # Set up logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    # Check if the directory exists
    if not os.path.exists(directory):
        logging.error(f"Directory {directory} does not exist.")
        return
    else:
        logging.info(f"Accessing directory: {directory}")

    try:
        with open(output_file, 'w') as outfile:
            # First process README.md if it exists
            readme_file = 'README.md'
            readme_path = os.path.join(directory, readme_file)
            if os.path.exists(readme_path):
                logging.info(f"Processing file: {readme_file}")
                outfile.write(f"### This is START of the {readme_file} file:\n~~~\n")
                with open(readme_path, 'r') as infile:
                    outfile.write(infile.read())
                outfile.write(f"\n~~~\n### This is END of the file {readme_file}!\n\n")

            # Iterate over all files in the directory
            for filename in os.listdir(directory):
                if filename.endswith(('.py')) and filename != 'concat.py':  # Exclude concat.py itself
                    logging.info(f"Processing file: {filename}")

                    # Write the start comment
                    outfile.write(f"### This is START of the {filename} file:\n~~~\n")

                    # Path to the current file
                    filepath = os.path.join(directory, filename)

                    # Read and write the content of the .py file
                    with open(filepath, 'r') as infile:
                        outfile.write(infile.read())

                    # Write the end comment
                    outfile.write(f"\n~~~\n### This is END of the file {filename}!\n\n")
            logging.info(f"All files have been processed. Output written to {output_file}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Directory path where concat.py is located
    directory_path = os.path.dirname(os.path.realpath(__file__))
    
    # Output file path in the same directory
    output_file_path = os.path.join(directory_path, 'output.txt')

    concatenate_py_files(directory_path, output_file_path)
