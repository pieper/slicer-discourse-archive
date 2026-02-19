---
topic_id: 10694
title: "View Linking Design"
date: 2020-03-16
url: https://discourse.slicer.org/t/10694
---

# View linking design

**Topic ID**: 10694
**Date**: 2020-03-16
**URL**: https://discourse.slicer.org/t/view-linking-design/10694

---

## Post #1 by @kayarre (2020-03-16 03:02 UTC)

<p>I have figured out how to view different images that are linked. at least it  is working for the two over two view I am currently at.<br>
Where is the documentation explaining how it works? (to lazy to google)<br>
Also, I have been confused about how it works in the past, but now that I need to explain it to someone else, I think I need to know some more details.</p>
<p>If I change anything in the slice controller section of the View Controllers module while the views are linked all the linked views update to the same thing. e.g. selecting a different image, or the (Axial, Saggital, Coronal) view orientation, and 3d view visibility.</p>
<p>In the image panels,  moving one image moves the other images, and It appears that window level and window width are also linked?</p>
<p>Is there a way to toggle what “linking” means. e.g. when linking is turned on it can be defined accordingly to only sync a subset of the possible linkings?</p>
<p>An example might be that I have two views, and I want them to be linked for image views, but not linked when I change the image volumes.   lets say I want to visually inspect 4 different volumes with one other volume one at a time, but I don’t want a view that compares all 5 at the same time, I would need to toggle the linking every time I change the image volume?</p>
<p>current behavior:</p>
<ol>
<li>unlink</li>
<li>change image</li>
<li>re-link</li>
</ol>
<p>desired behavior:</p>
<ol>
<li>In a menu panel toggle off sync for everything but view sync</li>
<li>turn on link</li>
<li>change image volume</li>
</ol>

---

## Post #2 by @lassoan (2020-03-16 12:30 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="10694">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>Where is the documentation explaining how it works?</p>
</blockquote>
</aside>
<p>In general, such low-level internal mechanisms are not described in documentation separately from the code. You can rely on comments in the code and understand it by reading the code or execute step-by-step in a debugger, and if there are any particular details that you cannot figure out then you can ask here.</p>
<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="10694">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>It appears that window level and window width are also linked?</p>
</blockquote>
</aside>
<p>Image display window/level is stored in the volume’s display node. Usually you only have one display node for a volume, which is used in all views. So, window/level changes show up in all views, regardless of view link settings. [quote=“kayarre, post:1, topic:10694”]<br>
Is there a way to toggle what “linking” means. e.g. when linking is turned on it can be defined accordingly to only sync a subset of the possible linkings?<br>
[/quote]</p>
<p>You could only customize this by modifying Slicer source code. I don’t recall ever receiving requests for this, so we don’t plan to implement this feature.</p>
<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="10694">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>An example might be that I have two views, and I want them to be linked for image views, but not linked when I change the image volumes. lets say I want to visually inspect 4 different volumes with one other volume one at a time, but I don’t want a view that compares all 5 at the same time, I would need to toggle the linking every time I change the image volume?</p>
</blockquote>
</aside>
<p>When you have a very specific workflow in mind then you can implement that in your own module.  For example add a volume selector section in your module GUI that automatically disables/enables view sync.</p>
<p>You might also find view groups useful. Properties are only synchronized between views in the same group.</p>

---

## Post #3 by @muratmaga (2020-03-16 19:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Along this line, at least would be possible to synchronize the segmentation field of the slice view controllers with the <code>Segment Editor</code> and <code>Segmentation</code> modules. It gets confusing and possibly error prone, when you are working with multiple segmentations. This can be a one-way setting (e.g., controlled from Segment Editor, so when I switch a segment, it automatically alters the segmentation node being displayed in the viewer).</p>

---

## Post #4 by @lassoan (2020-03-18 03:11 UTC)

<p>In contrast to foreground, background, and label volume, there is no limitation on how many segmentations you display at the same time. We wanted to make the transition from labelmaps to segmentations easier, that’s why we added a small section to adjust segmentation display properties, but if you find it confusing then we could remove it and use Data module and Segmentations module to show/hide segmentations (similarly to models, markups, etc.).</p>

---
