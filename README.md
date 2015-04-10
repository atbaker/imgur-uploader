# imgur-uploader

A simple command line client for uploading files to Imgur.

Created for my [PyCon US 2015 Docker tutorial](https://us.pycon.org/2015/schedule/presentation/312/) so that students using my cloud servers can see the gifs they create at the end of exercise 1.

This tool is open source under the [MIT License](LICENSE).

## Quickstart

### Getting Imgur API credentials

Go to https://api.imgur.com/oauth2/addclient and register a new Imgur API client. You will need an Imgur account to do this.

You can put it any valid URL for the callback URL - we won't be using it.

### Installing imgur-uploader

Installing imgur-uploader is easy. It runs on versions of Python >=2.7 or >=3.3.

1. Clone this repository
1. Install the tool with `pip install -e .`
1. Set the following environment variables using your client's credentials:
    - `IMGUR_API_ID`
    - `IMGUR_API_SECRET`

### Using imgur-uploader

Upload an image by running `imgur-uploader path/to/my.gif`

The tool return a shortened link to your uploaded gif upon completion:

```
Uploading file output.gif
...
File uploaded - see your gif at http://i.imgur.com/6WsQPpw.gif
```
