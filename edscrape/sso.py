import webview

def get_login_token(url) -> str:
  login_token = None
  print("Login with CalNetID in the opened window")
  window = webview.create_window("Login with CalNetID", url)

  def on_loaded():
    nonlocal login_token
    url: str = window.get_current_url()

    if "_logintoken" in url:
      # URL https://edstem.org/us?_logintoken=<TOKEN>
      login_token = url.split("=")[1]
      window.destroy()
  
  window.events.loaded += on_loaded

  # Blocks until completed
  webview.start()
  return login_token