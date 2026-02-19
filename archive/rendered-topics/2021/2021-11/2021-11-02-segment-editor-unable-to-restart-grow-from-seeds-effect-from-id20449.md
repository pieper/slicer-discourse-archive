---
topic_id: 20449
title: "Segment Editor Unable To Restart Grow From Seeds Effect From"
date: 2021-11-02
url: https://discourse.slicer.org/t/20449
---

# Segment Editor: unable to restart Grow from Seeds effect from scratch if Volume deleted

**Topic ID**: 20449
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/segment-editor-unable-to-restart-grow-from-seeds-effect-from-scratch-if-volume-deleted/20449

---

## Post #1 by @DIV (2021-11-02 06:25 UTC)

<p>The <em>Grow from Seeds</em> effect in the <strong>Segment Editor</strong> module has a couple of quirky points.</p>
<p>First is one small matter:  it only considers seeds for <code>Segments</code> that are toggled visible (in the current <code>Segmentation</code>).  Actually this is not a bad thing.  The problem for me is that I didn’t see it mentioned in the GUI.  Frankly speaking, I didn’t notice it at first in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#grow-from-seeds" rel="noopener nofollow ugc">documentation for the <strong>Segment Editor</strong> module</a> either, although eventually I see that it does say “<em>Only visible segments are used by this effect.</em>”.  Perhaps just one word could be inserted in the GUI to address this:<br>
“<code>Minimum two segments are required</code>”<br>
could be amended to<br>
“<code>Minimum two visible segments are required</code>”.</p>
<p>Secondly, it seems that there is a kind of ‘dead end’ created when the preview <code>Volume</code> is deleted through the <strong>Data</strong> module.<br>
Eventually I discovered the following workflow:</p>
<ol>
<li>(a) Paint seeds in many segments.  (b) Toggle visibility of some relevant segments off.</li>
<li>Set up <em>Grow from Seeds</em> effect by clicking <code>Initialize</code>.  This produces ‘wrong’ results in the preview <code>Volume</code>.</li>
<li>Click <code>Cancel</code> in the <em>Grow from Seeds</em> effect’s panel.</li>
<li>Toggle visibility of all relevant segments on.</li>
<li>Set up <em>Grow from Seeds</em> effect anew by clicking <code>Initialize</code> again.  This produces ‘right’ results.</li>
</ol>
<p>But there is a problem here:</p>
<ol>
<li>[as above]</li>
<li>[as above]</li>
<li>(a) Delete the preview <code>Volume</code> in the <em>Subject heirarchy</em> tab of the <strong>Data</strong> module.  (b) <strong>The <code>Cancel</code> button in the <em>Grow from Seeds</em> effect’s panel is disabled</strong>.</li>
<li>[as above]</li>
<li>Set up <em>Grow from Seeds</em> effect anew by clicking <code>Initialize</code> again.  <strong>This produces the same ‘wrong’ results as before, because <code>Cancel</code> was not clicked.</strong>
</li>
</ol>
<p>—DIV</p>

---

## Post #2 by @lassoan (2021-11-02 19:58 UTC)

<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Perhaps just one word could be inserted in the GUI to address this:</p>
</blockquote>
</aside>
<p>We host the Slicer documentation on github and welcome any suggestions there. Click on the “Edit on github” button on the top-right corner to edit the file and create a pull request from the suggested changes automatically.</p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Secondly, it seems that there is a kind of ‘dead end’ created when the preview <code>Volume</code> is deleted through the <strong>Data</strong> module.</p>
</blockquote>
</aside>
<p>It was obvious for the developers that the user must not delete the preview volume, but maybe not for all users. If you think that adding a note to the documentation would help then please add it. However, probably it would be better to make the effect more resilient. You can add submit a feature request to the <a href="https://github.com/Slicer/Slicer/issues">issue tracker</a> about this and someone will get to it eventually (you could volunteer, too).</p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<ul>
<li>Paint seeds in many segments. (b) Toggle visibility of some relevant segments off.</li>
<li>Set up <em>Grow from Seeds</em> effect by clicking <code>Initialize</code> . This produces ‘wrong’ results in the preview <code>Volume</code> .</li>
</ul>
</blockquote>
</aside>
<p>This is the intended, good, and useful behavior. Always using all segments for “Grow from seeds” would seriously limit what you can do with it. We already documented the behavior in that short sentence and rely on this in several tutorials, but maybe we should further explain it in the documentation with examples?</p>

