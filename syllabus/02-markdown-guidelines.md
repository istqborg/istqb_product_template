## Landing page

Data for the Landing page are defined in `metadata.yml` file as follows:

```yaml
schema: Certified Tester
level: Foundation Level
title: Example Syllabus Document
prefix: EXMPL
code: example
type: Syllabus
version: Version v0.1
date: 31 Octobver 2023
release: For internal use only
```

3rd parties can be added to the landing page by #TBD

## Paragraphs

You can write a new paragraph by writing a blank line as follows:

``` md
Here is the first paragraph.

Here is the second paragraph.
```

This will produce the following output:

Here is the first paragraph.

Here is the second paragraph.

## Line breaks

You can break a line in the middle of a paragraph by writing two spaces at the end of a line as follows:

``` md
Here is the first line of a paragraph␣␣
and here is the second line of the paragraph.
```

This will produce the following output:

Here is the first line of a paragraph  
and here is the second line of the paragraph.


## Lists

You can write an unnumbered list as follows:

``` md
* This is the first item in the list
* Folowed by a second one
* And so on, until you have them all here
```

This will produce the following output:

* This is the first item in the list
* Folowed by a second one
* And so on, until you have them all here

You can also write a numbered list as follows:

``` md
1. This is the first item in the list
1. Folowed by a second one
1. And so on, until you have them all here
```

The first number sets the sequence starting number. Every other number is ignored, but teh sequence is used.  
So it will produce the following output:

1. This is the first item in the list
1. Folowed by a second one
1. And so on, until you have them all here

## Sections {.landscape}

You can write the heading of a second-level section as follows:

``` md
## Sections
```

This will produce the same output as the heading of this section.

To display a section in a landscape layout, write `{.landscape}` next to the section heading as follows:

``` md
## Sections {.landscape}
```

This will move the section to the next page and format it the same as this section.

To make a section unnumbered, write `{-}` next to the section heading as follows:

``` md
## Unnumbered section {-}
```

This is applied e.g. in the Revision History section.

## Section references {#section-references}

To reference a section from the text of the document, first write a section identifier such as `{#section-references}` next to the section heading such as follows:

``` md
## Section references {#section-references}
```

This will produce the same output as the heading of this section.

You can reference the section from the text of the document by writing `<#section:section-references>`. This will produce the following output: <#section:section-references>.

