#!/usr/bin/env python3
"""
Ice Breaker - A simple tool to generate ice breaker questions for team building.
Perfect for FRC Team 1967 meetings and gatherings!
"""

import random
import sys


class IceBreaker:
    """A collection of ice breaker questions to help team members get to know each other."""
    
    def __init__(self):
        self.questions = [
            "What's your favorite robot from a past FRC season and why?",
            "If you could have any superpower, what would it be?",
            "What's the most interesting thing you've built or created?",
            "What's your favorite hobby outside of robotics?",
            "If you could travel anywhere in the world, where would you go?",
            "What's your favorite movie or TV show?",
            "What's one thing on your bucket list?",
            "What's your favorite food?",
            "If you could meet any historical figure, who would it be?",
            "What's your favorite subject in school and why?",
            "What's the best advice you've ever received?",
            "What's your favorite game (video game, board game, sport)?",
            "If you could have dinner with any three people (living or dead), who would they be?",
            "What's something new you'd like to learn this year?",
            "What's your favorite memory from being on the robotics team?",
            "What role on the team interests you most (programming, mechanical, electrical, business)?",
            "What's your favorite type of music or favorite artist?",
            "If you could instantly become an expert in something, what would it be?",
            "What's the most challenging thing you've overcome?",
            "What's something that always makes you laugh?",
            "What's your dream job or career?",
            "If you could invent anything, what would it be?",
            "What's your favorite season and why?",
            "What's one word your friends would use to describe you?",
            "What's your favorite way to spend a weekend?",
        ]
    
    def get_random_question(self):
        """Get a random ice breaker question."""
        return random.choice(self.questions)
    
    def get_multiple_questions(self, count=5):
        """Get multiple unique random questions."""
        if count > len(self.questions):
            count = len(self.questions)
        return random.sample(self.questions, count)
    
    def get_all_questions(self):
        """Get all ice breaker questions."""
        return self.questions.copy()


def print_header():
    """Print a nice header for the ice breaker application."""
    print("=" * 60)
    print("   🤖 FRC Team 1967 Ice Breaker 🤖")
    print("=" * 60)
    print()


def print_menu():
    """Print the menu options."""
    print("Options:")
    print("  1 - Get a random question")
    print("  2 - Get 5 random questions")
    print("  3 - Get 10 random questions")
    print("  4 - Show all questions")
    print("  q - Quit")
    print()


def interactive_mode():
    """Run the ice breaker in interactive mode."""
    icebreaker = IceBreaker()
    print_header()
    
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip().lower()
        print()
        
        if choice == 'q':
            print("Thanks for using Ice Breaker! See you at the next meeting! 🚀")
            break
        elif choice == '1':
            print("Here's your ice breaker question:")
            print(f"  ❓ {icebreaker.get_random_question()}")
            print()
        elif choice == '2':
            print("Here are 5 random ice breaker questions:")
            for i, question in enumerate(icebreaker.get_multiple_questions(5), 1):
                print(f"  {i}. {question}")
            print()
        elif choice == '3':
            print("Here are 10 random ice breaker questions:")
            for i, question in enumerate(icebreaker.get_multiple_questions(10), 1):
                print(f"  {i}. {question}")
            print()
        elif choice == '4':
            print("All ice breaker questions:")
            for i, question in enumerate(icebreaker.get_all_questions(), 1):
                print(f"  {i}. {question}")
            print()
        else:
            print("Invalid choice. Please try again.")
            print()


def main():
    """Main entry point for the ice breaker application."""
    if len(sys.argv) > 1:
        # Command-line mode
        icebreaker = IceBreaker()
        arg = sys.argv[1].lower()
        
        if arg in ['-h', '--help']:
            print("Ice Breaker - Team building questions for FRC Team 1967")
            print()
            print("Usage:")
            print("  python icebreaker.py          - Interactive mode")
            print("  python icebreaker.py random   - Get one random question")
            print("  python icebreaker.py 5        - Get 5 random questions")
            print("  python icebreaker.py all      - Show all questions")
            print("  python icebreaker.py --help   - Show this help message")
        elif arg == 'random':
            print(icebreaker.get_random_question())
        elif arg == 'all':
            for i, question in enumerate(icebreaker.get_all_questions(), 1):
                print(f"{i}. {question}")
        elif arg.isdigit():
            count = int(arg)
            for i, question in enumerate(icebreaker.get_multiple_questions(count), 1):
                print(f"{i}. {question}")
        else:
            print(f"Unknown argument: {arg}")
            print("Use --help for usage information")
            sys.exit(1)
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
