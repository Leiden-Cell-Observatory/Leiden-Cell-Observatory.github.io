# Leiden-Cell-Observatory.github.io

This repository contains the markdown files that build the Wiki website. Any committed changes automatically trigger Github Actions to rebuild the website.

The wiki uses [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/) template for enhanced features.

## How to edit the wiki content

### Quick edits
For small changes, edit markdown files directly on the Github website.

### Local editing (recommended)
1. Install [Github Desktop](https://desktop.github.com/) to manage your repository locally
2. Clone the repository to your computer
3. Install MkDocs:
   ```bash
   pip install mkdocs mkdocs-material
   ```
4. Preview changes locally:
   ```bash
   mkdocs serve
   ```
   This command will display a URL to view the wiki in your browser. Changes to markdown files will update the preview in real-time.

### Making significant changes
While you can edit directly in the main branch, consider creating a new branch for significant changes. When complete, create a pull request to merge your changes into the main branch.

### Recommended editors
- VS Code - offers markdown preview and integrated git support
- Notepad++ - lightweight editor with basic markdown support

After editing, stage your changes and create a commit through Github Desktop or your preferred git interface.

## Repository structure

The site structure is defined in the `mkdocs.yml` file, particularly in the `nav:` section. This controls how pages are organized and displayed in the navigation menu:

```yaml
nav:
  - Home: index.md
  - Microscopes:
    - microscopes/index.md
    - IBL Microscopes: microscopes/iblmicroscopes.md
```

To add new pages or sections, edit this navigation structure accordingly.

## Markdown basics

Here are some common markdown elements used in the wiki:

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
- Another bullet point

1. Numbered item
2. Another numbered item

[Link text](https://example.com)

![Alt text for image](path/to/image.png)

`inline code`

```python
# Code block with syntax highlighting
def function():
    return True
```

For more advanced formatting features available in Material for MkDocs, refer to the [Material for MkDocs reference](https://squidfunk.github.io/mkdocs-material/reference/). This includes:

- Code blocks with syntax highlighting
- Admonitions (note, warning, info boxes)
- Content tabs
- Tables
- And many more components

## Working with images

Images should be organized in subdirectories that match the structure of your markdown files:

```
docs/
├── omero/
│   ├── getting-started.md
│   ├── getting-started/
│   │   └── images/
│   │       ├── getting-started_01.png
│   │       ├── getting-started_02.png
│   │       └── ...
```

For each markdown file (e.g., `omero/getting-started.md`), place related images in a folder with the same name, inside an `images` subdirectory (e.g., `omero/getting-started/images/`).

When naming images, use the page name followed by a sequential number (e.g., `getting-started_01.png`, `getting-started_02.png`).

Reference images in your markdown using relative paths:

```markdown
![Description of image](getting-started/images/getting-started_01.png)
```

## Linking between pages

You can link to other pages within your wiki using relative paths:

```markdown
<!-- Link to a page in the same directory -->
[Link to another page](another-page.md)

<!-- Link to a page in a subdirectory -->
[Link to a page in a subfolder](subfolder/page.md)

<!-- Link to a page in a parent directory (one level up) -->
[Link to a page one level up](../another-page.md)

<!-- Link to a page in a different directory (two levels up) -->
[Link to a page in a different section](../../different-section/page.md)
```

## Linking to specific sections

You can link to specific headings within a page using anchor links (hashtags):

```markdown
<!-- Link to a section on the same page -->
[Link to a section](#section-name)

<!-- Link to a section on another page -->
[Link to a section on another page](another-page.md#section-name)
```

Note that the section name in the link should be the heading text converted to lowercase, with spaces replaced by hyphens, and any punctuation removed.

For example, to link to a section with the heading "Setting Up Your Environment", use:
```markdown
[Link to setup section](#setting-up-your-environment)
```
