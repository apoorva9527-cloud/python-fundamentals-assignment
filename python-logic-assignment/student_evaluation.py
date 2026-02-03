def greet_student(name):
    return "Hello, " + name

def analyze_scores(scores):
    count = len(scores)
    average = sum(scores) / count
    return count, average

def get_result(avg):
    if avg >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = "Apu"
    scores = [72, 45, 89, 30, 60]

    greeting = greet_student(name)
    subjects, avg = analyze_scores(scores)
    result = get_result(avg)

    print(greeting)
    print("Subjects:", subjects)
    print("Average:", avg)
    print("Result:", result)

main()
