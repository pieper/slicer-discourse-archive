---
topic_id: 21338
title: "Editing Segmentation Of Model And Saving It"
date: 2022-01-05
url: https://discourse.slicer.org/t/21338
---

# Editing segmentation of model and saving it

**Topic ID**: 21338
**Date**: 2022-01-05
**URL**: https://discourse.slicer.org/t/editing-segmentation-of-model-and-saving-it/21338

---

## Post #1 by @Raj_Kumar_Ranabhat (2022-01-05 15:06 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>Our lab created a model of spine based on fusion of CT and MR.</p>
<p>Here is the link</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/17IdTqRJaGpqKWOuAk-IeC3mNcQ5beAZi/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/17IdTqRJaGpqKWOuAk-IeC3mNcQ5beAZi/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/17IdTqRJaGpqKWOuAk-IeC3mNcQ5beAZi/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/17IdTqRJaGpqKWOuAk-IeC3mNcQ5beAZi/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">StandardModel.mrb</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I tried to make a segmentation smoother(nerves) and tried to save the file again in mrml or mrb .</p>
<p>But the issue is that, after saving the model/ bone (CT) gets cropped. I tried to fix this issue ( for example changing label map geometry) but didn’t work.</p>
<p>What could be the issue, Please advise for the solution. The mrb model is provided in the link.</p>

---

## Post #2 by @lassoan (2022-01-05 16:35 UTC)

<p>By default segmentations are saved using the “reference image geometry” (origin, spacing, axis directions, and extents) by default. In this segmentation, the reference image geometry has a narrower extent than the full extent of all segments, so when saved with default parameters then the segment is cropped.</p>
<p>If you want to use the minimum necessary extent that saves the full segmentation then you can check the “Crop to minimum extent” option in the Save Data dialog:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/111c51894b134df484f89f82aa54c87d453af047.png" data-download-href="/uploads/short-url/2rmMVkc9ODNxqJNMceS6rAo9MFx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/111c51894b134df484f89f82aa54c87d453af047_2_690x384.png" alt="image" data-base62-sha1="2rmMVkc9ODNxqJNMceS6rAo9MFx" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/111c51894b134df484f89f82aa54c87d453af047_2_690x384.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/111c51894b134df484f89f82aa54c87d453af047_2_1035x576.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/111c51894b134df484f89f82aa54c87d453af047_2_1380x768.png 2x" data-dominant-color="EAEBED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2151×1199 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you want to save the segmentation with the same geometry as one of the input images then before saving, use the “Specify geometry” button in Segment Editor:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/933e87a8f1a7da55f9d4149661ed78cf5d022dff.png" data-download-href="/uploads/short-url/l0A9MWR9e9I5mKa2TBXwGeVCkvd.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/933e87a8f1a7da55f9d4149661ed78cf5d022dff_2_690x400.png" alt="image" data-base62-sha1="l0A9MWR9e9I5mKa2TBXwGeVCkvd" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/933e87a8f1a7da55f9d4149661ed78cf5d022dff_2_690x400.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/933e87a8f1a7da55f9d4149661ed78cf5d022dff_2_1035x600.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/933e87a8f1a7da55f9d4149661ed78cf5d022dff_2_1380x800.png 2x" data-dominant-color="E7E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1640×953 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve tested these in with the latest Slicer Preview Release. If it does not work with the latest Slicer Stable Release then I would recommend to switch to the latest Slicer Preview Release.</p>
<p>We’ll make this behavior more clear (at least log a warning if the segmentation is cropped, but maybe expand the extents automatically). You can track the status of this here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6102">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6102" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6102" target="_blank" rel="noopener">Segmentation may be cropped when saved</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-01-05" data-time="16:29:19" data-timezone="UTC">04:29PM - 05 Jan 22 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-01-07" data-time="01:40:11" data-timezone="UTC">01:40AM - 07 Jan 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: High
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">If some parts of segments fall outside of the reference geometry then the segmen<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">tation is cropped (information is lost) without warning.

Originally the error was reported here: https://discourse.slicer.org/t/editing-segmentation-of-model-and-saving-it/21338

## Steps to reproduce

- Load this segmentation: https://1drv.ms/u/s!Arm_AFxB9yqHx-FOPAelcgsOIud1qA?e=Zz7wZ7
- Save the segmentation with default settings into a new file
- Load the saved segmentation from the new file -&gt; ERROR: the segmentation is cropped.

## Expected behavior

At the minimum, a warning should be displayed that explains that with this settings the segmentation will be cropped, and it would tell that the user should change reference geometry or enable "Crop to minimum extent" option.

If such segmentation (that has segments outside the reference geometry) can be easily created using latest Slicer Preview Release (e.g., by moving segments between segmentations) then we could consider expanding the extents automatically (with the effective extent) so that nothing is lost.

## Environment
- Slicer version: Slicer-4.13.0-2022-01-04
- Operating system: Windows 10</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
