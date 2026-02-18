# Set Specific Lookup Table depending on volume

**Topic ID**: 20486
**Date**: 2021-11-04
**URL**: https://discourse.slicer.org/t/set-specific-lookup-table-depending-on-volume/20486

---

## Post #1 by @park (2021-11-04 08:40 UTC)

<p>Hi all</p>
<p>Whenere I read some volumes in the 3D Slicer,<br>
It is always pop up as Grey Lookup Table</p>
<p>However, I would like to read some particular type (e.g., have specific file name or header) of volumes as different Lookup Table (i.e. ColdToHotRainbow) automatically.<br>
(E.g. “CT.nii” → Gray, “Vector.nii”-&gt; ColdToHotRainbow)</p>
<p>Could I get any insight to figure it out?</p>
<p>Thank you for your reply<br>
TY Park</p>

---

## Post #2 by @pieper (2021-11-04 15:07 UTC)

<p>I believe you would need to add a small script to your slicerrc.py, similar to this volume rendering example.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html?highlight=automatically#show-volume-rendering-automatically-when-a-volume-is-loaded" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html?highlight=automatically#show-volume-rendering-automatically-when-a-volume-is-loaded</a></p>

---

## Post #3 by @lassoan (2021-11-04 17:34 UTC)

<p>If you want to play nicer with other modules (which is important if you plan to distribute your module publicly) or go beyond just customizing the color table - for example customize how the volume is displayed, customize its icon in Data module, specify custom right-click menu actions - then you can add Subject Hierarchy plugin. When a node is loaded then Slicer iterates through all registered plugins and each plugin provides a “confidence value” that it is should own that node. The plugin with the highest confidence value will get the ownership and will be used to provide icon, menu actions, method to show/hide the node, etc.</p>

---

## Post #4 by @park (2021-11-05 05:05 UTC)

<p>Thank you for your reply</p>
<p>However, I could not find where is the “slicerrc.py” and where I put this file</p>

---

## Post #5 by @lassoan (2021-11-05 16:24 UTC)

<p>See detailed description of the .slicerrc.py startup file here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file" class="inline-onebox">Application settings — 3D Slicer documentation</a></p>

---
