# Error running VMTK Development version (vmtkcenterlines)

**Topic ID**: 28371
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/error-running-vmtk-development-version-vmtkcenterlines/28371

---

## Post #1 by @Lorenzo_Civilla (2023-03-14 11:40 UTC)

<p>Dear all,</p>
<p>I installed VMTK Development version on a VirtualMachine running Ubuntu 22.04.2. There I installed the latest versions of the dependencies of Git, Pyhton3, CMake and g++. The problem I have occurs when I run vmtkcenterlines: I manage to pick the source points and proceed by pressing “q”, but then the window that opens is completely freezed and executes in loop the lines</p>
<pre><code class="lang-auto">while any == 0:
    self.InitializeSeeds()
    self.vmtkRenderer.Render()
    any = self.PickedSeedIds.GetNumberOfIds()
</code></pre>
<p>It looks like the target points are already considered as picked after the assignement of the source point. Could you help me with this issue?</p>

---
