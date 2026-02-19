---
topic_id: 10206
title: "Slicer Removes The Volume In Segment Editor"
date: 2020-02-11
url: https://discourse.slicer.org/t/10206
---

# Slicer removes the volume in Segment Editor

**Topic ID**: 10206
**Date**: 2020-02-11
**URL**: https://discourse.slicer.org/t/slicer-removes-the-volume-in-segment-editor/10206

---

## Post #1 by @JanWitowski (2020-02-11 23:20 UTC)

<p>Hi, I’ve been trying to work with 2020-02-08 build of Slicer and encountered an error in Segment Editor. After choosing Master volume and adding a new layer, the volume set as Master is being detached/removed from the slicer.</p>
<p>I don’t think there is anything suspicous in an error log:</p>
<pre><code>Session start time .......: 2020-02-11 17:59:01

Slicer version ...........: 4.11.0-2020-02-08 (revision 28760) win-amd64 - installed release

Operating system .........: Windows / Personal / (Build 9200) - 64-bit

Memory ...................: 32701 MB physical, 48309 MB virtual

CPU ......................: GenuineIntel , 12 cores, 12 logical processors

VTK configuration ........: OpenGL2 rendering, TBB threading

Qt configuration .........: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)

Developer mode enabled ...: no

Prefer executable CLI ....: yes

Application path .........: D:/Programs/Slicer 4.11.0-2020-02-08/bin

Additional module paths ..: C:/Users/Witowski/AppData/Roaming/NA-MIC/Extensions-28760/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Witowski/AppData/Roaming/NA-MIC/Extensions-28760/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules

Scripted subject hierarchy plugin registered: Annotations

Scripted subject hierarchy plugin registered: SegmentEditor

Scripted subject hierarchy plugin registered: SegmentStatistics

Switch to module: "SegmentEditor"

QLayout::addChildLayout: layout "" already has a parent

Switch to module: "DICOM"

MultiVolumeImportPlugin::examine

DICOMMultiVolumePlugin found 2 multivolumes!

MultiVolumeImportPlugin:examineMultiseries

DICOMMultiVolumePlugin found 1 multivolumes!

Loading with imageIOName: GDCM

Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 4.88281e-05 mm, tolerance threshold is 0.001 mm).

Loading with imageIOName: GDCM

Switch to module: "SegmentEditor"

ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 100 1
</code></pre>
<p>I am loading an anonymized CT Angio study through DICOM browser. This happens also with all extensions disabled. Here is the example study that can reproduce the problem:  <a href="https://we.tl/t-7n7enaF3JU" rel="nofollow noopener">https://we.tl/t-7n7enaF3JU</a><br>
Edit: This also happens in fresh install of 2020-02-10 build.</p>

---

## Post #2 by @lassoan (2020-02-12 00:02 UTC)

<p>This is a huge volume (10x larger than usual) but other than that it looks normal and everything works well for me. Can you take a screen capture video of what you do?</p>

---

## Post #3 by @JanWitowski (2020-02-12 00:11 UTC)

<p>Yes, of course, this is the screen capture, just after loading the data:</p>
<div class="lazyYT" data-youtube-id="1EODjqAfLTU" data-youtube-title="2020 02 11 19 08 43" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #4 by @Juicy (2020-02-12 07:07 UTC)

<p>I just made <a href="https://discourse.slicer.org/t/how-to-save-my-work-into-dicom-format/10182/7">this post</a> using segment editor on that volume and it worked fine for me on the 4.11.0-2020-02-08 build.</p>

---

## Post #5 by @ungi (2020-02-12 13:05 UTC)

<p>Interesting. I have seen the same issue on somebody’s computer who asked me to help with this issue last week. We then restarted Slicer and couldn’t reproduce the issue again, so we didn’t report it. But it looked the same.</p>

---

## Post #6 by @lassoan (2020-02-12 16:54 UTC)

<p>I was able to reproduce the error. The input has to be imported from DICOM and the order of steps matter (create segmentation, load the volueme, go back to segmentation, select master volume, add segment). It’s a really interesting bug. I’ll push a fix soon.</p>

---

## Post #7 by @lassoan (2020-02-13 00:29 UTC)

<p>The root cause of the problem was that the DICOM image was anonymized incorrectly: patient ID was set to empty (which is not compliant to the DICOM standard), which led to placing the data set under the segmentation node as a child and got removed when the segment list was updated. I’ve <a href="https://github.com/Slicer/Slicer/commit/e4cbfc4526f2428a033135756c32dccd445ab06c">fixed the problem by generating the missing patient ID</a>.</p>

---
