from collections import Counter

def count_top_3_most_common_error(log_file):
    err_count = Counter()
    with open(log_file, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                err = line.split('ERROR')[1].strip()
                err_count[err] += 1

    return err_count.most_common(3)

if __name__ == "__main__":
    log_file = 'sample.log'
    top_errs = count_top_3_most_common_error(log_file)
    print("Top 3 most common errors:")
    for err, count in top_errs:
        print(f"{err}: {count} times")