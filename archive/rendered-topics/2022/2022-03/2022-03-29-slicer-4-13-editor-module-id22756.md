---
topic_id: 22756
title: "Slicer 4 13 Editor Module"
date: 2022-03-29
url: https://discourse.slicer.org/t/22756
---

# Slicer 4.13 Editor module

**Topic ID**: 22756
**Date**: 2022-03-29
**URL**: https://discourse.slicer.org/t/slicer-4-13-editor-module/22756

---

## Post #1 by @Cervantes (2022-03-29 18:38 UTC)

<p>Hi everyone,<br>
I have just installed Slicer 4.13 and am working on making some models from CT scans (I have been following the <em>Robles et al</em>. 2020 paper). I was successful in Slicer 4.11, but in 4.13 I can’t find the “Editor” module. The “Segment Editor” module is there, but it doesn’t have the “Make Model” button that was in Editor.<br>
Has this been removed/changed? Am I having an issue with my Antivirus possibly? Would it be better to go back to 4.11 (though with that I couldn’t get the ALPACA module to load)?<br>
Any suggestions are appreciated, though please don’t suggest a code-based approach… I’m not there yet. Thanks in advance for any suggestions!</p>

---

## Post #2 by @muratmaga (2022-03-29 18:46 UTC)

<p>Editor module has been discontinued. Everything you can in Editor (plus more) you can do in Segment Editor. With segment Editor, there is no need for Model Maker either.</p>
<p>ALPACA works with 4.11 Stable. Let us know if you have issues.</p>

---

## Post #3 by @cpinter (2022-03-29 18:52 UTC)

<aside class="quote no-group" data-username="Cervantes" data-post="1" data-topic="22756">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cervantes/48/14858_2.png" class="avatar"> Cervantes:</div>
<blockquote>
<p>doesn’t have the “Make Model” button that was in Editor.</p>
</blockquote>
</aside>
<p>You can simply click <code>Show 3D</code>. If you want to export to STL or other surface formats you can right click the segmentation in the <code>Data</code> module and choose <code>Export visible segments to models</code> then save, or you can use the <code>Export/import models and labelmaps</code> section in the <code>Segmentations</code> module to do it directly.</p>

---

## Post #4 by @Cervantes (2022-03-29 19:07 UTC)

<p>Good to know that ALPACA is stable in 4.11. I was suspecting it was an issue on my end, and now I at least have that confirmed. I’ll give it a bit more time and effort with 4.13 now that I know that it isn’t an issue of a missing module or something that didn’t install properly.</p>

---

## Post #5 by @Cervantes (2022-03-29 19:09 UTC)

<p>Thank you Csaba, I will give this a try! This likely solves all of my issues on how to proceed making the model in 4.13!</p>
<p>Between the two of you, I have all of the answers I needed!</p>

---
