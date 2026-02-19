---
topic_id: 17015
title: "Changing Units For A Vtkmrmlscalarvolume Node"
date: 2021-04-09
url: https://discourse.slicer.org/t/17015
---

# Changing Units for a vtkMRMLScalarVolume Node

**Topic ID**: 17015
**Date**: 2021-04-09
**URL**: https://discourse.slicer.org/t/changing-units-for-a-vtkmrmlscalarvolume-node/17015

---

## Post #1 by @nathanbmnt (2021-04-09 16:22 UTC)

<p>I currently have a module where I load a volume with units of “Shear Wave Velocity”. I want users to be able to select different units for the volume such as “Young’s Modulus” or “Shear Modulus”. When different units are selected I need the threshold, window/level, and color bar to convert accordingly. The conversion equation for Shear Wave Velocity to Young’s Modulus is<br>
youngs_modulus = (shear_wave_velocity ^ 2) * 3.0</p>
<p>Shear wave velocity:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46c8cc1ce95ede47b419030714879d07d2f22c17.jpeg" data-download-href="/uploads/short-url/a6bD0Djm6LtA7v7TTeUPLkTgjgX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/46c8cc1ce95ede47b419030714879d07d2f22c17_2_220x500.jpeg" alt="image" data-base62-sha1="a6bD0Djm6LtA7v7TTeUPLkTgjgX" width="220" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/46c8cc1ce95ede47b419030714879d07d2f22c17_2_220x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46c8cc1ce95ede47b419030714879d07d2f22c17.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46c8cc1ce95ede47b419030714879d07d2f22c17.jpeg 2x" data-dominant-color="424C5B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">322×731 67.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Young’s Modulus:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7f6d23131e837477d5720ff4981d7b53951717.jpeg" data-download-href="/uploads/short-url/8luHzZ7fssn5yo9n4VaRKU8UzAj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a7f6d23131e837477d5720ff4981d7b53951717_2_214x500.jpeg" alt="image" data-base62-sha1="8luHzZ7fssn5yo9n4VaRKU8UzAj" width="214" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a7f6d23131e837477d5720ff4981d7b53951717_2_214x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7f6d23131e837477d5720ff4981d7b53951717.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7f6d23131e837477d5720ff4981d7b53951717.jpeg 2x" data-dominant-color="3F4157"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">313×729 65.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But I also want to save the voxel data somewhere in its original Shear Wave Velocity units so I can calculate things based off the original data.</p>
<p>The way I currently do this is that I have the original volume (vtkMRMLScalarVolumeNode1) which the user never sees, and a display volume (vtkMRMLScalarVolumeNode2). When the user selects new units, I get the voxel value array of vtkMRMLScalarVolume1 with slicer.util.arrayFromVolume(vol_1).copy(), run my conversion equation on the array, and change the voxel values of my display volume with slicer.util.updateVolumeFromArray(new_arr, vol_2)</p>
<p>Unfortunately I then have to also convert the threshold min max and window/level of the display volume to the new units. Is there a better way to do this rather than have a second vtkMRMLScalarVolumeNode for display? Like could I have multiple vtkMRMLScalarVolumeDisplayNodes for vtkMRMLScalarVolumeNode1 which are in different units than vtkMRMLScalarVolumeNode1?</p>

---

## Post #2 by @jamesobutler (2021-04-12 12:50 UTC)

<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Are there examples of other image sets where Slicer already does some changing to a different unit representation?</p>
<p>To show a volume and do things like run stats on it, would you have to create a new volume node with the image data scaled to the new representation? Or is this something that should actually be handled by a display node? A new volume node would seemingly be an expensive operation if changing representation of a sequence volume where there is a lot more data.</p>
<p>The described situation of different unit representations and their relationship to MRML widgets such as for Window/Level and Threshold seem to be a bit of a bear if representations can’t be synced somehow. Such as if one uses a threshold min/max of 3/10 and then you select a representation which is the values squared, you would want the widget values to be 9/100. This would maintain the same pixels shown just in a different unit representation.</p>

---

## Post #3 by @lassoan (2021-04-12 18:59 UTC)

<aside class="quote no-group" data-username="nathanbmnt" data-post="1" data-topic="17015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/a9adbd/48.png" class="avatar"> nathanbmnt:</div>
<blockquote>
<p>I currently have a module where I load a volume with units of “Shear Wave Velocity”. I want users to be able to select different units for the volume such as “Young’s Modulus” or “Shear Modulus”. When different units are selected I need the threshold, window/level, and color bar to convert accordingly.</p>
</blockquote>
</aside>
<p>Thresholding and window/level is easy, you just set up the display node when you generate the volume.</p>
<p>Scalar bar is a bit more tricky, because you need to set the unit manually in the color bar (in DataProbe module). The proper solution would be to use VoxelValueQuantity and VoxelValueUnits properties of the volume node and generate the label based on that automatically. You can either update the DataProbe module to do this (it is just a Python scripted module that you can change easily; we can help you getting started) or you can implement this label update in your own module.</p>
<aside class="quote no-group" data-username="nathanbmnt" data-post="1" data-topic="17015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/a9adbd/48.png" class="avatar"> nathanbmnt:</div>
<blockquote>
<p>Unfortunately I then have to also convert the threshold min max and window/level of the display volume to the new units.</p>
</blockquote>
</aside>
<p>There is absolutely nothing wrong with this. Your module can very quickly and easily can generate all the quantities that you are interested in. Probably the simplest is to generate all the volumes the user could be interested in. Since ultrasound images are relatively small (usually medium-resolution 2D+t images; or low-resolution 3D+t images) computation time and memory needs should be negligible.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="17015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Are there examples of other image sets where Slicer already does some changing to a different unit representation?</p>
</blockquote>
</aside>
<p>We currently do all real world value mapping (RWVM) at import/export. There are so many ways of converting stored values to real world values (transforming with linear or arbitrary non-linear function, piece-wise linear function, or lookup-tables) that it would not be feasible to build that into all visualization and processing functions. If we added RWVM infrastructure to MRML then we would need to store both the raw and converted volume, thereby increasing complexity, memory usage, potential inconsistencies when saving/loading the data (or slower loading due to conversion after loading).</p>
<p>MRML scalar volume can already store quantity and units, which allows modules to cleanly manage different raw and real world value volumes. What should be improved is how this information is utilized - for example in Data Probe, scalar bar, sliders/spinboxes that display voxel values.</p>

---
