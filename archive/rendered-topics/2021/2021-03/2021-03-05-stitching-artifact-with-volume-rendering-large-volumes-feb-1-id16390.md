# Stitching artifact with volume rendering large volumes (Feb 17 2021 nightly)

**Topic ID**: 16390
**Date**: 2021-03-05
**URL**: https://discourse.slicer.org/t/stitching-artifact-with-volume-rendering-large-volumes-feb-17-2021-nightly/16390

---

## Post #1 by @hherhold (2021-03-05 15:40 UTC)

<p>I’m running into a weird stitching artifact with volume rendering, and at first I thought it was my volume (rather large) but I can duplicate it by resampling available sample data to make a large volume.</p>
<p>This is on a 2019 MacBook Pro 16" with a AMD Radeon Pro 5500M 8 GB, using GPU Raycasting.</p>
<ol>
<li>Start slicer</li>
<li>Download CT Chest sample data</li>
<li>Go to Crop Volume</li>
<li>Create an ROI, fit to volume</li>
<li>In spacing scale, pick 0.3x, so new volume is 1706x1706x483</li>
<li>Click “Apply”</li>
<li>Go to data module, delete original volume (save space)</li>
<li>Go to volume rendering, click eye to make volume visible</li>
</ol>
<p>It looks like the volume is split into several blocks, where the data looks like it’s wrapping or something. CPU recasting works (but is slow, of course). No errors in the console. I do not think I’m violating AMD’s 3D texture limit of 2048.</p>
<p>Image below. Any ideas?</p>
<p>Thanks!!</p>
<p>-Hollister</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31527a444d887f73ebbcac01bb24d79ae70d5fac.jpeg" data-download-href="/uploads/short-url/72k6pSaQn2N4bLpJZ211IoAqVwo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31527a444d887f73ebbcac01bb24d79ae70d5fac_2_690x474.jpeg" alt="image" data-base62-sha1="72k6pSaQn2N4bLpJZ211IoAqVwo" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31527a444d887f73ebbcac01bb24d79ae70d5fac_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31527a444d887f73ebbcac01bb24d79ae70d5fac_2_1035x711.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31527a444d887f73ebbcac01bb24d79ae70d5fac_2_1380x948.jpeg 2x" data-dominant-color="6E6F7B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1590×1094 460 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-03-05 15:41 UTC)

<p>Which Slicer version is this? Do you see any errors or warnings in the log?</p>

---

## Post #3 by @hherhold (2021-03-05 15:43 UTC)

<p>4.13.0-2021-02-17, the MacOS Feb 17 nightly build. No errors or warnings in the log.</p>

---

## Post #4 by @hherhold (2021-03-05 16:39 UTC)

<p>Incidentally, I made a dataset that exceeds the AMD 3D texture size limit and there are no errors in the log. So perhaps this is what is happening? <a class="mention" href="/u/muratmaga">@muratmaga</a>, you mentioned this a while back on a thread about external GPUs. Have you run into instances where you’ve exceeded AMD’s 3D texture limit?</p>
<p>Thanks!</p>

---

## Post #5 by @lassoan (2021-03-05 16:50 UTC)

<p>It works fine for me with an NVidia RTX2080 on Windows (other than the OS sometimes shutting down the application from time to time due to TDR timeout; but I could increase the timeout to prevent this). Most likely the problem you are experiencing is is a driver bug or hardware limitation.</p>

---

## Post #6 by @hherhold (2021-03-05 16:53 UTC)

<p>I’ve been considering an external GPU with 16GB of graphics card memory, but not if I still run into this problem. Need to find a Mac somewhere with 16GB graphics memory to test this.</p>
<p>Thanks for checking! Much appreciated.</p>
<p>-Hollister</p>

---

## Post #7 by @hherhold (2021-03-05 17:51 UTC)

<p>Apologies for the cross-post from an earlier thread on external graphics cards.</p>
<p>I’m not so sure this is an issue with the maximum 3D texture size on AMD cards. OpenGL caps viewer says this is 16384 on my system.</p>
<p>Doesn’t answer what’s going on, however.</p>

---

## Post #8 by @muratmaga (2021-03-05 18:09 UTC)

<p>Neither did I have any issue on Linux with Geforce 1080TI</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="16390">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>he application from time to time due to TDR timeou</p>
</blockquote>
</aside>
<p>I only have the TDR, when I have the GPU quality set to adaptive. Even on 1080TI the speed is great when the quality set to Normal (in adaptive it crashes).</p>

---

## Post #9 by @lassoan (2021-03-05 18:25 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="16390">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I only have the TDR, when I have the GPU quality set to adaptive. Even on 1080TI the speed is great when the quality set to Normal (in adaptive it crashes).</p>
</blockquote>
</aside>
<p>I’ve checked this and the same happens on my computer. “Maximum quality” mode causes TDR timeout immediately, “Adaptive” mode works fine if I rotate but times out when for example I center the view. “Adaptive” mode adjusts sampling distance to higher/lower values to determine the maximum image quality that can be achieved on the GPU and during these iterations it can run into slower rendering times, which can cause the TDR timeout.</p>
<p>Since rendering time estimation for GPU is very complex, it is hard to come up with a good adaptive scheme, so using “Normal” mode is reasonable.</p>

---

## Post #10 by @hherhold (2021-03-05 19:11 UTC)

<p>Down-sampling my large volume from 16 bit to 8 bit makes the problem go away. So it’s not an issue with image dimensions, but of memory usage. (I think.)</p>

