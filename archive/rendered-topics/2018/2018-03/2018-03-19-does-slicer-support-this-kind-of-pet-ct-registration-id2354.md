# Does Slicer support this kind of PET-CT registration?

**Topic ID**: 2354
**Date**: 2018-03-19
**URL**: https://discourse.slicer.org/t/does-slicer-support-this-kind-of-pet-ct-registration/2354

---

## Post #1 by @glhfgg1024 (2018-03-19 04:39 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.0<br>
Expected behavior: PET-CT registration<br>
Actual behavior: Not sure</p>
<p>Hi all, I have a this kind of data. For each case/patient, there are the following images:</p>
<pre><code>1. CT 
2. PET

3. CT for segmentation
4. DICOM-RT segmentation based on 3
</code></pre>
<p>The DICOM-RT 4 has the same voxel spacing as that of 3. And it seems 1,2,3 have different voxel spacing (thus they have different number of slices). 1 and 2 have different spatial size, 1 is 512x512 and 2 is 128x128.<br>
1 and 3 have different number of slices.</p>
<p>Does Slicer support this kind of registration? After registration, it is expected all the images have the same spacing. Thanks a lot! Any comments are greatly appreciated!</p>

---

## Post #2 by @ihnorton (2018-03-19 13:40 UTC)

<p>Generally speaking, yes. CT-CT should work very well; PET-CT can be a bit harder because PET is typically low resolution and has poorly defined skull. Please see the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary">Registration Case Library</a>, especially 8, 14, and 20.</p>
<p>I think most of the examples in the case library use other tools, but Elastix is now available as an extension and may be a good option to try first:</p>
<aside class="quote quote-modified" data-post="1" data-topic="165">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/elastix-registration-toolbox-is-now-available-in-slicer/165">Elastix registration toolbox is now available in Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a href="http://elastix.isi.uu.nl/">Elastix</a> is a very powerful registration toolbox with lots of advantages over stock ITK registration tools - it has many more metrics, transformation methods, constraints, optimizers, and it comes with a large registration parameter set database, which contains optimized settings for a wide range of registration tasks. 
This toolbox is now available in Slicer, through the SlicerElastix extension, in the latest nightly builds. 
Even the default settings work really well for simple (same patient, s…
  </blockquote>
</aside>


---

## Post #3 by @ihnorton (2018-03-19 13:42 UTC)

<p>Also, note that PET/CT scanners are often combined. So your 1-2 may be from the same scanner, in which case the images may already be implicitly aligned. Then you would only need to register 1 to 3.</p>

---

## Post #4 by @glhfgg1024 (2018-03-19 13:53 UTC)

<p>Hi <a class="mention" href="/u/ihnorton">@ihnorton</a> , greatly appreciated for your kind answer and suggestions!<br>
Thanks a lot!  I’ll try that.</p>
<p>I don’t know why the doctors contour on 3, not 1. Then we don’t need the registration. And for each CT, the patient will be injected the tracer once, which would harm the patient again.</p>

---

## Post #5 by @glhfgg1024 (2018-03-19 19:41 UTC)

<p>Hi <a class="mention" href="/u/ihnorton">@ihnorton</a>, I have another problem.</p>
<p>I have registered 1 to 3 and generated a transform. Then I used the transform to register 2 to 3. But the spatial size of 1 and 2 are not the same, e.g., 512x512 versus 128x128. I’m not sure how to do next. Could you please help give some hints? Thanks a lot!</p>
<p>The SlicerElastix will generate a transform. I think we cannot use this transform directly, right? We should first resample 2 to the same spatial size as 1, right?</p>

---

## Post #6 by @ihnorton (2018-03-19 21:46 UTC)

<aside class="quote no-group" data-username="glhfgg1024" data-post="5" data-topic="2354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/glhfgg1024/48/947_2.png" class="avatar"> glhfgg1024:</div>
<blockquote>
<p>The SlicerElastix will generate a transform. I think we cannot use this transform directly, right?</p>
</blockquote>
</aside>
<p>If you put the <code>Moving</code> volume under the transform (“Transforms” module), then the images will be comparable <em>within Slicer</em>; for example in the 2d and 3d views. I’m not sure if SlicerElastix will automatically put the volume under the new transform.</p>
<p>Otherwise, I believe if you select “Create New Volume” for the “Output Volume” field then Elastix will resample into the space of the <code>Fixed</code> image. See comments in the README here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerElastix">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerElastix" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/fd3be96e8291f6d6a252927c4d4188e39c7bb6fe1fce6efc6990a5db558003b0/lassoan/SlicerElastix" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerElastix" target="_blank" rel="noopener">GitHub - lassoan/SlicerElastix: This extension makes available Elastix...</a></h3>

  <p>This extension makes available Elastix medical image registration toolkit (http://elastix.isi.uu.nl/) available in Slicer. - GitHub - lassoan/SlicerElastix: This extension makes available Elastix m...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>(I haven’t used the module very much yet – probably <code>@lassoan</code> will comment with any corrections/suggestions when he sees this, within a few days)</p>

---

## Post #7 by @glhfgg1024 (2018-03-19 22:09 UTC)

<p>Yeah, got it! Thanks a lot!</p>

---

## Post #8 by @glhfgg1024 (2018-03-20 15:41 UTC)

<p>Hi <a class="mention" href="/u/ihnorton">@ihnorton</a>, I think I do the right thing.</p>
<p>I first resample the PET(128x128) to CT(512x512), the using the obtained transform (from SlicerElastix) to get the registered PET. Then it seems the PET and CT are both co-registered with the segmentation.</p>
<p>Thanks a lot for your kind advice!</p>

---

## Post #9 by @MSC19950601 (2018-12-11 08:57 UTC)

<p>How to resample the PET volume?</p>

---

## Post #10 by @lassoan (2018-12-11 23:48 UTC)

<p>You can use “Resample scalar/vector/dwi volume” module.</p>

---

## Post #11 by @MSC19950601 (2018-12-19 15:28 UTC)

<p>Could you give more details or tutorial about PET-CT co-registration?</p>

---

## Post #12 by @sandigeeup (2022-01-11 02:43 UTC)

<p>When you have 3 data sets, e.g ct, pet and MRI for registration, do you do this before you do any volume rendering or segmentation,  how does it work, what order registration if sets 1st or segmentations/ rendering?</p>

---
