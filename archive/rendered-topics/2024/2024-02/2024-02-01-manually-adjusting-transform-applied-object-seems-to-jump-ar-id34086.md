# Manually Adjusting Transform - Applied Object Seems to Jump Around; Matrixes Not Edited As Expected 

**Topic ID**: 34086
**Date**: 2024-02-01
**URL**: https://discourse.slicer.org/t/manually-adjusting-transform-applied-object-seems-to-jump-around-matrixes-not-edited-as-expected/34086

---

## Post #1 by @tpal_1 (2024-02-01 12:03 UTC)

<p>Operating system: Mac OS Monterey 12.7.1<br>
Slicer version: 5.6.1 (and 5.2.2)</p>
<p>I have had consistent issues when manually adjusting transforms in Slicer 5.2.2 and Slicer 5.6.1. It seems that minor changes result in the transformed image “jumping”, as if the origin has changed. For instance: If I change the LR value to be 1, then 1.2, then back to 0 (doing no other steps in the meantime) I would expect the final result to be nothing or the identity transform. However, it results in a shift of -2.4.</p>
<p>When I adjust the LR value to be 1, the transform matrix acts as expected</p>
<p>[1 0 0 1<br>
0 1 0 0<br>
0 0 1 0<br>
0 0 0 1]</p>
<p>Then, changing the LR value slightly more to be 1.2, suddenly the matrix jumps to be completely different:</p>
<p>[1 0 0 -1.2<br>
0 1 0 0<br>
0 0 1 0<br>
0 0 0 1]</p>
<p>and finally, setting the value back to 0 yields:</p>
<p>[1 0 0 -2.4<br>
0 1 0 0<br>
0 0 1 0<br>
0 0 0 1]</p>
<p>I have noticed the same behavior in other axes/rotations/etc. I’m attaching a few snapshots showing the above example.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55a1cf99f27f4f7ae33be823d7cd222dbf01370f.jpeg" data-download-href="/uploads/short-url/cdxgkfVol02q0tu5JbPN3JRDZi7.jpeg?dl=1" title="Fig1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a1cf99f27f4f7ae33be823d7cd222dbf01370f_2_690x344.jpeg" alt="Fig1" data-base62-sha1="cdxgkfVol02q0tu5JbPN3JRDZi7" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a1cf99f27f4f7ae33be823d7cd222dbf01370f_2_690x344.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a1cf99f27f4f7ae33be823d7cd222dbf01370f_2_1035x516.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a1cf99f27f4f7ae33be823d7cd222dbf01370f_2_1380x688.jpeg 2x" data-dominant-color="C8C8CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig1</span><span class="informations">1910×953 94.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0161073012b0b1d7f96973a0ac0309d37abeb58.jpeg" data-download-href="/uploads/short-url/mQbFoIkbkaFyryNvrK01nfOgdWo.jpeg?dl=1" title="Fig2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0161073012b0b1d7f96973a0ac0309d37abeb58_2_690x339.jpeg" alt="Fig2" data-base62-sha1="mQbFoIkbkaFyryNvrK01nfOgdWo" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0161073012b0b1d7f96973a0ac0309d37abeb58_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0161073012b0b1d7f96973a0ac0309d37abeb58_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0161073012b0b1d7f96973a0ac0309d37abeb58_2_1380x678.jpeg 2x" data-dominant-color="C8C8C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig2</span><span class="informations">1914×943 93.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b074d6056db6e370964801417b94c9184a45c40a.jpeg" data-download-href="/uploads/short-url/pb0lZV5Y4YXdBOHQXiOivVpgUPw.jpeg?dl=1" title="Fig3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b074d6056db6e370964801417b94c9184a45c40a_2_690x340.jpeg" alt="Fig3" data-base62-sha1="pb0lZV5Y4YXdBOHQXiOivVpgUPw" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b074d6056db6e370964801417b94c9184a45c40a_2_690x340.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b074d6056db6e370964801417b94c9184a45c40a_2_1035x510.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b074d6056db6e370964801417b94c9184a45c40a_2_1380x680.jpeg 2x" data-dominant-color="C7C7C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig3</span><span class="informations">1914×944 93.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I understand that this might be related to another question: <a href="https://discourse.slicer.org/t/transformation-questions-reset-plane-angle-when-adjust-another-one-possible-bug/28281" class="inline-onebox">Transformation questions, reset plane angle when adjust another one[possible bug]</a> and the note in transforms about resetting sliders to 0.</p>
<p>However, as-is, this still doesn’t seem to be performing as expected, and it makes it essentially impossible to make any manual adjustments to a transform (for instance, for creating an initialization for a registration or for manually adjusting the position of a model, etc).</p>
<p>Is there anything I should be doing differently? And if not, is there any way to address this?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2024-02-01 16:20 UTC)

