# getFirstNodeByName() returns None when '(' or ')' is in the name

**Topic ID**: 22437
**Date**: 2022-03-10
**URL**: https://discourse.slicer.org/t/getfirstnodebyname-returns-none-when-or-is-in-the-name/22437

---

## Post #1 by @koeglfryderyk (2022-03-10 16:40 UTC)

<p>Is it a feature or a bug that slicer.util.getFirstNodeByName() returns None when parentheses are in the name of a node?</p>

---

## Post #2 by @ebrahim (2022-03-10 16:56 UTC)

<p>I don’t know if this is intended, but I think it’s because the name is being treated as a regular expression. A workaround is to escape the parentheses by preceding them with a backslash <code>\</code>.</p>
<p>For the possible cause:</p>
<ul>
<li>see how <code>exactNameMatch</code> is set to <code>False</code> <a href="https://github.com/Slicer/Slicer/blob/df215d43a1349f22f553de3a0a3929f110c13623/Base/Python/slicer/util.py#L1348" rel="noopener nofollow ugc">here</a>
</li>
<li>see regular expression thing <a href="https://github.com/Slicer/Slicer/blob/df215d43a1349f22f553de3a0a3929f110c13623/Libs/MRML/Core/vtkMRMLScene.cxx#L1943" rel="noopener nofollow ugc">here</a>
</li>
</ul>
<p>Another workaround is to call <code>vtkMRMLScene::GetFirstNode</code> yourself:</p>
<pre data-code-wrap="py"><code class="lang-nohighlight">slicer.mrmlScene.GetFirstNode(your_node_name, None, False, True)```</code></pre>

---
