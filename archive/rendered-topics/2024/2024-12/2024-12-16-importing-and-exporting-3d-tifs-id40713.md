---
topic_id: 40713
title: "Importing And Exporting 3D Tifs"
date: 2024-12-16
url: https://discourse.slicer.org/t/40713
---

# Importing and exporting 3D TIFs

**Topic ID**: 40713
**Date**: 2024-12-16
**URL**: https://discourse.slicer.org/t/importing-and-exporting-3d-tifs/40713

---

## Post #1 by @Kajper (2024-12-16 13:51 UTC)

<p>Hello.<br>
I have received a CT scan in form of 3D tiff. It looks like a single image, but according to curator it contains all tiffs build in.<br>
However, the Slicer seem to not be able to read it properly (see attached)<br>
Also, I have tried to create my own 3d tiff in Slicer and try to load it. So I  go to Data and save volume as a TIF (2th photo). One enormous tif was saved. But importing this to Slicer give the same result as in previous case, some super thin slices in Green and Yellow windows but single slice in Red.<br>
Have anyone used Slicer to create such tiff format?<br>
Best regards<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90a109adc2031c1fae8cad92681a2ce891b25a4d.png" data-download-href="/uploads/short-url/kDrMdjf9cDFfp5UUcwMoX4q8UnX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90a109adc2031c1fae8cad92681a2ce891b25a4d_2_690x348.png" alt="image" data-base62-sha1="kDrMdjf9cDFfp5UUcwMoX4q8UnX" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90a109adc2031c1fae8cad92681a2ce891b25a4d_2_690x348.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90a109adc2031c1fae8cad92681a2ce891b25a4d_2_1035x522.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90a109adc2031c1fae8cad92681a2ce891b25a4d_2_1380x696.png 2x" data-dominant-color="37363D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1908×963 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8662ad1e14eba7caeabc5d01770cfec815bdd562.png" data-download-href="/uploads/short-url/jaPoqbL7y94G3vKiFNRmZccFzeW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8662ad1e14eba7caeabc5d01770cfec815bdd562.png" alt="image" data-base62-sha1="jaPoqbL7y94G3vKiFNRmZccFzeW" width="514" height="294"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">514×294 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-12-16 19:49 UTC)

<p>tiff isn’t an ideal format for 3d volumes so we don’t use it a lot with Slicer.  If you can, writing a small python script using an appropriate tiff library would be good.  Otherwise maybe use FIJI to split it up into files and use the ImageStacks module in SlicerMorph to load it.  Be sure you know the slice and pixel spacing of the sample.</p>

---

## Post #3 by @Kajper (2024-12-16 21:38 UTC)

<p>Ok, I will try this.<br>
Thanks!</p>

---

## Post #4 by @muratmaga (2024-12-17 01:43 UTC)

<p><a class="mention" href="/u/kajper">@Kajper</a> as I recall Slicer already supports multiframe TIFFs directly. You don’t need the ImageStacks to import the data. However, data loaded this will likely have incorrect image spacing. So after you loaded your file (just try drag and dropping into the slicer, and choose volume), go to <code>Volumes</code> module, check and edit the reported image spacing values and the immediately proceed to save the data a NRRD file to preserve the corrected values.</p>
<p>If you continue to keep them in TIFF format, those changes will be lost since TIFF cannot store that type of image geometry metadata.</p>

---

## Post #5 by @Kajper (2024-12-17 08:55 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/pieper">@pieper</a> thanks for help again. But it looks like the spacing is correct but the dimensions are wrong.<br>
Of course normally I would store the CT in NRRD but I want to try to combine Slicer and BounTI (<a href="https://github.com/Didziokas/BounTI" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Didziokas/BounTI</a>), that allows for automatic bone segmentation, and the only format it accepts is this 3D TIFF.<br>
Have you heard about analogous expansion for Slicer? I know there is a TotalSegmentator but I guess it works only on medical data (I tried it on the snake skull and does not work)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd22272d3f8d6cff46a5f06e446b098ec63083bf.png" data-download-href="/uploads/short-url/tgH3lv1qRfznC80Wdy91GkZ4qlh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd22272d3f8d6cff46a5f06e446b098ec63083bf.png" alt="image" data-base62-sha1="tgH3lv1qRfznC80Wdy91GkZ4qlh" width="548" height="391"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">548×391 9.82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2024-12-17 10:08 UTC)

<aside class="quote no-group" data-username="Kajper" data-post="5" data-topic="40713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kajper/48/18475_2.png" class="avatar"> Kajper:</div>
<blockquote>
<p>But it looks like the spacing is correct but the dimensions are wrong.</p>
</blockquote>
</aside>
<p>Did you try without the imagestacks? Imagestacks expects a sequence of images, not a single image with multiple frames. So it is reading only the first slice.</p>

---

## Post #7 by @muratmaga (2024-12-17 10:12 UTC)

