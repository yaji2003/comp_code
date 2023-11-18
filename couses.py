def course_schedule(n, prerequisites):
    max_course = max(max(prereq) for prereq in prerequisites) + 1
    graph = [[] for _ in range(max_course)]

    for pre in prerequisites:
        graph[pre[1]].append(pre[0])

    visited = set()
    path = set()
    order = []

    for course in range(max_course):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path, order, visited):
                return False
    return True

def dfs(graph, vertex, path, order, visited):
    path.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor in path:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            if not dfs(graph, neighbor, path, order, visited):
                return False

    path.remove(vertex)
    order.append(vertex)
    return True

# Taking user input for number of prerequisites and prerequisites
num_prerequisites = int(input("Enter the number of prerequisites: "))
prereq = []
print("Enter prerequisites as pairs (course, prerequisite):")
for _ in range(num_prerequisites):
    course, pre = map(int, input().split())
    prereq.append((course, pre))

result = course_schedule(num_prerequisites, prereq)
if result:
    print("It is possible to finish all courses.")
else:
    print("Cannot finish all courses due to cycle in prerequisites.")