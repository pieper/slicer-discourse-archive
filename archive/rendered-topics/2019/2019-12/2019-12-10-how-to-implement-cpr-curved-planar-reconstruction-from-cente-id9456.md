# How to implement CPR (curved planar reconstruction) from centerline?

**Topic ID**: 9456
**Date**: 2019-12-10
**URL**: https://discourse.slicer.org/t/how-to-implement-cpr-curved-planar-reconstruction-from-centerline/9456

---

## Post #1 by @RayCui (2019-12-10 03:01 UTC)

<p>I want to show the vessel in planar. Now I have a .csv file of centerline, that contains points of the veseel. How to reconstruction the vessel plannar from centerline file?</p>
<ol>
<li>How to import the csv file as a list of some point?</li>
<li>How to reconstruction and show in the window?</li>
</ol>
<p>And If the centerline file is a mask file, such as .mhd segmentation file (just some points). How can I implement CPR?</p>

---

## Post #2 by @timeanddoctor (2019-12-10 10:53 UTC)

<p>you can create a curve with ‘curvemaker’ module from your csv file readed with numpy.</p>

---

## Post #3 by @lassoan (2019-12-10 19:57 UTC)

<aside class="quote no-group" data-username="RayCui" data-post="1" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raycui/48/4517_2.png" class="avatar"> RayCui:</div>
<blockquote>
<p>How to import the csv file as a list of some point?</p>
</blockquote>
</aside>
<p>You can load a curve from a CSV file that has this structure:</p>
<pre data-code-wrap="csv"><code class="lang-csv"># Markups fiducial file version = 4.11
# CoordinateSystem = 0
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
1,-48.966353538964675,-101.7065776156342,74.67105263157896,0,0,0,1,1,1,0,MarkupsCurve-1,,
1,-53.75692521242794,-85.6239441404361,66.4605263157895,0,0,0,1,1,1,0,MarkupsCurve-2,,
1,-60.86814580722918,-72.76476934319273,60.7763157894737,0,0,0,1,1,1,0,MarkupsCurve-3,,
1,-65.87663276996875,-62.425437293974404,57.87936805530591,0,0,0,1,1,1,0,MarkupsCurve-4,,
1,-73.58132198684874,-44.72104505093102,57.37936805530591,0,0,0,1,1,1,0,MarkupsCurve-5,,
</code></pre>
<p>To load from Python, you can <code>curveNode = slicer.util.loadMarkupsCurve('some/folder/MarkupsCurve.fcsv')</code> (this convenience function is available in Slicer Preview Release downloaded tomorrow or later).</p>
<aside class="quote no-group" data-username="RayCui" data-post="1" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raycui/48/4517_2.png" class="avatar"> RayCui:</div>
<blockquote>
<p>How to reconstruction and show in the window?</p>
</blockquote>
</aside>
<p>I created a script for CPR earlier, but to make it more accessible, I’ve now added it as a module (“Curved Planar Reformat”) to SlicerSandbox extension. It is available for Slicer Preview Releases you download tomorrow or later (in Examples category).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/047b2b59aee261fee3f5d24781436ed5b916629e.jpeg" data-download-href="/uploads/short-url/DDNxeQZtU3mFWgG459I6bVbtV4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/047b2b59aee261fee3f5d24781436ed5b916629e_2_690x373.jpeg" alt="image" data-base62-sha1="DDNxeQZtU3mFWgG459I6bVbtV4" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/047b2b59aee261fee3f5d24781436ed5b916629e_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/047b2b59aee261fee3f5d24781436ed5b916629e_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/047b2b59aee261fee3f5d24781436ed5b916629e_2_1380x746.jpeg 2x" data-dominant-color="919095"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 396 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @RayCui (2019-12-11 02:22 UTC)

<p>Thank you for your response.<br>
Can you explain the meaning of CoordinateSystem and columns?</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto"># CoordinateSystem = 0 
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
</code></pre>
</blockquote>
</aside>
<p>And what’s the version of Slicer Preview Releases? I can’t find the SlicerSandbox extension in revision 28669 built 2019-12-10.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>a module (“Curved Planar Reformat”) to SlicerSandbox extension</p>
</blockquote>
</aside>

