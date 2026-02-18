# Recompiling Slicer with changes

**Topic ID**: 803
**Date**: 2017-08-01
**URL**: https://discourse.slicer.org/t/recompiling-slicer-with-changes/803

---

## Post #1 by @moselhy (2017-08-01 16:21 UTC)

<p>Hello,</p>
<p>I cloned the Slicer repository to C:\D\S4 and built it to C:\D\S4R using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">these instructions</a>. Then, I made a change to C:\D\S4\Applications\SlicerApp\Main.cxx. Then, I opened C:\D\S4R\Slicer.sln and clicked “Build ALL_BUILD”, and it seemed to build successfully. However, I don’t see the change that I made. Am I doing this correctly?</p>
<p>Edit: Nevermind. I saw the change.</p>
<p>Thanks</p>

---

## Post #2 by @jcfr (2017-08-01 16:44 UTC)

<p>Hi,</p>
<p>As an optimization, you could open <code>C:\D\S4R\Slicer-build\Slicer.sln</code> and only rebuild the project including the <code>Main.cxx</code> file.</p>
<p>Hth<br>
Jc</p>

---
