# Display common physical point on diffrent modalities

**Topic ID**: 24305
**Date**: 2022-07-14
**URL**: https://discourse.slicer.org/t/display-common-physical-point-on-diffrent-modalities/24305

---

## Post #1 by @Jakub_Mitura (2022-07-14 08:12 UTC)

<p>I know that slicer keeps track on physical position of each voxel - as a starting point for registration I would like to display using python or interactively in the same time voxels that correspond to the same physical position in diffrent images.</p>
<p>I suppose it could be done in compare volumes wizard, but to be honest I do not know How</p>
<p>From algorithm perspective</p>
<ol>
<li>
<p>read physical position of the cursor on image A  nad get its coordinates (x,y,z)</p>
</li>
<li>
<p>look in image B and C for voxel closest to (x,y,z) and display its position by some cross or  by temporarly changing the color of this voxel or gorup of voxels etc.   - for visualization</p>
</li>
</ol>

---

## Post #2 by @pieper (2022-07-14 18:39 UTC)

<p>You could just use the crosshair feature to look at the same spot in multiple volumes.  Enable it in the crosshair toolbar and then display the different volumes in different slice views (drag and drop volumes from the Data module to the views).  Use Transforms to show the volumes with or without the registration applied.</p>

---
