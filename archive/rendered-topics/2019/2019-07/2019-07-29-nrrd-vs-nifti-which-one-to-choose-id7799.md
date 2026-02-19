---
topic_id: 7799
title: "Nrrd Vs Nifti Which One To Choose"
date: 2019-07-29
url: https://discourse.slicer.org/t/7799
---

# NRRD vs NIFTI: which one to choose?

**Topic ID**: 7799
**Date**: 2019-07-29
**URL**: https://discourse.slicer.org/t/nrrd-vs-nifti-which-one-to-choose/7799

---

## Post #1 by @agirault (2019-07-29 18:41 UTC)

<p>This is a question for users of those two formats: if you had to set up a workflow where you need to store your medical images imported from DICOM in a single file, which would you choose between NRRD and NIFTI (or another?) and why?</p>
<p>Are there clear advantages known for each of those formats versus the other? Has anyone done any benchmarks to compare size, IO speed?</p>
<p>The only knowledge I have is that NIFTI is an upgrade from ANALYZE, and NIFTI itself has two versions where the image orientation can be stored in multiple ways, which aren’t always straightforward: <a href="https://brainder.org/2012/09/23/the-nifti-file-format/" class="inline-onebox" rel="noopener nofollow ugc">The NIFTI file format | Brainder.</a></p>
<p>Thank you</p>

---

## Post #2 by @Chris_Rorden (2019-07-29 20:13 UTC)

<p>While DICOM is very complicated, both NRRD and NIfTI are very simple. From my perspective, they fill a very similar niche and are of similar complexity. I would choose the one that is used most in your domain.</p>
<p>NIfTI is very explicit, with a fixed 348-byte binary header. This makes it very simple to read. However, it is a bit harder to write, because it demands the order of image data dimensions (e.g. a Red, Green, Blue image MUST be saved RGBRGBRGB…), the first three dimensions must be spatial the fourth temporal and dimensions 5,6,7 are up to the user.</p>
<p>NRRD is text based, so it is human readable. It is easy to write, as you can easily describe whatever order you want to your dimensions. The trade off is that it is harder to create a reader, as you need to juggle the image dimensions. What is elegant about NRRD is that the flexibility of the header allows you to create a tiny header that describes a complicated image in a different format, for example you could write a NRRD-format nhdr file that describes most uncompressed DICOM images allowing easy support for DICOM.</p>
<p>With respect to speed, both are very fast to parse, and the small cost of the header is swamped for larger images. Without a doubt, NIfTI being all binary is faster, but in real world cases the amount is negligible. Further, since the NIfTI format is so constrained, many users add a BIDS JSON text sidecar to store extra information, and reading this incurs the same penalty as the text header in NRRD.</p>
<p>In my experience, Slicer supports both thoroughly, so you might want to look at other tools in your toolchain to decide.</p>

---

## Post #3 by @lassoan (2019-07-30 03:54 UTC)

<p>Nifti format contains a lot of neuroimaging-specific details and it is quite rigid (fixed, binary header; inflexible dimensions). This makes nifti a good file format for neuroimaging but not well suited as a general image file format.</p>

---

## Post #4 by @agirault (2019-07-30 15:25 UTC)

<p>Thank you <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> and <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---

## Post #5 by @pieper (2019-08-01 17:58 UTC)

<p>I’d add another nice thing about nrrd is <a href="http://teem.sourceforge.net/unrrdu/" rel="nofollow noopener">the <code>unu</code> command</a>, which can be very convenient for manipulating datasets.  I don’t know if there’s anything similar for nifti.  I’d generally use python to do most of what <code>unu</code> does, but for certain circumstances it’s a good tool.</p>

---

## Post #6 by @Akshay_Goel (2020-12-02 01:33 UTC)

<p>Hello all,</p>
<p>I am a radiologist working on deep learning research and I’m curious on any perspectives on storing raw dicom data as a 3D NumPy volume? This would allow for the fast load times for downstream applications.</p>
<p>I have worked with NifTI and converting files into NumPy ended up slowing things down a lot.</p>

