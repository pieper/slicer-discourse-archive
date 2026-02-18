# Help with landmark registration/Fiducial registration

**Topic ID**: 20684
**Date**: 2021-11-18
**URL**: https://discourse.slicer.org/t/help-with-landmark-registration-fiducial-registration/20684

---

## Post #1 by @MachadoL (2021-11-18 13:25 UTC)

<p>Hello, friends. I am trying to perform a rigid alignment between a 2D gray-scale Image  and a LABEL image, or a segmentation image.</p>
<p>I set up both moving and fixed fiducials (as in the picture), define saving transform, and apply.<br>
Try to go on Data module and apply the transform generated, but NOTHING HAPPENS. What am I missing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cc98708edb29606d7cd45d276616e1b36a19a99.jpeg" data-download-href="/uploads/short-url/fwnkV889aQJJi9nFysJOrfdPZDr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6cc98708edb29606d7cd45d276616e1b36a19a99_2_689x353.jpeg" alt="image" data-base62-sha1="fwnkV889aQJJi9nFysJOrfdPZDr" width="689" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6cc98708edb29606d7cd45d276616e1b36a19a99_2_689x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6cc98708edb29606d7cd45d276616e1b36a19a99_2_1033x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cc98708edb29606d7cd45d276616e1b36a19a99.jpeg 2x" data-dominant-color="A7AFA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1195×613 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Any help is welcomed.<br>
Thanks.</p>

---

## Post #2 by @lassoan (2021-11-18 13:58 UTC)

<p>Which registration module do you use?<br>
Have you clicked on Apply?<br>
Do you see any errors or warnings in the application log?</p>

---

## Post #3 by @MachadoL (2021-11-18 14:32 UTC)

<p>Hello, <span class="mention">@lasso</span>.</p>
<p>I am using <strong>Fiducial Registration Module</strong>.<br>
I clicked on apply and I found no errors warning or message.</p>
<p>I was wondering… how do the program knows that the first pair of fiducuials are attached to gray-level image and that the other pair is attached to the label image?<br>
Just by placing the fiducial over them (image and label respectively)?</p>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2021-11-18 14:38 UTC)

<aside class="quote no-group" data-username="MachadoL" data-post="3" data-topic="20684">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/machadol/48/3372_2.png" class="avatar"> MachadoL:</div>
<blockquote>
<p>how do the program knows that the first pair of fiducuials are attached to gray-level image and that the other pair is attached to the label image?</p>
</blockquote>
</aside>
<p>There is no need to know if the point positions are associated with anything. Landmark registration just computes a transform that aligns the two point sets.</p>
<p>Can you check the “Save transform_1” transform values in Transforms module? Is that an identity matrix (1.0 in the diagonal and all other values 0.0)?</p>
<p>Could you save the scene as a .mrb file, upload it somewhere and post the link here? (make sure no patient information is included, you can use any image that you find on the web)</p>

---

## Post #5 by @MachadoL (2021-11-18 15:02 UTC)

<p>All right. I got it.<br>
It was a problem of defining correctly the fiducials. Rigid registration demands at least 3 fiducials (for both fix. and mov. I guess). The other thing was defining fiducials groups. Clicking in the fiducial icon (3 red stars) creates a list, then I had to add the individual ones by clicking in the up arrow icon.</p>
<p><strong>One last question remain</strong>. Will the algorithm try to match the _1 fiducial of the moving image with the _1 fiducial of the fixed image? (if its true fiducials should be placed in a specific orther.) Or it does not really matter?</p>

---

## Post #6 by @lassoan (2021-11-18 15:31 UTC)

