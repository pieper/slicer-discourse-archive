---
topic_id: 20640
title: "New Feature Configurable Volume Display Presets In Right Cli"
date: 2021-11-16
url: https://discourse.slicer.org/t/20640
---

# New feature: configurable volume display presets in right-click menu and Volumes module

**Topic ID**: 20640
**Date**: 2021-11-16
**URL**: https://discourse.slicer.org/t/new-feature-configurable-volume-display-presets-in-right-click-menu-and-volumes-module/20640

---

## Post #1 by @rbumm (2021-11-16 09:22 UTC)

<p>Volume display preset selections have been added to the slice view right-click menu (view context menu). It offers setting volume display (window width and level and colormap) from:</p>
<ul>
<li>Window/level presets stored in the volume’s display node (typically read from DICOM)</li>
<li>Automatic window/level (maps the full intensity range of the voxels to black-&gt;white)</li>
<li>Window/level and color presets stored in VolumeDisplayPresets.json file</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f702679eef5f83899065ad9823bad44ae5400a8d.png" alt="image" data-base62-sha1="zf95pWz28iwNE0sFhyPwRd55uq1" width="580" height="422"></p>
<p>The presets are defined in a json file (VolumeDisplayPresets.json) and presets can be added, removed, modified by editing the file.</p>
<p>View context menu can modify both foreground or background volume’s window/level, using the same logic as in the window/level adjustment mouse mode (if both reground and background volume are displayed in a slice view then then foreground volume will be adjusted if foreground opacity &gt;0 and mouse is clicked in a region inside the foreground volume).</p>
<p>The Volumes module’s preset selector, too, uses the window/level and color presets specified in VolumeDisplayPresets.json file.</p>
<p>Current limitation (will be probably improved in future versions of requested) is that VolumeDisplayPresets.json file is only read at startup. Presets cannot be dynamically changed at runtime.</p>
<p>Slicer preview version required.</p>
<p>Author: Rudolf Bumm (<a class="mention" href="/u/rbumm">@rbumm</a>)<br>
Co-authored-by: Andras Lasso (<a class="mention" href="/u/lassoan">@lassoan</a>)</p>

---
