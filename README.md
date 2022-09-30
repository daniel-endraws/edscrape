# edscrape

A python script to view every single unread post on ed.

## Dependencies

*ON WINDOWS*

Requires python 3.8. 

Using `pythonnet` 3.0.0 should allow you to use a higher version of python (as per [this reply](https://github.com/r0x0r/pywebview/issues/868#issuecomment-1250769488)), but I got a similar bug to [this post](https://stackoverflow.com/questions/70640459/python-pywebview-webview-start-system-nullreferenceexception-object-reference), which shockingly wasn't solved by the SO comment.  

## Installation

```shell
$ pip install .
```

## Usage

Ensure the place `pip` installed is on your path, and execute by running the installed package
```shell
$ edscrape
```

## Resources

- Debug requests using [this](https://stackoverflow.com/questions/10588644/how-can-i-see-the-entire-http-request-thats-being-sent-by-my-python-application)