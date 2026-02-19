---
topic_id: 4889
title: "Create A Volume"
date: 2018-11-27
url: https://discourse.slicer.org/t/4889
---

# Create a volume

**Topic ID**: 4889
**Date**: 2018-11-27
**URL**: https://discourse.slicer.org/t/create-a-volume/4889

---

## Post #1 by @Heiko_Stark (2018-11-27 14:03 UTC)

<p>For a test case I want to create a volume and fill it with data.<br>
How can I do this with Slicer?<br>
Filling should go with the editor.</p>
<p>Best regards!<br>
Heiko</p>

---

## Post #2 by @lassoan (2018-11-27 14:16 UTC)

<p>You can do this with the Segment Editor module.</p>
<p>Add a region of interest (ROI) widget that covers the area where the volume will be (on the toolbar, click down-arrow of the place icon then click in the center of the region and at a corner) and set the desired voxel size:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d47a553e02b89d4b61355b6cc846a4bec3439f8.png" alt="image" data-base62-sha1="1TtHRQVasI1ogPEh5YZkeXvJfFC" width="369" height="304"></p>
<p>After this, unfortunately, you need to choose a volume as Master volume, because several effects of SegmentEditor requires presence of a master volume. It can be any volume, for example you can download MRHead image using SampleData module. We’ll figure out some way to not require this step (maybe create a blank volume), but right now you need to do this.</p>
<p>Then you can start painting using Paint, Draw, scissors effect, etc.</p>
<p>Once you are done, you can export your segmentation to a labelmap volume by right-clicking on the segmentation node in Data module and choose “Export visible segments to binary labelmap”.</p>

---

## Post #3 by @martosalex (2020-03-07 10:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> It works! Thanks for your help!</p>

---
