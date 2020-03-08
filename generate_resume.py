"""
generate_resume.py

Author: adoubekk

Generates my resume as HTML for use in my personal website.
"""

from Cheetah.Template import Template
import yaml

with open('resume.yaml') as resume_yaml_file:
    resume_data = yaml.full_load(resume_yaml_file.read())

with open('templates/resume.template.html') as html_template_file:
    html_template = html_template_file.read()

with open('index.html', 'w') as html_out_file:
    html_out_file.write(str(Template(html_template, searchList=resume_data)))
