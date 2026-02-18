# Standardizing Volume Measurement

**Topic ID**: 31725
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/standardizing-volume-measurement/31725

---

## Post #1 by @JasmineFlake (2023-09-14 19:30 UTC)

<p>Hello,</p>
<p>I am trying to calculate the volume of a lesion around a tooth. After I am able to identify the lesion using “grow seeds” function I go to segment statistics to calculate the volume. Even though my partner and I have the same lesion closely identified, we are getting different volumes every time that seem to vary in a scaled manner. Every time the voxel number is different, but as I mentioned, they are scaled. For instance :<br>
He calculated a volume of 24.5045 mm3 with 12546 voxels.<br>
I calculated a volume of 17.9472 with 9189 voxels.<br>
9189/12546 =0.732<br>
17.9472/24.5045 =0.732</p>
<p>How do we calculate the true volume?</p>
<p>Thank you so much!</p>

---

## Post #2 by @mikebind (2023-09-14 22:46 UTC)

<p>I would guess that it is the case that your segmentations are actually different, even though they may look similar.  The ratio of mm3 to # of voxels just gives you the volume of a single voxel in mm3, so it is expected that you each have the same ratio.</p>
<p>You can compare directly by</p>
<ul>
<li>loading your partner’s segmentation into your Slicer</li>
<li>copying their lesion segment from their segmentation into your segmentation</li>
<li>using logical operators find the intersection between the two regions and then subtract that from the union of the two regions</li>
<li>what remains after subtraction will be a segment containing the voxels which are in one segmentation but not the other<br>
I expect you will find this region will account for the 3400 voxel difference.   Which is the “true” volume depends on which segmentation is more accurate, which is going to be a judgment call that you and your partner can discuss.  Working together, you may be able to decide on a rigid procedure for segmentation that can yield a consistent volume independent of the user and which also produces an acceptably good segmentation.  Grow from seeds can be a very useful tool, but the actual segmentation you get can depend significantly on the exact seeds you start from.  If those are hand drawn, you may see significant variability in volumes from user to user.</li>
</ul>

---

## Post #4 by @JasmineFlake (2023-09-15 13:13 UTC)

<p>Got it, thanks for your response!</p>
<p>In your opinion, is grow from seeds the most reliable way to consistently measure volume of a lesion?</p>

---

## Post #5 by @mikebind (2023-09-15 16:20 UTC)

<p>If you start from identical seeds on identical images, then the results of growing from those seeds will be consistent and identical.  However, if you start from different seeds (which hand-drawn seeds inevitably will be) the results of growing from those seeds may differ considerably, depending on how conspicuous the boundaries are between the regions you are trying to delineate.  If I remember correctly, grow from seeds grows each seeded region at a rate that depends on the local gradient of image voxels, so regions grow fast across flat regions (roughly uniform voxel values) but slow down if there is a change in voxel values (a gradient or an edge), slowing down a lot if it is a sharp edge with a big voxel value change across it.  Thus, if you have two uniform regions at very different voxel values and a very sharp edge between them, it doesn’t matter as much where exactly you put the seeds because both will grow very quickly up to the edge and then basically stop there.  However, if you have two uniform regions at very different voxel values, but a very blurry edge between them, then your seed placement will matter more because the region with the seed closer to the edge will reach the edge first and begin to slowly grow into the edge region while the other region is still filling it’s uniform area.  This head start will remain as both regions grow slowly into the edge region, and the segment which reached the edge first will end up occupying more than half of the edge region when the segments meet and the process is finished.  A “correct” segmentation in this case would probably put the boundary exactly halfway into the blurry edge, so one could argue against the use of grow from seeds on that basis, but it remains one of the best approaches for complex segmentation tasks because it handles generating a reasonable segmentation containing many segments in a way that does a pretty good job of putting segment boundaries at image edge features in 3D without anyone needing to manually trace all those edges.</p>
<p>For consistent volume measurements, however, I would probably avoid grow from seeds using hand drawn seeds because of this issue of the final boundaries between segments usually depending on the initial seed locations.  Grow from seeds might still be a good approach if you can find a procedure to generate your seed regions in a consistent way (i.e. not hand-drawn).  It’s hard to propose specific ideas without knowing what your images look like, but perhaps you could generate the starting seeds by thresholding in different bands of voxel values, possibly including some island selection or splitting, hole closing or opening, etc. If you had a fixed procedure of steps for generating seed regions which you could use on a variety of tooth images with lesions, and which gave good segmentations when grown, then you would have a procedure which would give consistent volumes across users.  That doesn’t make them “correct”, but it sounds like there are multiple segmentation possibilities which could all look “correct” but actually yield significantly different volumes.  In that case, there are advantages to using a system which will consistently choose only one of those correct-looking segmentations, especially if you wanted to do something like track whether a particular lesion was changing size between two imaging sessions. If there are hand-drawn elements, then you will have to wonder if any difference you detect is due to human input noise rather than real size change, since you would get a different volume even if there were no change in the image at all.</p>

---
