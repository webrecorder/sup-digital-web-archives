# Stanford University Press Digital Publication Web Archives

This repository contains the site for [https://archive.supdigital.org](https://archive.supdigital.org)

The site includes **16** web archives of [SUP Digital](https://www.sup.org/digital/) publications,
presented using the [ReplayWeb.page](https://replayweb.page) browser-based replay system.

The site embeds the web archives loaded from static storage in the browser and can be hosted on any web server.

The web archives are stored using the new [WACZ](https://github.com/webrecorder/wacz-format) format, which contains WARCs, indexes and other
metadata about the archive all in one file.


## Publications

The site contains the following publications:

  1. [Enchanting the Desert](https://archive.supdigital.org/enchanting-the-desert.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:pj930vw7523/etd.wacz))

  2. [Filming Revolution](https://archive.supdigital.org/filming-revolution.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:kv106fw2233/fr.wacz))

  3. [Black Quotidian](https://archive.supdigital.org/black-quotidian.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:rq867gk6622/bq.wacz))

  4. [When Melodies Gather](https://archive.supdigital.org/when-melodies-gather.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:yg504wh6319/yg504wh6319_wmg.wacz))

  5. [Constructing the Sacred](https://archive.supdigital.org/constructing-the-sacred.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:yj995wy0505/cts.wacz))

  6. [The Chinese Deathscape](https://archive.supdigital.org/the-chinese-deathscape.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:pg355vp4268/tcd2.wacz))

  7. [Feral Atlas](https://archive.supdigital.org/feral-atlas.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:qj089fs5316/fa.wacz))

  8. [Shadow Plays](https://archive.supdigital.org/shadow-plays.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:jy040sq1372/sp.wacz))

  9. [Layered Lives](https://archive.supdigital.org/layered-lives.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:jm374kc0685/ll.wacz))

  10. [Transmedia Stories](https://archive.supdigital.org/transmedia-stories.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:jf302kz7177/ts.wacz))

  11. [America's Public Bible](https://archive.supdigital.org/americas-public-bible.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:nw289ms9710/apb.wacz))

  12. [Ego Media](https://archive.supdigital.org/ego-media.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:kc966hg9270/em.wacz))
  
  13. [Country of Words](https://archive.supdigital.org/country-of-words.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:gw244nr4392/cw.wacz))
  
  14. [2020 Dreams](https://archive.supdigital.org/2020-dreams.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:yh739tk2490/2d.wacz))
  
  15. [Harlem in Disorder](https://archive.supdigital.org/harlem-in-disorder.html) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:nb781fd3746/hid.wacz))
  
  16. [A World Made by Travel](https://archive.supdigital.org/a-world-made-by-travel) - (Web Archive File: [Download WACZ](https://stacks.stanford.edu/file/druid:wq312tb4909/a-world-made-by-travel.wacz))


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

To change the links to be on a different domain than `https://archive.supdigital.org`, simply run with `python generate.py -d https://archive.supdigital.org` or change the default domain in [generate.py](/generate.py)
