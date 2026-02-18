# Questionable performance on GPU workstation

**Topic ID**: 17140
**Date**: 2021-04-16
**URL**: https://discourse.slicer.org/t/questionable-performance-on-gpu-workstation/17140

---

## Post #1 by @mluerig (2021-04-16 21:39 UTC)

<p>New user here. Basic I/O tasks like loading volumes, but also rendering models, selecting ROIs or working in the segmentation editor takes very long to complete, i.e. 10s of seconds to half a minute or more for a 1000x1000x1000px CT scan. A look into windows performance monitor suggests that 3Dslicer may not be making use of the two RTX2080Ti GPUs, but CPU only. Slicer uses the global settings (see below).</p>
<p>Are my expectations too high?</p>
<p>Other specs:<br>
i9-9900K Octacore<br>
64GB RAM<br>
OS on SSD, data on HDD</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c7230d5cbf75c5112e332fac5b90e69267f7809.png" data-download-href="/uploads/short-url/mjZ8ym5KDGoXOZq4mRFjXZa8G1z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c7230d5cbf75c5112e332fac5b90e69267f7809.png" alt="image" data-base62-sha1="mjZ8ym5KDGoXOZq4mRFjXZa8G1z" width="434" height="499" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">759×873 38.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2021-04-16 21:50 UTC)

<p>Slicer does not use GPU for any operations beyond 3D rendering.<br>
Only Volume Rendering benefits from high-end GPU.</p>

---

## Post #3 by @muratmaga (2021-04-17 03:58 UTC)

<p>Few more comments:</p>
<p>I see you have a SSD as your OS drive. You would benefit from fast I/O operations, if you keep your datasets on SSD. When saving NRRD (or nifti) volumes, Slicer tries to compress files by default. As far as I know, compression is currently single-threaded and can be quite long for large datasets. When you are saving, you can optionally disable compression (expand Options, and uncheck compress). Here is a related post showing the impact compression may have on I/O: <a href="https://discourse.slicer.org/t/can-slicer-utilise-multiple-cores-on-linux/9240/6" class="inline-onebox">Can Slicer utilise multiple cores on linux? - #6 by muratmaga</a></p>
<p>Your GPU is good that you should get very nice 3D rendering performance in volume rendering. If it stutters, make sure to set the Rendering quality to “Normal” (Advanced-&gt;Techniques-&gt;Quality in Volume Rendering module).</p>

---

## Post #4 by @lassoan (2021-04-18 04:41 UTC)

<p>10-30 seconds load/save time is normal for a 1GB volume if it is compressed. If you can zip a 1GB file on your computer much faster with any software then let us know.</p>
<p>GPU (or many-core CPU) can only make an algorithm faster if you can split the processing to many independent tasks. Unfortunately, most algorithms are sequential in nature and you need to make significant effort to redesign them to allow running some parts of it in parallel. GPU implementations of algorithms have many disadvantages compared to CPU versions, such as they are much more complex (you can only utilize a GPU if parts of the code run concurrently, and this is always complex), not as flexible as CPU implementations (only work for certain data types, require certain graphics hardware and software capabilities, etc.), much harder to debug (no direct access to data during interactive debugging), and it takes significant amount of time to move data between GPU memory and the rest of the application (CPU memory).</p>
<p>In practice, for generic computational algorithms (that are not particularly easy to parallelize) you can only achieve a modest performance improvement (let’s say computation will be 2x faster overall), which is of course nice, but not worth the effort of implementing and maintaining parallel CPU/GPU implementations of large parts of the code.</p>
<p>We heavily utilize GPUs for rendering and other processing steps that are very close to the end of the data processing&amp;rendering pipeline, because GPUs are well positioned to perform these steps for many reasons. The data is already in the GPU, many rendering operations are relatively easily parallelizable, you don’t need to send the results back to CPU, rendering can run in parallel with processing, rendering pipeline is relatively rigid compared to data processing pipelines, etc.</p>
<p>We have a infrastructure and few examples of doing other data processing on GPU. Therefore, if you identify performance bottlenecks in your workflow then you may decide to reimplement those steps and run a bit faster on GPU. However, in general, best use of your resources is to utilize the GPU for tasks that its special architecture fits well naturally.</p>
<hr>
<p>To improve performance make sure that the input volume is cropped and downsampled to the minimum necessary size (you can use Crop volume module). If you cannot go any lower and performance is still not good enough then use a computer that has high CPU clock rate and lots of fast RAM. If that’s not feasible then you can to cut up your volume to smaller ones, edit these pieces one by one, and in the end put the pieces back together into one large volume.</p>

---

## Post #5 by @mluerig (2021-04-18 09:31 UTC)

<p>thanks everyone for the extensive replies!</p>
<p>I am travelling and will get back to you as soon as I have access to the workstation again, in a week or so</p>

---

## Post #6 by @mluerig (2021-06-21 15:44 UTC)

<p>I recently got back to working in 3D slicer, and I paid some more attention to performance at different steps. I think everything is performing as expected given the file sizes and the machine. loading on cropped images is MUCH faster than the whole thing, and rendering performance IS great, not stuttering or anything.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, thanks again for taking the time to explain the nature of GPU optimization!</p>

---
