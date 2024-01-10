#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """
    Print the statistics based on the accumulated data.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def process_line(line, total_size, status_codes):
    """
    Process a single line and update the total size and status codes count.
    """
    try:
        parts = line.split()
        size = int(parts[-1])
        code = int(parts[-2])
        total_size += size
        if code in status_codes:
            status_codes[code] += 1
        else:
            status_codes[code] = 1
    except ValueError:
        pass

    return total_size, status_codes

if __name__ == "__main__":
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            total_size, status_codes = process_line(line.strip(), total_size, status_codes)

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_stats(total_size, status_codes)

