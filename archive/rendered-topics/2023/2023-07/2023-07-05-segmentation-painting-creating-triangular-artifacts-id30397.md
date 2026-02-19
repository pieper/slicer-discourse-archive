---
topic_id: 30397
title: "Segmentation Painting Creating Triangular Artifacts"
date: 2023-07-05
url: https://discourse.slicer.org/t/30397
---

# Segmentation Painting creating triangular artifacts

**Topic ID**: 30397
**Date**: 2023-07-05
**URL**: https://discourse.slicer.org/t/segmentation-painting-creating-triangular-artifacts/30397

---

## Post #1 by @kaylaquest (2023-07-05 00:55 UTC)

<p>Hi everyone! First time posting here, so apologies if this is unclear, I can provide extra details if needed, but I am currently working on my first big project in slicer segmenting cephalic glands in snake heads. The anatomical planes of the scans were not aligned with the correct axes to start off with, so I’ve done a quick transform to rotate the heads into the proper position, then resampled the scalar volume using the lanczos interpolation method. Pretty much just following the steps of this video: <a href="https://www.youtube.com/watch?v=GkPHEsB9rOI" class="inline-onebox" rel="noopener nofollow ugc">Tutorial: Re-orientation of 3D volumes in 3DSlicer by Dr Jeremy Shaw - YouTube</a></p>
<p>Having the anatomical planes be aligned with the axes of the program is pretty important, because many of these cephalic head glands and other bits used for orientation are quite difficult to identify without easily visible symmetries and familiar planes through which to orientate oneself in the digital 3D space (if that makes sense).</p>
<p>The issue is, after completely segmenting two snake heads, I’ve had the issue of the third head ending up with stripe artifacts during segmentation that make the process much more difficult (at least, I think that’s what these are called. Because I’ve rotated the original volume in all three axes, the result is less the stripes shown <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" rel="noopener nofollow ugc">here</a> and more triangles and other non-quadrilateral shapes, thereby making incomplete segmentation on an individual layer and bleeding through into other nearby layers). I’ve tried several solutions to this thus far, to little or no success.</p>
<ol>
<li>Cropping the volume. Didn’t solve the problem.</li>
<li>Clicking the small button to the right of ‘Source Volume’ in segment editor, changing the source volume to the cropped version, turning on isotropic spacing, and the oversampling factor. The oversampling factor needs to be turned off to 2.5 or 3 in order to completely eliminate the artifacts, but this seems to quite quickly result in the program running out of memory and crashing, and each mark takes about a minute to process. Not ideal.</li>
<li>I am aware of the Rotate To Volume Plane button in the top bar of the slice windows, but that overall is counterproductive, because when I do it, it simply just seems to undo all the transformation progress I’ve made, turning the slices back into their original orientations.</li>
</ol>
<p>For additional help, I’ve been creating a WIP workflow to share with others working in the same lab, so these are the exact steps I’ve been following.</p>
<p><strong>3D Slicer</strong></p>
<p>Files were loaded into 3DSlicer using the SlicerMorph Extension. From the modules menu, SlicerMorph → Input and Output → ImageStacks. Then, the desired reconstructed file was selected for Filename Pattern, and images other than the first in the file seemed to work better. Note that the reconstructed file tended to be nested inside the original scan file. Adjust the spacing to the pixel size (convert µm to mm), then load a preview. In the Volume Rendering module, select the eye symbol next to Volume and Display ROI, and select a preset to display in the 3D window, adjusting the shift to get a clear image. Then, adjust the ROI to be as close around the intended area to analyze as possible, reducing the file size, then return to ImageStacks to load the model at half or even full size.</p>
<p><strong>Orientation of the Model</strong></p>
<ol>
<li>In the Volume Rendering module, make the volume and the Region of Interest (ROI) visible by clicking the ‘eye’ buttons next to each of them</li>
<li>Go the Data module. In the second tab, ‘Transform Hierarchy’, right click and select ‘Add Transform’. This should create a transformation with a name like ‘LinearTransform’. Then, back in the first tab, ‘Subject Hierarchy’, right click the grid icon at the far right of the module window for the volume being worked with (created during the previous ImageStacks step) and change the transform select the transformation created (for example, ‘LinearTransform’, in my case).</li>
<li>Go to the Transforms module, and move the file you are wanding to orient to the right window by selecting it and clicking the green arrow. Then, use the Rotation (and Translation, if necessary) tools to move the volume so that the coronal, sagittal, and transverse planes of the specimen line up with the coronal, sagittal, and transverse planes of the program. When this is complete, click the file in the Transformed window, and click the ‘Solidify Transforms’ button below the two green arrows to permanently apply the transformations to the figure.</li>
<li>Go to the Resample Scalar Volume module (you will have to look it up, select the <em>lanczos</em> option, the input volume to be the transformed one, and the output volume to be ‘Create New Volume As’. Name this with something you’ll remember, then hit apply. This might take a few minutes.</li>
<li>After that, you may note that the ROI in the slice windows will likely no longer be a rectangle, and the slices will not be the squared off segments you rotated the volume to get. To fix this, hover over the top left arrow of each window, and change the plane from ‘Reformatted’ to ‘Axial,’ ‘Sagittal’, or ‘Coronal’. This should fix the issue.</li>
<li>After this, cropping is important to prevent oblique slices from forming and complicating the segmentation process. Go to the “Crop Volume” Module, set the input volume to the output of your resampled scalar volume, select ‘Create New AnnotationROI As’ and name it, and select ‘Create New Volume As’ and name it. The bounding box will likely be diagonal, so return to the Data module, right click the grid icon which should be tilted, and set the transformation to ‘None’. This should bring the box in line. Then, set the white bounding box ROI around the figure, be sure the interpolator is set to linear, and click ‘Apply’</li>
</ol>

---

## Post #2 by @lassoan (2023-07-05 01:09 UTC)

<p>Have you seen the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">Oblique Slice Segmentation</a> page? It describes a workflow that uses a rotated ROI to reformat the image.</p>

---

## Post #3 by @kaylaquest (2023-07-05 23:29 UTC)

<p>NOTE: Solved (right before I was about to post this, but I’ll include the response I was gonna write for posterity’s sake).</p>
<p>Yeah, I was trying to follow the two recommended workflow/solutions there. The Option A workflow kind of works, like I said above, but is really slow (sometimes taking a minute to load a single brushstroke) and often causes the program to crash on me. So it is <em>sort of</em> a solution, but I guess I am sort of hoping for something better? If it exists.</p>
<p>Then there’s the rotated ROI method to reformat the image, which I’ve tried and unfortunately doesn’t work. Using the rotated and cropped volume as the source volume for segmentation still results in triangular artifacts.</p>
<p>Interestingly, I’ve been working on some other specimens while trying to figure this out, and don’t have the same issues with triangular artifacts, despite following the same exact steps. And I’ve tried doing the same process I described above several times over on the specimen giving me issues, to the same results of triangular artifacts. So I don’t really know what’s going on.</p>
<p><strong>SOLUTION:</strong> The solution that worked for me was making a new ‘segmentation’ from the drop-down menu using ‘Create New Segmentation’, instead of using a new cropped source volume. I think the program was trying to segment on angles that were outdated, in line with the original planes of the model, and thus creating the triangular artifacts, so even when using new source volumes, it was causing issues. But this solved it, thanks for your help!</p>

---

## Post #4 by @lassoan (2023-07-06 16:18 UTC)

<p>Thanks for the update. It is great that all works well for you now. As you have figured it out, you need to set up the source volume before starting segmentation.</p>
<p>This is so because segmentation geometry (origin, spacing, axis directions, extents) is set by the source volume <em>that is selected first</em>. If you later select a different source volume or the change the geometry of the source volume then it will have no effect (you may use many source volumes for creating your segmentation and you would not want your segmentation be resampled each time you switch between volumes).</p>
<p>To change the segmentation’s geometry, you can use the “Specify geometry” button in Segment Editor and then edit the segmentation (e.g., by applying Smoothing effect).</p>

---
