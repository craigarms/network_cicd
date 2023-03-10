from ruamel.yaml import YAML
from jinja2 import Environment, FileSystemLoader
import os
import argparse
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'YAML to config with Jinja',
                                     prog = 'jinja_renderer.py')
    parser.add_argument("tpl", help="Jinja template file")
    parser.add_argument("config", help="YAML Dictionary file")
    
    args = parser.parse_args()
    
    tpl = str(Path(args.tpl)).replace('\\','/')
    config = str(Path(args.config)).replace('\\','/')
    print(main(tpl,config))


def main(tpl, config):
    jinja = Environment(loader = FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)

    if os.path.exists(tpl) and os.path.exists(config):
        template = jinja.get_template(tpl)
    
        yaml=YAML()
        
        with open(config) as f:
            y = yaml.load(f)
        
        return template.render(y)
    else:
        return ""