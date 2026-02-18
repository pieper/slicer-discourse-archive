# Question About Loading Data in 3D Slicer

**Topic ID**: 11686
**Date**: 2020-05-25
**URL**: https://discourse.slicer.org/t/question-about-loading-data-in-3d-slicer/11686

---

## Post #1 by @eKwas (2020-05-25 01:44 UTC)

<p>Hello:</p>
<p>When loading data (not DICOM) into 3D Slicer (using Windows 10 Slicer version 4.11.0, but I have had this same issue with 4.10.2), is there a way to change the presets (what appears when you click “Show Options”). More specifically, I want to have 3D Slicer automatically make the column of boxes labelled “Single File” unchecked when it loads my images (by default, this is a checked box-column). What would also help is a means by which to select many of these boxes at a time (rather than one box at a time, which is how I currently work); is there a way to do this? I commonly work with hundreds of images at a time, so unchecking all of these one-by-one can be quite laborious.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-05-25 02:02 UTC)

<p>If you need to repeat the same operation more than a couple of times, then it may worth writing a short python script to automate it. For example, you can write a module that loads your data set with exactly how you want them to be loaded. You can find lots of examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file">script repository</a>. You can learn more about scripting and module creation in Slicer from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">these tutorials</a>.</p>

---