<p>I just downloaded the sample multiframe tiff from the repository and dragged into slicer and as expected it loads perfectly fine but with wrong image spacing. This is also extremely simple segmentation task, I am not sure you need that iterative method to accomplish it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c37c1c13812a8819583ec76a2c886659e9e9b53b.jpeg" data-download-href="/uploads/short-url/rTl0EiP4CAYkDRO9Tc9EQvUCVbZ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c37c1c13812a8819583ec76a2c886659e9e9b53b_2_690x329.jpeg" alt="image" data-base62-sha1="rTl0EiP4CAYkDRO9Tc9EQvUCVbZ" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c37c1c13812a8819583ec76a2c886659e9e9b53b_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c37c1c13812a8819583ec76a2c886659e9e9b53b_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c37c1c13812a8819583ec76a2c886659e9e9b53b_2_1380x658.jpeg 2x" data-dominant-color="68696B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×917 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Kajper (2024-12-17 11:01 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> this BounTI requires this 3D TIFF, not a image stack. I am not familiarised with this kind of files as usually I have my CT in a series of normal TIFF. BounTI should segment every single bone separately, like in the photo, so it is not that easy task. I work with Slicer a lot on different scans so this kind of automatization would be great.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1317042c8e9db3dd64523cc36236f3f8e7c2e78c.jpeg" data-download-href="/uploads/short-url/2ISnOElEJ2yxj1n6OOGmbxroWFC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1317042c8e9db3dd64523cc36236f3f8e7c2e78c_2_690x339.jpeg" alt="image" data-base62-sha1="2ISnOElEJ2yxj1n6OOGmbxroWFC" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1317042c8e9db3dd64523cc36236f3f8e7c2e78c_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1317042c8e9db3dd64523cc36236f3f8e7c2e78c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1317042c8e9db3dd64523cc36236f3f8e7c2e78c.jpeg 2x" data-dominant-color="1E1C1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×392 43.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @muratmaga (2024-12-17 11:35 UTC)

<p>You should be able to do all this in Slicer without needing any additional tool using a combination of functions such as:<br>
threshold<br>
margin operation<br>
island tool<br>
and grow from the seed.</p>

---

## Post #10 by @muratmaga (2024-12-17 11:41 UTC)

<p>This took 10 seconds from loading data to creating this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6adaf88fb7d7b8379148cf4f820ee016cbaf389.jpeg" data-download-href="/uploads/short-url/uD8ivzTOjyshSHPpJdr8hdwQ91D.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6adaf88fb7d7b8379148cf4f820ee016cbaf389_2_690x346.jpeg" alt="image" data-base62-sha1="uD8ivzTOjyshSHPpJdr8hdwQ91D" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6adaf88fb7d7b8379148cf4f820ee016cbaf389_2_690x346.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6adaf88fb7d7b8379148cf4f820ee016cbaf389_2_1035x519.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6adaf88fb7d7b8379148cf4f820ee016cbaf389_2_1380x692.jpeg 2x" data-dominant-color="68686D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×964 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @muratmaga (2024-12-17 11:42 UTC)

<p>You can continue from this point on using the grow from seed to separate the vertebra, and then probably use the margin tool a bit more aggressively to pull apart the individual cranial bones.</p>

---

## Post #12 by @Kajper (2024-12-17 11:51 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I am aware of these methods. For fossils, it is the only way and Slicer is doing a great job. But some kind of automatization is clearly possible for modern species where the boundaries between the bones are clear.</p>

---

## Post #13 by @muratmaga (2024-12-17 15:17 UTC)

<p>So I am lost what you are asking from us? You can automate these in Slicer. But if you want to use the other tool that’s fine do.</p>

---

## Post #14 by @sulli419 (2024-12-20 00:45 UTC)

<p>I’m fairly new to slicer and might be missing the nuance of your question.  I have not tried saving a TIFF stack out of slicer (note that it’s not ideal to save your segments as TIFFs) but I was able to import a TIF stack into slicer doing the following… Open your single file TIFF stack in image J.  Click Save as&gt;image sequence (I found that 3d slicer only works when each slice is saved separately in one directory).  Install and run slicermorph extension in 3D slicer and follow the instructions in this video.  So far most the segmentation tools appear to be generally working on my TIFF file.    <a href="https://www.youtube.com/watch?v=1xvevF8tBws" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=1xvevF8tBws</a></p>

---

## Post #15 by @muratmaga (2024-12-20 01:28 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="14" data-topic="40713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>but I was able to import a TIF stack into slicer doing the following… Open your single file TIFF stack in image J. Click Save as&gt;image sequence (I found that 3d slicer only works when each slice is saved</p>
</blockquote>
</aside>
<p>If you read my answer above (linked below), you will see that you do NOT need to do any of these, as you can directly load a multiframe TIFF file into Slicer without having to do anything with FiJi or ImageStacks module. The only thing you need to do is to correct the spacing.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="40713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I just downloaded the sample multiframe tiff from the repository and dragged into slicer and as expected it loads perfectly fine but with wrong image spacing.</p>
</blockquote>
</aside>

---

## Post #16 by @sulli419 (2024-12-20 18:25 UTC)

<p>Thanks for reminding me to retry the simple method.  Yes, importing the single file TIFF stack by dragging into Slicer works–no extensions needed.  My Z voxel size was 100x the size and this was throwing me off as new user.  As you probably state somewhere, I went to volumes and corrected the image spacing and everything looks in order.  Cheers</p>

---

## Post #17 by @muratmaga (2024-12-21 03:04 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="16" data-topic="40713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>My Z voxel size was 100x the size and this was throwing me off as new user.</p>
</blockquote>
</aside>
<p>Thats exactly the reason Slicer does not want to save 3D volumes in these formats (including multiframe tiff). They don’t retain that information.</p>

---
