from math import floor


def get_angle(hour, minute):
    hour_angle = (hour % 12) * 30 + minute / 2
    minute_angle = minute * 6
    return abs(hour_angle - minute_angle)


def min_cost(hour, minute, queries, A, B, X, Y):
    total_cost = 0
    for angle in queries:
        min_cost = float('inf')
        for hour_move in [-1, 1]:
            for minute_move in [-1, 1]:
                new_hour = (hour + hour_move) % 12
                new_minute = (minute + 60 * minute_move) % 60
                cost = abs(angle - get_angle(new_hour, new_minute)) * \
                    (X * abs(hour_move) + Y * abs(minute_move))
                cost += abs(angle - 360 + get_angle(new_hour, new_minute)
                            ) * (X * abs(hour_move) + Y * abs(minute_move))
                min_cost = min(min_cost, cost)
        total_cost += min_cost
    return total_cost


if __name__ == "__main__":
    initial_time = input().split(":")
    hour, minute = map(int, initial_time)

    Q = int(input())
    A, B, X, Y = map(int, input().split())

    queries = []
    for _ in range(Q):
        queries.append(int(input()))

    print(min_cost(hour, minute, queries, A, B, X, Y))
