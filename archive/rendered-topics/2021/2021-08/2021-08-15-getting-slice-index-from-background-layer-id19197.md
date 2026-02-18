# Getting slice index from background layer

**Topic ID**: 19197
**Date**: 2021-08-15
**URL**: https://discourse.slicer.org/t/getting-slice-index-from-background-layer/19197

---

## Post #1 by @sogo (2021-08-15 03:37 UTC)

<p>Hi,<br>
We want to use this code to get the slice number/index (found it on script repository but now the code is gone and we are unable to refer back to it as script repository documentation is updated) and wanted to confirm few things:</p>
<pre><code class="lang-auto">if (d-&gt;sliceLogic != nullptr) {
		vtkMRMLSliceLayerLogic* BL = d-&gt;sliceLogic-&gt;GetBackgroundLayer();
		vtkGeneralTransform* xyToIJK = BL-&gt;GetXYToIJKTransform();
		const float inCoord[3] = { 0,0,0 };
		float outCoord[3] = { 0,0,0 };
		xyToIJK-&gt;InternalTransformPoint(inCoord, outCoord);
		k = outCoord[c];
	}
	return k;
</code></pre>
<ol>
<li>What is the inCoord for, as per my understanding, is it defining the origin of 3D volume?</li>
<li>Does the k, which is the z-axis always corresponds to Axial view?</li>
<li>We are storing ‘k’ as int type but the coordinate is float type. Should we round the outCoord to nearest integer before storing into ‘k’? because the way it is right now, it will always floor.</li>
</ol>
<p>Regards<br>
SI</p>

---

## Post #2 by @lassoan (2021-08-16 05:10 UTC)

<p>DICOM does not allow any kind of indexing based on slice position, so no geometric conversion exists between physical coordinates to “slice index”.</p>
<p>The number that you see in 2D DICOM viewers when you browse the images is the <a href="http://dicomlookup.com/lookup.asp?sw=Tnumber&amp;q=(0020,0013)">Instance number</a>, which is usually assigned to image slices based on where the image slice is located and/or when it was acquired. It is usually offset by one compared to the third voxel coordinate value (as instance numbers are typically 1-based, while voxel coordinates are 0-based) and often also inverted (as voxel coordinate increases, instance number can increase or decrease), and sometimes (e.g., when not all originally frames are available) then the offset may change throughout the series. Since a slice view is not always aligned with the original image slices (reformatted in orthogonal or oblique orientations), the instance number also often changes within a slice (different regions of the displayed image is reconstructed from different original slices).</p>
<p>Therefore, the only reliable way to get the instance number for a physical point position is the following:</p>
<ul>
<li>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-fiducial-ras-coordinates">get the IJK coordinates</a> of the volume at the position of interest</li>
<li>get the SOP instance UID for the K-th slice in the volume - this UID is <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-tag-of-a-volume-loaded-from-dicom-for-example-get-the-patient-position-stored-in-a-volume">stored in the <code>DICOM.instanceUIDs</code> attribute</a>
</li>
<li>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-top-level-tags-of-dicom-images-imported-into-slicer">get the instance number from the DICOM database for that UID</a> for the K-th slice of the volume</li>
</ul>
<p>Implementation in Python (after the IJK coordinates are computed):</p>
<pre><code class="lang-python">ijk = [12, 34, 56]
volumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLVolumeNode')
instanceUID = volumeNode.GetAttribute('DICOM.instanceUIDs').split(' ')[ijk[2]]
instanceNumber = slicer.dicomDatabase.instanceValue(instanceUID, '0020,0013')
print(f"Instance Number: {instanceNumber}")
</code></pre>
<p>You can add this code snippet to DataProbe.py to make the instance number show up in the Data Probe in the bottom-left of the screen. If you implement it and works well for you then send a pull request, we may consider adding it to the Slicer core, as it can be useful for cross-referencing positions with slices shown in other DICOM viewers.</p>

---

## Post #3 by @sogo (2021-08-17 02:36 UTC)

<p>Hi Andras,</p>
<p>Thanks for the detailed information. I have a follow up question:</p>
<p>For scans that we know for sure were acquired as a series of axially scanned slices each stored as DICOM file, is the code I posted valid, for determining the slice index? Basically, the math corresponding to the code I posted seems to be as follows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a86eb60a8f42ee787997e052a88d4eaf77e78a4.jpeg" data-download-href="/uploads/short-url/cUQ2e3COkw3YRQaPe4RQCHuxDxi.jpeg?dl=1" title="20210816_191803" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a86eb60a8f42ee787997e052a88d4eaf77e78a4_2_690x261.jpeg" alt="20210816_191803" data-base62-sha1="cUQ2e3COkw3YRQaPe4RQCHuxDxi" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a86eb60a8f42ee787997e052a88d4eaf77e78a4_2_690x261.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a86eb60a8f42ee787997e052a88d4eaf77e78a4_2_1035x391.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a86eb60a8f42ee787997e052a88d4eaf77e78a4_2_1380x522.jpeg 2x" data-dominant-color="BFBEBE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20210816_191803</span><span class="informations">1920×727 293 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>so it seems like the <code>a12</code> element always encodes the “slice index” is that correct?</p>

---

## Post #4 by @lassoan (2021-08-17 03:28 UTC)

<p>As I wrote above, you cannot determine the DICOM instance number from the slice number (a12) because there are several unknown factors, out of your control that influences this mapping. Even if you find that for some images, slice index + 1 =  DICOM instance number, it does not mean that will be true for other images as well. It is enough that the imaging technologist slightly adjusts an acquisition parameter and you get a slightly or completely different mapping.</p>
<p>Fortunately, there is a reliable solution that I described above.</p>

---

## Post #5 by @kpopuri (2021-08-17 05:08 UTC)

<p>Hi Andras, thanks got it about the slice number/index aka <code>K</code> NOT having a simple relation with the InstanceNumber, and hence we have to use <code>K</code> to query the DICOM database tor retrieve the InstanceNumber. But, our main question is, can we ALWAYS trust <code>a12</code> to be the same as the slice number/index aka <code>K</code>? , where <code>a12</code> is the (3, 4)th element of the transformation matrix obtained via:<br>
<code>xyToIJK = BL-&gt;GetXYToIJKTransform()</code></p>
<p>Would greatly appreciate your confirmation of this. Thanks.</p>

---

## Post #6 by @lassoan (2021-08-17 17:59 UTC)

<aside class="quote no-group" data-username="kpopuri" data-post="5" data-topic="19197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kpopuri/48/6263_2.png" class="avatar"> kpopuri:</div>
<blockquote>
<p>But, our main question is, can we ALWAYS trust <code>a12</code> to be the same as the slice number/index aka <code>K</code> ?</p>
</blockquote>
</aside>
<p>Yes, when you load an image using DICOM module using DICOMScalarVolumePlugin then third voxel coordinate value (K) is always the same as the index in the instanceUIDs list (because the same list is used to populate the instanceUIDs list that is passed to the DICOM reader).</p>

---

## Post #7 by @sogo (2021-08-17 22:39 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a>  for your support, closing this thread.</p>

---
