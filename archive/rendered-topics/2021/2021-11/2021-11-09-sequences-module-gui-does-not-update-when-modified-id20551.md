---
topic_id: 20551
title: "Sequences Module Gui Does Not Update When Modified"
date: 2021-11-09
url: https://discourse.slicer.org/t/20551
---

# Sequences module GUI does not update when modified

**Topic ID**: 20551
**Date**: 2021-11-09
**URL**: https://discourse.slicer.org/t/sequences-module-gui-does-not-update-when-modified/20551

---

## Post #1 by @mikebind (2021-11-09 19:33 UTC)

<p>I used the Crop Volume Sequence module to create a new cropped version of a volume sequence.  This worked fine, but the resulting sequence is not listed in the Sequences module, despite it clearly having been added to the original sequence browser as a synchronized sequence (because changing the frame in the browser changes the frame in the cropped sequence).  I can’t figure out how to get the GUI to update to reflect the current state.  From general experience with Slicer I suspect that a “somethingModified” event was not fired somewhere, but I don’t know where or how to trigger it myself if the Crop Volume Sequence module missed it. Any suggestions?</p>
<p>Getting the browserNode and calling <code>browserNode.Modified()</code> didn’t do it. It seems like the Sequences module is CLI style, which I understand less well, and doesn’t seem to have the equivalent to an <code>updateGUIFromParameterNode()</code> function, which was another idea I thought to try.</p>

---

## Post #2 by @lassoan (2021-11-09 20:00 UTC)

<p>Sequences module GUI refresh was very expensive, which slowed down sequence replay. Therefore, (years ago) the code was reworked to minimize the number of updates, and as a side effect, in some cases changes that should be detected and cause a GUI update may be missed. If you can provide a list of steps that we can follow to reproduce the issue then we can have a look.</p>

---

## Post #3 by @mikebind (2021-11-09 20:21 UTC)

<p>Thanks!</p>
<p>Here are the steps I followed:</p>
<ol>
<li>Load a volume sequence</li>
<li>Open Crop Volume Sequence module
<ol>
<li>Select volume sequence as input</li>
<li>Select “Create new sequence” for output</li>
<li>Click to jump to Crop Volume module</li>
</ol>
</li>
<li>In Crop Volume module,
<ol>
<li>select proxy volume as input</li>
<li>Select “Create new MarkupsROI”</li>
<li>Click “Fit to Volume”</li>
<li>Manually adjust boundaries to desired location</li>
<li>Choose “Create new volume” as output (I think this was unnecessary)</li>
</ol>
</li>
<li>Go back to Crop Volume Sequence module and ensure that “CropVolumeParameters” was selected</li>
<li>Click “Apply”</li>
</ol>
<p>After this process, the new cropped volume sequence was created (as well as an invalid scalar volume that I think was due to my choice of “Create new volume” as output in the Crop Volume module).  The output sequence is named “Sequence”, is automatically displayed in the slice views, and changes with the frame change of the previously existing sequence browser. So far, this is all exactly what I want to happen, but if I go to the Sequences module, the new Sequence is not listed in the list of synchronized nodes, so I can’t, for example, change whether I want the sequence proxy node to be renamed with frame changes (I don’t in this case) or whether I want to “save changes” in the proxy node into the sequence node (I do).</p>
<p>Let me know if you have any trouble reproducing.</p>

---
