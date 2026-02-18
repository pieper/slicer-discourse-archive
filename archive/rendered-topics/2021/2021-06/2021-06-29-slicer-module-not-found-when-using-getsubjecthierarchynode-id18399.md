# Slicer module not found when using GetSubjectHierarchyNode

**Topic ID**: 18399
**Date**: 2021-06-29
**URL**: https://discourse.slicer.org/t/slicer-module-not-found-when-using-getsubjecthierarchynode/18399

---

## Post #1 by @nchaves (2021-06-29 15:07 UTC)

<p>Hi,</p>
<p>I was trying to get all the children of a folder in the subject hierarchy node using the convenience method slicer.mrmlScene.GetSubjectHierarchyNode. It didn’t work and I got the error:</p>
<ul>
<li>NameError: name ‘slicer’ is not defined</li>
</ul>
<p>Inspecting Slicer’s repo (I think this is the place to look in, but I’m not sure: <a href="https://github.com/Slicer/Slicer/blob/1807944b939b81145ec2a049ef088e0d59d5039f/Base/Python/slicer/util.py#L1367" class="inline-onebox" rel="noopener nofollow ugc">Slicer/util.py at 1807944b939b81145ec2a049ef088e0d59d5039f · Slicer/Slicer · GitHub</a>) I found which is, perhaps, the problem. It seems like that function is lacking the “import slicer” statement.</p>
<p>I’m relatively new to slicer so I’m not sure if this is correct. If it is, is there something I can do to patch it up? If not, could you please show me how to use this function?</p>
<p>Thank you very much in advance for your answers! Cheers,</p>
<p>Nicolas</p>

---

## Post #2 by @lassoan (2021-06-30 02:20 UTC)

<p>What Python environment have you tried to run your code in?</p>
<p>In Slicer’s Python interpreter <code>slicer</code> package is already imported, but maybe in your module’s scope you need to call <code>import slicer</code> first.</p>

---

## Post #3 by @nchaves (2021-06-30 05:54 UTC)

<p>Thank you for your reply Andras!</p>
<p>I now realized I didn’t write the correct function that is not working for me, which is slicer.util.getSubjectHierarchyItemChildren()</p>
<p>I am using Slicer’s Python interpreter in Slicer 4.11.20210226 r29738 / 7a593c8</p>
<p>To reproduce the error, you just need to write that function in the interpreter, after which I get the error mentioned before.</p>
<p>I also tried importing slicer before running that command, but it keeps throwing the same error. If I copy the function in the GitHub link that I provided in the interpreter, everything works, so I am not sure why it is having trouble finding the slicer module.</p>

---

## Post #4 by @lassoan (2021-06-30 12:22 UTC)

<p>Good catch, somehow the <code>import slicer, vtk</code> statement was missed in that function. I’ve <a href="https://github.com/Slicer/Slicer/commit/aaa9f918a4ee4f35bf09e05c5d7e53d083b2e4e3">added it now</a> and the fix will be available in the Slicer Preview Release from tomorrow. You can fix this now on your computer by updating this file.</p>

---
