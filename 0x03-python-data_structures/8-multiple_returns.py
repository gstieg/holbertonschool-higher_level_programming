#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length is 0:
        return (length, None)
    else:
        return (length, sentence[0])
