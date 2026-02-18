# Python code for getting current displayed slice on a red window

**Topic ID**: 35891
**Date**: 2024-05-03
**URL**: https://discourse.slicer.org/t/python-code-for-getting-current-displayed-slice-on-a-red-window/35891

---

## Post #1 by @mlh (2024-05-03 14:08 UTC)

<p>Hi all!<br>
Would you please share to me python snippet on how to get a slice index which is shown on a red window?<br>
Please point me to similar post if already answered. I couldn’t find it though.</p>
<p>Thanks a lot!</p>

---

## Post #2 by @rfenioux (2024-05-03 14:59 UTC)

<p>Do you mean the slice offset (in mm, displayed in the top right corner of the view)?<br>
If so, you can do:</p>
<pre><code class="lang-auto">redSliceNode = slicer.util.getNode('vtkMRMLSliceNodeRed')
redSliceNode.GetSliceOffset()
</code></pre>

---

## Post #3 by @mlh (2024-05-16 12:03 UTC)

<p>Alright, thanks. And how to convert it to image coordinate (IJK)? <a class="mention" href="/u/rfenioux">@rfenioux</a></p>

---
