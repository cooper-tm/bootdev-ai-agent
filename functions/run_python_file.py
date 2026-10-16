import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        is_file = os.path.isfile(abs_file_path)
        is_py = abs_file_path.endswith(".py")

        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not is_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not is_py:
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file_path]

        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=abs_working_dir,
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
        output_parts = []
        if result.returncode:
            output_parts.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")
        else:
            output_parts.append(f"STDOUT: {result.stdout}")
            output_parts.append(f"STDERR: {result.stderr}")

        final_out = "\n".join(output_parts)

        return final_out

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": "string",
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}
