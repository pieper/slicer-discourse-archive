---
topic_id: 4532
title: "Access Visible Widgets"
date: 2018-10-25
url: https://discourse.slicer.org/t/4532
---

# Access visible widgets

**Topic ID**: 4532
**Date**: 2018-10-25
**URL**: https://discourse.slicer.org/t/access-visible-widgets/4532

---

## Post #1 by @kayarre (2018-10-25 20:13 UTC)

<p>I know how to grab  an active node like this</p>
<pre><code class="lang-auto">segmentEditorNode = slicer.mrmlScene.GetSingletonNode("SegmentEditor", "vtkMRMLSegmentEditorNode")
</code></pre>
<p>Is it possible to access the actual widgets without instantiating a new one? e.g.<br>
instead of <code>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()</code>  do something like the above. I think the answer is no based on this <a href="https://discourse.slicer.org/t/accessing-the-module-window/2241">thread</a>.</p>
<p>But I am curious to know what is the suggested approach? or maybe point me to the mental model of how the gui widgets interact with the mrmlScene?</p>

---

## Post #2 by @lassoan (2018-10-25 20:33 UTC)

<p>You can access any Qt widgets and manipulate their properties. However, directly manipulating a widget that is managed by another module may cause errors (as you may change the state of the widget in a way that the owner module does not expect).</p>
<p>It is safe to modify MRML nodes and safe to modify state of widgets that you create, so these approaches are recommended. For testing purposes or some workflow automation (e.g., if you only simulate a few button clicks in a very controlled scenario, …) it might be acceptable to deviate from these.</p>
<p>What would you like to achieve? Is there something that you cannot do by sticking to the recommended approaches?</p>

---

## Post #3 by @kayarre (2018-10-25 21:22 UTC)

<p>Thank you Andras,<br>
I think my main confusion is wrapping my head around which things are  used in what way depending on what it is. I think the workflow suggested is fine, but confusing still.  what constitutes direct manipulation vs manipulations of properties? I think the model is that <code>slicer.qMRMLSegmentEditorWidget()</code> is some sort of instantiation of a gui itself and has the method <code>setMasterVolumeNode</code>, but  the <code>segmentEditorNode</code> as created above thing is somehow linked to the gui and has a method <code>SetAndObserveMasterVolumeNode</code>.</p>
<p>they seem similar, but in order to activate and edit the segmentation pragmatically i need to use the widget, but when I am manually using the built in gui I am manipulating the same segmentation but with a different gui. maybe it’s the knowing what’s data vs the thing acting on the data?</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/man_shrugging.png?v=6" title=":man_shrugging:" class="emoji" alt=":man_shrugging:"></p>

---

## Post #4 by @lassoan (2018-10-26 04:09 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="3" data-topic="4532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>what constitutes direct manipulation vs manipulations of properties</p>
</blockquote>
</aside>
<p>If you create a widget in your own module then you are free to do anything with it. However, you are not supposed to access GUI of another module.</p>
<p>You can either use a module from another module by modifying MRML nodes (they are shared between all modules and anybody can modify a MRML node anytime) or calling methods of the module logic class.</p>
<p>You may find our lab’s yearly bootcamp training materials useful, especially <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">day3_2_SlicerProgramming.pptx</a>, which explains some high-level design concepts.</p>

---
