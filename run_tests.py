"""Contains all the tests for markdown-newtab."""
from unittest import TestCase, main
from markdown import Markdown
from markdown_newtab import NewTabExtension


# pylint: disable=invalid-name, missing-docstring
class TestNewTab(TestCase):
    """Contains all the test cases for markdown-newtab."""
    def setUp(self):
        """Load markdown, and make sure that we see full diffs."""
        self.md = Markdown(extensions=[NewTabExtension()])
        self.maxDiff = None

    def assertEqualMarkdown(self, markdown, parsed):
        """Helper function; parses markdown and compares the result."""
        self.assertEqual(self.md.convert(markdown), parsed)

    def test_external_link(self):
        self.assertEqualMarkdown(
            """[one](https://ddg.gg)""",
            """<p><a href="https://ddg.gg" target="_blank">one</a></p>""",
        )

    def test_external_link_hovertext(self):
        self.assertEqualMarkdown(
            """[two](https://ddg.gg "test")""",
            """\
<p><a href="https://ddg.gg" target="_blank" title="test">two</a></p>""",
        )

    def test_external_anchor_link(self):
        self.assertEqualMarkdown(
            """[three](https://ddg.gg#p1)""",
            """<p><a href="https://ddg.gg#p1" target="_blank">three</a></p>""",
        )

    def test_local_anchor_link(self):
        self.assertEqualMarkdown(
            """[four](#part2)""",
            """<p><a href="#part2">four</a></p>""",
        )

    def test_external_reference(self):
        self.assertEqualMarkdown(
            """\
[one][un]

[un]: https://ddg.gg""",
            """<p><a href="https://ddg.gg" target="_blank">one</a></p>""",
        )

    def test_external_reference_hovertext(self):
        self.assertEqualMarkdown(
            """\
[two][deux]

[deux]: https://duck.co "test" """,
            """\
<p><a href="https://duck.co" target="_blank" title="test">two</a></p>""",
        )

    def test_external_anchor_reference(self):
        self.assertEqualMarkdown(
            """\
[three][trois]

[trois]: https://ddg.gg#p1""",
            """<p><a href="https://ddg.gg#p1" target="_blank">three</a></p>""",
        )

    def test_local_anchor_reference(self):
        self.assertEqualMarkdown(
            """\
[four][quatre]

[quatre]: #part2""",
            """<p><a href="#part2">four</a></p>""",
        )

    def test_external_short_reference(self):
        self.assertEqualMarkdown(
            """\
[one]

[one]: https://ddg.gg""",
            """<p><a href="https://ddg.gg" target="_blank">one</a></p>""",
        )

    def test_external_short_reference_hovertext(self):
        self.assertEqualMarkdown(
            """\
[two]

[two]: https://duck.co "test" """,
            """\
<p><a href="https://duck.co" target="_blank" title="test">two</a></p>""",
        )

    def test_external_anchor_short_reference(self):
        self.assertEqualMarkdown(
            """\
[three]

[three]: https://ddg.gg#p1""",
            """<p><a href="https://ddg.gg#p1" target="_blank">three</a></p>""",
        )

    def test_local_anchor_short_reference(self):
        self.assertEqualMarkdown(
            """\
[four]

[four]: #part2""",
            """<p><a href="#part2">four</a></p>""",
        )

    def test_external_autolink(self):
        self.assertEqualMarkdown(
            """<https://ddg.gg>""",
            """\
<p><a href="https://ddg.gg" target="_blank">https://ddg.gg</a></p>""",
        )

    def test_external_anchor_autolink(self):
        self.assertEqualMarkdown(
            """<https://ddg.gg#p1>""",
            """\
<p><a href="https://ddg.gg#p1" target="_blank">https://ddg.gg#p1</a></p>""",
        )

    def test_email_autolink(self):
        self.assertEqualMarkdown(
            """<address@example.com>""",
            """\
<p><a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#97;&#100;&#100;&#114;\
&#101;&#115;&#115;&#64;&#101;&#120;&#97;&#109;&#112;&#108;&#101;&#46;&#99;\
&#111;&#109;" target="_blank">&#97;&#100;&#100;&#114;&#101;&#115;&#115;&#64;\
&#101;&#120;&#97;&#109;&#112;&#108;&#101;&#46;&#99;&#111;&#109;</a></p>"""
        )


if __name__ == '__main__':
    main()
