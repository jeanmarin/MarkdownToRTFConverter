'''
Markdown to RTF converter

Jean-Louis Marin
October 31 2023

paste a block of text in a dialog box and convert the markdown to RTF. --> Done
Saved in RTF file --> Done

Bug fixed encoding in the output file. --> DONE

'''

import re
import tkinter as tk
from tkinter import simpledialog, messagebox

def markdown_to_rtf(md_text):
    # Headers
    md_text = re.sub(r'^# (.+)$', r'\\b\\fs32 \1\\b0\\fs20\\par ', md_text, flags=re.M) # H1
    md_text = re.sub(r'^## (.+)$', r'\\b\\fs28 \1\\b0\\fs20\\par ', md_text, flags=re.M) # H2
    md_text = re.sub(r'^### (.+)$', r'\\b\\fs24 \1\\b0\\fs20\\par ', md_text, flags=re.M) # H3

    # Bold
    md_text = re.sub(r'\*\*(.+?)\*\*', r'\\b \1\\b0', md_text)
    
    # Italics
    md_text = re.sub(r'\*(.+?)\*', r'\\i \1\\i0', md_text)
    
    # Links
    md_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'\\ul \1\\ul0 (\\cf1 \2\\cf0)', md_text)

    # Convert newlines to RTF's format
    md_text = re.sub(r'\n', r'\\par ', md_text)
    
    # Add RTF headers and footers
    rtf_text = "{\\rtf1\\ansi {\\colortbl;\\red0\\green0\\blue255;}" + md_text + "}"

    return rtf_text

def main():
    # Path to save the file
    file_path = "d:/Scripts/Markdown to RTF/RTF/output.rtf"
    
    # Initialize the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open the input dialog
    md_input = simpledialog.askstring("Markdown Input", "Paste your markdown text:")

    # Check if the user provided input or cancelled
    if md_input:
        rtf_result = markdown_to_rtf(md_input)

        # Save the content to a file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(rtf_result)

        messagebox.showinfo("Success", f"RTF content saved to {file_path}")
    else:
        messagebox.showwarning("Warning", "No input provided!")

    root.destroy()

if __name__ == "__main__":
    main()