# Default setting for different modules

**Topic ID**: 10758
**Date**: 2020-03-20
**URL**: https://discourse.slicer.org/t/default-setting-for-different-modules/10758

---

## Post #1 by @danpak94 (2020-03-20 03:54 UTC)

<p>Hi. Is there a way to change the default settings for different modules? For example, I would like:</p>
<p>Models -&gt; 3D display -&gt; Representation: Surface with Edges<br>
Model Maker -&gt; Model Maker Parameters -&gt; Filter Type: Laplacian, and so on.</p>
<p>I saw this page:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a><br>
and learned that I could update .slicerrc.py to run that change every time I start the program, but I was unable to find an example that allows me to make the changes I wanted.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2020-03-23 16:02 UTC)

<p>There has not been a way to change defaults for CLI modules, but I’ve added methods for it now (see <a href="https://github.com/Slicer/Slicer/commit/c7720dd3eee0a1ff5afd9b838a96ed1382bd9bd2">here</a>). Slicer Preview Release that you download tomorrow or later will include this feature.</p>
<p>For all other MRML nodes, you can specify default value and add to the scene as described in the script repository.</p>
<p>If you have trouble finding how to change a specific default value then let us know.</p>

---
