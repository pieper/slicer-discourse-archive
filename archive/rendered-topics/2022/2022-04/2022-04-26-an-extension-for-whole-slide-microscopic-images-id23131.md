---
topic_id: 23131
title: "An Extension For Whole Slide Microscopic Images"
date: 2022-04-26
url: https://discourse.slicer.org/t/23131
---

# An extension for whole slide microscopic images

**Topic ID**: 23131
**Date**: 2022-04-26
**URL**: https://discourse.slicer.org/t/an-extension-for-whole-slide-microscopic-images/23131

---

## Post #1 by @gaoyi.cn (2022-04-26 16:07 UTC)

<p>Dear All,</p>
<p>Whole slide microscopy histopathology images can be as large as several GB in file size, with jpeg compression. I’m preparing an extension that uses python script module to dynamically load portions of the whole slide image (WSI) at the desired resolution into the current Slicer view.</p>
<p>I put some basic info at:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slicerscope.github.io/">
  <header class="source">

      <a href="https://slicerscope.github.io/" target="_blank" rel="noopener nofollow ugc">SlicerScope</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicerscope.github.io/" target="_blank" rel="noopener nofollow ugc">About SlicerScope</a></h3>

  <p>A 3D-Slicer based open platform for whole slide histopathology image computing</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’m hoping to add this through the extension management system and would like to hear about your suggestions/opinions.</p>
<p>Thanks!<br>
yi</p>
<p><strong>NOTE: The extension has been renamed to <code>BigImage</code></strong></p>

---

## Post #2 by @pieper (2022-04-26 17:32 UTC)

<p>This looks great, thanks <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>It would be cool to try this out with some of the &gt;14TB of microscopy data recently made available via IDC.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.canceridc.dev/t/idc-april-2022-release/264">
  <header class="source">
      <img src="https://aws1.discourse-cdn.com/business4/uploads/canceridc/optimized/1X/bcc7a5768242bd6bc0bb64d72a559597a035c060_2_32x32.jpeg" class="site-icon" width="32" height="32">

      <a href="https://discourse.canceridc.dev/t/idc-april-2022-release/264" target="_blank" rel="noopener" title="03:23AM - 06 April 2022">Imaging Data Commons – 6 Apr 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/338;"><img src="https://aws1.discourse-cdn.com/business4/uploads/canceridc/optimized/1X/2fa13d836b00f81c30ac10b8070997acd887f020_2_1024x503.png" class="thumbnail" width="690" height="338"></div>

<h3><a href="https://discourse.canceridc.dev/t/idc-april-2022-release/264" target="_blank" rel="noopener">IDC April 2022 release</a></h3>

  <p>NCI Imaging Data Commons April 2022 release is out!  Here are some of the highlights:    Data: slide microscopy imaging data is now available for all of the TCGA collections and for the NLST collection - that’s the total of &gt;14 TB of new slide...</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 1 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @gaoyi.cn (2022-05-05 07:21 UTC)

<p>Thank you Steve!</p>
<p>I have added the s4ext file to the extension index and created a pull request.</p>
<p>However when I was trying to create another PR for the shape analysis module, seems the two PRs are considered as one?</p>
<p>Not sure how i can retrieve the later one and do it in a separated PR…</p>
<p>Thanks for advice!</p>
<p>Best,<br>
yi</p>

---

## Post #4 by @pieper (2022-05-05 12:48 UTC)

<p>Hi Yi -</p>
<p>It sounds like perhaps you created the second pull request as a branch off the first pull request.  That would link them together in github.  To confirm the process, you should first checkout the mater branch of the extension index, create a branch for the first extension, add the file and push to github to create the first PR.  Then you checkout the master branch again, create a second branch for the second s4ext file, and then push the second branch to github to create a second PR.  Then each PR will have and independent history.  Can you try that?</p>
<p>Cheers <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><br>
Steve</p>

---

## Post #5 by @gaoyi.cn (2022-05-06 00:08 UTC)

