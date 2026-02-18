# Measuring angles from vector field

**Topic ID**: 12299
**Date**: 2020-06-30
**URL**: https://discourse.slicer.org/t/measuring-angles-from-vector-field/12299

---

## Post #1 by @Yordano_Jimenez (2020-06-30 15:01 UTC)

<p>Hi all,</p>
<p>I am vertebrate morphologist using Slicer to segment bones and muscles (from contrast-stained specimens).</p>
<p>I am currently in need of help with the following: I have segmented a chunk of muscle, analyzed its fiber tracks in a software by Heiko Stark (<a href="https://stark-jena.de/research-interests/software/" rel="noopener nofollow ugc">https://stark-jena.de/research-interests/software/</a>), and now have an output file with a vector field. Is there a way to measure these angles in bulk fashion relative to custom planes and not relative to CT space?</p>
<p>I should also mention that I have the vector field data in multiple file formats (txt, obj, track, etc.), but I don’t know which would be best for taking my measurements.</p>
<p>Any help would be greatly appreciated!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/483669e47f473b44010c04a726eaa7bb744b0716.png" data-download-href="/uploads/short-url/aiOXqIKqJhLcA2Kgc5vuo1ZNfzU.png?dl=1" title="myomere1_fibers_JUN29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/483669e47f473b44010c04a726eaa7bb744b0716_2_690x378.png" alt="myomere1_fibers_JUN29" data-base62-sha1="aiOXqIKqJhLcA2Kgc5vuo1ZNfzU" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/483669e47f473b44010c04a726eaa7bb744b0716_2_690x378.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/483669e47f473b44010c04a726eaa7bb744b0716_2_1035x567.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/483669e47f473b44010c04a726eaa7bb744b0716_2_1380x756.png 2x" data-dominant-color="ECDCDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">myomere1_fibers_JUN29</span><span class="informations">1921×1054 394 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-06-30 15:19 UTC)

<p>Is the vector field specified on a point set (points of a surface mesh or unstructured volumetric mesh) or a volume (dense rectilinear grid)?</p>
<p>Once you have loaded the data, computation of an angle between a plane and vectors is trivial, it should be just a couple of lines of Python script.</p>

---

## Post #3 by @Yordano_Jimenez (2020-06-30 15:34 UTC)

<p>It is specified on a volume, I think.</p>
<p>How would I go about extracting the position of the desired plane in order to perform the calculations in Python? For example, I would like to import a scene with the entire scan and then measure angles relative to the frontal plane and sagittal plane.</p>
<p>One final question, is it possible to measure relative to a curved plane? The CT scan has a fish in a bent position, so a straight reference plane would yield undesired measurements.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b54f82d7f4e595d9b08c17df66b97578e75ed390.png" alt="image" data-base62-sha1="pRWLYVmz7cbB5h9wxVtBcSZRdqE" width="537" height="421"></p>

---

## Post #4 by @lassoan (2020-06-30 21:19 UTC)

<aside class="quote no-group" data-username="Yordano_Jimenez" data-post="3" data-topic="12299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yordano_jimenez/48/5858_2.png" class="avatar"> Yordano_Jimenez:</div>
<blockquote>
<p>One final question, is it possible to measure relative to a curved plane? The CT scan has a fish in a bent position, so a straight reference plane would yield undesired measurements.</p>
</blockquote>
</aside>
<p>This should be no problem at all. I would straighten the volume using Curved Planar Reformatting module (in Sandbox extension) and then compute everything on the straightened volume. See for example this post:</p>
<aside class="quote quote-modified" data-post="7" data-topic="9456">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-implement-cpr-curved-plannar-reconstruction-from-centerline/9456/7">How to implement CPR (curved planar reconstruction) from centerline?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Andras, 
Sometimes people end up having to scan coiled snakes, or fish that are in little jars. Depending on what they need to do with it, they may have to ‘straighten’ the specimen. Is there a way this CPR can be generalized for such use cases? 
[image] 
[image]
  </blockquote>
</aside>


---
