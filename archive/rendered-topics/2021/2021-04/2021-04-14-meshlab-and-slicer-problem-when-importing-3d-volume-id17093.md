---
topic_id: 17093
title: "Meshlab And Slicer Problem When Importing 3D Volume"
date: 2021-04-14
url: https://discourse.slicer.org/t/17093
---

# MeshLab and Slicer problem when Importing 3D Volume

**Topic ID**: 17093
**Date**: 2021-04-14
**URL**: https://discourse.slicer.org/t/meshlab-and-slicer-problem-when-importing-3d-volume/17093

---

## Post #1 by @will_kim (2021-04-14 15:33 UTC)

<p>Hi, when I import the same file on Slicer and MeshLab the STL volumes are either inverted or rotated differently. Firstly, I do not understand why this only occurs for few STL files I have and what I could do to fix it, as the orientation/coordinates of these volumes matter to me. Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0ca1e3feccf534eca416ffcb925c87394b86e29.png" data-download-href="/uploads/short-url/w4zZlOSlkQPWpjUSbJNsuhdMNzX.png?dl=1" title="slicer_meshlab" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ca1e3feccf534eca416ffcb925c87394b86e29_2_690x420.png" alt="slicer_meshlab" data-base62-sha1="w4zZlOSlkQPWpjUSbJNsuhdMNzX" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ca1e3feccf534eca416ffcb925c87394b86e29_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0ca1e3feccf534eca416ffcb925c87394b86e29.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0ca1e3feccf534eca416ffcb925c87394b86e29.png 2x" data-dominant-color="6768A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_meshlab</span><span class="informations">900×549 30.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2021-04-14 16:29 UTC)

<p>Did you generate these STLs in an earlier version of Slicer?<br>
If so, Slicer recently changed to using LPS coordinate system for 3D Models: <a href="https://discourse.slicer.org/t/model-files-are-now-saved-in-lps-coordinate-system/10446" class="inline-onebox">Model files are now saved in LPS coordinate system</a>.</p>
<p>If you expand the Load Data dialog box options, and change the Coordinate system from default to RAS, perhaps that will fix it.</p>

---

## Post #3 by @lassoan (2021-04-14 16:39 UTC)

<p>Slicer stores the coordinate system in the header of all mesh files (STL, OBJ, PLY, VTK, VTP, VTU) in a comment such as <code>SPACE=LPS</code> or <code>SPACE=RAS</code>. If there is no such comment in the file header then the coordinate system is assumed to be LPS, because this is the most commonly used coordinate system convention in medical image computing.</p>
<p>The world coordinate system in Slicer is RAS (this decision had to be made 20 years ago, when it was not clear if LPS or RAS was going to win). Therefore, when loading a file, Slicer automatically inverts the first two coordinate axes if the file uses LPS coordinate system.</p>

---

## Post #4 by @will_kim (2021-04-14 16:58 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a>, <a class="mention" href="/u/lassoan">@lassoan</a> thank you that makes sense.</p>

---
