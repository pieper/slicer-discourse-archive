---
topic_id: 14637
title: "Volume Rendering A Masked Area"
date: 2020-11-16
url: https://discourse.slicer.org/t/14637
---

# Volume rendering a masked area

**Topic ID**: 14637
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/volume-rendering-a-masked-area/14637

---

## Post #1 by @Jason_C (2020-11-16 16:20 UTC)

<p>I’d like to use the volume renderer to render a portion of an MRI, but I only want to render the area covered by (a) specific segmentation(s).</p>
<p>I’m just learning slicer so this might be a rtfm case, but how can I do this? Can I either specify a segmentation to use as a volume renderer mask, or perhaps create a new volume with everything outside the segmentation removed and render that?</p>
<p>Thanks!!</p>

---

## Post #2 by @muratmaga (2020-11-16 16:22 UTC)

<p>Install the SegmentEditorExtraEffects extension and use either the MaskVolume (if you have one segment) or SplitVolume (each segment masked individually and volume reduced to the smallest extend) to extract a new volume based on your mask.</p>

---

## Post #3 by @Jason_C (2020-11-17 06:29 UTC)

<p>Thanks.</p>
<p>So, I did that (I’ve actually been using SegmentEditorExtraEffects already it’s pretty great; I didn’t know what mask volume did). Creating the masked volume worked fine. Then I went to the volume renderer; I selected the masked volume, and as soon as I clicked one of the volume renderer presets Slicer crashed. No messages or anything (not even the Windows crash dialog), it just closed; losing the work.</p>
<p>On restart I found that I could no longer import DICOM files (clicking the import button does nothing), could no longer see my DICOM database (empty), and I could no longer click the File, View, or Edit menus unless I clicked the Help menu first then moved the mouse to one of them.</p>
<p>I started ignoring modules and eventually found that the built-in DICOM module was the culprit. Ignoring it, and the menus work (although of course, I can’t load DICOM without it). Including it, and the problems happen.</p>
<p>So whatever happened when I picked a volume renderer preset broke the DICOM module permanently. It looks like I lost the DICOM database too.</p>
<p>I uninstalled and reinstalled Slicer and it’s still broken.</p>
<p>Not really sure what to do.</p>
<p>Version 4.11.</p>

---

## Post #4 by @lassoan (2020-11-17 06:40 UTC)

<p>Crash when switching between volume rendering modes is fixed in recent Slicer Preview Releases.</p>
<p>When the application crashed, you’ve lost your settings (Slicer.ini file) and probably Slicer reverted to using a default DICOM database location that contains an old, incompatible database. After you start Slicer, change the DICOM database location in menu: Edit / Application settings / DICOM section and it should all work well. If this does not solve all the problems then you can delete/rename your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">Slicer.ini file</a>.</p>

---

## Post #5 by @Jason_C (2020-11-17 06:43 UTC)

<p>That was it, thank you! The db location got reset. Phew.</p>
<p>Probably should have asked that as a new question.</p>

---

## Post #6 by @Jason_C (2020-11-17 06:48 UTC)

<p>Oh on reinstalling extensions I noticed you’re the author of SegmentEditorExtraEffects.</p>
<p>It’s indispensable; thank you, nice work!!! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
