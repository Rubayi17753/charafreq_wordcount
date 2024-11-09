import os

def process_files(*filenames):
    data = {}
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    string, number = line.strip().split('\t')
                    number = int(number)
                    if string in data:
                        data[string] += number
                    else:
                        data[string] = number
                except (ValueError, UnicodeDecodeError):
                    # Skip unparseable or unreadable lines
                    continue
    
    return data

def write_output(data, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as file:
        for string, number in data.items():
            file.write(f"{string}\t{number}\n")

def main():
    source_files = ['blog_wordfreq.release.txt', 'literature_wordfreq.release.txt','news_wordfreq.release.txt','technology_wordfreq.release.txt','weibo_wordfreq.release.txt']
    output_file = 'output.txt'

    processed_data = process_files(*source_files)
    write_output(processed_data, output_file)

if __name__ == "__main__":
    main()