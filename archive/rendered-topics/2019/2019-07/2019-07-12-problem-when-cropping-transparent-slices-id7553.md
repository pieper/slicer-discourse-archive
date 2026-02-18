# Problem when cropping! >> Transparent slices

**Topic ID**: 7553
**Date**: 2019-07-12
**URL**: https://discourse.slicer.org/t/problem-when-cropping-transparent-slices/7553

---

## Post #1 by @NoobForSlicer (2019-07-12 16:19 UTC)

<p>So i have loaded a bunch of .pngs as a sequence into slicer…</p>
<p>When I dragged the first png onto the slicer window&gt;&gt; it offered me a pop up window where I chose&gt;&gt; show options&gt;&gt;&gt; then unchecked the little box that says single file&gt;&gt; Then I chose fullrainbow next to it (maybe I should choose only rainbow and not the fullrainbow?!).</p>
<p>Either way once I click okay, the pngs load as a sequence and I can see them. I transform them a little bit, I flip the vertical axis (it is sadly upside down) and then I proceed to crop it.</p>
<p>The problem? When I crop a part of the volume&gt;&gt; the pngs seem to overaly each other and become transparent to a certain degree. So one always sees 2 pngs both somewhat transparent.</p>
<p>The hell?!<br>
I use crop volume to crop it.</p>
<p>Then I close everything open the slicer again and load the sequence and this time before cropping it, I move the bar in the red perspective (coronary) all the way to the lowest slice and then move the bar a little bit right and then&gt;&gt;&gt; they suddenly appear transparent again!!  :S CATASTORPHY!</p>
<p>WHy would they not look transparent but then when I pull the bar and go to the lowest slice and then move back they become &gt;&gt; transparent. What the hell?</p>
<p>Then I tried to not do that and just don’t scroll to the lowest slice, instead I make sure that they are not transparent and then&gt;&gt; crop the volume.</p>
<p>Problem&gt;&gt;&gt; on the cropped volume they still look transparent.</p>
<p>No matter what I do with the cropped volume, they remain cropped. I tried translation, move it it half a slice up, half a slice down, I tried scrolling it back to the beginning and scrolling it to the end. Nothing works… they remain cropped and transparent. What the hell?!</p>
<p>Hmm…</p>
<p>I must submit my project soon so this is very very scary now I might nor be able to solve it.</p>

---

## Post #2 by @lassoan (2019-07-12 16:24 UTC)

<p>Could you add a few screenshots so that we can better understand what’s happening?</p>
<p>Can you give a bit higher-level view of what you are trying to achieve?</p>

---

## Post #3 by @NoobForSlicer (2019-07-12 16:25 UTC)

<p>good idea! God bless you Andras, I’ve seen you help so many people on this forum</p>

---

## Post #4 by @NoobForSlicer (2019-07-12 16:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6fc1459a77b5674a821366f202929e3a9242fd9.jpeg" data-download-href="/uploads/short-url/q6KYBirj2pRT3TbluY09GktjoEh.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6fc1459a77b5674a821366f202929e3a9242fd9_2_690x433.jpeg" alt="Screenshot_1" data-base62-sha1="q6KYBirj2pRT3TbluY09GktjoEh" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6fc1459a77b5674a821366f202929e3a9242fd9_2_690x433.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6fc1459a77b5674a821366f202929e3a9242fd9_2_1035x649.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6fc1459a77b5674a821366f202929e3a9242fd9.jpeg 2x" data-dominant-color="47473E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1053×662 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98d5e97474bc11bf6c62bb91d72a7e5e0dc17124.jpeg" data-download-href="/uploads/short-url/lO2SxBSZL5Yy5rYMVKUHgp2Nlk0.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98d5e97474bc11bf6c62bb91d72a7e5e0dc17124_2_690x474.jpeg" alt="Screenshot_2" data-base62-sha1="lO2SxBSZL5Yy5rYMVKUHgp2Nlk0" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98d5e97474bc11bf6c62bb91d72a7e5e0dc17124_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98d5e97474bc11bf6c62bb91d72a7e5e0dc17124_2_1035x711.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98d5e97474bc11bf6c62bb91d72a7e5e0dc17124.jpeg 2x" data-dominant-color="585750"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1036×712 48.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here I have took a screenshot… If I delete number  5 up there it clears up and I see only one image.</p>

---

## Post #5 by @lassoan (2019-07-12 17:03 UTC)

<p>What you see is the effect of interpolation between adjacent slices (when you move the slice slider to a position between two slices then there is a gradual fading between them). You can disable interpolation by unchecking “Interpolate” in Volumes module.</p>

---

## Post #6 by @NoobForSlicer (2019-07-12 17:30 UTC)

<p>Indeed, unchecking interpolation makes images non-transparent and everything is beautiful.</p>
<p>However&gt;&gt;&gt; cropping the volume still produced transparent volumes and no matter what i do with the cropped volume, I get them transparent (they remain transparent for the cropped volume, even after I turn off the interpolation.</p>
<p>Hmm</p>
<p>btw thank you so much for replying, I am puzzled how much you are helpful and help people out! Amazing</p>

---

## Post #7 by @NoobForSlicer (2019-07-12 17:45 UTC)

<p>Ohhh I just realized in cropping menu it says “interpolated cropping”… that one unchecked, crops the image perfectly without fusing them or making them transparent…</p>
<p>I wonder what is this feature interpolation is used at all</p>

---

## Post #8 by @lassoan (2019-07-12 18:15 UTC)

<p>Normally, slices are spatially related, so when you are in between two slices then you want to see the a weighted average of the two closest slices. Most probably your image is not a real 3D volume (2D slices are misaligned, there are burnt-in 2D annotations, etc.) and that’s why interpolation is not desirable for visualization.</p>

---

## Post #9 by @NoobForSlicer (2019-07-12 18:35 UTC)

<p>Thank you so much Lasso &lt;3 You are life savior!</p>
<p>I will ask one more question in the forum <strong>I hope I am not annoying with the questions</strong>. It is not related to this issue so I will post it as a new thread.</p>
<p>Thank you soo so much!<br>
Learning about slicer over and over and I’ve seen your answers in so many questions and wonderful explanations Lasso!</p>

---
