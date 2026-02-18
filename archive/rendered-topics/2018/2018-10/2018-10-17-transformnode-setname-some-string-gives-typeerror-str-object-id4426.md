# transformNode.SetName('some_string') gives TypeError: 'str' object is not callable

**Topic ID**: 4426
**Date**: 2018-10-17
**URL**: https://discourse.slicer.org/t/transformnode-setname-some-string-gives-typeerror-str-object-is-not-callable/4426

---

## Post #1 by @brhoom (2018-10-17 08:18 UTC)

<p>Hi,</p>
<p>while getName works, why setName does not work? how can one change the transform node name from script.</p>
<pre><code>            &gt;&gt; t =getNode('LinearTransform_1')
            &gt;&gt; t
            (vtkCommonCorePython.vtkMRMLLinearTransformNode)0x7f7686c06188
            &gt;&gt; tname = t.GetName()
            'LinearTransform_1'              
            &gt;&gt;t.SetName(tname)
                Traceback (most recent call last):
                 File &amp;quot;&amp;lt;console&amp;gt;&amp;quot;, line 1, in &amp;lt;module&amp;gt;
                 TypeError: 'str' object is not callable</code></pre>

---

## Post #2 by @brhoom (2018-10-17 08:35 UTC)

<p>The workaround I found is using SubjectHierarchy:</p>
<pre><code>   &gt;&gt; shn = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
   &gt;&gt; sii = shn.GetSceneItemID()
   &gt;&gt; t = shn.GetItemChildWithName(sii,'LinearTransform_1')
   &gt;&gt; shn.SetItemName(t, 'NewName')</code></pre>

---

## Post #3 by @pieper (2018-10-17 12:05 UTC)

<p>Doublecheck your steps.  This works:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; n = getNode('MRH*')
&gt;&gt;&gt; n.GetName()
'MRHead'
&gt;&gt;&gt; n.SetName('hoot')
&gt;&gt;&gt; n.GetName()
'hoot'
</code></pre>

---

## Post #4 by @brhoom (2018-10-17 12:23 UTC)

<p>Thanks for your comment. Yes it works but I had to restart Slicer. It seems there where variable conflicts. in the python interactor</p>

---
