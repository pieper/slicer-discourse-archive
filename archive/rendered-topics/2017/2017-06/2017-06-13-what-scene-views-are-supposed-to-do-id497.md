# What scene views are supposed to do?

**Topic ID**: 497
**Date**: 2017-06-13
**URL**: https://discourse.slicer.org/t/what-scene-views-are-supposed-to-do/497

---

## Post #1 by @lassoan (2017-06-13 19:58 UTC)

<p>We experienced many problems related to scene views, seen many workarounds in many places in the code, and there are many open issues caused by or related to scene views.</p>
<p>The main problem seems to be that it is unclear what information scene views should store and restore.</p>
<p><strong>Should it be enough for scene views to store display information of nodes, view layout, view settings, and camera settings?</strong></p>
<p>If that’s true, we could simplify the scene view implementation a lot, because we would not need to deal with storable nodes (display, camera, etc. nodes are always stored in the scene). We could also delete display properties of nodes that are removed from the scene.</p>

---

## Post #2 by @pieper (2017-06-13 20:23 UTC)

<p>+1 for simplifying scene views.  I agree with your analysis of the complexity of the current approach.</p>

---

## Post #3 by @jcfr (2017-06-13 20:39 UTC)

<p>If still think scene views (or snapshots)  are useful, they allow to capture different state of a workflow.</p>
<p>What would be needed is the notion of implicit sharing and copy on write for storable node.</p>
<p>This also means that if the same dataset is loaded multiple times, the dataset would be effectively in memory only once (until it is effectively modified).</p>
<p>This could be addressed at the itkImage/vtkImage level. or further up the stack at the node level.</p>

---

## Post #4 by @lassoan (2017-06-13 22:39 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="3" data-topic="497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This also means that if the same dataset is loaded multiple times, the dataset would be effectively in memory only once (until it is effectively modified).</p>
</blockquote>
</aside>
<p>This is what the scene undo/redo mechanism does.</p>
<p>There are a couple of scene state management mechanisms:</p>
<ul>
<li>To demonstrate going through a processing a workflow, it is much simpler and safer to save each state as a separate scene.</li>
<li>If you want to capture different time points, you can use Sequences module.</li>
<li>To show different views of the same data, there is the current Scene views infrastructure.</li>
<li>For scene state snapshots, there is the (now mostly hidden) undo/redo infrastructure.</li>
<li>There is undo/redo stack in Editor and Segment editor for labelmap and segmentation nodes.</li>
</ul>
<p>I’m not sure if we need to extend snapshots in addition to all these existing mechanisms for scene state management (scene views never saved storable nodes, so they were never usable for generic scene state management).</p>

---

## Post #5 by @fedorov (2017-06-13 22:58 UTC)

<p>I love the title of this thread! I was struggling with this question when I started using Slicer 3, never found the answer, despite many attempts, and decided to just ignore the existence of this “feature”.</p>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Should it be enough for scene views to store display information of nodes, view layout, view settings, and camera settings?</p>
</blockquote>
</aside>
<p>Yes!</p>
<p>Ironically, this is essentially what I suggested about 10 years ago to Ron, Steve and Nicole! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @pieper (2017-06-13 23:53 UTC)

<p>Don’t forget there were other people involved in the implementation - I<br>
won’t name names!</p>

---

