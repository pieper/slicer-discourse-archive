# Viewing a volume with two different volume rendering properties at same time

**Topic ID**: 16411
**Date**: 2021-03-07
**URL**: https://discourse.slicer.org/t/viewing-a-volume-with-two-different-volume-rendering-properties-at-same-time/16411

---

## Post #1 by @mohammed_alshakhas (2021-03-07 12:49 UTC)

<p>i was wonderin if it is possible to view two volume properties at once .</p>
<p>in my workflow, i can greatly benefit from making a soft tissue outline rendering while i can view a hard tissue rendering at the same time .</p>
<p>i already did that with segmentation and altering opacity , but in many cases, the volume rendering can be superior way to visaulaization  and a shorter way to do so , of course, that highly depends on the quality of  the images</p>

---

## Post #2 by @muratmaga (2021-03-07 17:58 UTC)

<p>You can clone your volume and use the second volume property on that. You need to use gpu multi volume ray casting, which is experimental. For some cases regular gpu rendering may also work, but depending on angles you might have artifacts. This is a use case we are interested in seeing more support. Let us know how it goes.</p>

---

## Post #3 by @mohammed_alshakhas (2021-03-08 04:16 UTC)

<p>I’ll try that . Thank you for the suggestion</p>
<p>Just to mention that I’m used to this way of rendering in Planmeca cbct viewer .<br>
It has a soft tissue and hard tissue rendering control .  I doubt it uses two volume since it is fast and seamless .</p>

---

## Post #4 by @lassoan (2021-03-08 05:43 UTC)

<p>Please attach a few screenshots and we can then tell what volume rendering settings to use to achieve a similar look.</p>

---

## Post #5 by @mohammed_alshakhas (2021-03-08 10:18 UTC)

<p>this is done in planmeca viewer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7ba73650c7afe98860dbe918a3815023958e8ee.jpeg" data-download-href="/uploads/short-url/qdkQs2yJyetnoglR35Jj2ielivI.jpeg?dl=1" title="Screen Shot 2021-03-08 at 12.30.30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7ba73650c7afe98860dbe918a3815023958e8ee_2_690x388.jpeg" alt="Screen Shot 2021-03-08 at 12.30.30" data-base62-sha1="qdkQs2yJyetnoglR35Jj2ielivI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7ba73650c7afe98860dbe918a3815023958e8ee_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7ba73650c7afe98860dbe918a3815023958e8ee_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7ba73650c7afe98860dbe918a3815023958e8ee_2_1380x776.jpeg 2x" data-dominant-color="333533"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-08 at 12.30.30</span><span class="informations">1920×1080 354 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>this is done in slicer with multi volum</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/daabd6484e4a591b7437f77f052b955f7e0506d1.jpeg" data-download-href="/uploads/short-url/vcsfmeA5R4qpUxpJBHlqyDkyVJT.jpeg?dl=1" title="Screen Shot 2021-03-08 at 13.12.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/daabd6484e4a591b7437f77f052b955f7e0506d1_2_690x388.jpeg" alt="Screen Shot 2021-03-08 at 13.12.20" data-base62-sha1="vcsfmeA5R4qpUxpJBHlqyDkyVJT" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/daabd6484e4a591b7437f77f052b955f7e0506d1_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/daabd6484e4a591b7437f77f052b955f7e0506d1_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/daabd6484e4a591b7437f77f052b955f7e0506d1_2_1380x776.jpeg 2x" data-dominant-color="BAB8B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-08 at 13.12.20</span><span class="informations">1920×1080 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>however the one with slicer is hard to get very well defined soft tissues outline which is the most important thing for the soft tissue rendering in this use</p>

---

## Post #6 by @pieper (2021-03-08 13:40 UTC)

<p>We had a prototype for a mode something like that.  It worked with Slicer volume rendering but we never fully integrated it in the UI.  The whole Slicer Volume Rendering module could use a rework when someone has the time.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="4Q9NfNmN-9w" data-video-title="TransferFunctionEditor" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=4Q9NfNmN-9w" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/4Q9NfNmN-9w/maxresdefault.jpg" title="TransferFunctionEditor" width="" height="">
  </a>
</div>


---

## Post #7 by @mohammed_alshakhas (2021-03-08 13:45 UTC)

<p>that looks awesome , hopefully we see this in slicer soon</p>

---

## Post #8 by @lassoan (2021-03-08 14:46 UTC)