<p>As far as I know, the last column is the translation values. So, if you are entering 1.2, it is shifting the image to the R by 1.2 mm. This is equivalent to using the sliders  for translation and in the L/R sliders shifting to 1.2mm. So that’s expected and normal.</p>
<p>It not a typical case you want to edit the transformation matrix manually. What are you trying to do ?</p>

---

## Post #3 by @muratmaga (2024-02-01 16:26 UTC)

<aside class="quote no-group" data-username="tpal_1" data-post="1" data-topic="34086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/94ad74/48.png" class="avatar"> tpal_1:</div>
<blockquote>
<p>If I change the LR value to be 1, then 1.2, then back to 0 (doing no other steps in the meantime) I would expect the final result to be nothing or the identity transform.</p>
</blockquote>
</aside>
<p>That’s exactly observsing in my end:<br>
No displacement<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61cd714afe9ba73d567aac740ce0e52a58c1e1c0.jpeg" data-download-href="/uploads/short-url/dXctlf3C2Jnbf1uUGoKEOjVQHVS.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61cd714afe9ba73d567aac740ce0e52a58c1e1c0_2_378x375.jpeg" alt="image" data-base62-sha1="dXctlf3C2Jnbf1uUGoKEOjVQHVS" width="378" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61cd714afe9ba73d567aac740ce0e52a58c1e1c0_2_378x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61cd714afe9ba73d567aac740ce0e52a58c1e1c0_2_567x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61cd714afe9ba73d567aac740ce0e52a58c1e1c0_2_756x750.jpeg 2x" data-dominant-color="BBBABB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1448×1432 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
2.5 mm L/R shift<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0da3cf55d643ae4ca038e726cec5b1e8830c94be.jpeg" data-download-href="/uploads/short-url/1WFaqCsTNwqw6VT6DHsozyW2LsG.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0da3cf55d643ae4ca038e726cec5b1e8830c94be_2_353x375.jpeg" alt="image" data-base62-sha1="1WFaqCsTNwqw6VT6DHsozyW2LsG" width="353" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0da3cf55d643ae4ca038e726cec5b1e8830c94be_2_353x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0da3cf55d643ae4ca038e726cec5b1e8830c94be_2_529x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0da3cf55d643ae4ca038e726cec5b1e8830c94be_2_706x750.jpeg 2x" data-dominant-color="B6B7B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1506×1598 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Back to where we started:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c464ad0a5836d459a7611a6f144fb38a9898c304.jpeg" data-download-href="/uploads/short-url/s1nhrKxeFMejqvi5L8gUohWneBe.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c464ad0a5836d459a7611a6f144fb38a9898c304_2_409x500.jpeg" alt="image" data-base62-sha1="s1nhrKxeFMejqvi5L8gUohWneBe" width="409" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c464ad0a5836d459a7611a6f144fb38a9898c304_2_409x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c464ad0a5836d459a7611a6f144fb38a9898c304_2_613x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c464ad0a5836d459a7611a6f144fb38a9898c304_2_818x1000.jpeg 2x" data-dominant-color="BABBBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1482×1808 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @tpal_1 (2024-02-01 16:28 UTC)

<p>My issue is that when I enter 1 the shift is to the right (as expected) by 1, but then if I amend it to be 1.2, the result is actually a shift to the LEFT (ie -1.2).</p>
<p>In your example if after the first change to 2.5 you changed it to be 2.7 do you see the same behavior?</p>
<p>We use this functionality fairly regularly, to manually place models in expected places and/or make small-adjustments to registrations.</p>

---

## Post #5 by @muratmaga (2024-02-01 16:37 UTC)

<p>Changes are not cumulative. if you enter 1 and then retype it 1.2, the expected shift is 1.2, not 2.2. Were you expecting to be 2.2?</p>
<p>Because simply altered the origin in X coordinate by 1.2, instead of 1.0.</p>

---

## Post #6 by @tpal_1 (2024-02-01 16:40 UTC)

<p>I would expect the result to be1.2. 2.2 would also make sense to me, but not -1.2, which is what I’m seeing.</p>

---

## Post #7 by @muratmaga (2024-02-01 16:46 UTC)

