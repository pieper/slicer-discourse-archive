# Saving of MultiVolume Problems

**Topic ID**: 30590
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/saving-of-multivolume-problems/30590

---

## Post #1 by @Liam_S (2023-07-13 21:45 UTC)

<p>Hi<br>
I am using slicer 5.2.2 to segment 4D Cardiac CT data. I am trying to use sequences to segment each time point but there seems to be an issue with saving volume sequences and multivolume datasets.</p>
<p>I can load my image data just fine. I can use the sequence registration extension to create the transformation which takes warps an initial segmentation towards each time point in the sequence (a very cool extension) and when I scrub through time points I can assess the result as both the images and segmentations change to each time point appropriately.</p>
<p>However when I save the data I get a warning for each volume dataset:<br>
'Failed to delete directory: […]/TempWrite…"<br>
'Cannot write data file: … nrrd"</p>
<p>The resulting .nrrd file containing my 4D CT data is greately reduced in file size and the result seems to be that when I reload my project I somehow lose all but one time frame in my multivolume sequence (the sequence of segmentations still work but the image remains static).</p>
<p>Additionally the scene which loads then creates duplicate nodes of the various images, sequences and segmentations and I don’t know where these came from.</p>
<p>I can reimport the 4D CT dataset again but this isn’t an elegant work around and additionally I don’t know how to link this back to the original segmentation to start segmenting again.</p>
<p>I hope this explanation made sense. Is there something I am doing wrong or is there a known issue with saving and reloading sequences?</p>
<p>Kind regards<br>
Liam</p>

---

## Post #2 by @lassoan (2023-07-15 15:20 UTC)

<p>You either have run out of disk space, exceeded the maximum path length (that is rather short on Windows) or the temporary folder is not writable.</p>
<p>Nodes might be duplicated if you load both the scene (.mrml) file, which loads all the data nodes and you also load all the data files. The solution is to load a saved scene by only loading the .mrml file.</p>

---
