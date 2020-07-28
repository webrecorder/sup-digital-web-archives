#!/usr/bin/env python

import json
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    """ Generate the html for:
        - Each project page using templates/proj-template.html
        - Index with links to each project from templates/index-template.html
    """
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    with open(os.path.join("data", "projects.json")) as fh:
        projects = json.loads(fh.read())

    # generate project templates
    for project in projects["projects"]:
        template = env.get_template("proj-template.html")
        res = template.render(project=project)
        with open(project["filename"], "wt") as fh:
            print("Generating Project ({0})".format(project["filename"]))
            fh.write(res)

    # generate index template
    template = env.get_template("index-template.html")
    index = template.render(projects=projects["projects"])
    with open("index.html", "wt") as fh:
        print("Generate Index (index.html)")
        fh.write(index)


if __name__ == "__main__":
    main()
