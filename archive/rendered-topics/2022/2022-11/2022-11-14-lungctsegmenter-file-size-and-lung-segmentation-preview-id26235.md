---
topic_id: 26235
title: "Lungctsegmenter File Size And Lung Segmentation Preview"
date: 2022-11-14
url: https://discourse.slicer.org/t/26235
---

# LungCTSegmenter: File Size and "Lung segmentation preview "

**Topic ID**: 26235
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/lungctsegmenter-file-size-and-lung-segmentation-preview/26235

---

## Post #1 by @Faraday_Caraway (2022-11-14 14:51 UTC)

<p>Hello, I am a novice user of 3D Slicer and trying to use version 5.0.3 of the software in windows 11.<br>
I performed the same operation with my partner. But he and I got different results. He is a mac OS system user.<br>
First, I generated one more file than he did.<br>
Just like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9480625a4e87a8fb5c646fb7cdf15af9e90bf7e6.png" data-download-href="/uploads/short-url/lbHJ6shbvihjR5WiI7w9dUdUbEW.png?dl=1" title="1668437156682" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9480625a4e87a8fb5c646fb7cdf15af9e90bf7e6_2_690x153.png" alt="1668437156682" data-base62-sha1="lbHJ6shbvihjR5WiI7w9dUdUbEW" width="690" height="153" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9480625a4e87a8fb5c646fb7cdf15af9e90bf7e6_2_690x153.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9480625a4e87a8fb5c646fb7cdf15af9e90bf7e6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9480625a4e87a8fb5c646fb7cdf15af9e90bf7e6.png 2x" data-dominant-color="26343F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1668437156682</span><span class="informations">856×191 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
"Lung segmentation preview "is the file that was added.</p>
<p>Second, I saved the file in a different size than he did, and to be precise, the sharpness of the image formed by the segmentation performed was much worse than his.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd24f067563c12e4ffcb7665675896b29174b835.jpeg" data-download-href="/uploads/short-url/A7pWnCWPnb1PXy1cmjoRN9Wx2oB.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd24f067563c12e4ffcb7665675896b29174b835_2_690x41.jpeg" alt="2" data-base62-sha1="A7pWnCWPnb1PXy1cmjoRN9Wx2oB" width="690" height="41" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd24f067563c12e4ffcb7665675896b29174b835_2_690x41.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd24f067563c12e4ffcb7665675896b29174b835_2_1035x61.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd24f067563c12e4ffcb7665675896b29174b835_2_1380x82.jpeg 2x" data-dominant-color="2D272B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">3155×188 35.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ee128899872a1a0a2010a494f871828cb21c63c.png" data-download-href="/uploads/short-url/bfNDOKn3UxYARNCo056FkG4hK6o.png?dl=1" title="1668437342094" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ee128899872a1a0a2010a494f871828cb21c63c.png" alt="1668437342094" data-base62-sha1="bfNDOKn3UxYARNCo056FkG4hK6o" width="690" height="80" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1668437342094</span><span class="informations">821×96 3.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What may the reason be? Thanks for any help!</p>

---

## Post #2 by @rbumm (2022-11-14 17:29 UTC)

<p>“Lung segmentation preview” is generated when you “Start” the Lung CT Segmenter process during the placement of the markups.<br>
As soon as you press “Apply” you should get the “real” segmentation and the “preview” should be removed automatically,</p>

---

## Post #3 by @rbumm (2022-11-14 17:36 UTC)

<aside class="quote no-group" data-username="Faraday_Caraway" data-post="1" data-topic="26235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/faraday_caraway/48/15934_2.png" class="avatar"> Faraday_Caraway:</div>
<blockquote>
<p>Second, I saved the file in a different size than he did, and to be precise, the sharpness of the image formed by the segmentation performed was much worse than his.</p>
</blockquote>
</aside>
<p>The preview is generated from a downsampled copy of your input volume. That is why it might have a poor resolution.</p>
<p>So try again:</p>
<p>Start Slicer and load the volume.<br>
Go to Lung CT Segmenter and press “start”</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eb081ae71bfed1ee9631717436abdd046e43fb7.png" alt="image" data-base62-sha1="25WQAlipLn9ySjOlNxVQx4ljfNB" width="674" height="303"></p>
<p>Place your markups until the last one - the trachea markup.</p>
<p>Press “Apply”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/151bc4edfdf0e4d31578135ef5660551c2efa3c1.png" data-download-href="/uploads/short-url/30JwntHL6bmU8uqqYUqdaWSENcR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/151bc4edfdf0e4d31578135ef5660551c2efa3c1.png" alt="image" data-base62-sha1="30JwntHL6bmU8uqqYUqdaWSENcR" width="690" height="239" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×243 11.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Faraday_Caraway (2022-11-15 03:44 UTC)

<p>Thank you very much. I have solved my problems.</p>
<p>You are my guide on the path of learning! I really admire your work and I think this extension is really useful and cool!!!</p>

---
