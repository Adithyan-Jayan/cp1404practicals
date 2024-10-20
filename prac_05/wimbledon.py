def read_wimbledon_data(filename):

    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(',')
            data.append(parts)
    return data


def count_champions(data):
    champions_count = {}
    for row in data:
        champion = row[2]
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1
    return champions_count


def get_countries(data):
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return sorted(countries)


def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)

    champions = count_champions(data)

    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
