"""
The Quest To Unravel The Mysteries Of The Ancien Scroll

In a land where words hold secret powers, you find yourself in the midst of a
coding quest. Your mission is to develop a spell-checker, not for typos, but
for enchanted words.

The elders provide you with a scroll containing a series of mystical words,
each potentially hiding a unique charm. Your task is to write a spell-checking
algorithm that determines whether a given word possesses a special property:
the ability to maintain its essence when its letters are rearranged.

Embark on this coding adventure and unveil the hidden magic within these
cryptic words. Can you create an incantation that distinguishes the enchanting
words from the mundane ones? The elders await your solution to unlock the
linguistic mysteries of this ancient scroll!
"""


def enchantedSpellDetector(text):
    """
    Parameters
    ----------
    text: str
        Text that may or may not be a spell

    Returns
    -------
    boolean
        Whether the text is a spell or not
    """

    l, r = 0, len(text) - 1

    while l < r:

        while not text[l].isalnum():
            l += 1

        while not text[l].isalnum():
            r -= 1

        if text[l].lower() != text[r].lower():
            return False

        l += 1
        r -= 1

    return True
