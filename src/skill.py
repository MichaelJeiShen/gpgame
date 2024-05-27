from enum import Enum
from pygame import Vector2


class SkillArea(Enum):
    NONE = []

    """
    o
    """
    SELF = [
        Vector2(+0, +0),
    ]

    """
        +
    o + +
        +
    """
    TRIANGLE_1_3 = [
        Vector2(+1, +0),
        Vector2(+2, +1),
        Vector2(+2, +0),
        Vector2(+2, -1),
    ]

    """
    o + + + +
    """
    LINE_4 = [
        Vector2(+1, +0),
        Vector2(+2, +0),
        Vector2(+3, +0),
        Vector2(+4, +0),
    ]

    """
    + + +
    + o +
    + + +
    """
    ROUND_1 = [
        Vector2(-1, +1),
        Vector2(+0, +1),
        Vector2(+1, +1),
        Vector2(-1, +0),
        Vector2(+1, +0),
        Vector2(-1, -1),
        Vector2(+0, -1),
        Vector2(+1, -1),
    ]

class Skill:
    def __init__(self) -> None:
        self.name = ""
        self.area = SkillArea.NONE
        self.damage = 0
        self.heal = 0
    def __init__(self, name, area, damage, heal) -> None:
        self.name = name
        self.area = area
        self.damage = damage
        self.heal = heal

class FrostBolt(Skill):
    super()