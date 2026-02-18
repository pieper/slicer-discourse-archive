# Segmentation of Alveolar cleft

**Topic ID**: 15104
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/segmentation-of-alveolar-cleft/15104

---

## Post #1 by @manjula (2020-12-17 00:57 UTC)

<p>I am trying to find a predictable way to measure the volume of an alveolar bone cleft in cleft lip and palate children with CBCT.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2c873b11059cad415aaab49e2c3ccdde258290a.jpeg" data-download-href="/uploads/short-url/u4FJzxNqnULKjSIg9E57qmAlfoC.jpeg?dl=1" title="image_00001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2c873b11059cad415aaab49e2c3ccdde258290a_2_683x499.jpeg" alt="image_00001" data-base62-sha1="u4FJzxNqnULKjSIg9E57qmAlfoC" width="683" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2c873b11059cad415aaab49e2c3ccdde258290a_2_683x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2c873b11059cad415aaab49e2c3ccdde258290a_2_1024x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2c873b11059cad415aaab49e2c3ccdde258290a.jpeg 2x" data-dominant-color="41352D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_00001</span><span class="informations">1250×914 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f857d8ae1def112c76de0e746a1810badedcfea8.jpeg" data-download-href="/uploads/short-url/zqWCBLYWpKJtCzVbK52EPLfTrpm.jpeg?dl=1" title="image_00002" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f857d8ae1def112c76de0e746a1810badedcfea8_2_683x499.jpeg" alt="image_00002" data-base62-sha1="zqWCBLYWpKJtCzVbK52EPLfTrpm" width="683" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f857d8ae1def112c76de0e746a1810badedcfea8_2_683x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f857d8ae1def112c76de0e746a1810badedcfea8_2_1024x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f857d8ae1def112c76de0e746a1810badedcfea8.jpeg 2x" data-dominant-color="332922"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_00002</span><span class="informations">1250×914 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Several papers describe that they have done it but it is very vague. The main problem is to define the anterior and posterior limits of the alveolar bone.</p>
<p>So far the best result I got was with the fill between slice option. Looking for a better and predictable way of segmenting this area to measure the volume which is not very nice in the anterior margin. (Superior and Inferior is not a problem as it can be defined with landmarks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/187bbc37556551d93dd21d324dc15a42f1d5c937.jpeg" data-download-href="/uploads/short-url/3uAyLCvQ2BM848iQlsNUlQcGiUL.jpeg?dl=1" title="image_00031" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187bbc37556551d93dd21d324dc15a42f1d5c937_2_672x500.jpeg" alt="image_00031" data-base62-sha1="3uAyLCvQ2BM848iQlsNUlQcGiUL" width="672" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187bbc37556551d93dd21d324dc15a42f1d5c937_2_672x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187bbc37556551d93dd21d324dc15a42f1d5c937_2_1008x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/187bbc37556551d93dd21d324dc15a42f1d5c937.jpeg 2x" data-dominant-color="666C84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_00031</span><span class="informations">1248×928 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What would be the best way to do this?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2020-12-17 01:15 UTC)

<p>The images are very helpful but it is still not very clear what the main challenge is. Could you join the segmentation breakout session tomorrow at 2pm EST and bring this as a case to look at?</p>

---

## Post #3 by @Tina_Kapur (2020-12-17 02:50 UTC)

<p>Btw, the Project Week Segmentation breakout session is at 11am EST tomorrow (not 2pm)</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://etsmtl.zoom.us/zoom.ico" class="site-icon" width="16" height="16">
      <a href="https://etsmtl.zoom.us/j/86140790592?pwd=U3ExVk9sV1NHV2dubytnMVp4K0M4Zz09" target="_blank" rel="noopener nofollow ugc">Zoom Video</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://etsmtl.zoom.us/j/86140790592?pwd=U3ExVk9sV1NHV2dubytnMVp4K0M4Zz09" target="_blank" rel="noopener nofollow ugc">Join our Cloud HD Video Meeting</a></h3>

<p>Zoom is the leader in modern enterprise video communications, with an easy, reliable cloud platform for video and audio conferencing, chat, and webinars across mobile, desktop, and room systems. Zoom Rooms is the original software-based conference...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2020-12-17 02:56 UTC)

<p>We agreed on Monday to move the segmentation session to the afternoon because we wanted to have a segmentation storage format discussion and we could not find any other timeslot that worked for everyone. I updated the time in the breakout list, but not in the calendar. This afternoon I fixed this, they are now in sync.</p>

---

## Post #5 by @manjula (2020-12-17 06:19 UTC)

<p>I will try to add better photos.<br>
I can come.today and bring this data for the breakout session. Thanks you</p>

---

## Post #6 by @manjula (2020-12-17 10:09 UTC)

