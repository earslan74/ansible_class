#!/usr/bin/env python
import yaml
from pprint import pprint


def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)

def main():
    filename = raw_input("YAML Filename: ")
    try:
        pprint(read_yaml(filename))
    except:
        print "File name is incorrect!"


if __name__ == "__main__":
    main()
