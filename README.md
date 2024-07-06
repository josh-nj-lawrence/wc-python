# wc-python
Linux wc tool clone written in python

A Python clone of the Linux `wc` (word count) command-line tool.

## Overview
This project aims to replicate the functionality of the traditional `wc` command found in Unix/Linux systems, providing basic text analysis capabilities such as counting lines, words, characters, and bytes in text files. It was initiated as part of John Cricketts' Weekly Coding Challenges, focusing initially on a minimal viable product (MVP) that covers the core features outlined in his challenge. Future developments will explore more advanced features present in the original `wc` tool, enhancing the utility and versatility of this Python clone.

## Features
The current implementation of `wc-python` supports the following options, similar to the Linux `wc` command:

- `-l`, `--lines`: Count the number of lines in a text file.
- `-w`, `--words`: Count the number of words in a text file.
- `-m`, `--chars`: Count the number of characters in a text file.
- `-c`, `--bytes`: Count the number of bytes in a text file.

Additionally, the tool can accept input from standard input (stdin), allowing it to be used in Unix-like pipelines.

## Usage
To use `wc-python`, you can specify one or more options followed by the file name(s):

```bash
python wc.py -l -w -m myfile.txt
```

This command will output the number of lines, words, and characters in myfile.txt.

To process multiple files, simply list them:
```bash 
python wc.py -w file1.txt file2.txt
```

For reading from stdin, use:

```bash
cat myfile.txt | python wc.py -l
```

This will count and output the number of lines in myfile.txt using the data piped from cat.

## Installation
No installation is necessary. Ensure you have Python installed on your system. You can run wc-python directly as a script.

## Contributing
Contributions to wc-python are welcome. Whether it's adding new features, improving existing ones, or reporting bugs, your input is valuable. Please feel free to fork the repository and submit pull requests.

## License
wc-python is open-source software licensed under the MIT License. See the LICENSE file for more details. ```

