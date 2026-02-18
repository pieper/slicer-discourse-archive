# Wrap Solidify: How can I choose "split cavities"?

**Topic ID**: 26231
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/wrap-solidify-how-can-i-choose-split-cavities/26231

---

## Post #1 by @Alessia_Giorgi (2022-11-14 14:27 UTC)

<p>Hi everyone,</p>
<p>I’m a biomedical engineer and I’m following a project on craniostenosis.<br>
I’d like to share with you a doubt. I hope someone can help me.</p>
<p>In order to evaluate the intracranial volume, I’m using Wrap Solidify, in particular “Largest cavity” function, but I can’t understand the meaning of “Split Cavities”. How can I choose its parameter?</p>
<p>Thank you.</p>
<p>Alessia</p>

---

## Post #2 by @lassoan (2022-11-14 15:39 UTC)

<p>Enable split cavities if you want to remove smaller cavities that are connected to the largest cavity with a narrow neck. For example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6b6d406d8382df7d7fb3b1681cd62e7a10501fe.png" data-download-href="/uploads/short-url/nMOY06AwiM7CxB1g3XzyXJkr8dM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6b6d406d8382df7d7fb3b1681cd62e7a10501fe_2_689x183.png" alt="image" data-base62-sha1="nMOY06AwiM7CxB1g3XzyXJkr8dM" width="689" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6b6d406d8382df7d7fb3b1681cd62e7a10501fe_2_689x183.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6b6d406d8382df7d7fb3b1681cd62e7a10501fe_2_1033x274.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6b6d406d8382df7d7fb3b1681cd62e7a10501fe_2_1378x366.png 2x" data-dominant-color="5E5A4F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">5330×1415 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Largest cavity is the connected A-B-C cavity. Region B is connected to A with a narrowing of about 10mm. Region C is connected to A with a narrowing of about 7mm.</p>

---

## Post #3 by @Alessia_Giorgi (2022-11-14 16:00 UTC)

<p>Thank you very much, now it’s clear!</p>
<p>If it’s possibile, I’d like to know how the algorithm of extraction works.<br>
What does It do at each iterations?</p>
<p>Thank you again!</p>

---

## Post #4 by @lassoan (2022-11-14 18:09 UTC)

<p>See some information here: <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify</a></p>
<p>I’ve also added some more clarifications - not merged yet but available here: <a href="https://github.com/lassoan/Slicer-SurfaceWrapSolidify#how-it-works">https://github.com/lassoan/Slicer-SurfaceWrapSolidify#how-it-works</a></p>

---

## Post #5 by @Alessia_Giorgi (2022-11-15 09:14 UTC)

<p>Thank you!</p>
<p>I can’t understand this part:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4326e0f0bb05b96491c56cef987d76a478c74864.png" data-download-href="/uploads/short-url/9A3hPTnZZ2BstQ5kjCa86nZ9uYY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4326e0f0bb05b96491c56cef987d76a478c74864_2_690x47.png" alt="image" data-base62-sha1="9A3hPTnZZ2BstQ5kjCa86nZ9uYY" width="690" height="47" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4326e0f0bb05b96491c56cef987d76a478c74864_2_690x47.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4326e0f0bb05b96491c56cef987d76a478c74864_2_1035x70.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4326e0f0bb05b96491c56cef987d76a478c74864.png 2x" data-dominant-color="F0F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1071×74 10.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
is it inverted in what?<br>
why is it shrunk by the value specified in <em>split cavities</em>?</p>

---

## Post #6 by @lassoan (2022-11-15 17:08 UTC)

<aside class="quote no-group" data-username="Alessia_Giorgi" data-post="5" data-topic="26231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alessia_giorgi/48/13980_2.png" class="avatar"> Alessia_Giorgi:</div>
<blockquote>
<p>is it inverted in what?</p>
</blockquote>
</aside>
<p>The segmentation is inverted: filled parts become unfilled, unfilled parts become filled.</p>
<aside class="quote no-group" data-username="Alessia_Giorgi" data-post="5" data-topic="26231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alessia_giorgi/48/13980_2.png" class="avatar"> Alessia_Giorgi:</div>
<blockquote>
<p>why is it shrunk by the value specified in <em>split cavities</em>?</p>
</blockquote>
</aside>
<p>To make small connecting bridges between cavities disappear.</p>
<p>If you want to understand the algorithm then you can enable “Save intermediate results” and inspect all the outputs generated during the processing.</p>

---

## Post #7 by @Alessia_Giorgi (2022-11-16 08:57 UTC)

<p>Thank you for your help!</p>
<p>Do you estimate the accuracy of the method in extracting largest cavity?</p>

---

## Post #8 by @Alessia_Giorgi (2022-11-16 09:45 UTC)

<p>I’m sorry, but I can’t understand passages from this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25e1516de2842605f41bb448469a717c24e4bd34.jpeg" data-download-href="/uploads/short-url/5p6pj130YuwbhMDz1q3cTMagKUc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25e1516de2842605f41bb448469a717c24e4bd34_2_690x271.jpeg" alt="image" data-base62-sha1="5p6pj130YuwbhMDz1q3cTMagKUc" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25e1516de2842605f41bb448469a717c24e4bd34_2_690x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25e1516de2842605f41bb448469a717c24e4bd34_2_1035x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25e1516de2842605f41bb448469a717c24e4bd34_2_1380x542.jpeg 2x" data-dominant-color="6D6C6C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×756 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
to this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09aa1110ca22be8ea5a9512274f9ef2fe1187176.jpeg" data-download-href="/uploads/short-url/1nuF81wq96a3vRnXV16NmKy4Lae.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09aa1110ca22be8ea5a9512274f9ef2fe1187176_2_690x286.jpeg" alt="image" data-base62-sha1="1nuF81wq96a3vRnXV16NmKy4Lae" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09aa1110ca22be8ea5a9512274f9ef2fe1187176_2_690x286.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09aa1110ca22be8ea5a9512274f9ef2fe1187176_2_1035x429.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09aa1110ca22be8ea5a9512274f9ef2fe1187176_2_1380x572.jpeg 2x" data-dominant-color="6D6D67"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×797 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What did the algorithm do?</p>

---

## Post #9 by @lassoan (2022-11-21 20:38 UTC)

<p>It grew the segment by the specified margin.</p>

---
