from datetime import date

project = 'ClimateDT Evaluation'
author = 'ECMWF'
copyright = f'{date.today().year}, {author}'
release = '0.1.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = ['AQUA', 'climatedt_info.txt', '.venv']

extensions = [
    'sphinx_rtd_theme',
]

html_theme = 'sphinx_rtd_theme'
html_theme_options = {}
html_static_path = ['_static']

rst_epilog = f'''
.. |project| replace:: {project}
'''

nitpicky = True
html_css_files = [
  'service-doc.css'
]
