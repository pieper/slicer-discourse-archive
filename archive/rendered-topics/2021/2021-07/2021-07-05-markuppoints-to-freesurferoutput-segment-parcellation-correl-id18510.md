---
topic_id: 18510
title: "Markuppoints To Freesurferoutput Segment Parcellation Correl"
date: 2021-07-05
url: https://discourse.slicer.org/t/18510
---

# Markuppoints to freesurferoutput segment/parcellation correlations on 2dslicer viewer

**Topic ID**: 18510
**Date**: 2021-07-05
**URL**: https://discourse.slicer.org/t/markuppoints-to-freesurferoutput-segment-parcellation-correlations-on-2dslicer-viewer/18510

---

## Post #1 by @mubafz (2021-07-05 00:49 UTC)

<p>Hi all,</p>
<p>I wanted to ask if its possible to correlate markup points one has place to segmentations/parcellation labels of freesurfer output in ones MRI. I click the markup in the 2DSlicer viewers and it indicates where it falls or closest to in the parcellation labelling by freesurfer.</p>
<p>As an example I have 189 segments/parcellations of MRI brain from freesurfer output and I have 200 contact markup points. Is there a way to click on a markup and it indicates which segment label it roughly correlates to or closest to?</p>

---

## Post #2 by @lassoan (2021-07-09 05:01 UTC)

<p>This post should help:</p>
<aside class="quote" data-post="2" data-topic="16456">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/model-identity-at-fiducial-location/16456/2">Model identity at fiducial location</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    What you do is a very robust and efficient method of determining which models contain the selected point position. If you need to pick many thousands points then I would recommend keep using this method. 
If you just want to pick models at the current point position (or hundreds of positions but not hundreds of thousands of positions) then it is simpler to <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_displayable_manager_of_a_certain_type_for_a_certain_view">get the model displayable manager from the view</a> and use its <a href="http://apidocs.slicer.org/master/classvtkMRMLModelDisplayableManager.html#a2fb2b057ef3571dae97c1c8ef73bf289">Pick3D</a> and <a href="http://apidocs.slicer.org/master/classvtkMRMLModelDisplayableManager.html#a58918fec5e28c222b26bc36470b04640">GetPickedNodeID</a> methods.
  </blockquote>
</aside>

<p>If you get stuck at any point then let us know.</p>

---
