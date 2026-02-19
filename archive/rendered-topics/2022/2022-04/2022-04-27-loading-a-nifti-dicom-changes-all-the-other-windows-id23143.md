---
topic_id: 23143
title: "Loading A Nifti Dicom Changes All The Other Windows"
date: 2022-04-27
url: https://discourse.slicer.org/t/23143
---

# Loading a nifti/dicom changes all the other windows

**Topic ID**: 23143
**Date**: 2022-04-27
**URL**: https://discourse.slicer.org/t/loading-a-nifti-dicom-changes-all-the-other-windows/23143

---

## Post #1 by @nuttay (2022-04-27 08:01 UTC)

<p>Hi, this is maybe pretty basic but I can’t seem to find the solution ind documentation.</p>
<p>Whenever I drag-drop a nifti into one of the windows, all the other windows get changed; i.e. they load the same file or they change the view from axial-&gt;reformat or some random stuff.</p>
<p>How can I prevent 3D slicer from changing my other windows. I want to look at multi-serial MRI with a sequence in each windows.</p>

---

## Post #2 by @nuttay (2022-04-27 09:56 UTC)

<p>Similarly,  I also wish to be able to load a different label-map on each viewer-window, and only visualize that specific label map in each window. But it seems all label maps get stacked on top of each other so each viewer shows all labels maps.</p>

---

## Post #3 by @pieper (2022-04-29 13:45 UTC)

<p>I depends on how you drag and drop.  If you drag in from the desktop or a folder, then all views will update.  If you drag items from the Slicer Data Module you can make volumes and segmentations appear in specific windows where you drop them.  You may also find the CompareVolumes module useful for looking at multiple MR series conveniently.</p>

---

## Post #4 by @nuttay (2022-04-29 17:39 UTC)

<p>Thank you. This works for the image data.</p>
<p>But not for labels. It seems all labels get stacked on top of each other in all the windows?</p>

---

## Post #5 by @pieper (2022-04-29 18:10 UTC)

<p>If you use segmentations, then you can turn it off at the top level and it will go off everywhere. Then drag it to a single view and it only shows there.</p>

---
