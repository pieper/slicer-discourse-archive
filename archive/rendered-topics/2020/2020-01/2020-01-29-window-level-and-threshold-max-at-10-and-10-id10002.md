---
topic_id: 10002
title: "Window Level And Threshold Max At 10 And 10"
date: 2020-01-29
url: https://discourse.slicer.org/t/10002
---

# Window/level and Threshold max at -10 and 10

**Topic ID**: 10002
**Date**: 2020-01-29
**URL**: https://discourse.slicer.org/t/window-level-and-threshold-max-at-10-and-10/10002

---

## Post #1 by @Xavierb (2020-01-29 17:13 UTC)

<p>Hi,</p>
<p>I am trying to manually set the min and max values for my volume, however I am unable to change the range of values below -10 and above 10 (image 1). The volume histogram also does not appear. I have attached some images to give an idea of what I am referring to.</p>
<p>image 2 shows that I clearly have values greater than 10 in my volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90097699a89258d10d081a04bfa1b6ba322f37b.png" data-download-href="/uploads/short-url/sG9eNK6tHDRZYeTwZfVIt2DwnzR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90097699a89258d10d081a04bfa1b6ba322f37b.png" alt="image" data-base62-sha1="sG9eNK6tHDRZYeTwZfVIt2DwnzR" width="690" height="177" data-dominant-color="858788"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">917×236 3.75 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f31f768cf657fb6dc5d2618cff8828df8697451.png" alt="image" data-base62-sha1="4rXQXwrcra3sYBU3yF1YkFbaQOB" width="330" height="131"></p>
<p>Thank you for any help.</p>

---

## Post #2 by @lassoan (2020-01-29 17:14 UTC)

<p>It seems that the volume is empty. What do you see in Volumes module / Volume information section?</p>

---

## Post #3 by @Xavierb (2020-01-29 17:37 UTC)

<p>Hi Andras,</p>
<p>Are you referring to this information?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/258397192ee12a4fe409249d2e756c257943d864.png" data-download-href="/uploads/short-url/5lRB1wiR9rq1XUFdzR66GnFMJJq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/258397192ee12a4fe409249d2e756c257943d864.png" alt="image" data-base62-sha1="5lRB1wiR9rq1XUFdzR66GnFMJJq" width="690" height="319" data-dominant-color="F0EFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">907×420 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2020-01-29 17:55 UTC)

<p>It seems that the volume only contains zeros. Where does this volume come from?</p>

---

## Post #5 by @Xavierb (2020-01-29 18:13 UTC)

<p>The volume is really just a mask that corresponds to segmentations from a lung. The values range from 0-234 where 0 represents the background and certain integers in that range correspond to a sublobe of the mask.</p>
<p>So the main priority is really to get the min value as 0 and max value as 234.</p>

---

## Post #6 by @lassoan (2020-01-29 18:32 UTC)

<p>The loaded image only has zeros (see “Scalar range” field min/max values). Do you get any warning/error when you load that file? What format you load that image from?</p>

---

## Post #7 by @Xavierb (2020-01-29 19:07 UTC)

<p>There was not any error. It is a little peculiar because I have loaded in other volumes with the scalar range field having 0 min/max values and did not encounter the problem.</p>
<p>The file format of the image is read in as an .hdr and .img pair.</p>
<p>Perhaps there’s a way to simply override this field?</p>

---

## Post #8 by @lassoan (2020-01-29 19:58 UTC)

<aside class="quote no-group" data-username="Xavierb" data-post="7" data-topic="10002">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xavierb/48/5815_2.png" class="avatar"> Xavierb:</div>
<blockquote>
<p>.hdr and .img pair.</p>
</blockquote>
</aside>
<p>That seems like an image in the very old Analyze 7.5 file format. I would recommend to convert them with any software that can still read them to nifti or nrrd and never use this file format. Also, the image orientation after conversion and fix it as needed, because image orientation in the old Analyze file format was implementation-dependent.</p>
<aside class="quote no-group" data-username="Xavierb" data-post="7" data-topic="10002">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xavierb/48/5815_2.png" class="avatar"> Xavierb:</div>
<blockquote>
<p>Perhaps there’s a way to simply override this field?</p>
</blockquote>
</aside>
<p>There is no override. The image is actually empty after it is loaded into Slicer. Maybe the file is corrupted or it is special in some way that prevents Slicer from loading it.</p>

---

## Post #9 by @Xavierb (2020-01-30 19:11 UTC)

<p>Thanks for your help!</p>

---
