def write_to_file(filename, content):
    """Writes content to a file, overwriting if it exists."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"✅ Content written to {filename}")
    except IOError as e:
        print(f"❌ Error writing to file: {e}")

def append_to_file(filename, content):
    """Appends content to an existing file."""
    try:
        with open(filename, 'a') as file:
            file.write('\n' + content)
        print(f"✅ Content appended to {filename}")
    except IOError as e:
        print(f"❌ Error appending to file: {e}")

def read_from_file(filename):
    """Reads and returns content from a file."""
    try:
        with open(filename, 'r') as file:
            data = file.read()
        print(f"📖 Content of {filename}:\n{data}")
        return data
    except FileNotFoundError:
        print(f"⚠️ File {filename} not found.")
    except IOError as e:
        print(f"❌ Error reading file: {e}")

# Example usage
if __name__ == "__main__":
    filename = "example.txt"
    write_to_file(filename, "Hello, Shreeyasmita! This is your file.")
    append_to_file(filename, "Here's another line for you.")
    read_from_file(filename)