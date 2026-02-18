# Extract RAS coordinates from reformated slice

**Topic ID**: 29596
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/extract-ras-coordinates-from-reformated-slice/29596

---

## Post #1 by @bserrano (2023-05-23 08:58 UTC)

<p>Hi all,</p>
<p>I want to extract RAS coordinates from a reformated slice.</p>
<p>I built a cilinder with an offset on the axial view, so I create the segment you can see in the figure below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17599d7e7d2a516142a22589940b513a82c90b0f.png" data-download-href="/uploads/short-url/3kyYQYUqvge5bAPAb9bROjpfULl.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17599d7e7d2a516142a22589940b513a82c90b0f_2_690x414.png" alt="imagen" data-base62-sha1="3kyYQYUqvge5bAPAb9bROjpfULl" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17599d7e7d2a516142a22589940b513a82c90b0f_2_690x414.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17599d7e7d2a516142a22589940b513a82c90b0f_2_1035x621.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17599d7e7d2a516142a22589940b513a82c90b0f_2_1380x828.png 2x" data-dominant-color="232225"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1921×1153 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>With Extract Centerline module I generate the centerline and get the perpendicular plane we can see in the red slice. It would be very useful if I can get at a time all RAS coordinates from the whole slice and their pixel values, how can I do that?</p>
<p>Thanks ^^</p>

---

## Post #2 by @lassoan (2023-05-23 22:29 UTC)

<p>Each voxel have a different RAS coordinates. There should be no need to extract each. Any pixel-by-pixel processing would be unbearably slow.</p>
<p>You can get voxel values by using vtkImageReslice filter. Each slice view already has a reslice filter, so you may just use that instead of setting one up yourself.</p>
<p>What is your overall goal?</p>

---

## Post #3 by @bserrano (2023-05-26 07:07 UTC)

<p>Our goal is to segment a structure using perpendicular planes.</p>
<p>Imaging we have the cilinder in the post above. The axial planes correspond with the elipses, but we only know how to segment in the perpendicular view (circles).</p>
<p>The workflow is:</p>
<pre><code class="lang-auto">1. Load volume
2. Make a rough segmentation of the cilinder and generate a centerline
3. Obtain perpendicular planes in each point of the centerline (in a real case we have different orientations, the cilinder can be a vessel, for example)
4. Export the reformat slices as images 
5. Segment the images and obtain binary masks (outside Slicer)
6. Use this masks to rebuild the segment volume (cilinder) in Slicer.
</code></pre>
<p>We are having some issues with steps 4, since we do not know the optimal way to obtain voxel values of one slice in an optimal way,  and 6, since we need to know pixel coordinates of the perpendicular view to paint the original volume (in slicer) using the generated masks in step 4.</p>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2023-05-26 11:44 UTC)

