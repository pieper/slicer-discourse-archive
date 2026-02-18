# Internalerror in findedge() TetGen Problem

**Topic ID**: 22193
**Date**: 2022-02-26
**URL**: https://discourse.slicer.org/t/internalerror-in-findedge-tetgen-problem/22193

---

## Post #1 by @19lollo95 (2022-02-26 11:01 UTC)

<p>Hello everyone,<br>
I’m having trouble using the command “vmtkmeshgenerator” to obtain internal tetrahedral mesh, in particular starting with this command:</p>
<p><code>vmtk vmtkmeshgenerator -ifile sup3.vtp -skipremeshing 1 -volumeelementfactor 1 -ofile mesh.vtu</code></p>
<p>I obtain the following output:</p>
<pre><code class="lang-auto">...
...
Duplicating background mesh.
Internalerror in findedge():  Unable to find an edge in subface.
ERROR: In ../vtkVmtk/Misc/vtkvmtkTetGenWrapper.cxx, line 431
vtkvmtkTetGenWrapper (0x7fa3b27ef170): TetGen quit with an exception.
...
</code></pre>
<p>What do you suggest me to do?<br>
Thanks in advance.</p>

---
