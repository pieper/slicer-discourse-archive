---
topic_id: 40041
title: "Slicer Closes When Opening Already Known Datasets With Raw I"
date: 2024-11-05
url: https://discourse.slicer.org/t/40041
---

# Slicer closes when opening (already known) datasets with "Raw Image Guess" Module

**Topic ID**: 40041
**Date**: 2024-11-05
**URL**: https://discourse.slicer.org/t/slicer-closes-when-opening-already-known-datasets-with-raw-image-guess-module/40041

---

## Post #1 by @Marek57 (2024-11-05 19:30 UTC)

<p>Dear Community,</p>
<p>I am new in this forum. I have been successfully using Slicer for a few weeks only, but it suddenly stopped working a few days ago.<br>
I open generic datasets (files), containing stacks of equally sized binary images, stored in uint16 format. Images have typically 500x500 to 1000x1000 pixels size and up to 1000 images are sequentially stored in a single file (no header).<br>
I am using “Raw Image Guess” Module to open/read these files (with some manual adjustment of the volume size). So far I could open several of them, which were then appeared on an “Input file” list. Until recently I had had no problem in switching between (five) files from the list, load to the “Volume Rendering” module and view / manipulate the content. However, for unknown reason Slicer stopped working a few days ago and any attempt to open any of these files ends up with a crash, or Slicer disappearing (closing) without an message.</p>
<p>I am using Slicer 5.6.2 r32448, running on an older laptop (MSI GT72 6QD Dominator) under Windows 10 Pro 20H2. The configuration includes a i7-6700HQ CPU, 32 GB RAM and NVIDIA GeForce GTX 970M GPU. The drivers shall by all uo-to-date (to my knowledge, but have to check again). No software updates (neither Windows, nor other programs) have been done recently.</p>
<p>What shall / could I do, in order to trace (and solve) the problem? Any suggestions would be welcome.<br>
Thank you in advance!</p>

---

## Post #2 by @lassoan (2024-11-05 19:33 UTC)

<p>Does the crash happen only above a certain image size, or you get a crash even if you set image size to 50x50x50?</p>
<p>Have you installed any other extensions than RawImageGuess? If yes, then you can install Slicer again, into a new folder, install only RawImageGuess extension, and see if it behaves the same way.</p>

---

## Post #3 by @Marek57 (2024-11-05 22:01 UTC)

<p>I have not installed any other modules, just the standard set and “RawImageGuess”.<br>
I will check smaller sizes (for exeample 50x50x50), but I will not be able to do before Friday. I will then give you an update,</p>

---

## Post #4 by @muratmaga (2024-11-05 22:22 UTC)

<aside class="quote no-group" data-username="Marek57" data-post="1" data-topic="40041">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e68b1a/48.png" class="avatar"> Marek57:</div>
<blockquote>
<p>I open generic datasets (files), containing stacks of equally sized binary images, stored in uint16 format. Images have typically 500x500 to 1000x1000 pixels size and up to 1000 images are sequentially stored in a single file (no header).</p>
</blockquote>
</aside>
<p>Actually it will simpler to use ImageStacks module of SlicerMorph for this. RawImageGuess is more useful to experimentally test the geometry of the volume, when you don’t actually know the dimensions, or other image metadata.</p>

---

## Post #5 by @Marek57 (2024-11-11 07:45 UTC)

<p>I am back.<br>
I have done a few experiments with the following results:</p>
<ol>
<li>if I select a NEW small volume (I have tried 50^3 to 400^3) from the disk then they open without any problem</li>
<li>if I then select a larger volume (800 x 800 x 900), either from the disk or from the list (of last opened files) then also this data opens without crash</li>
<li>however, when I try to open ANY file, even a small one (50^3) - from a list or disk then Slicer silently crashes (disappears/closes)<br>
Could it be that the last opened large file (large enough) brings Slicer to crash? Memory buffer not being emptied before new load?<br>
The files I have been used so far are of max. 1,3 GB size and the laptop is equipped with 32 GB RAM. When Slicer (1,3 GB data), along with Windows and other applications is running then they take less then 14% of RAM.<br>
Any idea?</li>
</ol>
<p>By the way, is there any way to clean / reset the list of the last opened files, in order to let Slicer run with no “history” (empty data buffer)?</p>
<p>Thank you in advance!</p>

---

## Post #6 by @lassoan (2024-11-11 19:16 UTC)

<p>These two statements seems to contradict:</p>
<aside class="quote no-group" data-username="Marek57" data-post="5" data-topic="40041">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e68b1a/48.png" class="avatar"> Marek57:</div>
<blockquote>
<p>if I select a NEW small volume (I have tried 50^3 to 400^3) from the disk then they open without any problem</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Marek57" data-post="5" data-topic="40041">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e68b1a/48.png" class="avatar"> Marek57:</div>
<blockquote>
<p>however, when I try to open ANY file, even a small one (50^3) - from a list or disk then Slicer silently crashes (disappears/closes)</p>
</blockquote>
</aside>
<p>Please provide step-by-step instructions for reproducing <code>I try to open ANY file, even a small one (50^3) - from a list or disk then Slicer silently crashes</code>. Share the file that you are trying to load (upload to dropbox/onedrive/etc. and post the link here).</p>

---

## Post #7 by @Marek57 (2024-12-03 10:56 UTC)

<p>I am back again.<br>
The problem seems to persist.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> - regarding you last questions:<br>
I meant opening any (even very small) volume AFTER having (successfully) opened a large one leads to crash.</p>
<p>Now I cannot open ANY dataset (regardless of the size).<br>
After Windows update I am getting a new phenomenon, which might shed light on the problem:<br>
instead of closing the software, a message appears saying<br>
<em>“An unhandled win32 exception occured in Slicer App-real.exe”</em>.<br>
After activating a debugger the following further information is given:<br>
“<em>Unhandled exception at 0x00007FFC21FA7438 (Qt5Gui.dll) in SlicerApp-real.exe: 0xC00000FD: Stack overflow (parameters: 0x0000000000000001, 0x0000006FF3CD3000).</em>”</p>
<p>Any idea?<br>
Thank you in advance!</p>

---
