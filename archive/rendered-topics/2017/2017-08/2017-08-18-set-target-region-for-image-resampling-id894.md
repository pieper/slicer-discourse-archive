---
topic_id: 894
title: "Set Target Region For Image Resampling"
date: 2017-08-18
url: https://discourse.slicer.org/t/894
---

# Set target region for image resampling

**Topic ID**: 894
**Date**: 2017-08-18
**URL**: https://discourse.slicer.org/t/set-target-region-for-image-resampling/894

---

## Post #1 by @jclauneuro (2017-08-18 02:03 UTC)

<p>Operating system: Ubuntu 16.04 LTS, MacOS 10.12.3<br>
Slicer version: 4.6.2, also tested on 4.7.0 latest<br>
Expected behavior: preserved transformed state when file opened outside Slicer including the entire volume of interest<br>
Actual behavior: volume transformed but inappropriately cropped following resampling</p>
<p>Hi there,</p>
<p>This question builds on another thread I’ve found on the Slicer forum:</p><aside class="quote quote-modified" data-post="1" data-topic="431">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jrobin/48/663_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/image-with-hardened-transform-returns-to-original-when-opened-outside-slicer/431">Image with hardened transform returns to original when opened outside Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Operating system: Windows 10 
Slicer version: 4.6.2 
Expected behaviour: After hardening transform, saved image volume will preserve transformed state when opened outside Slicer 
Actual behaviour: Image returns to original (un-transformed) orientation when opened outside Slicer 
Hello, 
I am trying to perform a simple rotation transformation to a .mha volume and then save the transformed result to be available outside of Slicer; however, when I open the saved result outside of Slicer, the image …
  </blockquote>
</aside>

<p>I have used the <strong>ACPC Transform</strong> module to align an image relative to the AC-PC plane in a brain volume (make it more symmetric). As a result, I have a transform matrix.</p>
<p>I first tried applying then hardening the transform and saving the volume (as .nii.gz format), but the transformation was not preserved (the output is identical to the input image). I followed the suggestion in the referenced thread and tried using the <strong>Resample Image (BRAINS)</strong> module with the following parameters:</p>
<h4><a name="p-3638-inputs-1" class="anchor" href="#p-3638-inputs-1" aria-label="Heading link"></a>Inputs:</h4>
<ul>
<li>Image to Warp: original_volume</li>
<li>Reference Image: none</li>
</ul>
<h4><a name="p-3638-outputs-2" class="anchor" href="#p-3638-outputs-2" aria-label="Heading link"></a>Outputs:</h4>
<ul>
<li>Output Image: transformed_volume</li>
<li>Pixel Type: float</li>
</ul>
<h4><a name="p-3638-warping-parameters-3" class="anchor" href="#p-3638-warping-parameters-3" aria-label="Heading link"></a>Warping Parameters:</h4>
<ul>
<li>Displacement Field (deprecated): None</li>
<li>Transform file: ACPC transform</li>
<li>Interpolation Mode: NearestNeighbor</li>
</ul>
<p>All other settings were by default. After clicking apply, the volume appears transformed but is inappropriately cropped. I believe this is a result of not specifying a Reference Image (help text: <em>“Reference image used only to define the output space. If not specified, the warping is done in the same space as the image to warp.”</em>). I don’t have a reference image that matches the dimensions to be expected post-transform.</p>
<p>Any thoughts on how to resolve this problem?</p>
<p>Thanks!<br>
jon</p>

---

## Post #2 by @lassoan (2017-08-18 03:06 UTC)

<p>If the external program properly uses axis directions information in the image header then you don’t need resampling. If your program ignores axis directions and operates in voxel space then you need resampling.</p>
<p>To resample using an arbitrary region, you can use <code>Crop volume</code> module:</p>
<ul>
<li>Input volume: your transformed volume (no need to harden the transform)</li>
<li>Input ROI: create a new RAS-axes-aligned  region of interest by selecting <code>ROI</code> mouse mode on the toolbar, clicking in the middle of the image and a corner in the image, then adjust the size as needed.</li>
<li>Click Apply</li>
</ul>
<p>ROI place mode on the toolbar:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00d2c02ba3d9c1b200b853fa74d9bc95c36ddd2d.png" alt="image" data-base62-sha1="7hwW0pXwI39iqOFFl6k7XkmjAV" width="212" height="299"></p>