## Post #7 by @jcfr (2017-06-13 23:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are a couple of scene state management mechanisms:</p>
<p>To demonstrate going through a processing a workflow, it is much simpler and safer to save each state as a separate scene.</p>
</blockquote>
</aside>
<p>Agreed. It is not worth the complexity of managing complete scene within an existing scene.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you want to capture different time points, you can use Sequences module.<br>
To show different views of the same data, there is the current Scene views infrastructure.<br>
For scene state snapshots, there is the (now mostly hidden) undo/redo infrastructure.<br>
There is undo/redo stack in Editor and Segment editor for labelmap and segmentation nodes.</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=12" title=":thumbsup:" class="emoji only-emoji" alt=":thumbsup:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @jcfr (2017-06-13 23:56 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Ironically, this is essentially what I suggested about 10 years ago to Ron, Steve and Nicole! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="497" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Don’t forget there were other people involved in the implementation - I<br>
won’t name names!</p>
</blockquote>
</aside>
<p>The good news is that based on what we learnt we are moving forward and improving the platform <img src="https://emoji.discourse-cdn.com/twitter/fireworks.png?v=12" title=":fireworks:" class="emoji" alt=":fireworks:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @cpinter (2017-06-14 07:21 UTC)

<p>I agree that the feature set of the scene views should be better defined, and it should be made sure that the new feature set works correctly. I spent several days adding scene view support when rewriting subject hierarchy earlier this year, and it struck me that the only thing I needed to support in SH for scene views did not work (which I thought was basically re-adding removed nodes and removing new nodes - as display options are not stored in SH, these were the focus for me that time), but there was a mechanism for this and it was quite complex. So the same question popped up in my head: what is it supposed to do?</p>
<p>Based on my earlier conversations with people, I think it is mostly used for demonstrations/tutorials, so Sonia and Ron should definitely be asked.</p>
<p>My own opinion is that handling display properties should be enough. Cameras, display nodes, layouts, slice composite nodes, etc.<br>
What about hierarchies though? They are in some sense display properties, and for models and annotations, those are actual nodes we need to handle. For SH, it is only one node that needs to be replaced (and then validated).</p>

---

## Post #10 by @lassoan (2017-06-15 03:24 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="9" data-topic="497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>What about hierarchies though? They are in some sense display properties, and for models and annotations, those are actual nodes we need to handle. For SH, it is only one node that needs to be replaced (and then validated).</p>
</blockquote>
</aside>
<p>I would not save hierarchy nodes if at all possible. Is there any information in a hierarchy node that you think would be useful to capture in a scene view? Maybe the “Force color to children” setting (Expanded property)?</p>

---

## Post #11 by @cpinter (2017-06-15 07:08 UTC)

<p>I mainly meant the hierarchy itself. Parents-children. I don’t see a huge need to preserve this information, but to me the hierarchies seem like a kind of display properties of the already loaded data. Good point about the force color option as well.</p>
<p>Handling the hierarchies would keep some of the complexity of the scene view implementation we want to get rid of, so we should only consider this if others think it is important. I brought this up because this thread is about re-design, and this may be something to consider.</p>

---

## Post #12 by @pieper (2017-06-15 13:05 UTC)

<p>I’d like to see us come up with a concrete definition of a scene view (or<br>
if needed a new name for a new concept).</p>
<p>Functionally I’d say that creating a scene view is like saving an mrb, and<br>
that switching to a scene view should be equivalent to closing one scene<br>
and opening another.  Then the only real question is how to make this<br>
efficient by reusing data that is already loaded in memory.  This<br>
definition provides an easily testable baseline (which the current<br>
implementation doesn’t meet).</p>

---

## Post #13 by @lassoan (2017-06-15 14:51 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Functionally I’d say that creating a scene view is like saving an mrb</p>
</blockquote>
</aside>
<p>What would be the use case for this? For reviewing an atlas or a surgical plan you would not need a complete copy of all nodes - changing visualization settings (display nodes, view nodes, composite nodes, maybe hierarchy nodes) would be enough.</p>
<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>equivalent to closing one scene<br>
and opening another</p>
</blockquote>
</aside>
<p>Closing the scene means that we lose all node references (nodes that you selected in modules), so a scene view restore would be a huge, breaking change in the scene (you would need to set up everything again).</p>
<p>However, if we just update existing nodes in the scene, it would be very difficult to do it correctly for all nodes: node references and adding/removal of nodes between scene views is particularly tricky. Correct management of large storable nodes would be very difficult to implement, too.</p>

---

## Post #14 by @pieper (2017-06-15 17:09 UTC)

<p>If there’s a fuzzy line about what gets reset and what doesn’t when a scene<br>
view changes it’s going to continue to be problematic.</p>
<p>In terms of module selections that’s not a problem if they have parameter<br>
nodes (like CLIs).</p>

---

## Post #15 by @fedorov (2017-06-15 17:18 UTC)

<p>Related issue from 5 years back!!</p>
<p><a href="https://issues.slicer.org/view.php?id=1869" class="onebox" target="_blank">https://issues.slicer.org/view.php?id=1869</a></p>

---

## Post #16 by @lassoan (2017-06-15 17:28 UTC)

<p>If you follow the close scene rule then those parameter nodes will be deleted when you restore a previous scene view.</p>
<p>I think we can define a clear line: we restore content of all display nodes and view nodes (and potentially hierarchy nodes). If we limit the types of nodes that we support then we can ensure correct save/restore behavior. The behavior will be also very simple if we don’t support adding/removing nodes (we just hide anything that we don’t want to show) and saving/restoring content from files (all saved/restored data can be stored in xml string).</p>

---

## Post #17 by @pieper (2017-06-15 18:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you follow the close scene rule then those parameter nodes will be deleted when you restore a previous scene view.</p>
</blockquote>
</aside>
<p>Yes, that’s the point - you get the parameter nodes from the other scene view that were in effect when it was created.</p>
<p>But what you are describing to just save view and display nodes could work.  When you restore you can ignore anything that doesn’t apply (like display nodes for data that has been deleted).  There will need to be graceful handling of data that’s been added since the view was created.</p>

---
