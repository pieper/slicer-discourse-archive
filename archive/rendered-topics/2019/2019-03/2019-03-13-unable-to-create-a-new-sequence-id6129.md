---
topic_id: 6129
title: "Unable To Create A New Sequence"
date: 2019-03-13
url: https://discourse.slicer.org/t/6129
---

# Unable to create a new sequence

**Topic ID**: 6129
**Date**: 2019-03-13
**URL**: https://discourse.slicer.org/t/unable-to-create-a-new-sequence/6129

---

## Post #1 by @Jainey (2019-03-13 11:39 UTC)

<p>Hi ,Sorry for posting this again.<br>
I am trying to create new sequence out of several multivolume sequences.<br>
I have about 3-5 frames in each multivolume sequence that I want to play back together.<br>
I ve selected the first sequence as the active node in the sequences module and added subsequent sequences on to that by left arrow key.</p>
<p>My problems</p>
<ol>
<li>The subsequent sequences does not show all the frames , they get sent to the left hand box as one single entity, not as separate frames.<br>
2.When I play back , it only show the original sequence, the second one is not added</li>
</ol>
<p>Thank you very much</p>

---

## Post #2 by @lassoan (2019-03-13 12:40 UTC)

<p>Would you like to concatenate them into a long sequence or replay them in sync?</p>
<p>Have you loaded the .nrrd files as MultiVolume nodes or as Volume Sequence nodes (using Sequences extension)? A .nrrd file is loaded by default as MultiVolume - you need to choose “Volume Sequence” in the “Description” column to load it as a Volume Sequence that you can edit in Sequences module. You can make a .nrrd file loaded as Volume Sequence by default, by changing the file extension from .nrrd to .seq.nrrd.</p>

---

## Post #3 by @Jainey (2019-03-13 16:19 UTC)

<p>Thank you very much Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a>. Yes I am im trying to concatenate them into a long sequence.</p>
<p>I have loaded them as a volume sequence, not as .nrrd.<br>
Is it possible to do it while keeping this as a volume sequence.<br>
Actually I want to make a long sequence out of output volume frames that are resulted by sequence registration.<br>
Any advice please. Thanks</p>

---

## Post #4 by @lassoan (2019-03-13 17:40 UTC)

<p>To concatenate sequences, probably the simplest is to load all the sequences into the scene and then copy-paste <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Concatenate_all_sequences_in_the_scene_into_a_new_sequence" rel="nofollow noopener">this script</a> into the Python console.</p>

---

## Post #5 by @Jainey (2019-03-17 01:01 UTC)

<p>Thank you very much Prof@lassoan</p>

---

## Post #6 by @Jainey (2019-03-19 12:32 UTC)

<p>Hi Prof. Lasso, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Many thanks for the help.<br>
Sorry to continue the same thread but I have two questions and will be grateful if you could help.</p>
<ol>
<li>
<p>I want to create a sequence of output volumes. i.e after image registration of multiple frames, I create about 10 output volumes. This is because I try to reference the fisrt frame to the second and then the second to the third rather than do it all at once. I expect the accuracy will be more if I do that.<br>
My question is if I concatenate all output volumes will that automatically give me the transformation sequence to calculate displacement using fiducial markers.</p>
</li>
<li>
<p>I am trying to segment my images, which are bones. Sp If I achieve frame 1 segmented stl model and save it , and then try to do the next frame segmentation they overlap. What should I do to get individual segmented models for each frame without overlapping, please. only way I can think is load the sequence repeatedly and get the frame of interest and delete all others and segment and save. Probably do this procedure for multiple  frames. Is there an easy alternative.</p>
</li>
<li>
<p>If I do this somehow, can I make a sequence of STL files that can be registered using elastix- please<br>
Thanks a lot<br>
Please let m know if I need to create a separate thread for this.<br>
Thanks<br>
Jain</p>
</li>
</ol>

---

## Post #7 by @lassoan (2019-03-19 12:51 UTC)

<aside class="quote no-group" data-username="Jainey" data-post="6" data-topic="6129">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>My question is if I concatenate all output volumes will that automatically give me the transformation sequence to calculate displacement using fiducial markers.</p>
</blockquote>
</aside>
<p>Yes. Once you have your input as a volume sequence, you can use Sequence Registration extension to compute transform sequence that you can apply to markup fiducials.</p>
<aside class="quote no-group" data-username="Jainey" data-post="6" data-topic="6129">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>What should I do to get individual segmented models for each frame without overlapping</p>
</blockquote>
</aside>
<p>You can allow overlapping of segments (without overwriting each other) by setting “Overwrite other segments” → “None” in Masking section Segment Editor module. Since you will have all segments in a single segmentation node, you cannot switch between the segments using Sequence Browser.</p>
<p>If you want to create a segmentation sequence for a volume sequence then follow instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Example:_Create_a_segmentation_node_sequence" class="inline-onebox">Documentation/Nightly/Extensions/Sequences - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="Jainey" data-post="6" data-topic="6129">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>If I do this somehow, can I make a sequence of STL files that can be registered using elastix</p>
</blockquote>
</aside>
<p>If you have a volume sequence then you can use Sequence Registration extension to register the frames to each other using Elastix.</p>

---
