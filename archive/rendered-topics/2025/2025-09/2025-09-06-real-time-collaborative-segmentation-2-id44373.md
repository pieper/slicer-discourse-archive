# Real-time collaborative segmentation #2

**Topic ID**: 44373
**Date**: 2025-09-06
**URL**: https://discourse.slicer.org/t/real-time-collaborative-segmentation-2/44373

---

## Post #1 by @gregsharp.geo (2025-09-06 16:52 UTC)

<p>Hello friends.  Good to be back.</p>
<p>I read the topic ( <a href="https://discourse.slicer.org/t/adding-near-real-time-collaborative-manual-segmentation/29255" class="inline-onebox">Adding near-real time collaborative manual segmentation</a> ) with interest, and it partly answered my questions.  But it seems maybe different use case, so I started a new topic.</p>
<p>Is Slicer a good platform for collaborative (desktop, no VR) manual segmentation?  Two users would edit segmentations simultaneously in the same scene, with near real-time update, and maybe a third view-only workstation.  The VNC solution seems not be suitable; but maybe this is possible through OpenIGTLink?</p>
<p>Also, what is the current state of Slicer dual screen?</p>

---

## Post #2 by @muratmaga (2025-09-06 17:09 UTC)

<aside class="quote no-group" data-username="gregsharp.geo" data-post="1" data-topic="44373">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/6bbea6/48.png" class="avatar"> gregsharp.geo:</div>
<blockquote>
<p>Is Slicer a good platform for collaborative (desktop, no VR) manual segmentation? Two users would edit segmentations simultaneously in the same scene, with near real-time update,</p>
</blockquote>
</aside>
<p>Slicer is a great platform for collaborative segmentation. but what’s the use case for <strong>simultaneous segmentation with near real-time update?</strong> Also are segmenters segmenting the same structure or adjacent structures (but not the same thing)?</p>
<p>If you give more information we can give more to do the point feedback.</p>
<aside class="quote no-group" data-username="gregsharp.geo" data-post="1" data-topic="44373">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/6bbea6/48.png" class="avatar"> gregsharp.geo:</div>
<blockquote>
<p>Also, what is the current state of Slicer dual screen?</p>
</blockquote>
</aside>
<p>You can dock out the module pane, python console and log and move them to a second screen, but the main application window (with viewers) will be on a single monitor.</p>

---

## Post #3 by @pieper (2025-09-06 17:32 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/waving_hand.png?v=14" title=":waving_hand:" class="emoji" alt=":waving_hand:" loading="lazy" width="20" height="20"> <a class="mention" href="/u/gregsharp.geo">@gregsharp.geo</a></p>
<p>Here’s an experiment to test the multiscreen idea.  It would be pretty easy to make something like this a core feature.</p>
<pre><code class="lang-auto">w = qt.QWidget()
w.setLayout(qt.QVBoxLayout())
t = slicer.app.layoutManager().threeDWidget(0)
w.layout().addWidget(t)
w.show()
</code></pre>
<p>For collaborative segmentation projects, <a class="mention" href="/u/muratmaga">@muratmaga</a> and I have been working on <a href="https://github.com/MorphoCloud/SlicerMorphoDepot">MorphoDepot</a> which aims to handle the bookkeeping.  I could imagine adding some realtime features, but like Murat I’m not sure I see the use case.</p>

---

## Post #4 by @gregsharp.geo (2025-09-06 17:56 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="44373">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Slicer is a great platform for collaborative segmentation. but what’s the use case for <strong>simultaneous segmentation with near real-time update?</strong> Also are segmenters segmenting the same structure or adjacent structures (but not the same thing)?</p>
</blockquote>
</aside>
<p>Yes of course.  My use case is adaptive radiotherapy (RT).</p>
<p>In North America 2025, a small subset (&lt;1%) of RT procedures have become more like surgery. We plan and treat on the spot. Traditional RT uses a pre-planned radiation plan every day, adjusting only for patient translation and rotation.</p>
<p>In 2025, these adaptive treatments are perhaps 45 minutes with perhaps 4-5 persons (including a physician).  A traditional treatment is perhaps 15 minutes with perhaps 2-3 persons (and no physician).  Adaptive RT is high quality, but access is limited due to cost.</p>
<p>The goal would be for to allow a smaller non-physician team (two people) to segment avoidance structures at the same time, reducing the treatment time.  Physician would come at the end, review and edit if needed, and then we treat within 20 mins.</p>

---

## Post #5 by @pieper (2025-09-06 18:34 UTC)

<p>This is a great use case Greg.  Have you tried nnInteractive to speed up the segmentation?</p>
<p>Also, given the results we’ve seen in other fields, I think we would be able to train AI models for this task given a decent set of ground truth segmentations.</p>

---
