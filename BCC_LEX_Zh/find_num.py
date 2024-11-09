import os

def merge_files(a_file, b_file, output_file):
    data_a = {}
    with open(a_file, 'r', encoding='utf-8') as file_a:
        for line in file_a:
            string, number = line.strip().split('\t')
            data_a[string] = int(number)
    
    with open(b_file, 'r', encoding='utf-8') as file_b, \
         open(output_file, 'w', encoding='utf-8') as output:
        for line in file_b:
            string = line.strip()
            number = data_a.get(string, None)
            if number is not None:
                output.write(f"{string}\t{number}\n")

def main():
    a_file = 'output.txt'
    b_file = 'query.txt'
    output_file = 'query_amount.txt'

    merge_files(a_file, b_file, output_file)

if __name__ == "__main__":
    main()
