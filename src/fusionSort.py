from math import sqrt


def getDistance(startPoint, endPoint):
    # X et Y de la tourelle
    endX = endPoint.x
    endY = endPoint.y
    # X et Y des particules
    startX = startPoint.x
    startY = startPoint.y
    # Calcul de la distance (delta X / delta Y)
    dist = sqrt((startX - endX) ** 2 + (startY - endY) ** 2)
    return dist, [startX, startY]


def fusion(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def fusionSort(list):
    if len(list) < 2:
        return list

    mid = len(list) // 2
    left = fusionSort(list[:mid])
    right = fusionSort(list[mid:])

    return fusion(left, right)


def fusionSortDistances(startPoints, endPoint, nbDistances=3):
    distances = []
    distancesPoints = {}
    pointsClass = {}
    for point in startPoints:
        dist, closePoint = getDistance(point, endPoint)
        distances.append(dist)
        distancesPoints[dist] = closePoint
        pointsClass[point] = closePoint
    distancesSorted = fusionSort(distances)
    closestPoints = []
    closestPointsClass = []
    for dist in distancesSorted[:nbDistances]:
        closestPoints.append(distancesPoints[dist])
        for pointClass in pointsClass.keys():
            if pointsClass[pointClass] == distancesPoints[dist]:
                closestPointsClass.append(pointClass)
    return closestPoints, closestPointsClass
