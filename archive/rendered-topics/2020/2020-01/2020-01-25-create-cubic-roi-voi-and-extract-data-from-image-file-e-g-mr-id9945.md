# Create cubic ROI (VOI) and extract data from image file (e.g MRI)?

**Topic ID**: 9945
**Date**: 2020-01-25
**URL**: https://discourse.slicer.org/t/create-cubic-roi-voi-and-extract-data-from-image-file-e-g-mri/9945

---

## Post #1 by @sfglio (2020-01-25 17:22 UTC)

<p>I want to draw/create a cubic VOI of 1cm x 1cm x 0.5cm, I haven’t found the right tool in editor/segment editor??<br>
Furthermore I want to place this VOI into a MRI image and save this VOI (but including the dimensions of the original MRI data set. i.e. I assume the VOI needs to be transformed based on the dimensions of the MRI).<br>
Last but not least is there an option to extract the image content of the VOI box?</p>
<p>kind regards<br>
florian</p>

---

## Post #2 by @lassoan (2020-01-26 02:30 UTC)

<p>You can create a model node of such a box (using “Create models” module of SlicerIGT extension or a few-line python script). Then translate/rotate using a transform node (you can use interactive widget in 3D views - can be enabled in Transforms module; or using markups points, lines, etc).</p>
<p>There are several examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">Python script repository</a> that you can use, if you want to create automated/customized tools.</p>

---

## Post #3 by @sfglio (2020-01-26 10:40 UTC)

<p>Thank you for your fast reply!!!<br>
However I fail to see/rotate the 3d cube on the dicom image (after I set the cube to transform under Transforms). Is there a chance to change to colour of the cube (or can it be only done in python?)</p>

---

## Post #4 by @manjula (2020-01-26 11:48 UTC)

<p>You can always easily change the color of the cube by clicking on the node color icon and selecting the desired color.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbcc1aa3f8eaebdb9dc83ae7df035e930f9ad2c1.png" data-download-href="/uploads/short-url/vmpR8bTROVbep1yPtaEl3f6PQUV.png?dl=1" title="Screenshot from 2020-01-26 12-46-38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbcc1aa3f8eaebdb9dc83ae7df035e930f9ad2c1_2_690x300.png" alt="Screenshot from 2020-01-26 12-46-38" data-base62-sha1="vmpR8bTROVbep1yPtaEl3f6PQUV" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbcc1aa3f8eaebdb9dc83ae7df035e930f9ad2c1_2_690x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbcc1aa3f8eaebdb9dc83ae7df035e930f9ad2c1_2_1035x450.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbcc1aa3f8eaebdb9dc83ae7df035e930f9ad2c1_2_1380x600.png 2x" data-dominant-color="6F5D73"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-01-26 12-46-38</span><span class="informations">1816×792 87.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-01-26 14:50 UTC)

<aside class="quote no-group" data-username="sfglio" data-post="3" data-topic="9945">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sfglio/48/3346_2.png" class="avatar"> sfglio:</div>
<blockquote>
<p>However I fail to see/rotate the 3d cube on the dicom image (after I set the cube to transform under Transforms)</p>
</blockquote>
</aside>
<p>After you applied the transform to the cube, you can use Transforms module’s sliders to change the transformation or enable “Visible in 3D view” option and translate rotate interactively in the 3D view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1438c9ded451e3da48b0021822a0f4993f11ee33.png" data-download-href="/uploads/short-url/2STdxg77YtYO1TLbMUSEWuneuNt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1438c9ded451e3da48b0021822a0f4993f11ee33_2_482x499.png" alt="image" data-base62-sha1="2STdxg77YtYO1TLbMUSEWuneuNt" width="482" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1438c9ded451e3da48b0021822a0f4993f11ee33_2_482x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1438c9ded451e3da48b0021822a0f4993f11ee33_2_723x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1438c9ded451e3da48b0021822a0f4993f11ee33_2_964x998.png 2x" data-dominant-color="F3F4F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1134×1176 61.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @sfglio (2020-02-21 14:03 UTC)

<p>Thank you for your replies!<br>
Unfortunately I still fail to extract the ROIs:</p>
<ol>
<li>Is there a difference between creating a ROI or creating a cube using the ITK Modul? Because if it is a surface mesh maybe thats the problem, as I actually only want to extract the MRI data of this specifc cube (=ROI)</li>
<li>After I have positioned my cube using the the transforms tool:<br>
I have to convert it afterwards? reference vol=my MRI data, output displacement field=new transform as?-&gt;Apply?<br>
3)From the data modul I should then be able to export this transformed cube as dicom, which is not working for me at all</li>
</ol>
<p>I am looking for an option where I can create a <strong>mask</strong> of the MRI file (like in FSL), create my ROI in this mask and save this mask with the original MRI dimension and including my ROI (like a binary mask). Later it would be great to just extract the MRI data within this cube.<br>
I further want to place multiple ROIs in one mask and calculate distances (distance transformation) and apply a transformation matrix on this mask?<br>
Is there a chance to solve this in slicer?</p>
<p>kind regards<br>
florian</p>

