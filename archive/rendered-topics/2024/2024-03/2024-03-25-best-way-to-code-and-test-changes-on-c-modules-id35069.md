# Best way to code and test changes on C++ modules

**Topic ID**: 35069
**Date**: 2024-03-25
**URL**: https://discourse.slicer.org/t/best-way-to-code-and-test-changes-on-c-modules/35069

---

## Post #1 by @randomizedid (2024-03-25 19:53 UTC)

<p>Hi everyone, I am new to Slicer and C++ development.</p>
<p>I have more experience with Python, and I have noticed that modifying a Python script after installation and restarting the software lets you see the change. Is there something similar for C++ (for example, is there a way to modify the C++ of the SlicerMainWindow and see the change without having to rebuild Slicer, in order to test it?</p>

---

## Post #2 by @RafaelPalomar (2024-03-26 08:33 UTC)

<p><a class="mention" href="/u/randomizedid">@randomizedid</a> C++ code needs to be compiled and this cannot be avoided. <code>qt-loadable-modules</code> usually are not that time consuming when compiling them, if you can structure your development in this way you will experience shorter compilation times.</p>
<p>If you cannot structure your development in a <code>qt-loadable-module</code>, you can still speed up the building process. The Slicer building system is structured in many build targets. The default compilation is <code>all</code>, which will try to build everything (in practice, this will go through the files and check for changes, so it is not as time consuming as a fresh compilation…still, it takes a while). However, you can build a specific target (typically that part of Slicer where you have made changes; this should already avoid building code that is not related). There is even a <code>/fast</code> version of targets, which I believe won’t resolve dependencies (this can be risky if you don’t know what you are doing). Finally, you can use <code>ccache</code> (<a href="https://discourse.slicer.org/t/speeding-up-slicer-builds-with-ccache/20497" class="inline-onebox">Speeding up Slicer builds with CCache</a> and <code>ccache</code> tip in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#configure-and-generate-the-slicer-build-project-files" class="inline-onebox" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a>). I’m not sure <code>ccache</code> is available for Windows and MAC, but it is possible to use it on GNU/Linux systems.</p>

---
