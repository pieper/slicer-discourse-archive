# Can’t cut away unwanted tissue

**Topic ID**: 20417
**Date**: 2021-10-30
**URL**: https://discourse.slicer.org/t/can-t-cut-away-unwanted-tissue/20417

---

## Post #1 by @mdear (2021-10-30 02:26 UTC)

<p>Newbie question.<br>
I pull in DICOM data, go to data module and drag the data series into the 3D window. I then go to the segmentation editor and select threshold tool and select all voxels. I then select the box to allow me to select on the 3D window.  use cut tool to cut away unwanted portions. I see the cut away portions disappearing up on the three slice views but the voxels do not disappear from the 3D view. What am I missing here ?  Those extra voxels are obstructing the view I want. Thanks.</p>

---

## Post #2 by @lassoan (2021-10-30 03:26 UTC)

<p>If you display the volume using volume rendering then you can use Mask volume effect to remove (blank out) parts of the volume that occlude your view:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' width="" height="">
  </a>
</div>


---

## Post #3 by @mdear (2021-10-30 23:51 UTC)

<p>Fabulous, thanks!  I’m getting better at this every day.  Appreciate the pointer.</p>

---
