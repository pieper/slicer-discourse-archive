---
topic_id: 9504
title: "Encode Volume Rendering Preset In Single Mrml File"
date: 2019-12-15
url: https://discourse.slicer.org/t/9504
---

# Encode volume rendering preset in single mrml file

**Topic ID**: 9504
**Date**: 2019-12-15
**URL**: https://discourse.slicer.org/t/encode-volume-rendering-preset-in-single-mrml-file/9504

---

## Post #1 by @mrm63 (2019-12-15 14:12 UTC)

<p>Hi folks–quick question:</p>
<p>We are trying to make a very portable version of some volume files with Slicer, such that we could simply send a master .mrml file (along with the .mhd and .raw) files to a user, who could simply open Slicer to the preferred view of the volume by clicking &amp; opening the mrml file.</p>
<p>Is it possible to encode a set of desired volume properties into the mrml file, such that this option would be included in the presets under the Volume Rendering module? (right next to the “CT-AAA”, “MR-MIP”, options etc.).</p>
<p>Alternatively, could the mrml file be specified simply to open to these custom volume properties/volume view? (no need to click through volume rendering &amp; select a preset)</p>
<p>Many thanks.</p>

---

## Post #2 by @lassoan (2019-12-15 14:44 UTC)

<p>I think you can do these by creating “Scene views”. It remembers not just volume rendering options, but all other view settings, you get a thumbnail and can specify a name and description. User can switch between scene views in “Scene views” module. It is important that nodes should not be added or removed from the scene after scene views are created.</p>

---

## Post #3 by @pieper (2019-12-15 15:00 UTC)

<p>You also have the option of saving a ‘medical reality bundle’ (.mrb extension) which puts the mrml scene file together with the data into a single file that will open up with the pre-defined views.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SavingData#Save_Options" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SavingData#Save_Options</a></p>

---
