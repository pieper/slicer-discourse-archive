---
topic_id: 37732
title: "Load Raw Microct Data With Vgi Metadata"
date: 2024-08-06
url: https://discourse.slicer.org/t/37732
---

# Load .raw microCT data with .vgi metadata

**Topic ID**: 37732
**Date**: 2024-08-06
**URL**: https://discourse.slicer.org/t/load-raw-microct-data-with-vgi-metadata/37732

---

## Post #1 by @mpuig (2024-08-06 14:07 UTC)

<p>Hello,</p>
<p>I am trying to load .raw data, that are paired with rich .vgi metadata. I’m aware of the RawImageGuess module, But is there not a way to directly use the .vgi file in conjunction with a .raw file?<br>
For the sake of completion, I have the following files :</p>
<ul>
<li>.raw</li>
<li>.raw.xmp</li>
<li>.nhdr</li>
<li>.vgi</li>
</ul>
<p>I tried using the RawImageGuess extension on the .raw files manually inputing the metadata I found in the .nhdr and the .vgi but I didn’t find any signal, maybe because I don’t have information about the header size.</p>
<p>Any advice as to the best way to load this microCT data?<br>
Thank you very much.</p>

---

## Post #2 by @muratmaga (2024-08-06 15:18 UTC)

<aside class="quote no-group" data-username="mpuig" data-post="1" data-topic="37732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e9c0ed/48.png" class="avatar"> mpuig:</div>
<blockquote>
<p>But is there not a way to directly use the .vgi file in conjunction with a .raw file?</p>
</blockquote>
</aside>
<p>It is possible to develop a module to do that. We already one example in SlicerMorph called <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/GEVolImport/GEVolImport.py" rel="noopener nofollow ugc">GEVolImport</a></p>
<p>You can take a look at it, and modify it to work for your cases.</p>
<p>However, you will have to reverse engineer the vgi format and decide what fields to read and what to ignore. Also if VGStudio changes the format of the file, you have to keep updating the module.</p>
<p>So it is often simpler to look at the data extends and the type from the vgi file, and then use the RawImageGuess to directly enter those values to import the file. But if you are willing to try developing a module, we can guide you…</p>

---

## Post #4 by @mpuig (2024-08-08 09:43 UTC)

<p>Thank you,<br>
I will ask the lab for more detail about the data format and work from there</p>

---
