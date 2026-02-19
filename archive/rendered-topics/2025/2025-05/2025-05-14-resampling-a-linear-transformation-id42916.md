---
topic_id: 42916
title: "Resampling A Linear Transformation"
date: 2025-05-14
url: https://discourse.slicer.org/t/42916
---

# Resampling a linear transformation

**Topic ID**: 42916
**Date**: 2025-05-14
**URL**: https://discourse.slicer.org/t/resampling-a-linear-transformation/42916

---

## Post #1 by @muratmaga (2025-05-14 01:51 UTC)

<p>In the recent versions of Slicer, I am having a hard time exporting a resampled volume from a linear transform. Hardening simply changes the image direction matrix, so does the crop volume (when the image is under a linear transform). I am pretty sure at some point Crop Volume used to create a resampled image, but that doesn’t seem to be the behavior anymore.</p>
<p>I don’t want to use resample vector/DWI because that means I need to figure out a reference image and its extends. That’s too much unnecessary work.</p>
<p>Resampling is automatically done for non-linear transforms. I think this needs to be an option for linear transforms too (e.g., harden vs harden via resample),</p>

---

## Post #2 by @lassoan (2025-05-14 04:30 UTC)

<p>“Crop volume” module resamples the image if <code>Interpolated cropping</code> option is enabled. This behavior has not been changed in the past couple of years. The output volume is placed under the same transform as the input volume, so one thing to pay attention to is that if you want to have a volume with RAS-aligned axes then you need to harden the transform on the input volume before cropping. Would this fulfill your needs? If hardening the transform before cropping is an issue then we could add an advanced option to place the output under the parent transform of the ROI (instead of the parent transform of the input volume).</p>
<p>Adding a “Harden via resample” option would add quite a bit of noise to the GUI, as it would need to be added at 3 places (Data module / Subject hierarchy tab, right-click on transform column; Data module / Subject hierarchy tab, right-click on transformed node; Transforms module / Apply transforms) and it would be nice if the user could also specify the desired output spacing and background fill value.</p>
<p>I assume that you need this for reorienting non-clinical scans to canonical orientation. I think the closest to this is Crop volume module, we would just need to make it a bit easier to use it for this purpose. Maybe something like these would be sufficient:</p>
<ul>
<li>Add a “Reorient” checkbox (show/hide the transform interaction handles; if no transform is applied yet then add a parent transform) and a “Harden transform” button next to it (it would harden the transform on the volume). These would make it very easy to set the correct orientation.</li>
<li>Add a “Resize to volume” button (next to “Fit to volume” button), which would set the ROI axes to the axes of the parent transform (by default RAS) coordinate system axes and just change the size of the ROI to include the entire volume. If “Interpolated cropping” is enabled then the auto-fix button could use this “Resize to volume” button.</li>
</ul>
<p>Then reorientation could be completed by these steps:</p>
<ul>
<li>Check “Reorient” checkbox</li>
<li>Adjust the volume orientation in slice views using the transform handles</li>
<li>Click “Harden transform”</li>
<li>Click “Resize to volume”</li>
<li>Click “Apply”</li>
</ul>

---

