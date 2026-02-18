# Locking the markups list

**Topic ID**: 17451
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/locking-the-markups-list/17451

---

## Post #1 by @smrolfe (2021-05-04 17:33 UTC)

<p>I’d like to add the ability to lock a markups list so no further points can be added (see discussion <a href="https://github.com/Slicer/Slicer/pull/5325" rel="noopener nofollow ugc">here</a>). Currently, there is a max number of points that limits the total allowed. When this number non-zero, a new markups node is generated when additional points are placed, and this happens automatically when in persistent placement mode. When working with landmark templates containing a pre-specified number of named points, this causes unneeded points and markup nodes placed in the scene.</p>
<p>I am wondering if this behavior is useful for other purposes or if it may make sense to always stop placement on reaching the max number? One option that would preserve the current functionality would be adding a new state to the max point property, such as -1, indicating that the max is fixed to the current number. Either way, I also plan to add a button to toggle this setting in the Markups control points menu.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> can you let me know if you have some advice on this?</p>

---

## Post #2 by @lassoan (2021-05-04 18:09 UTC)

<p>If you disable persistent placement then placement stops after you reached them maximum number of points in the markup. No new markup is created.</p>
<p>If you want to make multiple measurements (e.g., measure 10 diameters across a long structure). It makes measurement many times faster if you enable persistent placement, because then when you finished placing a line then you can immediately place the next one, without having to go to the toolbar with your mouse.</p>
<p>I agree that this behavior is inconvenient when you must enable persistent placement for other reasons, for example because you want to place many markups. While we could add a new “persistent” option variant that would control keeping placement mode active between markups, I would rather see an overall better model for creating and editing markups and points.</p>
<p>Needs to address in the interaction scheme:</p>
<ul>
<li>limiting maximum number of points in markup</li>
<li>ability to define, redefine, or add points for an existing markup (you already have a work-in-progress pull request for this)</li>
<li>keyboard shortcuts to activate/deactivate placement mode (moving the mouse to the toolbar is too disruptive)</li>
<li>improve the toolbar to make it more clear if we create a new markup or just adding a new point to an existing markup (for example, currently you need to switch to a different markup type and back, if you want to place multiple curves)</li>
</ul>
<p>Could you try to design an interaction scheme and toolbar + markups module GUI that would address these needs?</p>

---

## Post #3 by @smrolfe (2021-05-04 18:53 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> I’ll discuss this with our group and see if we can come up with a reasonable proposal.</p>

---

## Post #4 by @muratmaga (2021-05-04 22:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="17451">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It makes measurement many times faster if you enable persistent placement, because then when you finished placing a line then you can immediately place the next one, without having to go to the toolbar with your mouse.</p>
</blockquote>
</aside>
<p>I agree with this, but to me solution is not the persistent mode, but a keyboard action (like p) to drop a fiducial wherever the cursor is on the 2D/3D viewer(s). This becomes a two-handed workflow, where you interact with the scene via the mouse, and place points via keyboard.</p>
<p>Persistent mode makes only sense for fiducial nodes, have (almost) no relevance to other markup types, and works only when you primarily operate on the single static view. If you are going to rotate your 3D viewer, zoom in/out, switch slice views, the potential for complications (accidentally creating a fiducial), as well as the amount mouse clicks going in/out of placement mode  just doesn’t worth the effort.</p>
<p>Whether it is applicable or not, I am not sure, but there’s a prototype of this behavior in SlicerMorph (<a href="https://github.com/SlicerMorph/SlicerMorph/blob/ffb5b375dde7336557aaa91e121b203f132acd42/MorphPreferences/Resources/SlicerMorphRC.py#L151" class="inline-onebox">SlicerMorph/MorphPreferences/Resources/SlicerMorphRC.py at ffb5b375dde7336557aaa91e121b203f132acd42 · SlicerMorph/SlicerMorph · GitHub</a>)<br>
There are some issues with it. It is susceptible to high-resolution screen scaling problems (i.e., there might be an offset between where the cursor is vs the point dropped, which gets fixed if you login in/out of the session). I think the behavior is more intuitive then the persistent mode, and would like to see a better version of it supported in core slicer.</p>
<p><a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #5 by @lassoan (2021-05-04 22:46 UTC)

<p>I agree that there are many solutions to each problem of the current implementation. That’s why we should come up with a complete plan and not just one tweak to fix one of the pain points.</p>

---

## Post #6 by @muratmaga (2021-05-04 22:59 UTC)

<p>Sounds good. I believe <a class="mention" href="/u/smrolfe">@smrolfe</a> will join the next developer’s call to discus the proposed plan (and solutions).</p>

---

## Post #7 by @mikebind (2021-05-05 18:49 UTC)

