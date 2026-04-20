import random
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, body):
        index_score = []
        for score in self.scores:
            if score == body:
                index_score.append(self.scores.index(score))
        return index_score

    def get_sorted(self):
        scores = self.scores.copy()
        count = len(scores) - 1
        while count > 0:
            for i in range(count):
                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]
            count -= 1
        return scores

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    result = results.scores
    print(results.count())
    for i in range(results.count()):
        print(f"Student: {i}: {result[i]} points - {results.get_grade(i)}")
    print(f"Student s plným počtem bodů měl index: {results.find(100)}")
    print(results.get_sorted())


    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

main()