import click

from src.dataToCode.write_files import write_files
from src.xmlToData.drawIoXmlParser import DrawIoXmlParser


@click.command()
@click.option('--xml_file', required=True, prompt=True, type=click.File(mode='r'),
              help='The XML file path')
@click.option('--code_path', required=True, prompt=True, type=click.Path(exists=True),
              help='The path of the code to be written')
@click.option('--language', required=True, prompt=True,
              type=click.Choice(['python', 'java'], case_sensitive=False),
              help='The programming language of the code to be written')
def run(xml_file, code_path, language):
    """Program that writes code of an UML class diagram"""
    draw_io_xml_parser = DrawIoXmlParser(xml_file)
    list_of_classes, list_of_interfaces = draw_io_xml_parser.read_xml()

    objects = list_of_classes + list_of_interfaces

    write_files(objects, code_path, language)


if __name__ == '__main__':
    run()
