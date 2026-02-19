---
topic_id: 25065
title: "3D Slicer For Fiber Analysis"
date: 2022-09-03
url: https://discourse.slicer.org/t/25065
---

# 3D slicer for fiber analysis

**Topic ID**: 25065
**Date**: 2022-09-03
**URL**: https://discourse.slicer.org/t/3d-slicer-for-fiber-analysis/25065

---

## Post #1 by @Trailer (2022-09-03 12:23 UTC)

<p>Hello,</p>
<p>I have an image of rigid fibers, as depicted bellow.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfa6ea674b1b3b2614cb02cc8c7704a030965076.jpeg" alt="image" data-base62-sha1="vUw5DRNVJ4rxAq5eEPTe8kVvnoO" width="689" height="452"></p>
<p>What information can I get out from 3D slicer?</p>
<p>Is is possible to get the length, diameter, begining and end of the fiber/centerlines?</p>
<p>Best Regards</p>

---

## Post #2 by @pieper (2022-09-03 16:57 UTC)

<p>That looks like pretty clean data so you should be able to get measurements with some effort.  You could start with vmtk vesselness filtering, then threshold, skeletonize, and run segment statistics.  There are a lot of touching fibers so you’ll have a lot of noise in whatever signal you extract.</p>

---

## Post #3 by @Trailer (2022-09-05 10:21 UTC)

<p>Hello Mr. Steve,</p>
<p>The vesselness filter is not doing much (or I am not applying it correctly). Do you know if it would be possible to isolate induvidual fibers and export them as .stl files?</p>

---

## Post #4 by @pieper (2022-09-05 17:31 UTC)

<p>From the image you posted it looks like the fibers touch.  Maybe you can threshold them and then use the island operator to make each into a separate segment and export the results as stl.  But probably some or most will be stuck together.  If the fibers have a bright core it may be easier to separate them.  Maybe you can post some images of the slices or post the data to get suggestions.</p>

---

## Post #5 by @Trailer (2022-10-12 15:00 UTC)

<p>Hi.</p>
<p>I will post a small image set since I am still stuck with this issue, and would really appreciate some help.</p>
<p>Link: <a href="https://we.tl/t-Nnf89qRwU5" class="inline-onebox" rel="noopener nofollow ugc">WeTransfer - Send Large Files &amp; Share Photos Online - Up to 2GB Free</a>.</p>
<p>Would it be possible to obtain the orientation of the objects ? a theta, phi angle?</p>

---
