---
topic_id: 31994
title: "4D Ultrasound 3Dus To 4D Nrrd"
date: 2023-10-02
url: https://discourse.slicer.org/t/31994
---

# 4D Ultrasound (.3dus) to 4D NRRD

**Topic ID**: 31994
**Date**: 2023-10-02
**URL**: https://discourse.slicer.org/t/4d-ultrasound-3dus-to-4d-nrrd/31994

---

## Post #1 by @eyalyah (2023-10-02 13:49 UTC)

<p>I have an 4D ultrasound from a vivid E95 machine, I successfully loaded it the 4D volume to slicer by changing  the extension of the file to .3dus</p>
<p>when I load it to slicer i have 2 data entries, one is the 3d data and the other is a time sequence table.</p>
<p>Is there anyway to combine the two flies to created a one 4D NRRD file?</p>

---

## Post #2 by @lassoan (2023-10-02 14:05 UTC)

<p>Yes, you can very easily store custom data in additional fields in a nrrd file: all attributes of the sequence node are stored in the volume sequence file (<code>something.seq.nrrd</code>). You can access attributes in the node attributes table in <code>Data</code> module / <code>All nodes</code> tab / <code>MRML Node information</code> section and programmatically using <code>SetAttribute</code> and <code>GetAttribute</code> methods of the sequence node.</p>
<p>You can avoid renaming the file by selecting <code>3D ultrasound image</code> in the Description column in the <code>Add data</code> window.</p>

---

## Post #3 by @lassoan (2023-10-02 14:46 UTC)

<p>We chose to store the ECG signal as a separate table, as it makes it easy to directly plot the signal by a few clicks, but for archiving it could be simpler to store the ECG along with the ultrasound image in a single file. We haven’t explored this in detail yet because ultrasound imaging manufacturers rarely give access to the ECG signal (most notably, Philips ultrasound systems do not let extract ECG signal from their images), so we don’t rely on using it yet.</p>
<p>If you decide to store the ECG signal in the sequence then you can make a small change in the importer to not write the ECG signal not just into the table node but also into a node attribute (similarly to <code>SlicerHeart.ProbeName</code> and <code>SlicerHeart.ProbeType</code>). You may consider sending a pull request with this change to <a href="https://github.com/SlicerHeart/SlicerHeart">SlicerHeart</a> extension so that we can review and give feedback and make it standard behavior for everyone.</p>

---
