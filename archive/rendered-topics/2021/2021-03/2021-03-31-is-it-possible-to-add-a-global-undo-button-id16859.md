# Is it possible to add a global undo button?

**Topic ID**: 16859
**Date**: 2021-03-31
**URL**: https://discourse.slicer.org/t/is-it-possible-to-add-a-global-undo-button/16859

---

## Post #1 by @slicer365 (2021-03-31 02:09 UTC)

<p>Sometimes during the process, I accidentally moved the model and wanted to return it. I found it difficult. I had to move it back manually, but it was not very accurate.Of course, there are still many situations. If there is a global Undo tool or Go back to the previous step in editing menu, it will be very good .Like this picture.<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b598d9161b7907df3a098161830c377f0dd76d3.jpeg" alt="捕获" data-base62-sha1="hBcAUgmMoxBZfpu6U5zhMjhuFsD" width="449" height="352"></p>

---

## Post #2 by @timeanddoctor (2021-03-31 04:32 UTC)

<p>the function like 3matic in 3d slicer is the segmentEditor, you can undo or redo in this module.<br>
And there are many more function in slicer just like the ITK/VTK, some processing can  not be redo…</p>

---

## Post #3 by @lassoan (2021-04-03 03:18 UTC)

<p>We used to have a global undo/redo operation in Slicer but as many features were added it was hard to keep it working correctly, so it got hidden.</p>
<p>We plan to re-enable it for specific node types (<a href="https://github.com/Slicer/Slicer/issues/4576">markups</a>, transforms), but there is no specific timeline.</p>
<p>Add a comments below describing what node types you would like to undo and why it is particularly important.</p>

---

## Post #4 by @ga1g (2023-08-26 07:33 UTC)

<p>Hello,<br>
Slicer is great!<br>
The most important feature for me as a beginner is an undo for color selecting in volume as well as volume rendring.<br>
Some times it takes a lot of time to find the right adjusments and by clicking “Auto” in “volume” module or “suncronize with volume module” in “volume rendring” module just loose evrything…<br>
So undo for colors is appreciated. Hope it is not too complicated…</p>
<p>Thank<br>
Gal.</p>

---

## Post #5 by @lassoan (2024-06-27 02:27 UTC)

<p>Making it possible to undo any operations on any node types would be challenging. However, we could enable undo for a few nodes types (at least to get started).</p>
<p><strong>What node changes would you like to be able to undo?</strong><br>
(you can select up to 3)</p>
<div class="poll" data-poll-charttype="bar" data-poll-max="3" data-poll-min="1" data-poll-name="poll" data-poll-public="true" data-poll-results="always" data-poll-status="open" data-poll-type="multiple">
<div class="poll-container">
<ul>
<li data-poll-option-id="e461f11007048033c70e33b4bdcff747">Markup (point list, line, curve, ROI, …)</li>
<li data-poll-option-id="d7faa13be73f2ff33631a139c51b56e8">Transform</li>
<li data-poll-option-id="316e83274008ec3ec1195b23be1d37e0">Table</li>
<li data-poll-option-id="a7a0f11bfca840786fedc4617c011f8e">Text</li>
<li data-poll-option-id="04d043ffda2014563e7310bc6aba89d5">Segmentation</li>
<li data-poll-option-id="1d05e2623ad36a76cfc3516cba864ba5">Volume (CR, MRI, …)</li>
<li data-poll-option-id="4ae8c3aa4b28a8772eba8842160832c5">Label volume</li>
<li data-poll-option-id="69b92ab651156b7d6909dfdf5c30a5f9">Model</li>
<li data-poll-option-id="3ecf5d307de008040643fd4cd7c0f0a3">Display (that stores color, visibility, etc. properties)</li>
<li data-poll-option-id="f75aa6c49357665c02093239deca6461">View (slice position, field of view, background color, …)</li>
<li data-poll-option-id="c40c16af3482ce5a337e3cca9afd0f4e">Color table</li>
</ul>
</div>
<div class="poll-info">
<div class="poll-info_counts">
<div class="poll-info_counts-count">
<span class="info-number">0</span>
<span class="info-label">voters</span>
</div>
</div>
</div>
</div>

---

## Post #6 by @lassoan (2024-06-29 01:19 UTC)

<p>Everyone who voted for this feature: please complete the poll above.</p>
<p>Please also ask your colleagues, collaborators, etc. to vote on features. There are about 9000 people on this forum and only a couple dozen has voted so far.</p>

---

## Post #7 by @zifangx (2024-12-10 17:23 UTC)

<p>Hi,</p>
<p>Thanks for making the undo/redo button available to the Markup module, I was able to get the buttons back to the 3D Slicer interface following <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/" rel="noopener nofollow ugc">this</a> instruction.<br>
Just wanted to report on a bug: I discovered that it almost always crashes the session when I hit Undo on an open curve that’s constrained to a model (unconstrained curves have no problem at all).<br>
Otherwise, it’s been working well.</p>
<p>Thanks,<br>
Zifang</p>

---

## Post #8 by @chir.set (2024-12-10 21:15 UTC)

<aside class="quote no-group" data-username="zifangx" data-post="7" data-topic="16859">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zifangx/48/77050_2.png" class="avatar"> zifangx:</div>
<blockquote>
<p>it almost always crashes the session when I hit Undo on an open curve that’s constrained to a model</p>
</blockquote>
</aside>
<p>I tested <a href="https://gitlab.com/chir-set/RcHacks7/-/blob/900664b75fca04210a065f1324d7fae0214eb559/14-UndoRedo.py.txt" rel="noopener nofollow ugc">this</a> implementation that <em>derives</em> from the <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/" rel="noopener nofollow ugc">original</a> work you linked and did not observe any crash in the scenario you described. May be you could give it a try.</p>

---
