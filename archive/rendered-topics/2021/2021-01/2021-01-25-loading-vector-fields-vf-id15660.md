# Loading vector fields (.vf)

**Topic ID**: 15660
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/loading-vector-fields-vf/15660

---

## Post #1 by @marianaslicer (2021-01-25 18:10 UTC)

<p>Hello everyone,</p>
<p>Is it possible to load vector fields with .vf extension? I tried to load them in the preview release 3D Slicer version but I couldn’t do it.<br>
I would appreciate any help.<br>
Thank you.</p>

---

## Post #2 by @lassoan (2021-01-25 20:04 UTC)

<p>What software generated this file?</p>
<p>Can you save it as a NRRD volume file or ITK HDF5 transform file instead? (these are the formats Slicer can read displacement fields from)</p>
<p>If you cannot save your vector field in any of these formats then you can you have a few other options:</p>
<ul>
<li>load the .vf file as a numpy array with some Python package that can read such files, then use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray">slicer.util.updateVolumeFromArray</a> to get it into a volume node (which can then be saved as a .nrrd file)</li>
<li>use RawImageGuess extension to generate a NRRD file header (.nhdr file) that Slicer can use to load the volume</li>
</ul>

---

## Post #3 by @marianaslicer (2021-01-26 09:46 UTC)

<p>Hi Andras, thank you for your response.</p>
<p>I was trying to use the online available dataset <a href="https://www.creatis.insa-lyon.fr/rio/popi-model_original_page" rel="noopener nofollow ugc">popi-model_original_page - Rayonnement, Images, Oncologie (insa-lyon.fr)</a>, including CT images, masks and vector fields. I can load them into VV software, but I’m afraid that I cannot save them as a NRRD volume file or another format type. So, I will try to follow your suggestion. Thank you.</p>

---

## Post #4 by @lassoan (2021-01-29 06:18 UTC)

<p>The website describes the format of the data. You can use that information in <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess</a> extension.</p>

---

## Post #5 by @grupesh (2022-06-20 16:14 UTC)

<p><a class="mention" href="/u/marianaslicer">@marianaslicer</a> Were you able to use RawImageGuess module to load .vf files? If yes, can you please share that? I’m trying to use these .vf data in matlab/python and I don’t see a way to export them from VV software.</p>

---

## Post #6 by @lassoan (2022-06-21 01:57 UTC)

<p>Writing a small Python script to read these files could be a nice little project for the <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/">upcoming Slicer Project Week</a>. You can still sign up, it is virtual and participation is free of charge. You just need to describe your project in a few sentences and upload it to the project week website; present your project it in 1 minute on the first day, work with experts during the week, and present what you accomplished in 1 minute on the last day.</p>

---

## Post #7 by @grupesh (2022-06-21 18:19 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks for your suggestion. I was able to write a python script to read these .vf files and convert them to np arrays / .mhd (which works with VV, Slicer)</p>

---

## Post #8 by @lassoan (2022-06-21 18:39 UTC)

<p>Great! Would you mind sharing the script so that others can use it, too?</p>
<p>If you want to read these files conveniently (just by drag-and-dropping the file into Slicer) then you can put your script in the <code>load</code> method of a file reader plugin. See example <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py">here</a>. I would be happy to help you with this if you are OK to make the script public.</p>

---

## Post #9 by @grupesh (2022-06-22 14:53 UTC)

<p>Sure, I would be happy to share the script / add it in file reader plugin. I’m git cloning the slicer repo and adding the code. Not sure on how to test it. Happy to work with you on that.</p>

---

## Post #10 by @lassoan (2022-06-25 15:05 UTC)

<p>No need to clone the Slicer repository, as you just add a Python scripted module in an extension. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">This page</a> should help you getting started and you can ask us here if you have any questions.</p>

---

## Post #11 by @cslzq1998 (2022-08-16 12:24 UTC)

<p>Would you please share the script here?I don’t know how to convert it to a format like numpy array or medical image</p>

---
