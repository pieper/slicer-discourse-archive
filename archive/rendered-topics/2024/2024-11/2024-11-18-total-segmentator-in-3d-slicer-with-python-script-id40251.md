---
topic_id: 40251
title: "Total Segmentator In 3D Slicer With Python Script"
date: 2024-11-18
url: https://discourse.slicer.org/t/40251
---

# Total segmentator in 3d Slicer with python script

**Topic ID**: 40251
**Date**: 2024-11-18
**URL**: https://discourse.slicer.org/t/total-segmentator-in-3d-slicer-with-python-script/40251

---

## Post #1 by @Benutzer-0815 (2024-11-18 18:16 UTC)

<p>Hi there, I am trying to write a python script that uses Totalsegmentator in 3dSlicer, but so far I am not able to make good progress. The aim of using it in 3dslicer instead of standalone is to be able to exctract SUV values from pet data later using the same script. So far the import seems to work, but I wasn`t able to figure out how to call totalsegmentator. Also, since the DICOM includes ct and pet files, the script should figure out which of the files (=CT) to use as input (?)<br>
So far my script is as follows, can someone help me out how to continue from here?</p>
<p>import os<br>
import sys<br>
import TotalSegmentator<br>
from DICOMLib import DICOMUtils</p>
<p>dicomDataDir = “C:/Users/user1/sample/dicom”  # input folder with DICOM files</p>
<h1><a name="p-119586-check-if-the-folder-exists-1" class="anchor" href="#p-119586-check-if-the-folder-exists-1" aria-label="Heading link"></a>Check if the folder exists</h1>
<p>if not os.path.exists(dicomDataDir):<br>
sys.exit(“Aborting the script. Folder is required.”)</p>
<p>loadedNodeIDs = <span class="chcklst-box fa fa-square-o fa-fw"></span></p>
<p>with DICOMUtils.TemporaryDICOMDatabase() as db:<br>
DICOMUtils.importDicom(dicomDataDir, db)<br>
patientUIDs = db.patients()<br>
for patientUID in patientUIDs:<br>
loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))</p>
<p>slicer.util.selectModule(“TotalSegmentator”)</p>

---

## Post #2 by @Benutzer-0815 (2024-12-09 17:08 UTC)

<p><a class="mention" href="/u/sergio">@Sergio</a> maybe? From the search results I noticed you did something similar (?)</p>
<p>(Btw, the formatting in my post didnt work, especially with the hashtag before “check if folder exists”, but I hope its still understandable…</p>

---

## Post #3 by @evaherbst (2024-12-14 10:48 UTC)

<p>try the following</p>
<blockquote>
<pre><code>TotalSegmentator = slicer.util.getModuleLogic('TotalSegmentator') 
TotalSegmentator.process(inputVolumeNode, outputSegmentation, fast=False, cpu=False, task="tissue_types", subset=None, interactive=False)
</code></pre>
</blockquote>
<p>You just need to update the nodes and parameters</p>

---

## Post #4 by @Benutzer-0815 (2024-12-15 22:42 UTC)

<p>Thank you very much for your reply!<br>
The process is running well with that  code, however it seems to ignore the “fast=False” parameter and runs with  ‘–fast’ included? Do you know why that might be?<br>
Also, the segmentation does not appear in the scene, it only appears to be in the temp folder? Is it possible to save it properly in that function?</p>

---

## Post #5 by @Matteboo (2024-12-16 09:45 UTC)

<p>Hello, I have a few questions,<br>
What makes you say that the code is running in fast mode ? The computation can be “quick” (a few minutes) even without fast mode</p>
<p>What version of slicer/Total segmentator are you using ? The syntaxe changed  between version (I think between version 5.4 and 5.6 but I’m not sure)</p>

---

## Post #6 by @Benutzer-0815 (2024-12-16 16:00 UTC)

<p>Hi, thanks for your time!<br>
3D Slicer V 5.6.2 r32448 with totalsegmentator V 221f84d (2024-09-20)</p>
<p>TotalSegmentator log seems to imply it`s using fast mode:<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/XXXXXXX/AppData/Local/Temp/Slicer/__SlicerTemp__2024-12-16_16+39+15.344/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/XXXXXXX/AppData/Local/Temp/Slicer/__SlicerTemp__2024-12-16_16+39+15.344/segmentation’, ‘–fast’]</p>
<p>It might have something to do with my GPU that has only 5 GB of RAM. When running TS from the GUI, however, it asks if I want to enable fast mode and then runs without the --fast flag after I click “no” (and it`s slower)</p>

---

## Post #7 by @Matteboo (2024-12-16 16:49 UTC)

<p>It’s hard to help you without having access to your machine, but you confirm that:<br>
-You manage to make totalsegmentator run on your PC in “slow” mode from the GUI<br>
-You can make TotalSegmentator run in fast mode from your code<br>
-When putting “fast” to false, totalsegmentator still run in fast mode</p>
<p>My advice would be to install a debugger and to check what turn fast mode on, but I’m very surprised that all of the above propositions are true</p>

---

## Post #8 by @evaherbst (2025-01-08 18:16 UTC)

<p>Hm, I am not sure why this would happen.</p>
<p>You can set interactive=True to enable a popup to come up - this is a popup that warns you that slow mode might be slow. Check if it comes up and what it says.</p>

---

## Post #9 by @jamesobutler (2025-01-08 19:47 UTC)

<p>You don’t get warned about insufficient GPU memory when calling <code>process</code> programmatically with the input argument <code>interactive=False</code>. It</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/blob/2d764fb116967fb6c42193fd1fe3c6b920a4379d/TotalSegmentator/TotalSegmentator.py#L975-L977">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/2d764fb116967fb6c42193fd1fe3c6b920a4379d/TotalSegmentator/TotalSegmentator.py#L975-L977" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/2d764fb116967fb6c42193fd1fe3c6b920a4379d/TotalSegmentator/TotalSegmentator.py#L975-L977" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerTotalSegmentator/blob/2d764fb116967fb6c42193fd1fe3c6b920a4379d/TotalSegmentator/TotalSegmentator.py#L975-L977</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="975" style="counter-reset: li-counter 974 ;">
          <li>if not fast and cuda and cuda.get_device_properties(cuda.current_device()).total_memory &lt; 7e9 and interactive:</li>
          <li>    if slicer.util.confirmYesNoDisplay("You have less than 7 GB of GPU memory available. Enable 'fast' mode to ensure segmentation can be completed successfully?"):</li>
          <li>        fast = True</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @Benutzer-0815 (2025-01-09 08:20 UTC)

<p>Thanks a lot for your responses, much appreciated!<br>
I managed to fix it in the meantime, but didn`t have time to respond yet and work on it much further.<br>
It was actually a rather stupid mistake hidden in plain sight: I meant to do task=“total” and not “tissue_types” (no idea at what point I copied and pasted “tissue_types” in there, but that resulted in running a pre-task with fast segmentation  and generating output in temp folder, but not running the full segmentation afterwards, probably due to no license…)</p>
<p>Do you know if the python skript continues while running the totalsegmentator process? Do I need add a wait command if I want to add things after the segmentation?<br>
(Planning to use SegmentStatistics based on the segmentation afterwards, probably also have to import PETDICOMExtension first, in oder to receive SUV values. )</p>

---

## Post #11 by @Benutzer-0815 (2025-02-01 19:54 UTC)

<p>Quick follow-up question, now that Im making some progress with my skript:<br>
Is it possible to create a log file in a specific location using the python skript? I noticed Sliced creates it`s own full log in the temp folder; but when I try to have it create a custom log file it doesnt work well - My aim is to make the skript it more robust…</p>
<pre><code class="lang-auto">import logging
logFilePath = os.path.join(exportDir, 'script_log.txt')
logging.basicConfig(filename=logFilePath, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
</code></pre>

---
