# Ice Breaker

A simple Python application to generate ice breaker questions for FRC Team 1967 team building activities.

## About

This tool helps team members get to know each other better through fun and engaging questions. Perfect for team meetings, gatherings, and building team chemistry!

## Features

- 🎲 Generate random ice breaker questions
- 📝 Get multiple questions at once
- 💻 Interactive mode or command-line mode
- 🤖 Robotics-themed questions included
- ⚡ Simple and easy to use

## Requirements

- Python 3.6 or higher (no external dependencies required!)

## Usage

### Interactive Mode

Simply run the script without arguments to enter interactive mode:

```bash
python icebreaker.py
```

You'll be presented with a menu where you can:
- Get a single random question
- Get 5 random questions
- Get 10 random questions
- Show all questions

### Command-Line Mode

Get a single random question:
```bash
python icebreaker.py random
```

Get multiple random questions (e.g., 5):
```bash
python icebreaker.py 5
```

Show all questions:
```bash
python icebreaker.py all
```

Show help:
```bash
python icebreaker.py --help
```

## Examples

### Example 1: Quick Random Question
```bash
$ python icebreaker.py random
What's your favorite robot from a past FRC season and why?
```

### Example 2: Interactive Session
```bash
$ python icebreaker.py
============================================================
   🤖 FRC Team 1967 Ice Breaker 🤖
============================================================

Options:
  1 - Get a random question
  2 - Get 5 random questions
  3 - Get 10 random questions
  4 - Show all questions
  q - Quit

Enter your choice: 1

Here's your ice breaker question:
  ❓ If you could have any superpower, what would it be?
```

## Making it Executable (Optional)

On Linux/Mac, you can make the script executable:

```bash
chmod +x icebreaker.py
./icebreaker.py
```

## Contributing

Feel free to add more ice breaker questions by editing the `questions` list in the `IceBreaker` class!

## License

This is a simple team-building tool for FRC Team 1967. Use and modify as needed!

## Support

For questions or suggestions, contact the team leadership.

---

**Go Team 1967!** 🚀🤖