---

## Post #5 by @lassoan (2019-12-11 04:00 UTC)

<p>See description of file format <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups#File_Format">here</a>. You just need to set x, y, z values and leave the rest as in the example.</p>
<p>The Sandbox is in the Examples category in the extension manager. Use Slicer rev 28672 or later.</p>

---

## Post #6 by @RayCui (2019-12-11 05:30 UTC)

<p>Where can I download Slicer rev 28672 or later? This link contains the newest Preview Release is rev 28669.<br>
<a href="https://download.slicer.org/" class="onebox" target="_blank" rel="nofollow noopener">https://download.slicer.org/</a></p>

---

## Post #7 by @muratmaga (2019-12-11 08:00 UTC)

<p>Hi Andras,</p>
<p>Sometimes people end up having to scan coiled snakes, or fish that are in little jars. Depending on what they need to do with it, they may have to ‘straighten’ the specimen. Is there a way this CPR can be generalized for such use cases?</p>
<p><img src="https://www.morphosource.org/media/morphosource/images/3/7/9/78366_ms_media_files_media_37923_preview190.jpg" alt width="190" height="190"></p>
<p><img src="https://www.3ders.org/images2017/universities-3d-scan-20000-vertebrates-morphosource-digital-database-2.jpg" alt width="600" height="447"></p>

---

## Post #8 by @timeanddoctor (2019-12-11 10:47 UTC)

<p>Is this micro-CT and has any three dimensional sigmentation?</p>

---

## Post #9 by @lassoan (2019-12-11 13:45 UTC)

<p>The module is already completely generic, so it can straighten snakes just as well as vessels. It would be great if you could post a few examples.</p>
<p>Here is one snake from MorphoSource straightened:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/762a741ad1acf6ebf98c76f98818b9dc64a54602.jpeg" data-download-href="/uploads/short-url/gRlisHPHakzv59ppGJyRfgG1Dvc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/762a741ad1acf6ebf98c76f98818b9dc64a54602_2_690x198.jpeg" alt="image" data-base62-sha1="gRlisHPHakzv59ppGJyRfgG1Dvc" width="690" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/762a741ad1acf6ebf98c76f98818b9dc64a54602_2_690x198.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/762a741ad1acf6ebf98c76f98818b9dc64a54602_2_1035x297.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/762a741ad1acf6ebf98c76f98818b9dc64a54602_2_1380x396.jpeg 2x" data-dominant-color="9194CA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1831×526 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>if the specimen touches itself then you need to apply masking and sharp breaks and wrinkles due to squeezing into a container cannot be fully compensated for, but it works quite well.</p>

---

## Post #10 by @manjula (2019-12-11 13:54 UTC)

<p>I cannot find the the curve planar reformat module to do this ? Where can i find it ? i am using the stable version and the nightly build 28669.</p>
<p>Or can you point me to a tutorial where  i could do this please ?</p>
<p>thank you</p>

---

## Post #11 by @lassoan (2019-12-11 13:58 UTC)

<p>Extensions are not available yet for 28669. Probably because today is Wednesday and Windows patches are usually installed Tuesday nights, which can interrupt the nightly build process. I expect the extensions will be available in a few hours.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Could you check the factory machines / restart the extensions build?</p>

---

## Post #12 by @jcfr (2019-12-11 14:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you check the factory machines / restart the extensions build?</p>
</blockquote>
</aside>
<p>After the associated build directory is cleaned, the extension build will be restarted.</p>
<p>Update: Windows extensions build in progress <img src="https://emoji.discourse-cdn.com/twitter/hourglass_flowing_sand.png?v=12" title=":hourglass_flowing_sand:" class="emoji" alt=":hourglass_flowing_sand:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @muratmaga (2019-12-11 16:31 UTC)

<p>Wow, this looks great thank you Andras!</p>

---

## Post #14 by @e36alpine (2020-06-01 16:05 UTC)

