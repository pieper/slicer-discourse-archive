# User guide and developer guide cannot be clicked and linked as distinct URL

**Topic ID**: 14042
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/user-guide-and-developer-guide-cannot-be-clicked-and-linked-as-distinct-url/14042

---

## Post #1 by @muratmaga (2020-10-14 20:04 UTC)

<p>On the read the docs page, I found it a bit awkward that I can not explicitly provide a URL for a <strong>User Guide</strong> for reference. Same for developer’s guide.</p>
<p>There are links for subsections (for example UI <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html</a>), and of course the top level page (<a href="https://slicer.readthedocs.io/en/latest/index.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/index.html</a>) but not for User Guide itself.</p>

---

## Post #2 by @pieper (2020-10-14 21:22 UTC)

<p>Yes, that is odd.  I guess something about readthedocs, but I don’t know if there’s a workaround (nothing obvious to me anyway).</p>

---

## Post #3 by @lassoan (2020-10-14 22:51 UTC)

<p>Readthedocs shows documents. It cannot render a folder. If you add “User manual” and “Developer manual” pages (some kind of overview or introduction) then that can referred to.</p>
<p>You can experiment with making any changes and submit a pull request. Automatic tests of the pull request include full documentation generation, so you can check everything before the changes are merged.</p>

---

## Post #4 by @lassoan (2020-10-29 04:16 UTC)

<p>I’ve tried to create distinct links to the “User manual” and “Developer manual”. Readthedocs does not show multiple levels of the documentation in the navigation tree, unless the user manually opens a section (this could be probably changed by customizing the theme, but then we would need to keep maintaining it, so I would avoid that).</p>
<p>Therefore, creating user and developer subsections would make the navigation bar a bit less usable (it would only show two items, so users would always need to click to open a section before seeing more content). See preview here: <a href="https://slicer--5280.org.readthedocs.build/en/5280/">https://slicer--5280.org.readthedocs.build/en/5280/</a></p>
<p>Another option would be to keep “user guide” pages in a top-level section and just move the “developer guide” one level lower (essentially, we would have “Slicer documentation” and “Developer guide” section). See preview here: <a href="https://slicer--5279.org.readthedocs.build/en/5279/">https://slicer--5279.org.readthedocs.build/en/5279/</a></p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> What do you think? Which one do you like better?</p>

---

## Post #5 by @muratmaga (2020-10-29 04:20 UTC)

<p>My vote is for number 2.</p>

---

## Post #6 by @pieper (2020-10-29 12:57 UTC)

<p>I could live with either, but I also prefer the second one because it gives you more options so you are more likely to get what you need in fewer clicks.</p>

---
