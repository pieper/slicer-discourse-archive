---
topic_id: 7280
title: "Mask Ultrasound Volume Vector"
date: 2019-06-22
url: https://discourse.slicer.org/t/7280
---

# Mask Ultrasound Volume Vector

**Topic ID**: 7280
**Date**: 2019-06-22
**URL**: https://discourse.slicer.org/t/mask-ultrasound-volume-vector/7280

---

## Post #1 by @lRaulMN7 (2019-06-22 14:57 UTC)

<p>Hello! I saw this video: <a href="https://www.youtube.com/watch?v=TIUWzhkdspY" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=TIUWzhkdspY</a></p>
<p>Originally, the ultrasound image has some numbers and information on it, however in slicer only the ultrasound image can be seen.</p>
<p>Right now I have a vector volume from a stream, and I want to mask the number part. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a377a932aa800815188f85fbc4f56ce599b4d11a.png" data-download-href="/uploads/short-url/nk6coXB9rMSyC27tt69fV5461Rg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a377a932aa800815188f85fbc4f56ce599b4d11a_2_690x462.png" alt="image" data-base62-sha1="nk6coXB9rMSyC27tt69fV5461Rg" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a377a932aa800815188f85fbc4f56ce599b4d11a_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a377a932aa800815188f85fbc4f56ce599b4d11a_2_1035x693.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a377a932aa800815188f85fbc4f56ce599b4d11a.png 2x" data-dominant-color="535469"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1176×788 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have been trying to accomplish that using the segmentation tool but I can’t find the right way to do it…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/272e7bec7c4f279070c85903835fb19f4f4b577e.png" data-download-href="/uploads/short-url/5ACdcRvnWGDH2YTigQDANktqtpY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/272e7bec7c4f279070c85903835fb19f4f4b577e_2_690x459.png" alt="image" data-base62-sha1="5ACdcRvnWGDH2YTigQDANktqtpY" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/272e7bec7c4f279070c85903835fb19f4f4b577e_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/272e7bec7c4f279070c85903835fb19f4f4b577e_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/272e7bec7c4f279070c85903835fb19f4f4b577e.png 2x" data-dominant-color="54576A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1173×781 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Once I have the area I want to work with, is there any way to save it as a mask and add it to PLUS Server for future connections? Thanks!</p>

---

## Post #2 by @lassoan (2019-06-22 17:49 UTC)

<aside class="quote no-group" data-username="lRaulMN7" data-post="1" data-topic="7280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lraulmn7/48/3048_2.png" class="avatar"> lRaulMN7:</div>
<blockquote>
<p>I have been trying to accomplish that using the segmentation tool but I can’t find the right way to do it…</p>
</blockquote>
</aside>
<p>To blank out everything outside a segment, install SegmentEditorExtraEffects extension, then use “Mask volume” effect.</p>
<p>If you attach a position tracker to the ultrasound probe (can be as simple as a <a href="https://youtu.be/MOqh6wgOOYs">webcam</a> if you don’t require high accuracy) then you can set up real-time tracked image acquisition as shown in the youtube video that you referenced above.</p>

---

## Post #3 by @lRaulMN7 (2019-06-22 19:02 UTC)

<p>Mask Volume works perfectly! Thanks.</p>
<p>Now I can set a better ROI at the ultrasound image and then apply Mask Volume to get rid of the numbers.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b1a314ab4aea3df045bb2321ee5eaa99282019b.png" data-download-href="/uploads/short-url/69iEcPRLH2inVVKAsL2H74wyWgz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b1a314ab4aea3df045bb2321ee5eaa99282019b_2_690x307.png" alt="image" data-base62-sha1="69iEcPRLH2inVVKAsL2H74wyWgz" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b1a314ab4aea3df045bb2321ee5eaa99282019b_2_690x307.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b1a314ab4aea3df045bb2321ee5eaa99282019b_2_1035x460.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b1a314ab4aea3df045bb2321ee5eaa99282019b_2_1380x614.png 2x" data-dominant-color="9A9BA8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1922×856 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So now, once I have created this “Crop Volume ROI” , is there anyway to save together with the mask, and load it again? Because I have been trying to export it as a .acsv but I don’t know how to get it back in when I reset slicer.</p>
<p>Also, it could be good to remove those black corners, to just display the ultrasound image. Because if I reduce the ROI I’ll be missing information.</p>
<p>I’ll do the real-time tracked next weekend with a tracker (I’ll have to make the ImageToProbe transformation), now I just want to make sure that I’m able to display the ultrasound image in the best way.</p>
<p>Thanks again for the response <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> There is a lot of documentation and tutorials, but sometimes I can’t find the proper ones for my purposes.</p>

---

## Post #4 by @lassoan (2019-06-22 19:18 UTC)

<p>If you only need the mask for real-time display then it’s even simpler: create a mask image, enable thresholding in Volumes module, and set up slice viewer layers to use the mask image as background and the ultrasound image as foreground image.</p>

---

## Post #5 by @lRaulMN7 (2019-06-23 10:28 UTC)

<p>Works, clean solution! Thanks <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/955b4411d8928513b58c0108c810357e65ff920e.png" data-download-href="/uploads/short-url/ljgG7xirV7GJlDsIdtV8ln36D4q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/955b4411d8928513b58c0108c810357e65ff920e_2_690x283.png" alt="image" data-base62-sha1="ljgG7xirV7GJlDsIdtV8ln36D4q" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/955b4411d8928513b58c0108c810357e65ff920e_2_690x283.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/955b4411d8928513b58c0108c810357e65ff920e_2_1035x424.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/955b4411d8928513b58c0108c810357e65ff920e_2_1380x566.png 2x" data-dominant-color="ACACC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1433×588 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