<p>That’s not what I am seeing, if I enter a positive value, image is shifting to the right (on the screen it is reversed due to the convention. But you can verify on the 3D rendering. I am using the MRHead sample data.</p>
<p>If this is not happening, check the IJK2RAS matrix of your volume, which you can find under volumes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95a034068a52b9891bf22229bc7566dcd910428f.png" data-download-href="/uploads/short-url/llEnmTjMn3ZqLOaCGY2diCrYPnx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95a034068a52b9891bf22229bc7566dcd910428f_2_690x283.png" alt="image" data-base62-sha1="llEnmTjMn3ZqLOaCGY2diCrYPnx" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95a034068a52b9891bf22229bc7566dcd910428f_2_690x283.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95a034068a52b9891bf22229bc7566dcd910428f_2_1035x424.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95a034068a52b9891bf22229bc7566dcd910428f.png 2x" data-dominant-color="E0E0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1254×516 27.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @tpal_1 (2024-02-01 16:55 UTC)

<p>I have the same issue even with the sample MRHead data.</p>
<p>A single adjustment results in the expected shift (in this example, a shift to the right of 10mm). Subsequently editing the 10.0 value to be 10.5 results in a shift to the left of 10.5mm.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7cbb5e0cc2ab238a39a1fd8688aa2709cb2a965.jpeg" data-download-href="/uploads/short-url/uN16qZMesxB1SEzfEyfW7zYbBFr.jpeg?dl=1" title="Screen Shot 2024-02-01 at 10.52.59 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7cbb5e0cc2ab238a39a1fd8688aa2709cb2a965_2_538x500.jpeg" alt="Screen Shot 2024-02-01 at 10.52.59 AM" data-base62-sha1="uN16qZMesxB1SEzfEyfW7zYbBFr" width="538" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7cbb5e0cc2ab238a39a1fd8688aa2709cb2a965_2_538x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7cbb5e0cc2ab238a39a1fd8688aa2709cb2a965_2_807x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7cbb5e0cc2ab238a39a1fd8688aa2709cb2a965.jpeg 2x" data-dominant-color="BAB9B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2024-02-01 at 10.52.59 AM</span><span class="informations">1014×942 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02eaa6056957b7f50efe3cd83b32f590600709c1.jpeg" data-download-href="/uploads/short-url/pNGB7AnDyauWqOQIyHSgUULRol.jpeg?dl=1" title="Screen Shot 2024-02-01 at 10.53.08 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02eaa6056957b7f50efe3cd83b32f590600709c1_2_538x500.jpeg" alt="Screen Shot 2024-02-01 at 10.53.08 AM" data-base62-sha1="pNGB7AnDyauWqOQIyHSgUULRol" width="538" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02eaa6056957b7f50efe3cd83b32f590600709c1_2_538x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02eaa6056957b7f50efe3cd83b32f590600709c1_2_807x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02eaa6056957b7f50efe3cd83b32f590600709c1.jpeg 2x" data-dominant-color="B8B7B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2024-02-01 at 10.53.08 AM</span><span class="informations">1023×949 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The IJK2RAS matrix looks as expected to me.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e05e9c8b186f72418ef6078e08bce791e6cd90cf.png" alt="Screen Shot 2024-02-01 at 10.50.58 AM" data-base62-sha1="w0RELJtKi8BjnPNh8Mq6XWT38o7" width="555" height="458"></p>

---

## Post #9 by @pieper (2024-02-01 17:09 UTC)

<p>I cannot replicate what you are describing <a class="mention" href="/u/tpal_1">@tpal_1</a></p>
<p>I do the following:</p>
<ul>
<li>Start a fresh Slicer</li>
<li>Load MRHead from SampleData</li>
<li>Add a linear transform and apply it to the MRHead</li>
<li>Type 10 into the upper right element of the linear transform → Head moves 1cm</li>
<li>Type 10.5 into the element → head moves another .5 mm</li>
</ul>
<p>No negative element is introduced.</p>

---

## Post #10 by @tpal_1 (2024-02-01 17:15 UTC)

<p>Thanks for looking <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>I consistently have this happen, even following your steps.<br>
Additionally, it makes no difference whether I hit enter after entering the 10.0 or whether I stay in the box and just continue editing.</p>

---

## Post #11 by @tpal_1 (2024-02-01 20:15 UTC)

<p>I have noticed that this issue only happens when entering decimal amounts (ie changing from 10.0 to 10.5) but not changing the whole value.</p>
<p>It seems to be resolved when instead of inserting a 5 after the decimal point, I instead replace the ‘0’ following the decimal point.</p>
<p>So changing the value from ‘10.0000’ to ‘10.50000’ causes the negative introduction I’m seeing, but changing the value from ‘10.0000’ to ‘10.5000’ does not.</p>
<p>Is there possibly some part of the code that requires a certain number of decimal places causing this issue?</p>

---

## Post #12 by @muratmaga (2024-02-01 22:36 UTC)

<p>So your issue is as you enter the decimal point, a negative sign is automatically inserted? Does it happen in other fields as well? Does this happen in any other module? E.g., if you enter the value into translation field (as opposed to the matrix), do see a sign change as well?</p>
<p>I can’t seem to replicate this on mac with 5.6.1. I increased the precision to 5 decimal place to see if that has an effect, it doesn’t seem to do anything.</p>
<p>Do you have any customizations done to via the slicerrc.py or some other means?</p>

---

## Post #13 by @tpal_1 (2024-02-02 16:00 UTC)

<p>I’m only editing the translation/rotation fields (the values next to the sliders), not the matrix itself. But this happens in any translation and any rotation.</p>
<p>I don’t believe I have any customizations, and I re-downloaded 5.6.1 directly from the website before doing these latest tests.</p>
<p>I think it’s easiest to demonstrate my problem by a screen recording, which I’m including a link to here: <a href="https://youtu.be/hgrFwzy9wVA" rel="noopener nofollow ugc">https://youtu.be/hgrFwzy9wVA</a></p>

---

## Post #14 by @muratmaga (2024-02-02 16:25 UTC)

<p>really bizarre, Can’t replicate on my end.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> ?</p>

---

## Post #15 by @pieper (2024-02-02 17:09 UTC)

<p>No, I can’t replicate that either. There must be something we’re not seeing…?</p>

---

## Post #16 by @tpal_1 (2024-02-02 18:56 UTC)

<p>This does only happen for me in local reference frame.</p>
<p>Additionally, I know colleagues of mine have the same issue, but admittedly we might be working with similar setups, although again I don’t think any of us has changed anything behind the scenes.</p>

---

## Post #17 by @pieper (2024-02-03 10:51 UTC)

<p>Can you replicate this using the MRHead SampleData?  Maybe you can share a file for which this happens, or at least show the Volume Information from the volumes module.   Maybe local mode is the issue.  Typing directly in the upper right element of the mattrix should do a global LR translation.</p>

---

## Post #18 by @tpal_1 (2024-02-05 15:44 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a></p>
<p>This happens regardless of the volume I use.</p>
<p>I have done this on the MRHead data, as in the above screenshots and recording <a href="https://www.youtube.com/watch?v=hgrFwzy9wVA" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=hgrFwzy9wVA</a></p>
<p>Again, this issue doesn’t occur when I edit the matrix itself, but rather the fields next to the sliders for LR, AP, IS and rotations.</p>

---

## Post #19 by @pieper (2024-02-05 15:58 UTC)

<p>Okay, thanks, yes, I can replicate this now.  It seems there’s some interaction between using the local mode and the code that manages the number of decimals being displayed.</p>
<p>I can replicate with these steps:</p>
<ul>
<li>Load MRHead, create and apply linear transform to it</li>
<li>Switch to local transformation mode</li>
<li>Click left of the decimal point in the LR translation slicer text box and type 1<br>
=&gt; head moves to patient right, upper right element of matrix is 1</li>
<li>Use arrow to move to the right of the decimal point and type 5<br>
=&gt; head moves to patient left, upper right element is -1.5</li>
<li>Type more 5s into and the matrix element gets more and more negative</li>
</ul>
<p>Until this can be investigated and resolved I would avoid the slider and edit the matrix directly.  Is there a reason that doesn’t work in your use case&gt;</p>

---

## Post #20 by @tpal_1 (2024-02-05 16:06 UTC)

<p>Thank you! Yes, we can work around this for now, but it will be great to have it resolved!</p>
<p>Is there some way that I should flag this as a bug officially?</p>

---

## Post #21 by @muratmaga (2024-02-05 16:34 UTC)

<p>you can submit a bug report at <a href="https://github.com/Slicer/Slicer" class="inline-onebox">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a> under the issues tab.</p>

---

## Post #22 by @tpal_1 (2024-02-05 17:18 UTC)

<p>Thanks. Issue submitted here: <a href="https://github.com/Slicer/Slicer/issues/7574" class="inline-onebox" rel="noopener nofollow ugc">Editing Decimal Values in Transform Fields Causes Introduction of Negative · Issue #7574 · Slicer/Slicer · GitHub</a></p>

---