---

## Post #3 by @DIV (2021-11-04 01:56 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="20449" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Perhaps just one word could be inserted in the GUI to address this:</p>
</blockquote>
</aside>
<p>We host the Slicer documentation on github and welcome any suggestions there. Click on the “Edit on github” button on the top-right corner to edit the file and create a pull request from the suggested changes automatically.</p>
</blockquote>
</aside>
<p>I had a go, but accidentally clicked the <code>Enter</code> button before I’d finished describing the change (or verifying what I’d actually changed).<br>
I couldn’t see how to edit a Pull Request, but maybe it’s alright.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="20449" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Secondly, it seems that there is a kind of ‘dead end’ created when the preview <code>Volume</code> is deleted through the <strong>Data</strong> module.</p>
</blockquote>
</aside>
<p>It was obvious for the developers that the user must not delete the preview volume, but maybe not for all users. If you think that adding a note to the documentation would help then please add it. However, probably it would be better to make the effect more resilient. You can add submit a feature request to the <a href="https://github.com/Slicer/Slicer/issues" rel="noopener nofollow ugc">issue tracker</a> about this and someone will get to it eventually (you could volunteer, too).</p>
</blockquote>
</aside>
<p>For me deleting the preview volume (after I discovered its existence) <em>seemed</em> to be the most conclusive course of action, because (in my mind) once it was gone, there couldn’t be any trace of the previous initialisation remaining.  Compared with an (in my mind) ‘anonymous’ <code>Cancel</code> button for which I wasn’t too sure what precisely was being “cancelled”.<br>
I agree with you that in this matter changing the documentation would be more of a stopgap, and a better solution would be to make the software more robust. For that I can suggest two alternative options:</p>
<ol>
<li>Deleting the preview volume automatically invokes all of the actions that would have been invoked by clicking <code>Cancel</code>.  The <code>Cancel</code> button becomes disabled/inactive upon completion.  (<em>Preferred</em>)</li>
<li>Deleting the preview volume does not have any further consequences.  The <code>Cancel</code> button remains enabled/active upon completion.  (<em>Less preferred</em>)</li>
</ol>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="20449" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group quote-modified" data-username="DIV" data-post="1" data-topic="20449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<ul>
<li>Paint seeds in many segments. (b) Toggle visibility of some relevant segments off.</li>
</ul>
<blockquote>
<ul>
<li>Set up <em>Grow from Seeds</em> effect by clicking <code>Initialize</code> . This produces ‘wrong’ results in the preview <code>Volume</code> .</li>
</ul>
</blockquote>
</blockquote>
</aside>
<p>This is the intended, good, and useful behavior. Always using all segments for “Grow from seeds” would seriously limit what you can do with it. We already documented the behavior in that short sentence and rely on this in several tutorials, but maybe we should further explain it in the documentation with examples?</p>
</blockquote>
</aside>
<p>Now that I understand what’s happening I can agree that it is indeed useful behaviour — at least when <em>irrelevant</em> segments are toggled off (although I had toggled off some <em>relevant</em> segments, which I tried to indicate in the enumerated workflows above).</p>
<p>It may be just me that missed the short sentence in the primary documentation on the first reading (but noticed it eventually).  I’ll take your word that it’s covered in the tutorials, which I either (for some) went through in the past and forgot that detail of, or else (for some others) did not go through.<br>
Perhaps with the small extra cue in the GUI (as suggested above) there <em>might not</em> be a need for further changes in the documentation, as the GUI provides the most ‘immediate’ guidance — unless several other users have also stumbled as I did.</p>

---
