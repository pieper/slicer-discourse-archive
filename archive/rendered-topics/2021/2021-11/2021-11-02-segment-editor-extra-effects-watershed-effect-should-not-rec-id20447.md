# Segment Editor : Extra Effects — Watershed effect should not recompute upon change of colour

**Topic ID**: 20447
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/segment-editor-extra-effects-watershed-effect-should-not-recompute-upon-change-of-colour/20447

---

## Post #1 by @DIV (2021-11-02 02:12 UTC)

<p>The <em>Watershed</em> (extra) effect in the <strong>Segment Editor</strong> module appeared to recompute upon a change of a segment’s colour (aka “color”), or possibly it was the segment’s <code>Property type</code>.  This seemed to happen automatically when “Auto-update” was ticked.  …Then later I couldn’t reproduce it.<br>
While recomputation is justified when changing the ‘content’ of a segment (adding or removing voxels through <em>Paint</em> or <em>Erase</em> effects), it shouldn’t be triggered by ‘æsthetic’ changes such as change of colour or renaming.</p>
<p>In trying to reproduce the above issue, a different issue arose:  when I changed a segment’s colour and name, the new colour was applied to the painted voxels, but the previewed regions expanded through the watershed algorithm remain at the old colour, and also the old name shows up in the <em>Data Probe</em> panel.  The updated colour and name should be applied to the previewed regions too.</p>
<p>Possibly some of this might apply to the <em>Grow from Seeds</em> effect too (untested).</p>
<p>—DIV</p>

---

## Post #3 by @DIV (2021-11-02 05:15 UTC)

<p>It does seem kind of similar in the <em>Grow from Seeds</em> effect too.<br>
The original initialisation took dozens of seconds.<br>
Changing the colour required some sort of recomputation for a few seconds, but maybe it’s just recomputation for the graphical display (including 3D)?<br>
Also the colours did not update in the preview, even after clicking <code>Update</code>.<br>
Updating of colours could be forced only by clicking <code>Cancel</code>, and then <code>Update</code> again.<br>
—DIV</p>

---

## Post #4 by @DIV (2021-11-02 05:43 UTC)

<p>In the <em>Grow from Seeds</em> effect I am also getting a long recomputation (dozens of seconds) after adjusting the <code>Seed locality</code> slider value, even though <code>Auto-update</code> of the preview is unticked.  This is a genuine recomputation of the segments, as the preview also changes noticeably.</p>
<p>Maybe due to this behaviour from the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#grow-from-seeds" rel="noopener nofollow ugc"><strong>Segment Editor</strong> module’s documentation</a>:  “<em>Master volume and auto-complete method will be locked after initialization</em>”.</p>

---

## Post #5 by @lassoan (2021-11-02 20:26 UTC)

<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20447">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>The <em>Watershed</em> (extra) effect in the <strong>Segment Editor</strong> module appeared to recompute upon a change of a segment’s colour (aka “color”), or possibly it was the segment’s <code>Property type</code> . This seemed to happen automatically when “Auto-update” was ticked. …Then later I couldn’t reproduce it.<br>
While recomputation is justified when changing the ‘content’ of a segment (adding or removing voxels through <em>Paint</em> or <em>Erase</em> effects), it shouldn’t be triggered by ‘æsthetic’ changes such as change of colour or renaming.</p>
</blockquote>
</aside>
<p>We could probably be do more sophisticated change analysis and perform less recomputations in response to segment changes. However, considering how infrequently users are expected to change segment colors or other properties during region growing seed painting, implementing of such optimizations would be assigned a very low priority.</p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20447">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>In trying to reproduce the above issue, a different issue arose: when I changed a segment’s colour and name, the new colour was applied to the painted voxels, but the previewed regions expanded through the watershed algorithm remain at the old colour, and also the old name shows up in the <em>Data Probe</em> panel. The updated colour and name should be applied to the previewed regions too.</p>
</blockquote>
</aside>
<p>I agree that there is room for improvement here, but this issue (and the others in your follow-up comments). You can submit them as feature requests on the issue tracker to keep track of them, but since they would be classified as low impact, low/medium workload tasks, most likely they would go into the backlog and only be implemented if there is specific funding attached or a volunteer chooses to implement them. So, it may be sufficient to just keep these improvement ideas here on the forum.</p>

---