---

## Post #7 by @lassoan (2020-12-02 02:00 UTC)

<p>Loading speed: Loading a 3D array from nrrd or nifti is just as fast as loading from npy/npz file. You may have compared uncompressed npy loading time to compressed nrrd/nifti loading times. All these formats can optionally use compression, which typically cuts required disk space by half and increases loading time by 5-10x.  Loading from DICOM files (single-frame-per-file) takes about 100x more time than loading the same volume from nrrd/nifty/npy (regardless of compression).</p>
<p>Fast loading of course is not the only factor consider, so normally you will use all three kind of data representations: DICOM, research file formats (nrrd, nifti), and tensor files (numpy npy/npz arrays or other specialized hypercube storage). Each file format has its own very important role:</p>
<ul>
<li>DICOM: long-term archival format, preserves all metadata and UIDs; usable across projects and institutions; very slow and complicated.</li>
<li>Research file formats (nrrd, nifti): preserves essential metadata (i.e., image geometry); suitable for representing a single cohort, usable across experiments within a single project, by a small group of collaborators; fast and simple, suitable for images only.</li>
<li>Numpy array (npy, npz): does not preserve metadata, therefore it is only usable for a single experiment, by one or few closely collaborating researchers; fast and very simple, supports arbitrary dimensions and can represent non-image vector data.</li>
</ul>

---

## Post #8 by @Akshay_Goel (2020-12-02 02:08 UTC)

<p>Thank you so much for the quick response <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>Yes, compression could have definitely been a factor.</p>
<p>I was considering the idea of storing a hybrid format with NumPy array for pixel data, than JSON for key metadata of interest. The original dicom data could also be preserved in an archive.</p>
<p>This seems like an optimal combination for a ML pipeline, but would love to hear any possible downsides to this.</p>

---

## Post #9 by @lassoan (2020-12-02 02:37 UTC)