<p>You’ll see that Slicer is pretty amazing. All the steps that you need to do are already implemented and it is all very fast and accurate.</p>
<ul>
<li>Step 2 is implemented in <code>Extract centerline</code> module in <code>VMTK</code> extension.</li>
<li>Step 3-4 és <a href="https://youtu.be/WJQexDTiRRc">called curved planar reformatting</a> and it is implemented in <a href="https://github.com/PerkLab/SlicerSandbox#curved-planar-reformat"><code>Curved Planar Reformat</code> module</a> in <code>Sandbox</code> extension. You just specify the image, centerline, resolution, slice size and the module provides you all the reformatted slices in a 3D array ('Straightened volume<code>). It is all very accurate and efficient. Moreover, it also provides the </code>Straightening transform`, which can translate any 3D object (image, segmentation, centerline, landmark points, etc.) between the original image space and the straightened space.</li>
<li>You can save the 3D volume, process it slice by slice (segment the vessel lumen, segment/characterize plaque, etc) and then save the result in a 3D volume that had the same geometry (origin, spacing, axis directions) as the input volume.</li>
<li>Step 6 - volume reconstruction is implemented in Slicer, too. If the centerline resolution and slice size is chosen that slices do not intersect then you can reconstruct the segmentation by simply inverting the straightening transform, apply it to the straightened image segmentation, and harden the transform (each of these steps are just a <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#use-cases">few clicks</a>). In case your centerline is highly curved or you need very high resolution along the centerline then the extracted slices may intersect each other. In this case, you can use use <code>Volume Reconstruction</code> module in SlicerIGT extension, as this module can reconstruct volumes from <a href="https://discourse.slicer.org/t/ultrasound-3d-reconstruction/22952">arbitrarily moving, intersecting slices</a>. The input of this module is a time series of properly positioned and oriented slices, so if you want to use this module then you need to copy each oriented slice into a volume sequence.</li>
</ul>

---

## Post #5 by @bserrano (2023-05-29 06:47 UTC)

<p>That’s exactly what we needed! Slicer continues surprising us <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @bserrano (2023-05-30 12:19 UTC)

<p>Hi Andras, we are very pleasent with the results of the straightening module, but now we want to use it to straight our own segmentations and mask  over it, and we found some issues. Our process is basically:</p>
<ol>
<li>
<p>Upload the segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ae6dbf962f9cc4e9b8a9b132f87669eb2c606dc.png" data-download-href="/uploads/short-url/jOMvhOMICGpGvd2uMGbCvIn3MTO.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ae6dbf962f9cc4e9b8a9b132f87669eb2c606dc_2_178x375.png" alt="imagen" data-base62-sha1="jOMvhOMICGpGvd2uMGbCvIn3MTO" width="178" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ae6dbf962f9cc4e9b8a9b132f87669eb2c606dc_2_178x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ae6dbf962f9cc4e9b8a9b132f87669eb2c606dc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ae6dbf962f9cc4e9b8a9b132f87669eb2c606dc.png 2x" data-dominant-color="32364B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">262×549 44.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>Extract centerlines.</p>
</li>
<li>
<p>Use Curved Planar Reformat to straight the volumen around the centerline.</p>
</li>
<li>
<p>Use straightening Transform to straight the segmentation. We straight all the segmentation but we are interested only in a specific region (Around the straight Volume we made before).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4f40b7ff1d79602c3cd135419467be472deb620.png" alt="imagen" data-base62-sha1="wFpJ4WVfJDCyrsTxcGHvlg1Y0BW" width="91" height="386"></p>
</li>
<li>
<p>Create a mask from the straightened segmentation we made.</p>
</li>
<li>
<p>Use this mask for our porpouses (out of Slicer).</p>
</li>
</ol>
<p>The problem arises when we try to generate the mask, because it’s not well made. To do this mask we use two methods:</p>
<ol>
<li>
<p>Mask Volume tool: If we use the Mask Volume on our straight segment, the tool generates a non-accurate mask.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c71d7aa146528ef016265cf9bfe19f207d4b267e.png" data-download-href="/uploads/short-url/spsaRdIKFr2uJwlXIjpM6KH0pUq.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c71d7aa146528ef016265cf9bfe19f207d4b267e_2_674x500.png" alt="imagen" data-base62-sha1="spsaRdIKFr2uJwlXIjpM6KH0pUq" width="674" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c71d7aa146528ef016265cf9bfe19f207d4b267e_2_674x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c71d7aa146528ef016265cf9bfe19f207d4b267e_2_1011x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c71d7aa146528ef016265cf9bfe19f207d4b267e_2_1348x1000.png 2x" data-dominant-color="191A1A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1428×1059 61.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>LabelMap: In the Data module we can make a binary labelmap from the straightened segmentation. The results here are pretty good (see image below), but the problem is the fact that the segment its bigger than the straight volume. To reduce the labelmap to the straight volume, we use the Crop Volume module, but the interpolation made on the ROI gets a worse mask, losing information and making it a non valid way to masking.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a17e7ad8ca9e98717ce0e26c1c7d0ebc0cd362.png" data-download-href="/uploads/short-url/gm4qJ0rTjROZpxNkvSbtzqH8uiu.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a17e7ad8ca9e98717ce0e26c1c7d0ebc0cd362.png" alt="imagen" data-base62-sha1="gm4qJ0rTjROZpxNkvSbtzqH8uiu" width="149" height="500" data-dominant-color="1E291E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">307×1025 4.15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ol>
<p>If any of the steps are not enough clear, please tell us.</p>
<p>Thanks ^^</p>

---

## Post #7 by @lassoan (2023-05-30 19:53 UTC)

<p>You can increase the image resolution if you find that the interpolation artifacts are non-negligible. For example, you can set <code>Spacing scale</code> to 0.5 or 0.25 in <code>Crop volume</code> module.</p>

---

## Post #8 by @bserrano (2023-06-01 10:02 UTC)

<p>Hi Andras, with those methods related on the previous comment we didn´t achieve any results… If we focus on the first one:</p>
<ol>
<li>When we straight the volume around one centerline, we also use the straightening transform to straight the model of the segmentation that we have.</li>
<li>In this procedure, the model becomes straight over the centerline and the rest is usually distorted.</li>
<li>Then, we use this model to create a new segmentation (if we don’t do this proccess segmentation → model → segmentation, the results are even worse). In this segmentation we obtain the volume using the tool Mask Volume from Segment Editor module.</li>
<li>The mask is used out of slicer.</li>
</ol>
<p>With this method, which we consider is more solid and useful, we found some technical issues:</p>
<p>•	The quality of the segmentation made from the model is poor (see image below) on critical zones.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86f7d129af5019eca3aad83875757f3d0d1faffc.jpeg" data-download-href="/uploads/short-url/jfYVrRPjfYbS9uLlenAxz4zFDju.jpeg?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86f7d129af5019eca3aad83875757f3d0d1faffc_2_376x499.jpeg" alt="imagen" data-base62-sha1="jfYVrRPjfYbS9uLlenAxz4zFDju" width="376" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86f7d129af5019eca3aad83875757f3d0d1faffc_2_376x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86f7d129af5019eca3aad83875757f3d0d1faffc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86f7d129af5019eca3aad83875757f3d0d1faffc.jpeg 2x" data-dominant-color="494566"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">517×686 63.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<em>Blue: straighten model<br>
Pink: straighten segment obtained by converting the model to a segment</em></p>
<p>Although this zone is bad reconstructed, the “easy” zones are well reconstructed (see image below). However, we need to be very precise in all the segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/013030e0cfecfec50d1e9bb35697fa9ac9dd9fd9.jpeg" data-download-href="/uploads/short-url/avJ0Z2wH7OEtT0z70Axa5e266t.jpeg?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/013030e0cfecfec50d1e9bb35697fa9ac9dd9fd9_2_384x500.jpeg" alt="imagen" data-base62-sha1="avJ0Z2wH7OEtT0z70Axa5e266t" width="384" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/013030e0cfecfec50d1e9bb35697fa9ac9dd9fd9_2_384x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/013030e0cfecfec50d1e9bb35697fa9ac9dd9fd9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/013030e0cfecfec50d1e9bb35697fa9ac9dd9fd9.jpeg 2x" data-dominant-color="4A4164"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">533×693 64.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<em>Blue: straighten model<br>
Pink: straighten segment obtained by converting the model to a segment</em></p>
<p>What we expected is that all pixel inside the blue model would be part of the pink segmentation, but it is not the case.</p>
<p>•	Also, we want to know if is possible, starting from a segmentation we have, select only the part that corresponds to a specific centerline and work with this cut-out instead with the original segmentation.</p>
<p>Finally, one more question:  Slicer is awesome when it works with geometries ([x,y,z] world), because we can clearly straight a geometry and nothing bad happens, but is slicer able to, given a volume (made of mask images), come through the transform an recover the original segmentation with enough quality?<br>
We lose information becoming from the model to the segmentation.</p>
<p>That´s all, we hope the procedure is clearly enough.</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> .</p>

---