<p>In the Planmeca screenshot the skin surface is displayed using transparent surface-like rendering. There are several options for achieving this in Slicer.</p>
<p>There are two interesting things to note on the Planmeca screenshot:</p>
<ol>
<li>The skin surface and bones come from two completely different images. You can see this very clearly at the tip of the chin. Do you intentionally visualize skin surface from one image and bones from another?</li>
<li>Skin, soft-tissues, and low-density bone are all aggressively suppressed, so it seems that Planmeca uses the technique shown in <a class="mention" href="/u/pieper">@pieper</a>’s demo above (have a 0-opacity gap in the scalar opacity mapping to suppress soft tissues, while showing skin surface and bone)</li>
</ol>
<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="7" data-topic="16411" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>that looks awesome , hopefully we see this in slicer soon</p>
</blockquote>
</aside>
<p>Just to clarify, this rendering is already available in Slicer (what the demo shows is just a different way of editing transfer functions, so that you can move selected control points together, independently from the others). For example, reproducing the same two-peak scalar opacity transfer function using the current volume rendering module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a141f38d3b102ea7e0649fbbcb460272984ba2ee.jpeg" data-download-href="/uploads/short-url/n0yaIF27PyviZxnqJTJMYzVYDFk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a141f38d3b102ea7e0649fbbcb460272984ba2ee_2_690x366.jpeg" alt="image" data-base62-sha1="n0yaIF27PyviZxnqJTJMYzVYDFk" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a141f38d3b102ea7e0649fbbcb460272984ba2ee_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a141f38d3b102ea7e0649fbbcb460272984ba2ee_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a141f38d3b102ea7e0649fbbcb460272984ba2ee_2_1380x732.jpeg 2x" data-dominant-color="8E9589"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1199 536 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can increase ambient lighting to make the edges of the skin surface better visible:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5d76157a6383021a7991b66ba027835b5899fa2.jpeg" data-download-href="/uploads/short-url/uvJ9noZT9ig6NAQrWrGWfXjvAXM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5d76157a6383021a7991b66ba027835b5899fa2_2_690x383.jpeg" alt="image" data-base62-sha1="uvJ9noZT9ig6NAQrWrGWfXjvAXM" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5d76157a6383021a7991b66ba027835b5899fa2_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5d76157a6383021a7991b66ba027835b5899fa2_2_1035x574.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5d76157a6383021a7991b66ba027835b5899fa2_2_1380x766.jpeg 2x" data-dominant-color="94A09C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2134×1187 498 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In addition to suppressing soft tissues using scalar opacity mapping, you can also suppress soft tissues using gradient opacity mapping (since there are no sudden intensity changes in soft tissues):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c568b2c3c2e71bd3b36c1c50a647503489b0ad63.jpeg" data-download-href="/uploads/short-url/samnmegcdaPEcGMhwAIMeUiZ2zF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c568b2c3c2e71bd3b36c1c50a647503489b0ad63_2_690x349.jpeg" alt="image" data-base62-sha1="samnmegcdaPEcGMhwAIMeUiZ2zF" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c568b2c3c2e71bd3b36c1c50a647503489b0ad63_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c568b2c3c2e71bd3b36c1c50a647503489b0ad63_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c568b2c3c2e71bd3b36c1c50a647503489b0ad63_2_1380x698.jpeg 2x" data-dominant-color="949C8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1143 517 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, it seems that you can achieve skin surface + bone rendering with a single volume renderer. However, Slicer also offers many other options for suppressing soft tissues and displaying skin surface differently from bone (mask out soft tissue and use single-volume rendering; separate skin surface and bone using volume masking and render the two volumes independently using multi-volume rendering; or segment skin surface using thresholding, fill holes using Wrap Solidify effect, and render as a transparent model).</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47e93b114eb7b1dbb4bad23f2e09e8bc439f1e7e.mp4">
  </div><p></p>

---

## Post #9 by @mohammed_alshakhas (2021-03-08 16:15 UTC)

<p>thank you for extensive replay , really appreciated .</p>
<p>the soft tissue in planmecca is just a chin rest making the soft tissue seeming funny . otherwise its the same patient .</p>
<p>i already tried the skin segmentation/bone render solution nicely in many cases  ,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23948e6fe5b3c49aaa69ca69d779e2cc5a5eac5c.jpeg" data-download-href="/uploads/short-url/54KZvwZKN4RomFvmEBEI91h9hKc.jpeg?dl=1" title="Screen Shot 2021-03-08 at 19.08.33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23948e6fe5b3c49aaa69ca69d779e2cc5a5eac5c_2_690x431.jpeg" alt="Screen Shot 2021-03-08 at 19.08.33" data-base62-sha1="54KZvwZKN4RomFvmEBEI91h9hKc" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23948e6fe5b3c49aaa69ca69d779e2cc5a5eac5c_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23948e6fe5b3c49aaa69ca69d779e2cc5a5eac5c_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23948e6fe5b3c49aaa69ca69d779e2cc5a5eac5c_2_1380x862.jpeg 2x" data-dominant-color="615D6F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-08 at 19.08.33</span><span class="informations">2880×1800 576 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>i wanted to experiment with rendering different component since it gives some sort off texture that i don’t know if possible with segmentation</p>
<p>two question comes to me now<br>
1 is that a preset available in slicer the one you used here for the cbct rendering  ?<br>
2 what’s  difference between gradient  opacity and scalar map opacity ?</p>
<p>thanks</p>

---

## Post #10 by @lassoan (2021-03-08 16:31 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="9" data-topic="16411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>is that a preset available in slicer the one you used here for the cbct rendering ?</p>
</blockquote>
</aside>
<p>It is not a built-in preset, but you can choose a similar built-in preset, modify it by drag-and-dropping control points in the transfer functions, and then add it to the preset list. See:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/i-want-to-boot-up-with-my-very-own-color-map-and-a-black-background/16383/" class="inline-onebox">I want to boot up with my very own color map and a black background</a></li>
<li><a href="https://discourse.slicer.org/t/create-volume-rendering-presets/16339" class="inline-onebox">Create volume rendering presets</a></li>
</ul>
<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="9" data-topic="16411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>what’s difference between gradient opacity and scalar map opacity ?</p>
</blockquote>
</aside>
<p>Scalar opacity mapping allows you to assign opacity to a voxel based on its intensity value. It can be used to suppress visibility (set opacity to 0) of soft tissues, without impacting visibility of bone.</p>
<p>Gradient opacity mapping allows you to assign opacity to a voxel based on the rate of intensity change at that position. This can be used to enhance regions where there is a sudden intensity change, such as skin surface (air/soft tissue intensity are very different) and bone surface (bone/soft tissue intensity are very different).</p>
<p>Probably you can achieve the best results by tuning all transfer functions.</p>
<p>Once you figure out what general shape of transfer function works, you would usually create a simple module that allows the user to generate that transform function using 3-4 sliders:</p>
<ul>
<li>size and position of gap between the two scalar opacity mapping function peaks</li>
<li>height of the “skin” peak</li>
<li>threshold in gradient opacity mapping function below that the opacity is set to 0</li>
</ul>

---
