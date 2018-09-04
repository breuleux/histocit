
# histocit

Get the history of the number of citations an author has over the years.

## Requirements

* Python >= 3.6
* `requests` and `beautifulsoup4`

Install using `pip install -r requirements.txt`


## Usage

    python histocit.py "Author Name"

Author name should be in quotes.


## Programmatic usage

The `citation_history` function takes an author name and returns a dict of year: ncit.

```python
from histocit import citation_history
print(citation_history("Author Name"))
```
