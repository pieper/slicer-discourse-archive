# Reorder segments in Segment Editor?

**Topic ID**: 230
**Date**: 2017-04-30
**URL**: https://discourse.slicer.org/t/reorder-segments-in-segment-editor/230

---

## Post #1 by @hherhold (2017-04-30 18:53 UTC)

<p>Is there a way to reorder the segments in the segment list in the Segment Editor? I looked through nightly docs but couldn’t find anything.</p>

---

## Post #2 by @lassoan (2017-04-30 19:03 UTC)

<p>We haven’t implemented a convenient user interface to reorder segments (it is tracked in this feature request: <a href="http://na-mic.org/Mantis/view.php?id=4370">http://na-mic.org/Mantis/view.php?id=4370</a>), but you can use the Segmentations module “Copy/move segments” to achieve this: Create an empty Segmentation node and move segments there. If you move the segments back in the original Segmentations node then they will be added to the end. You can select multiple segments with shift/ctrl, so it should not be too difficult to get the order you need.</p>

---

## Post #3 by @hherhold (2017-05-01 00:49 UTC)

<p>Got it, that’s a great workaround.</p>
<p>Thanks very much!!</p>
<p>-Hollister</p>

---

## Post #4 by @fedorov (2017-05-01 13:28 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> just curious - what is your use case that requires to reorder segments?</p>

---

## Post #5 by @hherhold (2017-05-24 22:08 UTC)

<p>Sorry, very slow reply.</p>
<p>It’s more of a convenience than anything else. I often group anatomical elements together in my segmentations, even if I don’t segment them in a given order. My work is primarily on insects, so I’ll separate out head, thorax, abdomen, and then separate out legs and wings, and it would be handy for those to be ordered with the thorax. I’ll also separate out abdominal organs and group those, for example.</p>
<p>Again, it’s largely a convenience thing - if I wind up with a bunch of segments, it’s useful to have “neighboring” segments close to each other in the list.</p>
<p>Hope this helps - thanks!</p>
<p>-Hollister</p>

---

## Post #6 by @fedorov (2017-05-24 23:00 UTC)

<p>Thanks a lot for these details <a class="mention" href="/u/hherhold">@hherhold</a>, it is very helpful!</p>
<p>What is the format of your image data?</p>
<p>Do you use coded terms while annotating the data, and if yes - do they belong to an ontology that is publicly available?</p>
<p>An ontology with well-defined relationships could be useful to help browsing segmentations. Perhaps this could be one direction for improvement of our infrastructure. Unfortunately, an unsolved and a very contentious topic in clinical imaging. Perhaps things are better in the world of insects! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #7 by @hherhold (2017-05-25 15:26 UTC)

<p>The data is from micro-CT scans, and it’s usually NRRD stacks I’ve made from TIFF stacks using ImageJ/Fiji. I do a fair amount of cropping and pre-processing in ImageJ to make file sizes manageable. The data itself is usually 16 bit (unsigned int), although I have a couple from synchrotrons that are 32 bit float. I’ll occasionally decimate to 8 bit unsigned if I’m not concerned about slight variations in internal anatomy - say, looking at just trachea, for example.</p>
<p>Annotations are generally just anatomical descriptions from published literature. We don’t use coded terms.</p>
<p>As far as established relationships for insect anatomy - there are some standardized relationships, even though the 30 or so orders vary widely in morphology. Some areas, however, are still debated - there are a couple different ways of describing wing venation, for example, and it can be a character for species identification. Apologies if I’m not understanding your question!</p>
<p>Hope this helps!</p>
<p>-Hollister</p>

---
