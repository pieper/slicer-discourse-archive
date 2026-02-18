# VMTK issues in Slicer 4.6.2

**Topic ID**: 661
**Date**: 2017-07-10
**URL**: https://discourse.slicer.org/t/vmtk-issues-in-slicer-4-6-2/661

---

## Post #1 by @manish (2017-07-10 11:27 UTC)

<p>I am using Slicer 4.6.2 in Fedora. I have installed Vmtk Slicer Module using the 3D Slicer extension wizard. But its not working ? Could anybody guide me to get success.</p>
<p>Message output by 3D-Slicer are as follows:</p>
<p>File “/home/saurabh/manish/DICOM/Slicer-4.6.2-linux-amd64/SlicerVMTK/lib/Slicer-4.6/qt-scripted-modules/VesselnessFiltering.py”, line 94, in setup<br>
self.__seedFiducialsNodeSelector.markupsSelectorComboBox().noneEnabled = False<br>
AttributeError: qSlicerSimpleMarkupsWidget has no attribute named 'markupsSelectorComboBox’<br>
Traceback (most recent call last):<br>
File “/home/saurabh/manish/DICOM/Slicer-4.6.2-linux-amd64/SlicerVMTK/lib/Slicer-4.6/qt-scripted-modules/VesselnessFiltering.py”, line 236, in onMRMLSceneChanged<br>
self.restoreDefaults()<br>
File “/home/saurabh/manish/DICOM/Slicer-4.6.2-linux-amd64/SlicerVMTK/lib/Slicer-4.6/qt-scripted-modules/VesselnessFiltering.py”, line 286, in restoreDefaults<br>
self.__detectPushButton.checked = True<br>
AttributeError: VesselnessFilteringWidget instance has no attribute ‘_VesselnessFilteringWidget__detectPushButton’</p>
<p>Thanks</p>
<p>Manish</p>

---

## Post #2 by @ihnorton (2017-07-10 11:28 UTC)

<p>Please try the nightly.</p>

---

## Post #3 by @manish (2017-07-10 12:12 UTC)

<p>Hi Norton,</p>
<p>Many Thanks for the reply!</p>
<p>But, when I am trying to download nightly from : <a href="http://download.slicer.org/bitstream/661661" rel="nofollow noopener">http://download.slicer.org/bitstream/661661</a>, downloading fails every time.</p>
<p>Could you comment on this?</p>
<p>Thanks once again!<br>
Manish</p>

---

## Post #4 by @pieper (2017-07-10 12:40 UTC)

<p>Hi Manish -</p>
<p>I just tested and I can download from that link and Slicer runs fine on CentOS 7 machine.  The VMTK extension installs and runs fine as well.</p>
<p>What error do you get downloading?</p>
<p>-Steve</p>

---

## Post #5 by @manish (2017-07-11 05:26 UTC)

<p>Hi Pieper,</p>
<p>Thanks for the quick reply.</p>
<p>I also able to download and its working fine.</p>
<p><span class="mention">@Norton</span>: Nightly works.</p>
<ul>
<li>Manish</li>
</ul>

---
