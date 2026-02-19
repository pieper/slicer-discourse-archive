---
topic_id: 19412
title: "Opening File Consumes Large Amount Of Memory"
date: 2021-08-30
url: https://discourse.slicer.org/t/19412
---

# Opening file consumes large amount of memory

**Topic ID**: 19412
**Date**: 2021-08-30
**URL**: https://discourse.slicer.org/t/opening-file-consumes-large-amount-of-memory/19412

---

## Post #1 by @hourglassnam (2021-08-30 11:28 UTC)

<p>Hello,<br>
I am so sorry for continuously asking similar questions, but I can’t get my head around this.<br>
I am still suffering from a bad allocation problem.<br>
This time, not during any process but just opening the file use memory up to 63GB.<br>
The memory usage spikes up to 63GB then lowers down to 18GB.<br>
And continuously use about 28GB of my memory without any process.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bab45876e57c55ddd914e0c10c4bab7339292b83.png" alt="화면 캡처 2021-08-30 170018" data-base62-sha1="qDFcht4wa4N64VwmvdMRvMgpcbN" width="415" height="50"><br>
Other files use up to 30-40GB during the opening process.<br>
below is my sample .mrb file.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15aJWGcfPi9_ZHXPDI25G8t8Eq2SQ_uAs%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15aJWGcfPi9_ZHXPDI25G8t8Eq2SQ_uAs%2Fview%3Fusp%3Dsharing&amp;ifkv=AaSxoQzqZtaiORjJ_tJRj2LEgB3g5gXo0yxVMA0truuDjpTC-WGzbItWp6Kcd50wmBtrnU8BOmlCMw&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1242000888%3A1715913387288118&amp;ddm=0">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15aJWGcfPi9_ZHXPDI25G8t8Eq2SQ_uAs%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15aJWGcfPi9_ZHXPDI25G8t8Eq2SQ_uAs%2Fview%3Fusp%3Dsharing&amp;ifkv=AaSxoQzqZtaiORjJ_tJRj2LEgB3g5gXo0yxVMA0truuDjpTC-WGzbItWp6Kcd50wmBtrnU8BOmlCMw&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1242000888%3A1715913387288118&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15aJWGcfPi9_ZHXPDI25G8t8Eq2SQ_uAs%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15aJWGcfPi9_ZHXPDI25G8t8Eq2SQ_uAs%2Fview%3Fusp%3Dsharing&amp;ifkv=AaSxoQzqZtaiORjJ_tJRj2LEgB3g5gXo0yxVMA0truuDjpTC-WGzbItWp6Kcd50wmBtrnU8BOmlCMw&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1242000888%3A1715913387288118&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Can anyone please tell me what I am doing wrong again?<br>
My computer is Window10, 64GB RAM, i7, RTX 3070 Graphic.<br>
Any help would be great.<br>
Thank you always.</p>

---

## Post #2 by @chir.set (2021-08-30 15:05 UTC)

<p>While not resolving your problem, I can at least confirm running in the same issue while loading your file on Linux. It consumes 64GB + 16 GB swap space before crashing Slicer. Please update if you find a solution or explanation.</p>

---

## Post #3 by @pieper (2021-08-30 15:11 UTC)

<p>What kind of file is this?  I’m not in a place where I can test at the moment, but if this is a highly compressed file it might actually require that much memory.</p>

---

## Post #4 by @hourglassnam (2021-08-30 16:23 UTC)

<p>Hello,</p>
<p>I used a series of reconstructed BMP files.<br>
(I don’t remember if it was 16 or 32 bit, but from what I know the dimension of each .bmp file is 1008*1008)</p>
<p>To write down the whole process:</p>
<ol>
<li>I used Skyscan1272 to take CT and then reconstructed the images into BMP files with a higher bit.</li>
<li>Then I dragged the BMP files into the 3D Slicer using the ImageStacks module.<br>
a. The Image spacing was set to 0.008um(the pixel size)<br>
b. I selected half resolution to optimize the process.</li>
<li>Then a series of segmentation processes was done in order to separate my samples from the surroundings.</li>
<li>I recreated another volume with full resolution and then used my segments to create cleaned-up volume of my samples.</li>
<li>I deleted all the volumes except for the cleaned-up version.</li>
<li>Then again, I went through series of segmentation process to separate each samples.</li>
<li>There are 8 samples and I used each segmented area to create new 8 volumes.</li>
<li>Each volume was going to be segmented once again to pull out final data such as volume, area, thickness, and etc.<br>
The last step couldn’t be done due to the file taking up too much memory.</li>
</ol>
<p>The segments I am trying to separate only have slight density differences. So I tried to work in high resolution to not lose any data. Maybe I was too greedy?</p>
<p>I saw somewhere that the BMP files create vector volumes and should be converted to scalar volume.<br>
I tried to do so, but my volumes were already scalar.<br>
I think I am doing something terribly wrong with my ignorance, but I just can’t figure out what.<br>
I wish I could attach my BMP files, but I don’t have my laptop with me at this moment.</p>

---

## Post #5 by @muratmaga (2021-08-30 16:54 UTC)

