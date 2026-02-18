# How can I interact with the slicer internal implementation functions?

**Topic ID**: 27056
**Date**: 2023-01-05
**URL**: https://discourse.slicer.org/t/how-can-i-interact-with-the-slicer-internal-implementation-functions/27056

---

## Post #1 by @dsa934 (2023-01-05 13:50 UTC)

<p>Operating system: window 11<br>
Slicer version: slicer 4.13.0<br>
Expected behavior: python module extention<br>
Actual behavior:</p>
<p>Hi, I am a newbie in 3D image processing.</p>
<p>What I’d like to do is:<br>
I want to extend the Python module file I made to 3D slicer.<br>
However, this module needs to interact with several functions inside the 3D slicer.</p>
<p>List of necessary 3D slicer internal functions</p>
<ol>
<li>When an image is added to 3d slicer, load the corresponding image variable.</li>
<li>I want to import point (x,y,z) information that is marked through 3d sclier’s markups function.</li>
</ol>
<p>In order to access the above two functions through my module function, please let me know the function name or method that I need to refer to.</p>
<p>e.g ) from somewhere_in_3d_sclier_functinos import *bring_data_function, *bring_position_function</p>

---

## Post #2 by @rbumm (2023-01-05 14:06 UTC)

<p>The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> should get you started. There are good examples of the solution for both of your problems. Please also consult chatGPT.</p>

---
