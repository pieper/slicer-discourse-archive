---
topic_id: 12981
title: "Markup Nodes Option For Locked Unlocked On Creation"
date: 2020-08-13
url: https://discourse.slicer.org/t/12981
---

# Markup nodes - option for locked/unlocked on creation?

**Topic ID**: 12981
**Date**: 2020-08-13
**URL**: https://discourse.slicer.org/t/markup-nodes-option-for-locked-unlocked-on-creation/12981

---

## Post #1 by @hherhold (2020-08-13 17:46 UTC)

<p>It looks like the default lock status for markup nodes is unlocked by default - looking in the vtkMRMLMarkupsNode() constructor, it sets Locked to 0 on the second line of code.</p>
<p>I almost never move markups, unless to move them back after creating them and accidentally moving them if they’re unlocked. I basically have added hitting the “lock all” button periodically to my workflow to make sure I don’t inadvertently move them around.</p>
<p>Is there a reason they’re unlocked by default? Would there be any interest in an option for toggling unlocked/locked on creation?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-08-13 18:05 UTC)

<p>As far as I can see, moving markup points is very common: most often you place it approximately in one view, potentially in 3D, then you verify and fine-tune the position in multiple, zoomed-in slice views. If that’s not your workflow then no problem, you can modify default properties of new nodes by specifying a default node - see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_all_slice_views_linked_by_default">examples in script repository</a>. You can put those few lines into your <code>.slicerrc.py</code> file to make it always the default on your computer.</p>

---

## Post #3 by @hherhold (2020-08-13 18:08 UTC)

<p>Ah, ok - that’s MUCH cleaner than my solution. Right now I have a hotkey set to place a fiducial, and in that function I run SetAllMarkupsLocked().</p>
<p>Thanks Andras! Hope you’re doing well.</p>
<p>-Hollister</p>

---

## Post #4 by @hherhold (2021-10-04 13:15 UTC)

<p>This is a <em>very</em> stale thread, sorry, but I’m finally getting to doing this the right way rather than my old hacky solution.</p>
<p>I’m trying to make a default markups node like this:</p>
<pre><code>defaultMarkupNode = slicer.vtkMRMLMarkupsNode()
defaultMarkupNode.SetLocked(1)
slicer.mrmlScene.AddDefaultNode(defaultMarkupNode)
</code></pre>
<p>but when I do this, new markups still show up as unlocked.  What am I doing wrong here?</p>
<p>THANKS!</p>
<p>-Hollister</p>

---

## Post #5 by @lassoan (2021-10-04 13:26 UTC)

<p>It is all good, you just need to create more concreate default node class(es). To prevent moving line node endpoints after placement:</p>
<pre><code class="lang-python">defaultMarkupNode = slicer.vtkMRMLMarkupsLineNode()
defaultMarkupNode.SetLocked(1)
slicer.mrmlScene.AddDefaultNode(defaultMarkupNode)
</code></pre>

---

## Post #6 by @hherhold (2021-10-04 13:44 UTC)

<p>Hmph… something still missing, I put both these code snippets in my <code>.slicerrc.py</code> file and  when I make a new markup node and add points, they’re still unlocked. Is there something I need to do to tell the <code>vtkMRMLMarkupsFiducialNode</code> that it needs to use those particular <code>vtkMRMLMarkupsNode</code>s as defaults? (This question likely doesn’t make any sense…)</p>

---

## Post #7 by @jamesobutler (2021-10-04 14:57 UTC)

<p>For a Fiducial node, the following works for me where the control points are not movable and are locked. If it doesn’t work for you, download a new Slicer version, don’t install any extensions, and test this snippet.</p>
<pre><code class="lang-python">defaultMarkupNode = slicer.vtkMRMLMarkupsFiducialNode()  # fiducial node markup
defaultMarkupNode.SetLocked(1)
slicer.mrmlScene.AddDefaultNode(defaultMarkupNode)
</code></pre>

---

## Post #8 by @hherhold (2021-10-04 15:05 UTC)

<p>OK, that does make the point immovable, but it does not show as locked in the control points list. I’m also not able to rename the point by right-clicking on the point - it’s completely locked and not modifiable.</p>
<p>What I’m looking for is to lock the position by default but be able to rename it via right clicking.</p>
<p>My hacky work-around has been okay thus far, so if this takes any real amount of time to look into, no need to bother.</p>
<p>Thanks!!!</p>

---

## Post #9 by @jamesobutler (2021-10-04 15:13 UTC)

<p>Yes the example code has been setting the Locked state for the node which applies to all control points rather than setting the locked state for the individual control point. The locked state in the example code is indicated by the locked icon in the GUI as shown with the tooltip.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a74b0ee415451db02463120c7860358898e317f.png" alt="image" data-base62-sha1="aCFlefN4ev0cPrbuzRFxmgh8xd5" width="319" height="249"></p>

---

## Post #10 by @hherhold (2021-10-04 15:14 UTC)

<p>Ah, okay. Is it possible to make a default control point that is locked?</p>

---

