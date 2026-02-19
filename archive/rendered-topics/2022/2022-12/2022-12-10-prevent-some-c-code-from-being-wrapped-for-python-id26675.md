---
topic_id: 26675
title: "Prevent Some C Code From Being Wrapped For Python"
date: 2022-12-10
url: https://discourse.slicer.org/t/26675
---

# Prevent some C++ code from being wrapped for Python

**Topic ID**: 26675
**Date**: 2022-12-10
**URL**: https://discourse.slicer.org/t/prevent-some-c-code-from-being-wrapped-for-python/26675

---

## Post #1 by @adeguet1 (2022-12-10 16:51 UTC)

<p>Hello,</p>
<p>I have some code I’d like to NOT wrap in Python. In my extension’s MRML directory, I created some “internal” classes that should ideally not be exposed to the user. I’ve been looking at 3 options:</p>
<ul>
<li>A preprocessor defined value I could use to surround the code I don’t need to wrap using <span class="hashtag">#if</span> and <span class="hashtag">#endif</span>.   I couldn’t find anything obvious on google nor using grep on the Slicer and VTK source trees.</li>
<li>Exclude a full file using CMake source file properties. I tried <code>set_source_files_properties</code> with <code>WRAP_EXCLUDE_PYTHON 1</code> but the xxxPython.cxx file is still generated and compiled.</li>
<li>The third option I can think of is to create a separate library to hide all my private classes.  I haven’t tried yet. I fear the CMake part is not going to be trivial since I will need to compile and link against VTK/Slicer libraries but the Slicer CMake macros will likely enable Python wrapping.</li>
</ul>
<p>Any thoughts before I go deeper in this rabbit hole?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-12-10 16:55 UTC)

<p>You can skip the .h in CMakeLists.txt file (only include the .cxx) to prevent classes showing up in Python. However, I would recommend to wrap all Python classes, even if users are not expected to use them, because they may be important for you (or for your users) for testing and troubleshooting (and you may decide later to use these classes from Python).</p>

---
