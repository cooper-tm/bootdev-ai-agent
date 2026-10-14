import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        is_dir = os.path.isdir(abs_file_path)
        if not abs_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if is_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        if not os.path.dirname(abs_file_path):
            os.makedirs(abs_file_path, exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f'Error: writing file "{file_path}": {e}'
