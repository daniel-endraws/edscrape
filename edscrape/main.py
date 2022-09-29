from sso import get_login_token
import requests


def get_sso_url() -> str:
  """Gets a link to log in to ed with a CalNetID"""

  r = requests.post("https://us.edstem.org/api/login_type", data={"login": "@berkeley.edu"})
  r.raise_for_status()

  return r.json()["url"]


def main():
  # TODO: check if we have a saved token, and use 
  # POST https://us.edstem.org/api/renew_token
  
  try:
    sso_url = get_sso_url()
  except IndexError as e:
    print("Error: No field 'url' in response when trying to get SSO URL")
    return
  except Exception as e:
    print("Error: Could not get SSO URL")
    print(e)
    return

  login_token = get_login_token(sso_url)


if __name__ == "__main__":
  main()