# Exporting DICOMS with annotations

**Topic ID**: 21101
**Date**: 2021-12-17
**URL**: https://discourse.slicer.org/t/exporting-dicoms-with-annotations/21101

---

## Post #1 by @Maharshi_Panchal (2021-12-17 00:23 UTC)

<p>Hello,</p>
<p>I was wondering if there was a way to export DICOM images after making annotations on them. For example, if I mark CT scans slice-by-slice using the “draw” effect in Segment Editor, is there any way for me to export the DICOM images so that they contain these markings?</p>
<p>Thank you.</p>

---

## Post #2 by @Juicy (2021-12-17 01:20 UTC)

<p>The most simple way I can think of involves using the segment editor extra effects. First you need to go to the extensions manager and install the “SegmentEditorExtraEffects” add on.</p>
<p>Then paint your annotations using the paint tool in the segment editor. Once you have finished making annotations go the the “Mask volume” effect in the segment editor. Choose “fill inside”, then pick a fill value. You can only really have the annotations appear black or white (or grey) in a greyscale image so for a standard 12 bit CT scan choose 3070 if you want your annotations to appear white, or choose -1000 if you want them to look black. Press apply and the Mask volume effect will create a new masked volume.</p>
<p>Find this new volume in the data module, right-click on it and choose “Export to DICOM”. This should give you dicom slice images with all your annotations in either white or black. I am not sure how to go about making coloured annotations, I am sure it would be possible just may be more complicated. Perhaps someone else could advise?</p>

---
