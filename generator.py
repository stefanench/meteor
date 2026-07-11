import random
import string


def create_code(length):

    alphabet = (
        string.ascii_letters +
        string.digits
    )

    return "".join(
        random.choice(alphabet)
        for _ in range(length)
    )
