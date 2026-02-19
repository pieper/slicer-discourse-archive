---
topic_id: 31172
title: "Segmentmesher Error Command Cleaver Cli Exe Returned Non Zer"
date: 2023-08-16
url: https://discourse.slicer.org/t/31172
---

# SegmentMesher, Error: Command 'cleaver-cli.exe' returned non-zero exit status 3221226505

**Topic ID**: 31172
**Date**: 2023-08-16
**URL**: https://discourse.slicer.org/t/segmentmesher-error-command-cleaver-cli-exe-returned-non-zero-exit-status-3221226505/31172

---

## Post #1 by @Mehdi_Khamesi (2023-08-16 05:34 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.2.2<br>
Expected behavior: Creating volumetric mesh<br>
Actual behavior: Error: Command ‘cleaver-cli.exe’ returned non-zero exit status 3221226505</p>
<p>Hello everyone,</p>
<p>I have a Segmentation.seg.nrrd file which include four segments. I want to create volumetric mesh of that. But when I choose that and run SegmentMesher, it gives me the following error:</p>
<p>Error: Command ‘cleaver-cli.exe’ returned non-zero exit status 3221226505</p>
<p>I have tried it several times, even by one segment but got the same response.<br>
Please let me know if you have any suggestions to solve this issue.</p>
<p>Best wishes<br>
Mehdi</p>

---

## Post #3 by @lassoan (2023-08-16 12:12 UTC)

<p>Try to adjust the parameters to generate a smaller, simpler, less accurate model to see if the mesh generation succeeds then.</p>

---

## Post #4 by @Mehdi_Khamesi (2023-08-16 14:18 UTC)

<p>Thanks for your attention.<br>
In fact, it does not generate mesh for a simple small tumor.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d0b43aa4a4b22a4f4f1ce81445bc4712fae3787.png" data-download-href="/uploads/short-url/k7JskN23n9ThNzTq3fh9oNaArxZ.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d0b43aa4a4b22a4f4f1ce81445bc4712fae3787_2_690x367.png" alt="Untitled" data-base62-sha1="k7JskN23n9ThNzTq3fh9oNaArxZ" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d0b43aa4a4b22a4f4f1ce81445bc4712fae3787_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d0b43aa4a4b22a4f4f1ce81445bc4712fae3787_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d0b43aa4a4b22a4f4f1ce81445bc4712fae3787_2_1380x734.png 2x" data-dominant-color="7A7981"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1918×1021 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Mehdi_Khamesi (2023-08-16 18:27 UTC)

<p>I installed this extension on another computer with same system and it works.<br>
So it seems that the model is not the problem.</p>
<p>Do you have any suggestion in this regard?</p>
<p>Many thanks</p>

---

## Post #6 by @lassoan (2023-08-17 11:23 UTC)

<p>It may be possible that language/regional settings in your operating system cause problems - indicated by the special characters in the working directory.</p>
<p>Could you try changing <a href="https://github.com/lassoan/SlicerSegmentMesher/blob/11c44ad4cb637a263facfdd980711dc370d6faa7/SegmentMesher/SegmentMesher.py#L638">this line</a> to the line below and test if it resolved the issue?</p>
<pre><code>    tempDirName = "test123“
</code></pre>

---

## Post #7 by @Mehdi_Khamesi (2023-08-18 13:31 UTC)

<p>Thank you for your response. I have installed the software in Windows 10 and to change this code I would try installing in Linux this weekend.</p>
<p>However, I wanted to analyze the output in COMSOL and I got it from the other computer. But I found that I can’t import .vtk or .msh into COMSOL. It seems that importing mesh file into COMSOL is much more complicated than other format specially for adding different physics. Also, I tried Gmsh and Salome to convert it to other importable formats. This wasn’t successful, too.</p>
<p>On the other hand, when I saved the model as STL format, it gives me a specific error in COMSOL (Geometry error (fin): Self-intersecting curve)<br>
Is there anyway to improve the quality of STL file that 3D Slicer gives us? Or any ideas to solve this issue?</p>
<p>Hope the best,<br>
Mehdi</p>

---

## Post #8 by @lassoan (2023-08-18 20:45 UTC)

<p>Some users reported that they successfully converted VTK volumetric meshes using <code>meshio</code> Python package. You can install it into 3D Slicer’s Python environment by opening the Python console, typing <code>pip_install('meshio')</code>, then follow examples of the meshio package documentation.</p>

---

## Post #9 by @Mehdi_Khamesi (2023-08-20 18:39 UTC)

<p>Yes, as always you are right. It was due to language settings.</p>
<p>How ever I changed it in control panel. In fact, I didn’t understand in which section of program I need to change this code. I need to change line number 638, but where? Could you tell the path.</p>
<p>Many thanks</p>

---
