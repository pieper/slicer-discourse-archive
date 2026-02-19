---
topic_id: 4417
title: "Diffusion Export To Ply Extension Not Available"
date: 2018-10-16
url: https://discourse.slicer.org/t/4417
---

# Diffusion export to PLY extension not available

**Topic ID**: 4417
**Date**: 2018-10-16
**URL**: https://discourse.slicer.org/t/diffusion-export-to-ply-extension-not-available/4417

---

## Post #1 by @Matthias_Cabri (2018-10-16 14:30 UTC)

<p>I have a DTI tractography from a brain that I would like to export as a 3D model with the color map included. I tried exporting as STL file, but that gives me a 3d file with dots (instead of tubes) and no colormap.</p>
<p>I installed the nightly build 4.9.0-2018-10-15<br>
I put the fiber bundle coloring to fractional anisotrophy<br>
I installed the SlicerDMRI extension</p>
<p>I do not seem to have the Export tractography to PLY (mesh) module</p>
<p>Why am I missing that module?</p>

---

## Post #2 by @ihnorton (2018-10-16 14:58 UTC)

<p>Hi <a class="mention" href="/u/matthias_cabri">@Matthias_Cabri</a>,</p>
<p>What operating system? Also, just to double-check, did you restart Slicer after installing the extension?</p>
<p>If so, could you please upload or send me an error log (inorton at bwh dot harvard dot edu) following these instructions: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report</a> (<em>please make sure there is no patient information, including in filenames and messages</em>)</p>

---

## Post #3 by @Matthias_Cabri (2018-10-16 15:07 UTC)

<p>Hi <a class="mention" href="/u/ihnorton">@ihnorton</a></p>
<p>OS: windows 7<br>
I did restart slicer after installing the DMRI extension<br>
Error log contains no privacy informatio and is sent to you</p>

---

## Post #4 by @ihnorton (2018-10-16 15:48 UTC)

<p>Thanks for the log file. It looks you are hitting this issue:</p>
<p><a href="https://discourse.slicer.org/t/2018-10-15-windows-nightly-build-unable-to-import-vtk/4403/4">https://discourse.slicer.org/t/2018-10-15-windows-nightly-build-unable-to-import-vtk/4403/4</a></p>
<p>I would suggest to either wait for that thread to be resolved and download the corrected package, or if you are in a hurry you can download the following build from a few days ago:</p>
<p><a href="http://slicer.kitware.com/midas3/download/?bitstream=882771&amp;offset=0&amp;name=Slicer-4.9.0-2018-10-07-win-amd64.exe" class="onebox" target="_blank">http://slicer.kitware.com/midas3/download/?bitstream=882771&amp;offset=0&amp;name=Slicer-4.9.0-2018-10-07-win-amd64.exe</a></p>

---

## Post #5 by @Matthias_Cabri (2018-10-17 08:33 UTC)

<p>This has indeed solved my problem. Thank you for your help</p>

---
