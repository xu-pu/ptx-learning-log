#!/usr/bin/env python

import sys


def main():

    total_len = int(sys.stdin.readline())
    fence = [int(plank) for plank in (sys.stdin.readline()).split()]
    n = int(sys.stdin.readline())
    query_list = [ (int(line[0]), int(line[1])) 
                   for line in [(sys.stdin.readline()).split() for index in range(n)]]

    delta_list = []
    delta_dict = {}

    def find_match(piece,start=0, end=total_len-1):
        piece_start, piece_end = piece
        piece_len = end-start+1
        for start_point in delta_dict[delta_list[piece_start+1]]:
            

    for index in range(total_len):
        if index == 0:
            delta_list.append(None)
            # the first plank is in the list but not indexed
        else:
            delta = fence[index]-fence[index-1]
            delta_list.append(delta)
            if delta in delta_dict:
                delta_dict[delta].append(index)
            else:
                delta_dict[delta] = [index]

    for query in query_list:
        print(find_match(query, end=query[0])+find_match(query, start=query[1]))

if __name__ == '__main__':
    main()
