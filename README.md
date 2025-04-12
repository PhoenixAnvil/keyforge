# 🔐 KeyForge

**A secure password generator forged in the fires of The Forge.**

KeyForge is a Python command-line tool designed to generate strong, secure passwords using cryptographically secure
randomization. Built with simplicity and reliability in mind, it's perfect for developers, sysadmins, and anyone who
values security.

---

## 🚀 Features

- Generate secure passwords of custom lengths
- Support for:
    - Alphabetic characters
    - Numeric digits
    - Special characters
    - All-character combinations
- Verbose mode to view generated output
- Built with Python’s `secrets` module for strong randomness
- Fully tested with `pytest`

---

## 📦 Installation

> 📌 **Coming soon on [PyPI](https://pypi.org/)!**

For now, clone the repo manually:

```
git clone https://github.com/PhoenixAnvil/keyforge.git
cd keyforge
python3 -m keyforge.cli password -c -v
```

---

## 🛠 Usage

```
python3 -m keyforge.cli password [options]
```

Options:

| Flag          | Description                              |
|---------------|------------------------------------------|
| -l, --length  | Set password length (default: 24)        |
| -a, --alpha   | Use alphabetic characters only           |
| -n, --numeric | Use numeric digits only                  |
| -s, --special | Use special characters only              |
| -c, --combo   | Use a combination of all character types |
| -v, --verbose | Show the generated password in output    |

Example:

```
python3 -m keyforge.cli password -l 32 -c -v
```

---

## ✅ Tests

KeyForge is fully tested with pytest.

To run the test suite:

```
pytest
```

---

## 📂 Project Structure

```
keyforge/
├── __init__.py
├── cli.py # Command-line interface logic
├── forge.py # Core password generation logic
tests/
├── __init__.py
├── test_cli.py
├── test_forge.py
```

---

## 🔥 A Product of The Forge

KeyForge is proudly crafted by PhoenixAnvil Labs — where tools aren’t just built…
they’re forged.

Learn more about our philosophy and DevOps workflow at:

➡️ https://phoenixanvilabs.dev

---

## 📬 Questions or Feedback?

We love hearing from the community!

> 📌 **Coming soon!**

### Mailing Lists

- 💬 Users: keyforge-users@phoenixanvilabs.dev
- 💻 Developers: keyforge-devel@phoenixanvilabs.dev

📣 Want updates about new releases?
Join the **KeyForge-Announce** mailing list!

- 📣 Announce: keyforge-announce@phoenixanvilabs.dev

### IRC Channels

---

## 📜 License

KeyForge is released under the MIT License — free for both personal and commercial use.

---