---

## Post #3 by @jclauneuro (2017-08-18 04:17 UTC)

<p>Appreciate your quick response!</p>
<p>I’ve attached a screenshot of my current workflow. It may be worth stepping back for a moment to better explain my objective, which is to correct a tilt in an image volume. I have used the <strong>ACPC Transform</strong> module, to reorient the image, and want to resample it then export as .nii format (input image was also .nii format). The goal is to have the AC-PC anatomical structures (labelled as 1 and 2 in the screenshot) aligned to be parallel to the anterior-posterior axis of the resampled volume.</p>
<p>I am following your suggestion to use the <strong>Crop Volume</strong> module. You mention ways to augment the size of the ROI box (white outline on screenshot). Is there a way to rotate/ the ROI box? I’m also wondering if there is a more automatic way to detect the optimal crop volume (looks like the magenta-coloured box in the 3D view would be the optimal ROI box so if somehow that could be fed in as the input ROI to <strong>Crop Volume</strong>…).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66dbefc554ee9bd3128ada3290d471795f887c2e.jpeg" data-download-href="/uploads/short-url/eFVUFn1dFQU7u90ClKUh9qQhjI2.jpg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/66dbefc554ee9bd3128ada3290d471795f887c2e_2_649x499.jpg" alt="Screenshot" data-base62-sha1="eFVUFn1dFQU7u90ClKUh9qQhjI2" width="649" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/66dbefc554ee9bd3128ada3290d471795f887c2e_2_649x499.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/66dbefc554ee9bd3128ada3290d471795f887c2e_2_973x748.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66dbefc554ee9bd3128ada3290d471795f887c2e.jpeg 2x" data-dominant-color="43434B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1249×961 297 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2017-08-18 04:26 UTC)

<p>Create a new RAS-axes-aligned region of interest by selecting ROI mouse mode on the toolbar, clicking in the middle of the image and a corner in the image, then adjust the size as needed. If you make the Crop Volume module create the ROI for you or you use Fit ROI button then the ROI will be aligned with your volume’s axes and not with RAS axes.</p>
<p>Of course, you can also rotate the ROI box by applying the transform to it. If you use it for ACPC alignment, then you need to invert the transform if you apply it to the ROI.</p>

---

## Post #5 by @jclauneuro (2017-08-18 15:52 UTC)

<p>Thanks, this worked!</p>
<p>To recap, here is the workflow:</p>
<ol start="0">
<li>Import <em>original_volume</em> (.nii.gz) into 3D Slicer.</li>
<li>Compute the transformation using the <strong>ACPC Transform</strong> module.</li>
<li>Apply the transformation to the <em>original_volume</em> using the <strong>Transforms</strong> module.</li>
<li>Create a new RAS-axes aligned ROI (toolbar; see screenshot above from <a class="mention" href="/u/lassoan">@lassoan</a>) centered on the midpoint between AC and PC. Manually adjust the size of the box.</li>
<li>Use the <strong>Crop Volume</strong> module with the following settings, and hit Apply:
<ul>
<li>Input Volume: <em>original_volume</em>
</li>
<li>Input ROI: <em>R</em> (default name for new RAS ROI)</li>
<li>Output Volume: <em>transformed_volume</em>
</li>
<li>Interpolated Cropping: On</li>
<li>Spacing scale: 1.00x</li>
<li>Isotropic spacing: On</li>
<li>Interpolator: Linear</li>
</ul>
</li>
<li>Save the <em>transformed_volume</em> as .nii.gz</li>
</ol>
<p>Comments: It is not immediately obvious that post-tranformation resampling would be handled by a Slicer module called <strong>Crop Volume</strong> (luckily there is great support here!). A nice-to-have down the road would be to have resampling as options in the <strong>ACPC Transform</strong> or better yet the <strong>Transforms</strong> module (perhaps as an option next to “hardening the transform”)? I understand that part of the problem stems from the export to .nii.gz format (which is not handling the axis information the way Slicer expects), but it is worth considering that this is one of the most common neuroimaging file formats in use these days.</p>

---

## Post #6 by @lassoan (2017-08-19 04:30 UTC)

