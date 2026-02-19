---
topic_id: 23470
title: "Issues Building Slicer On Arch Linux"
date: 2022-05-18
url: https://discourse.slicer.org/t/23470
---

# Issues building Slicer on Arch Linux

**Topic ID**: 23470
**Date**: 2022-05-18
**URL**: https://discourse.slicer.org/t/issues-building-slicer-on-arch-linux/23470

---

## Post #1 by @tsims (2022-05-18 13:47 UTC)

<p>Hi everyone, I am having some issues installing slicer and was hoping to get some help…</p>
<p>When I go to build the latest version of Slicer, I get the following error:</p>
<pre><code class="lang-auto">In file included from /home/tsims/Documents/Slicer-git/Slicer-SuperBuild-Debug/VTK/Common/DataModel/vtkSphericalPointIterator.cxx:15:
/home/tsims/Documents/Slicer-git/Slicer-SuperBuild-Debug/VTK/Common/DataModel/vtkSphericalPointIterator.h:272:8: error: ‘unique_ptr’ in namespace ‘std’ does not name a template type
  272 |   std::unique_ptr&lt;SphericalPointIterator&gt; Iterator;
      |        ^~~~~~~~~~
/home/tsims/Documents/Slicer-git/Slicer-SuperBuild-Debug/VTK/Common/DataModel/vtkSphericalPointIterator.h:82:1: note: ‘std::unique_ptr’ is defined in header ‘&lt;memory&gt;’; did you forget to ‘#include &lt;memory&gt;’?
   81 | #include "vtkSmartPointer.h" // auto destruct
  +++ |+#include &lt;memory&gt;
   82 | 
</code></pre>
<p>Adding the <code>#include &lt;memory&gt;</code> statement as the compiler suggests will allow the code to compile, but when running the binary at the end of the process it exits with a address boundary error.</p>
<p>I was wondering if there is a compiler setting or something I’m missing to get this to work?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @tsims (2022-05-18 15:23 UTC)

<p>To add some more specifics to the errors I am getting:</p>
<p>running <code>./Slicer</code> returns</p>
<pre><code class="lang-auto">error: [/home/tsims/Documents/Slicer-git/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>And trying to manually run <code>./bin/SlicerApp-real</code> returns</p>
<pre><code class="lang-auto">fish: Job 1, './bin/SlicerApp-real' terminated by signal SIGSEGV (Address boundary error)
</code></pre>

---

## Post #3 by @chir.set (2022-05-18 16:24 UTC)

<p>I had to add the &lt;memory&gt; include in</p>
<pre><code class="lang-auto">Modules/Loadable/Markups/MRML/vtkMRMLMarkupsJsonStorageNode_Private.h

Common/DataModel/vtkSphericalPointIterator.h
</code></pre>
<p>for a successful build. It’s working flawlessly however, from a clean build. You may trash everything and restart.</p>

---

## Post #4 by @tsims (2022-05-18 19:49 UTC)

<p>Thank you so much for your advice! Resetting my local version to the latest changes and running the build again fixed the compilation issue, but it still won’t launch for some reason, giving the same errors as above but that must be something funky on my system.</p>

---
