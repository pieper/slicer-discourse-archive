# Python : how to centre volume on load?

**Topic ID**: 10220
**Date**: 2020-02-12
**URL**: https://discourse.slicer.org/t/python-how-to-centre-volume-on-load/10220

---

## Post #1 by @chir.set (2020-02-12 16:45 UTC)

<p>Previously, using the ‘Add data’ menu, we would check the ‘Centre’ widget so that the loaded volume (DICOM series) was centered. The ‘Add data’ menu is no longer maintained for this use, and I’m using the DICOM module instead.</p>
<p>I could not find an option to centre a loaded volume in the DICOM module. I can always go the Volumes module to do that. I’m looking for an automated way however. This is because I have to CROP the volumes after loading them, using fixed ROIs (saved on storage) as templates. Studies from different OEMs have different centre point.</p>
<p>I tried this to no avail in slicerrc.py :</p>
<pre><code>@vtk.calldata_type(vtk.VTK_OBJECT)
def onNodeAdded(caller, event, calldata):
  node = calldata
  if isinstance(node, slicer.vtkMRMLVolumeNode):
    volumesLogic = slicer.modules.volumes.logic()
    volumesLogic.CenterVolume(node)

slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, onNodeAdded)
</code></pre>
<p>I could not find more useful code in the <a href="https://www.slicer.org/wiki/Documentation/4.10/ScriptRepository" rel="nofollow noopener">repository</a>. (There’s a code snippet to centre the 3D view, but that’s not what I need to do.)</p>
<p>I’m asking for some help here for this task.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2020-02-12 19:27 UTC)

<p>Looks like you are on the right track - you might try adding some print statements to confirm the node is what you expect.  Maybe it doesn’t have the image data yet or something.</p>
<p>But, for your workflow, I understand you are loading loading dicoms as scalar volumes and you know how you plan to process them, so why not write a custom import feature.  Even overload the drag-and-drop so that everything behaves in the most efficient way for you?</p>

---

## Post #3 by @chir.set (2020-02-12 21:00 UTC)

<p>I’m not skilled at Python , and even less in Slicer’s internals. I was expecting a few liners solution here, I’ll try a few random inspirations wildly.</p>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2020-02-13 01:17 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="10220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Studies from different OEMs have different centre point.</p>
</blockquote>
</aside>
<p>Center of the coordinate system is chosen by the scanner’s operator. It often contains somewhat useful information that is should not be simply discarded. Erasing the information would also make the volume spatially misaligned with other data structures that are defined in the same coordinate reference.</p>
<p>“Center volume” irreversibly erases image position and orientation, so it should not be used. This option was added decades ago and we haven’t removed it, because it is quite hidden and so unlikely that people would find it.</p>
<p>If you want to automatically fit templates to an image then image bounds are not ideal for this anyway, but you want to do a simple analysis of the image content instead. For example, if you apply simple thresholding then <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203">oriented bounding box or principal axes</a> will tell you the physical location of the chosen object within the image.</p>

---

## Post #5 by @chir.set (2020-02-13 12:46 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="2" data-topic="10220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>But, for your workflow … so why not write a custom import feature</p>
</blockquote>
</aside>
<p>This hinted me to modify my <a href="https://github.com/chir-set/TemplateROICrop" rel="noopener nofollow ugc">custom</a> module, it restores back automated centering like before.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="10220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>we haven’t removed it, because it is quite hidden</p>
</blockquote>
</aside>
<p>Removing it would be a major drawback to me. It’s deeply hidden, no one is seeing, so it can remain there <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks.</p>

---

## Post #6 by @lassoan (2020-02-13 13:42 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="5" data-topic="10220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Removing it would be a major drawback to me. It’s deeply hidden, no one is seeing, so it can remain there</p>
</blockquote>
</aside>
<p>Centering the volume is just a single line of code (set the origin to half the size of the volume), but you can do much better than that, with fully automatic positioning of the ROIs based on image <em>content</em> (using oriented bounding box or centroid/principal axes/moments).</p>

---
