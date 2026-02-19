---
topic_id: 24175
title: "Segment Smooting Performance Issue Using A M1 Apple Silicon"
date: 2022-07-04
url: https://discourse.slicer.org/t/24175
---

# Segment smooting performance issue using a M1 Apple Silicon Mac

**Topic ID**: 24175
**Date**: 2022-07-04
**URL**: https://discourse.slicer.org/t/segment-smooting-performance-issue-using-a-m1-apple-silicon-mac/24175

---

## Post #1 by @lodumont (2022-07-04 22:31 UTC)

<p>I am using Slicer 5.0.2 on a Mac Studio with a M1 Max chip (10 cores, 64 GB memory) in order to segment the volumes of archaeological finds (in that case a Bronze Age sword hilt). I am working with a 5.84 GB nrrd file with the following dimensions:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/806404ae8e8d92e7dfd91592e1c1f3e56fbdc996.png" alt="Slicer_sword" data-base62-sha1="ijNp4yMU8zxR1RBRO0HHzkIPkuq" width="608" height="86">.</p>
<p>Using the segment editor, I created 6 segments for the different components of the hilt and the background using Grow from seeds. The process was quite long, with a long update time for each modification, but that worked eventually. The segment of the blade shows extrusions and holes I would like to smooth. After removing the most obvious mistakes using 3D scissors, I tried to use a median filter with a 1 mm kernel size (I cannot increase it). Slicer then freeze with an endless spinning wheel. The activity monitor shows Sliceer is using around 20 GB of memory, which is fine, but almost all CPU power. I let it run for a couple of days without any change. I also tried the same operation with a smaller volume susing the “Crop Voume” module with a 2.00 spacing scale factor and to apply the smoothing on a small area using the smoothing brush, the result is the same. I always run the smoothing operations with the 3D view deactivated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66af61417454d884b71e1eb4032d81a2d9fc855e.jpeg" data-download-href="/uploads/short-url/eEos0kBbEEyzcgKWm1mCPGj4q5M.jpeg?dl=1" title="Sclicer_sword_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66af61417454d884b71e1eb4032d81a2d9fc855e_2_690x455.jpeg" alt="Sclicer_sword_2" data-base62-sha1="eEos0kBbEEyzcgKWm1mCPGj4q5M" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66af61417454d884b71e1eb4032d81a2d9fc855e_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66af61417454d884b71e1eb4032d81a2d9fc855e_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66af61417454d884b71e1eb4032d81a2d9fc855e_2_1380x910.jpeg 2x" data-dominant-color="616064"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sclicer_sword_2</span><span class="informations">1776×1172 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The smoothing works fine if I export the segments as stl files and open them on Meshlab, but I’d like to process everything in Slicer. Any idea how I can make it work?</p>
<p>Thank you.</p>

---

## Post #2 by @muratmaga (2022-07-05 21:50 UTC)

<aside class="quote no-group" data-username="lodumont" data-post="1" data-topic="24175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/e9a140/48.png" class="avatar"> lodumont:</div>
<blockquote>
<p>1 mm kernel size</p>
</blockquote>
</aside>
<p>With the resolution of our dataset, 1mm kernel would be 153x153x153 voxels (1mm / 0.0065mm voxel size). That’s a huge kernel size for that filter. Normally you would run a median filter with 3-5 voxels. So try a value that’s like 0.02mm, which should give you a 3x3x3 kernel size.</p>
<p>If the precision displayed in the kernel size field is not enough to enter 0.02, you can increase the number of decimal points by hitting <code>CTRL+ALT+PLUS</code> (+ key) In Mac, I believe it is CMD + ALT + PLUS (+ key)</p>

---
