---
topic_id: 34148
title: "Bug While Saving Data As Bundle With No Segments"
date: 2024-02-05
url: https://discourse.slicer.org/t/34148
---

# BUG while saving data as bundle with no segments

**Topic ID**: 34148
**Date**: 2024-02-05
**URL**: https://discourse.slicer.org/t/bug-while-saving-data-as-bundle-with-no-segments/34148

---

## Post #1 by @MJamal (2024-02-05 05:52 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<p>I loaded sample data with no segments and then saved it as a bundle.</p>
<p>Next time when i load the bundled file and try to add my first segment the effects does not seem to work. Here’s an image that shows i am not able to adjust threshold value as they appear disabled.</p>
<p>The threshold slider is neither sliding nor the spinner values:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57e1710bd2ceba2948b85900c58360d7079bf04d.png" data-download-href="/uploads/short-url/cxqxRYNuyPgk3iXvNBuJSev9xZr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e1710bd2ceba2948b85900c58360d7079bf04d_2_690x384.png" alt="image" data-base62-sha1="cxqxRYNuyPgk3iXvNBuJSev9xZr" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e1710bd2ceba2948b85900c58360d7079bf04d_2_690x384.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e1710bd2ceba2948b85900c58360d7079bf04d_2_1035x576.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57e1710bd2ceba2948b85900c58360d7079bf04d.png 2x" data-dominant-color="2C2F2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1141×635 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to know if this is a bug or something else?</p>

---

## Post #2 by @pieper (2024-02-05 12:55 UTC)

<p>Could be a bug.  Can you share an mrb that shows this problem on SampleData along with a step-by-step description of what you did to create it?  Also report what Slicer version you used.</p>

---

## Post #3 by @MJamal (2024-02-05 13:54 UTC)

<p>Sure, here are the steps I followed:</p>
<ol>
<li>Navigate to File → Download Sample Data → MRHead.</li>
<li>After downloading, simply press <code>Ctrl+S</code> to save the scene as an mrb bundle without making any further changes.</li>
<li>Go to File → Close Scene.</li>
<li>Then go to File → Add Data → Choose file(s) to add and load the previously saved mrb file.</li>
<li>Proceed to the Segment Editor, add one or more segments, and then navigate to the Threshold effect.</li>
<li>Attempt to change the threshold range; you will notice that it won’t work.</li>
</ol>
<p>Slicer version: <code>5.6.1 r32438 / 117ce5f</code></p>
<p>Here’s the mrb file for your reference:</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1bcMe9PCtSvt6SZk5ztp1sFfQvznPE2bP/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1bcMe9PCtSvt6SZk5ztp1sFfQvznPE2bP/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1bcMe9PCtSvt6SZk5ztp1sFfQvznPE2bP/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1bcMe9PCtSvt6SZk5ztp1sFfQvznPE2bP/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">2024-02-05-Scene.mrb</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @muratmaga (2024-02-05 16:40 UTC)

<p>I don’t think this has anything to do with bundle.</p>
<p>When the two sliders overlap (in your case they were both set to 78), they are hard to move around (because you don’t know which one is which). I would suggest typing value in the intensity field in one of the field to move them apart, and then you should be able to move them independently.</p>
<p>Otherwise, everything works as expected for me.</p>

---

## Post #5 by @MJamal (2024-02-06 01:10 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="34148">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I don’t think this has anything to do with bundle.</p>
</blockquote>
</aside>
<p>This occurs only when attempting to load a bundle that has no segments.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="34148">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I would suggest typing value in the intensity field in one of the field to move them apart, and then you should be able to move them independently.</p>
</blockquote>
</aside>
<p>Is changing the value in the intensity field effective for you? On my end, it doesn’t seem to work. I’ve attempted to modify the value, but it remains unchanged.</p>

---

## Post #6 by @muratmaga (2024-02-06 02:34 UTC)

<aside class="quote no-group" data-username="MJamal" data-post="5" data-topic="34148">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>This occurs only when attempting to load a bundle that has no segments.</p>
</blockquote>
</aside>
<p>This is what I get, following your instructions:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64e5f60e2c90ec55ddf3acf980efb9d613ef8047.jpeg" data-download-href="/uploads/short-url/eoAr44NXea8K1M3iJVMSKGs7AwL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64e5f60e2c90ec55ddf3acf980efb9d613ef8047_2_563x500.jpeg" alt="image" data-base62-sha1="eoAr44NXea8K1M3iJVMSKGs7AwL" width="563" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64e5f60e2c90ec55ddf3acf980efb9d613ef8047_2_563x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64e5f60e2c90ec55ddf3acf980efb9d613ef8047_2_844x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64e5f60e2c90ec55ddf3acf980efb9d613ef8047_2_1126x1000.jpeg 2x" data-dominant-color="8A8D87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2046×1814 563 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.</p>
<p>So all looks good to me.</p>
<aside class="quote no-group" data-username="MJamal" data-post="5" data-topic="34148">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>Is changing the value in the intensity field effective for you?</p>
</blockquote>
</aside>
<p>Yes, you should be able to type in a value directly into the<br>
threshold range boxes.</p>

---

## Post #7 by @MJamal (2024-02-06 04:38 UTC)

<p>Sorry, I forgot to mention one more step, which is to save the bundle while the segment editor module is open.</p>
<p>I have attached a video for your reference:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1tyr15I-fqalwKyngdpUph0i1hq9-lcDI/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1tyr15I-fqalwKyngdpUph0i1hq9-lcDI/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1tyr15I-fqalwKyngdpUph0i1hq9-lcDI/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1tyr15I-fqalwKyngdpUph0i1hq9-lcDI/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">slicer.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @MJamal (2024-02-07 08:30 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Could you please confirm whether this is a bug or not?</p>

---

## Post #9 by @pieper (2024-02-07 19:52 UTC)

<p>Yes, it sounds like a bug and should be filed.  Saving and restoring with the segment editor open sounds like a valuable clue.  You can file it at <a href="https://github.com/Slicer/Slicer/issues" class="inline-onebox">Issues · Slicer/Slicer · GitHub</a> and add a link to this discussion.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> hasn’t commented here yet, but he’ll probably want to have a look.</p>

---

## Post #10 by @MJamal (2024-02-12 11:33 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I’ve filed the issue. See <a href="https://github.com/Slicer/Slicer/issues/7576" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/7576</a>.</p>

---

## Post #11 by @MJamal (2024-02-28 05:53 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
Any update on this issue?</p>

---

## Post #12 by @lassoan (2024-02-28 13:22 UTC)

<p>The issue was that you cannot write an image file without voxel data, so an 1x1x1 array was used as image data, but when that segmentation was loaded then the extent was set to that single voxel.</p>
<p>I implemented a fix, just have not yet submitted the pull request.</p>

---

## Post #13 by @MJamal (2024-03-14 04:34 UTC)

<p>Understood.<br>
Thanks for the update <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---