<p>Hi Steve,</p>
<p>Yes that’s was the situation… I’ll do again following your advice.</p>
<p>Thanks!</p>
<p>Best,<br>
yi</p>

---

## Post #6 by @gaoyi.cn (2022-05-06 03:20 UTC)

<p>Hi Steve,</p>
<p>the new PR is created and the comments and suggestions in the previous PR by Andras and James have been addressed.</p>
<p>Thanks!<br>
yi</p>

---

## Post #7 by @sbalci (2022-08-27 07:54 UTC)

<p>Dear <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> Dr. Gao,<br>
The SlicerScope extension is not visible on Slicer 5.0.3.<br>
Would you please guşde me how to install your module.<br>
Best wishes<br>
Serdar Balci, MD, Pathologist</p>

---

## Post #8 by @jamesobutler (2022-08-27 15:41 UTC)

<p><a class="mention" href="/u/sbalci">@sbalci</a> it appears <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> renamed SlicerScope to SlicerBigImage so look for “BigImage” in the extensions manager.</p>

---

## Post #9 by @sbalci (2022-08-27 17:14 UTC)

<p>Hi,<br>
I could not find it either. They do not appear in extensions or modules.</p>
<p>I tried to built from github source but I could not do it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/917b62f523fcaf9a402f5bf2a1704e9b875d534d.png" data-download-href="/uploads/short-url/kKZAr3ZgNy4wpBcTszaThaDor2R.png?dl=1" title="Screen Shot 2022-08-27 at 20.13.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/917b62f523fcaf9a402f5bf2a1704e9b875d534d_2_690x409.png" alt="Screen Shot 2022-08-27 at 20.13.27" data-base62-sha1="kKZAr3ZgNy4wpBcTszaThaDor2R" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/917b62f523fcaf9a402f5bf2a1704e9b875d534d_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/917b62f523fcaf9a402f5bf2a1704e9b875d534d_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/917b62f523fcaf9a402f5bf2a1704e9b875d534d_2_1380x818.png 2x" data-dominant-color="D8DBDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-08-27 at 20.13.27</span><span class="informations">1772×1052 39.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58a86d487f1a403bc602b5d20e82f906eeaf9534.png" data-download-href="/uploads/short-url/cEiRXAMOJxUN5VV0DPfra5Zzkwc.png?dl=1" title="Screen Shot 2022-08-27 at 20.12.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58a86d487f1a403bc602b5d20e82f906eeaf9534_2_689x438.png" alt="Screen Shot 2022-08-27 at 20.12.45" data-base62-sha1="cEiRXAMOJxUN5VV0DPfra5Zzkwc" width="689" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58a86d487f1a403bc602b5d20e82f906eeaf9534_2_689x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58a86d487f1a403bc602b5d20e82f906eeaf9534_2_1033x657.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58a86d487f1a403bc602b5d20e82f906eeaf9534.png 2x" data-dominant-color="222222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-08-27 at 20.12.45</span><span class="informations">1346×856 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @sbalci (2022-08-27 17:23 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="23131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>BigImage</p>
</blockquote>
</aside>
<p>It does not appear under extension builds either:</p>
<p><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=BigImage" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=BigImage</a></p>

---

## Post #11 by @lassoan (2022-08-27 22:24 UTC)

<p>The BigImage extension was only submitted to the Extensions Index of Slicer-5.1, but not for Slicer-5.0. I’ve submitted it now, so if the extension is compatible with Slicer-5.0 then it will show up in the Extensions Manager in Slicer-5.0.3 tomorrow. Until then you can use Slicer-5.1.x (the latest Slicer Preview Release).</p>

---

## Post #12 by @sbalci (2022-08-28 11:03 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> thank you very much. I have switched to 5.1 version and I can download the module now.</p>
<p><a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> also reached me and instructed to 5.1.</p>
<p>thank you both.</p>
<p>I hope to use it in our group’s pancreas research.</p>
<p>Best wishes.</p>
<p>Serdar</p>

---
