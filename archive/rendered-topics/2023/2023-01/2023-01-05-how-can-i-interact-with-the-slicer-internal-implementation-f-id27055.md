# How can I interact with the slicer internal implementation functions?

**Topic ID**: 27055
**Date**: 2023-01-05
**URL**: https://discourse.slicer.org/t/how-can-i-interact-with-the-slicer-internal-implementation-functions/27055

---

## Post #1 by @dsa934 (2023-01-05 13:48 UTC)

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

## Post #2 by @jcfr (2023-01-05 22:11 UTC)

<blockquote>
<p>newbie in 3D image processing</p>
</blockquote>
<p>Welcome ! And thanks for reaching out <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=12" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>Python module file I made to 3D slicer.</p>
</blockquote>
<p>To better understand where you are coming form, did you create your module following the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#create-an-extension">Create an extension</a> guide ?</p>
<p>If not, I suggest you review the content of the guide and associated links, this may help answer some of your initial questions.</p>
<blockquote>
<p>List of necessary 3D slicer internal functions</p>
</blockquote>
<p>The following sections may be helpful:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html">Developer Guide / Slicer API</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Developer Guide / Script repository</a></li>
</ul>

---
