import webview

def get_login_token(url):
  login_token = None
  print("Opening window")
  window = webview.create_window("Login with CalNetID", url)

  def on_loaded():
    nonlocal login_token
    url: str = window.get_current_url()

    if "_logintoken" in url:
      # URL https://edstem.org/us?_logintoken=5JsE73Q0pmtbH00a3qomgNro
      login_token = url.split("=")[1]
      window.destroy()
  
  window.events.loaded += on_loaded

  # Blocks until completed
  webview.start(debug=True)