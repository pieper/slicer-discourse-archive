---
topic_id: 45223
title: "How To Save All Modified Volume Rendering Presets In An Mrb"
date: 2025-11-25
url: https://discourse.slicer.org/t/45223
---

# How to Save All Modified Volume-Rendering Presets in an MRB File

**Topic ID**: 45223
**Date**: 2025-11-25
**URL**: https://discourse.slicer.org/t/how-to-save-all-modified-volume-rendering-presets-in-an-mrb-file/45223

---

## Post #1 by @Eva_Monclus_Lahoya (2025-11-25 15:01 UTC)

<p>Operating system:Windows<br>
Slicer version:5.8.1</p>
<p>Hello everyone, I’m working with a CT volume dataset and experimenting with the volume-rendering presets. I’d like to apply various changes to multiple presets and save all of them. However, when I save the scene using the MRB file format, only the most recent changes to the last preset I used are saved.</p>
<p>Is there a way to save all the modifications I’ve made to the different presets?</p>
<p>Thanks in advance,</p>

---

## Post #2 by @muratmaga (2025-11-25 17:59 UTC)

<aside class="quote no-group" data-username="Eva_Monclus_Lahoya" data-post="1" data-topic="45223">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/eva_monclus_lahoya/48/80854_2.png" class="avatar"> Eva_Monclus_Lahoya:</div>
<blockquote>
<p>modifications I’ve made to the different presets</p>
</blockquote>
</aside>
<p>You will probably need to save them as new volume property files for changes to be retained.</p>

---

## Post #3 by @Eva_Monclus_Lahoya (2025-11-26 14:45 UTC)

<p>Okay. But I’m wondering whether it’s possible to upload them separately while keeping the same scene, without having to reload the entire scene using a different volume-property file?</p>

---

## Post #4 by @muratmaga (2025-11-26 16:20 UTC)

<p>You mean modify the preset with your own customization and make it persist between Slicer sessions? That’s currently not possible. There has been some discussion about adding a functionality about creating and adding custom user presets, but I believe it is not ready yet.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---
