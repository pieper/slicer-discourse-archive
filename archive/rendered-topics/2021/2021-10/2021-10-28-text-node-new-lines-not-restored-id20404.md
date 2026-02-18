# Text node: new lines not restored

**Topic ID**: 20404
**Date**: 2021-10-28
**URL**: https://discourse.slicer.org/t/text-node-new-lines-not-restored/20404

---

## Post #1 by @chir.set (2021-10-28 18:51 UTC)

<p>New lines are not restored when opening a saved scene.</p>
<p>If the scene project file has the following :</p>
<pre><code class="lang-auto">&lt;Text
  id="vtkMRMLTextNode2" name="Text_1" hideFromEditors="false" selectable="true" selected="false" userTags="" text="x
y
z
" encoding="3" &gt;&lt;/Text&gt;
</code></pre>
<p>selecting Text_1 node shows ‘x y z’ without the new lines.</p>
<p>I suppose it needs a fix, thanks for looking into this.</p>

---

## Post #2 by @lassoan (2021-10-29 00:34 UTC)

<p>Good catch. It’ll be fixed in the Slicer Preview Release by tomorrow.</p>

---
