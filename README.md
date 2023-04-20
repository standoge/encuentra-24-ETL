# Encuentra 24 scraper
Scraper for Encuentra24 El Salvador with `Selenium` to extract sedan cars models announcements and after be analyzed.

Project is separated in two. A notebook for extraction with Selenium and another to analyze the data extracted. Is used a `xpath.yml` file
where are defined the `xpath` sentences to use to extract required data to create the dataframes.

### Dependencies:
There are defined in `requirements.txt`.

## Extraction :brain:
Notebook is structured by sections. Here data are extracted from `Encuentra24.com`.
* Includes init instructions (dependencies, global configurations)
* Functions section, where are defined all functions used.
* Relevant cell has its respective text to explain what is happening.

## Transformation: :moon:
This section is shared in `Extraction` notebook. Here data are transformed to be consistent.
* Functions section, where are defined all functions used.
* Transformations required are explained, with a subtitle and description to explain what was the transformation applied.

## Load :chart:
Notebook is structured by sections. Here data are split to follow a start model in db (or warehouse) .

---
Enjoy :bamboo: