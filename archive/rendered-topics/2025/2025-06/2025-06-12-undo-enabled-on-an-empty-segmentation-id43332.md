# Undo enabled on an empty segmentation

**Topic ID**: 43332
**Date**: 2025-06-12
**URL**: https://discourse.slicer.org/t/undo-enabled-on-an-empty-segmentation/43332

---

## Post #1 by @nhjohnston (2025-06-12 18:43 UTC)

<p>When completing the following steps, the undo/redo buttons are enabled despite no visible changes being made to the segmentation in the scene.</p>
<ol>
<li>Create a new segmentation</li>
<li>Select the erase tool</li>
<li>Erase in the scene (undo is enabled)</li>
<li>Click the undo button (redo is enabled)</li>
</ol>
<p>Although this makes sense, because editor effects are being applied, it is a little jarring for the user because the segment labelmap is empty the whole time. I feel like the expected behavior would be for the undo/redo button to remain disabled if there is no visible change to the segmentation.  Is there a current workaround for this?</p>
<p>Operating system: Windows 11<br>
Slicer version: 5.8.1</p>

---

## Post #2 by @lassoan (2025-06-12 18:57 UTC)

<p>Some undo-able changes may not be easily noticeable, but as far as I can see, everything works as expected.</p>
<p>I could not follow the steps you described: I could not select the “Erase” effect without loading an image and creating a segment; but then by the time I got to selecting the “Erase” tool, the undo button was already enabled. So, I performed these steps instead:</p>
<ul>
<li>Start Slicer</li>
<li>Go to Sample Data module</li>
<li>Load MRHead sample data</li>
<li>Go to Segment Editor module</li>
<li>Add Segment =&gt; Undo button has become enabled (clicking it removes the segment) - good</li>
<li>Select “Erase” effect</li>
<li>Click-and-drag in a slice view =&gt; Undo button is still enabled (clicking it reverts the segment’s state change from “Not started” to “In progress”; clicking again removes the segment) - good</li>
</ul>
<p>Everything worked as expected.</p>
<p>I’ve also tried loading a scene that has a segmentation, selected the erase tool, but when I erased an empty region then no undo state was added (undo did not get enabled). So, again, everything worked well.</p>

---

## Post #3 by @jamesobutler (2025-06-12 19:05 UTC)

<p>Using Slicer 5.8.1, I observe</p>
<ol>
<li>Start Slicer</li>
<li>Load MRHead</li>
<li>Go to Segment Editor module</li>
<li>Add Segment (undo becomes enabled related to the adding of the segment)</li>
<li>Select “Erase” effect</li>
<li>Single left-click in 4 places on the volume. First click changes the segment state from “Not started” to “In progress” although the labelmap has not changed and is still empty.</li>
<li>Click undo multiple times and observe that you have to click undo “4” times before observing the segment going back to the “Not started” state and then clicking undo a 5th reflecting the removal of the segment.</li>
</ol>
<p>So the clicking of the effect like Erase at a time when the binary labelmap is seemingly not changing before or after the event is resulting in a recorded node state in the undo/redo chain.</p>

---

## Post #4 by @lassoan (2025-06-12 22:17 UTC)

<p>I see, thank you for the clarification. Clicking undo button reverts the <em>last user action</em> - the last editing operation that the user initiated, regardless if the action was effective (resulted in change) or not.</p>
<p>Your proposal is to make clicking undo revert the <em>last effective user action</em>. While this could seem more intuitive, it would lead to undeterministic behavior, as the user often has no way of knowing if an action was effective or not.</p>
<p>Example: I apply smoothing on the segmentation. Seemingly nothing changes. I want to redo the segmentation with a stronger smoothing factor. Should I click undo before changing the smoothing factor and applying smoothing again?</p>
<ul>
<li>If clicking undo revert the <em>last user user action</em> (current): Answer is easy, yes, click undo. It takes me back to the state before the last smoothing operation, regardless if my last smoothing attempt actually changed something or not.</li>
<li>If clicking undo reverts the <em>last effective user action</em> (proposed): It is impossible to tell what to do. I cannot determine if the last operation actually changed something in the segmentation somewhere. I may be able to see changes in the current slice, but how would I know if  there has been some subtle change somewhere else?</li>
</ul>
<p>So, overall, I think keeping the current behavior is better, as it is more deterministic.</p>

