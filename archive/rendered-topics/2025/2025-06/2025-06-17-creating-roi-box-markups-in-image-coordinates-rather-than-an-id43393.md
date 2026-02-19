---
topic_id: 43393
title: "Creating Roi Box Markups In Image Coordinates Rather Than An"
date: 2025-06-17
url: https://discourse.slicer.org/t/43393
---

# Creating ROI box markups in image coordinates (rather than anatomical coordinates)

**Topic ID**: 43393
**Date**: 2025-06-17
**URL**: https://discourse.slicer.org/t/creating-roi-box-markups-in-image-coordinates-rather-than-anatomical-coordinates/43393

---

## Post #1 by @tvercaut (2025-06-17 16:44 UTC)

<p>Hi,</p>
<p>I am interested in getting 3D box annotations in MRI data. ROI markups appear to be a good fit for this but the current behaviour is counterintuitive to users. In particular, they got confused by getting forced into creating “skewed” boxes, see snapshot below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee29f34f0612d02d651bdc4a5e2d963435518463.png" data-download-href="/uploads/short-url/xYTw0NyAnGG3tj3noHVuLHRof99.png?dl=1" title="Screenshot 2025-06-17 at 10.37.11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee29f34f0612d02d651bdc4a5e2d963435518463.png" alt="Screenshot 2025-06-17 at 10.37.11" data-base62-sha1="xYTw0NyAnGG3tj3noHVuLHRof99" width="296" height="248"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-06-17 at 10.37.11</span><span class="informations">296×248 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It seems this comes from “conflicting” default behaviours in 3D Slicer. Indeed, by default, the MRI volume is loaded to display in image coordinates but the box ROI markups are created in anatomical coordinates. So it’s not a skew but rather an oblique clipping that is observed.</p>
<p>Anyway, I was thus wondering if there is an option to create box ROI markups that are aligned with image coordinates rather than anatomical ones. The UI and documentation don’t seem to indicate this is possible but probably I missed something:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#roi-settings-section">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#roi-settings-section" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#roi-settings-section" target="_blank" rel="noopener nofollow ugc">Markups — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If not from the UI, is it possible to customise <code>~/.slicerrc.py</code> or similar to introduce such a behaviour?</p>
<p>Best wishes,<br>
Tom</p>

---

## Post #2 by @muratmaga (2025-06-17 16:48 UTC)

<p>If you create ROI inside the Volume Rendering module, it will be aligned with respect to your rotated MRI image (and not be skewed) like that. There is sort of a related issue here:</p>
<aside class="quote" data-post="7" data-topic="42916">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/resampling-a-linear-transformation/42916/7">Resampling a linear transformation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I agree, this feature will make it easier to create an RAS-axis-aligned volume by resampling.
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2025-06-17 16:51 UTC)

<p>Good point! Most of the time users would probably want to place the ROI with axes aligned with the slice view axes, so probably we should change the placement behavior (instead of making it configurable).</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> would this behavior would be an improvement for your workflows, too?</p>

---

## Post #4 by @muratmaga (2025-06-17 16:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="43393">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> would this behavior would be an improvement for your workflows, too?</p>
</blockquote>
</aside>
<p>For us the biggest improvement would come enabling easier linear resampling after we manually align our microCT scans (which is the linked issue). If it is possible to do that both, that would be great.</p>

---

## Post #5 by @tvercaut (2025-06-17 18:22 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="43393" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If you create ROI inside the Volume Rendering module, it will be aligned with respect to your rotated MRI image (and not be skewed) like that.</p>
</blockquote>
</aside>
<p>I’m not sure I understand the suggestion. The behaviour is the same if I initiate the ROI markup in the volume rendering view. The box remains aligned with anatomical axes.</p>

---

## Post #6 by @tvercaut (2025-06-17 18:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="43393" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Good point! Most of the time users would probably want to place the ROI with axes aligned with the slice view axes, so probably we should change the placement behavior (instead of making it configurable).</p>
</blockquote>
</aside>
<p>That default behaviour would be great for us.</p>
<p>I am currently thinking about using a workaround to display images in anatomical coordinates but it’s not ideal for downstream usage where voxel grid based box ROIs would be expected. We would need to compute the tightest box in image coordinates that encapsulates the anatomically aligned box. This makes the annotation process fuzzier than I would hope but makes for a slighly more intuitive operation for annotaters.</p>

---

## Post #7 by @muratmaga (2025-06-17 18:30 UTC)

