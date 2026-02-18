# Applying the Grow from Seeds Effect to only selected slices

**Topic ID**: 2855
**Date**: 2018-05-20
**URL**: https://discourse.slicer.org/t/applying-the-grow-from-seeds-effect-to-only-selected-slices/2855

---

## Post #1 by @cphillips (2018-05-20 15:18 UTC)

<p>Operating system: Mac OS High Sierra<br>
Slicer version: 4.8.1</p>
<p>I am attempting to use the Grow from seeds effect (in the Label editor) to segment out and calculate the volume of an photothrombotically induced infarct region on a T2W MRI image. This image has 8 coronal slices, and the infarct is only present on 5 of those 8 slices, so I would only like the region to be grown over those slices. Right now I am seeding on the 5 slices where it appears only, but the region is being grown over all 8.</p>
<p>It is difficult to seed to begin with, since the lesion includes a brighter ring of dead cells, as well as an enclosed darker area representing the region-at-risk (the darker inner region resembles normal tissue).</p>
<p>Any ideas on how I might direct it to only grow over the 5 slices I have seeded?</p>

---

## Post #2 by @lassoan (2018-05-20 18:05 UTC)

<p>If you find any misclassified region after “Grow from seeds” initialization then you can continue to paint more seeds (using infarct and/or “other” segment) to add/remove regions from infarct segment.</p>
<p>Including/excluding complete slices would be completely arbitrary (slice edges are not anatomical boundaries), so I would not recommend doing it. However, if you still want to do it then you can simply fill a slice with a certain segment. Grow from seeds effect never changes any region where user specified seed segment.</p>

---

## Post #3 by @cphillips (2018-05-24 18:07 UTC)

<p>Many thanks for your response. This brings me to another question–when calculating the total volume of a segment that spans multiple slices (the volume calculated that is displayed in the Segment Statistics module, that is), does Slicer calculate the volume slice by slice (taking the slice thickness into account at each stage), and add the sub-volumes together to give the final result?</p>

---

## Post #4 by @lassoan (2018-05-24 18:18 UTC)

<p>Yes, of course, Slicer computes the correct 3D volume - as you see the 3D object on the screen.</p>

---
