# Optimizing Build Time and Implements in SlicerCustomAppTemplate

**Topic ID**: 36690
**Date**: 2024-06-11
**URL**: https://discourse.slicer.org/t/optimizing-build-time-and-implements-in-slicercustomapptemplate/36690

---

## Post #1 by @park (2024-06-11 02:52 UTC)

<p>Hello all,</p>
<p>I’m looking to create a working environment using SlicerCustomAppTemplate. There are three main things I want to do:</p>
<ol>
<li>Modify and add code such as .cxx files within the CustomApp/Application folder.</li>
<li>Modify and add loadable or scriptable modules in CustomApp/Modules folder.</li>
<li>Make slight modifications to the Slicer source code.</li>
</ol>
<p>However, every time I make small modifications and try to build the SlicerCustomAppTemplate project, the entire Slicer is rebuilt, which takes a long time. Is there a way to resolve this?</p>
<p>Alternatively, should I implement at the module level and only use SlicerCustomAppTemplate when packaging? In this case, how should modified implementations of Slicer’s source be applied?</p>
<p>Best,</p>

---

## Post #2 by @pieper (2024-06-13 21:35 UTC)

<p>Yes, changes to C++ code require rebuilding and that can take a while.  But at least in the main Slicer app it’s possible to only rebuild the specific shared libraries involved in the change (as long as the change is in the implementation C++ code and not in the header).  You should be able to do the same with the custom app.</p>
<p>In general it’s good to think of the C++ code as core functionality with a robust interface to implement the performance-critical parts of the code, and these can be developed and tested in isolation.  Then the Python modules assemble these features into an application-level interface that can be iteratively refined more efficiently.</p>

---
