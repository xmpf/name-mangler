## name-mangler

Quick and dirty script to generate combinations for usernames and e-mails from full names (scraped from LinkedIn or other sources).

```
usage: name-mangler [-h] [-o OUTPUT] [-f FILE] [--format [{john.doe,j.doe,johndoe,jdoe,john.d,johnd,doe.john,d.john,doejohn,djohn,doe.j,doej} ...]] [--all-formats] [-s SUFFIX]

generate combinations

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file
  -f FILE, --file FILE  File that contains full names
  --format [{john.doe,j.doe,johndoe,jdoe,john.d,johnd,doe.john,d.john,doejohn,djohn,doe.j,doej} ...]
                        Format of the generated output
  --all-formats         Select all available formats
  -s SUFFIX, --suffix SUFFIX
                        Add a suffix
```