You can also create a clickable link to the section by writing `[displayed text](#section:section-references)`. This will produce the following output: [displayed text](#section:section-references).

## Figures {#figures}

You can display a figure from the `img/` folder as follows:

``` md
![label](istqb-logo-default){width=3cm}
```

This will produce the following output:

![label](istqb-logo-default){width=3cm}

Notice that we did't need to specify the suffix of the figure, it was guessed automatically.

You can add a caption to the figure as follows:

``` md
![another-label](istqb-logo-default "Here is a caption describing the image."){width=3cm}
```

This will produce the following output:

![another-label](istqb-logo-default "Here is a caption describing the image."){width=3cm}

You can reference a captioned figure from the text of the document by writing `<#figure:another-label>`. This will produce the following output: <#figure:another-label>.

## Tables

You can write a table as follows:

``` md
 | Right | Left | Center | Default |
 |------:|:-----|:------:|---------|
 |   12  |  12  |    12  |    12   |
 |  123  |  123 |   123  |   123   |
 |    1  |  1   |     1  |   1     |
```

This will produce the following output:

 | Right | Left | Center | Default |
 |------:|:-----|:------:|---------|
 |   12  |  12  |    12  |    12   |
 |  123  |  123 |   123  |   123   |
 |    1  |  1   |     1  |   1     |

The second line of the table allows you to define the formatting of columns.
Writing `---:`, `:---`, or `:--:` will cause the cells in the column to be typeset at their natural width with either right-aligned, left-aligned, or centered content.
Writing `----` will stretch the column to the page width and left-align its content.
If you write `----` for several columns, each will stretch to a uniform portion of the remaining page width.

You can add a caption to the table as follows:

``` md
 | Right | Left | Center | Default |
 |------:|:-----|:------:|---------|
 |   12  |  12  |    12  |    12   |
 |  123  |  123 |   123  |   123   |
 |    1  |  1   |     1  |   1     |

 : Here is a caption describing the table. {#label}
```

This will produce the following output:

 | Right | Left | Center | Default |
 |------:|:-----|:------:|---------|
 |   12  |  12  |    12  |    12   |
 |  123  |  123 |   123  |   123   |
 |    1  |  1   |     1  |   1     |

 : Here is a caption describing the table. {#label}

You can reference a captioned table from the text of the document by writing `<#table:label>`. This will produce the following output: <#table:label>.

## References {#references}

You can add five types of references to your documents: standards, ISTQB documents, books, journal articles, and web pages.

First, you would define the references in file `syllabus-example/bibliography.bib` as follows:

``` bib
% Standards
@report{iso-iec:2022,
  institution = {International Organization for Standardization},
  title = {Software and systems engineering -- Software testing},
  subtitle = {Part 1: General Concepts},
  date = {2022-01},
  type = {Standard},
  volume = {2022}
}

% ISTQB documents
@misc{istqb:2023,
  title = {Certified Tester},
  subtitle = {Foundation Level Syllabus},
  date = {2023-04-21},
  note = {Version 4.0},
  keywords = {istqb}
}

% Books
@book{beizer:1990,
  author = {Boris Beizer},
  title = {Software Testing Techniques},
  year = {1990},
  publisher = {Van Nostrand Reinhold: Boston MA},
  volume = {2}
}

% Articles
@article{brykczynski:1992,
  author = {Bill Brykczynski},
  title = {A survey of software inspection checklists},
  year = {1992},
  journal = {{ACM SIGSOFT} Software Engineering Notes},
  volume = {24},
  number = {1},
  pages = {82-89}
}

% Further Reading
@online{marick:2013,
  author = {Brian Marick},
  title = {Exploration through Example},
  date = {2003-08-21},
  url = {http://www.exampler.com/old-blog/2003/08/21/},
  urldate = {2023-07-11}
}
```

You can cite the defined references in the text by writing `[@istqb:2023]`. This produces the following output: [@istqb:2023].
You can also add prefixes and suffixes to your references and chain several references together by writing `[see @beizer:1990, Chapter 5; @brykczynski:1992, Section 3]`.
This produces the following output: [see @beizer:1990, Chapter 5; @brykczynski:1992, Section 3].

Furthermore, if you want to use citations as the subject or the object of a sentence, you can write without parentheses: `@iso-iec:2022`. This produces the following output: @iso-iec:2022.
Several citations without parentheses can be stringed together by writing `@iso-iec:2022 @marick:2013`. This produces the following output: @iso-iec:2022 @marick:2013.

Cited references of all types except web pages are placed in section *References* at the end of each document.
Uncited references and web pages are placed in section *Further Reading* at the end of the document.

For further instructions on defining references, see the `Bib\LaTeX`{=tex} manual [@kime:2023, Chapter 2].

## Indexing

You can index terms by writing `[0-switch coverage]{.index}`, `[functional appropriateness]{.index}`, or `[component integration testing]{.index}`. This will produce the following output: [0-switch coverage]{.index}, [functional appropriateness]{.index}, or [component integration testing]{.index}.

Indexed terms are placed in section *Index* at the end of the document together with the page numbers on which the terms appeared.

# Architecture of the solution

This example document contains several files with different purpose and structure:

- `istqb.cls` and `markdownthemeistqb_syllabus.sty` are the `\LaTeX`{=tex} template for ISTQB documents:
    - `istqb.cls` defines the design and the `\LaTeX`{=tex} commands provided by the `\LaTeX`{=tex} template.
    - `markdownthemeistqb_syllabus.sty` defines the processing of YAML metadata and the mapping between markdown elements and `\LaTeX`{=tex} commands.
- `example.yml` is a YAML document that contains the metadata of the example document.
- `example.bib` is a `Bíb\LaTeX`{=tex} database with references, as discussed in <#section:references>.
- `example-*.md` are markdown documents that contain different parts of the text of the example document.
- `example.tex` is a `\LaTeX`{=tex} document that typesets the example document.

Here is the structure of file `example.tex`:

  1. The files `istqb.cls` and `markdownthemeistqb_syllabus.sty` with the `\LaTeX`{=tex} template are loaded:

     ``` tex
     \documentclass{istqb}
     \usepackage{markdown}
     \markdownSetup{
       import = {
         istqb/syllabus = metadata
       }
     }
     ```

  2. The file `syllabus-example/metadata.yml` with the document metadata is loaded:

     ``` tex
     % Metadata
     \markdownInput[snippet=metadata]{syllabus-example/metadata.yml}
     ```

  3. The file `syllabus-example/bibliography.bib` with references is loaded:

     ``` tex
     % References
     \addbibresource{syllabus-example/bibliography.bib}
     ```

     You may use more `\addbibresource` `\LaTeX`{=tex} commands to include additional `Bíb\LaTeX`{=tex} databases.

  4. The front matter is typeset, including the markdown documents `syllabus-example/copyright.md` and `syllabus-example/revisions.md`:

     ``` tex
     % Landing Page
     \istqblandingpage
    
     % Copyright Notice
     \markdownInput{syllabus-example/copyright.md}
    
     % Revision History
     \markdownInput[texComments]{syllabus-example/revisions.md}
    
     % Table of Contents
     \istqbtableofcontents
     ```

     Here, the `texComments` option is used to allow the breaking of long lines in the revision table using the percent sign (`%`).
     You may use more `\markdownInput` `\LaTeX`{=tex} commands to include additional markdown documents. For each `\markdownInput`
     command, you may provide options supported by the Markdown package for `\TeX`{=tex} [@novotny:2023] like `texComments` to alter the flavor
     of markdown used in the markdown document.

  5. The main matter of the document is typeset, including the markdown documents `syllabus-example/intro.md` and `syllabus-example/content.md`:

     ``` tex
     % Document Text
     \markdownInput{syllabus-example/intro.md}
     \markdownInput{syllabus-example/content.md}
     ```

     You may use more `\markdownInput` `\LaTeX`{=tex} commands to include additional markdown documents.

  6. The back matter of the document is typeset:

     ``` tex
     % Bibliography
     \nocite{*}  % Include references that are not cited in the text
     \printistqbbibliography
    
     % List of Tables
     \listoftables
    
     % List of Figures
     \listoffigures
    
     % Index
     \printindex
     ```

The example document also contains the directory `img/` with figures, as discussed in <#section:figures>.
