# Separate Segmentation

**Topic ID**: 22776
**Date**: 2022-03-31
**URL**: https://discourse.slicer.org/t/separate-segmentation/22776

---

## Post #1 by @Jakob (2022-03-31 13:00 UTC)

<p>Operating system: macOS Monterey<br>
Slicer version: 4.13</p>
<p>Hello! I’ve made a segmentation of the upper airway using the Paint and Grow From Seeds Module in 3D Slicer. Now I would like to separate the segmentation of the upper airway in different segmentations (one for the nasopharyngeal part, one for the oropharyngeal part…) in order to calculate the volume of the segmentation for each part separately. How can I do this?<br>
Thank you very much!</p>

---

## Post #2 by @lassoan (2022-03-31 13:02 UTC)

<p>You can use the technique described in the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">craniotomy segmentation recipe</a>.</p>
<p>                    <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/image-005.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/image-005.png" width="487" height="500">
          </a>

</p>

---

## Post #3 by @rbumm (2022-03-31 13:33 UTC)

<p>Alternatively, you could clone the airway segmentation you have in the “Data” module to f.e.“trachea”:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ad14d8b8f2d5c7143835a261c838b4d877b5161.png" alt="image" data-base62-sha1="m5zXvJfWG9QDalrI4yHVjokXiqB" width="602" height="479"></p>
<p>then go “Segment editor” and use the “Scissors” effect with “Erase inside” to cut away the regions from the airway segmentation that you do not want in “trachea”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f47668944f8a6d7caf5b9343fa6da46c0782e52.jpeg" data-download-href="/uploads/short-url/bjkH5XLQLw8VrwNBJq44NKdOfui.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f47668944f8a6d7caf5b9343fa6da46c0782e52_2_690x309.jpeg" alt="image" data-base62-sha1="bjkH5XLQLw8VrwNBJq44NKdOfui" width="690" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f47668944f8a6d7caf5b9343fa6da46c0782e52_2_690x309.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f47668944f8a6d7caf5b9343fa6da46c0782e52_2_1035x463.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f47668944f8a6d7caf5b9343fa6da46c0782e52_2_1380x618.jpeg 2x" data-dominant-color="92939A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×860 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(Slicer demo data set with permission)</p>

---

## Post #4 by @Jakob (2022-04-01 13:47 UTC)

<p>Thank you very much for your solutions. It was exactly I was looking for.</p>

---
