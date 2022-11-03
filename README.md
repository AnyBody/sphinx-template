# AnyBody Sphinx template

<!-- start sphinx snippet -->

This template is used to easily create sphinx pages using Markdown. It uses the [sphinx book theme](https://sphinx-book-theme.readthedocs.io/), but can be easily changed:

Pages are written in [MyST Markdown](https://myst-parser.readthedocs.io/en/latest/) which makes it easy write basic
pages, while maintaining the full power of sphinx. 

<!-- end sphinx snippet -->


## Quickstart


<!-- start quickstart -->

All documenation files are placed in the `Docs/` subfolder. They can be moved if another directory structure if needed. 

The theme requires a few Python libraries to build. These are easily install with 
conda.

1. Install Sphinx Python build environment.

   ```text
   conda env create -f Docs/environment.yaml
   ```

2. Customize the `Docs/conf.py` file to adapt the project title names etc. .

3. To build the sphinx documenation's HTML pages run the following: 🎉

   ```
   conda activate sphinx
   cd Docs
   make html
   ```

4. Remove the `quickstart.md` file and `customize/` folder and add your own content into `index.md`. 

<!-- end quickstart -->


## Development tips/tricks

* Use vscode for development
* Install [MyST vscode extension](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) to enable syntax highlighting markdown files. 
* See the following resources for how to write pages:
  - [Markup reference](https://pradyunsg.me/furo/reference/) for basic syntax.
  - [Sphinx design](https://sphinx-design.readthedocs.io/en/furo-theme/) for adavanced html elements