<p>What software do you use for visualizing the saved nifti file? If that software does not ignore image axis directions then you don’t even need resampling.</p>
<p>We could add resampling to Transforms or ACPC modules, but as you can see, resampling is not trivial (has many options), so overall it’s cleaner to have it in a separate module instead of repeating it in many modules. But I agree that having automatic fitting of RAS-axis-aligned ROI would be useful and it would be also nice to consolidate all the cropping/resampling modules (there are 4 of them), and have better names. Maybe “Crop and resample volume” name would be more descriptive?</p>

---

## Post #7 by @jclauneuro (2017-08-21 14:14 UTC)

<p>I use mainly fslview and ITK-snap for visualizing the saved nifti files. I’m not sure if nifti takes into account image axis directions.</p>
<p>I would put my vote in for a resampling option in Transforms with automatic fitting of RAS-axis aligned ROI. Consolidating the different options would also make sense. Is there a protocol I should follow for making these feature requests?</p>

---

## Post #8 by @lassoan (2017-08-22 02:24 UTC)

<p>Features requests can be entered at <a href="http://issues.slicer.org">issues.slicer.org</a>. However, this request is a typical example where we would need to choose between conflicting requirements of flexibility &lt;-&gt; ease of use of the software. Also, it is difficult to implement resampling of volume types in the core Transforms module for unknown volumes (that are defined in extensions, such as tensor volumes, 4D volumes, etc). In general, we try to keep core modules as simple as possible and not bundle multiple features, which are often used together in certain workflows, because in other workflows they are not, or they are combined with other modules.</p>
<p>Nowadays, we address conflicting flexibility &lt;-&gt; ease of use requirements and avoid complicated designs by implementing application-specific workflows by Python scripted modules. Very small and simple Python scripted modules can provide a streamlined user interface and internally use multiple core modules.</p>
<p>In your case, you could add a simple extension that would use ACPC, Transforms, and Resample modules to implement the complete processing workflow. If you think it would be too much work for you then what we can do is to add automatic ROI extension to one of the resample modules or maybe rename the Crop volume module to better reflect that it does resampling, too?</p>

---

## Post #9 by @lassoan (2017-08-22 02:34 UTC)

<aside class="quote no-group" data-username="jclauneuro" data-post="7" data-topic="894">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jclauneuro/48/1821_2.png" class="avatar"> jclauneuro:</div>
<blockquote>
<p>I use mainly fslview and ITK-snap for visualizing the saved nifti files. I’m not sure if nifti takes into account image axis directions.</p>
</blockquote>
</aside>
<p>ITK-Snap correctly reads image header but it does not support editing in oblique planes, so you need to resample the input images manually.</p>
<p>Slicer’s recently introduced <code>Segment Editor</code> module (available in nightly builds) does not have this limitation: you can segment in arbitrarily oriented planes (if needed, image resampling is performed automatically in the background). Segment Editor has many more effects than ITK-Snap and has many unique features (allows overlapping segments, has sophisticated masking options, editing in 3D views, support of standard DICOM terminologies, etc). I would recommend to try Segment Editor and let us know if you find that compared to ITK-Snap anything is missing or you cannot figure out how to use. See <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">reference manual</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation_for_3D_printing">tutorials</a>.</p>

---

## Post #10 by @jclauneuro (2017-09-22 02:43 UTC)

<p>Sorry for the delay in responding. I did not receive an email notice.</p>
<p>I understand your concerns about feature modifications to core modules. However if transforming 4D or diffusion data works as expected in the Transforms module, I would imagine it would be possible to also handle resampling in the module as well (just apply the same resampling to each of the associated volumes in the N-D dataset)?</p>
<p>Regarding quicker fixes, one of the modules named “Resample …” should handle this functionality so either of the options you proposed would work. It’s just intuitively where any beginner-to-immediate user would look.</p>
<p>I’ve been meaning to give the Segment Editor a try. (please tell me there is an undo button)</p>

---

## Post #11 by @lassoan (2017-09-22 13:44 UTC)

<aside class="quote no-group" data-username="jclauneuro" data-post="10" data-topic="894">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jclauneuro/48/1821_2.png" class="avatar"> jclauneuro:</div>
<blockquote>
<p>please tell me there is an undo button</p>
</blockquote>
</aside>
<p>There is.</p>
<p>Use the latest nightly version of Slicer.</p>

---