<p>I like the keyboard press to place fiducial markup idea.  One possible approach to avoiding the high DPI scaling issues is to place the point at the intersection of the 3 slice views.  This location is unambiguous and well visualized, and for me, is usually where I want to drop my point. (The work is done to navigate to this point, and if I accidentally click somewhere else, that represents a placement error for me).  I very much appreciate that there are lots of possible workflows and that this scheme probably wouldn’t fit for others; I just wanted to throw it out as an additional idea to have in the mix.</p>

---

## Post #8 by @muratmaga (2021-05-05 19:12 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="7" data-topic="17451">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>One possible approach to avoiding the high DPI scaling issues is to place the point at the intersection of the 3 slice views</p>
</blockquote>
</aside>
<p>I find the slice views (particularly when all three are shown) are too obstructive in 3D view to actually locate the structure I want to LM. But apart from personal preferences, high DPI issue is sort of random, happens more on remote connections, or when you attached an external monitor to a laptop and it affects our other modules (such as MarkupEditor).</p>
<p>But it has been quite hard to consistently reproduce, and has been a challenge to find the actual sequence of events that trigger it. On windows 10, if you simply log off and on to the same session (without modifying your setup or resolution), it seems to fix itself.</p>

---

## Post #9 by @mikebind (2021-05-06 15:29 UTC)

<p>Sorry, <a class="mention" href="/u/muratmaga">@muratmaga</a>, I didn’t mean the slice intersection as visualized on the 3D view, I mean the slice intersection as seen on the slice views with the intersection cross-hairs on.  I am usually locating landmarks using the slice views rather than the 3D view. I am looking in multiple planes to make sure I am in the right spot, usually using the shift-key scrolling and then sometimes just regular scrolling in a slice view to check adjacent slices. Once I have decided the location is correct, it would be easier to just place the fiducial at the slice intersection than to try to accurately place a mouse click there (which is what I do now).   I realize that it would probably be fairly easy to set this up myself with a python keyboard shortcut, but I haven’t gotten around to figuring that out, which probably says something about how important it is to me :), but if the feature was available, I would use it.</p>

---

## Post #10 by @muratmaga (2021-05-06 16:52 UTC)

<p>Np. I think it we can reliably make this work, it should be real simple to do what you want to do.</p>
<p>I spent sometime yesterday, and on a windows laptop when display scaling is set to anything above 100% I can now reproducibly produce the incorrect offset between where cursor is and where the point is dropped. So that’s a start. <a href="https://github.com/SlicerMorph/SlicerMorph/issues/156" class="inline-onebox">Points placed incorrectly with the 'p' shortcut when display scaling is &gt;100 · Issue #156 · SlicerMorph/SlicerMorph · GitHub</a></p>
<p>M</p>

---

## Post #11 by @lassoan (2021-05-07 20:08 UTC)

<p>I don’t see screen resolution to be an issue, because at any point you can zoom in using the mouse wheel in any views without interfering with the placement. You can also use two views for placement, one that gives a good overview, and one that is zoomed in a lot. You can go to the area where you want to place the landmark using Shit+MouseMove (centered mode), then drop the landmark very accurately in the zoomed-in view. Currently, we don’t center 3D views, but we can easily enable that, if placement is mainly done in 3D views.</p>
<p>I would prefer activating the landmark placement with a shortcut, see verify the landmark’s name and position in other views, and then commit the placement by a single mouse click.</p>
<p>Regarding placement in slice intersection position: Slice intersection is not a well-defined position. If you have several view groups (e.g., 4-over-4 view) then there is an intersection for each group. The intersection may not exist or may not be a point (depending on the number, position, and orientation of slice views). It would be much simpler and more robust to place the markup at the current cursor position instead (the cursor position is changed when you move the mouse while you hold down Shift key). There is one global crosshair position in the scene, it exists regardless of the number or types of views, and the crosshair can be display in different styles (with various length and thickness options). You can make slice intersections move to the cursor position (by default non-centered jump is enabled), so often you don’t even realize that these are two different things.</p>
<p>We don’t need to choose between these placement options, but we can have separate keyboard shortcuts for:</p>
<ol>
<li>activating/deactivating placement mode</li>
<li>place point at current mouse pointer position</li>
<li>place mode at current crosshair position.</li>
</ol>

---

## Post #12 by @mikebind (2021-05-07 22:49 UTC)

<p>Those are excellent points, <a class="mention" href="/u/lassoan">@lassoan</a>.  In light of those, I agree that having a “place fiducial at slice intersection” position is not a good general-purpose option.   In the past, I found using the global “crosshair” indicator confusing as I was not really clear on what actions would move it and what would leave it where it was, so I haven’t even tried turning it on in a few years. For my use cases, I would be happy with the controls scheme you outline.</p>

---
