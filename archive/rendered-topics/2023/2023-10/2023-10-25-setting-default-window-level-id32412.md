# Setting default window/level?

**Topic ID**: 32412
**Date**: 2023-10-25
**URL**: https://discourse.slicer.org/t/setting-default-window-level/32412

---

## Post #1 by @cuatrocinco (2023-10-25 16:21 UTC)

<p>I am working on manually segmenting kidneys for a large number of abdominal CT scans.</p>
<p>For some reason, when I load the DICOMs the default window/level is essentially the same as the CT-Air preset, which is no good for evaluating kidneys.</p>
<p>I am able to right click the scan and change the preset to CT-Abdomen, but it takes several seconds, and over the course of several hundred scans that time adds up.</p>
<p>Is there a way to modify the default window/level settings in 3D Slicer so that I have the option of making all newly imported scans display with a specific window/level?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2023-10-25 16:25 UTC)

<p>By default, we apply the window/level that is stored in the DICOM file.</p>
<p>I would recommend to specify your own custom hanging protocol and add a keyboard shortcut to activate. See a complete example here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#activate-hanging-protocol-by-keyboard-shortcut" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#activate-hanging-protocol-by-keyboard-shortcut</a></p>
<p>All you need is to copy-paste this into Slicer’s Python console. Probably you can delete the part between <code># Set up view layout and content</code> and <code># Register keyboard shortcut</code> and remove all the PET related parts.</p>

---
