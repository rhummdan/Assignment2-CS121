from webpage import Webpage

html = """
<div>
    <p>apple Hello, <b>world</b> my name is lana it's!</p>
    <p> apple 00</p>
</div>
"""

test = Webpage("hey.com", html)
print(test.word_frequencies)
