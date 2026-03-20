---
topic_id: 46507
title: "3D Slicer With Totalsegmentator For Abdominal Ct"
date: 2026-03-19
url: https://discourse.slicer.org/t/46507
---

# 3D slicer with TotalSegmentator for abdominal CT

**Topic ID**: 46507
**Date**: 2026-03-19
**URL**: https://discourse.slicer.org/t/3d-slicer-with-totalsegmentator-for-abdominal-ct/46507

---

## Post #1 by @DiannaB (2026-03-19 18:49 UTC)

<p>I am honestly don’t even know if this is possible, but I have the DICOM files from my husband’s CT scan (abdominal with contrast) and I would love to be able to 3D model them. He has an intussusception in his small bowel, and we thought it would be cool to be able to visualize the full small bowel, since looking at slices individually, it can be hard to “follow.” I am entirely unfamiliar with 3D slicer. I have done some design work in sketchup 3d, which is obviously quite different, but what I would love is to have the functionality of visualizing his small bowel and being able to use a “slice” to hide the part on the one side so I can “see inside” if that makes sense.</p>
<p>Unfortunately, even the first step of getting TotalSegmentator to work has evaded me, and I am getting an error when I try to run the Total Segmentator module.</p>
<p>I am on a 2023 MacBook Pro running Sequoia 15.6.1, Apple M3 Max. Should have plenty of memory and space.</p>
<p>I am getting the first error referenced on Github: Problem: Error popup appears: <code>Failed to compute results ... Command ... 'pip', 'install' ... returned non-zero exit status 1</code></p>
<p>Any help would be appreciated, or even if someone could tell me whether what I’m looking for is even a possibility. I am admittedly not very tech savvy.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2026-03-19 20:08 UTC)

<p>Yes, getting things installed and running can be tricky.  There may be particular problems on a mac, I haven’t tried.</p>
<p>You might want to try their web page version instead: <a href="https://totalsegmentator.com/">https://totalsegmentator.com/</a></p>
<p>That should give you something you can use in Slicer.  If you install the Sandbox extension you should be able to get renderings like the example here: <a href="https://github.com/lassoan/SlicerTotalSegmentator/tree/main?search=1" class="inline-onebox">SlicerTotalSegmentator/ at main · lassoan/SlicerTotalSegmentator · GitHub</a></p>

---

## Post #3 by @DiannaB (2026-03-19 20:16 UTC)

<p>Update: this took a couple of days to get approved. In the meantime, I went back and installed 5.8.1 and it worked right out of the gate. Downloaded TotalSegmentator, ran it, and used segment editor to see the areas relevant.</p>
<p>My next question would be: if I wanted to visualize “inside” an organ, how would I do so? Is there a way, on the 3d segmentation, to visualize the variations, like different dark areas, etc? I am viewing a CT with contrast. I did go through and “painted” the segments with contrast a different shade, but that just makes the segment a solid color. It would be amazing to be able to visualize the different variations and gas bubbles and specifically the intussusception itself.</p>

---

## Post #4 by @pieper (2026-03-19 21:07 UTC)

<p>It’s not clear to me exactly what you are looking for, but the ColorizeVolume has some nice feature for exploring the data within a segment.  You may need to practice a bit.</p>

---