## Post #11 by @lassoan (2021-10-04 16:16 UTC)

<p>Control points are currently always initialized unlocked. You could lock them without Slicer core change by adding an observer to control point add event and lock every newly added control points. However, if “locked by default” is a common need then it would be quite easy to add a flag for this in the markups node.</p>
<p>I guess you need locking because you want to avoid accidental modification of placed points (e.g., when you rotate the view you may accidently click on a control point), which must be a common need. <a class="mention" href="/u/smrolfe">@smrolfe</a> How do your users solve the problem of accidentally misplaced control points?</p>
<p><a class="mention" href="/u/hherhold">@hherhold</a> would you mind describing your use case on <a href="https://github.com/Slicer/Slicer/wiki/Markups-rework">this page</a> so that we can get  more complete picture of how people use markups?</p>

---

## Post #12 by @hherhold (2021-10-04 17:19 UTC)

<p>Yeah, as described in the use case I added (below), I set up a shortcut key to run a quick function that locks all control points. The minus is that it locks all the ones done thus far, so the one just placed is unlocked, but it’s been better than nothing. (Yes, very hacky.)</p>
<p>I’ll take a look at adding an observer - that’s far more elegant.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="12981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/hherhold">@hherhold</a> would you mind describing your use case on <a href="https://github.com/Slicer/Slicer/wiki/Markups-rework" rel="noopener nofollow ugc">this page</a> so that we can get more complete picture of how people use markups?</p>
</blockquote>
</aside>
<p>Done.</p>

---

## Post #13 by @smrolfe (2021-10-04 17:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="12981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>guess you need locking because you want to avoid accidental modification of placed points (e.g., when you rotate the view you may accidently click on a control point), which must be a common need.</p>
</blockquote>
</aside>
<p>Yes, this is a common need. We’ve had some requests for an undo button to correct these kind of mistakes. Using a landmark template should help with this. If the landmark points are locked when the template is created, they can be placed but not moved in the scene (by default) when the template is imported.</p>

---

## Post #14 by @Saima (2023-07-11 05:53 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="13" data-topic="12981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>g a landmark template should help with thi</p>
</blockquote>
</aside>
<p>how to individually lock control points (python script) when they are created? are they still locked when saving and when opening them with a new application program.</p>
<p>regards,<br>
saima</p>

---

## Post #15 by @hherhold (2023-07-11 11:18 UTC)

<p>This is how I do it, it is <em>absolutely</em> not the best way, and not even the right way, but it works for my workflow. I have a 5-button programmable mouse, so I’ve set a hotkey/shortcut of <code>;</code> to add a markup point and then programmed a mouse button to type that key. You can also just type <code>;</code> from the keyboard. Anyway, this shortcut runs a python function that sets the interaction node to placement node, then locks all markups for that node. For whatever reason, it locks all nodes except the one that’s just been placed, but since I place a lot of points in a row, it’s good enough for me.</p>
<p>Locked markups are saved as locked and reloaded as locked. You can look at the JSON file that has the markups and check the “locked” attribute and see that it is set to “on”.</p>
<p>The right way, as described above, is to change the default markup node to be locked. I’ve been unable to get this to work but I haven’t spent enough time debugging it since my <em>very</em> hacky method works for me.</p>
<p>The shortcut function is:</p>
<pre><code class="lang-auto">def hh_place_fiducial():
    try:
        interactionNode = slicer.app.applicationLogic().GetInteractionNode()
        interactionNode.SetCurrentInteractionMode(interactionNode.Place)
        mod = slicer.util.getModule("Markups")
        ml = mod.logic()
        n = slicer.util.getNode(ml.GetActiveListID())
        ml.SetAllMarkupsLocked(n, True)
    except AttributeError:
        pass

</code></pre>
<p>And to set it as a hotkey/shortcut: (You don’t need the loop below for setting only one, I have a number of shortcuts I’ve defined but edited those out for clarity.)</p>
<pre><code class="lang-auto">shortcuts = [
  (';', lambda: hh_place_fiducial())
]

for (shortcutKey, callback) in shortcuts:
    shortcut = qt.QShortcut(slicer.util.mainWindow())
    shortcut.setKey(qt.QKeySequence(shortcutKey))
    shortcut.connect( 'activated()', callback)
</code></pre>
<p>(As an aside, this what I have tried for setting the default node to be locked, but it does <em>not</em> work. If anybody’s got ideas on why, any help would be awesome.)</p>
<pre><code class="lang-auto">### THIS DOES NOT WORK
defaultMarkupNode = slicer.vtkMRMLMarkupsFiducialNode() 
defaultMarkupNode.SetLocked(1)
slicer.mrmlScene.AddDefaultNode(defaultMarkupNode)
</code></pre>

---

## Post #16 by @Saima (2023-07-13 05:31 UTC)

<p>Hi,<br>
Thanks for your reply. I am locking the control points while creating them using the markupnode.SetNthFiducialControlPointLocked(cp_no, True).</p>
<p>regards,<br>
Saima</p>

---
