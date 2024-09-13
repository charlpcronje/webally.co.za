import os
import re
import argparse


def create_file(path, content, safe_mode=False):
    if safe_mode:
        print(f"Would create file: {path}")
        print(f"Content preview: {content[:50]}..." if len(
            content) > 50 else f"Content: {content}")
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Created file: {path}")


def extract_files_from_markdown(markdown_file, safe_mode=False):
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r'<!-- (.*?) -->\s*```(?:svelte|typescript|css|yaml)\s*(.*?)```'
    matches = re.findall(pattern, content, re.DOTALL)

    for file_path, file_content in matches:
        file_path = file_path.strip()
        file_content = file_content.strip()
        if file_path and file_content:
            try:
                create_file(file_path, file_content, safe_mode)
            except OSError as e:
                print(
                    f"Error {'would occur' if safe_mode else 'occurred'} creating file {file_path}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract files from markdown and create them.")
    parser.add_argument("--safe", action="store_true",
                        help="Run in safe mode (don't create files, just preview)")
    args = parser.parse_args()

    markdown_file = "prompts.md"
    print(f"Running in {'safe mode' if args.safe else 'normal mode'}")
    extract_files_from_markdown(markdown_file, args.safe)
    print("File extraction preview complete." if args.safe else "File extraction complete.")
