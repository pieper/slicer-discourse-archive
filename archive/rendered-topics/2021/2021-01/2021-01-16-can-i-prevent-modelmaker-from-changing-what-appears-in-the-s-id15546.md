---
topic_id: 15546
title: "Can I Prevent Modelmaker From Changing What Appears In The S"
date: 2021-01-16
url: https://discourse.slicer.org/t/15546
---

# Can I prevent ModelMaker from changing what appears in the Slice views?

**Topic ID**: 15546
**Date**: 2021-01-16
**URL**: https://discourse.slicer.org/t/can-i-prevent-modelmaker-from-changing-what-appears-in-the-slice-views/15546

---

## Post #1 by @sfrisken (2021-01-16 00:56 UTC)

<p>I am using ModelMaker in a custom Python module to generate models from a labelmap. I’ve used the code in EditorLib/MakeModelEffect.py as a template.</p>
<p>When the model is generated, the state of the views (i.e., the background image and labelmap) is changed so that only the generated model is visible. Can anyone tell me if this is an intended side effect? Is there a good way to retain the state of the views when the new model is added to the scene?</p>
<p>Note that this behavior occurs when I call ModelMaker from my module (the use case I am interested in), but it also occurs when I use ModelMaker from the Slicer module menu.</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2021-01-16 05:27 UTC)

<p>When a CLI module returns a mini-scene (as far as I know Model Maker is the only module that does this) then all MRML node selectors are reset. See details in this issue:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4570" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4570" target="_blank" rel="noopener">Selection in node selector is lost if importing a scene</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:03:36" data-timezone="UTC">01:03AM - 13 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">priority:high</span>
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The issue is still open, because it only impacts Model Maker, which is now not needed (model&lt;-&gt;segmentation&lt;-&gt;labelmap conversions can be done using segmentations) and the problem is really hard to solve.</p>

---

## Post #3 by @ond12 (2021-05-21 09:36 UTC)

<p>I have the same issue with this model Maker module.<br>
I tried the “labelmap conversions” as you said, but with this tool I can’t set the “smooth” or decimate" parameter. Is there a way to set thoose parameters with the labelmap conversions tool from "segment Editor " ?</p>

---

## Post #4 by @lassoan (2021-05-21 12:59 UTC)

<p>You can change decimation and smoothing parameters in Segmentations module as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#create-new-representation-in-segmentation-conversion">here</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d066dcc42ad32375dafc36d2fd6943139ccf5dda.png" data-download-href="/uploads/short-url/tJBH7lQ3o7snqGOqx1L6KLxmSx4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d066dcc42ad32375dafc36d2fd6943139ccf5dda_2_580x500.png" alt="image" data-base62-sha1="tJBH7lQ3o7snqGOqx1L6KLxmSx4" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d066dcc42ad32375dafc36d2fd6943139ccf5dda_2_580x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d066dcc42ad32375dafc36d2fd6943139ccf5dda_2_870x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d066dcc42ad32375dafc36d2fd6943139ccf5dda_2_1160x1000.png 2x" data-dominant-color="E8EAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1484×1278 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @ond12 (2021-05-21 13:14 UTC)

<p>Thank a lot very usefull, do you have a python code example that  change decimation and smoothing ?</p>

---

## Post #6 by @lassoan (2021-05-21 16:58 UTC)

<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#re-convert-using-a-modified-conversion-parameter">this example</a> in the script repository.</p>

---
