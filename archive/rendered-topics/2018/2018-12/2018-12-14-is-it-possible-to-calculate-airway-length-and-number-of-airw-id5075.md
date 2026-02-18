# Is it possible to calculate airway length and number of airway tree generation with the help of slicer

**Topic ID**: 5075
**Date**: 2018-12-14
**URL**: https://discourse.slicer.org/t/is-it-possible-to-calculate-airway-length-and-number-of-airway-tree-generation-with-the-help-of-slicer/5075

---

## Post #1 by @anitakh1 (2018-12-14 07:12 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2018-12-14 13:00 UTC)

<p>Have a look at <a href="https://chestimagingplatform.org/" rel="nofollow noopener">https://chestimagingplatform.org/</a></p>

---

## Post #3 by @anitakh1 (2019-01-18 09:39 UTC)

<p>thanks for reply. But can you pl tell me how to use and find airway length, no. of branches and centerline of segmented 3D airways.</p>

---

## Post #4 by @anitakh1 (2019-01-18 11:14 UTC)

<p>hello sir,<br>
i downloaded the 3D slicer version 4.8.1 which has CIP and airway inspector. is it same as COPD module? moreover i was following tutorial video given in <a href="http://airwayinspector.acil-bwh.org/multani" rel="nofollow noopener">http://airwayinspector.acil-bwh.org/multani</a>  for airway inspector but after selecting airways using ‘a’, i can’t find save as option in file and can i use ‘analyze tool’ to see whole airway which i detected, pl guide.<br>
thanks you</p>

---

## Post #5 by @pieper (2019-01-18 15:17 UTC)

<p><a class="mention" href="/u/raul">@raul</a> may be able to provide more guidance here.  The slides you linked to describe an older version of Slicer (version 2 from many years ago) but the provided virtual machine images might still work.</p>

---

## Post #6 by @anitakh1 (2019-01-30 12:33 UTC)

<p>sir, how to locate centreline of airways in lung CT volume, pl guide. thanks</p>

---

## Post #7 by @anitakh1 (2019-02-07 09:14 UTC)

<p>pl tell me sir how to find airway length, no. of branches and centreline using slicer. is there any tutorial for this?</p>

---

## Post #8 by @anitakh1 (2019-02-27 08:19 UTC)

<p>sir, can u help me by telling me how to add to segmented results to compare showing different colors like the one in picture attached. i tried adding two volumes module but it shows just one color result.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/024a6c24b180b44257a096f64005dd74f9a6df34.png" alt="image" data-base62-sha1="kgp41pd2CInEdhcj7G3zwi7xY0" width="215" height="259"></p>

---

## Post #9 by @cpinter (2019-02-27 13:58 UTC)

<p>Are these “volumes” segmentations? You can check by hovering it in the Data module, it will tell you in the tooltip.<br>
(Or if you used Segment Editor, then we know it’s a segmentation, and in that case use the Logical operators effect)</p>

---

## Post #10 by @anitakh1 (2019-02-28 05:19 UTC)

<p>hello sir,<br>
i have two segmented results of airways which i did using some algorithms, one preliminary and one advance and i want to compare them like the way shown in picture enclosed to show the difference. kindly help</p>

---

## Post #11 by @anitakh1 (2019-02-28 05:19 UTC)

<p>yes these are volume segmented results</p>

---

## Post #12 by @jakesantiago (2019-02-28 14:10 UTC)

<p>Hi, I am also stuck with the similar issue. How do I add two segmented results?</p>
<p>Even Anita has slightly different results… mine got sliced far more differently.</p>

---

## Post #13 by @cpinter (2019-02-28 14:54 UTC)

<p>I need to know the answer to this question to give a proper answer.</p>
<aside class="quote no-group" data-username="cpinter" data-post="9" data-topic="5075">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Are these “volumes” segmentations? You can check by hovering it in the Data module, it will tell you in the tooltip.</p>
</blockquote>
</aside>
<p>Please let me know what the tooltip says or send a screenshot from what the Data module shows</p>

---

## Post #14 by @anitakh1 (2019-03-05 06:37 UTC)

