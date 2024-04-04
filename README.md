# Extract Top Articles Leading to Users Registration

A python script to process a hitlog .csv file in the following format:
```
page-name,page-url,user-id,timestamp
some_name,/some/url/,1515355866
```

## Run Steps
To run the process use python3 to execute the main script of the project (which is `extract_top_articles.py`)
Example command:
```bash
python extract_top_articles.py source_csv/hitlog.csv top_3_articles.csv 3
```

### Parameters
The process accepts 3 *positional* parameters
* Input file path (default is `source_csv/hitlog.csv`)
* Output file path (default is `top_3_articles.csv`)
* Output number of articles limit (default is `3`)

## Testing
The program is covered by fixtured tests: unit tests and functional tests. Unit tests ensure that individual components of the process work as expected, while functional tests validate the behavior of the process as a whole. You can run the tests using the following commands:

```bash        
python -m pytest
``` 