<aside class="quote no-group" data-username="Akshay_Goel" data-post="8" data-topic="7799">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_goel/48/9041_2.png" class="avatar"> Akshay_Goel:</div>
<blockquote>
<p>I was considering the idea of storing a hybrid format with NumPy array for pixel data, than JSON for key metadata of interest. The original dicom data could also be preserved in an archive.</p>
<p>This seems like an optimal combination for a ML pipeline, but would love to hear any possible downsides to this.</p>
</blockquote>
</aside>
<p>This is definitely a good approach for low-level ML pipeline, for a single user, for a specific experiment.</p>
<p>Downsides:</p>
<ul>
<li>numpy file format is only supported in numpy: you cannot directly read it into any medical image computing software; there are no official, high-quality libraries for reading/writing them in any other languages (C++, Java, C#, etc.)</li>
<li>clumsy metadata storage: cannot easily store metadata in the same file, if you store data in separate files then there is a high risk of data corruption (when you copy/move/rename data)</li>
<li>no standard conventions for storing even the most essential metadata (image origin, spacing, axis directions, axis roles, dimensions): you can define your custom metadata format/conventions, but of course it would not be sustainable (imagine what would happen if every researcher would implement his own format)</li>
</ul>
<p>For a specific application domain, larger group of users can agree in their own custom conventions. A good example for this is <a href="https://bids.neuroimaging.io/">BIDS</a>. They do something similar to what you describe (simple image file format + json sidecar for metadata). However, these solutions are only simple and efficient because all users work on sufficiently similar projects, so their assumptions and needs are similar.</p>

---

## Post #10 by @Akshay_Goel (2020-12-02 02:47 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Those are great points to consider! I will definitely also take a look at  <a href="https://bids.neuroimaging.io/" rel="noopener nofollow ugc">BIDS</a></p>

---

## Post #11 by @Akshay_Goel (2020-12-02 04:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="7799">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>inflexible dimensions</p>
</blockquote>
</aside>
<p>For Nifti: What aspects are inflexible about the dimensions? I have used Nifti to store masks for abdominal imaging projects with standard MR dimensions of 512 x 512 x [slices].</p>
<p>Thanks again! I’m learning a lot from this conversation</p>

---

## Post #12 by @Akshay_Goel (2020-12-02 04:46 UTC)

<p>Also, I think HDf5 will answer a lot of the considerations and works as a really nice medium for merging data formats such as numpy and attribute data.</p>

---

## Post #13 by @lassoan (2020-12-02 05:04 UTC)

<aside class="quote no-group" data-username="Akshay_Goel" data-post="11" data-topic="7799">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_goel/48/9041_2.png" class="avatar"> Akshay_Goel:</div>
<blockquote>
<p>For Nifti: What aspects are inflexible about the dimensions?</p>
</blockquote>
</aside>
<p>See in the <a href="https://brainder.org/2012/09/23/the-nifti-file-format/">nifti standard</a>. There is pretty much no flexibility in how you define 5 out of 7 dimensions.</p>
<blockquote>
<p>In the nifti format, the first three dimensions are reserved to define the three spatial dimensions — <em>x</em> , <em>y</em> and <em>z</em> —, while the fourth dimension is reserved to define the time points — <em>t</em> . The remaining dimensions, from fifth to seventh, are for other uses. The fifth dimension, however, can still have some predefined uses, such as to store voxel-specific distributional parameters or to hold vector-based data.</p>
</blockquote>
<aside class="quote no-group" data-username="Akshay_Goel" data-post="12" data-topic="7799">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_goel/48/9041_2.png" class="avatar"> Akshay_Goel:</div>
<blockquote>
<p>HDf5 will answer a lot of the considerations and works as a really nice medium for merging data formats such as numpy and attribute data.</p>
</blockquote>
</aside>
<p>HDF5 is a very powerful container format. Unfortunately, it is so complex that in practice it often creates more problems than it solves (see for example <a href="https://cyrille.rossant.net/should-you-use-hdf5/">here</a>).</p>

---

## Post #14 by @Akshay_Goel (2020-12-02 05:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="7799">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>fast and very simple, supports arbitrary dimensions and can represent non-image vector data.</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. I will review those references. I really appreciate all of your feedback!</p>

---

## Post #15 by @Chris_Rorden (2020-12-02 11:58 UTC)

<p><a href="https://cyrille.rossant.net/moving-away-hdf5/" rel="noopener nofollow ugc">Cyrille Rossant</a> describes some of the concerns with HDF5.</p>
<p>Compression always trades off file size for speed. Both NRRD and NIfTI use the gz format. This is an old, simple format. However, due to its popularity a lot of development has focused on optimizing this tool. Using an optimized gz-compatible library (CloudFlare, ng or lib deflate) can dramatically accelerate this format for <a href="https://github.com/neurolabusc/zlib-bench-python" rel="noopener nofollow ugc">single</a> and <a href="https://github.com/neurolabusc/pigz-bench-python" rel="noopener nofollow ugc">parallel</a> threaded environments.</p>
<p>A limitation of most compression schemes (gz, zstd, etc) is that they are tuned for text and 8-bit data. Raw MRI and CT scans are typically 16-bit integer, and 32-bit float is common for computation. With these data types, <a href="https://github.com/facebook/zstd/issues/1492" rel="noopener nofollow ugc">bit-shuffling</a> can dramatically improve performance.</p>
<p>If you want to share data with other tools, leveraging the large ecosystem, I would encourage NIfTI or NRRD (uncompressed when speed matters, compressed for file size).</p>
<p>If you want a nice container format that is strictly for Python, you may want to look at <a href="https://zarr.readthedocs.io/en/stable/" rel="noopener nofollow ugc">zarr</a> with its support of <a href="https://numcodecs.readthedocs.io/en/stable/blosc.html" rel="noopener nofollow ugc">bit-shuffling optimized zstd</a>. You could again choose uncompressed for speed, but would have access to a modern, high performance compression method that is optimized for your data.</p>

---
