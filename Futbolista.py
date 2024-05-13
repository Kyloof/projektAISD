# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def trip_checker(A, B, routes, result):
    if A == B:
        result.append((A, B))
        return result

    J = A
    for i in range(A+1, B + 1):
        if i in routes[J]:
            J += 1
        else:
            if find_route(A, B, J, i, routes):
                J += 1

    if J == B:
        result.append((A, B))
    return result


def find_route(A, B, start_route, searched, routes):
    visited = set()
    stack = [start_route]

    while stack:
        current_route = stack.pop()

        if current_route < A or current_route > B:
            continue

        if searched in routes[current_route]:
            return True

        if len(routes[current_route]) == 1 and routes[current_route][0] in visited:
            continue

        visited.add(current_route)

        for route in routes[current_route]:
            if route not in visited:
                stack.append(route)

    return False


def calculate_routes(T, N):
    routes_from_K = []
    for i in range(N):
        routes_from_K.append([])
    for i in range(N):
        for j in range(N):
            if (i == T[j] and i != j):
                routes_from_K[i].append(j)
                routes_from_K[j].append(i)
    return routes_from_K


def solution(T):
    result_tab = []
    N = len(T)
    routes_from_K = calculate_routes(T, N)
    print(routes_from_K)
    for A in range(N):
        for B in range(A, N):
            result_tab = trip_checker(A, B, routes_from_K, result_tab)
    return len(result_tab)




