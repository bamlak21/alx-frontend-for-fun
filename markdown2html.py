#!/usr/bin/python3
import sys
import os
import markdown

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as md_file:
        markdown_text = md_file.read()
        html_text = markdown.markdown(markdown_text, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br'])

    # Parse bold syntax
    html_text = html_text.replace("<strong>", "<b>")
  
    # Replace **bold** with <strong>bold</strong> in the HTML
    html_text = html_text.replace('<p><strong>', '<strong>')
    html_text = html_text.replace('</strong></p>', '</strong>')
  
    with open(output_file, 'w') as html_file:
        html_file.write(html_text)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(input_filename):
        sys.stderr.write(f"Missing {input_filename}\n")
        sys.exit(1)

    # Convert Markdown to HTML
    convert_markdown_to_html(input_filename, output_filename)

    sys.exit(0)















