import os
class Counter:
    def __init__(self, results_path):
        self.results_path = results_path

    def count(self):
        file1 = open(self.results_path, 'r')
        lines = file1.readlines()
        ids = set()
        for line in lines:
            curr_id = int(line.split(',')[1])
            ids.add(curr_id)
        print(sorted(ids))
        print("Number of people occured in the seq is " + str(len(ids)))

if __name__ == '__main__':
    counter = Counter(os.path.join('./output', 'results.txt'))
    counter.count()

