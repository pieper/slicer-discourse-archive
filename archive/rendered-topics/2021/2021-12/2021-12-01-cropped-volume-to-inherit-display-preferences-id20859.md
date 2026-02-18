# Cropped volume to inherit display preferences

**Topic ID**: 20859
**Date**: 2021-12-01
**URL**: https://discourse.slicer.org/t/cropped-volume-to-inherit-display-preferences/20859

---

## Post #1 by @DIV (2021-12-01 03:00 UTC)

<p>In the <strong>Crop Volume</strong> module a user can create a new volume by cropping an existing volume.</p>
<p>Where the <em>existing volume</em> has a display <code>Preset</code> configured for 3D rendering in the <strong>Volume Rendering</strong> module and/or display settings (<code>Lookup Table</code> and <code>Window/Level</code>) configured for slice display in the <strong>Volumes</strong> module, the <em>cropped volume</em> loses this information.</p>
<p>I think it would be a nice default for the cropped volume to inherit this information from the original volume.</p>
<p>—DIV</p>

---

## Post #2 by @rbumm (2021-12-01 07:29 UTC)

<p>With a Slicer preview version, my cropped lung CT (top) gets the same volume window/level preset (“Lung CT”) as the source CT (bottom) [image source <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> open source COV dataset]</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b25df7b6807d44766132ac56b3b10bb6477ac54.jpeg" data-download-href="/uploads/short-url/3Sa27ocPA4kgbUayBYutn2BHwAA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b25df7b6807d44766132ac56b3b10bb6477ac54_2_449x500.jpeg" alt="image" data-base62-sha1="3Sa27ocPA4kgbUayBYutn2BHwAA" width="449" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b25df7b6807d44766132ac56b3b10bb6477ac54_2_449x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b25df7b6807d44766132ac56b3b10bb6477ac54_2_673x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b25df7b6807d44766132ac56b3b10bb6477ac54.jpeg 2x" data-dominant-color="757573"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">737×820 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @DIV (2021-12-10 03:29 UTC)

<p>Hello, Rudolf.<br>
Just today I have downloaded and installed the latest preview (4.13.0-2021-12-08).<br>
I can confirm that in this version of 3D Slicer the cropped volume:</p>
<ul>
<li>
<em>does</em> inherit the 2D slice display settings (per <strong>Volumes</strong> module);  but</li>
<li>
<em>does not</em> inherit the 3D reconstruction display settings (per <strong>Volume Rendering</strong> module).</li>
</ul>
<p>—DIV</p>

---

## Post #4 by @rbumm (2021-12-19 18:15 UTC)

<p>Sry, late reply. Thank you.</p>
<p>Is cropping and then volume rendering something you use often and lose too much time when selecting the preset? Could you maybe better crop <em>inside</em> volume rendering by using its ROI function? That is what I always do …</p>

---

## Post #5 by @lassoan (2021-12-19 20:13 UTC)

<aside class="quote no-group" data-username="DIV" data-post="3" data-topic="20859">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<ul>
<li><em>does not</em> inherit the 3D reconstruction display settings (per <strong>Volume Rendering</strong> module).</li>
</ul>
</blockquote>
</aside>
<p>You can choose to share volume rendering and cropping settings between multiple volumes. By default they are different, but in Volume Rendering module / Inputs section you can select the same ROI and Property nodes.</p>
<p>But I think <a class="mention" href="/u/rbumm">@rbumm</a>’s suggestion of cropping in Volume Rendering module is probably a better idea. You can later select the same ROI in Crop Volume module.</p>

---

## Post #6 by @DIV (2022-01-18 06:22 UTC)

<p>Hello, Rudolf &amp; Andras.</p>
<p>I would be regularly cropping (in the <strong>Crop Volume</strong> module) and volume rendering according to my current ‘workflow’.  I don’t think I would say “often”, though:  it would generally be once per CT scan.  This is for the purposes of <em>segmentation</em>, specifically:</p>
<ul>
<li>reducing the volume to be segmented (cutting computational load, and making it easier to see what’s going on);  and</li>
<li>improving the sampling properties (resolution &amp; aspect ratio of voxels), as per the advice below.</li>
</ul>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-can-i-configure-slicer-to-open-automatically-with-my-preferred-settings-for-the-view-controllers-module/20233/11">How can I configure Slicer to open automatically with my preferred settings for the View Controllers module?</a></div>
<blockquote>
<p>a one-time cropping and resampling to isotropic spacing before starting segmentation is usually beneficial.</p>
</blockquote>
</aside>
<aside class="quote" data-post="2" data-topic="21055">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/is-resampling-necessary/21055/2">Is Resampling Necessary?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If you are going to need to use filters for smoothing, or do morphological operations (dilation and erosion), you will find that resultant segments will look better if you have isotropic data.
  </blockquote>
</aside>

<p>On the other hand I do often use the cropping within the <strong>Volume Rendering</strong> module purely for visualisation.  AFAIK, the functionality in that module is not able to restrict the voxels being segmented, nor resample.  Did I miss something?</p>
<p>—DIV</p>

---
