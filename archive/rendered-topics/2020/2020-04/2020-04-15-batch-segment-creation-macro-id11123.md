# Batch segment creation - macro

**Topic ID**: 11123
**Date**: 2020-04-15
**URL**: https://discourse.slicer.org/t/batch-segment-creation-macro/11123

---

## Post #1 by @Ezio_Lanza (2020-04-15 11:15 UTC)

<p>Dear all,</p>
<p>Is there a way to instruct segment editor to do the following operations with one click ? Let me offer an example:</p>
<p>I have the segment LUNG which comprises the whole lung volume.<br>
I would like with one click to order Slicer do the following operations:</p>
<p>a) Create a new segment “Newsegment”<br>
b) Use the Threshold tool to populate a new segment with the intervals -1000HU-100HU inside LUNG without overwriting other segments.</p>
<p>Is it there an easy way to do it?</p>
<p>Thanks a lot for your help.</p>

---

## Post #2 by @cpinter (2020-04-15 12:29 UTC)

<p>It should be pretty easy to do with some python scripting. See lots of examples here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>
<p>Once you have a script, if you want it to have its own effect button, then it’s easy to add too.</p>

---

## Post #3 by @Ezio_Lanza (2020-04-22 14:27 UTC)

<p>Hello, thanks for helping and sorry for bothering. I’m really new to python and only have experience on HTML coding. But I’m willing to learn.<br>
I got to the point where I created a test module using the extension manager.<br>
I found a useful example here <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" rel="nofollow noopener">https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37</a></p>
<p>But I cannot get past the way to use the current volume that I have selected in the drop down menu.<br>
How do I access it in the script?</p>
<p>I need to replace the following line</p>
<p>masterVolumeNode = SampleData.SampleDataLogic().downloadCTChest()</p>
<p>with something that fills the variable masterVolumeNode with the volume currently selected in the InputVolume dropdown menu.<br>
Couldn’t find easy answer until now</p>

---

## Post #4 by @lassoan (2020-04-22 14:41 UTC)

<p>These are explained in detail, with examples in Slicer programming tutorials, such as <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">this</a>.</p>

---

## Post #5 by @Ezio_Lanza (2020-04-22 18:31 UTC)

<p>Thanks Andras, your work is amazing.<br>
Just wanted to let you know that thanks to your indications  I am getting super-close to creating what I need.</p>

---
