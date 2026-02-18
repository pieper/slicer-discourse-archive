# Adding two volumes

**Topic ID**: 7339
**Date**: 2019-06-27
**URL**: https://discourse.slicer.org/t/adding-two-volumes/7339

---

## Post #1 by @anitakh1 (2019-06-27 12:37 UTC)

<p>i had segmented a volume from top and bottom (and hence the slices are less in this) and did some processing in segmented volume. now i want to add the original volume and this segmented volume. how can i do this? pl help</p>

---

## Post #2 by @lassoan (2019-06-28 23:01 UTC)

<p>This topic should answer your question: <a href="https://discourse.slicer.org/t/landmark-registration-and-combining-intenstities-of-fixed-and-moving-volume/7106" class="inline-onebox">Landmark registration and combining intenstities of fixed and moving volume</a></p>

---

## Post #3 by @anitakh1 (2019-07-02 11:06 UTC)

<p>i don’t understand how to do this “you can harden the transform (from the right-click menu in the Transform hierarchy of the Data module) and then use Filtering-&gt;Add Scalar Volumes.”</p>

---

## Post #4 by @lassoan (2019-07-02 17:36 UTC)

<aside class="quote no-group" data-username="anitakh1" data-post="3" data-topic="7339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>“you can harden the transform (from the right-click menu in the Transform hierarchy of the Data module) and then use Filtering-&gt;Add Scalar Volumes.”</p>
</blockquote>
</aside>
<p>Step-by-step instructions:</p>
<ul>
<li>Open Data module</li>
<li>Click on “Transform hierarchy” tab</li>
<li>Right-click on the node that you would like to harden the transform on</li>
<li>Click “Harden transform”</li>
<li>Open “Add Scalar Volumee” module (click on the module list, click Filtering category, click Arithmetic category, click Add Scalar Volumes)</li>
<li>Set input and output nodes and click Apply</li>
</ul>

---

## Post #5 by @anitakh1 (2019-07-03 06:50 UTC)

<p>sorry but when i right click on the node, it show insert transform, edit properties, rename and delete but no harden transform. i can’t find harden transform anywhere. i am working on 3Dslicer  4.10.2.</p>

---

## Post #6 by @anitakh1 (2019-07-03 10:48 UTC)

<p>one more thing. once add scalar volume is opened, i can’t see set input and output nodes there. sorry</p>

---

## Post #7 by @lassoan (2019-07-03 16:59 UTC)

<aside class="quote no-group" data-username="anitakh1" data-post="5" data-topic="7339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>sorry but when i right click on the node, it show insert transform, edit properties, rename and delete but no harden transform</p>
</blockquote>
</aside>
<p>You need to Apply the transform (by drag-and-dropping the node under a transform) before you can harden the transform on the node.</p>
<aside class="quote no-group" data-username="anitakh1" data-post="6" data-topic="7339" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>one more thing. once add scalar volume is opened, i can’t see set input and output nodes there. sorry</p>
</blockquote>
</aside>
<p>If you have scalar volumes in the scene then they should show up in node selectors in “Input volume 1” and “Input volume 2”. Normally you create a new node for output volume. Are your volumes scalar volumes or labelmap volumes (you can check the type in Volumes module / Volume information section)?</p>

---