<aside class="quote no-group" data-username="MachadoL" data-post="5" data-topic="20684">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/machadol/48/3372_2.png" class="avatar"> MachadoL:</div>
<blockquote>
<p>Will the algorithm try to match the _1 fiducial of the moving image with the _1 fiducial of the fixed image? (if its true fiducials should be placed in a specific orther.) Or it does not really matter?</p>
</blockquote>
</aside>
<p>Yes, and this is very important: “Fiducial Registration” module requires point orders to match (N-th moving fiducial will be matched to N-th fixed fiducial.</p>
<p>“Fiducial registration” module is very basic, if you need automatic point matching (so that order and number of fiducials in the fixed and moving list do not have to match exactly) or you want to do warping transform, or just want to have a more convenient user interface, then I would recommend to use the “Fiducial registration wizard” module in SlicerIGT extension.</p>

---

## Post #7 by @MachadoL (2021-11-18 18:08 UTC)

<p>“Fiducial registration wizard” module in SlicerIGT extension just worked like magic.<br>
Such a perfect solution.</p>
<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---

## Post #8 by @MachadoL (2021-11-19 19:36 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, just a continuation of this thread.</p>
<p>I had a <strong>2D image</strong> with a segmentation (<strong>.seg.nrrd</strong>) misaligned. I used the fiducial registration wizards, find the right transform, <strong>harden the transform and overwrite the .seg.nrrd file</strong>.</p>
<p>In the next stage, I load both <strong>image and .seg.nrrd</strong> into <strong>python notebook</strong> and use the <strong>nrrd package</strong> to manipulate the label in the segmentation. I then plot the image with the overlaid segmentation. Its a fast visual check in my application.</p>
<p>There is the problem. The resulting plot (with matplotlib) is misaligned as the previous stage. Take a look on the images:</p>
<p><strong>In 3Dslicer</strong>, after alignment, saved, and reopened:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9be1a8331e02913d5cf1186f0d6057a19f832e9.png" data-download-href="/uploads/short-url/sMHgwGJP9aJ6yxtp0bGBk4vilG9.png?dl=1" title="Corrected" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9be1a8331e02913d5cf1186f0d6057a19f832e9_2_690x336.png" alt="Corrected" data-base62-sha1="sMHgwGJP9aJ6yxtp0bGBk4vilG9" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9be1a8331e02913d5cf1186f0d6057a19f832e9_2_690x336.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9be1a8331e02913d5cf1186f0d6057a19f832e9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9be1a8331e02913d5cf1186f0d6057a19f832e9.png 2x" data-dominant-color="70785A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Corrected</span><span class="informations">893×436 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>In matplotlib</strong> output:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3f355d4082907bb2a9288005f09c36614ac93d6.png" data-download-href="/uploads/short-url/uf05yGDIn2nbPm1eSAEpSwT4iCa.png?dl=1" title="Persistente" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3f355d4082907bb2a9288005f09c36614ac93d6_2_690x344.png" alt="Persistente" data-base62-sha1="uf05yGDIn2nbPm1eSAEpSwT4iCa" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3f355d4082907bb2a9288005f09c36614ac93d6_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3f355d4082907bb2a9288005f09c36614ac93d6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3f355d4082907bb2a9288005f09c36614ac93d6.png 2x" data-dominant-color="515882"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Persistente</span><span class="informations">809×404 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is strange, it is like the .seg.nrrd file just did not change any geometric info.<br>
Any helpe, please?</p>

---

## Post #9 by @mikebind (2021-11-19 20:29 UTC)

<p>I wonder if the problem is that matplotlib is aligning the images by their dimensions (i.e. by aligning a corner of the images) rather than by spatial information associated with them. This would be a normal approach for a system unused to dealing with images which need to be located in space. The Slicer registration and transform hardening modified only header information, not the pixel grid. If matplotlib is aligning based on the pixel grid, then it will look like the registration had no effect.</p>

---

## Post #10 by @MachadoL (2021-11-19 20:52 UTC)

<p>I have a feeling that, Matplotlib itself is not the issue. Take a look on the code I use to convert .seg.nrrd to array image:</p>
<pre><code class="lang-auto">import slicerio as sio
import nrrd

    segmentation_info = sio.read_segmentation_info(input_filename)
    segment_names = sio.segment_names(segmentation_info)
    number_of_segments = len(segmentation_info["segments"])

    # Extracting structure 1:
    segment_names_to_labels = [("Segment_1",1)]
    voxels, header = nrrd.read(input_filename)
    segment_1, extracted_header = sio.extract_segments(voxels, header, segmentation_info, 
    segment_names_to_labels)
</code></pre>
<p>At the end, <strong>segment_1</strong> should contain both spacial and grid info converted into array, shouldn’t it?</p>
<p>Maybe, I would need an interpolation itself, so that the grids would hold new values produced by the transformation. I’m not sure it makes sense, but…</p>

---

## Post #11 by @mikebind (2021-11-19 21:22 UTC)

<p>Perhaps I’m being unclear.  Here is a better description of what I imagine may be happening:</p>
<p>Initial State:<br>
Original Image is, for example, 100 pixels x 100 pixels with an origin at (0,0)<br>
Original Labelmap/Segmentation is also 100 pixels x 100 pixels and has an origin at (0,0)</p>
<p>However, the original labelmap is not aligned with the original image, so you perform fiducial registration and the resulting transform translates points up 10 mm and to the right 10 mm.  You apply this transform to the original Segmentation/Labelmap and harden the transform.  The modified Segmentation/Labelmap is still 100 pixels x 100 pixels, but it now has an origin at (10, 10) instead of at (0,0).  When you save the modified version, the only change from the original is that it has a different origin, and this information is only in the nrrd header, not in the pixel grid image.  When you extract the pixel grid from the modified version it is identical to the pixel grid from the unmodified version.  Slicer shows the modified version as shifted because it reads the header and positions the pixel grid with respect to the origin.  Matplotlib almost certainly does not do this, instead implicitly assuming that the (0,0) voxel of one image should be lined up with the (0,0) voxel of the other. The positioning information necessary to line up the image and the segment is contained in the header and is not accessible to matplotlib, which is only given the pixel grid.</p>
<p>So, I think what you likely need is a version of the registered segmentation/labelmap which has been resampled into the same grid as the original image.  Try the following:</p>
<p>From the Segmentations module, select your segmentation (with the transform already hardened) and go down to the section titled Export/import models and labelmaps</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/864f969d3e95710a975e3b6eb6c85ea36a1963b4.png" alt="image" data-base62-sha1="jaauTkC8lFzyjA3umWuyhumBYoY" width="510" height="300"></p>
<p>and select “Export”, “Labelmap”, and open up the “Advanced” section.  For “Reference volume”, select your original image.  Then click “Export”.</p>
<p>Save the exported labelmap and try overlaying that in matplotlib with your original image.  If that works, then what I’ve laid out above is probably the correct diagnosis of the problem.</p>

---
