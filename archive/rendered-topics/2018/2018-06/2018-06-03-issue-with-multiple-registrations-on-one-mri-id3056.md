# Issue with multiple registrations on one MRI

**Topic ID**: 3056
**Date**: 2018-06-03
**URL**: https://discourse.slicer.org/t/issue-with-multiple-registrations-on-one-mri/3056

---

## Post #1 by @muchenik (2018-06-03 11:31 UTC)

<p>Hello,<br>
My team’s use of 3D slicer requires both registering an MRI volume to an Atlas (using Landmark Registration) and registering the same MRI volume to a different volume (using Fiducials Models registration in IGT extension) in order to receive X,Y,Z coordinates for the purposes of our experiment. I am having no problems doing each of these separately, but issues arise when both registrations are done on the same volume; performing the Landmark Registration first to the Atlas prevents fiducial markups from being placed for the second registration, while performing the Fiducials Models registration first prevents landmarks from being placed to register the MRI to the Atlas. A few transforms are also performed so each of these registrations are possible, not sure if that is a potential cause of the issue.</p>
<p>How can we get around this problem?</p>

---

## Post #2 by @lassoan (2018-06-03 11:50 UTC)

<p>I don’t understand what you are doing exactly, but probably unexpected behavior is due to some modules only taking into account transforms that are permanently applied (“hardened”) on the node. Try to harden transform on the volume using Transforms module.</p>
<p>You can also combine registration results by applying a transform to another transform. Order of transformations matter, so if you compute both transforms “from” the same MR volume then you need to invert one of them (to make transform “to” the MR volume) to combine them to a transform chain. <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorial</a> U-04 may be useful in learning more about transforms.</p>

---