<aside class="quote no-group" data-username="tvercaut" data-post="5" data-topic="43393">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tvercaut/48/80445_2.png" class="avatar"> tvercaut:</div>
<blockquote>
<p>I’m not sure I understand the suggestion. The behaviour is the same if I initiate the ROI markup in the volume rendering view.</p>
</blockquote>
</aside>
<p>No, use the crop volume feature in the volume rendering module to create the ROI. Not the markups one.</p>

---

## Post #8 by @tvercaut (2025-06-17 18:44 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="43393" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>No, use the crop volume feature in the volume rendering module to create the ROI. Not the markups one.</p>
</blockquote>
</aside>
<p>I found a crop volume module but no crop volume function in the volume rendering module:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/cropvolume.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/cropvolume.html" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/cropvolume.html" target="_blank" rel="noopener nofollow ugc">Crop Volume — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
I assume you refer to the former.</p>
<p>I confirm this generate image axis aligned box ROIs but it’s not super intuitive to use. I’ll have a hard time convincing people to use that for annotation purposes.</p>
<p>But given that the functionality is there and these ROIs show in the list of markups, maybe the default behaviour through the markup module can be hacked with a python hook in the short term?</p>

---

## Post #9 by @muratmaga (2025-06-17 18:48 UTC)

<p>See the screenshot for crop volume functionality in volume rendering.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9c7579f4dca56c204b584ce661425e4e22f2ee.png" data-download-href="/uploads/short-url/4dX3C0cHDLg7HsMGn8y4Mw06OXc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9c7579f4dca56c204b584ce661425e4e22f2ee_2_690x461.png" alt="image" data-base62-sha1="4dX3C0cHDLg7HsMGn8y4Mw06OXc" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9c7579f4dca56c204b584ce661425e4e22f2ee_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9c7579f4dca56c204b584ce661425e4e22f2ee.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9c7579f4dca56c204b584ce661425e4e22f2ee.png 2x" data-dominant-color="BCB7C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">993×664 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is the same ROI markups initialized different. I agree it is cumbersome. I only offered this since it is available to do what you want to do right now (as opposed to wait for implementation, and funding for it).</p>

---

## Post #10 by @tvercaut (2025-06-17 19:05 UTC)

<p>Ah yes, clicking “Enable” and “Display ROI”  next to “Crop” in the “volume rendering” module also works, albeit for a single box ROI. The path through the “crop volume” module allows creation of multiple box ROIs.</p>

---

## Post #11 by @muratmaga (2025-09-27 20:12 UTC)

<p>for posterity this feature is now implemented in slicer, and part of the <code>CropVolume</code> module since Sept 21s.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8737">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8737" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8737" target="_blank" rel="noopener nofollow ugc">ENH: Add volume reorientation to Crop Volume module</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:crop-volume-reorient</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-09-20" data-time="18:24:43" data-timezone="UTC">06:24PM - 20 Sep 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 8 files with 528 additions and 69 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8737/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+528</span>
            <span class="removed">-69</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Orientation of the input volume can now be easily fixed in Crop Volume module us<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8737" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ing the new "Reorient volume" section.

Options are added to tune "Fit to volume" beheavior. It is now possible to align the cropped volume's ROI to the world coordinate system (or keep the current ROI orientation). This is useful if the user wants to align the cropped volume axes to the world coordinate system, for example to make segmentation in anatomical planes easier.

fixes #8415

&lt;img width="1282" height="1027" alt="image" src="https://github.com/user-attachments/assets/270c25cf-7b08-4f5d-9ac1-1da266aa824f" /&gt;

@muratmaga</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>To align your volume with anatomical planes, hit expand “reorient volume” tab, then use the widgets to transform your volume and harden it to finalize. If you want to create a new volume that’s in inline with the world axes, choose the <code>Align to world axis and resize</code> from the new drop down associated with Fit to Volume button. This will resample the oriented volume into the new grid and save the output to the output volume.</p>
<p>thanks for <a class="mention" href="/u/lassoan">@lassoan</a> implementing this.</p>

---

## Post #12 by @philippepellerin (2025-09-28 07:43 UTC)

<p>There was a fast and effective way to do that, as you suggested in an answer to one of my questions.</p>
<p>Reorient the slices with the Slice Plane Intersect with interaction enabled. Then, built the volume ROI and crop.</p>

---

## Post #13 by @muratmaga (2025-09-28 16:20 UTC)

<p>This is the same thing, integrated in a single module (CropVolume). You do the alignment, cropping and resampling all in one place…</p>

---
