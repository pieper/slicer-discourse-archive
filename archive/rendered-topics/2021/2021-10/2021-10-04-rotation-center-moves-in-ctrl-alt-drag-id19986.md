---
topic_id: 19986
title: "Rotation Center Moves In Ctrl Alt Drag"
date: 2021-10-04
url: https://discourse.slicer.org/t/19986
---

# Rotation center moves in Ctrl+Alt+Drag

**Topic ID**: 19986
**Date**: 2021-10-04
**URL**: https://discourse.slicer.org/t/rotation-center-moves-in-ctrl-alt-drag/19986

---

## Post #1 by @gaoyi.cn (2021-10-04 10:18 UTC)

<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a58dbf1b41d61bb98f1863f5db4843fbba374afc.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a58dbf1b41d61bb98f1863f5db4843fbba374afc.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a58dbf1b41d61bb98f1863f5db4843fbba374afc.mp4</a>
    </source></video>
  </div><br>
Dear All,<p></p>
<p>I’m trying to use the Ctrl+Alt+Drag to rotate the volume interactively. However the Center seems moving with rotation.</p>
<p>But this only seems happen when I have a customized layout (shown in the video). This moving-center does not happen in standard layout such as the Four-Up and others.</p>
<p>Thanks for any hint!</p>
<p>yi</p>

---

## Post #2 by @lassoan (2021-10-04 12:26 UTC)

<p>Slice rotation centerpoint is computed automatically as the average of all slice intersections visible in that view (see implementation <a href="https://github.com/Slicer/Slicer/blob/04d69cd0749ce72b44113535fa2c4da20386142c/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionRepresentation2D.cxx#L584-L639">here</a>). Probably the issue is that the theoretically parallel G1 slice is not perfectly parallel (due to numerical precision issues) with the G slice, therefore it intersects with the G slice (the intersection appears just outside the displayed image region at the bottom), moving the average intersection position lower.</p>
<p>If you want your (R, G, Y) and (R1, G1, Y1) views move in two groups then assign two different view group IDs to them (e.g., 0 and 1). If you want them all move together then in the <code>if (vtkLine::Intersection...</code> line add a check that if the two lines are almost parallel (e.g., angle difference is less than 3 degrees) and if they are parallel then ignore that intersection.</p>

---

## Post #3 by @gaoyi.cn (2021-10-04 22:43 UTC)

<p>Thanks Andras! I’ll follow this direction and investigate more.</p>

---

## Post #4 by @gaoyi.cn (2021-10-08 02:44 UTC)

<p>Hi Andras,</p>
<p>I followed your suggestion on the “checking for parallelism” and it worked. I submitted a pull request.</p>
<p>On the other hand, towards your other suggestion about “assigning group IDs to different views”, could I have some suggestions on how to achieve that? or could i have some example modules to study?</p>
<p>Thanks!<br>
yi</p>

---

## Post #5 by @lassoan (2021-10-08 03:44 UTC)

<p>See description of view groups and API to set it here: <a href="https://apidocs.slicer.org/master/classvtkMRMLAbstractViewNode.html#a896bad470fb25f642165eb6305eee4fc" class="inline-onebox">Slicer: vtkMRMLAbstractViewNode Class Reference</a></p>
<p>You can set the view group of a view node in the GUI in “View controllers” module’s Advanced section.</p>

---

## Post #6 by @gaoyi.cn (2021-10-08 09:56 UTC)

<p>Thanks Andras! Will check that.</p>

---
