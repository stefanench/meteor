def report(links):

    total = sum(
        link.visits
        for link in links
    )

    print("-" * 30)
    print(f"Stored Links: {len(links)}")
    print(f"Total Visits: {total}")

    popular = max(
        links,
        key=lambda x: x.visits
    )

    print(
        f"Most Popular: {popular.title}"
    )
