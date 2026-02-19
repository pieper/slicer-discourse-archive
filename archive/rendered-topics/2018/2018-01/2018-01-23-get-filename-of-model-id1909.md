---
topic_id: 1909
title: "Get Filename Of Model"
date: 2018-01-23
url: https://discourse.slicer.org/t/1909
---

# Get filename of model

**Topic ID**: 1909
**Date**: 2018-01-23
**URL**: https://discourse.slicer.org/t/get-filename-of-model/1909

---

## Post #1 by @Frederic (2018-01-23 15:53 UTC)

<p>Hi all,<br>
Is there a way to have the filename of the data.stl loaded (like for the name ‘model.GetName()’)?<br>
Thanks in advance!</p>

---

## Post #2 by @pieper (2018-01-23 16:08 UTC)

<p>Yes, something like:</p>
<blockquote>
<blockquote>
<blockquote>
<p>s = getNode(‘Model’)<br>
s.GetStorageNode().GetFileName()</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #3 by @Frederic (2018-01-23 16:29 UTC)

<p>Thanks for your quick reply Steve.</p>

---
