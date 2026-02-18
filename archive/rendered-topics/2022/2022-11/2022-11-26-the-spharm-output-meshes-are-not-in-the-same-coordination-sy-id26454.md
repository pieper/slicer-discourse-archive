# The SPHARM output meshes are not in the same coordination system!

**Topic ID**: 26454
**Date**: 2022-11-26
**URL**: https://discourse.slicer.org/t/the-spharm-output-meshes-are-not-in-the-same-coordination-system/26454

---

## Post #1 by @Moh_d_Al-Watary (2022-11-26 13:19 UTC)

<p>Dears in  the Slicer forum, wish you all having good life. I am facing a problem as explained below. I am conducting a project in which measuring the mandibular condyle remodeling is a part of it, I am using the SPHARM as a step in achieving this goal.</p>
<ol>
<li>When importing the T1 and T2 condylar segmentation (A) to SPHARM to generate mesh: the output mesh was generated as 110 KB.</li>
<li>Then, on Slicer, both meshes were imported, but they were not on the same coordination system (B), as you can see in the image below.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b16aed8fa6eca40d7bcfa65a1c9708c2c741258.jpeg" data-download-href="/uploads/short-url/aIgpjPdcUWeY4ac9X73imyt6Wr6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b16aed8fa6eca40d7bcfa65a1c9708c2c741258_2_690x387.jpeg" alt="image" data-base62-sha1="aIgpjPdcUWeY4ac9X73imyt6Wr6" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b16aed8fa6eca40d7bcfa65a1c9708c2c741258_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b16aed8fa6eca40d7bcfa65a1c9708c2c741258_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b16aed8fa6eca40d7bcfa65a1c9708c2c741258.jpeg 2x" data-dominant-color="C0C1C8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could you please help me answering these questions:</p>
<ol>
<li>What could be the cause?</li>
<li>How to solve this problem?</li>
</ol>
<p>Thank you so much for your support and sincere help.</p>

---

## Post #2 by @lassoan (2022-11-26 16:28 UTC)

<p>Does it help if you load the meshes in RAS coordinate system? (you can select the coordinate system in Add data window if you click on Advanced checkbox).</p>

---

## Post #3 by @Moh_d_Al-Watary (2022-11-27 09:56 UTC)

<p>Thank you so much for your suggestion, I have tried both coordinate (RAS and LPS) but unfortunately did not work.</p>

---
