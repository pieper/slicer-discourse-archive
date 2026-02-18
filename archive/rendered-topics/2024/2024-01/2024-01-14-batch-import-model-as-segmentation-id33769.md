# Batch import model as segmentation?

**Topic ID**: 33769
**Date**: 2024-01-14
**URL**: https://discourse.slicer.org/t/batch-import-model-as-segmentation/33769

---

## Post #1 by @dantaylor (2024-01-14 16:27 UTC)

<p>I have an array made up of hundreds of individual .STL files that I’d  want to import into a CT volume in order to query HU values in specific regions.  I can drag/drop the array into 3D Slicer, then the popup menu asks if I want them imported as model or segmentations… problem is that I have to click each individual line item if I want it to be a segmentation - this is tedious and I wondered if I can do this as a batch somehow.  I have also tried to select all the models at once and convert to segmentation, but this ends up bogging down my PC for hours… and sometimes the PC crashes before it is complete.  Is there a better way?</p>

---

## Post #2 by @pieper (2024-01-14 16:58 UTC)

<p>In the Add Data dialog, you can hold down the shift key while switching one of the file entries to a Segmentation and they’ll all change.</p>
<p>You might still run into the issue that using these files as segmentations is computationally heavy.</p>

---

## Post #3 by @dantaylor (2024-01-14 17:01 UTC)

<p>Great, thanks for the response! I will try it as soon as the current conversion is completed!</p>

---

## Post #4 by @dantaylor (2024-01-14 20:13 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, the shift-select method worked to change all file entries into a segmentation, that’s non-intuitive but extremely useful - thanks again for that tip.  Unfortunately, after the Add Data completes, each file is imported as a segment inside its own segmentation, but I need them all to be within a single segmentation so I can collect the statistics in a single table.  Is there a way to transfer them all into a single segmentation?</p>

---

## Post #5 by @pieper (2024-01-14 21:46 UTC)

<p>You can use copy/move segments in the Segmentations module.  If you have a lot to do probably scripting is more efficient.</p>
<p>I agree the Shift key trick to change all the types is not discoverable.  I’m not sure who added that feature - maybe someone who thought it would be a handy thing for themselves and couldn’t think of a way to expose it cleanly in the UI.</p>

---

## Post #6 by @dantaylor (2024-01-14 22:13 UTC)

<p>Thanks, Steve.  Definitely can’t manually copy/move in module, it takes forever.  I will try to learn how to do the scripting thing.  Any guidance in that direction would be much appreciated, as I’m going to start from zero.</p>

---

## Post #7 by @pieper (2024-01-14 22:21 UTC)

<p>There are lots of examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">segmentations section of the script repository</a>.  There may not be an exact example of doing that, but you could use this method<br>
<code>bool vtkSegmentation::CopySegmentFromSegmentation(vtkSegmentation* fromSegmentation, std::string segmentId, bool removeFromSource/*=false*/)</code></p>
<p>If that’s not clear, you’ll need to start working through some of the scripting documentation.  HTH.</p>

---

## Post #8 by @dantaylor (2024-01-15 00:19 UTC)

<p>Excellent, thanks very much!</p>

---

## Post #9 by @pieper (2024-01-15 17:32 UTC)

<p>You might also want to ask one of the new chatbots (or ask several since they all might give differently wrong answers).  Phind, bard, bing, perplexity, chatgpt, etc all seem to give reasonable starting points for automating slicer functions with python scripts.</p>

---
