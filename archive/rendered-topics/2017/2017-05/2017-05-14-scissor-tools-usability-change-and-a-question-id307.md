# Scissor tools usability change and a question

**Topic ID**: 307
**Date**: 2017-05-14
**URL**: https://discourse.slicer.org/t/scissor-tools-usability-change-and-a-question/307

---

## Post #1 by @muratmaga (2017-05-14 05:44 UTC)

<p>Hi,</p>
<p>May I suggest to add a keystroke to scissors functionality so that the user doesn’t have to go back and forth between ‘none’ and ‘scissors’ effects constantly to spin the specimen in the 3D view while segmenting. Perhaps, during the scissors effect holding the shift or control with the left click can temporarily become the rotation.</p>
<p>Also, is it possible to integrate the scissors with ROI clipping? Sometimes I want the scissors to affect only a portion of the volume, not all the slices. With ROI, perhaps there can be an additional option for operation to be effective within ROI (or outside of of ROI).<br>
Thanks,<br>
M</p>

---

## Post #2 by @lassoan (2017-05-14 11:13 UTC)

<p>You can activate/deactivate effects with number keys (1, 2, …, 0). With the default effect order, scissors is assigned to key ‘0’.</p>
<p>Scissors can be marked, so you can fill/erase only inside a selected region: change “Editable region” in masking section.</p>

---

## Post #3 by @muratmaga (2017-05-15 04:49 UTC)

<p>Thanks Andras. Key shortcuts were exactly what I needed. Sped up the tasks quite a bit.</p>
<p>However, i am not sure how editable region setting would work in my task. I tried to illustrate one example here. This highlighted bone is not touching the rest of the specimen. In most cases I can find an angle where nothing is in the field of view behind it, and I can easily remove it with scissors. However, there are cases where I can’t find such an angle, so it becomes more challenging.</p>
<p>Also would it be possible to use the scissors to not to erase something, but to assign a different segment.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef3c42f6b9fde3ee154241327d4c9907540de60.png" alt="image" data-base62-sha1="rfeZ9DBPiiikuoPwLXojuUWJ3cQ" width="607" height="405"></p>

---

## Post #4 by @lassoan (2017-05-15 05:17 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Also would it be possible to use the scissors to not to erase something, but to assign a different segment.</p>
</blockquote>
</aside>
<p>You can do all kind of separation, masking, and fusion with the right combination of scissors and masking settings. For example, to assign a part of segment A to segment B:</p>
<ul>
<li>In segment list (above the effect buttons): select segment B</li>
<li>In Masking / Editable area: select Inside segment A</li>
<li>In Scissors effect options: select Fill inside</li>
</ul>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>In most cases I can find an angle where nothing is in the field of view behind it, and I can easily remove it with scissors. However, there are cases where I can’t find such an angle, so it becomes more challenging.</p>
</blockquote>
</aside>
<p>Use the same setup as described above (for separating segments) but hide Segment B. This allows you to temporarily hide any parts by assigning to an invisible segment. The hidden parts can be added back later using Scissors effect or Logical operators.</p>

---

## Post #5 by @jo1 (2022-01-24 05:33 UTC)

