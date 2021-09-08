# notebook

This repository provides the framework for creating a digital notebook based on a [jekyll blog](https://jekyllrb.com). My intention is for this notebook to be run as a local server, with each jekyll post corresponding to a traditional notebook entry.

## Set up

Install [jekyll](link), then clone this repository. Then simply navigate to the folder where the local version of this repo is and run `jekyll serve` to launch the server, which is found at [http://127.0.0.1:4000](http://127.0.0.1:4000).

## Organization

The landing page of the notebook at `index.html` serves as a brief table of contents, displaying the most recent five notebook entries. The full table of contents can be accessed on the TOC page at `contents.html`. Additionally, entries can be grouped into projects, which are listed at `projects.html`. 

### Creating projects and entries

At the moment, I envision a workflow based around `projects`. To create a project, use the helper script `create-project` which will ask for a project name (`name`), a project nickname (`short_name`; which is the tag used to label entries as belonging to the project), and a short project description. This will create a project file `_projects/short_name.md`, which will be listed under the `Projects` tab in the notebook.

Alternatively, use the helper script `create-entry` and select option `0: New project` to create a new project along with its first entry. The `create-entry` script can be used to create new entries assigned to existing projects as well. This script will ask for a long a short title for the entry (`title` and `short_title`), and will automatically create the markdown file `_posts/YYYY-MM-DD-short_title.md`.
