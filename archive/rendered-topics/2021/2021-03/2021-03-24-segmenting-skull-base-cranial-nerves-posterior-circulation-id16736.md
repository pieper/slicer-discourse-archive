---
topic_id: 16736
title: "Segmenting Skull Base Cranial Nerves Posterior Circulation"
date: 2021-03-24
url: https://discourse.slicer.org/t/16736
---

# Segmenting skull base, cranial nerves & posterior circulation

**Topic ID**: 16736
**Date**: 2021-03-24
**URL**: https://discourse.slicer.org/t/segmenting-skull-base-cranial-nerves-posterior-circulation/16736

---

## Post #1 by @peter_adidharma (2021-03-24 03:10 UTC)

<p>Hello everyone,</p>
<p>I am planning to segment skull base from CT, and cranial nerves with posterior circulation arteries from MRI. Is there any way to fuse segmentation results from these two modalities (CT &amp; MRI) so that the end product merge precisely at its designated anatomical location?</p>
<p>Many thanks,<br>
Peter</p>

---

## Post #2 by @pieper (2021-03-24 13:54 UTC)

<p>Yes, you can easily merge these by first doing registration and then you’ll want to start with the CT as the master volume to set the segmentation geometry.  Then you can swap between the CT and MR to segment various structures.</p>
<p>The accuracy of the registration will determine the precision of the anatomical locations.  There are many methods you can study here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/registration.html</a></p>

---

## Post #3 by @peter_adidharma (2021-03-28 13:44 UTC)

<p>Dear All,</p>
<p>Thank you very much for the kind answer. I tried several methods of doing registration, including using elastix extension. Yet, none of the methods seems to be working the way it wanted to be.</p>
<p>Here I attached the CT &amp; MRI files I have been using. Is there any suggestion in dealing with registration of these two files?</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/e0ff92rk37cml6n/CT&amp;MRI.zip?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-zip-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/e0ff92rk37cml6n/CT&amp;MRI.zip?dl=0" target="_blank" rel="noopener nofollow ugc">CT&amp;MRI.zip</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Many thanks,<br>
Peter</p>

---

## Post #4 by @peter_adidharma (2021-04-05 01:50 UTC)

<p>Dear all,</p>
<p>As the previously uploaded file contains certain information that it shouldn’t, I uploaded the file as .nrrd here:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/sh/ka6vsiiu9wxx6f2/AADXdUuzJntCBpHzNLGfLqjia?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/sh/ka6vsiiu9wxx6f2/AADXdUuzJntCBpHzNLGfLqjia?dl=0" target="_blank" rel="noopener nofollow ugc">3D slicer</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I tried to take the MRI as close as it can get to the CT scan manually then applied the automatic registrations, yet it seems to make the aligment worse. Is there any suggestion in dealing with this case?</p>
<p>Many thanks,<br>
Peter</p>

---

## Post #5 by @pieper (2021-04-05 15:21 UTC)

<p>Hi Peter -</p>
<p>Thanks for sharing the data.  I was able to get what looks to me like a nice registration result.</p>
<p>Here’s what I did:</p>
<ul>
<li>Put the MR in a linear transform and got them close, then hardened the transform</li>
<li>I used CropVolume to get a roughly similar area of coverage where the MR is</li>
<li>used General Registration (BRAINS) with no initialization and setting the percentage of samples to 0.2 (instead of the default 0.002)</li>
<li>Used the Compare Volumes wizard with the Rock option to inspect the results</li>
</ul>
<p>DM me with your email address if you want me to send you the matrix, but hopefully you can just replicate the result on your end.</p>
<p>-Steve</p>
<div class="youtube-onebox lazy-video-container" data-video-id="EZ7n3Dcw3WA" data-video-title="MR+CT brains Screen Recording 2021 04 05 at 11 04 11 AM" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=EZ7n3Dcw3WA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/EZ7n3Dcw3WA/maxresdefault.jpg" title="MR+CT brains Screen Recording 2021 04 05 at 11 04 11 AM" width="" height="">
  </a>
</div>


---

## Post #6 by @peter_adidharma (2021-04-15 01:20 UTC)

<p>Dear Pieper,</p>
<p>Sorry for the late reply. Your suggestion works really well. Here I attach the segmentation results.</p>
<p>Many thanks,<br>
Peter<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c16854931aa67ce05460c824ad8e7390ee6e242.png" data-download-href="/uploads/short-url/aR6xm9gDuhw2LIRxxASJ4f19JSi.png?dl=1" title="Screen Shot 2021-04-15 at 08.20.24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c16854931aa67ce05460c824ad8e7390ee6e242_2_690x332.png" alt="Screen Shot 2021-04-15 at 08.20.24" data-base62-sha1="aR6xm9gDuhw2LIRxxASJ4f19JSi" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c16854931aa67ce05460c824ad8e7390ee6e242_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c16854931aa67ce05460c824ad8e7390ee6e242_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c16854931aa67ce05460c824ad8e7390ee6e242.png 2x" data-dominant-color="484944"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-15 at 08.20.24</span><span class="informations">1122×540 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
