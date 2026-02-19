---
topic_id: 10119
title: "How To Call The Slicer Python Interactor"
date: 2020-02-05
url: https://discourse.slicer.org/t/10119
---

# How to call the slicer python interactor?

**Topic ID**: 10119
**Date**: 2020-02-05
**URL**: https://discourse.slicer.org/t/how-to-call-the-slicer-python-interactor/10119

---

## Post #1 by @timeanddoctor (2020-02-05 07:08 UTC)

<p>I studied the Shortcut keys in slicer and I want to custom a KEY(not default ctrl+3) to call the slicer python interactor. Can I do it with py?<br>
Thanks!</p>

---

## Post #2 by @pieper (2020-02-05 12:33 UTC)

<p>Yes, you should be able to connect any key to call:</p>
<p><code>slicer.util.pythonShell().show()</code></p>

---

## Post #3 by @timeanddoctor (2020-02-06 05:30 UTC)

<p>Ok,<br>
Thank you very much!</p>

---
