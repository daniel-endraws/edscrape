from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from pathlib import Path

from .api import Api
from .user import Course

def main():
  """Main entry point to the module"""
  api = Api()
  
  # Pick class
  user = api.get_user()

  course: Course = inquirer.select(
    message="Choose class:",
    choices=map(lambda c: Choice(c, f"{c.code} - {c.name}"), user.active_courses),
    vi_mode=True
  ).execute()

  print(f"You chose {course.code} {course.name} ({course.id})")