# Rendering images sequentially

**Topic ID**: 32231
**Date**: 2023-10-15
**URL**: https://discourse.slicer.org/t/rendering-images-sequentially/32231

---

## Post #1 by @ehdrmfdl3648 (2023-10-15 13:42 UTC)

<p>Good to see you.<br>
Thank you very much for developing 3d slicer.</p>
<p>I am currently working on a project using 3d slicer, but there is one problem.</p>
<p>What I am trying to do is to display an ultrasound image in 3D space. I have a position sensor for this.</p>
<ol>
<li>i imported the ultrasound image from verasonics into 3d slicer using openIGTL.</li>
<li>I also imported the transform matrix using the electromagnetic sensor data from polhemus into 3d slicer using openIGTL.</li>
</ol>
<p>As a result, I was able to display a single piece of ultrasound data in 3d slicer at the location I sent it.</p>
<p>Now what I want to do is send the next one,<br>
When I send the next image, the first visualization disappears.</p>
<p>Is there any way to visualize consecutive imported frames without losing them?</p>
<p>Any help would be appreciated!</p>
<p>ㅜ…ㅜ</p>

---

## Post #2 by @lassoan (2023-10-15 21:44 UTC)

<p>We usually record image and transform time sequences using Sequences module. Add a sequence for each node you want to record, set the proxy node to the changing node, and enable recording. You can then click record button on the sequence toolbar to start recording.</p>
<p>You can add a browser node for each time point you want to display. However, we usually create a 3D volume from the tracked image frames using the volume reconstruction module, because then you can show the image in 3D, create 3D segmentations, or reslice anywhere in any direction.</p>
<p>What is your clinical application? Or do you work on preclinical imaging?</p>

---

## Post #3 by @ehdrmfdl3648 (2023-10-16 02:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24ae7d0df748eb0591d03786e68691ac40fb5277.png" data-download-href="/uploads/short-url/5ev1MKvMKN98qQATRHuQCHOR5QP.png?dl=1" title="캡처" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ae7d0df748eb0591d03786e68691ac40fb5277_2_690x368.png" alt="캡처" data-base62-sha1="5ev1MKvMKN98qQATRHuQCHOR5QP" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ae7d0df748eb0591d03786e68691ac40fb5277_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ae7d0df748eb0591d03786e68691ac40fb5277_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ae7d0df748eb0591d03786e68691ac40fb5277_2_1380x736.png 2x" data-dominant-color="69696F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">캡처</span><span class="informations">1905×1016 89.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you very much for your reply.</p>
<p>My situation right now is the same as above.</p>
<p>I have temporarily floated a random image in a random location.</p>
<p>But when I float the next image in a different position, the previous one disappears.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/018c3c78c4dfdc7ca1a0714fa5a7dff0b2034f26.png" alt="asddsads" data-base62-sha1="dGVNiVhYxNLyalUpZxdKcxFA1g" width="658" height="234"></p>
<p>Above is a figure attached to Dr. prevost’s paper “3D Freehand US without External Tracking using DL”.<br>
This is what I ultimately want to achieve. !ㅜ__ㅜ!</p>

---

## Post #4 by @lassoan (2023-10-16 18:16 UTC)

<p>Thank you for the additional information. Your question is answered here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="32240">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/3d-ultrasound-reconstruction-with-openigtl-verasonics-polhemus/32240/2">3D Ultrasound Reconstruction with openIGTL (Verasonics &amp; Polhemus)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I would recommend to use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#view-data">“Show slice in 3D views” button (eye icon)</a> to display the image slice in 3D instead of using volume rendering for a single slice. Volume rendering is much more expensive and more difficult to display an opaque image. 
You can use volume reconstruction module of SlicerIGT extension to “stack” (it is much more complex than that, as images may be oriented arbitrarily) the images into a 3D volume. See step-by-step instructions in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT Tutorial</a> U-34. 
Note that the d…
  </blockquote>
</aside>


---
