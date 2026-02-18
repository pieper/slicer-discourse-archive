# Draw line that is fit to segmented voxels using SVD

**Topic ID**: 31312
**Date**: 2023-08-23
**URL**: https://discourse.slicer.org/t/draw-line-that-is-fit-to-segmented-voxels-using-svd/31312

---

## Post #1 by @Annabel_W (2023-08-23 09:57 UTC)

<p>Hi there,</p>
<p>I am attempting to localise the end of intracranial electrodes within a CT scan. I have isolated an electrode in a binarised label map and am now trying to run SVD analysis.</p>
<p>I have been running this code;</p>
<pre><code class="lang-python">import numpy as np
import slicer
from slicer.ScriptedLoadableModule import *

# Load the binarized label map node (replace with your actual node name)
label_map_node = slicer.util.getNode("Segmentation_1-label")

# Convert the label map to a numpy array
label_map_array = slicer.util.arrayFromVolume(label_map_node)

# Get the indices where the electrode is labeled (assuming electrode label value is 1)
electrode_indices = np.where(label_map_array == 2)

# Convert indices to points
electrode_points = np.column_stack(electrode_indices)

# Calculate the centroid of the points
centroid = np.mean(electrode_points, axis=0)


# Perform Singular Value Decomposition (SVD) on the covariance matrix
covariance_matrix = np.cov(electrode_points, rowvar=False)
u, s, vh = np.linalg.svd(covariance_matrix)

# Line direction is the first singular vector
line_direction = vh[0]

# Generate endpoints of the line
line_length = 100  # Adjust this as needed
endpoint1 = centroid - line_direction * line_length / 2
endpoint2 = centroid + line_direction * line_length / 2

# Visualize the data and the line in 3D Slicer
view = slicer.app.layoutManager().threeDWidget(0).threeDView()
line_source = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode")
line_source.SetPositionWorldCoordinates1(endpoint1)
line_source.SetPositionWorldCoordinates2(endpoint2)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9af16aa9d340be04767c66f05f8bd193abbf8add.jpeg" data-download-href="/uploads/short-url/m6GLjUxzwqU9B2ZEZK5ibEpc1Rj.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af16aa9d340be04767c66f05f8bd193abbf8add_2_690x330.jpeg" alt="Capture" data-base62-sha1="m6GLjUxzwqU9B2ZEZK5ibEpc1Rj" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af16aa9d340be04767c66f05f8bd193abbf8add_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af16aa9d340be04767c66f05f8bd193abbf8add_2_1035x495.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9af16aa9d340be04767c66f05f8bd193abbf8add.jpeg 2x" data-dominant-color="32333D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1351×648 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The markup to show the location of the electrodes is present but in coordinated unrelating to the images.</p>
<p>Please could you give me some advise on how to resolve this.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-08-23 11:26 UTC)

<p>You have computed the line endpoint in voxel (IJK) coordinates (or maybe KJI, as you used numpy array indices). You need to convert these coordinates to world (RAS) coordinates as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-centroid-of-a-segment-in-world-ras-coordinates">this example</a> in the script repository.</p>

---

## Post #3 by @lassoan (2023-08-23 11:34 UTC)

<p>Also note that this feature (finding center of gravity, direction vector, extents) of segments is already implemented in Segment Statistics module. All you need to do is to segment the image, for example using Segment Editor use Threshold effect to get a segment that contains all electrodes, then use Islands effect to split each electrode into a separate segment, then run Segment Statistics to get position, size, orientation, shape descriptors, etc. of each segment. You can use these properties to determine which segments are actually electrodes (based on shape, size, position, etc.) and reject the rest. You can find an <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi">example in the script repository</a> for drawing an oriented box around each segment - you can slightly modify that to draw a line instead of a box.</p>

---
