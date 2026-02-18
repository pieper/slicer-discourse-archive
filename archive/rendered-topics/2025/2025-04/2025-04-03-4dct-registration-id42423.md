# 4DCT registration

**Topic ID**: 42423
**Date**: 2025-04-03
**URL**: https://discourse.slicer.org/t/4dct-registration/42423

---

## Post #1 by @Cesar (2025-04-03 13:00 UTC)

<p>I’ve been trying to register 4DCT data, but it seems like I’m missing a step or doing something wrong. Here’s what I’ve been doing:</p>
<ol>
<li>Load the data of interest (static and dynamic).</li>
<li>Segment the static data.</li>
<li>Create partial volumes based on step 2.</li>
<li>Place all the partial volumes inside the radius.</li>
<li>Perform registration using Hierarchy3DRegistration, but this is where I run into trouble (see picture below).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/173a45a763a76fc4fedcf97b725c3061b069fc14.jpeg" data-download-href="/uploads/short-url/3jtPpoBsLvnHRoq3m1KshCNxxFq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/173a45a763a76fc4fedcf97b725c3061b069fc14_2_690x441.jpeg" alt="image" data-base62-sha1="3jtPpoBsLvnHRoq3m1KshCNxxFq" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/173a45a763a76fc4fedcf97b725c3061b069fc14_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/173a45a763a76fc4fedcf97b725c3061b069fc14_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/173a45a763a76fc4fedcf97b725c3061b069fc14_2_1380x882.jpeg 2x" data-dominant-color="5A545B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1760×1125 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>Could you help me figure out what I might be doing wrong? Thank you!!!</p>

---

## Post #2 by @Amy_Morton (2025-04-03 14:10 UTC)

<p>You’re super close! Your hierarchy just needs to have model nodes instead of the partial volumes. You can use the segmentation nodes you generated, in the data module right clicking the node and select “export visible segments to models”. Then arrange them in a hierarchy and try registering.</p>
<ul>
<li>Shelly Belsky</li>
</ul>

---