<p>yes sir, these are 3D segmented outputs. i don’t know what tooltip means but attaching a screen shot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/011786bc933e13d257c0f3eb832c762f35570043.png" data-download-href="/uploads/short-url/9ESHOVT8SjFwN77gDqszpuszWb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/011786bc933e13d257c0f3eb832c762f35570043_2_690x388.png" alt="image" data-base62-sha1="9ESHOVT8SjFwN77gDqszpuszWb" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/011786bc933e13d257c0f3eb832c762f35570043_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/011786bc933e13d257c0f3eb832c762f35570043_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/011786bc933e13d257c0f3eb832c762f35570043_2_1380x776.png 2x" data-dominant-color="BFBFC5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @anitakh1 (2019-03-08 08:54 UTC)

<p>hello sir,<br>
pl tell the way to show two separate 3D segmented output as one but showing the different in two</p>

---

## Post #16 by @anitakh1 (2019-03-12 10:38 UTC)

<p>please tell me the solution sir. both are segmented 3D results which i found out using two algorithms</p>

---

## Post #17 by @lassoan (2019-03-13 14:00 UTC)

<p>I don’t think <a href="https://chestimagingplatform.org/library-cip" rel="nofollow noopener">CIP</a> can automatically compute airway length. I don’t know what you mean by “number of airway tree” (there is one tree).</p>
<p>VMTK (vascular modeling toolkit) extension can compute centerline and endpoints of arterial trees, which could be usable for airways, too.</p>
<p>If these automatic methods fail and you don’t have time or expertise to fix them then you can do the work manually: use markups module to define centerlines, measure curve length, and count number of branches.</p>

---

## Post #18 by @anitakh1 (2019-03-14 12:55 UTC)

<p>thanks a lot, will try. i mean how to find number of airway branches detected and not tree, sorry</p>

---

## Post #19 by @anitakh1 (2019-04-30 10:32 UTC)

<p>sir can you tell me how to find slice thickness and transversal resolution in lung volume CT data?<br>
thanks</p>

---

## Post #20 by @lassoan (2019-05-03 12:53 UTC)

<p>You can find slice thickness in Volumes module, Volume Information section, Image spacing. Slice spacing is usually the third value.</p>

---

## Post #21 by @anitakh1 (2019-05-06 05:07 UTC)

<p>thank you sooooo much</p>

---

## Post #22 by @joshWilliams (2019-07-06 14:14 UTC)

<p>Hi Anitakh,</p>
<p>How did you segment the airways you show in this image? I am having difficulty segmenting below the trache and main bronchus. To segment the smaller airways is quite challenging.</p>
<p>Any help would be greatly appreciated.</p>

---

## Post #23 by @anitakh1 (2019-07-08 11:57 UTC)

<p>you can do it by region growing technique or follow the method given in a paper by Deniz Akykac et al IEEE transaction 2003. you can follow other methods given in different methods.</p>

---

## Post #24 by @rbumm (2019-07-08 15:47 UTC)

<aside class="quote no-group" data-username="anitakh1" data-post="23" data-topic="5075">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>Deniz Akykac et al IEEE transaction 2003</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>I am having the same problem.<br>
There are several questions.<br>
Could you describe a bit more in detail how you segment the smaller airways ?<br>
How do you use the region growing technique ?<br>
Do you start with the airway segmentation of the chest imaging suite ?</p>
<p>Where can I find information about the Akykac method ?</p>
<p>Thank you very much.</p>

---

## Post #25 by @anitakh1 (2019-07-26 08:55 UTC)

<p>sir, is it possible to put different points of different colors on airway segmented tree. this will help to know total branches in each generation.! i am showing sample in pic<a href="/404" data-orig-href="upload://6QQ4AHa5L6C8atYf8QfTfp1suXS.png">marking_branches|547x500</a></p>

---

## Post #26 by @lassoan (2019-07-26 12:01 UTC)

<p>You can place markups fiducial points. In each markups node you can specify two colors (selected and non-selected). If you need more colors then you can create more markups nodes (or write a script that observes point positions and places a differently colored sphere at each point position).</p>

---
