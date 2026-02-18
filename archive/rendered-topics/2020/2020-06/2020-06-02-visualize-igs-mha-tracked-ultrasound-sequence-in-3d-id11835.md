# Visualize .igs.mha tracked ultrasound sequence in 3D

**Topic ID**: 11835
**Date**: 2020-06-02
**URL**: https://discourse.slicer.org/t/visualize-igs-mha-tracked-ultrasound-sequence-in-3d/11835

---

## Post #1 by @Tonight1121 (2020-06-02 14:47 UTC)

<p>Hi! I am new to the Slicer and I am trying to visualize some seqeunce file examples shared in PlusDataLib repository.<br>
While I load the SpineUltrasound-Lumbar-C5.igs.mha as Sequence Metafile into the Sequence browser, it displays well in the 2D window. Since I noticed that every frame inside this sequence file has a corresponding transformation (ReferenceToTrackerTransform), I was expecting the 3D window could show the different spatial position of each frame. However, the frames showed in the 3D window (right most) tends to have a fixed location: frames does not move based on different transformation matrix.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c7b9f6da4b2b6597ed50803f24d09aa13008958.gif" alt="SpineUltrasound" data-base62-sha1="aUB9c6wAmqEG16I9WlMfiCtn0kE" width="600" height="264"><br>
In fact, I was expecting some visualization effects like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd29e44bf601c0cf14156a9a7a589efea5641ed5.gif" alt="UltrasoundToolGuidance3dOnly" data-base62-sha1="tgXDjLMcNX7k2fsJ1855TOEmZBr" width="344" height="268"><br>
How can I visualize the frames sequence while each frame is posed on its corresponding transformation? Thank you so much for your time!</p>

---

## Post #2 by @lassoan (2020-06-02 19:05 UTC)

<p>There can be lots of transforms in a .igs.mha file and you have several choices for reference transform. To specify these, apply a ImageToX (ImageToReference, ImageToRAS, …) to the image and make a selected slice view move with the image by using “Volume reslice driver” module.</p>
<p>These are all described in detail in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>. Let us know if something is not clear.</p>

---

## Post #3 by @Tonight1121 (2020-06-07 20:00 UTC)

<p>Thank you very much! I checked SlicerIGT tutorials and  “Tracked ultrasound visualization in 3D Slicer” solved my problem!</p>

---

## Post #4 by @Tonight1121 (2020-06-26 16:58 UTC)

<p>Hello Dr. Lasso! Since last time I have been trying to convert our own data into the .mha type of images for visualization in Slicer. After checking the SlicerIGT tutorials, a new problem just came to me: I am not sure what the “Reference”  means in “ImageToReferenceTransform”. Could you please help shed some light on that? Thank you so much!</p>

---

## Post #5 by @lassoan (2020-06-26 17:32 UTC)

<p>You can choose any coordinate system as reference. ImageToReferenceTransform defines origin, axes directions, and spacing of the image in that coordinate system. See examples here:</p>
<ul>
<li><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/CommonCoordinateSystems.html">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/CommonCoordinateSystems.html</a></li>
<li><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationfCalCoordinateSystemDefinitions.html">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationfCalCoordinateSystemDefinitions.html</a></li>
</ul>

---

## Post #6 by @Tonight1121 (2020-07-15 17:42 UTC)

<p>Thank you Dr. Lasso!</p>
<p>I have managed to generate the .mhd sequence file, loaded into Slicer and build a reconstructed 3D ultrasound volume using VolumeReconstructor.exe. The outcome is amazing and thank you so much for the incredible work!</p>
<p>Just a minor question: Is there a version of VolumeReconstructor that can run in Linux environment? So far I only succeeded running it in Windows, and I read about the fact (<a href="https://plustoolkit.github.io/developersguide.html" rel="nofollow noopener">developer guide</a>) that “many of the drivers written for devices are Windows specific, and thus capture cannot be done on a Linux or MacOSX machine”. Is it still under development? Much appreciated for your time!</p>

---

## Post #7 by @lassoan (2020-07-16 03:19 UTC)

<p>Volume reconstruction module is included in SlicerIGSIO extension, which is available on all platforms and can be used with the interactive GUI or from C++ or Python (and therefore via command line, too).</p>
<p>You can also build <a href="https://github.com/PlusToolkit/PlusLib">Plus toolkit</a> on Linux, which contains the command-line VolumeReconstructor utility.</p>

---

## Post #8 by @Tonight1121 (2020-09-16 00:22 UTC)

<p>Hi Dr. Lasso! Recently I have been trying to do some data processing for my research, I met a problem and cannot understand why this happens. And I really appreciate it if you can help shed some lights on this.</p>
<p>First of all, I have managed visualize the image sequence. Each frame correspond to a 4x4 transformation matrix, and it looks good in the Slicer window:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9d7d7e2abbec45cec14d79e39cb88db24d5a06c.gif" data-download-href="/uploads/short-url/sNApEh1f15qCEcZ17LkfztsOYDW.gif?dl=1" title="normal2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9d7d7e2abbec45cec14d79e39cb88db24d5a06c_2_517x342.gif" alt="normal2" data-base62-sha1="sNApEh1f15qCEcZ17LkfztsOYDW" width="517" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9d7d7e2abbec45cec14d79e39cb88db24d5a06c_2_517x342.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9d7d7e2abbec45cec14d79e39cb88db24d5a06c_2_775x513.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9d7d7e2abbec45cec14d79e39cb88db24d5a06c_2_1034x684.gif 2x" data-dominant-color="32323D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">normal2</span><span class="informations">1461×969 2.91 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then, I use matrix multiplication, multiply every transformation matrix with the inverse of the first transformation matrix. I did this because I want to move the first frame to the origin of the coordinate system, and want to maintain the inter-frame relationship across the sequence. After I did this, the visualization looks weird to me, with only the very first frames appear normal, and rest of the sequence seem to be cropped in a weird way:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d2a32322516d301c56753dc0272fc7c967686bb.gif" data-download-href="/uploads/short-url/fzIrPNlJdc7dQgUp7C60w0030wj.gif?dl=1" title="weird2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d2a32322516d301c56753dc0272fc7c967686bb_2_517x342.gif" alt="weird2" data-base62-sha1="fzIrPNlJdc7dQgUp7C60w0030wj" width="517" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d2a32322516d301c56753dc0272fc7c967686bb_2_517x342.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d2a32322516d301c56753dc0272fc7c967686bb_2_775x513.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d2a32322516d301c56753dc0272fc7c967686bb_2_1034x684.gif 2x"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">weird2</span><span class="informations">1461×969 1.95 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I thought that: we can imagine that the inverse of the first frame’s transformation matrix is also a transformation matrix. It can move the first frame to the identity matrix. And since every frame will be transformed again by the first frame’s inverse, it looks like we are moving all the rest frames in the same way.</p>
<p>But I just cannot figure it out, why the images seem to be oddly cropped after my operations. Could you please shed some light on this? Thank you so much!</p>

---

## Post #9 by @lassoan (2020-09-17 02:47 UTC)

<p>Make sure you set the image as input in Volume reslice driver module.</p>

---
