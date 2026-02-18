# Transfering calibration data to 3DSlicer

**Topic ID**: 1083
**Date**: 2017-09-19
**URL**: https://discourse.slicer.org/t/transfering-calibration-data-to-3dslicer/1083

---

## Post #1 by @Fatemeh_Salehi (2017-09-19 06:30 UTC)

<p>Hello,</p>
<p>We already done free hand calibration in fCal Application and then save log file in .xml format.<br>
Now, we want to transfer our saved data and log file to 3DSlicer. we would be grateful if you could give us instructions to do so.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2017-09-19 13:14 UTC)

<p>Install Sequences and SlicerIGT extensions and drag-and-drop recorded .mha files to the Slicer application window to load them. In the add data dialog, choose “Sequence Metafile”. See tutorials at <a href="http://www.slicerigt.org">www.slicerigt.org</a> for details.</p>

---

## Post #3 by @Fatemeh_Salehi (2017-09-20 10:24 UTC)

<p>thanks.<br>
but this for .mha files. and we want to load “calibration data” that save in .xml format.<br>
this calibration done by fCal application.</p>

---

## Post #4 by @lassoan (2017-09-20 11:36 UTC)

<p>We usually send all the transforms to Slicer in real-time using PlusServer through OpenIGTLink. You can also save all the transforms that you receive using Sequences extension.</p>
<p>If we want to have not just the raw transforms in the sequence file, then we use EditSeqFile to add those (for example, ImageToReference).</p>
<p>To get a transform from the device set config file:</p>
<ul>
<li>open the xml file in any text editor/viewer</li>
<li>copy the 16 numbers of the matrix to the clipboard</li>
<li>in Slicer go to Transforms module</li>
<li>create or select a transform</li>
<li>click paste button.</li>
</ul>

---

## Post #5 by @Fatemeh_Salehi (2017-11-13 14:13 UTC)

<p>thanks.<br>
We done that, but the name of transforms in fCal and 3DSlicer are not same. and if we change the names in xml file in plusServer or create new matrix of transforms, is not resulted! and when we move instruments, models of instruments in 3Dslicer not move.<br>
we would be grateful again if you could give us instructions to do so.</p>

---

## Post #6 by @lassoan (2017-11-13 14:29 UTC)

<p>Name of transforms sent through OpenIGTLink is trimmed to 20 characters. If that causing issues then you can use shorter coordinate system names so that transform names remain below 20.</p>

---