<p>Hi everyone,  I have been trying to figure this module out for a while now.  Unfortunately I’m not getting the same results as you.  Would someone mind posting a youtube video on exactly how this works.  It seems pretty straight forward but I think the rotation angle is messing me up?  Also if the CT scan itself is angled I can’t figure out how to transform it back straight (if that is even necessary).  How do you figure out that angle?  Any help is much appreciated as these reconstructions are no long offered to our in house surgeons without having to pay.</p>

---

## Post #15 by @e36alpine (2020-06-01 16:09 UTC)

<p>Also, which series are you using from the data set?  Thanks!</p>

---

## Post #16 by @Neda (2020-06-25 09:25 UTC)

<p>Is it possible to get the transformation matrix/formula for this 3D to 2D projection (I mean generation of panoramic image based on the curve/points and initial 3D volume)?</p>

---

## Post #17 by @lassoan (2020-06-25 20:53 UTC)

<aside class="quote no-group" data-username="e36alpine" data-post="14" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/a9a28c/48.png" class="avatar"> e36alpine:</div>
<blockquote>
<p>I have been trying to figure this module out for a while now. Unfortunately I’m not getting the same results as you. Would someone mind posting a youtube video on exactly how this works. It seems pretty straight forward but I think the rotation angle is messing me up?</p>
</blockquote>
</aside>
<p>Sorry for the delayed response. We have a new version of the module now. It does not have the rotation angle slider anymore but instead the output volume is automatically aligned with the input volume. You can rotate reslicing axes as shown in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="WJQexDTiRRc" data-video-title="Transform markups between original and straightened vessel" data-video-start-time="179" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=WJQexDTiRRc&amp;t=179" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/WJQexDTiRRc/maxresdefault.jpg" title="Transform markups between original and straightened vessel" width="" height="">
  </a>
</div>

<aside class="quote no-group" data-username="Neda" data-post="16" data-topic="9456" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neda/48/7160_2.png" class="avatar"> Neda:</div>
<blockquote>
<p>Is it possible to get the transformation matrix/formula for this 3D to 2D projection (I mean generation of panoramic image based on the curve/points and initial 3D volume)?</p>
</blockquote>
</aside>
<p>Projection is done by <a href="https://github.com/PerkLab/SlicerSandbox/blob/6e7c5c2c59bd313222a47aad8c620957fd9713b0/CurvedPlanarReformat/CurvedPlanarReformat.py#L334-L339">simple averaging</a>, which corresponds to X-ray projection (with intensity normalization). If you need minimum or maximum intensity projection then you may just replace <code>mean</code> by <code>min</code> or <code>max</code>.</p>

---

## Post #18 by @Neda (2020-07-02 08:57 UTC)

