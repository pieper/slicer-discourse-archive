---
topic_id: 15532
title: "Vff Import Errors"
date: 2021-01-14
url: https://discourse.slicer.org/t/15532
---

# VFF Import Errors

**Topic ID**: 15532
**Date**: 2021-01-14
**URL**: https://discourse.slicer.org/t/vff-import-errors/15532

---

## Post #1 by @SmHoop (2021-01-14 22:12 UTC)

<p>Hello,</p>
<p>I am attempting to import a .vff file I have created from a .mat cube (170x170x182), which is an optical CT reconstruction (through matlab iradon). I am using <a href="https://www.mathworks.com/matlabcentral/fileexchange/62039-mat_to_vff" rel="noopener nofollow ugc">matlab file</a> to convert my .mat file into .vff. I can open this new .vff file in MicroView (only if I choose the “rescale” option present in the mat_to_vff.m file (otherwise it is black and apparently only 3 slices). I can see in MicroView the image information is present (eg Title, patient position, modality, voxel size). When I attempt to import into 3DSlicer I see 3 related errors of:</p>
<p>“LoadVffFile: Incorrect parameters or required parameters that were not set, vff file failed to load. The required parameters are: rank, type, format, bits, bands, size, spacing, origin, rawsize, data scale, data offset, and title.”</p>
<p>"Warning: In D:\D\P\S-0-E-b\SlicerRT\VffFileReader\Logic\vtkSlicerVffFileReaderLogic.cxx, line 435<br>
vtkSlicerVffFileReaderLogic (0000026065493930): LoadVffFile: Empty filter value! The value must be separated from the parameter with an ‘=’ "</p>
<p>"LoadVffFile: The value entered for the format must be slice.</p>
<p>LoadVffFile: A string was not entered for Handle Scatter. The value must be separated from the parameter with an ‘=’. The value entered for Handle Scatter must be factor."</p>
<p>I’m assuming the first error can be solved by manually entering some meta data (not sure how) but the other two I am stumped.</p>
<p>This was tested with 4.10.2 and 4.11.0 (the errors are the same for both)</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2021-01-15 11:52 UTC)

<p>The VFF reader imposes several requirements to the VFF file, see here in the code: <a href="https://github.com/SlicerRt/SlicerRT/blob/master/VffFileReader/Logic/vtkSlicerVffFileReaderLogic.cxx#L233-L442" class="inline-onebox">SlicerRT/vtkSlicerVffFileReaderLogic.cxx at master · SlicerRt/SlicerRT · GitHub</a></p>
<p>The error message you get indicates exactly what is missing. You can either improve the conversion script to comply to these requirements, or suggest changes to the reader script.</p>
<p>You can find sample files that the VFF reader can read without problems here: <a href="https://github.com/SlicerRt/SlicerRtData/tree/master/gel-dosimetry-01/Opt%20CT%20Data" class="inline-onebox">SlicerRtData/gel-dosimetry-01/Opt CT Data at master · SlicerRt/SlicerRtData · GitHub</a></p>

---

## Post #3 by @SmHoop (2021-01-15 15:19 UTC)

<p>Thank you for the reply!</p>
<p>Am I correct in assuming there is a way to add in this missing data to the VFF itself (akin to metadata to a DICOM) so it complies with Slicer? I’m not sure I understand how to/am comfortable with editing the actual code slicer is running on. If I were to edit the script per your suggestion, would I have to compile and run slicer from the source code or is there a way to edit this from within the installed application? Thank you!</p>

---

## Post #4 by @cpinter (2021-01-15 15:42 UTC)

<p>What I’d do if I didn’t want to touch the reader code in SlicerRT is that I’d</p>
<ul>
<li>Manually edit a VFF file outputted by your matlab converter script so that the missing metadata indicated by the error messages are in the header so that the VFF is valid as far as SlicerRT is concerned, then</li>
<li>Edit the matlab converter script to add those metadata so you don’t need to add them manually for each volume</li>
</ul>

---

## Post #5 by @SmHoop (2021-01-15 15:43 UTC)

<p>I will try this first and if I can’t get this to work I will try the reader code. Thank you again!</p>

---

## Post #6 by @SmHoop (2021-01-15 16:50 UTC)

<aside class="quote no-group" data-username="SmHoop" data-post="1" data-topic="15532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f6c823/48.png" class="avatar"> SmHoop:</div>
<blockquote>
<p>The required parameters are: rank, type, format, bits, bands, size, spacing, origin, rawsize, data scale, data offset, and title.”</p>
</blockquote>
</aside>
<p>I was able to change the Matlab converter to supply the required information and the VFF now loads into Slicer with no errors, however it appears unusable. It loads into MicroView fine, though. I’ve included two pictures to compare them. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c19ac69211380c74e706b4a04e530d6ed44cf82e.png" data-download-href="/uploads/short-url/rCHKWpQyNrXEPHtiS9Hc9YHURno.png?dl=1" title="MicroView_VFF" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c19ac69211380c74e706b4a04e530d6ed44cf82e_2_690x343.png" alt="MicroView_VFF" data-base62-sha1="rCHKWpQyNrXEPHtiS9Hc9YHURno" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c19ac69211380c74e706b4a04e530d6ed44cf82e_2_690x343.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c19ac69211380c74e706b4a04e530d6ed44cf82e_2_1035x514.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c19ac69211380c74e706b4a04e530d6ed44cf82e_2_1380x686.png 2x" data-dominant-color="667179"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MicroView_VFF</span><span class="informations">1915×952 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @cpinter (2021-01-15 17:38 UTC)

