---
topic_id: 16550
title: "How To Save Curvednode As Mrk Json In Python"
date: 2021-03-15
url: https://discourse.slicer.org/t/16550
---

# How to save CurvedNode as .mrk.json in python?

**Topic ID**: 16550
**Date**: 2021-03-15
**URL**: https://discourse.slicer.org/t/how-to-save-curvednode-as-mrk-json-in-python/16550

---

## Post #1 by @newtonsbm (2021-03-15 15:16 UTC)

<p>Im trying to export a CurvedNode to .mrk.json in python using Slicer in Jupyter Notebook<br>
(lassoan/slicer-notebook:2020-05-15-89b6bb5) but it only saves as fcsv format.</p>
<p>Currently Im doing:</p>
<pre><code class="lang-auto">file_path = os.path.join("saved", "markups.mrk.json")
myStorageNode = curveNode.CreateDefaultStorageNode()
myStorageNode.SetFileName(file_path)
myStorageNode.WriteData(curveNode)
</code></pre>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2021-03-27 18:14 UTC)

<p>I don’t think saving in json format was available then. You need to use a more recent Slicer version.</p>

---
