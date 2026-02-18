# Read pixel data of DICOM RT files

**Topic ID**: 6916
**Date**: 2019-05-24
**URL**: https://discourse.slicer.org/t/read-pixel-data-of-dicom-rt-files/6916

---

## Post #1 by @calvin.kohwy (2019-05-24 13:01 UTC)

<p>Slicer version:4.10.2</p>
<p>Dear all</p>
<p>Is it possible that we are able to extract the pixel and map it to dose from the dicom files?</p>
<p>For example,</p>
<p>I have a set of dicom files exported from Treatment planning system (Plan, Structure, dose, CT images). Using these dicom files, I have used Geant4 to do a dose calculation which output me another “dose” dicom file.</p>
<p>Does SlicerRT allow us to upload the dose and CT dicom files and mapped it together? Furthermore, can we then extract the exact dose values such that it can be used for further data processing in Matlab or python like plotting of Spread out Bragg Peak etc…</p>
<p>Thank you!</p>
<p>Calvin</p>

---

## Post #2 by @lassoan (2019-05-24 23:04 UTC)

<p>Yes, these are all straightforward to do in Slicer using SlicerRT. Let us know if you get stuck.</p>

---

## Post #3 by @calvin.kohwy (2019-05-25 05:33 UTC)

<p>Hi Lassoan</p>
<p>This is my first time using slicer… Do you know where I can refer to to start using SlicerRT? Is there any guide or tutorial for slicerRT available?</p>
<p>Thanks alot!</p>

---

## Post #4 by @lassoan (2019-05-25 11:56 UTC)

<p>Tutorials are available here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Tutorials" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Tutorials</a></p>
<p>Feel free to post new topics if you have any specific questions.</p>

---

## Post #5 by @calvin.kohwy (2019-05-27 08:13 UTC)

<p>Hi Lassoan</p>
<p>I still couldn’t really find the section where is shows how to extract the exact dose values such that it can be use for further data processing. Could you give me some pointers where I should start looking or which options should i be clicking on?</p>
<p>Thank you.</p>

---

## Post #6 by @cpinter (2019-05-27 13:45 UTC)

<p>Hi Calvin,</p>
<p>Several people have inquired in the past weeks about integrating SlicerRT and Geant4/TOPAS. I’d be more than happy to help, but I don’t have access to any Geant4 dose calculation workflow. If you could show us what the output looks like, then it would be a great first step towards this goal.</p>
<p>The current idea is that we’d add a Geant4 plugin into <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ExternalBeamPlanning" rel="nofollow noopener">External Beam Planning</a>, and you could do the planning transparently in Slicer (load data, define beams within Slicer, click a button to do the calculation, then automatically see the result in Slicer). Then you could do your Matlab-based processing from Slicer too via <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge" rel="nofollow noopener">MatlabBridge</a>. Also plotting is quite easy in Slicer.<br>
Please let me know if you’d be interested in something like this rather than just importing the result dose volume into Slicer. In any case, if you could share a Geant4 dose file with us, it would be a great first step!</p>
<p>Thank you!</p>

---
