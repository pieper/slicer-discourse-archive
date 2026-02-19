---
topic_id: 22228
title: "How Do I Clear All The Nodes So That It Looks Like It Just S"
date: 2022-03-01
url: https://discourse.slicer.org/t/22228
---

# How do I clear all the nodes so that it looks like it just started to run?

**Topic ID**: 22228
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/how-do-i-clear-all-the-nodes-so-that-it-looks-like-it-just-started-to-run/22228

---

## Post #1 by @yllgl (2022-03-01 06:57 UTC)

<p>I just want to use python to help me do some jobs on some patients’ data. Each patient data is independent, and to prevent interference between data while the code is running, I want to be able to clear all currently saved state nodes after processing a patient data.</p>

---

## Post #2 by @yllgl (2022-03-01 09:34 UTC)

<p>I have solved this.</p>
<pre><code class="lang-python">if slicer.mrmlScene:
    tmpdict = slicer.util.getNodes(useLists=True)
    for name,tmplist in tmpdict.items():
        for node in tmplist:
            slicer.mrmlScene.RemoveNode(node)
</code></pre>

---

## Post #3 by @ebrahim (2022-03-01 10:58 UTC)

<p>I think your code would delete all the singleton nodes like the view nodes, etc.</p>
<p>This should achieve the same thing without deleting those:</p>
<pre data-code-wrap="py"><code class="lang-nohighlight">slicer.mrmlScene.Clear()
</code></pre>

---
