---
topic_id: 34087
title: "How To Determine The Resolution Of The Stl File Exported Fro"
date: 2024-02-01
url: https://discourse.slicer.org/t/34087
---

# How to determine the resolution of the STL file exported from the 3D slicer?

**Topic ID**: 34087
**Date**: 2024-02-01
**URL**: https://discourse.slicer.org/t/how-to-determine-the-resolution-of-the-stl-file-exported-from-the-3d-slicer/34087

---

## Post #1 by @Yunus (2024-02-01 12:03 UTC)

<p>I have segmented kidneys and other organs with 3D Slicer and exported them as an STL file. I also need to specify the model resolution, but I don’t know how to do this.<br>
What I have tried so far:</p>
<ol>
<li>before I exported the STL file to 3D Slicer, I searched for settings to set the resolution. But unfortunately found nothing</li>
<li>uploaded the exported STL file to a printer software with the hope that the resolution of the model will be displayed. But I got nowhere there either.</li>
</ol>

---

## Post #2 by @pieper (2024-02-01 16:20 UTC)

<p>STL can have coordinates in any units.  Slicer exports in millimeters.</p>

---

## Post #3 by @Yunus (2024-02-01 16:32 UTC)

<p>Thank you for your answer. I know that the unit is in millimeters, but I need the resolution of the model, such as 0.01 mm</p>

---

## Post #4 by @pieper (2024-02-01 16:34 UTC)

<p>Resolution is not really a property of an STL file.  More likely it’s determined by the source data that created the mesh.</p>

---

## Post #5 by @Yunus (2024-02-01 16:38 UTC)

<p>Ok. I have to say I’m not a professional at this. How would you determine the resolution of the exported STL file from 3D Slicer?</p>

---

## Post #6 by @pieper (2024-02-01 16:46 UTC)

<p>How did you create the STL?</p>
<p>As I mentioned, if you started with a 1mm cubed volume you could argue that the STL is 1mm resolution, but really it depends on how the STL was created.  For example, the mesh may have been smoothed or decimated which would change the concept of “resolution”.</p>
<p>What purpose to you have for knowing the “resolution” of an exported STL file?</p>

---

## Post #7 by @Yunus (2024-02-02 13:52 UTC)

<p>I created the STL in the “Segment Editor” module. Of course, I first smoothed the segmented data using the “Median” method.<br>
I need the resolution for the printer selection</p>

---

## Post #8 by @pieper (2024-02-02 23:43 UTC)

<aside class="quote no-group" data-username="Yunus" data-post="7" data-topic="34087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/b38774/48.png" class="avatar"> Yunus:</div>
<blockquote>
<p>I need the resolution for the printer selection</p>
</blockquote>
</aside>
<p>What do you mean by this?</p>

---

## Post #9 by @Yunus (2024-02-03 14:05 UTC)

<p>Each printer has a certain limit up to which resolution it can print</p>

---

## Post #10 by @pieper (2024-02-04 15:45 UTC)

<p>It seems we still aren’t understanding each other.  The surface mesh coming from 3D Slicer may have large or small triangles, and you may smooth or optimize the mesh can influence that.  A lot depends on the input data and use case.  How much of the mesh detail is reproduced by the printer is a separate issue.  You probably have to work from both directions to get good prints.</p>

---

## Post #11 by @Melodicpinpon (2025-06-26 16:52 UTC)

<p>Did you find the way to reduce the definition before exporteing a segmentation?<br>
I export a stl from the skin of a whole pig and the file weights 2Gb, it is nearly impossible to open or to handle by my computer.<br>
I think that I had done it a few years before.</p>

---

## Post #12 by @muratmaga (2025-06-26 17:31 UTC)

<aside class="quote no-group" data-username="Melodicpinpon" data-post="11" data-topic="34087">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>Did you find the way to reduce the definition before exporteing a segmentation?</p>
</blockquote>
</aside>
<p>That’s done by decimation. You can set it in Segment Editor under the <code>Show 3D</code> model, or do it after the fact using the <code>Surface Toolbox</code>.</p>

---
