```markdown
# Markdown to RTF Converter

This utility is a simple tool that allows users to paste a block of Markdown text into a dialog box and convert it to Rich Text Format (RTF). The resulting RTF is then saved to a file.

## Changelog

- **October 31, 2023**
  - Initial release with basic functionality.
  - The paste and convert feature has been implemented.
  - RTF file saving capability has been added.

## Bug Fixes

- Fixed an issue with encoding in the output RTF file.

## Requirements

- Python 3.x (The script has been tested on Python 3.6 and above).
- Standard libraries: `re`, `tkinter`

`tkinter` comes pre-installed with Python, but if you encounter any issues running `tkinter`, particularly on Linux, you might need to install it via your distribution's package manager:

```bash
sudo apt-get install python3-tk
```

Additionally, ensure that you have the `pygtk` library for the dialog box and `markdown` for Markdown processing if the script uses them.

## Installation

To set up this script, clone the repository or download the `.zip` file:

```bash
git clone TBD
cd your-repository
```

Then, you can run the script with Python 3:

```bash
python3 markdown_2_rtf.py
```

## How to Use

1. Run the script.
2. Paste your Markdown text into the dialog box that appears.
3. The script will convert it to RTF and save the file.

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository, make improvements, and submit a pull request.

## License

MIT
https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt


## Author

Jean-Louis Marin - [jeanmarin](https://github.com/jeanmarin)

---

For more information on how to use this script, or for bug reports, please open an issue in the GitHub repository.
```
