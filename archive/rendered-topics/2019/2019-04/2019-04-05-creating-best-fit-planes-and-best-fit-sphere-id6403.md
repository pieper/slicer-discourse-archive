---
topic_id: 6403
title: "Creating Best Fit Planes And Best Fit Sphere"
date: 2019-04-05
url: https://discourse.slicer.org/t/6403
---

# creating best fit planes and best fit sphere

**Topic ID**: 6403
**Date**: 2019-04-05
**URL**: https://discourse.slicer.org/t/creating-best-fit-planes-and-best-fit-sphere/6403

---

## Post #1 by @clauzi (2019-04-05 12:08 UTC)

<p>Operating system: windows<br>
Slicer version: 4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,<br>
I am trying to calculate angles between planes (working with AnglePlane module) and need to create a plane where I cannot use just 3 landmarks but it needs to be a best fit plane of the acetabular rim to create the acetabular plane.</p>
<p>I am also trying to define the acetabulum using a best fit sphere.</p>
<p>Thanks so much for your help. This is great!</p>
<p>Claudia</p>

---

## Post #2 by @lassoan (2019-04-05 12:20 UTC)

<aside class="quote no-group" data-username="clauzi" data-post="1" data-topic="6403">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/35a633/48.png" class="avatar"> clauzi:</div>
<blockquote>
<p>3 landmarks but it needs to be a best fit plane of the acetabular rim to create the acetabular plane.</p>
</blockquote>
</aside>
<p>You can align slice plane with 3 landmark points by copy-pasting these few lines of code to Slicer’s Python interactor (menu: View / Python interactor): <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Fit_slice_plane_to_markup_fiducials" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="clauzi" data-post="1" data-topic="6403">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/35a633/48.png" class="avatar"> clauzi:</div>
<blockquote>
<p>I am also trying to define the acetabulum using a best fit sphere.</p>
</blockquote>
</aside>
<p>You can manually define/visualize a sphere as shown here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer</a><br>
You may be able to register a sphere by creating a sphere and segmenting the acetabulum and use Segment Registration module to automatically align them.</p>

---

## Post #3 by @lassoan (2022-04-15 11:10 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/please-some-help-about-making-best-fit-sphere-of-humeral-head/22975/2">Please some help about making best fit sphere of humeral head</a></p>

---
