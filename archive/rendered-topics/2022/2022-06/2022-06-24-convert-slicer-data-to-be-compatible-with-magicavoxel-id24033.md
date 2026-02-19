---
topic_id: 24033
title: "Convert Slicer Data To Be Compatible With Magicavoxel"
date: 2022-06-24
url: https://discourse.slicer.org/t/24033
---

# Convert Slicer data to be compatible with MagicaVoxel

**Topic ID**: 24033
**Date**: 2022-06-24
**URL**: https://discourse.slicer.org/t/convert-slicer-data-to-be-compatible-with-magicavoxel/24033

---

## Post #1 by @MatthewBrown (2022-06-24 17:14 UTC)

<p>Hello,<br>
I am currently creating a VR project to visualize an MRI in a VR environment and allow a patient and a doctor to connect to one another to analyze it together. The functionality for this is available in Unreal Engine specifically using the voxel plugin. The current plan is to create a 3D model of the MRI in slicer and then transfer it to either Unreal directly or into MagicaVoxel which has built in compatibility with Unreal’s plugin.<br>
If anyone knows a method that can allow slicer data to be saved in a voxel format it would be greatly appreciated.<br>
Thank you.</p>

---

## Post #2 by @lassoan (2022-06-24 19:55 UTC)

<p>This is very cool. So, it seems 3D Slicer’s Segment Editor module is actually an powerful voxel art editor.</p>
<p>You can create a .vox file in Slicer quite easily:</p>
<ul>
<li>Segment what you would like yo display using Segment Editor module</li>
<li>Export segmentation to labelmap</li>
<li>Crop and resample as needed using Crop volume module (to reduce file size)</li>
<li>Convert to unsigned char using Cast scalar volume</li>
<li>Export to .vox file by copy-pasting this code snippet into the Python console:</li>
</ul>
<pre><code class="lang-python"># This only needed once, may take a couple of minutes
pip_install('py-vox-io')

# Write labelmap volume to vox file
labelmapVolumeNode = getNode('Segmentation-Segment_1-label cropped')
outputFilePath = r'c:\Users\andra\VoxEdit\test\test2.vox'
import numpy as np
from pyvox.models import Vox
from pyvox.writer import VoxWriter
a = arrayFromVolume(labelmapVolumeNode)
vox = Vox.from_dense(a)
VoxWriter(outputFilePath, vox).write()
</code></pre>
<p>Here is how bones segmented from CTChest sample data look like in MagicaVoxel:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86fc56ad68f3f20e67575db729319a2e9c69b20f.jpeg" data-download-href="/uploads/short-url/jg8C44kSZr7wxTlo9WolqfeAYdp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86fc56ad68f3f20e67575db729319a2e9c69b20f_2_690x441.jpeg" alt="image" data-base62-sha1="jg8C44kSZr7wxTlo9WolqfeAYdp" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86fc56ad68f3f20e67575db729319a2e9c69b20f_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86fc56ad68f3f20e67575db729319a2e9c69b20f_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86fc56ad68f3f20e67575db729319a2e9c69b20f_2_1380x882.jpeg 2x" data-dominant-color="51514A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1229 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can see, the voxelized look is interesting, quite cool. However, probably you are much better off just saving the segmentations as .obj or export to .gltf (using SlicerOpenAnatomy extension) and visualize that, because the voxelization does not reproduce smooth surfaces very well.</p>
<p>As a comparison, the original smooth segmentation is rendered in Slicer like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bab65d48cea82087ba5cb4f9326bc6bc91dfe6e.jpeg" data-download-href="/uploads/short-url/3WM6NQdpm8j8mLTkCjjHsH0Rt26.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bab65d48cea82087ba5cb4f9326bc6bc91dfe6e_2_575x500.jpeg" alt="image" data-base62-sha1="3WM6NQdpm8j8mLTkCjjHsH0Rt26" width="575" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bab65d48cea82087ba5cb4f9326bc6bc91dfe6e_2_575x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bab65d48cea82087ba5cb4f9326bc6bc91dfe6e_2_862x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bab65d48cea82087ba5cb4f9326bc6bc91dfe6e_2_1150x1000.jpeg 2x" data-dominant-color="8894AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1192×1036 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Note that Slicer can directly display the scene content in a 3D headset and some collaborative virtual reality features are in the works, too. If you are interested in virtual reality then you may join related discussions and breakout sessions at the <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/">upcoming Slicer Project week</a> (starting on Monday).</p>

---

## Post #3 by @MatthewBrown (2022-08-08 17:50 UTC)

<p>Hello, I have been messing around with your code and I noticed that getNode is a function not defined in py-vox-io. How did you define that function? Is there another library you have used?</p>

---

## Post #4 by @lassoan (2022-08-09 06:39 UTC)

<p><code>getNode</code> and <code>arrayFromVolume</code> functions are in <code>slicer.util</code> package.</p>
<p>The code snippet is meant to be run in 3D Slicer Python environment (e.g., in the Python console that to can open by hitting <kbd>Ctrl</kbd>+<kbd>3</kbd>) to convert a labelmap volume node that is loaded into the application.</p>

---
