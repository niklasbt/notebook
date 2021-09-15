# notebook

This repository provides the framework for creating a digital notebook based on a [jekyll blog](https://jekyllrb.com). My intention is for this notebook to be run as a local server, with each jekyll post corresponding to a traditional notebook entry. The notebook is fully searchable, using the client-side search library [lunr.js](https://lunrjs.com).

## Set up

Install [jekyll](link) and [git](https://git-scm.com) then clone this repository:
```
$ git clone https://github.com/niklasbt/notebook
```
Then simply navigate to the folder where the local version of this repo is and run `jekyll serve` to launch the server, which is found at [http://127.0.0.1:4000](http://127.0.0.1:4000).

## Organization

The landing page of the notebook at `index.html` serves as a brief table of contents, displaying the most recent five notebook entries. The full table of contents can be accessed on the TOC page at `contents.html`. Additionally, entries can be grouped into projects, which are listed at `projects.html`.

### Creating projects and entries

At the moment, I envision a workflow based around `projects`. To create a project, use the helper script `lib/project.py` which will ask for a project name (`name`), a project nickname (`short_name`; which is the tag used to label entries as belonging to the project), and a short project description. This will create a project file `_projects/short_name.md`, which will be listed under the `Projects` page in the notebook.

Alternatively, use the helper script `lib/entry.py` and select option `0: New project` to create a new project along with its first entry. The `lib/entry.py` script can be used to create new entries assigned to existing projects as well. This script will ask for a long a short title for the entry (`title` and `short_title`), and will automatically create the markdown file `_posts/YYYY-MM-DD-short_title.md`.

#### Templates

You can also create custom entry templates, if you plan on creating cookiecutter-type entries. Simply write a markdown file with the desired boilerplate and then run the `lib/template.py` script on it, which will create a template script in `lib/templates` which will be appended to the list of available templates when using `lib/entry.py`.

Alternatively, you can create your own template manually and save it in the `lib/templates` folder. The template must be a python script containing the `get_body()` function (which is called by `lib/entry.py`):

```
def get_body():
    body = []
    ### Customization here #####################################################
    # body must be a list of strings, to be written to the output file

    ### Customization end ######################################################
    return(body)
```

An example of a more complex template file is provided in `lib/templates/reaction.py`, which is a use case I find typical in my synthetic chemistry workflow. You can, of course, create templates for whatever use case, as long as the template returns in `body` a list of strings to be appended to the entry file.
