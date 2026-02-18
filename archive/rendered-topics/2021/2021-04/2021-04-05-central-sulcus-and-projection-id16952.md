# Central sulcus and projection

**Topic ID**: 16952
**Date**: 2021-04-05
**URL**: https://discourse.slicer.org/t/central-sulcus-and-projection/16952

---

## Post #1 by @Pierpaolo_Croce (2021-04-05 19:31 UTC)

<p>Dear Community,<br>
I would like to segment the central sulcus from an mri and then project all the points of the segmented sulcus to the scalp in order to obtain the shape of the sulcus on the scalp. There are similar tasks from which I can start? Any suggestions?</p>

---

## Post #2 by @lassoan (2021-04-06 13:46 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do you have any suggestions?</p>

---

## Post #3 by @Sunderlandkyl (2021-04-06 14:49 UTC)

<p>It’s different from what we’ve done with the parcellation, so I’m not sure I have any good suggestions.</p>
<p>You might try the following:</p>
<ul>
<li>Segment the white matter using “Grow Cut” or “<a href="https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233">Local threshold</a>”</li>
<li>Trace the path along the central sulcus using markup curve (<a href="https://discourse.slicer.org/t/new-feature-draw-curve-on-surface/10431" class="inline-onebox">New feature: draw curve on surface</a>).</li>
<li>Project the path of the curve back onto the scalp.</li>
</ul>

---

## Post #4 by @Pierpaolo_Croce (2021-04-06 15:52 UTC)

<p>Many thanks,<br>
this would be very helpful!!!<br>
Could you suggest to me how the projection should be done?<br>
Which tool should I use?<br>
Sorry but I’m a 3dslicer beginner!</p>

---

## Post #5 by @Sunderlandkyl (2021-04-06 19:05 UTC)

<p>The resample section of the markups module could be used to map the points on the white matter curve to the closest points on the scalp mesh.</p>

---

## Post #6 by @smrolfe (2021-04-06 19:15 UTC)

<p>I have some python example <a href="https://github.com/SlicerMorph/SlicerMorph/blob/10f0a9d251194205ba984397063713527225748a/CreateSemiLMPatches/CreateSemiLMPatches.py#L601" rel="noopener nofollow ugc">here</a> that projects the control points of a curve on one surface to another by expansion/contraction along the normal vectors of the original surface.</p>

---

## Post #7 by @Pierpaolo_Croce (2021-04-06 19:25 UTC)

<p>Thank you very much! I will go through the code…</p>

---

## Post #8 by @Pierpaolo_Croce (2021-04-07 16:13 UTC)

<p>Since we would like to have a semi automatic procedure, I was wondering if it’s possibile to apply such a procedure to the freesurfer labelled output? In particular, leave only the precentral and postcentral cortical structures and then project such surfaces on the scalp. Is it in principle doable?</p>

---

## Post #9 by @Sunderlandkyl (2021-04-07 16:20 UTC)

<p>Yes, for parcellation we draw trace sulci on imported FreeSurfer surfaces.<br>
You can even perform weighted pathfinding using imported curv and sulc overlay.</p>
<p>If you want to import FreeSurfer files, you just need to install the SlicerFreeSurfer extension.</p>
<p>This video has an example of the sulcal tracing (at 51seconds):</p><div class="youtube-onebox lazy-video-container" data-video-id="UeGhzSGUZOA" data-video-title="Drawing curves on surface mesh" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UeGhzSGUZOA" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UeGhzSGUZOA/maxresdefault.jpg" title="Drawing curves on surface mesh" width="" height="">
  </a>
</div>


---

## Post #10 by @Pierpaolo_Croce (2021-04-10 17:16 UTC)

<p>Thanks for sharing.<br>
It is possible to use segment editor tools on freesurfer imported models? As for segmentation for example scissors etc?</p>

---
