def euclidean_distance(p1, p2):
    ans = 0

    for i in range(len(p1.position)):
        ans += (p1.position[i] - p2.position[i])**2

    return ans


def find_closest(p, population):
    min_dist = None
    closest = None

    for i in population:
        if i != p:
            dist = euclidean_distance(i, p)

            if closest is None or dist < min_dist:
                min_dist = dist
                closest = i

    return closest
