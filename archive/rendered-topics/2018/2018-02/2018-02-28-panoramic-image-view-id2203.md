---
topic_id: 2203
title: "Panoramic Image View"
date: 2018-02-28
url: https://discourse.slicer.org/t/2203
---

# Panoramic image/view

**Topic ID**: 2203
**Date**: 2018-02-28
**URL**: https://discourse.slicer.org/t/panoramic-image-view/2203

---

## Post #1 by @bernard (2018-02-28 02:26 UTC)

<p>Is it possible to reconstruct a panoramic view as is often used in dentistry and if not, are there any plans to add that capability? Thank you.</p>
<p>Operating system: MAC 10.13 (High Sierra)<br>
Slicer version: 4.6.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2018-02-28 06:38 UTC)

<p>There is no panoramic view but you can set up curved multi-planar reconstruction view:</p>
<div class="lazyYT" data-youtube-id="thExIlffL0I" data-youtube-title="Curved multi-planar reconstruction (MPR) view in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>It would not take too much time to create a module that sets this up by a few clicks and you could also generate an image stack or projection image (traditional 2D panoramic view) using this approach or as described in <a href="http://www.vtkjournal.org/browse/publication/838">this VTK journal article</a>. If you are willing to contribute some development time or funding then you can make it happen soon, otherwise you need to wait for someone else’s contribution. There has been <a href="https://discourse.slicer.org/t/kruvi-crowdfunding-slicer-extension-development/2026">interest in improving Slicer usability for dentistry</a>, but I’m not sure if anything materialized.</p>
<p>Use the latest stable version (4.8.1).</p>

---

## Post #3 by @mihai (2018-02-28 17:25 UTC)

<p>Hi Andras,</p>
<p>thanks for the mention. We’re still running the crowdfunding campaign for that <a href="https://bthbdental.com/kruvi" rel="nofollow noopener">project</a> until the end of next month and the functionality described above is a key component of our workflow.</p>
<p>So far there have been a few commitments, most of them from small labs/individual dentists rather than research groups. I’ll let you know how it turns out.</p>
<p>Kind regards,</p>
<p>Mihai</p>

---

## Post #4 by @Baez (2018-02-28 17:39 UTC)

<p>very very Thks,<br>
I am studing all publication,</p>

---

## Post #5 by @bernard (2018-03-02 12:53 UTC)

<p>Is it possible to do a panoramic reconstruction, a view dentists often use, in Slicer? And if so, how?</p>
<p>Thank you.</p>
<p>Bernard Friedland</p>

---
