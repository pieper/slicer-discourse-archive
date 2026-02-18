# Output in different order ar eat execution

**Topic ID**: 12447
**Date**: 2020-07-08
**URL**: https://discourse.slicer.org/t/output-in-different-order-ar-eat-execution/12447

---

## Post #1 by @MachadoL (2020-07-08 18:56 UTC)

<p>The output (features extracted and values) come in a random order every time I execute (in this <a href="https://discourse.slicer.org/u/machadol">Post</a>). It use to work well but I do not know what happened that it is now random.<br>
Any thoughts?</p>

---

## Post #2 by @fedorov (2020-07-30 20:47 UTC)

<p><a class="mention" href="/u/machadol">@MachadoL</a> the post you linked appears to be deleted. Were you able to resolve this issue?</p>

---

## Post #3 by @JoostJM (2020-07-31 04:44 UTC)

<p>PyRadiomics features are returned as a Python dictionary, which is an unordered set. The easiest way to combine features would be to use the pandas package.</p>

---

## Post #4 by @MachadoL (2020-11-18 17:20 UTC)

<p>Well, I do not know what I did, except running the script in another computer, But it worked well. Features were printed in order. Although I do recognize that <strong>THIS IS A SERIOUS ISSUE for PyRadiomics</strong>. Another friend reported the same.</p>

---

## Post #5 by @MachadoL (2020-11-18 17:21 UTC)

<p>I see. I guess that is an <strong>issue</strong>. Sometimes it works, sometimes it does not. Some friends reported the same.</p>

---
