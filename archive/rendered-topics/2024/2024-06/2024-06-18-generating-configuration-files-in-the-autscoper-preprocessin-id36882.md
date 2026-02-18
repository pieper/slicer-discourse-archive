# Generating configuration files in the Autscoper preprocessing module

**Topic ID**: 36882
**Date**: 2024-06-18
**URL**: https://discourse.slicer.org/t/generating-configuration-files-in-the-autscoper-preprocessing-module/36882

---

## Post #1 by @Amy_Morton (2024-06-18 16:06 UTC)

<p><a class="mention" href="/u/jeffrey_k_spear">@Jeffrey_K_Spear</a></p>
<p>Could you add some details about your data, which you’re trying to prep for use in Autoscoper?</p>

---

## Post #2 by @Jeffrey_K_Spear (2024-06-18 21:56 UTC)

<p>Details of my files:</p>
<p><strong>Radiographs:</strong><br>
Files were originally .avi video files that I converted to .jpg files in FIJI in order to read them into XMA Lab without lag. Originally I had exported them as .jpg files and then converted them to .tiff, but after we spoke I tried exporting the undistorted files directly as .tiffs. I then created a test dataset of only two radiograph images that I edited to be 1260x1260 squares (in Gimp). After editing the Mayacam files to be 1260x1260, I loaded our jury-rigged .cfg file but the images still don’t show up. So I suspect you’re right that important ‘hidden’ data got lost along the way somewhere. I will keep experimenting and let you know if I find anything. The next thing I plan to try is to read the .avi files directly into XMALab and then export undistorted .tiffs from there.</p>
<p><strong>CT data:</strong><br>
CT data was originally a .tiff stack that I read into Slicer.</p>
<p><strong>Segmentations/Volumes:</strong><br>
I segmented the bones directly in Slicer. I created the partial volumes using the Autoscoper pre-processing module. As we saw today, the volume files seem to load just fine when using the jury-rigged .cfg file.</p>
<p><strong>Calibration files:</strong><br>
My calibration files are Mayacam 2.0 files as .txt files exported from XMALab.</p>

---
