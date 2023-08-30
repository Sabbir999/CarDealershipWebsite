#lab_08
#Saifur Sabbir
def get_scores_above_average(scores):
    average = sum(scores) / len(scores)
    above_average = [score for score in scores if score > average]
    return above_average

def get_max_score(scores, names):
    max_score = max(scores)
    max_index = scores.index(max_score)
    max_name = names[max_index]
    return max_score, max_name

def main():
    # Read data from scores.txt
    scores = []
    names = []
    with open('scores.txt', 'r') as file:
        for line in file:
            name, score = line.strip().split()
            names.append(name)
            scores.append(int(score))

    # Calculate required values
    num_scores = len(scores)
    max_score, max_name = get_max_score(scores, names)
    average_score = sum(scores) / num_scores
    above_average_scores = get_scores_above_average(scores)

    # Write output to output.txt
    with open('output.txt', 'w') as file:
        file.write(f'Number of Scores: {num_scores}\n')
        file.write(f'Max Score: {max_score}\n')
        file.write(f'Name with max Score: {max_name}\n')
        file.write(f'Average of Scores: {average_score:.1f}\n')
        file.write('Scores above average: ')
        file.write(' '.join(map(str, above_average_scores)))

if __name__ == '__main__':
    main()
