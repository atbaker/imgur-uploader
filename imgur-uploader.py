from imgurpython import ImgurClient

import click

client_id = 'f14f192893b2e09'
client_secret = 'bca4c5cd1e0cac6eab386ab49bdca9702c04ea88'

client = ImgurClient(client_id, client_secret)

@click.command()
@click.argument('gif', type=click.Path(exists=True))
def upload_gif(gif):
    """Uploads an image file to Imgur"""
    click.echo('Uploading file {}'.format(click.format_filename(gif)))

    response = client.upload_from_path(gif)

    click.echo('File uploaded - see your gif at {}'.format(response['link']))

if __name__ == '__main__':
    upload_gif()

