def dfs(graph, start_number, visited, finished, cur_path):
    global number_of_students_in_team
    stack = [start_number]
    while stack:
        current_number = stack.pop()
        cur_path.append(current_number)
        visited[current_number] = True
        next_student = graph[current_number]
        if finished[next_student]:
            return
        if next_student in cur_path:
            if current_number == next_student:
                number_of_students_in_team += 1
                finished[current_number] = True
                return
            else:
                team = cur_path[cur_path.index(next_student):]
                number_of_students_in_team += len(team)
                for s in team:
                    finished[s] = True
                return
        else:
            stack.append(next_student)
T = int(input())
for _ in range(T):
    number_of_students_in_team = 0
    n = int(input())
    finished = [False] * (n + 1)
    visited = [False] * (n + 1)
    number_list = list(map(int, input().split()))
    number_list.insert(0, None)
    for student in range(1, n + 1):
        cur_path = []
        if not visited[student]:
            dfs(number_list, student, visited, finished, cur_path)
    print(n - number_of_students_in_team)