---

## Post #7 by @lassoan (2020-02-21 14:45 UTC)

<aside class="quote no-group" data-username="sfglio" data-post="6" data-topic="9945">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sfglio/48/3346_2.png" class="avatar"> sfglio:</div>
<blockquote>
<p>I am looking for an option where I can create a <strong>mask</strong> of the MRI file (like in FSL), create my ROI in this mask and save this mask with the original MRI dimension and including my ROI (like a binary mask). Later it would be great to just extract the MRI data within this cube.</p>
</blockquote>
</aside>
<p>You can import a model of the right shape and size into segmentation node, then export it as labelmap, using the MRI file as reference volume. You can blank out areas outside the segment using Mask Volume effect.</p>
<aside class="quote no-group" data-username="sfglio" data-post="6" data-topic="9945">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sfglio/48/3346_2.png" class="avatar"> sfglio:</div>
<blockquote>
<p>I further want to place multiple ROIs in one mask and calculate distances (distance transformation) and apply a transformation matrix on this mask?</p>
</blockquote>
</aside>
<p>If you want to do this to register segments then you can do this directly using Segment Registration extension. It computes the distance maps, registers them, and returns the resulting transform (linear or deformable). If you want to do this to compute Hausdorff distance or other error statistics then you can use Segment Comparison module.</p>

---

## Post #8 by @sfglio (2020-02-23 16:27 UTC)

<p>Thank you for your great efforts you put in the slicer project!!</p>
<p>That was exactly what I was looking for!</p>
<p>I have tried out different settings (knowing that the original voxel dimensions of the MRI matters in this context)</p>
<ul>
<li>simply exporting the label map provides the best results (i.e. nearest design of a cube with only minor edges and overhangs)</li>
<li>mask volume effect: much more edges and overhangs</li>
<li>model to labelmap node (which I thought could even fasten the process) does not improve segmentation whether standard setting of 1.0 or lower of 0.1 is used and is not as good as the first method<br>
main problem with this node: despite the fact that the cube is transformed, it always uses the original centered version?</li>
</ul>
<p>Do you have any recommendations how I could improve segmentation in order to get an almost perfect cube with only minor deviations along its faces/sides?</p>

---

## Post #9 by @sfglio (2020-03-01 15:27 UTC)

<p>Are there any recommendations for obtaining best results when segmenting MRI data?<br>
the segmented cube has so many edges even though I rescaled the volume using bspline:<br>
the original voxels are: 0.7, 0.7, 0.8<br>
So I thought rescaling to 0.8, 0.8, 0.8 using bspline would help but it does not.<br>
I do not understand why segmentations ob a cube results in so many edges (figure 2)?<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a18b10a3533790a1d11d49cbc9a509af342d085.png" alt="Bildschirmfoto 2020-03-01 um 16.23.21" data-base62-sha1="cR1SaLo95KxbxPbBzXUxu1zu8hD" width="418" height="430"> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4170e2791891cc74913160279a6ea6b0486e7f.png" data-download-href="/uploads/short-url/fSdcLaRwlpSw3QJVCSlTeLQyno3.png?dl=1" title="Bildschirmfoto 2020-03-01 um 16.22.31" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4170e2791891cc74913160279a6ea6b0486e7f.png" alt="Bildschirmfoto 2020-03-01 um 16.22.31" data-base62-sha1="fSdcLaRwlpSw3QJVCSlTeLQyno3" width="496" height="499" data-dominant-color="0A0005"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2020-03-01 um 16.22.31</span><span class="informations">584×588 207 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Is the resolution of the MRI still to low to obtain a more detailed cube (as depicted in the figure 1)</p>

---

## Post #10 by @lassoan (2020-03-01 20:04 UTC)

<p>How large is the cube? To get smooth edges, you need to have at least 50-100 voxels along the edge of the cube.</p>

---

## Post #11 by @sfglio (2020-03-01 20:12 UTC)

<p>the cube I tested is 10mm x 10mm x 10mm, however I tend to use one of 15mm x 10mm x 5mm for my study</p>
<p>btw: I tried oversampling the label map (specify geometry) and resampling the mri volume to 0.1 bspline and both not really improved the final labelmap</p>

---

## Post #12 by @lassoan (2020-03-01 20:33 UTC)

<aside class="quote no-group" data-username="sfglio" data-post="11" data-topic="9945">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sfglio/48/3346_2.png" class="avatar"> sfglio:</div>
<blockquote>
<p>the cube I tested is 10mm x 10mm x 10mm, however I tend to use one of 15mm x 10mm x 5mm for my study</p>
</blockquote>
</aside>
<p>This is expected then. Your whole volume was about 12x12x12 voxels. If you resample the input volume (not the exported labelmap) <em>before</em> you start segmentation to make voxel size about 0.1mm then edges of the cube will be smooth.</p>

---
