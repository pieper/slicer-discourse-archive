# New sequnce building

**Topic ID**: 4204
**Date**: 2018-09-27
**URL**: https://discourse.slicer.org/t/new-sequnce-building/4204

---

## Post #1 by @Melanie (2018-09-27 08:03 UTC)

<p>Operating system: windows 10<br>
Slicer version:4.9<br>
Expected behavior:<br>
Actual behavior:<br>
How could I crop and merge two volume sequences please. If I have 100 frames (transformed from multivolume to image sequence) and I want to select 10 out of those and play together with a different 10 frames as one sequence so that I can use the same fiducial points in one sequence on the other. Also is there a way to save all fiducial points  frame by frame as fscv file automatically rather than saving frame by frame.</p>
<p>Thanks for the advice.</p>

---

## Post #2 by @Melanie (2018-09-27 14:58 UTC)

<p>HI Could someone kindly let me know why I cannot build up a new sequence from combining previously loaded 2 sequences please. I followed the steps on sequences document, but sequence browser does not play back the combined sequence. Is there any other tutorial or document to read please<br>
Thanks</p>

---

## Post #3 by @lassoan (2018-09-27 18:43 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="1" data-topic="4204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>How could I crop and merge two volume sequences please.</p>
</blockquote>
</aside>
<p>The only user interface for editing items in a sequence is the Sequences module. You can clip the sequence by selecting items and click the trashcan button. You can concatenate by selecting proxy node of the other sequence, then go to the first frame you want to add, click left-arrow button to add the frame to the selected sequence, switch to next frame (hit Ctrl+Shift+right-arrow key), click left-arrow button… and repeat the last two steps until you reach the last frame. These operations are tedious if you have more than a few ten frames, but you can automate this quite easily by Python scripting. In the future we plan to add a convenient module for clipping and merging - if you are interested in helping out with writing these simple Python scripted modules then let us know.</p>
<aside class="quote no-group" data-username="Melanie" data-post="2" data-topic="4204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>build up a new sequence from combining previously loaded 2 sequences</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Melanie" data-post="1" data-topic="4204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>play together</p>
</blockquote>
</aside>
<p>For synchronized replay of multiple sequences, you need to make sure all sequences have the exact same index name, unit, and type (you can set it in Sequences module). Index values must match be in the same range if index type is “numeric” (must match exactly if index type is “text”).</p>
<aside class="quote no-group" data-username="Melanie" data-post="1" data-topic="4204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>Also is there a way to save all fiducial points frame by frame as fscv file automatically rather than saving frame by frame</p>
</blockquote>
</aside>
<p>Yes, you can write a simple Python script to iterate through all sequence items and append markup point coordinates to a selected file. You can see a simple example of how to iterate through a sequence in <a href="https://github.com/SlicerRt/Sequences/blob/b1b2eeb7f8b33c728d5aeb983a605027a588f2bc/CropVolumeSequence/CropVolumeSequence.py#L197-L206">Crop volume sequence module</a>.</p>

---

## Post #4 by @Melanie (2018-09-27 18:54 UTC)

<p>Thank you very much Prof Lasso, I will try this. will reduce the number of frames and try. This has been very useful. I am happy to help in anyway I could, but from my questions you may understand that I am ‘0’ software. (trying to learn python as it looks very useful) But if I could make any contribution  like giving input about what options will be useful for research we do, I am more than happy to help in anyway I could.</p>

---

## Post #5 by @Melanie (2018-09-27 19:41 UTC)

<p>Sorry for continuing the thread. I did try this  but when I select the proxy node of the second sequence , I cannot get the frames that I clipped from the first sequence on the right hand box. Adding the whole second sequence does not work. Could you please advise whether I am doing some step wrong/ Thanks a lot</p>

---

## Post #6 by @lassoan (2018-09-27 20:17 UTC)

<p>In Sequences module, proxy node of the second sequence will only show up if the node type of the second sequence’s proxy node is the same as the type of nodes in the sequence that you are editing.</p>

---
