import csv

FILE = 'contacts.csv'

def add(name, phone):
    with open(FILE, 'a', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow([name, phone])

def find(name):
    out = []
    with open(FILE, 'r', encoding='utf-8') as f:
        r = csv.reader(f)
        for row in r:
            if name.lower() in row[0].lower():
                out.append(row)
    return out

if __name__ == '__main__':
    add('Alice', '123')
    print(find('Alice'))
