def trip_checker(A, B, routes, result):
    result.append((A, A))

    J = A
    for i in range(A + 1, B):
        if not find_route(A, B, A, i, routes):
            continue
        else:
            result.append((A, i))

    if J == B:
        result.append((A, B))
    return result


def find_route(A, B, start_route, searched, routes):
    # if searched in visited:
    #   return True
    visited = set()
    stack = [start_route]

    while stack:
        current_route = stack.pop()

        if current_route < A or current_route > searched:
            continue
        visited.add(current_route)

        if len(visited) == searched-A+1 and searched in visited:
            return True


        if len(routes[current_route]) == 1 and routes[current_route][0] in visited:
            continue

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
    for A in range(N):
        result_tab = trip_checker(A, N, routes_from_K, result_tab)

    return len(result_tab)

