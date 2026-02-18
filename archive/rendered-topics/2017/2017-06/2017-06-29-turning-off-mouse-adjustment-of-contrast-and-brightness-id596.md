# Turning off mouse adjustment of contrast and brightness

**Topic ID**: 596
**Date**: 2017-06-29
**URL**: https://discourse.slicer.org/t/turning-off-mouse-adjustment-of-contrast-and-brightness/596

---

## Post #1 by @bobread (2017-06-29 14:19 UTC)

<p>Is it possible to turn off the left mouse button adjustment of contrast and brightness in the Segment Editor? When manually painting a segment I keep accidentally changing the values and it is driving me up the wall!</p>

---

## Post #2 by @fedorov (2017-06-29 15:48 UTC)

<p>This would indeed be a very useful feature to be able to “lock” window/level for a given volume, but I don’t think it is possible right now, unfortunately.</p>

---

## Post #3 by @lassoan (2017-06-29 16:09 UTC)

<p>We’ve added this recently to the nightly version. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Disable_certain_user_interactions_in_slice_views">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Disable_certain_user_interactions_in_slice_views</a></p>
<p>Currently there is no graphical user interface to activate this, so you have to write 2-3 lines of Python code (get list of slice views from the layout manager, iterate through all of them and disable interactions that you don’t need).</p>

---

## Post #4 by @fedorov (2017-06-29 16:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We’ve added this recently to the nightly version</p>
</blockquote>
</aside>
<p>Excellent news! I think this deserves an announcement, unless I missed it. Thank you!</p>

---

## Post #5 by @fedorov (2017-06-29 16:32 UTC)

<p>I have to say that for some of the use cases I have in mind, it would be a lot more convenient to toggle these properties (or at least w/l) on the volume node, not for individual viewers.</p>

---

## Post #6 by @lassoan (2017-06-30 13:20 UTC)

<p>I agree that locking W/L of volume display nodes could be useful, too. Ultimately, I think the most useful would be to have better mouse mode management (so that you could choose the mouse drag-and-drop to do nothing).</p>
<p>Do you have a specific use case where per-volume W/L locking would be preferred over disabling W/L adjustment by drag-and-drop in all views?</p>

---

## Post #7 by @fedorov (2017-06-30 14:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you have a specific use case where per-volume W/L locking would be preferred over disabling W/L adjustment by drag-and-drop in all views?</p>
</blockquote>
</aside>
<p>Yes, I do!</p>
<p>In one of our use cases, we do Standardized Uptake Value (SUV) correction for the PET data. While viewing SUV images, since the measurements are more or less normalized, W/L is fixed for the given tracer at certain level. It should never be changed while reviewing the data. Here is the code in the plugin that sets W/L based on the tracer for an SUV volume loaded:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/DICOMRWVMPlugin/DICOMRWVMPlugin.py#L270-L281">
  <header class="source">

      <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/DICOMRWVMPlugin/DICOMRWVMPlugin.py#L270-L281" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/DICOMRWVMPlugin/DICOMRWVMPlugin.py#L270-L281" target="_blank" rel="noopener">QIICR/Slicer-PETDICOMExtension/blob/master/DICOMRWVMPlugin/DICOMRWVMPlugin.py#L270-L281</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="270" style="counter-reset: li-counter 269 ;">
          <li>instanceUIDs = instanceUIDs[:-1]  # strip last space</li>
          <li></li>
          <li># get the instance UID for the RWVM object</li>
          <li>derivedItemUID = ""</li>
          <li>try:</li>
          <li>  derivedItemUID = slicer.dicomDatabase.fileValue(loadable.rwvFile,self.tags['sopInstanceUID'])</li>
          <li>except AttributeError:</li>
          <li>  # no derived items</li>
          <li>  pass</li>
          <li></li>
          <li>if loadable.quantity:</li>
          <li>  imageNode.SetVoxelValueQuantity(loadable.quantity)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>As you understand, it will be quite cumbersome to keep W/L settings fixed with the current functionality. But I still think it is better than nothing, and I definitely understand there are situations where it is important and convenient to keep W/L fixed on a per-viewer basis.</p>

---

## Post #8 by @lassoan (2017-07-01 00:03 UTC)

<p>I’ve added window/level locking in Volumes module (r26142). It’ll available in tomorrow’s nightly build. Let me know if you have any comments or suggestions.</p>

---

## Post #9 by @fedorov (2017-07-02 20:09 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a>! It works as expected, and I made a PR to leverage this feature in the PET SUV DICOM plugin: <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/pull/6">https://github.com/QIICR/Slicer-PETDICOMExtension/pull/6</a>.</p>
<p>I believe this feature will be very useful for quantitative imaging applications! <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=5" title=":thumbsup:" class="emoji" alt=":thumbsup:"></p>

---

## Post #10 by @Joshua_Broder (2020-02-21 15:38 UTC)

<p>I seem to have lost the ability to adjust brightness and contrast in the planar views in the current stable release (4.10.2, reision 28257) and the nightly build (4.11.0, revision 28783). I see the discussion about intentionally locking these, but is there a way to unlock these (as the default)?  This is crucial fundamental feature.  Thanks!</p>
<p>I’m running Windows 10.</p>
<p>Josh</p>

---

## Post #11 by @lassoan (2020-02-21 15:47 UTC)

<p>This should help: <a href="https://discourse.slicer.org/t/adjust-window-level-is-not-working-nightly-release-4-11-0/6817/3" class="inline-onebox">Adjust Window Level is not working (nightly release 4.11.0)</a>. If you have any remaining questions then let us know.</p>
<p>We plan to add mouse mode selection to right-click menu so that you don’t need to move the mouse to the toolbar.</p>

---
