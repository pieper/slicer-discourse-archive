---
topic_id: 10072
title: "Creating 3D Printed Model Of Airways Using Ct"
date: 2020-02-02
url: https://discourse.slicer.org/t/10072
---

# Creating 3D printed model of Airways using CT

**Topic ID**: 10072
**Date**: 2020-02-02
**URL**: https://discourse.slicer.org/t/creating-3d-printed-model-of-airways-using-ct/10072

---

## Post #1 by @Zwell (2020-02-02 20:44 UTC)

<p>Hi,</p>
<p>I am trying to make a 3D printed airway from CT scan. I have managed to do a version myself but it isn’t the best - I have seen online there is a Airway Segmentation Extension - how do I get access for this to use please?</p>
<p>Thanks</p>

---

## Post #2 by @manjula (2020-02-02 23:58 UTC)

<p>Go to View —&gt; Extension manager or ctrl + 4 --&gt; Install extensions --&gt; Slicer Airway segmentation --&gt; Install</p>

---

## Post #3 by @Zwell (2020-02-03 09:40 UTC)

<p>Perfect - Thank you so much!</p>
<p>Next question…</p>
<p>So I have managed to managed to download the extension and have placed the point within the trachea and hit apply - but it only comes up with a small dot rather than expanding to the whole airways like the tutorial - any ideas?</p>

---

## Post #4 by @lassoan (2020-02-03 17:31 UTC)

<p>I’ve just tried and it worked well for me, but I guess the results may depend on image quality. For segmenting more challenging images, I would recommend to install “SegmentEditorExtraEffects” extension, then segment the airways using Segment Editor module using Fast marching effect:</p>
<div class="lazyYT" data-youtube-id="tJMGe3FMTk0" data-youtube-title="Airway segmentation from CT in 1 minute using 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---
