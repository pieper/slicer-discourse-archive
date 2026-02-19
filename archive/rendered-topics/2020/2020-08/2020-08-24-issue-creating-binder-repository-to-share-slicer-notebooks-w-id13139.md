---
topic_id: 13139
title: "Issue Creating Binder Repository To Share Slicer Notebooks W"
date: 2020-08-24
url: https://discourse.slicer.org/t/13139
---

# Issue creating binder repository to share Slicer notebooks (Wrong Kernel)

**Topic ID**: 13139
**Date**: 2020-08-24
**URL**: https://discourse.slicer.org/t/issue-creating-binder-repository-to-share-slicer-notebooks-wrong-kernel/13139

---

## Post #1 by @allihuwa (2020-08-24 09:57 UTC)

<p>Hello,</p>
<p>I am trying to run my Github repository via binder to be able to share my slicer notebook files (.ipynb) with other people. I am able to create the binder repository but when I open up a .ipynb file the default kernel is set to Python 3 and the dropdown menu does not show the Slicer 4.11 kernel for me to select as for example when I open a .ipynb file in the tutorial binder repository( <a href="https://hub.gke.mybinder.org/user/slicer-slicernotebooks-n86z0bik/tree" rel="nofollow noopener">https://hub.gke.mybinder.org/user/slicer-slicernotebooks-n86z0bik/tree</a>). Do I have to introduce some sort of requirement in a txt file or define that I want the Slicer kernel to be used?</p>
<p>github link I am trying to put on binder: <a href="https://github.com/allihuwa/Content-Production-for-Improving-Cancer-Treatment-Worklflow" rel="nofollow noopener">https://github.com/allihuwa/Content-Production-for-Improving-Cancer-Treatment-Worklflow</a></p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-08-24 14:01 UTC)

<p>To have a Slicer kernel, all you need is two small text files in the your repository’s root (<code>Dockerfile</code> and <code>start</code>) as it is one in this repository: <a href="https://github.com/Slicer/SlicerNotebooks">https://github.com/Slicer/SlicerNotebooks</a>.</p>

---
