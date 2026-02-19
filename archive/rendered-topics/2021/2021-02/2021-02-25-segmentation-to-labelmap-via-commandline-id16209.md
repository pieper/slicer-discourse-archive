---
topic_id: 16209
title: "Segmentation To Labelmap Via Commandline"
date: 2021-02-25
url: https://discourse.slicer.org/t/16209
---

# Segmentation to labelmap via commandline

**Topic ID**: 16209
**Date**: 2021-02-25
**URL**: https://discourse.slicer.org/t/segmentation-to-labelmap-via-commandline/16209

---

## Post #1 by @PaoloZaffino (2021-02-25 10:56 UTC)

<p>Hi all,<br>
is there a way for converting a segmentation into a labelmap via command line?<br>
The labelmap should fit the shape of an anatomical image, so this would be another parameter to specify.</p>
<p>In addition: can I apply (via command line, again) a transformation to a segmentation?</p>
<p>Basically, I would first apply one (or more) transformation to the segmentation, then convert the contours to fit the final image shape.</p>
<p>Thanks a lot.</p>
<p>Paolo</p>

---

## Post #2 by @lassoan (2021-02-25 18:42 UTC)

<p>See examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #3 by @PaoloZaffino (2021-03-01 12:11 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> .</p>
<p>Since I need to do all this via command line, I have to run slicer specifying the reference volume, the segmentation, and the python script with the code for conversion.</p>
<p>Am I right?</p>
<p>Paolo</p>

---

## Post #4 by @lassoan (2021-03-01 12:32 UTC)

<p>Yes. You can pass all the code that loads inputs, runs processing, and exports output to files. Or, you can create a small script and just specify the script and input/output file paths as command-line arguments.</p>

---
