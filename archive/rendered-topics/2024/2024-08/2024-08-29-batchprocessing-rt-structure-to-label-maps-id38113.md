---
topic_id: 38113
title: "Batchprocessing Rt Structure To Label Maps"
date: 2024-08-29
url: https://discourse.slicer.org/t/38113
---

# BatchProcessing RT structure to label maps

**Topic ID**: 38113
**Date**: 2024-08-29
**URL**: https://discourse.slicer.org/t/batchprocessing-rt-structure-to-label-maps/38113

---

## Post #1 by @xuec (2024-08-29 12:36 UTC)

<p>Hi I am trying to convert many dicom RT structure to labelmaps,<br>
and I found that I can use the BatchStructureSetConversion.py<br>
(<a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py" class="inline-onebox" rel="noopener nofollow ugc">SlicerRT/BatchProcessing/BatchStructureSetConversion.py at master · SlicerRt/SlicerRT · GitHub</a>)</p>
<p>However, I got an error while doing it,<br>
TODO: implement cloud fingerprint store<br>
Traceback (most recent call last):<br>
File “”, line 7, in <br>
File “./project/<br>
BatchStructureSetConversion.py”, line 99<br>
logging.info(f’  Converting structure set {segmentationNode.GetName()} to labelmap’)<br>
^<br>
SyntaxError: invalid syntax</p>
<p>I am a bit lost about what I can change and what to do? Would appreciate any help. Thank you.</p>

---

## Post #2 by @cpinter (2024-08-29 12:56 UTC)

<p>The line in question seems fine to me, the error is quite strange. What Slicer version do you use?</p>

---

## Post #3 by @xuec (2024-08-29 15:09 UTC)

<p>I am currently using Slicer 4.10.2, do I need to upgrade my slicer to use the function? Thanks! I running the command in Linux  with something like this: Slicer —no-main-window —python-script BatchStructure.py -i image/folder -o image/folder</p>

---

## Post #4 by @cpinter (2024-08-29 15:11 UTC)

<p>Please try it on the latest Slicer, we can only help with recent versions. 4.10 is kind of ancient by now.</p>

---

## Post #5 by @xuec (2024-09-03 03:12 UTC)

<p>I already tried it with the newest version 5.6.2, however there are still these errors:</p>
<p>qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added</p>
<p>appreciate any pointers. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> thank you</p>

---

## Post #6 by @xuec (2024-09-03 04:01 UTC)

<p>Please disregard my previous post, I forgot to download the RT plugins.</p>
<p>I do have one question regarding how the files were supposed to be placed, if there is more than 1 RT structure in the folder, will it be okay to run?</p>
<p>My folder consists of several folders:</p>
<ul>
<li>1st RT structure folder</li>
<li>2nd RT structure folder</li>
<li>CT dicom folder</li>
<li>RTdose folder</li>
<li>RTplan folder</li>
</ul>
<p>Do I need to separate them? because I still have these errors:<br>
When loading module  “DicomRtImportExport” , the dependency “Volumes” failed to be loaded.<br>
When loading module  “BatchStructureSetConversion” , the dependency “DicomRtImportExport” failed to be loaded.<br>
When loading module  “Beams” , the dependency “Models” failed to be loaded.<br>
When loading module  “DicomRtImportExport” , the dependency “Volumes” failed to be loaded.<br>
error: [/home/Slicer-5.6.2-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
<p>Thank you very much!</p>

---

## Post #7 by @cpinter (2024-09-03 09:49 UTC)

<p>There must be some problem with your installation. The dependencies that cannot be found, Volumes and Models are basic Slicer modules. Can you find them in the module list?</p>

---

## Post #8 by @xuec (2024-09-04 02:46 UTC)

<p>By module list, do you mean if I can use the module? I can find both modules when I use the UI version of 3D Slicer.</p>

---

## Post #10 by @cpinter (2024-09-04 08:54 UTC)

<p>Yes this is what I mean.</p>
<p>The error message <code>When loading module “DicomRtImportExport” , the dependency “Volumes” failed to be loaded.</code> means that some basic SlicerRT modules are not available because it cannot find some parts of the Volumes module. This usually means binary files (.dll on Windows, .so on linux), and if that happens the module does not work at all. So if you can switch to the Volumes module and use it too, then I’m out of ideas. Maybe the extension binaries are somehow not compatible with the Slicer ones.</p>
<p>One last thing that occurs to me is to ask you to try the very latest Slicer preview. Since we usually only fix issues in the latest version, it would help me see if the issue is still present, and if it is, I’ll try it on my Linux machine. I use Ubuntu 22.04. What is your distribution?</p>

---

## Post #11 by @xuec (2024-09-04 09:07 UTC)

<p>I actually also tried the latest Slicer preview (5.7.0), but the same issue is still there. I am using Ubuntu 20.04.6 LTS.</p>
<p>The module is working perfectly in the UI platform. I have no idea why that doesn’t work in the terminal</p>
<p>Other than using a command line, do you have tips or examples if I could script it in python? I actually only need the segmentation with certain names from the segment files.</p>
<p>Thank you so much for your input so far.</p>

---

## Post #12 by @cpinter (2024-09-04 09:10 UTC)

<p>You could cannibalize the BatchProcessing python file and run it from the Python console if it’s urgent! For now what I can do is to try it myself on Linux (I’m usually on Windows so it will take a bit of time).</p>

---

## Post #13 by @xuec (2024-09-05 06:10 UTC)

<p>Let me try to see if I can butcher it correctly, or find myself a windows computer to run the code. Tho if you have any update about running it in Linux, please kindly update us. Thank you very much!</p>

---

## Post #14 by @cpinter (2024-09-05 08:16 UTC)

<p>Note that I am also unsure if it runs on Windows. I’ll given an update if I have one.</p>

---
