import re

def process_data(data):
    r = []
    results = []

    current_radius = None
    current_gaps = []

    for line in data.split("\n"):
        if "Radius is" in line:
            if current_radius is not None:
                results.append([current_radius] + current_gaps)
            current_radius = float(re.search(r"Radius is ([\d.]+)", line).group(1))
            current_gaps = [0, 0, 0, 0]
        elif "Gap from band" in line:
            frequency_min = float(re.search(r"\(([\d.]+)\)", line).group(1))
            frequency_max = float(re.search(r"to band \d+ \(([\d.]+)\)", line).group(1))
            if current_gaps[0] == 0:
                current_gaps[:2] = [frequency_min, frequency_max]
            else:
                current_gaps[2:] = [frequency_min, frequency_max]

    if current_radius is not None:
        results.append([current_radius] + current_gaps)

    for result in results:
        r.append(",".join(map(str, result)))
    return r
