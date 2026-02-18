# I am new to slicer,  after applying linear transform to a 3D images and save it on my local computes the images seems to be same as untransformed or original image is there a way I can save a transformed images 

**Topic ID**: 19006
**Date**: 2021-07-31
**URL**: https://discourse.slicer.org/t/i-am-new-to-slicer-after-applying-linear-transform-to-a-3d-images-and-save-it-on-my-local-computes-the-images-seems-to-be-same-as-untransformed-or-original-image-is-there-a-way-i-can-save-a-transformed-images/19006

---

## Post #1 by @Josiane (2021-07-31 18:39 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2021-07-31 19:28 UTC)

<p>Hardening with an affine only changes the header, not the pixels.</p>
<p>See this thread for more info:</p>
<aside class="quote" data-post="5" data-topic="2151">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c5a1d2/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-transformed-data/2151/5">Save transformed data</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have tried “hardening” the transformation and saving it. The saved images are in their native coordinate spaces and orientations. Is there a way to save them all regridded to the same 3D matrix? 
Sorry if this is an obvious question, but I can’t seem to find how to do this in the documentation. 
The data is all registered and ready to go. 
I have been meaning to learn Python, but don’t have time today to jump in. 
Thanks, 
Nathan
  </blockquote>
</aside>


---
