from InquirerPy import inquirer

from .api import Api
from .user import Course
from . import TOKEN_FILE

def main():
  """Main entry point to the module"""

  saved_token = None
  if TOKEN_FILE.exists():
    # Ask user if we wants to use the file
    from_file = inquirer.confirm(
      message="Saved token found, try to use it?", 
      default=True
    ).execute()
    if from_file:
      with open(TOKEN_FILE, "r") as f:
        saved_token = f.read()

  api = Api(saved_token)
  
  # Pick class
  user = api.get_user()

  print(f"Logged in as {user.name} ({user.email})")

  course: Course = inquirer.select(
    message="Choose class:",
    choices=[{
      "value": c,
      "name": f"{c.code} - {c.name}"
    } for c in user.active_courses],
    vi_mode=True
  ).execute()

  cid = course.id
  num_read = 0
  while tids := api.get_unread_threads(cid):
    for tid in tids:
      api.read_thread(tid)
      num_read += 1

      # TODO: maybe query the actual read thing?
      print(f"Number of posts read: {num_read}", end="\r")

  print(f"No more unread posts! Total posts read: {num_read}")
