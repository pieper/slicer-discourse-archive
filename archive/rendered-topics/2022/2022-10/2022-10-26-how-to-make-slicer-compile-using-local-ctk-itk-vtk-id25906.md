# How to make slicer compile using local ctk, itk, vtk

**Topic ID**: 25906
**Date**: 2022-10-26
**URL**: https://discourse.slicer.org/t/how-to-make-slicer-compile-using-local-ctk-itk-vtk/25906

---

## Post #1 by @miniminic (2022-10-26 02:28 UTC)

<p>For example, I modified ctk to implement the control style I wanted, but slicer was first compiled by downloading the latest ctk from the web. How do I get slicer to use the local ctk.</p>

---

## Post #2 by @pieper (2022-10-26 11:25 UTC)

<p>Slicer’s build system is not extensively documented, but all the source code is available for inspection and it uses community standard tools like CMake and git.  We suggest following the documented build instructions carefully to avoid complicated debugging, but if you want to do something custom you’ll want to get very comfortable with all the build tools and libraries.</p>

---

## Post #3 by @jcfr (2022-10-26 12:47 UTC)

<p>To use a local copy of most of the external project, you could (re-)configure the Slicer top-level project passing options like:</p>
<pre><code class="lang-auto">cmake \
  -DSlicer_${proj}_GIT_REPOSITORY:STRING=file:///path/to/local/project-src \
  -DSlicer_${proj}_GIT_TAG:STRING=master \
  ...
</code></pre>
<p>where <code>${proj}</code> is the name of the project.</p>
<p>Inspecting the <code>External_${proj}.cmake</code> file found in the <a href="https://github.com/Slicer/Slicer/tree/main/SuperBuild">SuperBuild</a> folder may help understand which project support this.</p>

---

## Post #4 by @miniminic (2022-10-27 06:17 UTC)

<p>Ok, thank you very much. I’ll go back and try it</p>

---
