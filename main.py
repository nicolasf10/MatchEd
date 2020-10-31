def match(students, teachers):
    matches = []
    have_match = []
    people = []

    # Iterating over all students
    for i_key, i_value in students.items():
        # Iterating over all teachers
        for n_key, n_value in teachers.items():
            possible = False

            # Adding the teacher to the total list of teachers if they're not there yet
            if n_key not in people: people.append(n_key)
            if n_key not in have_match:
                if i_key not in have_match:
                    # Checking if the student is compatible with the teacher
                    if i_value[0] in n_value[0] and i_value and i_value[1] in n_value[1] and i_value[3] == n_value[3]:
                        for y in i_value[2]:
                            if y in n_value[2]: possible = True

                    # If this match between student i and teacher n
                    if possible:
                        have_match.append(i_key)
                        have_match.append(n_key)
                        matches.append((i_key, n_key))
            if i_key not in people: people.append(i_key)

    no_match = [x for x in people if x not in have_match]

    return('Matches: {}\nAll people: {}\nHave match: {}\nNo match: {}\n'.format(matches, people, have_match, no_match))

# Nested dictionary with students
students = {
    "Tom-Garcia": {
        0: 'math',
        1: 12,
        2: ['#linear-function', '#algebra', '#slope-intercept-form'],
        3 : 'english',
        4: "I love to learn!"
    },
    "Charlotte-William": {
        0: 'chemistry',
        1: 9,
        2: ['#periodic-table', '#atoms', '#ions', '#ionic-bonds'],
        3: 'spanish',
        4: "I'm eager to learn more about chemistry today!"
    },
    "Joaquin-David": {
        0: 'english',
        1: 10,
        2: ['#grammar', '#sentence-fluency'],
        3: 'english',
        4: "English is not my first language, but looking forward to learning more."
    }
}

# Nested dictionary with teachers
teachers = {
    "Emma-Andino": {
        0: ['english', 'film'],
        1: [11, 10, 9],
        2: ['#grammar', '#plays', '#shakespeare', '#film-editing'],
        3: 'english',
        4: "English is my favorite subject, and I love to teach others about it!"
    },
    "Amelia-Hart": {
        0: ['math'],
        1: [12, 11, 10],
        2: ['#linear-function', '#algebra', '#functions', '#quadratic-functions', "#euler's-number"],
        3: 'english',
        4: "I'm eager to learn more about chemistry today!"
    },
    "Cynthia-Ricci": {
        0: ['chemistry'],
        1: [10, 11, 9],
        2: ['#atoms', '#ions', '#periodic-table'],
        3: 'spanish',
        4: "The periodic table is what I love to talk about!"
    }
}

print(match(students, teachers))
