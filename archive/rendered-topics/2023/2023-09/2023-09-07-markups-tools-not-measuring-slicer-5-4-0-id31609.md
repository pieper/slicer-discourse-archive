# Markups tools not measuring Slicer 5.4.0

**Topic ID**: 31609
**Date**: 2023-09-07
**URL**: https://discourse.slicer.org/t/markups-tools-not-measuring-slicer-5-4-0/31609

---

## Post #1 by @jmhuie (2023-09-07 19:11 UTC)

<p>With Slicer 5.4.0, it seems that the MarkupsLineNode and other Markups Nodes are not showing their measurements, nor does it appear to be registering an actual measurement. When I try to get the measured length using python it returns “0.0” when it is greater than that. Is anyone else running into this issue? Currently running on a Mac.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15427cecd3e06a9524d9640dc9b29c4e2bda9263.jpeg" data-download-href="/uploads/short-url/324tyA4DoCVXp7gSI6pkZ7cHTIn.jpeg?dl=1" title="Screenshot 2023-09-07 at 3.06.05 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15427cecd3e06a9524d9640dc9b29c4e2bda9263_2_690x431.jpeg" alt="Screenshot 2023-09-07 at 3.06.05 PM" data-base62-sha1="324tyA4DoCVXp7gSI6pkZ7cHTIn" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15427cecd3e06a9524d9640dc9b29c4e2bda9263_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15427cecd3e06a9524d9640dc9b29c4e2bda9263_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15427cecd3e06a9524d9640dc9b29c4e2bda9263_2_1380x862.jpeg 2x" data-dominant-color="353537"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-07 at 3.06.05 PM</span><span class="informations">1920×1200 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-09-07 19:26 UTC)

<p>I cannot reproduce the behavior you described. Can you take a video or describe the exact steps (each click) you make?</p>

---

## Post #3 by @jmhuie (2023-09-13 01:27 UTC)

<p>I did some more investigating. It looks like the problem may have to do the SlicerMorph customizations, as I only have this problem when the customizations are enabled. <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>To be clear, what I did was:</p>
<ol>
<li>re-downloaded Slicer 5.4 on Mac</li>
<li>Open Slicer and immediately drew a line using the Markups tools and saw the length being displayed</li>
<li>Installed SlicerMorph</li>
<li>Confirmed that the line tool still works</li>
<li>Enabled SlicerMorph customizations, restarted Slicer, and found that the line tool stopped measuring</li>
<li>Turned off customizations, restarted Slicer, and found that the line tool works again</li>
</ol>
<p>Possibly unrelated, but upon initially launching Slicer the python window has this error regarding the MarkupsToModel extension</p>
<pre><code class="lang-auto">[Qt]   Error(s):
[Qt]     Cannot load library /Applications/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib: (dlopen(/Applications/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib, 0x0085): Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib
[Qt]   Referenced from: &lt;8228E9E9-AE1B-31B6-BEEB-4F916BF21B91&gt; /Applications/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/libitkgdcmMSFF-5.3.1.dylib
[Qt]   Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/usr/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file, not in dyld cache))
</code></pre>

---

## Post #4 by @muratmaga (2023-09-13 02:27 UTC)

<p><a class="mention" href="/u/jmhuie">@jmhuie</a> what do you mean by <code>stops measuring?</code></p>
<p>I am trying to replicate this on an intel Mac I have, and line tools works as expected, but it doesn’t display the measurement field regardless whether slicermorph customization are enabled or disabled? Is this what you are referring to as the issue?</p>
<p>We did recently enabled undo for markups through the customization script, but I am not seeing any errors in the log file either.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff41cbf974133847e812e6ee12ffdd7eafc2e76f.png" data-download-href="/uploads/short-url/Aq6ISGQ0zpy6Sgkx7TXfWVhbo1V.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff41cbf974133847e812e6ee12ffdd7eafc2e76f_2_605x500.png" alt="image" data-base62-sha1="Aq6ISGQ0zpy6Sgkx7TXfWVhbo1V" width="605" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff41cbf974133847e812e6ee12ffdd7eafc2e76f_2_605x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff41cbf974133847e812e6ee12ffdd7eafc2e76f_2_907x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff41cbf974133847e812e6ee12ffdd7eafc2e76f_2_1210x1000.png 2x" data-dominant-color="9190A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2406×1986 393 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2023-09-13 02:31 UTC)

<p>Ok, I can replicate this with a new slicer session without customization script loaded at the beginning.</p>
<p>Thanks for reporting <a class="mention" href="/u/smrolfe">@smrolfe</a> can you take a look?</p>

---

## Post #7 by @jmhuie (2023-09-13 02:45 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="31609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I am trying to replicate this on an intel Mac I have, and line tools works as expected, but it doesn’t display the measurement field regardless whether slicermorph customization are enabled or disabled? Is this what you are referring to as the issue?</p>
</blockquote>
</aside>
<p>Yes that is what I’m referring to as the issue, except it does display the measurement when the slicermorph customizations are disabled. And if you were to measure the length of the line using python, it’d say the length is 0.0 when it clearly isn’t.</p>

---

## Post #8 by @muratmaga (2023-09-13 02:50 UTC)

<p>If you do want to use the customizations, as a temporary fix you can comment out or remove this line and it seems to fix the issue.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/de80128f9e5267df9c979a0a99142d21ee06573f/MorphPreferences/Resources/SlicerMorphRC.py#L178">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/de80128f9e5267df9c979a0a99142d21ee06573f/MorphPreferences/Resources/SlicerMorphRC.py#L178" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/de80128f9e5267df9c979a0a99142d21ee06573f/MorphPreferences/Resources/SlicerMorphRC.py#L178" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph/blob/de80128f9e5267df9c979a0a99142d21ee06573f/MorphPreferences/Resources/SlicerMorphRC.py#L178</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="168" style="counter-reset: li-counter 167 ;">
          <li>    if not shortcut.connect( 'activated()', callback):
