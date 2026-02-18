# How to change default snap to center slice when loading volume

**Topic ID**: 8057
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/how-to-change-default-snap-to-center-slice-when-loading-volume/8057

---

## Post #1 by @EricaMoreira (2019-08-16 09:28 UTC)

<p><strong>Operating system</strong> : macOS Mojave (version 10.14.6)<br>
<strong>Slicer version</strong> : 4.11.0-2019-07-29 r28413<br>
<strong>Desired behavior</strong> : Snap to the first slice of the volume when loaded<br>
<strong>Actual behavior</strong> : By default, the middle slice is displayed when the volume is loaded</p>
<p><strong>Details</strong> :</p>
<p>Is there a way to programmatically have the first slice of the volume displayed by default when a volume is loaded?</p>
<p>Which slice is displayed is controlled by the slider bar shown below, and the button circled in green snaps to the center slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc19c7b23011ccb0c61e770bdf186dc8c64a0dbb.png" data-download-href="/uploads/short-url/t7yDwynonATNMLPCkoJUjT2pRQn.png?dl=1" title="56%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc19c7b23011ccb0c61e770bdf186dc8c64a0dbb_2_690x88.png" alt="56%20AM" data-base62-sha1="t7yDwynonATNMLPCkoJUjT2pRQn" width="690" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc19c7b23011ccb0c61e770bdf186dc8c64a0dbb_2_690x88.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc19c7b23011ccb0c61e770bdf186dc8c64a0dbb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc19c7b23011ccb0c61e770bdf186dc8c64a0dbb.png 2x" data-dominant-color="CDBEBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">56%20AM</span><span class="informations">749×96 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I’m wondering if there a parameter I can add when loading the volume</p>
<p><code>[success, volume] = slicer.util.loadVolume(filename = image_path_slicer, returnNode=True)</code></p>
<p>to control that slider or the button?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-08-16 12:08 UTC)

<p>There is no volume loading parameter for centering on first slice.</p>
<p>You can get the physical position of the first slice  by converting its voxel position (i=(extent[0]+extent[1])/2; j=(extent[0]+extent[1])/2; k=0) to physical position as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates" rel="nofollow noopener">here</a> then <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates" rel="nofollow noopener">jump the slice to that position</a>.</p>

---
