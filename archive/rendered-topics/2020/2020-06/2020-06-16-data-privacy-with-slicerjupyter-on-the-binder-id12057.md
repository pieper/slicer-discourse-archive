# Data privacy with SlicerJupyter on the binder

**Topic ID**: 12057
**Date**: 2020-06-16
**URL**: https://discourse.slicer.org/t/data-privacy-with-slicerjupyter-on-the-binder/12057

---

## Post #1 by @tbillah (2020-06-16 15:57 UTC)

<p>If I use the <code>binder | slicer</code> from <a href="https://github.com/Slicer/SlicerJupyter" rel="nofollow noopener">here</a>, I believe it instantiates an image of the docker container to run a Notebook for me. If I upload data to the container/virtual machine, whatever we call it–</p>
<ol>
<li>Does anyone have access to the data other than me?</li>
<li>Will my data get destroyed when I exit the Notebook?</li>
</ol>
<p>I am trying to understand how data privacy can be upheld if I use the above binder.</p>

---

## Post #2 by @lassoan (2020-06-16 16:10 UTC)

<p>By design, nobody else can access your data and data is destroyed automatically, but since it is a free service, they don’t take responsibility for anything. They don’t want to be sued if information leaks because they make a mistake or they get hacked. See this page for details: <a href="https://mybinder.readthedocs.io/en/latest/faq.html#how-does-mybinder-org-ensure-user-privacy">https://mybinder.readthedocs.io/en/latest/faq.html#how-does-mybinder-org-ensure-user-privacy</a>.</p>

---
