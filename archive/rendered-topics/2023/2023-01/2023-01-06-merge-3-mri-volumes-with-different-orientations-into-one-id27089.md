---
topic_id: 27089
title: "Merge 3 MRI volumes with different orientations into one"
date: 2023-01-06
url: https://discourse.slicer.org/t/27089
last_bumped: 2026-02-23T10:30:07.038Z
---

# Merge 3 MRI volumes with different orientations into one

**Topic ID**: 27089
**Date**: 2023-01-06
**URL**: https://discourse.slicer.org/t/merge-3-mri-volumes-with-different-orientations-into-one/27089

---

## Post #1 by @Audrina_Fernandez (2023-01-06 14:14 UTC)

<p>Hi,<br>
I’m working on MRI to segment cheek fat volume and often I have one serie of few images for axial axe, one serie for coronal axe, one serie for sagittal axe (for one patient, one IRM). To get a better volume segmentation I would like to stitch these series. Stitch volume module can help me to match differents axes or it is for differents series of the same axe?</p>
<p>Sorry for my English <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @mikebind (2023-01-09 22:16 UTC)

<p>As currently written, the Stitch Volumes module only works for stitching together image volumes which are distributed along one axis (like a series of CT or MR volumes taken at different table position stations).  Trying to combine overlapping MR imaging with higher resolution in differing orientations is a very different problem and would require a different approach.  This is a common desire because this is often how clinical imaging is collected, but there is not a commonly-used, effective way to generate a high resolution volume from multiple anisotropic image volumes (at least not that I am aware of).</p>
<p>Here are some links to other discussions where someone wanted to do this where you can find some explanations and suggestions:</p><aside class="quote" data-post="1" data-topic="5939">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/9e8a1a/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-multiple-directional-series/5939">Combining Multiple Directional Series </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have DICOM files from a brain MRI but they are separated into axial, coronal, and sagittal series and thus I cant work with them together as one volume. If I try the other two planes appear blurry. Is there  way to combined the three series?
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f19dbf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Mac - High Sierra 
Slicer version: 4.8.1 
Expected behavior: One perfect, high resolution volume 
Actual behavior: Three volumes, each one being high resolution in only one plane (sagittal, coronal, transverse) 
I have been using 3D Slicer for many months and I’m slowly learning the ropes. I am using it to produce anatomical boney models, and have probably created between 10-15 models. 
After loading CT scans from their DICOM folder I always get several volumes, often with the …
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="5791">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/e95f7d/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/can-i-use-axial-coronal-and-sagittal-from-different-scans/5791">Can I Use Axial Coronal and Sagittal from Different Scans?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have loaded a DICOM file into Slicer. When I look at the Data module, I can see the separate scans done for each plane (a scan for axial, sagittal, and coronal) and each is listed as a volume. When looking at one of these volumes - axial for example - it shows the red, yellow, and green slices, and if I turn on the sight for the volume in Volume Rendering, I can see it there as a 3D rendering. The red slice window is the axial window, and in it shows the master information that the green and y…
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="2" data-topic="5478">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/3d-model-from-dicoms/5478/2">3D model from dicoms</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    First of all, what would you like to segment? Simple thresholding works well in cases when structures of interest have highly distinctive intensity value on the image (bone on CT, contrasted vessels, etc.). If you want to segment bone on MRI then you need to use more sophisticated tools than thresholding. 
Another problem is that, quite often 3 anisotropic MRI images are acquired (high resolution along two axes, very low resolution along a third axis) to reduce time spent in the MRI scanner. How…
  </blockquote>
</aside>


---

## Post #3 by @Vikas_Rajpurohit (2023-11-27 07:19 UTC)

<p>Actually, I have a solution to these to this problem, but should i tell it or not because like literally spent over more than 46 hours for solving this problem. But i can give u a hint that , try to think this problem as an vein diagram. You will find its solution for sure. Thanks</p>

---

## Post #4 by @nakcali (2026-02-14 14:13 UTC)

<p>Could you help me? I</p>

---

## Post #5 by @drnoorfatima (2026-02-20 10:58 UTC)

<p>You can dm me what issue specifically you are facing??</p>

---

## Post #6 by @nakcali (2026-02-22 20:40 UTC)