<p>No… in 4.11 20200930 ver, Smoothing is assigned to key 0.<br>
There is no shortcut for Scissors. I can’t find it. :((</p>

---

## Post #6 by @lassoan (2022-01-24 05:39 UTC)

<p>In current Slicer Preview Release, default shortcut for Smoothing is <kbd>0</kbd>, default shortcut for Scissors is <kbd>Shift</kbd>+<kbd>1</kbd> (or <kbd>!</kbd>). You may not need to use these, as you can switch between the last two effects using the <kbd>space</kbd> key, and you can also specify any keyboard shortcut to any action in Slicer (see for example how to make <kbd>s</kbd> key toggle sphere brush).</p>
<p>What is your workflow? What tools do you need to switch between frequently, in what order?</p>

---

## Post #7 by @jo1 (2022-01-24 08:26 UTC)

<p>finaly! Thank you!!!<br>
Oh…I want to make “vessel segmentation” for AI data.<br>
So I’m using Scissors, Threshold and Islands (also sometime using Logical operators)<br>
I tried so many different ways. But it didn’t work well (Local Threshold and over sampling or Nvidia AiAA or etc…)<br>
How can I separate artery and vein from the brain bone? so hard…</p>

---

## Post #8 by @chir.set (2022-01-24 10:39 UTC)

<aside class="quote no-group" data-username="jo1" data-post="7" data-topic="307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jo1/48/13932_2.png" class="avatar"> jo1:</div>
<blockquote>
<p>How can I separate artery and vein from the brain bone? so hard…</p>
</blockquote>
</aside>
<p>You could reduce the input volume by many means, and you should do it.</p>
<p>One way follows :</p>
<ul>
<li>Surround the brain with a ROI node</li>
<li>Use ‘Local threshold’ to mask the brain <em>in the ROI</em></li>
<li>Fill holes in this segment with ‘Smoothing’ effect</li>
<li><em>Shrink</em> the segment by 3 mm; you will unfortunately lose the internal carotids in the base skull</li>
<li>Create another volume by ‘Split volume’ from this segment. Use -1500 as ‘Fill value’</li>
<li>Create another segmentation and use the volume created by ‘Split volume’</li>
</ul>
<p>Using ‘Flood filling’, I could get this for surgically relevant arteries. But other segmentation tools can be used of course.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1f2fad7277f9f88ddd68ac66d96f63014195301.png" data-download-href="/uploads/short-url/weQ0N5eEz6wis6K9c7K0Gx46gX7.png?dl=1" title="minimal_cerebral_arteries" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1f2fad7277f9f88ddd68ac66d96f63014195301_2_690x467.png" alt="minimal_cerebral_arteries" data-base62-sha1="weQ0N5eEz6wis6K9c7K0Gx46gX7" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1f2fad7277f9f88ddd68ac66d96f63014195301_2_690x467.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1f2fad7277f9f88ddd68ac66d96f63014195301.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1f2fad7277f9f88ddd68ac66d96f63014195301.png 2x" data-dominant-color="060706"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">minimal_cerebral_arteries</span><span class="informations">930×630 72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At any step, you will have to get best parameters by trial and error.</p>
<p>This task remains a challenge, and there are no standard recipes.</p>

---

## Post #9 by @jo1 (2022-01-25 04:24 UTC)

<p>Thank you!!!<br>
can I ask where can I get information about ROI node?<br>
What exactly do you mean this?<br>
and How can I surround the brain? (I only assume “Markups” but still it’s nor clear)<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a9bc4697a11aa4ebc1d6e929fa3899f2d6a784a.png" alt="image" data-base62-sha1="huDYPyOx7gcZFswVlTFD21epys2" width="347" height="283"></p>
<p>you mean this…? I used MarkupsClosedCurve</p>

---

## Post #10 by @chir.set (2022-01-25 07:09 UTC)

<aside class="quote no-group quote-modified" data-username="jo1" data-post="9" data-topic="307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jo1/48/13932_2.png" class="avatar"> jo1:</div>
<blockquote>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html" class="inline-onebox" rel="noopener nofollow ugc">Markups — 3D Slicer documentation</a></p>
</blockquote>
</aside>
<p>This very page gives you information about ROI nodes. Spend much time tinkering with the basics of each Slicer core tool, and the basics of each Segment Editor tool. From your replies, I grant you should explore much more before performing advanced tasks.</p>

---

## Post #11 by @jo1 (2022-01-25 08:42 UTC)

<p>wow!!! Thank you!! I’m still not growing up enough though, I got a fancy image!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5975345d42a8a0e4a4942d378830509b598f06b0.png" data-download-href="/uploads/short-url/cLnBtwNvy1S2Kfl4fu0Ooq8OuTS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5975345d42a8a0e4a4942d378830509b598f06b0_2_400x500.png" alt="image" data-base62-sha1="cLnBtwNvy1S2Kfl4fu0Ooq8OuTS" width="400" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5975345d42a8a0e4a4942d378830509b598f06b0_2_400x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5975345d42a8a0e4a4942d378830509b598f06b0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5975345d42a8a0e4a4942d378830509b598f06b0.png 2x" data-dominant-color="151915"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">501×625 75.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @chir.set (2022-01-25 12:17 UTC)

<p>Please have a look at <a href="https://disk.yandex.com/i/hxq0vQRHBqHqyw" rel="noopener nofollow ugc">this</a> video. The steps are slightly different as described above to save time.</p>
<p>Note also that if you only need to <em>view</em> the arteries, Volume Rendering is faster and perhaps more efficient. And you should be careful to distinguish between arteries and veins.</p>

---

## Post #13 by @jo1 (2022-01-26 05:03 UTC)

<p>ahhhhhh got it. my step was a little bit different with yours.</p>

---
