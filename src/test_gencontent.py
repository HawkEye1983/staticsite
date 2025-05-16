import unittest
from gencontent import extract_title

class Test_Extract_Title(unittest.TestCase):
    def test_one(self):
        content = "# This is a title."
        title = extract_title(content)
        self.assertEqual(title, "This is a title.")
    
    def test_two(self):
        content = """
# This is a title.

# This is a second title.
"""
        title = extract_title(content)
        self.assertEqual(title, "This is a title.")

    def test_three(self):
        content = """
# This is a title

## This is a heading

```
This is come code
```
"""
        title = extract_title(content)
        self.assertEqual(title, "This is a title")