<p>Hello Fatima,</p>
<p>I am trying to create a 3D model of my brain. I am using Swiss Skull Stripper, but I am not able to do it properly. It looks like lego brain. My MRI data seem to be divided into several groups (for example: right side, left side, front side, etc.).</p>
<p>When I use 3D Slicer, it only uses one group and tries to create the 3D model from images taken from a single direction. Because of this, I think the process does not work correctly.</p>
<p>I am attaching some screenshots from the application. When I select a group, only one view has good resolution; the other views appear to reuse the same images from one side.</p>
<p>Could someone please help me understand how to do this correctly?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/516ad206e42181a0f8b72125c687ff9e67d28b69.jpeg" data-download-href="/uploads/short-url/bCfxhrru75vyDek5dfzWPqyMSH7.jpeg?dl=1" title="Ekran görüntüsü 2026-01-20 123545" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/516ad206e42181a0f8b72125c687ff9e67d28b69_2_690x409.jpeg" alt="Ekran görüntüsü 2026-01-20 123545" data-base62-sha1="bCfxhrru75vyDek5dfzWPqyMSH7" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/516ad206e42181a0f8b72125c687ff9e67d28b69_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/516ad206e42181a0f8b72125c687ff9e67d28b69_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/516ad206e42181a0f8b72125c687ff9e67d28b69_2_1380x818.jpeg 2x" data-dominant-color="454346"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2026-01-20 123545</span><span class="informations">1919×1140 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd94b5babf5c12e91b4f18b17b5f087101c4f46f.jpeg" data-download-href="/uploads/short-url/vCc85kBe06tXHRr4khevKWKjSmX.jpeg?dl=1" title="Ekran görüntüsü 2026-01-20 123528" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd94b5babf5c12e91b4f18b17b5f087101c4f46f_2_690x412.jpeg" alt="Ekran görüntüsü 2026-01-20 123528" data-base62-sha1="vCc85kBe06tXHRr4khevKWKjSmX" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd94b5babf5c12e91b4f18b17b5f087101c4f46f_2_690x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd94b5babf5c12e91b4f18b17b5f087101c4f46f_2_1035x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd94b5babf5c12e91b4f18b17b5f087101c4f46f_2_1380x824.jpeg 2x" data-dominant-color="464447"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2026-01-20 123528</span><span class="informations">1919×1146 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3d511050efcb70c49dd95d57b1197f79aa39a18.jpeg" data-download-href="/uploads/short-url/wvuStrvl6ZOlyA0u1Qpmz7dCWMg.jpeg?dl=1" title="Ekran görüntüsü 2026-01-20 123515" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3d511050efcb70c49dd95d57b1197f79aa39a18_2_690x411.jpeg" alt="Ekran görüntüsü 2026-01-20 123515" data-base62-sha1="wvuStrvl6ZOlyA0u1Qpmz7dCWMg" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3d511050efcb70c49dd95d57b1197f79aa39a18_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3d511050efcb70c49dd95d57b1197f79aa39a18_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3d511050efcb70c49dd95d57b1197f79aa39a18_2_1380x822.jpeg 2x" data-dominant-color="403E42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2026-01-20 123515</span><span class="informations">1919×1144 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @drnoorfatima (2026-02-23 01:52 UTC)

<p>Hi!</p>
<p>I can see exactly what’s happening here. The issue isn’t with Swiss Skull Stripper itself,  it’s that you’re running it on the wrong sequence. Looking at your data, not all your MRI sequences are suitable for 3D reconstruction, and selecting the right one makes all the difference between a “lego brain” and a clean model.</p>
<p>The good news is you actually have the right data for a proper 3D brain model in your dataset, it just needs to be identified and processed correctly.</p>
<p>I do this kind of work professionally. If you’d like it done properly without the trial and error you can dm me.</p>
<p>Good Luck.</p>

---

## Post #8 by @nakcali (2026-02-23 10:06 UTC)

<p>Hi,</p>
<p>Thank you for your response. I’d really appreciate your help with this. However, I don’t see an option to send you a direct message here. Could you please let me know how I can contact you?</p>
<p>Best regards.</p>

---

## Post #9 by @drnoorfatima (2026-02-23 10:30 UTC)

<p>i texted you check dm</p>

---