<p>Thanks for the reply, by projection I mean the straightening transformation of the volume. Having the volume in nrrd fomrat (ijk coordinates) and points of the curve from Slicer (LAS/world coordinates?) I am trying to do this in Python. Could you please clarify the following points:<br>
1- In CurvedPlanarReformat script<a href="https://github.com/PerkLab/SlicerSandbox/blob/6e7c5c2c59bd313222a47aad8c620957fd9713b0/CurvedPlanarReformat/CurvedPlanarReformat.py#L359" rel="noopener nofollow ugc">https://github.com/PerkLab/SlicerSandbox/blob/6e7c5c2c59bd313222a47aad8c620957fd9713b0/CurvedPlanarReformat/CurvedPlanarReformat.py#L359</a>,<br>
we get the transformation 4x4 matrix from point to world by “GetCurvePointToWorldTransformAtPointIndex”.<br>
If I want to get this matrix from DICOM parametetrs, Is this the right formula: [[spacing_x, 0 ,0, origin_x],[0,spacing_y, 0, origin_y],[0, 0 ,spacing_z, origin_z],[0 ,0 ,0 ,1]]?<br>
Is this the matrix to transform the curve points (gotten from Slicer markups) from slicer/world coordinates to image (ijk) coordinates so that I can proceed with the straightening transformation in a consistent coordinate?<br>
2- In the same script, could you explain how you define the grid dimension?<br>
“gridDimensions = [2, 2, numberOfSlices]”, what is 2 for? and why the dimension in x and y different from z?<br>
3- In “CurvedPlanarReformating.py” <a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07" rel="noopener nofollow ugc">https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07</a><br>
The panoramic plane spacing is defined base on FOV and image size, could you explain how exactly?</p>
<p>This is my current code (inspired by CurvedPlanarReformat script and tried to make it independently running in Python):</p>
<blockquote>
<p>import os<br>
import nrrd<br>
import csv<br>
import nrrd<br>
import pandas as pd<br>
import numpy as np<br>
from numpy.linalg import svd</p>
<p>def curveLength(x,y,z):<br>
diffs = np.sqrt(np.diff(x)**2+np.diff(y)**2+np.diff(z)**2)<br>
length = diffs.sum()</p>
<pre><code>return length
</code></pre>
<p>def planeFit(points):<br>
“”"<br>
p, n = planeFit(points)<br>
Given an array, points, of shape (d,…)<br>
representing points in d-dimensional space,<br>
fit an d-dimensional plane to the points.<br>
Return a point, p, on the plane (the point-cloud centroid),<br>
and the normal, n.<br>
“”"<br>
points = points.T # dimension is (N,3)<br>
points = np.reshape(points, (np.shape(points)[0], -1)) # Collapse trialing dimensions<br>
assert points.shape[0] &lt;= points.shape[1], “There are only {} points in {} dimensions.”.format(points.shape[1], points.shape[0])<br>
ctr = points.mean(axis=1)<br>
x = points - ctr[:,np.newaxis]<br>
M = np.dot(x, x.T) # Could also use np.cov(x) here.<br>
return ctr, svd(M)[0][:,-1]</p>
<p>def readPoints():</p>
<pre><code>pandas_data = pd.read_csv(r'path to \F.fcsv', sep=',', skiprows=3)
numpy_data = np.asarray(pandas_data)
all_points = np.asarray(numpy_data[:,1:4], 'float')
return all_points
</code></pre>
<p>def computeStraighteningTransform(curvePoints, outputSpacingMm = 0.1):</p>
<pre><code>transformation_RAS2ijk = np.array([[-0.287, 0 ,0, 73.212],[0, -0.287, 0, 75.644],[0, 0 ,0.287, -80.779],[0 ,0 ,0 ,1]]) # gotten from DICOM header

# Slice thickness characterizes how sharply focused your image slice is. can be found in metadata of CT
sliceSizeMm = [0.287,  0.287, 0.287]
curve_length = curveLength(curvePoints[:,0], curvePoints[:,1], curvePoints[:,2])
nPoints = curvePoints.shape[0]

transformSpacingFactor = 5 # there is no need to compute displacement for each slice we just compute for every n-th to make computation faster and inverse computation more robust

resamplingCurveSpacing = outputSpacingMm * transformSpacingFactor

# Z axis (from first curve point to last, this will be the straightened curve long axis)
#transformGridAxisZ = (curveEndPoint-curveStartPoint)/np.linalg.norm(curveEndPoint-curveStartPoint)
transformGridAxisZ = (curvePoints[-1,:]-curvePoints[0,:])/np.linalg.norm(curvePoints[-1,:]-curvePoints[0,:])


# X axis = average X axis of curve, to minimize torsion (and so have a simple displacement field, which can be robustly inverted)
sumCurveAxisX_RAS = np.zeros(3)
for nSlices in range(nPoints):

	curvePointToWorldArray = transformation_RAS2ijk

    curveAxisX_RAS = curvePointToWorldArray[0:3, 0]
    sumCurveAxisX_RAS += curvePoints[nSlices,:]

meanCurveAxisX_RAS = sumCurveAxisX_RAS/np.linalg.norm(sumCurveAxisX_RAS)
transformGridAxisX = meanCurveAxisX_RAS

# Y axis
transformGridAxisY = np.cross(transformGridAxisZ, transformGridAxisX)
transformGridAxisY = transformGridAxisY/np.linalg.norm(transformGridAxisY)

# Make sure that X axis is orthogonal to Y and Z
transformGridAxisX = np.cross(transformGridAxisY, transformGridAxisZ)
transformGridAxisX = transformGridAxisX/np.linalg.norm(transformGridAxisX)


