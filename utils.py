def get_problem_file(text_file="problem_input.txt", mode="r"):
    """Reads the problem input file and returns its lines."""
    try:
        with open(text_file, mode=mode) as f:
            return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{text_file}' was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the file: {e}")