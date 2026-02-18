# Export DICOM series of volume with a model as ROI

**Topic ID**: 1403
**Date**: 2017-11-08
**URL**: https://discourse.slicer.org/t/export-dicom-series-of-volume-with-a-model-as-roi/1403

---

## Post #1 by @TMC (2017-11-08 12:02 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.6.2</p>
<p>Dear forum,</p>
<p>I just began to discover 3D slicer as a software to handle 3D-scans of µCT.<br>
Normally I use the software delivered with my system (for research purposes). Hence a cooperation with an other team I’m “forced” to use 3D slicer.<br>
They send my a lot of files which I would like to analyse the way I used to do with my own samples (because I already begun to analyse my samples that way, and I cant change it during the study).<br>
The study is about analyzing human stapes.</p>
<p>Here is the problem:<br>
They send me 9 Volumes with a total of 15 samples in each volume.<br>
The Files are nrrd. Which normally is actually fine for me.<br>
But I cant figure which of specimens is which because they are all “unsorted”.<br>
The other Team did a segmentation of all of them and sorted them (which is good for me) and created an 3D-Model (.ply).<br>
As well they delivered a label map as .nnrd.</p>
<p>Here is the question:</p>
<p>For my analysis I need a single DICOM series of all of the specemin.<br>
Creating a DICOM series is easy. But I can’t get slicer to use the .ply file as an ROI.</p>
<p>Right now my approach is to load the nrrd file with all of the specemin, then load the 3D Model of one of the specimen and then create an ROI in the “Crop Volume” Module (wait for a long time) and then use this sub volume to “Create a DICOM Series”.</p>
<p>The real qestion is:</p>
<p>Is there a way to use the .ply file as an ROI for the export of an image series of just one of the specimen.<br>
Or is there any other way to speed up the process?</p>
<p>I hope I did not confuse you with so much information, if you have any questions feel free to ask</p>
<p>Best</p>
<p>TMC</p>

---

## Post #2 by @cpinter (2017-11-08 15:40 UTC)

<p>Hi! I’m having a hard time understanding what you want to do exactly, especially why you want to crop the volume with the model, because as you say the model contains a segmentation. You also say a labelmap is also provided, but I’m not sure if you want to use it for anything.</p>
<p>A few tips until we get a clearer picture:</p>
<ol>
<li>Please use the latest stable (4.8.0), as the version you use is more than a year old</li>
<li>Use the Data module for exporting into DICOM, as explained <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM">here</a>
</li>
<li>If you want to export to DICOM-RT (either the ply or the labelmap as the structure set), then you’ll need to create a “Segmentation” node from that. Please refer to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations#How_to">this description</a> (second point)</li>
</ol>

---

## Post #3 by @lassoan (2017-11-08 15:46 UTC)

<p>Yes, it’s not yet clear if you need:</p>
<ul>
<li>A. crop by a rectangular box</li>
<li>B. blank out all the voxels outside the segment</li>
</ul>
<p>What analysis do you need to do on the data?<br>
What software do you use for that now?<br>
Can that software import DICOM-RT structure sets?</p>
<p>You can speed up the process/make it completely automatic by Python scripting (see <a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Slicer4_Programming_Tutorial">this tutorial</a> to get started).</p>

---

## Post #4 by @TMC (2017-11-13 11:33 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/cpinter">@cpinter</a>,</p>
<p>thank you for your replys.<br>
I’m downloading the nightly build right now. And as well I’ll look into the Data module.<br>
About the DICOM-RT, I’m not sure I’d understand the difference to DICOM.<br>
The software I use, it is the standard software delivered from Bruker microCT. It is called CTAnalyzer.<br>
It can open DICOM but I’m not sure it would open DICOM-RT.<br>
The measurements we need are just some basic information about the stapes. Like hight, area and angle.<br>
I guess I could do this as well easily in slicer but since the study started using our µCT and the software, a change is (in my opinion) not recommended.</p>
<p>What I want to achieve is to export all of the stapes which are in one big volume.<br>
I have the label map and the ply models but I’m not able to figure out how to export all of them into separate DICOM series (or any other picture format like png, tiff).<br>
There must be an easy way. I just didn’t find it jet. (But I look into the Data module of the nightly build )</p>
<p>Best Tobias</p>

---

## Post #5 by @TMC (2017-11-13 12:37 UTC)

<p>Dear Iassoan,</p>
<p>well yes all I need is to blank out the voxels outside the segment. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I guess I really have all the necessary information about the data set in the label map and the ply models but i can’t figure it out how to achieve what I want. And maybe my approach is not the best, but it’s the way I want to do this ^^.</p>
<p>I tried to use the segmentation module to create a segment of one of the models.<br>
The I used the data module to “right klick” and “export to DICOM” module.<br>
But from there I cant export only the voxels inside the segmentation into a DICOM series of the greyvalues.</p>
<p>Many thanks so far</p>
<p>Best</p>

---

## Post #6 by @lassoan (2017-11-13 15:47 UTC)

<p>To blank out areas of a volume, use Mask Volume effect in Segment editor (see <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4">https://www.youtube.com/watch?v=xZwyW6SaoM4</a> for a short tutorial).</p>
<p>Generic micro-CT software will not likely to understand DICOM-RT information objects (such as RTSTRUCT for storing segments) or DICOM segmentation objects, so you need to export the modified scalar volume as a CT volume, using Data module as <a class="mention" href="/u/cpinter">@cpinter</a> suggested. See step-by-step instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#How_to_export_data_from_the_Slicer_scene_to_DICOM_files">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#How_to_export_data_from_the_Slicer_scene_to_DICOM_files</a>.</p>

---

## Post #7 by @TMC (2017-11-14 09:22 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>using the segment editor is helpfull <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Best TMC</p>

---
