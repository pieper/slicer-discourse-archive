---
topic_id: 43232
title: "Create A Script To Use Totalsegmentator From Script For 2 Sm"
date: 2025-06-05
url: https://discourse.slicer.org/t/43232
---

# Create a script to use TotalSegmentator from script for 2 small tasks

**Topic ID**: 43232
**Date**: 2025-06-05
**URL**: https://discourse.slicer.org/t/create-a-script-to-use-totalsegmentator-from-script-for-2-small-tasks/43232

---

## Post #1 by @Sebastiets (2025-06-05 14:39 UTC)

<p>Hi,<br>
I have a small project and being pretty new to programming, I’m having difficulties finding the right code to call some option.</p>
<p>Let me describe what I’m trying to do and the steps. I also have an other question not absolutely related to this subject, but if some of you want to help, always appreciated.</p>
<p>I need to segment the Femur, patela, fibulla and tibia of a CT scan. The best option I found was TotalSegmentator. To do so, I do a first segmentation with total to get the femur (as it’s separated from the appendicular bone licenced bones segmented). I run it on normal (not fast to get the best quality). I then have a segmentation of multiple bones with the femur.</p>
<p>I then return to TotalSegmentator, select “Appendicular bones” for the segmentation of tibia, patella and fibulla and run it on normal without forgetting the “Create new segmentation on Apply” option. This creates a new segmentation with all the bones with the three of interest.</p>
<p>I then want to move the bones I want in the second segmentation and the ones to delete in the first.</p>
<p>So in step, my scripts need to do these :</p>
<ol>
<li>Segmentation task → total</li>
<li>Apply</li>
<li>select normal mode</li>
<li>wait for segmentation to finish</li>
<li>segmentation task → appendicular …</li>
<li>Segmentation → Create new segmentation on Apply</li>
<li>Apply</li>
<li>wait for segmentation to finish</li>
<li>move the desired segmentation to second group and move unwanted in first group</li>
</ol>
<p>To give you an idea of my level of programming, here’s what I got so far<br>
slicer.util.selectModule(“TotalSegmentator”)</p>
<p>All help is welcomed!</p>

---

## Post #3 by @Sebastiets (2025-06-16 19:53 UTC)

