from src.katas.EnchantedSpellDetector import enchantedSpellDetector
import pytest 


@pytest.mark.parametrize(
    "text",
    [
        "Abra darba",
        "Mystsym",
    ]
)
def test_enchantedSpellDetector_spells(text):
    assert enchantedSpellDetector(text)


@pytest.mark.parametrize(
    "text",
    [
        "Abra ka dabra",
        "Lumos",
    ]
)
def test_enchantedSpellDetector_not_spells(text):
    assert not enchantedSpellDetector(text)
