from .sso import get_login_token
from .user import User
from . import BASE_URL, TOKEN_FILE
from requests import Session

class Api():
  """Class for interacting with the ed API"""

  def __init__(self, saved_token: str = None):
    self.s = Session()

    if saved_token:
      # Try to renew saved token
      try:
        ed_token = self.renew_token(saved_token)
        self.set_token(ed_token)
        return
      except Exception as e:
        print("Error reusing saved token...")
        print(e)
    
    self.get_new_token()

  def get_new_token(self):
    """Prompts the user to login with CalNetID and sets a new token"""
    sso_url = self.get_sso_url()
    login_token = get_login_token(sso_url)
    print(f"Extracted login token: <{login_token}>")
    if login_token is None:
      print("Error extracting login token...")
      exit(1)
    ed_token = self.get_ed_token(login_token)
    self.set_token(ed_token)

  def get_sso_url(self) -> str:
    """Gets a link to log in to ed with a CalNetID"""

    r = self.s.post(BASE_URL + "/login_type", json={"login": "@berkeley.edu"})
    r.raise_for_status()

    return r.json()["url"]

  def get_ed_token(self, login_token: str) -> str:
    """
    Sends a post request to /login_token
    consuming the login_token and returning the token ed expects
    """
    # TODO: investigate occasional 404 error, do I need to wait a little bit?

    r = self.s.post(BASE_URL + "/login_token", json={"login_token": login_token})
    r.raise_for_status()

    return r.json()["token"]

  def renew_token(self, old_token):
    """Sends a post request to /renew_token at re-login"""
    self.s.headers.update({"X-Token": old_token})
    r = self.s.post(BASE_URL + "/renew_token")
    r.raise_for_status()

    return r.json()["token"]

  def set_token(self, token):
    """Sets the token in the session, saving it to a file"""
    self.s.headers.update({"X-Token": token})

    with open(TOKEN_FILE, "w") as f:
      f.write(token)

  def get_user(self) -> User:
    r = self.s.get(BASE_URL + "/user")
    r.raise_for_status()

    return User(r.json())

  def get_unread_threads(self, course_id, limit: int = 30) -> 'list[int]':
    """Returns a list of unread thread ids"""
    r = self.s.get(
      BASE_URL + f"/courses/{course_id}/threads", 
      params={
        "filter": "unread",
        "limit": limit,
        "sort": "new"
      })
    r.raise_for_status()

    return [thread["id"] for thread in r.json()["threads"]]

  def read_thread(self, thread_id):
    """Sends a post request to read the given thread"""
    r = self.s.post(BASE_URL + f"/threads/{thread_id}/read")
    r.raise_for_status()