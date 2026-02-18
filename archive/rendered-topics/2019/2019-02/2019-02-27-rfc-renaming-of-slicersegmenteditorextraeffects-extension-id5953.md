# RFC: Renaming of SlicerSegmentEditorExtraEffects extension

**Topic ID**: 5953
**Date**: 2019-02-27
**URL**: https://discourse.slicer.org/t/rfc-renaming-of-slicersegmenteditorextraeffects-extension/5953

---

## Post #1 by @jcfr (2019-02-27 21:10 UTC)

<p>Sharing here a suggestion from <a class="mention" href="/u/hherhold">@hherhold</a>:</p>
<blockquote>
<p><code>Segment Editor Extra Effects</code> could probably be renamed <code>Segment Editor Essential Effects</code></p>
</blockquote>
<p>See <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" class="inline-onebox">GitHub - lassoan/SlicerSegmentEditorExtraEffects: Many additional segmentation tools for 3D Slicer's Segment Editor</a></p>

---

## Post #2 by @lassoan (2019-02-27 21:14 UTC)

<p>Essential effects are bundled with Slicer. These are experimental effects - not fully tested or optimized. So, if we changed the name then it should reflect that. Also, a new name must be <em>much</em> better than the previous name to justify all the complications the renaming causes (people cannot find extensions, instructions on Slicer forum becomes obsolete that refer to the old name, extension dependencies break, etc.).</p>

---

## Post #3 by @cpinter (2019-02-27 21:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="5953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Essential effects are bundled with Slicer</p>
</blockquote>
</aside>
<p>Exactly. The extension contains very useful but supplementary (and not as tested) effects. I don’t even understand how “essential” would be a good descriptor for those effects. Do you know Jc what is the idea behind it?</p>

---

## Post #4 by @hherhold (2019-02-27 21:36 UTC)

<p>It just came from a blog post I’m writing up on the use of Slicer in entomology. I use the Editor Extra Effects, and just as an aside commented that they’re really more “Essential” than extra - I didn’t mean to open up a can of worms!</p>

---

## Post #5 by @jcfr (2019-02-27 21:58 UTC)

<blockquote>
<p>I didn’t mean to open up a can of worms!</p>
</blockquote>
<p>Ooop. I take the blame on opening the can then <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<p>Anyway I think the comments of <a class="mention" href="/u/lassoan">@lassoan</a> are general and will be useful in the future.</p>

---

## Post #6 by @cpinter (2019-02-27 22:04 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="5953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>they’re really more “Essential” than extra</p>
</blockquote>
</aside>
<p>In this sense I agree with you - that some of them are really necessary. I always install it. Maybe instead of renaming it we should move some of them to core?</p>
<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="5953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I didn’t mean to open up a can of worms</p>
</blockquote>
</aside>
<p>Not at all.</p>

---

## Post #7 by @lassoan (2019-03-14 00:06 UTC)

<p>Yes extra effects that prove to be widely useful and become stable enough should get into the core. The advantage of having work-in-progress effects in an extension is that it is easier to deliver fixes and improvements, even to the stable version of Slicer.</p>

---

## Post #8 by @fedorov (2019-03-14 15:03 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/hherhold">@hherhold</a> maybe the original request should instead be reformulated into something like “RFC: move effects X Y and Z from SegmentEditorExtraEffects to the core”.</p>

---

## Post #9 by @muratmaga (2019-03-14 18:57 UTC)

<p>I find these ‘extra’ effects very useful too. My suggestion is to include them as part of the core segment editor, and have a little button that reads 'Enable experimental effects" with additional acknowledgement that they are not as stable as the core effects. And gradually move them into ‘core’ functionality as they become more mature…</p>

---

## Post #10 by @lassoan (2019-03-14 19:12 UTC)

<p>There are some open issues with each of these effects that would need to be addressed before moving. Once an effect is in the Slicer core, it is harder to fix and improve (especially in stable builds).</p>
<p>Some of them are close to be ready, for example Mask volume effect could be moved after the issues listed here are resolved: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/issues/10" rel="nofollow noopener">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/issues/10</a>. As always, contributions are welcome: if someone can implement these and send a pull request then it could get into the Slicer core within a few days.</p>

---

## Post #11 by @pieper (2019-03-14 19:23 UTC)

<p>Yes, or leave them as an extension but make them easy to install (and update) from within the Segment Editor.</p>

---

## Post #12 by @jamesobutler (2019-03-14 19:25 UTC)

<p>I agree there still needs to be an extension to install experimental effects to quickly fix issues.</p>
<p>It’s seems like part of the root issue is that the visibility of the extensions manager isn’t clear enough for users and users think segment editor effects are missing. So then they want these effects in core instead.</p>
<p>I don’t think installing extensions is an inconvenience and is a good way to prevent bloat in core. At least preview builds have the ability to quickly reinstall extensions from a previous install.</p>
<p>Ideas:</p>
<ul>
<li>Package SegmentEditorExtraEffects as an already installed extension for Slicer preview builds.</li>
<li>Add a button within the Segment Editor widget to “install experimental effects” which would install the extension without going through the extensions manager.</li>
</ul>

---
