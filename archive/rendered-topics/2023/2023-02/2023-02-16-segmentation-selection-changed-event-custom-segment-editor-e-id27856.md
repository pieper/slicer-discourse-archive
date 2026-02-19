---
topic_id: 27856
title: "Segmentation Selection Changed Event Custom Segment Editor E"
date: 2023-02-16
url: https://discourse.slicer.org/t/27856
---

# Segmentation selection changed event (custom segment editor effect)

**Topic ID**: 27856
**Date**: 2023-02-16
**URL**: https://discourse.slicer.org/t/segmentation-selection-changed-event-custom-segment-editor-effect/27856

---

## Post #1 by @lukas_n (2023-02-16 10:43 UTC)

<p>I am trying to write a function that is triggered when the user selects a different segmentation in the segment editor module. I searched for such event methods but could not find the right one. My guess is that there is an event for the DisplayNode of the corresponding segmentation that is triggered when selecting a different segmentation. I tried to add an observer to each segmentation node like this without success.</p>
<pre><code class="lang-python"># I tried this
segmentationNode.AddObserver(slicer.vtkMRMLSegmentationNode.SegmentationChangedEvent, self.onSegChanged)
# and this
segmentationNode.AddObserver(slicer.vtkMRMLSegmentationDisplayNode.MenuEvent, self.onSegChanged)
</code></pre>
<p>Here is a screenshot to further illustrate what I want to achieve.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb4b99a7700cb010136f38708c99b76aff7c5150.png" alt="tempsnip" data-base62-sha1="zR3OHzNuQI6dqnNt9gGbUBmhGAU" width="482" height="154"></p>
<p>I want to create an event method that triggers when “Segmentation_1” is changed to a different segmentation.</p>
<p>Thanks for the help in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @rajmadhan (2024-03-26 22:38 UTC)

<p>Hi Lukas,<br>
Do you by any chance able to find a solution for this problem?</p>

---

## Post #3 by @lukas_n (2024-03-28 12:35 UTC)

<p>Hello Raj,<br>
thanks for your reply, sadly I don’t work on this project anymore… I could not find a solution for this, but the problem was not that critical. It was a nice-to-have feature of the slicer plugin I made. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2024-03-28 15:42 UTC)

<p>You can use the <a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a4df0865783eaabce916723c830f3f287">segmentationNodeChanged</a> signal of the segment editor widget.</p>

---

## Post #5 by @rajmadhan (2024-04-01 22:09 UTC)

<p>Thanks for the reply.<br>
I found the solution based on <a class="mention" href="/u/lassoan">@lassoan</a> Andras Lasso response.</p>

---

## Post #6 by @rajmadhan (2024-04-01 22:13 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>  Andras Lasso,<br>
Thanks for your response.<br>
<a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a4df0865783eaabce916723c830f3f287" rel="noopener nofollow ugc">segmentationNodeChanged</a> signal didn’t work for my problem. This sends the signal when ever I changed the segmentation node, i.e., when a new image is loaded.<br>
<a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a9172bd5ffebecf7f8f71da4faddc9ace" rel="noopener nofollow ugc">currentSegmentIDChanged</a> worked as I expected. This sends the signal whenever I change selection of the segment in the segment editor widget.</p>

---
