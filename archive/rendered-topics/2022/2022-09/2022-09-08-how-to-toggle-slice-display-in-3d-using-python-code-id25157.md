# How to toggle slice display in 3D using python code?

**Topic ID**: 25157
**Date**: 2022-09-08
**URL**: https://discourse.slicer.org/t/how-to-toggle-slice-display-in-3d-using-python-code/25157

---

## Post #1 by @sunshine (2022-09-08 13:55 UTC)

<p>Hi everyone,</p>
<p>I have a question about window control using python codes.</p>
<p>What are the possible functions to call in order to to toggle slice display in 3D using python code?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17e24dbedd5e92818b1e465f16c3442b4e48249d.png" alt="image" data-base62-sha1="3phPMGVNKjeaJIA00hug3yKafGB" width="459" height="162"></p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @Sunderlandkyl (2022-09-08 14:18 UTC)

<p>You can toggle slice visibility like this:</p>
<pre><code class="lang-python">sliceNode = getFirstNodeByClassByName("vtkMRMLSliceNode", "Red")
sliceNode.SetSliceVisible(True)
</code></pre>

---

## Post #3 by @sunshine (2022-09-08 14:56 UTC)

<p>Thank you so much, Kyle!</p>

---
