# Plane-Cut on segment's labelmap

**Topic ID**: 45737
**Date**: 2026-01-11
**URL**: https://discourse.slicer.org/t/plane-cut-on-segments-labelmap/45737

---

## Post #1 by @shanfl (2026-01-11 02:36 UTC)

<p>I need to plane-cut a labelmap of a segment with a vtkplanewidget, but the cutting position is not correct.I think there might be an issue with the conversion from voxel ijk coordinates to RAS coordinates, but I can’t pinpoint the cause.</p>
<p>here is code</p>
<pre><code class="lang-auto">std::vector&lt;vtkSmartPointer&lt;vtkOrientedImageData&gt;&gt; PlaneCutImage(vtkOrientedImageData* image, double planeOrigin_World[3], double planeNormal_World[3])
{
	Q_D(qSlicerSurgeryPlanPlaneCutEffect);
	if (!image) {
		return {};
	}

	qDebug() &lt;&lt; "planeOrigin:" &lt;&lt; planeOrigin_World[0] &lt;&lt; " " &lt;&lt; planeOrigin_World[1] &lt;&lt; " " &lt;&lt; planeOrigin_World[2];
	qDebug() &lt;&lt; "planeNormal:" &lt;&lt; planeNormal_World[0] &lt;&lt; " " &lt;&lt; planeNormal_World[1] &lt;&lt; " " &lt;&lt; planeNormal_World[2];


	// ijk 2 ras
	vtkNew&lt;vtkTransform&gt; ijkToWorldTransform;
	vtkNew&lt;vtkMatrix4x4&gt; ijkToWorldMatrix;
	image-&gt;GetImageToWorldMatrix(ijkToWorldMatrix);
	ijkToWorldTransform-&gt;SetMatrix(ijkToWorldMatrix);

	PrintMatrixFormatted(ijkToWorldMatrix);



	//
	int dims[3];
	double spacing[3], origin[3];
	image-&gt;GetDimensions(dims);
	image-&gt;GetSpacing(spacing);
	image-&gt;GetOrigin(origin);

	// 
	if (dims[0] &lt;= 0 || dims[1] &lt;= 0 || dims[2] &lt;= 0) {
		return {};
	}



	// 
	int extent[6] = { 0, dims[0] - 1, 0, dims[1] - 1, 0, dims[2] - 1 };
	void* wholeInputPtr = image-&gt;GetScalarPointerForExtent(extent);
	if (!wholeInputPtr) {
		wholeInputPtr = image-&gt;GetScalarPointer();
		if (!wholeInputPtr) {
			return {};
		}
	}

	int scalarType = image-&gt;GetScalarType();
	int numComponents = image-&gt;GetNumberOfScalarComponents();
	size_t scalarSize = image-&gt;GetScalarSize();

	if (scalarSize == 0) {
		return {};
	}

	size_t voxelSize = scalarSize * numComponents;

	std::vector&lt;vtkSmartPointer&lt;vtkOrientedImageData&gt;&gt; ret;

	// 
	vtkNew&lt;vtkOrientedImageData&gt; part1;
	vtkNew&lt;vtkOrientedImageData&gt; part2;
	part1-&gt;DeepCopy(image);
	part2-&gt;DeepCopy(image);



	// 
	part1-&gt;AllocateScalars(scalarType, numComponents);
	part2-&gt;AllocateScalars(scalarType, numComponents);

	//
	void* wholePart1Ptr = part1-&gt;GetScalarPointerForExtent(extent);
	void* wholePart2Ptr = part2-&gt;GetScalarPointerForExtent(extent);

	if (!wholePart1Ptr || !wholePart2Ptr) {
		wholePart1Ptr = part1-&gt;GetScalarPointer();
		wholePart2Ptr = part2-&gt;GetScalarPointer();

		if (!wholePart1Ptr || !wholePart2Ptr) {
			return {};
		}
	}


	vtkIdType totalBytes = static_cast&lt;vtkIdType&gt;(dims[0]) * dims[1] * dims[2] * voxelSize;
	memset(wholePart1Ptr, 0, totalBytes);
	memset(wholePart2Ptr, 0, totalBytes);

	bool sideWrite[2] = { false, false };

	// handle every voxel
	for (int z = 0; z &lt; dims[2]; ++z) {
		for (int y = 0; y &lt; dims[1]; ++y) {
			for (int x = 0; x &lt; dims[0]; ++x) {

				//
				double ijkCenter[3] = { x + 0.5 ,y + 0.5 , z + 0.5 };
				double rasCenter[3];
				ijkToWorldTransform-&gt;TransformPoint(ijkCenter, rasCenter);

				if ((y == 0) &amp;&amp; (z == 0) &amp;&amp; (x == 0)) {
					qDebug() &lt;&lt; "IJK (0,0,0) -&gt; RAS:" &lt;&lt; rasCenter[0] &lt;&lt; rasCenter[1] &lt;&lt; rasCenter[2];
				}



				double vector[3] = {
					rasCenter[0] - planeOrigin_World[0],
					rasCenter[1] - planeOrigin_World[1],
					rasCenter[2] - planeOrigin_World[2]
				};

				double dotProduct =
					vector[0] * planeNormal_World[0] +
					vector[1] * planeNormal_World[1] +
					vector[2] * planeNormal_World[2];


				// 
				size_t offset = (z * dims[1] * dims[0] + y * dims[0] + x) * voxelSize;

				void* inputPtr = static_cast&lt;char*&gt;(wholeInputPtr) + offset;
				void* part1Ptr = static_cast&lt;char*&gt;(wholePart1Ptr) + offset;
				void* part2Ptr = static_cast&lt;char*&gt;(wholePart2Ptr) + offset;

				if (dotProduct &gt;= 0) {
					sideWrite[0] = true;
					memcpy(part1Ptr, inputPtr, voxelSize);
					
				}
				else {
					sideWrite[1] = true;
					memcpy(part2Ptr, inputPtr, voxelSize);
					
				}
			}
		}
	}

	
	part1-&gt;SetImageToWorldMatrix(ijkToWorldMatrix);
	part2-&gt;SetImageToWorldMatrix(ijkToWorldMatrix);

	//
	if (sideWrite[0]) {
		ret.emplace_back(part1);

		WriteNII("D:/part1.nii.gz", part1);
	}
	if (sideWrite[1]) {
		ret.emplace_back(part2);
		WriteNII("D:/part2.nii.gz", part2);
	}

	return ret;
}
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/998838dc79344ceec372a1327129e1b95ce926f5.png" data-download-href="/uploads/short-url/lUcUgtAdNJYHkXFbGTvzPcygNIF.png?dl=1" title="2026-01-09_214810" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/998838dc79344ceec372a1327129e1b95ce926f5_2_690x376.png" alt="2026-01-09_214810" data-base62-sha1="lUcUgtAdNJYHkXFbGTvzPcygNIF" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/998838dc79344ceec372a1327129e1b95ce926f5_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/998838dc79344ceec372a1327129e1b95ce926f5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/998838dc79344ceec372a1327129e1b95ce926f5.png 2x" data-dominant-color="DFD2C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2026-01-09_214810</span><span class="informations">722×394 61.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bf495f88ef29fafca2d0eff7c04161a67020586.png" data-download-href="/uploads/short-url/fp16WIr4xPuq9aAjwFWvJ5CIVDg.png?dl=1" title="2026-01-09_214856" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bf495f88ef29fafca2d0eff7c04161a67020586_2_690x376.png" alt="2026-01-09_214856" data-base62-sha1="fp16WIr4xPuq9aAjwFWvJ5CIVDg" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bf495f88ef29fafca2d0eff7c04161a67020586_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bf495f88ef29fafca2d0eff7c04161a67020586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bf495f88ef29fafca2d0eff7c04161a67020586.png 2x" data-dominant-color="C6C3BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2026-01-09_214856</span><span class="informations">719×392 42.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2026-01-11 22:39 UTC)

<p>VTK just provides basic visualization and processing infrastructure. There are many limitations and lots of features are missing. VTK widgets are a particularly weak (maybe the worst) part of VTK that we had to reimplement in Slicer/MRML almost from scratch. Image orientation is still not fully taken into account everywhere in VTK, so we manage IJK to RAS matrix outside VTK filters.</p>
<p>I would recommend to step up one level if you work with medical images - use VTK via MRML library or Slicer application instead of just raw VTK.</p>

---
