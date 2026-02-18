# How do I know that measurement tools (markups) give me the correct value?

**Topic ID**: 28018
**Date**: 2023-02-23
**URL**: https://discourse.slicer.org/t/how-do-i-know-that-measurement-tools-markups-give-me-the-correct-value/28018

---

## Post #1 by @rossanas (2023-02-23 16:37 UTC)

<p>Hello,</p>
<p>I am a clinical scientist in the process to exploring 3DSlicer for micro-CT images analysis. I am doing quite some quantitive measurements using the Markup Module and I would like to get info as to know the accuracy with which measurements can be taken.</p>
<p>How do I know that every measurement (length, angle, etc.) si correct? Does the software calculate an appropriate scale bar automatically based on the DICOM files I import?</p>
<p>I apologize if I am not using an appropriate language, and I hope I have explained myself sufficiently in order to get your help on this topi.</p>
<p>Many thanks in advance!</p>
<p>Rossana</p>

---

## Post #2 by @muratmaga (2023-02-23 17:52 UTC)

<p>Correct scale is usually provided by the dataset. Each volume three properties (image spacing, orientation and origin) that defines the correct coordinate system. If your dataset provides those correctly, then your measurements will of right scale.</p>
<p>DICOMs usually (but not necessarily always) provide these fields correctly.</p>

---

## Post #3 by @rossanas (2023-02-24 08:19 UTC)

<p>Thanks a lot for you rreply.</p>
<p>Is there any manual or documentation explaining this that I can refer to?</p>
<p>Rossana</p>

---

## Post #4 by @muratmaga (2023-02-24 15:35 UTC)

<p>I am not sure if there is a specific place in documentation for this, but you may want to read the sections of <code>Volumes</code> module, which discusses image headers (spacing, orientation and origin) and the detailed discussion of coordinate system used in slicer.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#panels-and-their-use" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#panels-and-their-use</a></p>
<p><a href="https://www.slicer.org/w/index.php/Coordinate_systems" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/w/index.php/Coordinate_systems</a></p>

---
