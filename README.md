# Piazza Discussion Counter

Count the number of followup discussions across posts for each student


## Description

This tool sums the following for each post and each student:
* whether a student posts a followup discussion: in {0, 1}
* the number of instrcutor's endorsement to the their followup discussions: in {0, 1, 2, ...}


## Getting Started

### Dependencies

```
python=3.8.5
```

### Installing

1. Install the requirements
```
pip install -r requirements.txt
```

2. Configure your settings in the beginning of `piazza-parser.py`
  * See the Piazza URLs of your posts for the ids: `https://piazza.com/class/<class_id>?cid=<cid>`
  * `class_id = "<class_id>"` is the id of your class
  * `cids = [<cid_1>, <cid_2>, ...]` are the ids of the posts included in the counts
  * `output_fname = "<your_file_name>.csv"` is the file name of the output csv file

### Executing program

1. Run the program
```
python3 piazza-parser.py
```
2. It will prompt `Email:` and `Password:` to you. Please enter your Piazza credentials for authorization.


## Authors

Shang-Ling Hsu [@shangling.info](http://shangling.info/)



## License

This project is licensed under the MIT License - see the LICENSE.md file for details
