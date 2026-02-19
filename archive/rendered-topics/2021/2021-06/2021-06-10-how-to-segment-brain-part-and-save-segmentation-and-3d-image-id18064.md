---
topic_id: 18064
title: "How To Segment Brain Part And Save Segmentation And 3D Image"
date: 2021-06-10
url: https://discourse.slicer.org/t/18064
---

# How to segment brain part and save segmentation and 3D image as one file not separate file? 

**Topic ID**: 18064
**Date**: 2021-06-10
**URL**: https://discourse.slicer.org/t/how-to-segment-brain-part-and-save-segmentation-and-3d-image-as-one-file-not-separate-file/18064

---

## Post #1 by @abhijeet2410 (2021-06-10 13:24 UTC)

<p>Hello Team,</p>
<p>Greetings!!</p>
<p>Thank you very much for best service. I have two question this time:</p>
<ol>
<li>
<p>How to remove skull part from the 3 D brain image (I am focusing on 3D part only).</p>
</li>
<li>
<p>For my project, I want (segmentation +  nill.  image file ) as one .niil file. How can I get segmented 3D image as one image?</p>
</li>
</ol>
<p>Sincerely,<br>
Student</p>

---

## Post #2 by @lassoan (2021-07-21 01:33 UTC)

<p>It seems that this message has fallen through the cracks and did not get answered. If you have not figured out the answer by now and still interested in how to do it then let us know.</p>
<p>In short: 1. This operation is called skull stripping and you can use SwissSkullStripper extensions for this. 2. You would need to specify how exactly you would like to fuse the images. For example, would you like to export a colored image where brightness of each voxel comes from the master volume and segments specify color hue?</p>

---