<p>You need to adjust brightness/contrast (i.e. window/level) in the Volumes module.</p>
<p>The range of the VFF images are very variable, and sometimes Slicer cannot automatically determine a good setting.</p>

---

## Post #8 by @SmHoop (2021-01-15 18:54 UTC)

<p>I should have mentioned, my first thought was also W/L but it only reveals that the image itself seems to be a randomly pixelated mess. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f75b1411598915ffa877efa97088952a4aae0a50.png" data-download-href="/uploads/short-url/zid4k7BQ8jbEvEcl9kXfipICPNS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f75b1411598915ffa877efa97088952a4aae0a50_2_690x360.png" alt="image" data-base62-sha1="zid4k7BQ8jbEvEcl9kXfipICPNS" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f75b1411598915ffa877efa97088952a4aae0a50_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f75b1411598915ffa877efa97088952a4aae0a50_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f75b1411598915ffa877efa97088952a4aae0a50.png 2x" data-dominant-color="A0A0A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1316×687 74.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> .</p>

---

## Post #9 by @cpinter (2021-01-18 10:24 UTC)

<p>It may be a data range issue. We tested the VFF reader with only one manufacturer, as it was the only one available and the one used by the project for which it was developed. Further work may be needed to support your VFF format.</p>
<p>Your data is originally not VFF, but Matlab. Why have you chosen to convert to a non-standard file format such as VFF? If you convert it to nrrd for example Slicer would be able to load it without problems as it is much more widely supported.</p>

---

## Post #10 by @SmHoop (2021-01-18 15:51 UTC)

<p>I tried to use VFF because I found an easy .m file to use (that works) and was also the format in the tutorial for the gel dosimetry module by Kevin Alexander, but I’ve also been directed towards an nrrd converter by Andras Lasso but I haven’t had success in utilizing it <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m" class="inline-onebox" rel="noopener nofollow ugc">SlicerMatlabBridge/nrrdwrite.m at master · PerkLab/SlicerMatlabBridge · GitHub</a></p>

---

## Post #11 by @lassoan (2021-01-18 16:38 UTC)

<p>NRRD is a simple, capable, and very widely used file format. You can find readers and writers for it in all programming environments. Do not use VFF unless you have absolutely no other option.</p>
<p>nrrdwrite.m in the SlicerMatlabBridge repository should work well. See detailed description and usage examples in its documentation. If you have any questions about it then let us know. If you want, you can use any other nrrd writer implementation in Matlab (there are several), but I would recommend the one in the SlicerMatlabBridge repository because it supports 4D data and allows easy access to image geometry (IJK to LPS transform).</p>
<p>As a side note, it could make sense to make the move from Matlab to Python (unless only a few years left of your professional career, then you may survive with sticking to Matlab), because any time that you spend on dealing with a declining, proprietary technology is time that you don’t spend on learning much more useful and relevant skills.</p>

---

## Post #12 by @SmHoop (2021-01-18 16:48 UTC)

<p>I see. I gravitated towards VFF as it was the example data given in the tutorial and is the first option listed when a user hovers over “Load non-DICOM data” in the slicelet (assumed it was the preferred format). I found a different nrrd writer <a href="https://www.mathworks.com/matlabcentral/fileexchange/48621-nrrdwriter-filename-matrix-pixelspacing-origin-encoding" rel="noopener nofollow ugc">here</a> which has worked. The linked nrrdwrite.m gives me dot indexing errors when I try to set the .mat cube I have as the img in order to run the file.</p>
<p>I’m using Matlab as it is part of the research I’m working on and I’m in my second year of my MS so I do not have time to switch the entire process over, as you mention.</p>
<p>I may keep trying to make the initial nrrdwrite.m work but so far this seems to be working…thank you for all the help and guidance!</p>

---

## Post #13 by @jdjutras (2024-02-08 21:10 UTC)

<p>Hello, I was trying to open a .vff image from the new Vista16 optical CT (from ModusQA with software version 2.2.12) in 3D Slicer v5.6.1 (stable release). It fails to load, without providing any info as to why. Has anyone encountered this recently?</p>

---

## Post #14 by @cpinter (2024-02-12 10:29 UTC)

<p>A basic question but could help a lot: If you open the error log, is there error or warning? Please copy-paste it here if so. Thanks!</p>

---
