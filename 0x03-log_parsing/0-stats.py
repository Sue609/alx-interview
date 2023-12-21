#!/usr/bin/python3
'''
script that reads stdin line by line and computes metrics
'''
import random
import sys


file_sizes = []
status_code_count = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
line_counter = 0

try:
    for line in sys.stdin:
        line = line.strip().split()
        if len(line) == 9:
            ip = line[0]
            _ = line[3]
            status_code = int(line[7])
            file_size = int(line[8])
            
            # Check if status code is valid
            if status_code in status_code_count:
                status_code_count[status_code] += 1
                file_sizes.append(file_size)
                line_counter += 1

            # Calculate and print stats for every 10 lines
            if line_counter == 10:
                total_file_size = sum(file_sizes)
                print(f"Total file size: {total_file_size}")
                for code in sorted(status_code_count):
                    if status_code_count[code] > 0:
                        print(f"{code}: {status_code_count[code]}")
                print()
                line_counter = 0

except KeyboardInterrupt:
    total_file_size = sum(file_sizes)
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_count):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")
