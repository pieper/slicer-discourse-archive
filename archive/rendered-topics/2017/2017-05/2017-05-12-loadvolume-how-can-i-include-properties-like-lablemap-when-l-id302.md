---
topic_id: 302
title: "Loadvolume How Can I Include Properties Like Lablemap When L"
date: 2017-05-12
url: https://discourse.slicer.org/t/302
---

# loadVolume: how can I include properties like lablemap when loading?

**Topic ID**: 302
**Date**: 2017-05-12
**URL**: https://discourse.slicer.org/t/loadvolume-how-can-i-include-properties-like-lablemap-when-loading/302

---

## Post #1 by @drAl (2017-05-12 14:12 UTC)

<p>Hi everyone!</p>
<p>i’m writing a script in python and I would like to set the labelmap to TRUE when loading a volume.<br>
I can’t find the way to do it with the slicer.util.loadVolume(fileName, properties, returnNode) instruction.<br>
I don’t konw how to pass the correct property!<br>
I’m trying to load an atlas mask (atlasmask.mha) to perform a Swiss Skull Stripper process.<br>
This is the line:<br>
aMask  = slicer.util.loadVolume(’/myroot/atlasMask.mha’, returnNode=True)</p>
<p>any clue on how to make it?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @mangotee (2017-05-12 14:39 UTC)

<p>Labelmaps have their own routine for loading, I think you need to use that instead of loadVolume.<br>
You would need to write:<br>
aMask = slicer.util.loadLabelVolume(’/myroot/atlasMask.mha’, returnNode=True)</p>

---

## Post #3 by @drAl (2017-05-12 14:41 UTC)

<p>Hi again guys!!</p>
<p>ok…I’m very sorry <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"> …the very second I went back to slicer after writing this post I begin typing and I saw this: slicer.util.loadLabelVolume()…</p>
<p>again…I’m sorry!!</p>
<p>I guess the “I’m new to slicer” excuse is worth it here, isn’t it?</p>
<p>Thaanks to anyone who’s read it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @drAl (2017-05-12 14:42 UTC)

<p>ohh hey mangotee!!<br>
Thanks a lot for replying…I’ll try to exhaust my options next time before asking <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Appreciate it!!</p>
<aside class="quote no-group quote-modified" data-username="mangotee" data-post="2" data-topic="302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>s have their own routine for loading, I think you need to use that instead of loadVolume.<br>
You would need to write:<br>
aMask = slicer.util.loadLabelVolume(‘/myroot/atlasMask.mha’, returnNode=True)</p>
</blockquote>
</aside>

---

## Post #5 by @mangotee (2017-05-12 14:44 UTC)

<p>no problem <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> first time I’m able to ANSWER a question! Usually, I’m on the receiving end of things…</p>

---
