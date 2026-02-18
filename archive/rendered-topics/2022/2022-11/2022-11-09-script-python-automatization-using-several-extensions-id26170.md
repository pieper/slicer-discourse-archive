# Script Python - Automatization using several extensions.

**Topic ID**: 26170
**Date**: 2022-11-09
**URL**: https://discourse.slicer.org/t/script-python-automatization-using-several-extensions/26170

---

## Post #1 by @lucas_sd (2022-11-09 17:18 UTC)

<p>Hi everyone,</p>
<p>Currently, Im using the modules Extract Centerline and Curved Planar Reformat, in order to obtain a straightened volume from a data set DICOM.</p>
<p>I have to do that for several examples, so I wondering if is possible to create a python script to automate the process; just charge the segmentation and points like the imput of the script, and obtain a straightened volume like the output.</p>
<p>Its possible this? Which is the way/syntax to interact with the input and output of each module? There are some examples about that? Or maybe an anorher way?</p>
<p>The workflow is:<br>
inputs_1 (points and segmentation)<br>
Center line code<br>
Output_1(center line)<br>
Inputs_2(center line and data)<br>
Straightened volume<br>
Output_2(Straightened volume)</p>
<p>Thanks, Lucas.</p>

---

## Post #2 by @lassoan (2022-12-01 07:25 UTC)

<p>Yes, this should not be too hard, even if you are completely new to Slicer. After you completed the Slicer programming tutorial (I would recommend <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">this one</a>, but there are many more on youtube), you can have a look at examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> and self-tests in VMTK and other extensions and ask here if you have any specific questions.</p>

---

## Post #3 by @lucas_sd (2022-12-02 18:49 UTC)

<p>Thanks! Finally, I could understand how to call or work with other modules from my script.</p>
<p>In the case of the module <em>curved planar reformat</em>, I imported the module and then I copied and edited the test case in terms of my variables and preferences. This also allowed me to understand precisely the importance of the logical class.</p>

---
