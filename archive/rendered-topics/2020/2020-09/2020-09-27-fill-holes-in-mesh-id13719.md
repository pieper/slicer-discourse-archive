# Fill holes in mesh

**Topic ID**: 13719
**Date**: 2020-09-27
**URL**: https://discourse.slicer.org/t/fill-holes-in-mesh/13719

---

## Post #1 by @loubna (2020-09-27 15:33 UTC)

<p>Hi;<br>
I have a 3D image (vtkImageData with holes) on which I applied Marching cubes and I get a 3d surface with small holes (see attached figure).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/005bf892cfe88406749d0ea3d5caf3cbc2aba47e.png" alt="mesh" data-base62-sha1="3b2UqyVY7cmUa4wURMXAf3dwDA" width="621" height="472"></p>
<p>To deal with this problem, I have resampled the 3D image with sampledFactor of 0.5 before applying the marching cubes</p>
<p>here is the code:</p>
<pre><code class="lang-auto">		double resampledFactor =0.5;
		
		vtkSmartPointer&lt;vtkImageReslice&gt; resampledImage =
		vtkSmartPointer&lt;vtkImageReslice&gt;::New();
		resampledImage-&gt;SetInputData(imageData);
		
		int extent[6];
		extent[0] = ext[0];
		extent[1] = ext[1] /resampledFactor;
		extent[2] = ext[2];
		extent[3] = ext[3] /resampledFactor;
		extent[4] = ext[4];
		extent[5] = ext[5] / resampledFactor;
		
		resampledImage-&gt;SetOutputSpacing(0.5,0.5,0.5);
		resampledImage-&gt;SetOutputOrigin(0,0,0);
		resampledImage-&gt;SetOutputExtent(extent);
		resampledImage-&gt;SetInterpolationModeToLinear();
		resampledImage-&gt;Update();
</code></pre>
<p>The resulted surface is enhenced but it is still contains smalll holes. My question is how can I fill in holes in vtkImageData or in mesh in order to get a closed 3D surface without holes.</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-09-27 19:27 UTC)

<p>Isosurface extracted from an unprocessed image is expected to be noisy. You can greatly improve quality by applying Gaussian smoothing, but that will also remove fine details. You can try non-linear filters, such as median or various anisotropic smoothing, which may preserve details while removing certain noise types. These filters (and many more) are available in “Simple filters” module.</p>
<p>However, most of the time you cannot extract structures by simple thresholding/isosurface extraction but you need to use various segmentation tools. You can find many of them in Segment Editor (and there are several extensions that installs provides additional ones).</p>

---

## Post #3 by @Nina (2020-09-28 10:43 UTC)

<p>-Thank you for response.</p>
<p>Im trying to create the model from the 3D coordinate points that are stored in the txt file (and not a segment). I use the Marching cubes algorithm. It looks like it´s not able to link individual points, and therefore holes are created in the model.</p>
<p>I tried  vtkImageOpenClose3D.h to close the holes but it seems do not give good results .</p>
<pre><code class="lang-cpp">        vtkSmartPointer&lt;vtkImageOpenClose3D&gt; openClose =
        vtkSmartPointer&lt;vtkImageOpenClose3D&gt;::New();
        openClose-&gt;SetInputData(imageData);
        openClose-&gt;SetOpenValue(255);
        openClose-&gt;SetCloseValue(0);
        openClose-&gt;SetKernelSize(5, 5, 5);
        //openClose-&gt;ReleaseDataFlagOff();
        openClose-&gt;GetOutput();
        openClose-&gt;GetCloseValue();
        openClose-&gt;GetOpenValue();
        openClose-&gt;Update();
</code></pre>

---

## Post #4 by @lassoan (2020-09-28 13:30 UTC)

<aside class="quote no-group" data-username="Nina" data-post="3" data-topic="13719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/e68b1a/48.png" class="avatar"> Nina:</div>
<blockquote>
<p>Im trying to create the model from the 3D coordinate points that are stored in the txt file</p>
</blockquote>
</aside>
<p>What software produces this text file?<br>
Do the coordinate correspond to a list of planar contours (coming from a DICOM RT structure set)?<br>
Or some software lists each individual voxel value of a binary labelmap (that would be extremely inefficient)?</p>

---

## Post #5 by @Nina (2020-09-30 12:57 UTC)

<p>Hi Mr;</p>
<p>I have created points from segmentation and generated surface to do some tests. I have resapmled and used vtkImageOpenClose3D. Now it works fine (all holes are filled</p>
<p>thank’s</p>

---
