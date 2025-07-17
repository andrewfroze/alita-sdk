import re

TOOLKIT_SPLITTER = "___"

# This pattern matches characters that are NOT alphanumeric, underscores, or hyphens
clean_string_pattern = re.compile(r'[^a-zA-Z0-9_.-]')


def clean_string(s: str) -> str:
    # Replace these characters with an empty string
    cleaned_string = re.sub(clean_string_pattern, '', s)
    return cleaned_string

def get_tool_name_for_toolkit(toolkit_name: str, initial_tool_name: str, ) -> str:
    return f"{clean_string(toolkit_name)}{TOOLKIT_SPLITTER}{initial_tool_name}"