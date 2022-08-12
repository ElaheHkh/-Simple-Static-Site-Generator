from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment (loader =FileSystemLoader(searchpath='./'))
template= template_env.get_template('layout.html')

with open ('article.md') as markdown_file:
    article=markdown(
        markdown_file.read(),
        extras= ['fenced-code-blocks', 'code-friendly'])
        
with open ('config.json') as config_file:
    config = load (config_file)

with open ('index.html','w' ) as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            head1=config['head1'],
            Header2=config['Header2'],
            Header3=config['Header3'],
            Header4=config['Header4'],
            paragraph1= config['paragraph1'],
            paragraph2= config['paragraph2'],
            paragraph3= config['paragraph3'],
            Level1= config['Level1'],
            Level2= config['Level2'],
            Level3= config['Level3'],
            author= config['author'],
            description= config['description'],
            code_link= config['code_link'],
            article= article
        )
    )
    
            
