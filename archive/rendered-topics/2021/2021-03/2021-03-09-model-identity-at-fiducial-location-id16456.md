# Model identity at fiducial location

**Topic ID**: 16456
**Date**: 2021-03-09
**URL**: https://discourse.slicer.org/t/model-identity-at-fiducial-location/16456

---

## Post #1 by @maloman (2021-03-09 17:00 UTC)

<p>Hi all,</p>
<p>I am trying to do a simple thing: For a fiducial markups list i want to output the model in a model list each fiducial point is intersecting with.</p>
<p>Currently I am using a cumbersome approach where i convert the fiducial RAS coordinates to a VolumeNode space of a Labelmap that has all the models in it. I then sample each point in that space.</p>
<p>Is there an easier way to script this directly without the conversions to labelmap?</p>
<p>Thanks in advance</p>
<p>Jan</p>

---

## Post #2 by @lassoan (2021-03-09 18:14 UTC)

<p>What you do is a very robust and efficient method of determining which models contain the selected point position. If you need to pick many thousands points then I would recommend keep using this method.</p>
<p>If you just want to pick models at the current point position (or hundreds of positions but not hundreds of thousands of positions) then it is simpler to <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_displayable_manager_of_a_certain_type_for_a_certain_view">get the model displayable manager from the view</a> and use its <a href="http://apidocs.slicer.org/master/classvtkMRMLModelDisplayableManager.html#a2fb2b057ef3571dae97c1c8ef73bf289">Pick3D</a> and <a href="http://apidocs.slicer.org/master/classvtkMRMLModelDisplayableManager.html#a58918fec5e28c222b26bc36470b04640">GetPickedNodeID</a> methods.</p>

---

## Post #3 by @maloman (2021-03-09 19:14 UTC)

<p>Thanks Andras, I guess i will continue using that approach then <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
