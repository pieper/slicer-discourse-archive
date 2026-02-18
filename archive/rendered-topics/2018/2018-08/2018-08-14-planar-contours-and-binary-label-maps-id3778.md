# Planar contours and binary label maps

**Topic ID**: 3778
**Date**: 2018-08-14
**URL**: https://discourse.slicer.org/t/planar-contours-and-binary-label-maps/3778

---

## Post #1 by @serduj (2018-08-14 19:08 UTC)

<p>Hi all.<br>
When i downloaded patient anatomy contours used in RT, Slicer represents it to me in form of planar contour (in the segmentation). When i’m trying to make contours in segment editor, slicer creates my countours in form of binary lable map. So my question is how can i make segmentation in form of planar contour in Slicer, or how to convert binary lablemaps into planar contours. (I’ve attached sreenshots to this question)<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e5e52c56f5d9d2e75dfb70d0330efd24908cfe3.jpeg" alt="2" data-base62-sha1="236LPb3xN0x7piVeFzrHghaY0fx" width="481" height="332"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3d6f69fb3fbf92d6b254f92dc2950a3e7a4f0a8.jpeg" alt="1" data-base62-sha1="pEW1uHuQBrOTOu77bkYTflJj3YY" width="484" height="313"></p>
<p>The second problem is that I can not upload images to the dosimetric film analysis module to calibrate. Looks like slicer tries to upload image, but the work screen remains empty anyway. I am trying PNG, TIF and JPEG formats, and several image sizes.</p>
<p>Good luck and thank you for help.</p>

---

## Post #2 by @gcsharp (2018-08-14 22:37 UTC)

<p>Hi Serduj,</p>
<p>When you do a DICOM export, Slicer will automatically create the planar contours required for RT structure set. But I agree, it looks like manually converting to planar contours is not currently available. Do you need the planar contour representation within Slicer for some other reason?</p>
<p>I defer to Csaba on the film analysis question.</p>
<p>Greg</p>

---

## Post #3 by @serduj (2018-08-15 06:16 UTC)

<p>Thank you for answer.</p>
<p>The purpose is to create contour of object on CT scans. Object usually have simple geometry like squares or circles (in one slice ofc.). Than created contours i want to import into planing system in DICOM format.</p>
<p>As you said earlier slicer convert my DICOM file, containing contours, into planar contours. And i want to do inverse procedure.</p>
<p>i.e. make contour in slicer 3D =&gt; convert to dicom =&gt; import dicom file into my planning system</p>
<p>and again thank you for help</p>

---

## Post #4 by @cpinter (2018-08-15 12:11 UTC)

<p>HI Serduj,</p>
<p>This is exactly what <a class="mention" href="/u/gcsharp">@gcsharp</a> described. You can create a segmentation in Segment Editor, arrange a study in the Data module (Subject / Study / CT + Segmentation), right-click the study, choose Export to DICOM, and select RT as type. You’ll need to have the SlicerRT extension installed to find the RT export type.</p>

---

## Post #5 by @serduj (2018-08-15 12:42 UTC)

<p>Thank you so much. My problem with contours solved. Instead of ‘export’ i am reading ‘import’ in Greg’s answer =)</p>
<p>And i still cant import images into the film analysis module, can you help me with that problem?</p>
<p>Good luck, i am very appreciate you’r help to me, thank you!</p>

---

## Post #6 by @cpinter (2018-08-15 13:01 UTC)

<p>The film slicelet covers only one specific workflow, and is really a prototype at this point. Can you please describe in detail what kind of data you have, ant in what format exactly?</p>

---

## Post #7 by @serduj (2018-08-17 18:47 UTC)

<p>I have a set of calibration images of irradiated EBT3 films. Images in TIF format obtained from CCD scanner. Resolution 200 by 80 pixels.</p>

---
