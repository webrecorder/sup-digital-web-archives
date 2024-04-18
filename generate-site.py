#!/usr/bin/env python

import json
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from argparse import ArgumentParser


DEFAULT_RWP = "https://cdn.jsdelivr.net/npm/replaywebpage@2.0.0"
DEFAULT_DOMAIN = "https://sup.webrecorder.net/"


def main(args=None):
    """ Generate the html for:
        - Each project page using templates/proj-template.html
        - Index with links to each project from templates/index-template.html
    """
    parser = ArgumentParser()
    parser.add_argument("-p", "--prefix", default=DEFAULT_RWP)
    parser.add_argument("-d", "--domain", default=DEFAULT_DOMAIN)

    res = parser.parse_args(args=args)

    rwp_prefix = res.prefix.rstrip("/")

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
        res_text = template.render(project=project, rwp_prefix=rwp_prefix)
        with open(project["filename"], "wt") as fh:
            print("Generating Project ({0})".format(project["filename"]))
            fh.write(res_text)

    # generate index template
    template = env.get_template("index-template.html")
    index = template.render(projects=projects["projects"])
    with open("index.html", "wt") as fh:
        print("Generate Index (index.html)")
        fh.write(index)

    # generate README
    template = env.get_template("README-template.md")
    readme = template.render(projects=projects["projects"], domain=res.domain)
    with open("README.md", "wt") as fh:
        print("Generate README (README.md)")
        fh.write(readme)

    # generate sw
    template = env.get_template("sw.js")
    with open(os.path.join("replay", "sw.js"), "wt") as fh:
        print("Generate SW (sw.js)")
        fh.write(template.render(rwp_prefix=rwp_prefix))


if __name__ == "__main__":
    main()
