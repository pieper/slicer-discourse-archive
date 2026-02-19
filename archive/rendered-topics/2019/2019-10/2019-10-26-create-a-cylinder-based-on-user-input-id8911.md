---
topic_id: 8911
title: "Create A Cylinder Based On User Input"
date: 2019-10-26
url: https://discourse.slicer.org/t/8911
---

# Create a cylinder based on user input

**Topic ID**: 8911
**Date**: 2019-10-26
**URL**: https://discourse.slicer.org/t/create-a-cylinder-based-on-user-input/8911

---

## Post #1 by @mpontin (2019-10-26 00:47 UTC)

<p>Hi everybody,<br>
I’m new to 3DSlicer so I don’t really know where to begin.<br>
I’m trying to develop a module in order to automatically create a cylinder based on user input.<br>
The idea is that the user selects a radius, then clicks on the point which will be the axis of the cylinder. Once the cylinder is created I want to show it and finally merge it with the previously loaded data.<br>
Any suggestion is greatly appreciated.<br>
Thank you!<br>
Marco</p>

---

## Post #2 by @Prashant_Pandey (2019-10-26 01:27 UTC)

<p>I recently needed to do this and I found the easiest method was to use the Markups to Models module included in the slicerIGT extension. This let’s you create a cylinder with at least 2 markup fiducials.</p>

---

## Post #3 by @mpontin (2019-10-27 16:33 UTC)

<p>Thanks a lot for the info Prashant_Pandey!<br>
One more question: is it possible to call the Markups to Models module from the python interactor?<br>
Based on the user input I created some fiducials in a python script. Now I would like to use these to create a closed surface automatically.<br>
Thanks</p>

---

## Post #4 by @lassoan (2019-10-27 16:58 UTC)

<p>You may also use markups lines or SegmentEditorExtraEffects extension’s Draw Tube effect. What would you like to achieve?</p>

---

## Post #5 by @mpontin (2019-10-27 17:05 UTC)

<p>Hello lassoan,<br>
The idea is that the user inserts a fiducial point in the center of the base of the cylinder and chooses a radius. Based on this information I want to automatically create a cylinder so that then I can merge the cylinder with the original volume and export as .stl<br>
Thanks</p>

---

## Post #6 by @lassoan (2019-10-27 17:14 UTC)

<p>How do you merge a cylinder (surface mesh) with a volume? If you do it in Segment Editor for that then Draw Tube effect may be the simplest method.</p>

---

## Post #7 by @mpontin (2019-10-27 17:21 UTC)

<p>I’m sorry, I’m new to Slicer and it’s not clear to me what is the simplest way forward.<br>
Based on the fact that I’d like to merge the cylinder (either obtained as surface or volume) with the existing volume in order to 3Dprint the two together, what would you suggest?<br>
Right now I have fiducials placed in a circle on two different levels on the z axis. Is it possible to create a solid cylinder starting from this configuration?<br>
Thank you very much for the patience.</p>

---

## Post #8 by @Prashant_Pandey (2019-10-28 03:17 UTC)

<p>I am sure you can access and use the logic of the Markups To Models in a python script, but I am not sure what the exact function calls are.</p>
<p>For combining the two, I would recommend converting the pertinent structure in your medical volume into a segment using a the ‘segment editor’ module and converting your cylinder model into a segment by importing it as a label map from the ‘segmentations’ module. You can then combine the two label maps and export as a surface model, which you can save as an .stl file to be used with your printer.</p>

---

## Post #9 by @lassoan (2019-10-28 11:38 UTC)

<p>Draw tube effect creates a cylinder-shape segment from input markup points, so this seems to be the most direct solution. There are also many examples of running segment editor effects from scripts in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---