</li>
          <li>        print(f"Couldn't set up {shortcutKey}")
</li>
          <li>logging.info(f"  {len(shortcuts)} keyboard shortcuts installed")
</li>
          <li>
</li>
          <li># set up undo/redo for markups
</li>
          <li>logging.info("Set up undo/redo buttons for markups")
</li>
          <li>slicer.mrmlScene.SetUndoOn()
</li>
          <li>
</li>
          <li>undoEnabledNodeClassNames = [
</li>
          <li>  "vtkMRMLMarkupsFiducialNode",
</li>
          <li class="selected">  "vtkMRMLMarkupsLineNode",
</li>
          <li>  "vtkMRMLMarkupsAngleNode",
</li>
          <li>  "vtkMRMLMarkupsCurveNode",
</li>
          <li>  "vtkMRMLMarkupsClosedCurveNode",
</li>
          <li>  "vtkMRMLMarkupsPlaneNode",
</li>
          <li>  "vtkMRMLMarkupsROINode",
</li>
          <li>  ]
</li>
          <li>for className in undoEnabledNodeClassNames:
</li>
          <li>  node = slicer.mrmlScene.CreateNodeByClass(className)
</li>
          <li>  node.SetUndoEnabled(True)
</li>
          <li>  slicer.mrmlScene.AddDefaultNode(node)
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @smrolfe (2023-09-13 02:52 UTC)

<p>Yes, I’ll look into it and update here.</p>

---

## Post #10 by @jcfr (2023-09-13 13:20 UTC)

<blockquote>
<p>Possibly unrelated, but upon initially launching Slicer the python window has this error regarding the MarkupsToModel extension</p>
<pre><code class="lang-auto">[Qt]   Error(s):
[Qt]     Cannot load library /Applications/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib: (dlopen(/Applications/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib, 0x0085): Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib
[Qt]   Referenced from: &lt;8228E9E9-AE1B-31B6-BEEB-4F916BF21B91&gt; /Applications/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/libitkgdcmMSFF-5.3.1.dylib
[Qt]   Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/usr/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file, not in dyld cache))
</code></pre>
</blockquote>
<p>Consider uninstalling &amp; re-installing the <code>SlicerMorph</code> extension as this a symptom of the following issue that just got addressed:</p>
<aside class="quote quote-modified" data-post="1" data-topic="31535">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/6de8d8/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extensions-can-not-work-on-slicer-5-4-0-on-macos/31535">New extensions can not work on Slicer 5.4.0 on MacOS</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I have just updated Slicer VMTK to 144582e (2023-08-22). It showed the following error: 
dlopen(/Applications/Slicer 5.4.0.app/Contents/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/qt-loadable-modules/qSlicerBranchClipperModuleWidgetsPythonQt.so, 0x0002): Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib
  Referenced from: &lt;8228E9E9-AE1B-31B6-BEEB-4F916BF21B91&gt; /Applications/Slicer 5.4.0.app/Contents/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/libitkgdc…
  </blockquote>
</aside>


---

## Post #11 by @smrolfe (2023-09-21 16:54 UTC)

<p><a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/" rel="noopener nofollow ugc">Enabling undo/redo</a> is causing this issue because there’s a bug where adding a default node to the scene removes the measurements displayed for that node type. This also occurs when SetUndoEnabled() is not set for the default node.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/smrolfe/SlicerMorph/blob/248235d5814e8cb91d709598658971d4753d35f9/MorphPreferences/Resources/SlicerMorphRC.py#L180C2-L183C1">
  <header class="source">

      <a href="https://github.com/smrolfe/SlicerMorph/blob/248235d5814e8cb91d709598658971d4753d35f9/MorphPreferences/Resources/SlicerMorphRC.py#L180C2-L183C1" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/smrolfe/SlicerMorph/blob/248235d5814e8cb91d709598658971d4753d35f9/MorphPreferences/Resources/SlicerMorphRC.py#L180C2-L183C1" target="_blank" rel="noopener nofollow ugc">smrolfe/SlicerMorph/blob/248235d5814e8cb91d709598658971d4753d35f9/MorphPreferences/Resources/SlicerMorphRC.py#L180C2-L183C1</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="180" style="counter-reset: li-counter 179 ;">
          <li>node = slicer.mrmlScene.CreateNodeByClass(className)
</li>
          <li>node.SetUndoEnabled(True)
</li>
          <li>slicer.mrmlScene.AddDefaultNode(node)
</li>
          <li>
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For now, we updated the SlicerMorph preferences to enable undo/redo for point lists only.</p>
<p>cc: <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #12 by @lassoan (2023-09-22 03:01 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="11" data-topic="31609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>because there’s a bug where adding a default node to the scene removes the measurements displayed for that node type</p>
</blockquote>
</aside>
<p>Is there a bug report for this. If not, could you create one? Thank you!</p>

---

## Post #13 by @smrolfe (2023-09-22 19:49 UTC)

<p>Issue added here: <a href="https://github.com/Slicer/Slicer/issues/7239" class="inline-onebox" rel="noopener nofollow ugc">Adding a default Markups node to scene removes measurements · Issue #7239 · Slicer/Slicer · GitHub</a></p>

---

## Post #14 by @coco (2024-02-22 15:33 UTC)

<p>This solved my problem thanks.</p>
<p>Not sure if this is related but I can now see measurments both next to my markups when drawing them and on the measurment tab. But I cannot see them in the table, nor export the measurments in a tab. Is this actually possible or related to a bug ?<br>
Thanks</p>

---
