from settings import APP_NAME, CODE_LENGTH
from generator import create_code
from registry import Registry
from link import Link
from sample_urls import URLS
from analytics import report
from history import record, show

registry = Registry()

print("=" * 35)
print(APP_NAME)
print("=" * 35)

for title, url in URLS:

    code = create_code(CODE_LENGTH)

    link = Link(
        title,
        url,
        code
    )

    registry.add(link)

registry.all()[0].open()
registry.all()[0].open()
registry.all()[1].open()
registry.all()[2].open()
registry.all()[2].open()

for link in registry.all():

    record(link.code)

    print(link.title)
    print(f"Short URL: {link.code}")
    print(f"Visits: {link.visits}")
    print()

report(registry.all())

show()
