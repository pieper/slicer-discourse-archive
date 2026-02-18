# Set identity transform on vtkOrientedGridTransform

**Topic ID**: 16012
**Date**: 2021-02-16
**URL**: https://discourse.slicer.org/t/set-identity-transform-on-vtkorientedgridtransform/16012

---

## Post #1 by @riep (2021-02-16 15:55 UTC)

<p>Hi everyone,<br>
I would like to know if there was a direct API to reset a vtkOrientedGridTransform to identity.<br>
Is there any workaround to do it?<br>
If not I was planning to set zeros in the displacement fields manually.</p>
<p>Thanks in advance for any feedback!<br>
Cheers,<br>
Pierre</p>

---

## Post #2 by @lassoan (2021-02-16 16:09 UTC)

<p>Yes, you can set displacements to 0 in the coefficient image as it is done in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a> by calling:</p>
<pre><code>imageData.GetPointData().GetScalars().Fill(0)</code></pre>

---

## Post #3 by @riep (2021-02-16 16:27 UTC)

<p>Sorry I try and let you know</p>

---

## Post #4 by @lassoan (2021-02-16 16:56 UTC)

<p>Since displacement field has 3 components, maybe you need to use <code>FillComponent(component, 0)</code> for component 0, 1, 2 (instead of just <code>Fill(0)</code>).</p>

---

## Post #5 by @riep (2021-02-17 07:45 UTC)

<p>Your solution was correct and did the job.</p>
<blockquote>
<p>transform.GetTransformToParent().GetDisplacementGrid().GetPointData().GetScalars().Fill(0)</p>
</blockquote>
<p>thanks</p>

---
