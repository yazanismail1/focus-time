import pytest
from logic.functions import morse_code

def test_morse_code():
    assert morse_code("A") == ".-"
    assert morse_code("1") == ".----"
    assert morse_code("Hello") == ".... . .-.. .-.. ---"
    assert morse_code("hello") == ".... . .-.. .-.. ---"
    assert morse_code("Hello hello") == ".... . .-.. .-.. ---       .... . .-.. .-.. ---"
    assert morse_code("Hi my name is Yazan Alfarra") == ".... ..       -- -.--       -. .- -- .       .. ...       -.-- .- --.. .- -.       .- .-.. ..-. .- .-. .-. .-"
    assert morse_code(",") == ","