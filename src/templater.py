from jinja2 import Environment, FileSystemLoader
from jinja2.environment import TemplateStream 
import os
import enum
import pandoc
import tempfile

class Templater(object):

    def __init__(self, template_file: str, file_format: str):
        dir_path = os.path.dirname(os.path.realpath(template_file))
        self.template_name = template_file.split('/')[-1]        
        self.env = Environment(
            loader=FileSystemLoader([dir_path])
        )
        
    def handler(self, data: dict, format: int) -> TemplateStream:
        stream = self.env.get_template(self.template_name).stream(data=data)
        stream.enable_buffering(1024)
        if Types(format) == Types.MARKDOWN:
            stream.dump(open('output.md', 'w+'))
        if Types(format) == Types.PDF:
            fp = tempfile.TemporaryFile(mode='w+', encoding='utf-8')
            stream.dump(fp)
            fp.seek(0)
            doc = pandoc.read(file=fp)
            pandoc.write(doc, format='pdf', file='output.pdf')
        if Types(format) == Types.HTML:
            fp = tempfile.TemporaryFile(mode='w+', encoding='utf-8')
            stream.dump(fp)
            fp.seek(0)
            doc = pandoc.read(file=fp)
            pandoc.write(doc, format='html', file='output.html', options=['--toc', '-c', 'src/themes/cosmo.css', '--self-contained'])


class Types(enum.Enum):
    HTML = 1
    PDF = 2
    PNG = 3
    MARKDOWN = 4
    SLACK = 5
    

