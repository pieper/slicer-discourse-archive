# Identifying problematic landmarks in large landmark dataset

**Topic ID**: 44498
**Date**: 2025-09-16
**URL**: https://discourse.slicer.org/t/identifying-problematic-landmarks-in-large-landmark-dataset/44498

---

## Post #1 by @christyhipsley (2025-09-16 14:40 UTC)

<p>I’m seeking advice on how to identify potentially problematic landmarks in a large (1531 landmarks on 101 specimens) dataset, where I suspect some landmarks may have fallen through the surface of the 3D objects. The landmarks were placed in Stratovan Checkpoint. When I run a GPA in SlicerMorph, I get some suspicious landmark variances using the elllipse type plot that do not look like biological variation - see elongated blue and green landmarks in screenshot below. My question is if there is an easy way to figure out in which specimens this may have happened, without going through them one by one. I reran the GPA in groups of 10 going from least to most Procrustes distance from the mean shape, and I indeed noticed these huge changes only in the last half of the dataset. But that would still be 50 models to go through, where it is difficult to track every landmark on the surface. Thank you if someone knows a less painful way to identify these likely user-generated errors.</p>
<p>Christy Hipsley</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28f85486e785c7525269a5f30161a007c37abb53.jpeg" data-download-href="/uploads/short-url/5Qr8UHlxC5OzsWSamWSHswZCPCP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28f85486e785c7525269a5f30161a007c37abb53_2_690x435.jpeg" alt="image" data-base62-sha1="5Qr8UHlxC5OzsWSamWSHswZCPCP" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28f85486e785c7525269a5f30161a007c37abb53_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28f85486e785c7525269a5f30161a007c37abb53_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28f85486e785c7525269a5f30161a007c37abb53_2_1380x870.jpeg 2x" data-dominant-color="D7E8E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1762×1112 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-09-16 16:13 UTC)

<p>The first step is to get the landmark indices of these potentialy problematic ones.  You will want to zoom into problematic landmarks, and turn the landmark labels on (you might have to adjust the visibility to make them bigger using the Markups module). Then you can look at the procrustes distance table, errors look very big, so hopefully those problematic samples are at the bottom of the table. These steps hopefully will give you the two critical pieces of information you need problematic landmarks and the which samples.</p>
<p>Then you can load the original data from these samples and carefully look at those landmark to see if the source of this large variation is non-biological.</p>
<p>If this doesn’t workout, you may have to write a bit of a script to identify them.</p>
<p>Then you can load the outputData.csv file (the procrustes aligned coordinates) and calculate the procrustes distance associated with each landmark (the information we use to make those spheres, but they are not exposed in slicerMorph).</p>

---