<p>I took a quick look at your scene file. I cannot load it to my laptop with 32GB of RAM either. The contents of the mrb files shows quite a few segmentation and a couple large volumes. I can load some of those individually without a problem, but I think the allocation problem happens when you try to load all of them.</p>
<p>Slicer has to keep everything loaded into the scene in the memory. So may not have sufficeint memory to load all of them at once. You can try to increase the virtual memory to get rid off the allocation error. Or selectively load a few things. MRB is just a zip file, you can decompress it like a zip archive and load the individual elements from it.</p>
<p>So for your last step, you can just load one volume, one segment to calculate area. Although you could have done this without separating your structures to 8 different subvolumes and loading them back individually into the same scene (which essentially doubled your memory consumption).</p>

---

## Post #6 by @hourglassnam (2021-08-30 17:11 UTC)

<p>Thank you so much for your reply.<br>
It is great to know that it is not the computer or the program’s fault!<br>
I will try to save the volumes individually.</p>
<p>May I ask another question?<br>
The reason I divided each volume was because the sectioning position is really important for me.<br>
I have not done it in this file but I tried to reposition each samples to achieve sectioning images at the same position.<br>
Can this be done without separating volumes? any suggestions?</p>
<p>Also, I wanted to get segment cross-section area of the transformed volume but couldn’t find a way to do so.<br>
Is there a way to get segment cross section area of the transformed volume?</p>
<p>Thank you always for help.</p>

---

## Post #7 by @muratmaga (2021-08-30 18:23 UTC)

<aside class="quote no-group" data-username="hourglassnam" data-post="6" data-topic="19412">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>segment cross-section area</p>
</blockquote>
</aside>
<p>First, I don’t think segment cross-sectional area works with transformed volumes at this point. There was some discussion but I am not sure if anythinng has changed. <a class="mention" href="/u/lassoan">@lassoan</a> ?</p>
<p>As for your memory issue, if your goal is to segment individual elements so that you can reorient them in an arbitrary plane, you should really use the ImageStack’s tools ROI option. That way you can reduce your memory usage considerably, since you will be importing only one specimen specimen at a time. Yes, this means you have to run ImageStacks eight times (since you have eight specimens in that scan), but that’s still considerably faster and memory efficient than using the segmentations.</p>

---

## Post #8 by @hourglassnam (2021-08-31 09:54 UTC)

<p>Thank you for your advice<br>
As you said, it probably is much faster to work with smaller 8 files than waiting for my monster to work.<br>
I will do accordingly.</p>
<p>For the segment cross-sectional area, I have read the discussion you have mentioned.<br>
I am assuming the module status is the same since then.<br>
I will just resample volume to work around the problem until any change is made.</p>
<p>One last question though, it seems like the original volume is needed as a reference volume to avoid the product being cropped during the resampling process.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffe4201db483b33c7087c1ef691524409c370868.jpeg" data-download-href="/uploads/short-url/AvIvIbliILUj1ZESan003ajlvVm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffe4201db483b33c7087c1ef691524409c370868_2_617x500.jpeg" alt="image" data-base62-sha1="AvIvIbliILUj1ZESan003ajlvVm" width="617" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffe4201db483b33c7087c1ef691524409c370868_2_617x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffe4201db483b33c7087c1ef691524409c370868_2_925x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffe4201db483b33c7087c1ef691524409c370868_2_1234x1000.jpeg 2x" data-dominant-color="58586F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2135×1730 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there any other way to prevent this without the original volume?<br>
So I can delete the original volume for the process optimization?</p>

---

## Post #9 by @muratmaga (2021-08-31 16:22 UTC)

<aside class="quote no-group" data-username="hourglassnam" data-post="8" data-topic="19412">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>One last question though, it seems like the original volume is needed as a reference volume to avoid the product being cropped during the resampling process.</p>
</blockquote>
</aside>
<p>As far as I know the original volume is only used as a reference geometry to set the geometry of the newly resampled volume. If your rotations moving the target out of the reference volume, then it will get cropped. In that case you need to make your reference volume in larger dimensions. But other may chime in.</p>

---

## Post #10 by @lassoan (2021-08-31 19:21 UTC)

<p>We (mostly <a class="mention" href="/u/chir.set">@chir.set</a>) worked a lot on cross-sectional measurements recently. I think the latest version of Centerline metrics module provides cross-sectional area measurements along arbitrary axis (or curve) without the need to transform the volume.</p>

---

## Post #11 by @chir.set (2021-08-31 21:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="19412">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>cross-sectional area measurements along arbitrary axis</p>
</blockquote>
</aside>
<p>Unfortunately, ‘Centerline metrics’ requires a markups curve that have ‘Radius’ scalars, i.e, produced by ‘Extract centerline’. It can of course be updated to work on arbitrary markups curve, except that the UI would become confusing.</p>
<p>I think there should be a separate module specially designed to calculate surface areas of models/segments  using arbitrary markups curve. Or add such a functionality to ‘Segment cross-section area’ module, based on ‘Centerline metrics’ approach.</p>
<p><a class="mention" href="/u/hherhold">@hherhold</a></p>

---

## Post #12 by @lassoan (2021-08-31 21:12 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="11" data-topic="19412">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Unfortunately, ‘Centerline metrics’ requires a markups curve that have ‘Radius’ scalars</p>
</blockquote>
</aside>
<p>We’ll remove that limitation. We cannot maintain 3 modules, each with an arbitrary set of limitations. We can easily make it one module for exploring and quantifying centerlines.</p>

---
