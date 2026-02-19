---
topic_id: 18932
title: "Slice Intersection Thickness"
date: 2021-07-26
url: https://discourse.slicer.org/t/18932
---

# Slice Intersection Thickness

**Topic ID**: 18932
**Date**: 2021-07-26
**URL**: https://discourse.slicer.org/t/slice-intersection-thickness/18932

---

## Post #1 by @jasmine-lou (2021-07-26 19:34 UTC)

<p>Hi everyone!</p>
<p>Is there any way that I could increase the slice intersection thickness? Right now I have the default red, green, and yellow crosshairs on my CTs but they appear very thin and can be hard to see. Can those crosshairs be manually edited to be more thick? Thanks!</p>

---

## Post #2 by @jamesobutler (2021-07-26 20:33 UTC)

<p>I’m assuming you may be using a higher DPI display such as a 4K or an Apple retina display.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> indicated that this could be edited with some simple coding.</p>
<aside class="quote" data-post="2" data-topic="17740">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-make-slice-intersection-line-thicker-and-change-their-color/17740/2">How to make slice intersection line thicker and change their color?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    There is no GUI for this, but Slice node is a model node and you can modify the line thickness in its display node.
  </blockquote>
</aside>

<p><a class="mention" href="/u/lassoan">@lassoan</a> Could you provide a python example to change the slice intersection thickness? I can’t seem to get a display node object from a vtkMRMLSliceNode in python.</p>

---

## Post #3 by @lassoan (2021-07-26 21:24 UTC)

<p>You need to dig into how to get the slice display nodes, but in most cases this for example will set the red slice intersection thickness to 5 points:</p>
<pre><code class="lang-python">getNode('vtkMRMLModelDisplayNode1').SetLineWidth(5)
</code></pre>

---
