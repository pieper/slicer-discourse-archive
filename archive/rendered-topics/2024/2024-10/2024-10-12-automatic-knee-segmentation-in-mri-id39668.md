# Automatic knee segmentation in MRI

**Topic ID**: 39668
**Date**: 2024-10-12
**URL**: https://discourse.slicer.org/t/automatic-knee-segmentation-in-mri/39668

---

## Post #1 by @JulianZulu (2024-10-12 05:38 UTC)

<p>Hello,</p>
<p>I have a 3DMRI dataset of the same knee with the following scan types with acquisition matrix 0\512\350\0 and slice thickness of 0.74mm.</p>
<ul>
<li>PD (TE: 35, TR:1100)</li>
<li>PD FS (TE: 35, TR:1100)</li>
<li>DESS (TE: 5.3, TR: 14.8)</li>
</ul>
<p>Does anyone know if there is an AI that can automatically segment the following structures:</p>
<ul>
<li>Bones</li>
<li>Cartilage</li>
<li>Meniscus</li>
<li>Ligaments (Primarily ACL, PCL, LCL, MCL)</li>
</ul>
<p>Additionally but not essential:</p>
<ul>
<li>Muscles &amp; Tendons</li>
<li>Neurovasculature</li>
</ul>

---

## Post #2 by @pieper (2024-10-12 15:52 UTC)

<p>I believe this thread is still accurate.  There are some papers about building models like this and it should be a solvable problem but I don’t know of any off-the-shelf models.</p>
<aside class="quote" data-post="1" data-topic="37254">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/roshawnbrown/48/77209_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/are-there-automatic-segmentation-models-for-musculoskeletal-anatomy/37254">Are there automatic segmentation models for musculoskeletal anatomy?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello all, 
Thank you introducing this. Are there any segmentations available for musculoskeletal anatomy? Specifically, I am looking for joints, tendons, ligaments, bursae, and cartilage.If not, are there any resources out there on how to create such segmentations? 
Thank you.
  </blockquote>
</aside>


---
