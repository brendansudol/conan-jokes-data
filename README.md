python script to fetch Conan O'Brien monologues [jokes](http://teamcoco.com/jokes); output is ~9k jokes over 6 years of shows

**regenerate**: 

(I used python 3.5)

    pip install requirements.txt
    python fetch.py

**output**:

* individual jokes stored in `output/jokes/*`
* all jokes (along with meta info) stored in `output/jokes-all.json`
* all jokes (just jokes, no meta info) stored in `output/jokes-all-clean.txt`

**sample entry**:

```json
{
  "body": "A lock of Justin Bieber's hair sold on eBay today for over $40,000. Now here's my question—do you think I should frame it or make it into a bracelet?",
  "credit-name": "Conan O'Brien",
  "hier1": "",
  "thumb": "http://cdn.teamcococdn.com/image/650x650,frame:1/monologue-s1-21d7cb1818b0e2c64c19ba2634b76e27.jpg",
  "title": "Mar 2, 2011 - A lock of Justin Bieber's hair sold on eBay today for over",
  "tags": [
    {
      "status": 1,
      "name": "Celebs",
      "tags": "",
      "type": {
        "title": "Jokes category",
        "name": "jokes",
        "id": 6
      },
      "content": 0,
      "hrefTag": "celebs",
      "tid": 7406,
      "data": null,
      "slug": "jokes/celebs",
      "description": ""
    },
    {
      "status": 1,
      "name": "Justin Bieber",
      "tags": "",
      "type": {
        "title": "Tags",
        "name": "tags",
        "id": 2
      },
      "content": 59,
      "hrefTag": "justin-bieber",
      "tid": 1013,
      "data": null,
      "slug": "category/tags/justin-bieber",
      "description": ""
    },
    {
      "status": 1,
      "name": "Ebay",
      "tags": "",
      "type": {
        "title": "Tags",
        "name": "tags",
        "id": 2
      },
      "content": 0,
      "hrefTag": "ebay",
      "tid": 6591,
      "data": [],
      "slug": "category/tags/ebay",
      "description": ""
    },
    {
      "status": 1,
      "name": "CONAN",
      "tags": "",
      "type": {
        "title": "Tags",
        "name": "tags",
        "id": 2
      },
      "content": 8,
      "hrefTag": "conan",
      "tid": 24,
      "data": null,
      "slug": "category/tags/conan",
      "description": ""
    }
  ],
  "id": 64606,
  "tag": "main",
  "thumbWithText": "http://cdn.teamcococdn.com/jokes/64606/1,1/650/jokes/mar-2-2011-a-lock-of-justin-biebers-hair-sold-on-ebay-today-for-over.jpg",
  "credit-date": "March 02, 2011",
  "slug": "jokes/mar-2-2011-a-lock-of-justin-biebers-hair-sold-on-ebay-today-for-over"
}
```