# Markups control points list window expandable? (v4.11.20200930)

**Topic ID**: 14464
**Date**: 2020-11-06
**URL**: https://discourse.slicer.org/t/markups-control-points-list-window-expandable-v4-11-20200930/14464

---

## Post #1 by @Greydon_Gilmore (2020-11-06 22:25 UTC)

<p>Hello,</p>
<p>I am working on the most recent stable release and have noticed the control points list window, within the Markups module, is more condensed then previous versions.</p>
<p>Is there a way to expand this window to be able to see more control points at one time?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3180cf9d51ee23f0fb7f284353666f1fc7aefc41.png" alt="image" data-base62-sha1="73Vn5fIy5Z64q8jxrasWCRGe88x" width="486" height="336"></p>
<p>Thank you!</p>

---

## Post #2 by @Greydon_Gilmore (2021-03-17 18:20 UTC)

<p>I wanted to follow-up on this. Is there any way for me to modify the number of rows in the Markups fiducial list? Currently I only see a maximum of 7 rows.</p>
<p>Greydon</p>

---

## Post #3 by @muratmaga (2021-03-17 19:17 UTC)

<p>I agree it would be nice to able to increase/decrease the control point table. meanwhile, did you try using the scroll bar next to it to see the additional points?</p>

---

## Post #4 by @Greydon_Gilmore (2021-03-17 19:31 UTC)

<p>Yes, I’ve been scrolling but sometimes a patient may have &gt;100 points… scrolling becomes tedious with only 7 points displayed at a time.</p>

---

## Post #5 by @lassoan (2021-03-17 19:55 UTC)

<p>Could you describe what is your overall goal and particular needs are? Slicer core modules are very generic, they expose all possible options, and therefore they are complex, take a lot of space, and not optimized for specific use cases.</p>
<p>If we cannot figure out a solution that works well for your use case but also preserves generality of the core Markups module then you can create a landmarking module with fine-tuned user interface for your particular task. It is very easy to put together such modules, because you can use high-level widgets that Slicer provides using a visual user interface editor.</p>
<p>I think something is already being developed in SlicerMorph, but it may or may not be optimal for your workflow. <a class="mention" href="/u/muratmaga">@muratmaga</a> is there a landmarking module in SlicerMorph? What are its main use cases?</p>

---

## Post #6 by @Greydon_Gilmore (2021-03-17 20:04 UTC)

<p>Could the bottom of the markups panel contain a <code>QSplitter</code> to allow a user to expose a greater number of markups rows at one time. In previous versions of Slicer the Markups panel would allow a greater number of points to be viewed at one time:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c5a5bb6a6fc54127c5073dc4ed941ad08949797.png" data-download-href="/uploads/short-url/1LhjV8vqtfWSjBi9XT7D5Zk9FR5.png?dl=1" title="old_behaviour" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c5a5bb6a6fc54127c5073dc4ed941ad08949797_2_318x500.png" alt="old_behaviour" data-base62-sha1="1LhjV8vqtfWSjBi9XT7D5Zk9FR5" width="318" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c5a5bb6a6fc54127c5073dc4ed941ad08949797_2_318x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c5a5bb6a6fc54127c5073dc4ed941ad08949797_2_477x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c5a5bb6a6fc54127c5073dc4ed941ad08949797.png 2x" data-dominant-color="EBEAF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">old_behaviour</span><span class="informations">573×900 68.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Seems like in the new markups iteration there is a lot of empty space.</p>

---

## Post #7 by @muratmaga (2021-03-17 20:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="14464">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I think something is already being developed in SlicerMorph, but it may or may not be optimal for your workflow. <a class="mention" href="/u/muratmaga">@muratmaga</a> is there a landmarking module in SlicerMorph? What are its main use cases?</p>
</blockquote>
</aside>
<p>Currently we do not have a ‘landmarking’ module in SLicerMorph, we still use and teach how to use the core Markups module for anatomical LM collection.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> is working on the ability to create blank LMs and be able to feed in a LM template to improve the experience. Once that’s done, we might visit the issue of having a simpler LM module with much fewer of the display features exposed (possibly with adjustable subject hiearrchy box and control table).</p>

---
