from typing import TypeVar

Number = TypeVar('Number', int, float)


def make_rule(
        title: str,
        msg: str,
        good_threshold: Number,
        ok_threshold: Number,
        bad_threshold: Number,
) -> dict:
    return {
        "title": title,
        "message": msg,
        "good_threshold": good_threshold,
        "ok_threshold": ok_threshold,
        "bad_threshold": bad_threshold,
    }