<p>After a week, I arrived to this script. It runs TotalSegmentator on “Total” and “Appendicular bones” and keeps only the interested bones. Finally, it changes the name of certain bones to uniform the names.</p>
<p>Here it is for future reference :<br>
import slicer<br>
from qt import QProgressDialog</p>
<p>slicer.app.pythonConsole().clear()</p>
<p>def show_progress(message):<br>
“”“Display modal progress dialog.”“”<br>
progress = QProgressDialog()<br>
progress.setLabelText(message)<br>
progress.setCancelButton(None)<br>
progress.setWindowModality(2)  # ApplicationModal<br>
progress.setMinimum(0)<br>
progress.setMaximum(0)<br>
progress.show()<br>
slicer.app.processEvents()<br>
return progress</p>
<p>def run_total_segmentator(volumeNode, task, segmentationName, fast=True):<br>
logic = slicer.modules.totalsegmentator.widgetRepresentation().self().logic<br>
segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”, segmentationName)</p>
<pre><code>progress = show_progress(f"Running TotalSegmentator: {task}...")
logic.process(
    inputVolume=volumeNode,
    outputSegmentation=segmentationNode,
    task=task,
    fast=fast
)
progress.close()
print(f"✅ Finished: {segmentationName}")
return segmentationNode
</code></pre>
<h1><a name="p-126031-step-1-get-the-first-scalar-volume-in-the-scene-1" class="anchor" href="#p-126031-step-1-get-the-first-scalar-volume-in-the-scene-1" aria-label="Heading link"></a>Step 1 – Get the first scalar volume in the scene</h1>
<p>volumeNode = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLScalarVolumeNode”)<br>
if not volumeNode:<br>
raise RuntimeError(“<img src="https://emoji.discourse-cdn.com/twitter/cross_mark.png?v=15" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> No scalar volume found in the scene.”)</p>
<h1><a name="p-126031-step-2-run-first-segmentation-with-tasktotal-2" class="anchor" href="#p-126031-step-2-run-first-segmentation-with-tasktotal-2" aria-label="Heading link"></a>Step 2 – Run first segmentation with task=“total”</h1>
<p>seg1 = run_total_segmentator(volumeNode, task=“total”, segmentationName=“Seg_Total”, fast=False)</p>
<h1><a name="p-126031-step-3-run-second-segmentation-with-taskappendicular_bones-3" class="anchor" href="#p-126031-step-3-run-second-segmentation-with-taskappendicular_bones-3" aria-label="Heading link"></a>Step 3 – Run second segmentation with task=“appendicular_bones”</h1>
<p>seg2 = run_total_segmentator(volumeNode, task=“appendicular_bones”, segmentationName=“Seg_Appendicular”, fast=False)</p>
<p>print(“<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> Both segmentations complete. ‘Seg_Appendicular’ is now visible.”)</p>
<h1><a name="p-126031-step-4-remove-all-unnecessary-segments-except-fibula-tibia-fmur-and-patella-4" class="anchor" href="#p-126031-step-4-remove-all-unnecessary-segments-except-fibula-tibia-fmur-and-patella-4" aria-label="Heading link"></a>Step 4 - Remove all unnecessary segments except Fibula, Tibia, Fémur and Patella</h1>
<h1><a name="p-126031-keywords-to-keep-case-insensitive-5" class="anchor" href="#p-126031-keywords-to-keep-case-insensitive-5" aria-label="Heading link"></a>Keywords to keep (case-insensitive)</h1>
<p>keywords_to_keep = [‘left femur’, ‘patella’, ‘tibia’, ‘fibula’]</p>
<h1><a name="p-126031-create-new-segmentation-node-to-collect-matching-segments-6" class="anchor" href="#p-126031-create-new-segmentation-node-to-collect-matching-segments-6" aria-label="Heading link"></a>Create new segmentation node to collect matching segments</h1>
<p>newSegNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”, “FilteredSegments”)</p>
<h1><a name="p-126031-ensure-it-has-a-display-node-7" class="anchor" href="#p-126031-ensure-it-has-a-display-node-7" aria-label="Heading link"></a>Ensure it has a display node</h1>
<p>if not newSegNode.GetDisplayNode():<br>
newSegNode.CreateDefaultDisplayNodes()</p>
<h1><a name="p-126031-get-all-existing-segmentation-nodes-before-creating-the-new-one-8" class="anchor" href="#p-126031-get-all-existing-segmentation-nodes-before-creating-the-new-one-8" aria-label="Heading link"></a>Get all existing segmentation nodes BEFORE creating the new one</h1>
<p>existingSegmentNodes = list(slicer.util.getNodes(‘vtkMRMLSegmentationNode*’).values())</p>
<h1><a name="p-126031-loop-through-original-segmentation-nodes-only-9" class="anchor" href="#p-126031-loop-through-original-segmentation-nodes-only-9" aria-label="Heading link"></a>Loop through original segmentation nodes only</h1>
<p>for segNode in existingSegmentNodes:<br>
if segNode == newSegNode:<br>
continue</p>
<pre><code>segmentation = segNode.GetSegmentation()
segmentIdsToCopy = []

# Identify segments to keep
for i in range(segmentation.GetNumberOfSegments()):
    segmentId = segmentation.GetNthSegmentID(i)
    segmentName = segmentation.GetSegment(segmentId).GetName()
    segmentNameLower = segmentName.lower()
    if any(keyword in segmentNameLower for keyword in keywords_to_keep):
        print(f"Keeping segment: {segmentName}")
        segmentIdsToCopy.append(segmentId)
    else:
        print(f"Discarding segment: {segmentName}")

# Copy segments to new node and rename if needed
for segmentId in segmentIdsToCopy:
    existingSegmentIds = set(newSegNode.GetSegmentation().GetSegmentIDs())
    success = newSegNode.GetSegmentation().CopySegmentFromSegmentation(segmentation, segmentId)
    if success:
        newSegmentIds = set(newSegNode.GetSegmentation().GetSegmentIDs()) - existingSegmentIds
        if newSegmentIds:
            newSegmentId = newSegmentIds.pop()
            originalName = segmentation.GetSegment(segmentId).GetName().lower()
            if 'left femur' in originalName:
                newSegNode.GetSegmentation().GetSegment(newSegmentId).SetName('Femur')
            elif 'tibia' in originalName:
                newSegNode.GetSegmentation().GetSegment(newSegmentId).SetName('Tibia')

# Remove original segmentation node from scene
print(f"Removing original segmentation node: {segNode.GetName()}")
slicer.mrmlScene.RemoveNode(segNode)
</code></pre>

---
