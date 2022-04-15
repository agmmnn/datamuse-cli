![](https://user-images.githubusercontent.com/16024979/168290323-fa1fe5ee-2a4d-4e81-aee6-7faa6713e296.svg)

# datamuse-cli

<div align="center">

<a href="https://github.com/agmmnn/datamuse-cli">
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/agmmnn/datamuse-cli"></a>
<a href="https://pypi.org/project/datamuse-cli/">
<img alt="PyPI" src="https://img.shields.io/pypi/v/datamuse-cli"></a>

A command line interface that displays results from the Datamuse API.

</div>

## Install:

```
pip install datamuse-cli
```

## Usage:

```python
> datamuse sky
# Show results for "sky"

> datamuse sky:color
# Show results for the word "sky" related to the topic "color".

> datamuse sky:color,human
# Show results for the word "sky" related to the topics "color, human".
```

## Example Usage:

```
> datamuse thyme -m 7

 🔡synonyms/similars:                       💭evocative:
╶─────────────────────────────────────────╴╶─────────────────────────────────────────╴
 herb, oregano, rosemary, marjoram,         marjoram, oregano, thymus, eyebright,
 parsley, tarragon, fennel                  harebell, thymol, hyssop


 📣sound[saʊnd]:              🧮similar spelling:          👂rhymic:
╶───────────────────────────╴╶───────────────────────────╴╶──────────────────────────╴
 them, theme, tham, thein,    rhyme, theme, chyme, tyme,   time, paradigm, sublime,
 thiem, thieme                thymy, thome                 rhyme, prime, crime, lime


 ___ + thyme:                 thyme + ___:                 thyme...:
╶───────────────────────────╴╶───────────────────────────╴╶──────────────────────────╴
 wild, fresh, lemon, common,  oil, leaved, mixture,        thymectomy, thymene,
 little, sweet, chopped       sauce, leaf, blossoms, bank  thymelaeaceae, thyme
                                                           camphor, thymes,
                                                           thyme-leaved speedwell
```

## Arguments

```
-h, --help         show this help message and exit
-m, --max          maximum number of words to display
-v, --version      show program's version number and exit
```

## Dependencies

- [rich](https://pypi.org/project/rich/)
- [aiohttp](https://pypi.org/project/aiohttp/)