---

## Post #5 by @jamesobutler (2025-06-12 22:37 UTC)

<p>Indeed an effect can cause a change elsewhere that is not visible to the user which could still be confusing. Though it would seem that the number of these instances could be reduced if say the binary labelmap is not changed by a user action, then it shouldn’t be added into the undo/redo stack as a modified event. This could reduce unnecessary memory usage if you have a large segmentation and you do an action that does not result in the binary labelmap changing at all while still utilizing the undo stack.</p>
<p>Would such an action be computationally expensive to check if the labelmap was changed during the last user action when deciding whether to add a node state to the undo history?</p>

---

## Post #6 by @lassoan (2025-06-13 00:17 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="43332">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>This could reduce unnecessary memory usage if you have a large segmentation and you do an action that does not result in the binary labelmap changing at all</p>
</blockquote>
</aside>
<p>Segmentation history only saves a new copy of the data object if it is modified. If you save new undo states without segment changes then the memory and computation cost is near zero.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="43332">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Would such an action be computationally expensive to check if the labelmap was changed during the last user action when deciding whether to add a node state to the undo history?</p>
</blockquote>
</aside>
<p>The check is somewhat expensive, but not prohibitive (we do it anyway when we have segments in multiple layers and overwriting of other segments is enabled). The main issue is user experience. How would you tell users that their action did not end up changing anything? Why would you complicate their life by telling them this (most of the time) irrelevant information? Who would explain them that they need this information so that they know what happens when they click undo?</p>
<p>We can find better ways to make the undo/redo behavior more intuitive while keeping it deterministic. For example, in “saveStateForUndo” we could store the name of the editor effect (and the effect could provide an optional extra description). We could use this to make the undo/redo button tooltip more informative (e.g., instead of “Undo last editing operation” the tooltip would be something like “Undo Paint”, “Undo Erase”, “Undo Scissors - Erase inside”). We could also add a dropdown menu to the undo/redo buttons for bulk undo/redo (although by default we save just 10 states, which are not that hard to navigate):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b209facb232d3a303ecdc77825cdd1d8c9b5d0b.jpeg" data-download-href="/uploads/short-url/fhGZ5HDXlfG8ifcaIiUfMaC6hGH.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b209facb232d3a303ecdc77825cdd1d8c9b5d0b.jpeg" alt="image" data-base62-sha1="fhGZ5HDXlfG8ifcaIiUfMaC6hGH" width="473" height="289"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">473×289 41.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jamesobutler (2025-06-13 02:32 UTC)

<p>I attempted to change the terminology or segment color to new states and also to the same selection to observe the undo/redo states and I observed:</p>
<p>Slicer 5.8.1:</p>
<ol>
<li>Add Segment</li>
<li>Double click color column in table to bring up terminology dialog and change “Tissue” selection to “Artery”.</li>
<li>Double click color column in table to bring up terminology dialog and change “Artery” selection to “Body fat”.</li>
<li>Double click color column in table to bring up terminology dialog and select “Body Fat” again.</li>
<li>Press “Undo” and observe that it goes to immediately removing the segment where it didn’t appear to remember anything about the terminology selections in the undo stack.</li>
</ol>
<p>Is there a reason that terminology selection is not an undo state of the segment? And that re-selecting the same terminology (producing a no change event) didn’t also produce an undo state if no change binary labelmap events create an undo event? This is to better understand what modifications to the segment are saved and if the same event selection is made for a given property (even though no change), does it count as an undo state.</p>
<p>It appears that double-clicking the name column and choosing a terminology saves an undo state for the segment name, but doesn’t actually undo to go back to the old terminology.</p>

---

## Post #8 by @lassoan (2025-06-13 14:32 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="7" data-topic="43332">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Is there a reason that terminology selection is not an undo state of the segment?</p>
</blockquote>
</aside>
<p>Good catch. Terminology selection should store an undo state for consistent behavior. Implementation might be a little tricky, because the segment list should emit the <code>segmentAboutToBeModified</code> just after the terminology popup is closed with “Select”, but before the terminology/color is updated in the segmentation, and if multiple properties are changed at once (segment name, color, terminology) then it would be nice to add only a single undo state for that - but it should be all doable. Please submit an issue for this, as I don’t know when someone will have time to implement it.</p>

---
