# Add UPTIME checks on Pingdom
Simple python script to list and create UPTIME checks on Pingdom.

## How to use:

### Libs used:
argparse
sys
json
requests
urllib.parse import urlparse


### URLs file

You can see the URL-list-file-example.txt Basically it's a simple CSV file with 2 objects (Name and Complete URL), for eg:
Website 1,[https://www.site1.com](https://www.site1.com)

### Running the script

#### Run without arguments

    python add_uptime_pingdom.py  usage: add_uptime_pingdom.py [-h] [-l] [-a] [-f filePath]
    
    Create UPTIME checks at Pingdom
    
    optional arguments:   -h, --help            show this help message and exit   -l, --list            List UPTIME checks from Pingdom   -a,
    --add             Add new entries, requires additional args for file
                            path   -f filePath, --file filePath
                            Path for the URL lists file, requires -a/--add arg

#### Adding new checks with file named list.txt

```

# python add_uptime_pingdom.py -a -f ~/Dekstop/list.txt

Added: 6611358 - Website 1 - [https://www.site1.com](https://www.site1.com)

Added: 6611359 - Website 2 - [https://wwww.site2.com](https://wwww.site2.com)

Added: 6611360 - Website 3 - [https://www.site3.com/test/pages](https://www.site3.com/test/pages)

----------

Total new checks added: 3

```

#### Listing the current checks:
```

# python add_uptime_pingdom.py -l

Here are the current checks: ID: 6611358 - Name: Website 1 - Status: unknown ID: 6611359 - Name: Website 2 - Status: unknown ID: 6611360 - Name: Website 3 - Status: unknown

----------

Total: 3

```

## To-Do (Wishlist)

- Improve the way we define check property, maybe setting in the file, so we can set different properties by each check.
