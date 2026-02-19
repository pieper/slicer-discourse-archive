---
topic_id: 36168
title: "Display Transform Using Python"
date: 2024-05-15
url: https://discourse.slicer.org/t/36168
---

# Display transform using Python

**Topic ID**: 36168
**Date**: 2024-05-15
**URL**: https://discourse.slicer.org/t/display-transform-using-python/36168

---

## Post #1 by @Matteboo (2024-05-15 13:34 UTC)

<p>Hello,<br>
I’m trying to display segmentation using python just like in this image<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1ce635ac08dcaf069bb996180b5b78f736f604ff.png" alt="image" data-base62-sha1="47EAE8s8cKe70s0LM8KYdxaEBsz" width="453" height="277"></p>
<p>However, in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#display" rel="noopener nofollow ugc">doc</a>, the link to the display section is dead (<a href="http://transforms.md/#display" rel="noopener nofollow ugc">dead link</a> )</p>
<p>I can’t find doc or the code for the <strong>display</strong> part of the transform module</p>
<p>If somebody knows where the code is or where I can find documentation for the display transform part that would be very usefull</p>

---

## Post #2 by @pieper (2024-05-15 14:48 UTC)

<p>This is the full link:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#display">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#display</a></p>
<p>Where did you see the other link?  If it was in the source code these get configured to full URLs when the page is built and deployed.</p>

---

## Post #3 by @Matteboo (2024-05-15 15:36 UTC)

<p>Here is where I found the link<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#visualize-transform" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#visualize-transform</a></p>
<p>Thank you for the link, but I already found this page. I’m looking for developper information since I want to display transform in a script.<br>
I want to answer questions like<br>
“How do I programmaticaly change the scale factor?”</p>
<p>I was hoping that the dead link was a link to the Github page</p>

---

## Post #4 by @pieper (2024-05-15 15:59 UTC)

<p>There are API docs here: <a href="https://apidocs.slicer.org/main/">https://apidocs.slicer.org/main/</a></p>
<p>But generally this approach works well:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>

---

## Post #5 by @Matteboo (2024-05-16 12:14 UTC)

<p>Thank you, Imanaged to find the answer to my questions<br>
<img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji only-emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---