---

## Post #11 by @hherhold (2021-03-05 19:23 UTC)

<p>Also from other thread - I cropped and resampled MRHead to be like 200x200x4096, and it renders fine. So it’s most likely memory usage (somehow).</p>

---

## Post #12 by @hherhold (2021-03-06 01:58 UTC)

<p>I was able to load the original volume that’s been giving me problems (16 bit, 922x1132x2020) into an older version of Drishti, which also does volume rendering using OpenGL but is much more limited in segmentation capabilities, and it renders fine with no stitching. So it is not a MacOs or OpenGL issue.</p>
<p>ParaView has the same issue when I load the NRRD file in. Could this be a MacOS ITK issue?</p>

---

## Post #13 by @hherhold (2021-03-06 02:02 UTC)

<p>Make that VTK, not ITK</p>

---

## Post #14 by @lassoan (2021-03-06 02:43 UTC)

<p>Check the source code of drishti (<a href="https://github.com/nci/drishti" class="inline-onebox">GitHub - nci/drishti: Drishti</a>). If its rendering code base is old then it is very likely that it downscales the volume before sending it to the GPU, because 8-10 years ago it was very rare that you could render a volume at its native resolution. VTK used to do this in its previous rendering backend, but this feature has not been reimplemented yet after its rendering backend was reworked a few years ago.</p>
<p>It is of course also possible that there is a bug in VTK how it splits up and sends the texture to the GPU (as far as I remember it does something like that), so I would recommend to write about this to the VTK forum. Maybe somebody recognizes the appearance of this artifact. It is good that it is reproducible in Paraview, too, because it proves that the problem is not how Slicer uses VTK.</p>

---

## Post #15 by @hherhold (2021-03-06 02:47 UTC)

<p>Okie dokie, thanks for the tips. Drishti for Mac hasn’t been updated in some time so it wouldn’t surprise me if it downsampled. It was only in the last update that it supported 16 bit data, for example.</p>
<p>I’ve been messing with some of the python VTK examples to get a simple example that shows the problem. But yeah, the fact that ParaView does it too is a useful data point.</p>
<p>Thanks, Andras!</p>

---

## Post #16 by @lassoan (2021-03-06 03:29 UTC)

<p>One more thing to try. You can partition the volume (upload to GPU in smaller blocks) using <code>SetPartition</code> method. For example, you can try this script (or change partitions to 4,4,4 or 1,1,2, …) and see it if makes any difference:</p>
<pre><code class="lang-python">threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
vrDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName('vtkMRMLVolumeRenderingDisplayableManager')
vrMapper = vrDisplayableManager.GetVolumeMapper(getNode('CTChest'))
vrMapper.SetPartitions(2,2,2)
</code></pre>
<p>Overall, I don’t see much difference when using partitions, but <code>SetPartition(4,4,4)</code> seems to decrease TDR occurrence a bit for me (that otherwise would quite frequently occur with the “Adaptive” quality option).</p>

---

## Post #17 by @hherhold (2021-03-06 14:21 UTC)

<p>Hmm, this seems to do <em>something</em>, or at least have some sort of effect. Screen shot is with 2,2,2 - I will play with this some more and see what it does.</p>
<p>Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9af82a07f25a080990b143669f890fd6d34fc03f.jpeg" data-download-href="/uploads/short-url/m6VdCL8moqZMaZZPCFTsCCv0UDZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9af82a07f25a080990b143669f890fd6d34fc03f_2_584x500.jpeg" alt="image" data-base62-sha1="m6VdCL8moqZMaZZPCFTsCCv0UDZ" width="584" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9af82a07f25a080990b143669f890fd6d34fc03f_2_584x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9af82a07f25a080990b143669f890fd6d34fc03f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9af82a07f25a080990b143669f890fd6d34fc03f.jpeg 2x" data-dominant-color="80828D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">624×534 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #18 by @hherhold (2021-03-06 15:16 UTC)

<p>OKAY!  (1,1,2) seems to work!</p>
<p>THANKS A MILLION!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1ffed7dc4554e393f1678ba0f87ce78f78a90ebc.jpeg" data-download-href="/uploads/short-url/4z2NDD3c70dm3OsiXndQuzzuqks.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ffed7dc4554e393f1678ba0f87ce78f78a90ebc_2_506x499.jpeg" alt="image" data-base62-sha1="4z2NDD3c70dm3OsiXndQuzzuqks" width="506" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ffed7dc4554e393f1678ba0f87ce78f78a90ebc_2_506x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1ffed7dc4554e393f1678ba0f87ce78f78a90ebc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1ffed7dc4554e393f1678ba0f87ce78f78a90ebc.jpeg 2x" data-dominant-color="85727E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">561×554 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #19 by @lassoan (2021-03-06 16:30 UTC)

<p>Awesome!</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> please keep an eye on this. If partitions can fix rendering of large volumes then we may expose this option in the GUI (or if we learn more about what settings work then even enable it automatically above a certain volume size).</p>

---

## Post #20 by @muratmaga (2021-03-06 16:37 UTC)

<p>OK. I will unfortunately, i never encountered this issue on the nvidia cards we have…</p>

---

## Post #21 by @lassoan (2021-03-07 01:46 UTC)

<p>Partitioning may also enable arbitrarily large volumes, as it breaks down the large array to smaller pieces and so you don’t hit the limit of maximum texture size.</p>

---
