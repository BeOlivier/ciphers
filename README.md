# Cipher Tools

A small Python project for experimenting with classic encryption, decryption, and beginner-friendly security tooling. The first goal is to build a clean command-line tool for Caesar cipher encryption/decryption with configurable shift steps. Over time, the project can grow into a collection of self-coded tools for cryptography practice, simple cracking challenges, and security learning.

The first version will stay as a command-line tool because it is simpler, cleaner, and fits cryptography practice well. Later, a Python GUI could be added with `tkinter` for a lightweight built-in interface, or a small web UI could be made with Flask if the project grows into a bigger toolkit.

## Current Goal

Build a Python-based Caesar cipher tool that can:

- Encrypt text with a chosen shift value.
- Decrypt text with a chosen shift value.
- Run from the terminal with clear input/output.
- Keep the code readable, version-controlled, and professional enough for a public Git repository.

## Roadmap / TODO

Newest ideas are added at the top, while the earliest foundation tasks stay at the bottom.

- [ ] Later: add small self-coded security utilities, such as image/steganography inspection helpers.
- [ ] Explore simple RSA demos with small, crackable values for learning.
- [ ] Add Vigenere cipher support.
- [ ] Refactor into clean functions/modules as the project grows.
- [ ] Add examples to this README.
- [ ] Add basic error handling for invalid inputs.
- [ ] Add support for custom shift values.
- [ ] Add terminal input so the user can choose encrypt/decrypt mode.
- [X] Add brute-force Caesar cracking mode.
- [X] Add simple tests for cipher behavior.
- [X] Preserve spaces, punctuation, and capitalization where possible.
- [X] Implement Caesar cipher decryption.
- [X] Implement Caesar cipher encryption.


## Development Setup

Install development dependencies:

```bash
brew install pytest
```

Save the currently installed Homebrew development tools:

```bash
brew list --versions pytest > requirements-dev.txt
```

Install saved development tools on a fresh setup:

```bash
brew install pytest
```

Update dependencies and refresh the saved versions:

```bash
brew upgrade pytest
brew list --versions pytest > requirements-dev.txt
```

Run tests:

```bash
pytest -v --tb=short
```
