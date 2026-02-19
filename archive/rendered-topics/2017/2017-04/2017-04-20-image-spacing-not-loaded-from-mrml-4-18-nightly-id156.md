---
topic_id: 156
title: "Image Spacing Not Loaded From Mrml 4 18 Nightly"
date: 2017-04-20
url: https://discourse.slicer.org/t/156
---

# Image spacing not loaded from MRML? [4-18 Nightly]

**Topic ID**: 156
**Date**: 2017-04-20
**URL**: https://discourse.slicer.org/t/image-spacing-not-loaded-from-mrml-4-18-nightly/156

---

## Post #1 by @hherhold (2017-04-20 20:36 UTC)

<p>This is probably one of those problem-between-chair-and-keyboard issues, as I’m still a bit of a newcomer to Slicer.</p>
<p>I load in a TIFF stack as a volume and set the image spacing (2.7 microns in this instance), and I center the volume. I then save the project as a MRML file, not as an MRB bundle. When I reload the MRML file, the image spacing is not restored for the volume.</p>
<p>When I save as a MRB bundle, however, everything is restored just fine.</p>
<p>I’m sure I’m doing something incorrectly when saving as an MRML file, but I’ve looked through saving data in the docs on the Wiki and I don’t see anything screaming out at me.</p>
<p>Any help would be much appreciated.</p>
<p>Thanks in advance,</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2017-04-20 21:43 UTC)

<p>In the Save data dialog, what file format is selected for your volume? Does saving/reloading works if you select .nrrd format?</p>

---

## Post #3 by @pieper (2017-04-20 22:35 UTC)

<p>When you save just the mrml file (xml) it points to the original tiff data, which has no spacing.  When you save an MRB it writes all the data out into a temp directory and uses nrrd.  So saving the volume as nrrd and referencing that from your mrml file, as <a class="mention" href="/u/lassoan">@lassoan</a> suggested, would be a good solution.</p>

---

## Post #4 by @hherhold (2017-04-21 12:22 UTC)

<p>Using NRRD works great.</p>
<p>Thanks for the help!!!</p>
<p>-Hollister</p>

---

## Post #5 by @mcranium (2023-01-04 13:07 UTC)

<p>I just had the same problem. It might be worthwhile to put a warning into the Volume Information tab of the Volumes model when someone works from a TIFF or another format which does not support storing spacing information. It was even more confusing because only the z spacing was forgotten after a restart of the application, letting me think this was a bug.</p>

---
