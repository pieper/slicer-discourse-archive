---
topic_id: 4048
title: "After Saving And Re Opening Files I Cannot Re Edit The Label"
date: 2018-09-10
url: https://discourse.slicer.org/t/4048
---

# After saving and re-opening files, I cannot re-edit the labels using Editor

**Topic ID**: 4048
**Date**: 2018-09-10
**URL**: https://discourse.slicer.org/t/after-saving-and-re-opening-files-i-cannot-re-edit-the-labels-using-editor/4048

---

## Post #1 by @jamieng (2018-09-10 15:09 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8.1</p>
<p>Hi, as I am new to Slicer, I am still quite unsure about many terminology and especially about the file type extensions. Please excuse me if I use some terms wrongly.<br>
I was doing a segmentation of the knee joint using Editor module, but after I saved all the files as .nrrd format and re-opened the files on a separate occasion, the labels were all no longer in the original “colours” and classifications, but all ended up as black labels. I also could no longer use Editor to edit the labels, for instance paint over using the same thresholding effect I used previously.<br>
Please advise if there is anything I can do to re-edit the labels using the same properties I previously had in place, and if there is anything I can do to prevent such situations from arising again.</p>
<p>Thank you so much!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1eebda7b91b30986282d2e9cc98684eb9ddf0f02.jpeg" data-download-href="/uploads/short-url/4pxDxGuA49TvsC5Xx6Av9ZyBsuS.jpeg?dl=1" title="Capture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1eebda7b91b30986282d2e9cc98684eb9ddf0f02_2_690x356.jpeg" alt="Capture3" data-base62-sha1="4pxDxGuA49TvsC5Xx6Av9ZyBsuS" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1eebda7b91b30986282d2e9cc98684eb9ddf0f02_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1eebda7b91b30986282d2e9cc98684eb9ddf0f02_2_1035x534.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1eebda7b91b30986282d2e9cc98684eb9ddf0f02_2_1380x712.jpeg 2x" data-dominant-color="B5B5C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture3</span><span class="informations">1993×1031 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2018-09-10 15:12 UTC)

<p>The Editor module is considered a legacy module and is no longer maintained. Please import the labelmap to a segmentation node: Segmentations module import/export section or in Data module by right-clicking the labelmap and choose “Convert labelmap to segmentation node”. Once this is done, you can edit the segmentation in the Segment Editor module.</p>

---

## Post #3 by @cpinter (2018-09-10 15:13 UTC)

<p>One more piece of advice: please download a recent nightly. The Segment Editor module especially went through a lot of improvements since the release of 4.8.1.</p>

---

## Post #4 by @jamieng (2018-09-10 16:09 UTC)

<p>Hello, thank you so much for the prompt reply!<br>
However, I wasn’t able to find that option in the Data module after right-clicking. <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4326d3305c45a41ca007110c450ee3509bd3929b.jpeg" data-download-href="/uploads/short-url/9A3aHuS5edC3LWJVgVgzyH1P4ef.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4326d3305c45a41ca007110c450ee3509bd3929b_2_690x388.jpeg" alt="Untitled" data-base62-sha1="9A3aHuS5edC3LWJVgVgzyH1P4ef" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4326d3305c45a41ca007110c450ee3509bd3929b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4326d3305c45a41ca007110c450ee3509bd3929b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4326d3305c45a41ca007110c450ee3509bd3929b_2_1380x776.jpeg 2x" data-dominant-color="A8A9B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1920×1080 349 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also, what do you mean by “legacy module”?<br>
Does this also imply that after saving and re-opening, I won’t be able to use the Editor module to edit labelmaps, but can only use the Segment Editor to edit? (I previously did not use the Segment Editor, purely the Editor module, followed by the Surface Model &gt; Model Maker to create my 3D model.)</p>
<p>Thank you so much for your help!</p>

---

