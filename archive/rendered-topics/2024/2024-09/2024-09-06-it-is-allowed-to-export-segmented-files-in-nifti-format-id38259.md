---
topic_id: 38259
title: "It Is Allowed To Export Segmented Files In Nifti Format"
date: 2024-09-06
url: https://discourse.slicer.org/t/38259
---

# It is allowed to export segmented files in NIfti format?

**Topic ID**: 38259
**Date**: 2024-09-06
**URL**: https://discourse.slicer.org/t/it-is-allowed-to-export-segmented-files-in-nifti-format/38259

---

## Post #1 by @Filippo_Parronchi (2024-09-06 12:54 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2024-09-06 13:33 UTC)

<p>Exporting segmentations into NIFTI file format is <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">allowed</a>, it is just <a href="https://github.com/lassoan/slicerio/blob/main/SegmentationFileFormat.md">not recommended</a>.</p>

---

## Post #3 by @Filippo_Parronchi (2024-09-06 13:40 UTC)

<p>Thanks. Can you explain me the reasons?<br>
I need segmentation Nifti file to use in AR with hololens2? Do you think it’s a problem?</p>

---

## Post #4 by @lassoan (2024-09-06 13:44 UTC)

<aside class="quote no-group" data-username="Filippo_Parronchi" data-post="3" data-topic="38259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/filippo_parronchi/48/77852_2.png" class="avatar"> Filippo_Parronchi:</div>
<blockquote>
<p>Can you explain me the reasons?</p>
</blockquote>
</aside>
<p>I included a link above to a page that compares DICOM, NRRD, NIFTI, but let me copy the reasons against NIFTI here then:</p>
<blockquote>
<ul>
<li>Orientation definition in NIFTI files can be ambiguous: there are multiple ways to define orientation, they can be both present, and contain contradicting information. Various softare will interpret these ambiguous files differently. See for example these discussions: <a href="https://www.openfmri.org/dataset-orientation-issues/">1</a>, <a href="https://discourse.slicer.org/t/orientation-origin/23365">2</a>, <a href="https://github.com/spinalcordtoolbox/spinalcordtoolbox/issues/3283">3</a></li>
<li>Not compatible with clinical software</li>
<li>Common convention for storing essential metadata does not exist</li>
<li>File header is not human-readable: you cannot use a text editor/viewer to see the actual file header but you always have to rely on a parser to give you an interpretation of the file header</li>
</ul>
</blockquote>
<aside class="quote no-group" data-username="Filippo_Parronchi" data-post="3" data-topic="38259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/filippo_parronchi/48/77852_2.png" class="avatar"> Filippo_Parronchi:</div>
<blockquote>
<p>I need segmentation Nifti file to use in AR with hololens2?</p>
</blockquote>
</aside>
<p>You actually don’t need to use NIFTI for this purpose, as NRRD can store all (and more) metadata and voxel information that NIFTI can.</p>
<p>Anyway, if you need to use some specific software that is limited to NIFTI then you can export segmentation as NIFTI file from Slicer as I described in the link above.</p>

---
