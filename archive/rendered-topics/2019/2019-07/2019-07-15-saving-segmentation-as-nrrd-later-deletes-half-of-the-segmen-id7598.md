---
topic_id: 7598
title: "Saving Segmentation As Nrrd Later Deletes Half Of The Segmen"
date: 2019-07-15
url: https://discourse.slicer.org/t/7598
---

# Saving Segmentation as NRRD, later deletes half of the segmentation?!

**Topic ID**: 7598
**Date**: 2019-07-15
**URL**: https://discourse.slicer.org/t/saving-segmentation-as-nrrd-later-deletes-half-of-the-segmentation/7598

---

## Post #1 by @NoobForSlicer (2019-07-15 22:48 UTC)

<p>So I have been cropping some bigger volume down to smaller volumes so that weaker PC on my job can handle it. Poor thing only has 2gb ram and slicer takes up to 3 to even 4 sometimes during cropping or some task. Plus it’s gpu is non existent.</p>
<p>So all worked nicely so far… However&gt;&gt;&gt; I worked today all day segmenting things however, once I saved files and sent them to my home email so I can compile it all into 1 file on my home computer which is much faster, I realized that half of segmentations in each file have simply disappeared…</p>
<p>what could possibly cause this?<br>
Maybe I clicked something wrong…<br>
Tomorrow I’ll be at my work so I will try again and be more careful this time…<br>
In a meanwhile maybe someone has an idea what I could have been doing wrong so that the half of structure is segmented and half of it not. I am 100% sure i segmented entire structure.</p>

---

## Post #2 by @cpinter (2019-07-16 13:27 UTC)

<p>This is very strange. We have had the segmentation file writer more or less unchanged in the last 3 years, and haven’t heard about a bug like this. That said it’s possible that calculating the joint extent that is saved to file is wrong in your case.</p>
<ul>
<li>Have you tried segmenting the same image at home? Even just drawing nonsense about the same size as the real segments (I don’t think the computer is the issue though)</li>
<li>How big is the image you’re segmenting?</li>
<li>How many segments do you have?</li>
</ul>
<p>While this issue is not solved, I suggest that you save an mrb (single-file scene - click on the gift icon in the save window) before you take it home just so you have the whole scene, and after that go to Segmentations module, switch the master to closed surface (make sure you have a surface shown in 3D - best if without any smoothing), and save it also in vtm/vtp format. It’s very unlikely that both the labelmap and surface writers are wrong.</p>

---

## Post #3 by @hherhold (2019-07-16 13:54 UTC)

<p>I did something like this once when I was not paying attention to node names and filenames and inadvertantly overwrote ‘Segmentation.seg.nrrd’. Make sure you have your names and directories set correctly.</p>

---

## Post #4 by @lassoan (2019-07-16 14:11 UTC)

<p>If you run out of memory then anything can happen. Saving is a very memory-intensive operation, so there is a chance that you run out of memory during saving.</p>
<p>Make sure to allocate enough virtual memory (typically 10x the size of your data set is enough) and you won’t run out of memory. If you only have 2GB of physical memory then things will be very slow but everything should still work if you have enough virtual memory.</p>

---

## Post #5 by @NoobForSlicer (2019-07-16 14:49 UTC)

<p>yes you are right!! I  took two cards of ram from another computer at my work and put it into this one and now works like charm!!</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @NoobForSlicer (2019-07-16 14:51 UTC)

<p>This is crazy!! This forum is extremely helpful, such a great community.</p>
<p>I never encountered such great forum. I am literally puzzled. Companies that pay dedicated customer service are not this helpful. How does this even work? I mean you guys are like super helpful</p>

---

## Post #7 by @cpinter (2019-07-16 15:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="7598">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you run out of memory then anything can happen. Saving is a very memory-intensive operation, so there is a chance that you run out of memory during saving</p>
</blockquote>
</aside>
<p>Wouldn’t this result in a crash? I assumed if the saving process ends without any apparent issues, then probably virtual memory managed to handle it right? I’m just trying to understand how we’d end up with a half-saved segmentation without a crash.</p>

---

## Post #8 by @NoobForSlicer (2019-07-16 16:14 UTC)

<p>To be honest I myself am confused, I just took out them 2 extra cards of ram and did everything and worked fine…</p>
<p>It could be that I stupidly somehow &gt;&gt; just created a second segment I did not save. Which is also very likely since as my nick says i am a NoobForSlicer.</p>
<p>However what you’re saying makes absolute sense… I had Slicer crash couple of times after it was not able to do cropping because of low ram. Sometimes it didn’t crash but instead just aborted the function after being frozen for like 10 minutes.</p>
<p>So this was probably my mistake</p>

---

## Post #9 by @lassoan (2019-07-16 16:28 UTC)

<p>If we run out of memory then the behavior is kind of undeterministic - depends what exact allocations failed. If we can allocate the entire write buffer but something fails while filling it then it is possible that only the half image is written.</p>

---
