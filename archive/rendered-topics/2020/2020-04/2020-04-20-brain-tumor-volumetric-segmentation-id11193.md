# Brain tumor volumetric segmentation

**Topic ID**: 11193
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/brain-tumor-volumetric-segmentation/11193

---

## Post #1 by @kalpathi (2020-04-20 00:34 UTC)

<p>I watched a Slicer video on a brain tumor segmentation -  that video used  a Volumetric Segmentation module (Slicer3D 4.6.x). I dont find it in the latest version. What has replaced that?  Are there more detailed documentation on doing basic volume segmentation I can look at and learn - been looking at videos but some of these are from eearlier versions of sliicer and am not able to map that to the new version (am running the latest  stable(4.10.2). I am trying to segment a 3D volume and illustrate models of that segmentation (like a tumor). As I am new to Slicer, its a little overwhelming…</p>
<p>Thanks.</p>
<pre><code>  -- krs</code></pre>

---

## Post #2 by @lassoan (2020-04-20 13:19 UTC)

<p>Slicer’s segmentation tools have been tremendously improved in the last few years, so those old tutorials are not that relevant anymore.</p>
<p>You can find up-to-date, step-by-step instructions for segmenting brain tumor, cyst, ventricles, doing diffusion tractography, etc. in the <a href="https://github.com/spujol/NeurosurgicalPlanningTutorial/blob/master/WhiteMatterExplorationTutorial_SoniaPujol-RonKikinis.pdf">Neurosurgical planning tutorial</a>.</p>

---

## Post #3 by @kalpathi (2020-04-27 15:07 UTC)

<p>Thanks a lot. That tutorial was very helpful. One question. After I did the tutorial myself, I noticed some parts of the tumor were not segmented. The tutorial used the Grow/Cut and Threshold tools to build segmentation.  How can I now augment the segmentation to ensure the remaining slices were also segmented and build a more accurate segmentation.</p>
<p>A second question is… are there more detailed description of each of the segmentation tools that appear in the segementation editor (that I can look up and help me decide which ones to use).  I am working with very noisy data, hence its going to take some combination of segmentation algorithms to get a reasonable segmentation.</p>
<p>Thanks.<br>
- krs</p>

---

## Post #4 by @lassoan (2020-04-27 16:03 UTC)

<aside class="quote no-group" data-username="kalpathi" data-post="3" data-topic="11193">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kalpathi/48/6543_2.png" class="avatar"> kalpathi:</div>
<blockquote>
<p>How can I now augment the segmentation to ensure the remaining slices were also segmented and build a more accurate segmentation.</p>
</blockquote>
</aside>
<p>There is no such thing as a perfect segmentation, just one that meets clinical requirements. While using “Grow from seeds” you are expected to keep painting more seeds until you find the segmentation accurate enough for your purpose.</p>
<aside class="quote no-group" data-username="kalpathi" data-post="3" data-topic="11193">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kalpathi/48/6543_2.png" class="avatar"> kalpathi:</div>
<blockquote>
<p>are there more detailed description of each of the segmentation tools that appear in the segementation editor (that I can look up and help me decide which ones to use)</p>
</blockquote>
</aside>
<p>Reference documentation of built-in tools are available <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">here</a>, but of course to be good in segmentation you also need to learn the strategy of how to use these tools in combination. You can learn them from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">segmentation tutorials and recipes</a>.</p>
<p>If you have any specific problems, post them as separate topics, with screenshots and detailed explanation of your requirements and difficulties that you are experiencing.</p>

---

## Post #5 by @kalpathi (2020-04-30 20:28 UTC)

<p>This was very helpful and I am getting there…  I went through the tutorial and did the segmentation. I saw that there were a few slices that didnt seem to be segmented and so I tried the same procedure marking 3 slices and then trying to follow the same procedure, but this part didnt work. At least I didnt see region growing algorthm work like the first time.  Any thoughts what I might be doing wrong. I read that you cannot edit a labeled volume, could that have something to do with it?   In other words, what I did was get the 3 segments (solid, cystic and ventricles) like in the tutorial and I wanted to go add seeds to 3 slices at the end of the sgementations (that wasnt segmented)  of the solid and cyst segments of the data. But my seeds remained the same and it didnt grow with the region growing algorithms… any thoughts what I am doing wrong?</p>

---

## Post #6 by @lassoan (2020-04-30 20:33 UTC)

<p>Segmentation region is determined from the initial seeds, by extending the region by 20% on all sides. If you add more seeds at or outside the boundary then reinitialize by clicking “Cancel” and then “Initialize”.</p>

---

## Post #7 by @kalpathi (2020-05-05 18:37 UTC)

<p>Thanks. Are t he segmentation seeds retained with the saved volume? I am noticing some parts of the data that was not segmented and was trying to see if I can go back to the state with just the seeds, modify/augment them and then run the segmentation algorithm again. Or is that too much to ask? -<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<pre><code>  -- krs</code></pre>

---

## Post #8 by @lassoan (2020-05-06 02:57 UTC)

<p>Segments are overwritten by the final segmentation results when you apply the segmentation. If you want to save the seeds then you can Clone the segmentation node in Data module (uding right-click menu).</p>

---
