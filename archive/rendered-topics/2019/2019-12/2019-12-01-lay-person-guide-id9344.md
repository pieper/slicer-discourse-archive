# Lay person guide?

**Topic ID**: 9344
**Date**: 2019-12-01
**URL**: https://discourse.slicer.org/t/lay-person-guide/9344

---

## Post #1 by @Diver84 (2019-12-01 05:06 UTC)

<p>I’m not educated in the medical field, I’m an engineer that is trying to help the local pediatric surgeon.  Our goal is to create models for surgical planning that could be used surgery prep or to 3D print for preforming implants to reduce surgical time.</p>
<p>I’m trying to segment L5 and lower of the spine and the end of the colon in a MRI.  I believe the quality of the MRI is very poor, as it looks like VCR video quality compared to 4k quality of the sample data in the Slicer library.</p>
<p>Can someone help me understand if its the source data or my ignorance?  I was able to extract a hip and print it from the sample data and I can’t get anything from this data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c4b9a4a34d62c8eae201ec56e49ff56e838c26e.jpeg" data-download-href="/uploads/short-url/1KLHSi2GZtUfETxRKVx8NQhROPA.jpeg?dl=1" title="07%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c4b9a4a34d62c8eae201ec56e49ff56e838c26e_2_606x500.jpeg" alt="07%20PM" data-base62-sha1="1KLHSi2GZtUfETxRKVx8NQhROPA" width="606" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c4b9a4a34d62c8eae201ec56e49ff56e838c26e_2_606x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c4b9a4a34d62c8eae201ec56e49ff56e838c26e_2_909x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c4b9a4a34d62c8eae201ec56e49ff56e838c26e_2_1212x1000.jpeg 2x" data-dominant-color="555560"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">07%20PM</span><span class="informations">1748×1442 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Amine (2019-12-01 16:57 UTC)

<p>It is probably the source data. the way some MRI sequences work is by providing a very detailed image on a plane at the acquisition level (coronal here, as of the sequence name), disregarding Multi planar reconstructions, as opposite to CTs which will always be based on axial slices to reconstruct other planes. But this depends on the MRI slice acquisition itself, within the same study you may find low slice thickness series that will provide excellent multi-planar reconstruction as well as high slice thickness (with good image clarity on a certain plane) that are targeted to image visual analysis on that same plane.</p>
<p>So the solution here might be to ask for lower slice thickness series.</p>

---

## Post #3 by @lassoan (2019-12-01 21:12 UTC)

<p>See some related discussion in this topic: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2" class="inline-onebox">Combining volumes - what am I missing?</a></p>

---
