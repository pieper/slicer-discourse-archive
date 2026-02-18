# LeftButtonClickEvent on Markups behavior

**Topic ID**: 8008
**Date**: 2019-08-13
**URL**: https://discourse.slicer.org/t/leftbuttonclickevent-on-markups-behavior/8008

---

## Post #1 by @jamesobutler (2019-08-13 17:55 UTC)

<p>In Slicer 4.11 nightly, the LeftButtonClickEvent on a markup fiducial results in the “Centered” Jump Slices behavior in the other slice viewers. This jumps the offsets and centers the fiducial in the center of all the other slice viewers.</p>
<p>In Slicer 4.10 this behavior didn’t exist, but I’m looking to keep similar behavior in Slicer 4.11 in certain situations where I want to easily allow left-click-and-drag events, but I don’t want to accidentally allow left-click events which then jumps slices.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> (markups developer) Would it make more sense for “Click to Jump Slices” in the Markups Module to become an application setting? The “Click to Jump Slices” behavior is currently specific to selecting rows in the table of the Markups module and a qSlicerSimpleMarkupsWidget has its own unique <code>JumpToSliceEnabled</code> attribute.</p>
<p>Or is there a way to simply block the LeftButtonClickEvent on markups from being processed?</p>
<hr>
<h2>Source Code</h2>
<p><code>this-&gt;SetEventTranslation(WidgetStateOnWidget, vtkMRMLInteractionEventData::LeftButtonClickEvent, vtkEvent::NoModifier, WidgetEventJumpCursor);</code><br>
<a href="https://github.com/Slicer/Slicer/blob/1d6c0774786427ccb86d83a4ae8ab4df2dbf244a/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L64" rel="nofollow noopener">source</a></p>
<p>The event ends up calling this code to jump slices and center:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/11a17936a35ffe4adc06fb541f4c6320f4928faa/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.cxx#L172-L174" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/11a17936a35ffe4adc06fb541f4c6320f4928faa/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.cxx#L172-L174" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/11a17936a35ffe4adc06fb541f4c6320f4928faa/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.cxx#L172-L174</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="172" style="counter-reset: li-counter 171 ;">
<li>// Jump centered in all other slices in the view group</li>
<li>this-&gt;JumpSlicesToNthPointInMarkup(markupsDisplayNode-&gt;GetDisplayableNode()-&gt;GetID(), controlPointIndex,</li>
<li>  true /* centered */, viewGroup, sliceNode);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #2 by @jamesobutler (2019-08-14 22:34 UTC)

<p>If anyone has opinions or other inputs to make Jump Slices behavior more consistent between slice viewer behavior and other widgets that would be great! Thanks</p>

---

## Post #3 by @lassoan (2019-08-14 23:25 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="8008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Would it make more sense for “Click to Jump Slices” in the Markups Module to become an application setting?</p>
</blockquote>
</aside>
<p>Yes, absolutely, that’s the plan. Currently, mapping of GUI events to widget events is implemented in the widget’s constructor, but it is designed so that settings can be stored in a simple series of IDs (interaction event ID, modifiers, widget event ID). It would be great if you could work on overriding mapping from application settings.</p>

---
