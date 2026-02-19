---
topic_id: 46111
title: "Mimics To Slicer Masks And Models Pre Tracking Segmentation"
date: 2026-02-10
url: https://discourse.slicer.org/t/46111
---

# Mimics to Slicer Masks and Models - Pre-Tracking Segmentation

**Topic ID**: 46111
**Date**: 2026-02-10
**URL**: https://discourse.slicer.org/t/mimics-to-slicer-masks-and-models-pre-tracking-segmentation/46111

---

## Post #1 by @Shilpa_Rao (2026-02-10 15:22 UTC)

<p>I’m trying to repeat segmentation workflows from Mimics to Slicer, with the end-goal being tracking.</p>
<p>In Mimics, there is a distinction between masks and models, where models are exported as VRML 2.0 files (then converted to IV files) and masks are exported as DICOM partial volumes. The IV files are then aligned to the PV files, and a TIFF stack is generated for each PV.</p>
<p>I cannot figure out how to repeat this process in Slicer… I can export the 3D models as STL files using the segment module, which can then be converted to IV using other software. Is there a way to export masks to partial volumes and then align the models accordingly the same way as Mimics?</p>
<p>Thank you!</p>
<hr>
<p>Operating system: Windows 10 Education, Version 22H2, OS Build 19045.6456<br>
Slicer version: 5.6.2</p>

---

## Post #2 by @muratmaga (2026-02-10 16:17 UTC)

<aside class="quote no-group" data-username="Shilpa_Rao" data-post="1" data-topic="46111">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/shilpa_rao/48/81941_2.png" class="avatar"> Shilpa_Rao:</div>
<blockquote>
<p>s there a way to export masks to partial volumes</p>
</blockquote>
</aside>
<p>Use the MaskVolume in the Segment editor to extract the volume under the current segmentation label. If you have more than one SplitVolume in SegmentEditorExtraEffects extension will do it all at once.</p>
<aside class="quote no-group" data-username="Shilpa_Rao" data-post="1" data-topic="46111">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/shilpa_rao/48/81941_2.png" class="avatar"> Shilpa_Rao:</div>
<blockquote>
<p>then align the models accordingly</p>
</blockquote>
</aside>
<p>You don’t need to align anything. Models derived from the segmentation and the subvolumes you saved will continue to  share the same coordinate system, and continue to align.</p>
<p>I don’t know mimics, so if you mean something else by align, then you need to explain.</p>

---
