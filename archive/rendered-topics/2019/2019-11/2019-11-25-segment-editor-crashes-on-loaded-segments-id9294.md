---
topic_id: 9294
title: "Segment Editor Crashes On Loaded Segments"
date: 2019-11-25
url: https://discourse.slicer.org/t/9294
---

# Segment editor crashes on loaded segments

**Topic ID**: 9294
**Date**: 2019-11-25
**URL**: https://discourse.slicer.org/t/segment-editor-crashes-on-loaded-segments/9294

---

## Post #1 by @fabian (2019-11-25 14:03 UTC)

<p>Hi All!</p>
<p>I have a problem with the Segment Editor crashing. I load a dataset and a set of segment nodes that I have created in a previous session (.nrrd). This works well. But as soon as I conduct any operation on these segments in the Segment Editor, Slicer crashes and shuts down.</p>
<p>This does not occur if I save my segments as a labelmap, load that, and then extract the segments from it. However, this is quite tedious for me because I have some segments that overlap each otherwhich is obviously corrupted in the labelmap conversion.</p>
<p>I have tried this on three Windows machines with Slicer versions 4.8.1, 4.10.2, and 4.11. The issue is reproducible in all of them.</p>
<p>Would be grateful for any hints. Thanks a lot!</p>

---

## Post #2 by @Sunderlandkyl (2019-11-25 14:45 UTC)

<p>What version of Slicer was the segment .nrrd saved with?<br>
Could you could upload your nrrd file somewhere?</p>

---

## Post #3 by @fabian (2019-11-25 15:22 UTC)

<p>Kyle! Thanks a lot -  I think your question may have already solved it. The nrrd file was saved with 4.10.2. Same problem occurred over a bunch of datasets. Now I saved one with 4.11.0 - and it seems to work. Didn’t think to try and <strong>save</strong> them with different versions.</p>
<p>Thanks a lot! I’ll be back if it occurs again. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @Sunderlandkyl (2019-11-25 15:27 UTC)

<p>Slicer should not be crashing with segments from 4.10.2, so there is still something wrong.<br>
If you could provide a segmentation that causes Slicer to crash, it would be very helpful.</p>

---

## Post #5 by @fabian (2019-11-25 15:50 UTC)

<p>Yup. Fair point! Thank you for your help!</p>
<p>Here’s a download link that’s valid for the next 24-ish hours. Let me know if this is in any way helpful.</p>
<p>edit - here’s the actual link: <a href="https://data.stimulate.ovgu.de/d/fd98c2896f9c471f931c/" rel="nofollow noopener">https://data.stimulate.ovgu.de/d/fd98c2896f9c471f931c/</a></p>

---

## Post #6 by @Sunderlandkyl (2019-11-25 16:00 UTC)

<p>Unfortunately, I can’t seem to replicate the issue. The segmentation loads fine on 4.10.2, as well as the latest nightly.</p>

---

## Post #7 by @fabian (2019-11-25 16:09 UTC)

<p>Can you edit the segments?</p>

---

## Post #8 by @Sunderlandkyl (2019-11-25 16:17 UTC)

<p>Ah sorry, I see the crash now. I’ll debug into this issue.<br>
Thanks for your assistance!</p>

---

## Post #9 by @Sunderlandkyl (2019-11-25 18:22 UTC)

<p>There seems to be a problem with the tumor extent. See line 22 in the NRRD file:<br>
<code>Segment1_Extent:=17 21 0 38 224 77</code></p>
<p>This isn’t a problem that I’ve seen before with saved segments.<br>
How was the tumor segment set?<br>
Was the NRRD edited manually?</p>

---

## Post #10 by @Sunderlandkyl (2019-11-25 18:38 UTC)

<p>In any case, I’ve made a pull request that should solve this issue here: <a href="https://github.com/Slicer/Slicer/pull/1267" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1267</a></p>

---

## Post #11 by @fabian (2019-11-26 06:44 UTC)

<p>That is awesome! Yes, it is modified manually and we get rid of the tumour segment but were not aware that it’s crucial to actually delete the whole thing. Thanks so much Kyle!</p>

---

## Post #12 by @Sunderlandkyl (2019-11-26 14:24 UTC)

<p>The fix should be availiable in the latest 4.11 nightly.</p>

---
