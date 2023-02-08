#!/usr/bin/python3
from models.base_model import BaseModel

def main():
    bm = BaseModel()
    print(bm)
    print(str(bm))
    print(bm.to_dict())

main()