## Post #3 by @muratmaga (2025-05-14 04:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="42916">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I assume that you need this for reorienting non-clinical scans to canonical orientation. I</p>
</blockquote>
</aside>
<p>True, and sometime people want to move data to other programs that does not read the image direction fields of NRRD (like Fiji). So volume needs to be resampled.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="42916">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>“Crop volume” module resamples the image if <code>Interpolated cropping</code> option is enabled.</p>
</blockquote>
</aside>
<p>I don’t think that true: This is my original data:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a6f0bb68ff57233f559595bf80591c849b965c1.jpeg" data-download-href="/uploads/short-url/m2brA7xKUX5wUMguE2t3AJHyBMd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6f0bb68ff57233f559595bf80591c849b965c1_2_690x277.jpeg" alt="image" data-base62-sha1="m2brA7xKUX5wUMguE2t3AJHyBMd" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6f0bb68ff57233f559595bf80591c849b965c1_2_690x277.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6f0bb68ff57233f559595bf80591c849b965c1_2_1035x415.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6f0bb68ff57233f559595bf80591c849b965c1_2_1380x554.jpeg 2x" data-dominant-color="828288"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×773 90.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Now I rotated with interaction widget to make it consistent with planes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c04916721ede6bfb52e8b64cef8ec6fe1cede68.jpeg" data-download-href="/uploads/short-url/mgcgSuRWD2ss8BzNwWXHurcD6pq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c04916721ede6bfb52e8b64cef8ec6fe1cede68_2_690x470.jpeg" alt="image" data-base62-sha1="mgcgSuRWD2ss8BzNwWXHurcD6pq" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c04916721ede6bfb52e8b64cef8ec6fe1cede68_2_690x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c04916721ede6bfb52e8b64cef8ec6fe1cede68_2_1035x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c04916721ede6bfb52e8b64cef8ec6fe1cede68.jpeg 2x" data-dominant-color="565663"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1367×932 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have hardened the interaction transform, and used the crop volume with interpolation checked and the first evidence that it is not resampled, output dimensions are not changing:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/524acd7ed6c64225bc291a20ef0abc2d50cb65e7.png" data-download-href="/uploads/short-url/bJZpPDiArswcbrSkdJj6z1tqdkX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/524acd7ed6c64225bc291a20ef0abc2d50cb65e7_2_469x500.png" alt="image" data-base62-sha1="bJZpPDiArswcbrSkdJj6z1tqdkX" width="469" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/524acd7ed6c64225bc291a20ef0abc2d50cb65e7_2_469x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/524acd7ed6c64225bc291a20ef0abc2d50cb65e7_2_703x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/524acd7ed6c64225bc291a20ef0abc2d50cb65e7.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×848 61.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And if you look at image directions of that cropped volume you can see it simply copied the transfrom from the original image:.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/903e417bb102efb9597d3fc1ca7392002bf5988e.png" data-download-href="/uploads/short-url/kA28z79qMKrj8z2AJuUiOi5XG4S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/903e417bb102efb9597d3fc1ca7392002bf5988e_2_690x446.png" alt="image" data-base62-sha1="kA28z79qMKrj8z2AJuUiOi5XG4S" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/903e417bb102efb9597d3fc1ca7392002bf5988e_2_690x446.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/903e417bb102efb9597d3fc1ca7392002bf5988e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/903e417bb102efb9597d3fc1ca7392002bf5988e.png 2x" data-dominant-color="EDF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">799×517 45.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The only way I can make this work, if I volume render and set the ROI to image extends in the volume rendering and then crop. The image is resampled.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614d8bbe7825f786d37fb29ec1511d0a32a65274.png" data-download-href="/uploads/short-url/dSMsguQNLoqZHF2wdrWFGeklldy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/614d8bbe7825f786d37fb29ec1511d0a32a65274_2_647x500.png" alt="image" data-base62-sha1="dSMsguQNLoqZHF2wdrWFGeklldy" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/614d8bbe7825f786d37fb29ec1511d0a32a65274_2_647x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614d8bbe7825f786d37fb29ec1511d0a32a65274.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614d8bbe7825f786d37fb29ec1511d0a32a65274.png 2x" data-dominant-color="EDF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">799×617 50.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2025-05-14 05:41 UTC)

<p>The ROI that “Fit to volume” button (or automatix “Fix” button) creates is aligned with the volume’s voxel axes (to avoid quality loss by default when cropping). That’s why the output volume had non-identity orientation matrix.</p>
<p>To get output volume with axes aligned with RAS directions, you can place an ROI manually (or as you did with the Volume Rendering module: create an ROI before the volume is transformed and then just change the size manually).</p>
<p>The “Resize to volume” button that I proposed above would simplify the ROI placement. It would create/update only the ROI <em>size</em> (to include the entire volume), but it would not change its <em>orientation</em> (by default it would be aligned with the parent coordinate system = RAS axes).</p>

---

## Post #5 by @muratmaga (2025-05-14 06:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="42916">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The ROI that “Fit to volume” button (or automatix “Fix” button) creates is aligned with the volume’s voxel axes (to avoid quality loss by default when cropping). That’s why the output volume had non-identity orientation matrix.</p>
</blockquote>
</aside>
<p>I think this is where we can provide the lossy, resampling option, for people who need. An option to set the ROI in the way Volume Rendering does, not align with voxel axes. Setting the ROI before and then modifying manually, or using the volume rendering is both cumbersome options.</p>

---

## Post #6 by @muratmaga (2025-05-14 15:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I added an issue on Slicer to track this: <a href="https://github.com/Slicer/Slicer/issues/8415" class="inline-onebox" rel="noopener nofollow ugc">Add an option to more easily resample linear transforms in Crop Volume · Issue #8415 · Slicer/Slicer · GitHub</a></p>

---

## Post #7 by @lassoan (2025-05-15 05:04 UTC)

<p>I agree, this feature will make it easier to create an RAS-axis-aligned volume by resampling.</p>

---

## Post #8 by @muratmaga (2025-09-27 20:13 UTC)

<p>This is now implemented. See the thread</p>
<aside class="quote quote-modified" data-post="11" data-topic="43393">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/creating-roi-box-markups-in-image-coordinates-rather-than-anatomical-coordinates/43393/11">Creating ROI box markups in image coordinates (rather than anatomical coordinates)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    for posterity this feature is now implemented in slicer, and part of the CropVolume module since Sept 21s. 


To align your volume with anatomical planes, hit expand “reorient volume” tab, then use the widgets to transform your volume and harden it to finalize. If you want to create a new volume that’s in inline with the world axes, choose the Align to world axis and resize from the new drop down associated with Fit to Volume button. This will resample the oriented volume into the new grid and s…
  </blockquote>
</aside>


---