<p>Dear Prof <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Idea is to calculate the volume of the bony cleft in cleft lip and palte children.</p>
<p>The area we want to segment is like a pyramid.</p>
<p>Defining the superior and inferior margins and the lateral and medial margins are no problem.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/408a796b521452d1b3687976792635d511c389a3.png" alt="1" data-base62-sha1="9cXeKxO1T0hsTu3UHMBoviyLtoT" width="411" height="282"></p>
<p>The problem is with the anterior and posterior walls. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/007919c3966940ff15aadeeabb1f2daeb9f14631.png" alt="2" data-base62-sha1="4bskqgSpanhS0e5ofoMwaobGj7" width="411" height="282"></p>
<p>People have tried different methods.</p>
<p>1, Marked the area in each slice and has multiplied that by spacing<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0ceb46a90e59f01b86af934c0f9e775d8ff224e6.png" alt="Screenshot from 2020-12-17 10-25-45" data-base62-sha1="1QhNYYZnHum8uc8lU22Jw9YFVlk" width="246" height="204"></p>
<p>But my idea is to replicate the method described here with the 3D Slicer in a much simpler way</p>
<p><a href="https://www.oooojournal.net/article/S2212-4403(17)30181-5/fulltext" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.oooojournal.net/article/S2212-4403(17)30181-5/fulltext</a></p>

---

## Post #7 by @TomAlexanderSchr (2023-04-06 15:26 UTC)

<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="15104">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>find a predictable way to measure the volume of an alveolar bone cleft in cleft lip and palate children with CBCT.</p>
</blockquote>
</aside>
<p>Hello<br>
Have you found a predictable way to measure the volume of an alveolar bone cleft in cleft lip and palate children with CBCT ?</p>

---

## Post #8 by @lassoan (2023-04-06 22:05 UTC)

<p>You can use the “Markups to model” module (provided by MarkupsToModel extension) to define the pyramid model by dropping a couple of markup points. You can get the volume of the model in Models module / Information section.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="lqABW0_ohi4" data-video-title="Quick volume measurement using boundary points" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=lqABW0_ohi4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/lqABW0_ohi4/maxresdefault.jpg" title="Quick volume measurement using boundary points" width="" height="">
  </a>
</div>

<p>You can improve the accuracy by importing the model into a segmentation and refine the shape in the Segment Editor module.</p>

---

## Post #9 by @TomAlexanderSchr (2023-04-22 13:46 UTC)

<p>Dear Prof <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>This workflow is tremendously helpful.<br>
Thank you a lot!</p>
<p>All the best</p>

---

## Post #10 by @TomAlexanderSchr (2025-03-28 20:21 UTC)

<p>Dear Prof <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I have found a problem that I unfortunately cannot solve myself.<br>
If I markup points in different planes, the inner points (middle plane) are not taken into account in the volume calculation.</p>
<p>See the markup points in the coronar plane below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e2b821b13b76a2aa5a527bfbec1958023ea0309.png" data-download-href="/uploads/short-url/4iTxtYIn9aUGXZ8e9PfAjvuM1MB.png?dl=1" title="{1FD4B7B3-8E66-4814-A4F8-78247DE37703}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e2b821b13b76a2aa5a527bfbec1958023ea0309_2_607x499.png" alt="{1FD4B7B3-8E66-4814-A4F8-78247DE37703}" data-base62-sha1="4iTxtYIn9aUGXZ8e9PfAjvuM1MB" width="607" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e2b821b13b76a2aa5a527bfbec1958023ea0309_2_607x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e2b821b13b76a2aa5a527bfbec1958023ea0309_2_910x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e2b821b13b76a2aa5a527bfbec1958023ea0309.png 2x" data-dominant-color="47474C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{1FD4B7B3-8E66-4814-A4F8-78247DE37703}</span><span class="informations">1001×824 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8837adb4b3af11e78f0e25a5796fd92f3e8960c.png" data-download-href="/uploads/short-url/o2JUnT9BNOXFQtmBJezdo9jr4Kw.png?dl=1" title="{5D36D2F7-F447-49E1-9361-79CCEAF286B0}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8837adb4b3af11e78f0e25a5796fd92f3e8960c_2_588x500.png" alt="{5D36D2F7-F447-49E1-9361-79CCEAF286B0}" data-base62-sha1="o2JUnT9BNOXFQtmBJezdo9jr4Kw" width="588" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8837adb4b3af11e78f0e25a5796fd92f3e8960c_2_588x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8837adb4b3af11e78f0e25a5796fd92f3e8960c_2_882x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8837adb4b3af11e78f0e25a5796fd92f3e8960c.png 2x" data-dominant-color="46464B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{5D36D2F7-F447-49E1-9361-79CCEAF286B0}</span><span class="informations">991×842 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b884fbb8860c850f1fb971abb2b99ca673900e4e.png" data-download-href="/uploads/short-url/qkkLJD9mjJiG0NSSxQdGRFL4RLE.png?dl=1" title="{59DCA9B3-4566-4F8F-90C4-7142107F4BBF}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b884fbb8860c850f1fb971abb2b99ca673900e4e_2_597x499.png" alt="{59DCA9B3-4566-4F8F-90C4-7142107F4BBF}" data-base62-sha1="qkkLJD9mjJiG0NSSxQdGRFL4RLE" width="597" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b884fbb8860c850f1fb971abb2b99ca673900e4e_2_597x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b884fbb8860c850f1fb971abb2b99ca673900e4e_2_895x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b884fbb8860c850f1fb971abb2b99ca673900e4e.png 2x" data-dominant-color="47464C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{59DCA9B3-4566-4F8F-90C4-7142107F4BBF}</span><span class="informations">990×829 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The main problem in the volume calculation is the sandglass-shaped configuration of the alveolar cleft.</p>
<p>Thx in advance</p>

---
