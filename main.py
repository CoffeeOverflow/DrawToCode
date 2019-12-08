import click

from src.plantToCode.write_files import write_files

@click.command()
@click.option('--xml_file', help='The XML file path')
@click.option('--code_path', help='The path of the code to be written')
@click.option('--language', help=(f'The programming language of the code to be '
                                  f'written'))
def run(xml_file, code_path, language):
    """Program that writes code of an UML class diagram"""
    ### CODE HERE, use objects ##
    raise ValueError("XML part To be implemented")
    
    write_files(objects, code_path, language)


if __name__ == '__main__':
    run()
