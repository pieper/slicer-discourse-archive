# Switch off cube and labels

**Topic ID**: 3667
**Date**: 2018-08-05
**URL**: https://discourse.slicer.org/t/switch-off-cube-and-labels/3667

---

## Post #1 by @ghoulfool (2018-08-05 20:52 UTC)

<p>Hi, I know I can switch off the wireframe 3d cube with</p>
<pre><code>    v = slicer.util.getNode("View1")
    v.SetBoxVisible(False)
</code></pre>
<p>But how do I switch off the ASLIPRA annotations as well?</p>
<p>Cheers</p>

---

## Post #2 by @lassoan (2018-08-05 21:23 UTC)

<p>This will hide axis labels: <code>v.SetAxisLabelsVisible(False)</code></p>
<p>See detailed documentation here: <a href="https://apidocs.slicer.org/master/classvtkMRMLViewNode.html">https://apidocs.slicer.org/master/classvtkMRMLViewNode.html</a></p>

---
