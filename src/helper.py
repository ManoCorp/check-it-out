from integrations import fs
from templater import Templater, Types

input_formats       = ['json', 'yaml', 'xml']
output_formats      = Types.__members__.keys()
output_integration  = {
    'file': fs.File
}