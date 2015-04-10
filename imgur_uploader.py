from imgurpython import ImgurClient

import click
import os

@click.command()
@click.argument('gif', type=click.Path(exists=True))
def upload_gif(gif):
    """Uploads an image file to Imgur"""

    client_id = os.environ.get('IMGUR_API_ID')
    client_secret = os.environ.get('IMGUR_API_SECRET')

    if client_id is None or client_secret is None:
        click.echo('Cannot upload - could not find IMGUR_API_ID or IMGUR_API_SECRET environment variables')
        return

    client = ImgurClient(client_id, client_secret)

    click.echo('Uploading file {}'.format(click.format_filename(gif)))

    response = client.upload_from_path(gif)

    click.echo('File uploaded - see your gif at {}'.format(response['link']))

if __name__ == '__main__':
    upload_gif()

