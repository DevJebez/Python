def process_text_file(input_file, output_file, char_limit=4000):
    try:
        # Read the content of the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove newline characters
        content = content.replace('\n', '')

        # Split content into chunks of specified size
        paragraphs = [content[i:i + char_limit] for i in range(0, len(content), char_limit)]

        # Write chunks to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            for paragraph in paragraphs:
                file.write(paragraph + '\n\n')  # Add a blank line between paragraphs

        print(f"File processed successfully. Output written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'stddev.txt'   # Replace with the path to your input file
output_file = 'output1.txt' # Replace with the path to your desired output file
process_text_file(input_file, output_file)