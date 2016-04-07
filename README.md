python script to fetch Conan O'Brien monologues [jokes](http://teamcoco.com/jokes); output is ~8k jokes over 6 years of shows

**regenerate**: 

(I used python 3.5)

    pip install requirements.txt
    python fetch.py

**output**:

* individual jokes stored in `output/jokes/*`
* all jokes (along with meta info) stored in `output/jokes-all.json`
* all jokes (just jokes, no meta info) stored in `output/jokes-all-clean.txt`
