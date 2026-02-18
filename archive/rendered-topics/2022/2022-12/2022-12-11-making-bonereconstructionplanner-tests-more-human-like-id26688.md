# Making BoneReconstructionPlanner tests more human like

**Topic ID**: 26688
**Date**: 2022-12-11
**URL**: https://discourse.slicer.org/t/making-bonereconstructionplanner-tests-more-human-like/26688

---

## Post #1 by @mau_igna_06 (2022-12-11 19:42 UTC)

<p>I guess I need an <a href="https://discourse.slicer.org/t/using-eventfilters-on-qt-objects/9744">event filter</a> on the mainWindow to ignore all mouse-clicks and key-strokes while the steps of the test are running in a visually appealing fashion by using:</p>
<pre><code class="lang-auto">slicer.app.processEvents()
#and maybe qt.QTimer.sleep(200)
</code></pre>
<p>And uninstall the event filter if the test fails or ends successfully</p>
<p><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/46c79ac059625f7cf4dd9183ee716efcd95c1bb8/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3690" rel="noopener nofollow ugc">Here is a test</a>, I would like to create the points more slowly and make it look kinda interactive</p>
<p>Hope you can help</p>

---

## Post #2 by @pieper (2022-12-11 19:48 UTC)

<p>It’s probably easier to use <code>slicer.app.processEvents(qt.QEventLoop.ExcludeUserInputEvents)</code>.</p>
<p>Or you can use <code>slicer.util.delayDisplay(message, msec)</code> for a similar purpose.</p>

---

## Post #3 by @mau_igna_06 (2022-12-11 20:16 UTC)

<p>Although making tests for every possible behavior would be impossible (in my opinion).</p>
<p>I would be aiming to have self-tests for a complete (linear) workflow that could teach users to use BoneReconstructionPlanner and achieve the surgical guides (so this could supplement or at least help minimize documentation efforts)</p>
<p>Is this idea common? Has it been done on other extensions I can refer to?</p>

---

## Post #4 by @pieper (2022-12-11 21:05 UTC)

<p>Yes, exactly.  No software tests can be exhaustive.  The original goal of the SelfTests was exactly to replicate end-to-end use cases in order to flag any regressions that would have an impact on end users.  These Application-level tests are in <a href="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp/Testing/Python"><code>Applications/SlicerApp/Testing/Python</code></a>.  The tests starting with RSNA for example correspond to the steps of the user tutorials held at that conference one year.</p>
<p>In the future we plan to further integrate the SelfTest scripts with the tutorial infrastructure so that we can more easily maintain tutorials with screenshots in multiple languages.  That is, we would use the test to capture screenshots and would run the script once for each language setting.</p>

---

## Post #5 by @lassoan (2022-12-12 18:02 UTC)

<p>A useful feature of some selftests that they have buttons for running each section of the test separately. Users than pick and choose which section they want to just watch and which ones they want to do themselves.</p>
<p>To use the self-tests as tutorials, it would be nice to record to video, because that would allow users to easily pause it, rewind, fast-forward, etc. as needed. For the videos it could be better to move text display from the center of the screen to somewhere near the bottom; and to show some animation where the mouse is clicked (and maybe even move the mouse pointer there).</p>

---