## Post #5 by @jamesobutler (2018-09-10 16:46 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I think suggesting to use a recently nightly is a good way for debugging to see if the issue has already been solved, but I don’t think all users should be using it.  If all users should be using it, then we would have a new stable release.  The editor module is listed as legacy in the nightly, but not legacy in the stable release.</p>
<p>Maybe the Slicer stable release schedule should be changed to more frequent releases instead of a yearly basis?</p>
<p><a class="mention" href="/u/jamieng">@jamieng</a> The Editor module is listed as legacy in the current Nightly, but you will still be able to use it.  The Segment Editor module is the newer replacement module for Editor.  In a future release the Editor module will be removed.</p>

---

## Post #6 by @cpinter (2018-09-10 16:58 UTC)

<p>We’re doing our best</p><aside class="quote quote-modified" data-post="1" data-topic="2486">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/update-toward-slicer-4-10-0/2486">Update: Toward Slicer 4.10.0</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    <a name="release-status-1" class="anchor" href="#release-status-1"></a>release status
We are getting close ! Thanks you everyone <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title="+1" alt="+1" class="emoji"> 
But considering that: 


the last VTK update addressing the <a href="https://issues.slicer.org/view.php?id=4510">#4510</a> (Cropping is broken with GPU Volume rendering if depth peeling is enabled), also introduced a  <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4071#note_395250">regression</a>. 


there are still issues with the <a href="https://discourse.slicer.org/t/extension-not-built-by-build-system/2462">extension build system</a>. - will be addressed in 4.10.0 


issue <a href="https://issues.slicer.org/view.php?id=4511">#4511</a> (Large camera view angle (used in OpenVR) not properly handled with GPU Volume Rendering) is not yet resolved. That seriously limits the usability of the Slice…
  </blockquote>
</aside>

<p>In the meantime, as 4.8.1 can now be considered ancient in terms of segmentation features, I disagree with you and think that users should use the nightly.</p>

---

## Post #7 by @lassoan (2018-09-10 17:17 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="4048">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If all users should be using it, then we would have a new stable release</p>
</blockquote>
</aside>
<p>Creating a stable Slicer release still requires a lot of manual effort, so unfortunately there is often a rather long time period when a nightly version is ready to be released as stable, yet it is still only labelled as nightly version.</p>
<p>Except a few very specific issues (which should only affect few users), the current nightly version works well, so the potential issues of nightly version are outweighed by those many fixes and improvements that it contains.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="4048">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Maybe the Slicer stable release schedule should be changed to more frequent releases instead of a yearly basis?</p>
</blockquote>
</aside>
<p>This is exactly the plan.</p>
<aside class="quote no-group" data-username="jamieng" data-post="4" data-topic="4048">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/22d042/48.png" class="avatar"> jamieng:</div>
<blockquote>
<p>I won’t be able to use the Editor module to edit labelmaps</p>
</blockquote>
</aside>
<p>You can still load labelmaps and edit them in Segment editor, you just need to import labelmaps into segmentation node as <a class="mention" href="/u/cpinter">@cpinter</a> described above.</p>
<aside class="quote no-group" data-username="jamieng" data-post="1" data-topic="4048">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/22d042/48.png" class="avatar"> jamieng:</div>
<blockquote>
<p>I also could no longer use Editor to edit the labels, for instance paint over using the same thresholding effect I used previously.</p>
</blockquote>
</aside>
<p>Per-structure volume management in Editor module was always very limited. As far as I know, per-structure volumes cannot be saved into the scene but you need to merge them into one labelmap before saving. Also, Editor module stores structure names in color nodes (separate from the nrrd files), so if you only save the nrrd files, then your labels are lost.</p>
<p>Since all these issues are solved by the new Segment Editor module (and will not be fixed in the old Editor module), it makes sense to switch from Editor to Segment Editor module. As Segment Editor is much improved in nightly version, it makes sense to switch from 4.8.x to the nightly version.</p>

---

## Post #8 by @jamieng (2018-09-10 17:35 UTC)

<p>I think I have a better idea of what you have been explaining now. I will use the Segment Editor module in future when I have to! Thank you so much for the advice and explanations.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thank you all so much for your help and expertise as well, it is much appreciated!</p>

---
