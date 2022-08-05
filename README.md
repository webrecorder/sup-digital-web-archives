# Stanford University Press Digital Publication Web Archives

This repository contains the site for [https://sup.webrecorder.net/](https://sup.webrecorder.net/)

The site includes **8** web archives of [SUP Digital](https://www.sup.org/digital/) publications,
presented using the [ReplayWeb.page](https://replayweb.page) browser-based replay system.

The site embeds the web archives loaded from static storage in the browser and can be hosted on any web server.

The web archives are stored using the new [WACZ](https://github.com/webrecorder/wacz-format) format, which contains WARCs, indexes and other
metadata about the archive all in one file.


## Publications

The site contains the following publications:

  1. [Enchanting the Desert](https://sup.webrecorder.net//enchanting-the-desert.html) - (Web Archive File: [Download WACZ](https://dh-preserve.sfo2.cdn.digitaloceanspaces.com/webarchives/sup/etd.wacz))

  2. [Filming Revolution](https://sup.webrecorder.net//filming-revolution.html) - (Web Archive File: [Download WACZ](https://dh-preserve.sfo2.cdn.digitaloceanspaces.com/webarchives/sup/fr.wacz))

  3. [Black Quotidian](https://sup.webrecorder.net//black-quotidian.html) - (Web Archive File: [Download WACZ](https://dh-preserve.sfo2.cdn.digitaloceanspaces.com/webarchives/sup/bq.wacz))

  4. [When Melodies Gather](https://sup.webrecorder.net//when-melodies-gather.html) - (Web Archive File: [Download WACZ](https://dh-preserve.sfo2.cdn.digitaloceanspaces.com/webarchives/sup/wmg.wacz))

  5. [Constructing the Sacred](https://sup.webrecorder.net//constructing-the-sacred.html) - (Web Archive File: [Download WACZ](https://dh-preserve.sfo2.cdn.digitaloceanspaces.com/webarchives/sup/cts2.wacz))

  6. [The Chinese Deathscape](https://sup.webrecorder.net//the-chinese-deathscape.html) - (Web Archive File: [Download WACZ](https://dh-preserve.sfo2.cdn.digitaloceanspaces.com/webarchives/sup/tcd2.wacz))

  7. [Feral Atlas](https://sup.webrecorder.net//feral-atlas.html) - (Web Archive File: [Download WACZ](https://dh-preserve.sfo2.cdn.digitaloceanspaces.com/webarchives/sup/fa.wacz))

  8. [Shadow Plays](https://sup.webrecorder.net//shadow-plays.html) - (Web Archive File: [Download WACZ](https://dh-preserve.sfo2.cdn.digitaloceanspaces.com/webarchives/sup/sp-v2.wacz))



## Deploying

To deploy the site, simply clone this repository or download the ZIP and put the site on a web server.

(Or start a local web server, eg. `python -m http.server 8080`)

No additional setup is needed!


## Updating

To simplify updating the site, running `python generate.py` will regenerate all of the pages using the data and templates.

The site is generated from a combination of a JSON data file and templates.


### Data File and Templates

The repository contains the following data files:
 - The projects json: [data/projects.json](data/projects.json)

 - Templates (for this README, index page and project pages): [templates/](templates/)


### Update web archive paths

The data JSON specifies the location of the hosted web archive (WACZ) files.

The files are too big to be in git but can be placed on any cloud or local storage.

To update the location of the WACZ files, simply update the `sourceUrl` paths in the [data/projects.json](data/projects.json)


### Update the site pages

To update the site UI, simply change the [templates/proj-template.html](templates/proj-template.html) for the project pages and
[templates/index-template.html](templates/index-template.html)


### Updating the version of ReplayWeb.page

The site is configured to use the latest release of [ReplayWeb.page](https://replayweb.page)

To build with a different version specify the version from which to load replayweb.page, ex: `python generate.py -p https://replayweb.page/`


### Updating the Domain

To change the links to be on a different domain than `https://sup.webrecorder.net/`, simply run with `python generate.py -d https://sup.webrecorder.net/` or change the default domain in [generate.py](/generate.py)