# Origin (makes the grid centered at the curve)
planeCenter, norm = planeFit(curvePoints)

transformGridOrigin = planeCenter
transformGridOrigin -= transformGridAxisX * sliceSizeMm[0]/2.0
transformGridOrigin -= transformGridAxisY * sliceSizeMm[1]/2.0
transformGridOrigin -= transformGridAxisZ * curve_length/2.0

# Create grid transform
# Each corner of each slice is mapped from the original volume's reformatted slice
# to the straightened volume slice.
# The grid transform contains one vector at the corner of each slice.
# The transform is in the same space and orientation as the straightened volume.

gridDimensions = [2, 2, nPoints]
gridSpacing = [sliceSizeMm[0], sliceSizeMm[1], resamplingCurveSpacing]
gridDirectionMatrixArray = np.eye(4)
gridDirectionMatrixArray[0:3, 0] = transformGridAxisX
gridDirectionMatrixArray[0:3, 1] = transformGridAxisY
gridDirectionMatrixArray[0:3, 2] = transformGridAxisZ


transformDisplacements_RAS = np.zeros((gridDimensions[0],gridDimensions[1],gridDimensions[2]))

for gridK in range(gridDimensions[2]):

    curvePointToWorldArray = transformation_RAS2ijk

    curveAxisX_RAS = curvePointToWorldArray[0:3, 0]
    curveAxisY_RAS = curvePointToWorldArray[0:3, 1]
    curvePoint_RAS = curvePointToWorldArray[0:3, 3]
    for gridJ in range(gridDimensions[1]):
        for gridI in range(gridDimensions[0]): 
            straightenedVolume_RAS = (transformGridOrigin+ gridI*gridSpacing[0]*transformGridAxisX+ gridJ*gridSpacing[1]*transformGridAxisY+ gridK*gridSpacing[2]*transformGridAxisZ)
            inputVolume_RAS = (curvePoint_RAS + (gridI-0.287)*sliceSizeMm[0]*curveAxisX_RAS + (gridJ-0.287)*sliceSizeMm[1]*curveAxisY_RAS)
            transformDisplacements_RAS[gridK][gridJ][gridI] = inputVolume_RAS - straightenedVolume_RAS # TODO ValueError: setting an array element with a sequence.

return transformDisplacements_RAS
</code></pre>
</blockquote>

---

## Post #19 by @lassoan (2020-12-06 04:22 UTC)

<p>A post was split to a new topic: <a href="/t/loading-markups-curves-from-fcsv-file/14906">Loading markups curves from fcsv file</a></p>

---

## Post #20 by @lassoan (2020-12-06 04:41 UTC)

<aside class="quote no-group" data-username="Neda" data-post="18" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neda/48/7160_2.png" class="avatar"> Neda:</div>
<blockquote>
<p>If I want to get this matrix from DICOM parametetrs, Is this the right formula: [[spacing_x, 0 ,0, origin_x],[0,spacing_y, 0, origin_y],[0, 0 ,spacing_z, origin_z],[0 ,0 ,0 ,1]]?</p>
</blockquote>
</aside>
<p>Internal Slicer coordinate system is RAS, but all files that Slicer writes are in LPS. DICOM is LPS.</p>
<p>If you run the processing in Slicer then everything is in RAS, so you don’t need RAS&lt;-&gt;LPS conversion. If you use DICOM and files that Slicer created then everything is LPS, so you don’t need RAS&lt;-&gt;LPS conversion either.</p>
<p>If for any other scenario you need LPS/RAS conversion then multiply the homogeneous coordinates by <code>np.diag([-1,-1,1,1])</code>.</p>
<aside class="quote no-group" data-username="Neda" data-post="18" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neda/48/7160_2.png" class="avatar"> Neda:</div>
<blockquote>
<p>In the same script, could you explain how you define the grid dimension?<br>
“gridDimensions = [2, 2, numberOfSlices]”, what is 2 for? and why the dimension in x and y different from z?</p>
</blockquote>
</aside>
<p>Since we apply the same transform to all points within a slice, it is enough to specify transform at the 4 corners of a slice (that’s why the first 2, 2). <code>numberOfSlices</code> is up to the user to decide: you just need to choose a resolution that you want in your output image, compute the transforms for each, and store the result in this array.</p>
<aside class="quote no-group" data-username="Neda" data-post="18" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neda/48/7160_2.png" class="avatar"> Neda:</div>
<blockquote>
<p>n “CurvedPlanarReformating.py” <a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07">https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07 </a><br>
The panoramic plane spacing is defined base on FOV and image size, could you explain how exactly</p>
</blockquote>
</aside>
<p>That was a preliminary implementation. The implementation in the Sandbox extension is completely reworked and all the spacings are computed accurately.</p>
<aside class="quote no-group" data-username="Neda" data-post="18" data-topic="9456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neda/48/7160_2.png" class="avatar"> Neda:</div>
<blockquote>
<p>This is my current code (inspired by CurvedPlanarReformat script and tried to make it independently running in Python):</p>
</blockquote>
</aside>
<p>The original CurvedPlanerReformat approach proved to be a dead end. Since it did not provide a grid transform, it was impossible to transform meshes, curves, landmark points along with the image (images require inverse transform, points/lines/meshes require forward transform) and performance is suffered, too, because you always had to compute a complete straightened volume (while if you have a transform then you can extract just the single slice that you display).</p>

