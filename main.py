import click


@click.command()
@click.option('--xml_file', help='The XML file path')
@click.option('--code_path', help='The path of the code to be written')
@click.option('--language', help=(f'The programming language of the code to be '
                                  f'written'))
def run(xml_file, code_path, language_path):
    """Program that writes code of an UML class diagram"""
    print(xml_file, code_path, language_path)
    raise ValueError("Functionality To be implemented")

if __name__ == '__main__':
    run()
