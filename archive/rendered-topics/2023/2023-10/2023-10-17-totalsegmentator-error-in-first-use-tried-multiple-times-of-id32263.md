---
topic_id: 32263
title: "Totalsegmentator Error In First Use Tried Multiple Times Of"
date: 2023-10-17
url: https://discourse.slicer.org/t/32263
---

# Totalsegmentator error in first use, tried multiple times of uninstall and reinstall

**Topic ID**: 32263
**Date**: 2023-10-17
**URL**: https://discourse.slicer.org/t/totalsegmentator-error-in-first-use-tried-multiple-times-of-uninstall-and-reinstall/32263

---

## Post #1 by @pssi_92 (2023-10-17 05:03 UTC)

<p>I just bought new desktop for my research, and installed Slicer 5.4.0 and Totalsegmentator extension. But an error showed up. I tried multiple times of deletion of the Slicer (Uninstall with <a href="http://Slicer.org" rel="noopener nofollow ugc">Slicer.org</a> folder deletion), and reinstallation.<br>
But nothing changed.</p>
<p>This is the step that I had.<br>
Step 1. Install GPU driver in GeForce experience.<br>
Step 2. Install CUDA with the CUDA link in the Totalsegmentator Github page.<br>
Step 3. Install Slicer 5.4.0<br>
Step 4. Install Totalsegmentator in the Extension manager.<br>
Step 5. Load sample data in Slicer and run the totalsegmentator.<br>
and an error showed up.</p>
<p>My computer information just in case:<br>
CPU: 13th Gen Intel(R) Core™ i7-13700F<br>
GPU: Nvidia GeForce RTX 4070 (Driver version: 537.58)<br>
RAM: 16Gb<br>
CUDA: 12.2</p>
<p>This is the Error message following:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\pssi9\AppData\Local\slicer.org\Slicer 5.4.0\bin\Python\slicer\util.py”, line 3146, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/pssi9/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 271, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/pssi9/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 868, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/pssi9/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 701, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/pssi9/AppData/Local/slicer.org/Slicer 5.4.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\pssi9\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/pssi9/AppData/Local/Temp/Slicer/__SlicerTemp__2023-10-16_23+50+39.954/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/pssi9/AppData/Local/Temp/Slicer/__SlicerTemp__2023-10-16_23+50+39.954/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>
<p>What should I do to fix the problem?</p>

---

## Post #2 by @rbumm (2023-10-17 05:24 UTC)

<p>Please try:</p>
<p>Delete the complete folder.<br>
Install 3D Slicer.<br>
Install Pytorch extension, run it and restart Slicer.<br>
Install TotalSegmenter extension, it should install itself on the first run. Otherwise, force install it again ( under “Advanced” do not check the latest developer version) and restart Slicer.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4bdaa4abfd79d849d35252754cf23309988f158.png" alt="image" data-base62-sha1="yV4RevxrPgyez6h7SPKIF1lFSdO" width="659" height="213"></p>
<p>Best</p>

---

## Post #3 by @rbumm (2023-10-17 06:04 UTC)

<p>Just tested a new installation and got a similar error.<br>
It seems as if the zenodo server, which holds the weights for download, is not active right now. Sorry for this error which will be passed to the developers. <a class="mention" href="/u/wasserth">@wasserth</a></p>

---

## Post #4 by @rbumm (2023-10-17 09:17 UTC)

<p>We have identified the error and will update the extension during the next few days.</p>

---

## Post #5 by @pssi_92 (2023-10-17 15:55 UTC)

<p>That is great.<br>
I did Force reinstall during multiple uninstall and reinstall, but same.<br>
Anyway, thank you for the reply!</p>

---