---

## Post #21 by @lassoan (2020-12-06 07:02 UTC)

<p>A post was merged into an existing topic: <a href="/t/load-markups-curve-from-file/14905/5">Load markups curve from file</a></p>

---

## Post #22 by @MOMOANNIE (2024-08-19 07:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hello, if I want to use [CPR (curved planar reconstruction)]) on PyCharm to process my own DICOM data, what should I do?</p>

---

## Post #23 by @lassoan (2024-08-19 13:14 UTC)

<p>That should be no problem. See a full example of how to use the Curved Planar Reformat module from a Python script <a href="https://github.com/PerkLab/SlicerSandbox/blob/461f25eb6a1a36cd26d437dc47014f3e4cd5bfc3/CurvedPlanarReformat/CurvedPlanarReformat.py#L526-L561">here</a>. The module requires the Python environment embedded in the 3D Slicer application. If you want to debug in PyCharm then you can follow <a href="https://github.com/SlicerRt/SlicerDebuggingTools">these instructions</a>.</p>

---

## Post #24 by @MOMOANNIE (2024-08-20 02:46 UTC)

<p>Are there corresponding version requirements for Pycharm and 3D slicer?</p>

---

## Post #25 by @MOMOANNIE (2024-08-20 10:09 UTC)

<p>Hello, when I debug CurvedPlanarReformat.py, the 3D slicer python console shows this prompt, how can I solve this? My pycharm version is 20241.4, and the 3D slicer version is 5.6.5<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c90b1b4a537320b97c17816ce41c0c4abd0ab9d.png" data-download-href="/uploads/short-url/fupzv9VC8dQSl65IOYSlCPFffzL.png?dl=1" title="Snipaste_2024-08-20_18-09-20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c90b1b4a537320b97c17816ce41c0c4abd0ab9d_2_633x500.png" alt="Snipaste_2024-08-20_18-09-20" data-base62-sha1="fupzv9VC8dQSl65IOYSlCPFffzL" width="633" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c90b1b4a537320b97c17816ce41c0c4abd0ab9d_2_633x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c90b1b4a537320b97c17816ce41c0c4abd0ab9d_2_949x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c90b1b4a537320b97c17816ce41c0c4abd0ab9d.png 2x" data-dominant-color="26282B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2024-08-20_18-09-20</span><span class="informations">1115×880 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c840438b723555bf03a0e8669e4758da682957d2.png" data-download-href="/uploads/short-url/szvb56b11RyQQDVK2NYuUWQ4NtE.png?dl=1" title="Snipaste_2024-08-20_18-08-52" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c840438b723555bf03a0e8669e4758da682957d2.png" alt="Snipaste_2024-08-20_18-08-52" data-base62-sha1="szvb56b11RyQQDVK2NYuUWQ4NtE" width="638" height="500" data-dominant-color="DFD8D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2024-08-20_18-08-52</span><span class="informations">922×722 56.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
