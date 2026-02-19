---
topic_id: 18783
title: "Set Volume Rendering Options With Python"
date: 2021-07-18
url: https://discourse.slicer.org/t/18783
---

# Set Volume Rendering Options with PYTHON

**Topic ID**: 18783
**Date**: 2021-07-18
**URL**: https://discourse.slicer.org/t/set-volume-rendering-options-with-python/18783

---

## Post #1 by @Jonathan_Lesage (2021-07-18 04:47 UTC)

<p>Hello,</p>
<p>I have seen some posts and scripts in the repository for setting parameters for volume rendering, however, I cannot seem to find a way to set the Synchronize with Volumes Module and set the Scalar Opacity Mapping, that is, I’d like a way to set the following options in my slicerrc file:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d7b88f4d6059de69cafa5b50268858cd8933325.png" alt="image" data-base62-sha1="4cOwbx8h99AI8Le6bTkiW9bCKPP" width="465" height="396"></p>
<p>Also, is there a way to make the 3d volume rendering linked to the chosen volume similar to how all slice views will change if the selected volume is changed in any other slice view provided they are linked?</p>
<p>Also, can one zoom to the extent of the 3d volume easily, preferably with python?</p>
<p>Thanks,</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #2 by @pieper (2021-07-19 14:02 UTC)

<p>These instructions describe how to find the implementation for features in the GUI and map them to code:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>

---
