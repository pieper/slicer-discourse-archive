# How to hide vtkMRMLAnnotationROINode only in 3d view?

**Topic ID**: 21178
**Date**: 2021-12-22
**URL**: https://discourse.slicer.org/t/how-to-hide-vtkmrmlannotationroinode-only-in-3d-view/21178

---

## Post #1 by @StephenLeePeng (2021-12-22 11:31 UTC)

<p>I have a requirement:<br>
When I switch to Volume Rendering module, I can Enable and Display ROI. Then a AnnotationROI node will generate and display in 3d view and three slice views.<br>
But I want to hide this AnnotationROI node only in 3d view.</p>
<p>What I have tried:<br>
I switch to Annotations module, and click “Edit” icon, then “Modify Annotation Properities” dialog appear, and I expand Advanced button, but I can’t hide this AnnotationROI in 3d view separate.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/653c41abc7df5f65d138441aa3851fa49dbe7610.png" data-download-href="/uploads/short-url/erzk3Efb81EwDZkPrCRaNDg0zO8.png?dl=1" title="lALPDhYBSRIM4LfNAl_NAuM_739_607" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/653c41abc7df5f65d138441aa3851fa49dbe7610_2_608x500.png" alt="lALPDhYBSRIM4LfNAl_NAuM_739_607" data-base62-sha1="erzk3Efb81EwDZkPrCRaNDg0zO8" width="608" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/653c41abc7df5f65d138441aa3851fa49dbe7610_2_608x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/653c41abc7df5f65d138441aa3851fa49dbe7610.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/653c41abc7df5f65d138441aa3851fa49dbe7610.png 2x" data-dominant-color="393939"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">lALPDhYBSRIM4LfNAl_NAuM_739_607</span><span class="informations">739×607 37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I want to know is there a method to hide it in 3d view?</p>

---

## Post #2 by @lassoan (2021-12-22 13:48 UTC)

<p>You need to switch to using markups ROI for this (which has many advantages anyway). In its display node you can control 2D and 3D visibility separately. You can also have multiple display nodes and specify in each of them which views you want to use them - this is useful if you want to make the ROI appear not just with different visibility but also different color, opacity, etc. in each view.</p>

---

## Post #3 by @jamesobutler (2021-12-22 14:48 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Using latest Slicer preview, going into the Volume Rendering module by default still creates a <code>vtkMRMLAnnotationROINode</code> instead of a <code>vtkMRMLMarkupsROINode</code>. Is there a plan to switch to the new ROI soon?</p>
<p>When I create a <code>vtkMRMLMarkupsROINode</code> using “Create ROI” from the Volume Rendering module, it is creating a Markups ROI that has no control points defined. Therefore when I enable “Crop”, the volume rendering completely disappears from the 3D View. I have to click the “Fit to Volume” button to actually begin using this new markups ROI easily.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38fcbf580e7c417e3674e6ab3c84b053e9b64ee7.jpeg" data-download-href="/uploads/short-url/888fkmo4cpX6BHqFufSSBngIeDZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38fcbf580e7c417e3674e6ab3c84b053e9b64ee7_2_690x373.jpeg" alt="image" data-base62-sha1="888fkmo4cpX6BHqFufSSBngIeDZ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38fcbf580e7c417e3674e6ab3c84b053e9b64ee7_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38fcbf580e7c417e3674e6ab3c84b053e9b64ee7_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38fcbf580e7c417e3674e6ab3c84b053e9b64ee7_2_1380x746.jpeg 2x" data-dominant-color="86868D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1038 257 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-12-22 16:13 UTC)

<p>I think we can switch the Volume Rendering module to use markups ROI. I will just add markups ROI support to CLI modules first.</p>
<p>When you manually create an ROI in Volume Rendering module (either annotation or markups) then it will have its default size. You can click “Fit to volume” button to fit to the volume. This is done automatically for the ROI that is created automatically, so this will not have to be changed when we switch to markups ROI.</p>

---

## Post #5 by @lassoan (2021-12-28 02:32 UTC)

<p>I’ve submitted a pull request that updates Crop Volume and Volume Rendering modules to use markups ROI by default (and adds a few related features and fixes):</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6094">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6094" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6094" target="_blank" rel="noopener">Use markups roi in crop volume and volume rendering</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:use-markups-roi-in-crop-volume-and-volume-rendering</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-12-28" data-time="02:28:15" data-timezone="UTC">02:28AM - 28 Dec 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="4 commits changed 38 files with 1428 additions and 1194 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6094/files" target="_blank" rel="noopener">
          <span class="added">+1428</span>
          <span class="removed">-1194</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">- Allow CLI modules to use markups ROI as input
- Update Volume Rendering and C<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6094" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rop Volume modules to use markups ROI node by default
- Fix in markups node API (rename CenterPosition property to CenterOfRotation, because a Center property already exists for ROI)
- Fix in specify geometry popup (set the exact requested output extent)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
