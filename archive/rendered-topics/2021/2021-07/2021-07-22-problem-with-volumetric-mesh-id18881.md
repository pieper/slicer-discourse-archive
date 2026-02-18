# Problem with volumetric mesh

**Topic ID**: 18881
**Date**: 2021-07-22
**URL**: https://discourse.slicer.org/t/problem-with-volumetric-mesh/18881

---

## Post #1 by @rcapozza (2021-07-22 18:15 UTC)

<p>Hi guys.<br>
I’ve a series of ct-scans images of a central part of human tibia, this was obtained with a Stratec pQCT machine and exported in jpg format, named accordingly, for perform later import in Slicer software. Once the scans are imported, I follow these steps: 1) set the x, y, z parameter in the “volume module”, 2) I segment the image, 3) I use the “mesher volume” module for creating a volumetric mesh from segmented image for finite element analysis performed later in FEBio. The question is, first: why the volumetric mesh obtained is not volumetric? I say that because I can’t see a mesh between outer and inner perimeter; and the last one question is, why the module “mesher module” not render the ends flats as I hoply?. Thanks in advance for the details that I should consider for the creation of the mesh, nothing more for now, best regards to all.</p>

---

## Post #2 by @Fluvio_Lobo (2021-07-22 18:31 UTC)

<p><a class="mention" href="/u/rcapozza">@rcapozza</a>,</p>
<p>Can you add some images that describe your workflow in a little more detail?<br>
I have used the <a href="https://github.com/lassoan/SlicerSegmentMesher" rel="noopener nofollow ugc">Segment Mesher</a> module in the past for <a href="https://discourse.slicer.org/t/meshing-self-intersecting-faces/13588">multi-compartment models</a> then simulated in FEBio.</p>

---

## Post #3 by @lassoan (2021-07-22 21:26 UTC)

<p>I would recommend to provide more details so that <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a> can help you more effectively, I just quickly reflect on a few specific questions you asked.</p>
<aside class="quote no-group" data-username="rcapozza" data-post="1" data-topic="18881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rcapozza/48/11682_2.png" class="avatar"> rcapozza:</div>
<blockquote>
<p>The question is, first: why the volumetric mesh obtained is not volumetric?</p>
</blockquote>
</aside>
<p>SegmentMesher module creates volumetric meshes. You need to cut into the mesh or threshold it so that you can see the volumetric mesh elements inside.</p>
<aside class="quote no-group" data-username="rcapozza" data-post="1" data-topic="18881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rcapozza/48/11682_2.png" class="avatar"> rcapozza:</div>
<blockquote>
<p>I say that because I can’t see a mesh between outer and inner perimeter; and the last one question is, why the module “mesher module” not render the ends flats as I hoply?</p>
</blockquote>
</aside>
<p>It is up to you how you want to visualize the plane cuts. You can choose crinkle cut (whole volumetric cells are kept) or straight cut (you cut into cells). You can adjust options in the Display section of SegmentMesher module or Display and Clipping planes sections of Models module.</p>

---

## Post #4 by @rcapozza (2021-07-23 01:32 UTC)

<p>Hello, according to what Fluvio_Lobo suggested, I am uploading a sequence of png files with the steps of importing cortical tibial bone sections and their subsequent export to volumetric mesh for finite element analysis.<br>
Thanks in advance, Ricardo<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929642b7a107300943fe57d433601249a1867a86.png" alt="Step1" data-base62-sha1="kULDQ1MkVT428IaHKywBw165VVY" width="624" height="351"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9ea6b6a269e974fa61894fa284353e27f84862d.png" alt="Step2" data-base62-sha1="zER8aC9RwhqO6Y3UFWgM3dxLI3b" width="624" height="351"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5e21ccb7228d8dc33215a51bbd250149de4f79b.png" alt="Step3" data-base62-sha1="wNDMDySB5V5AzRn9hQjHLwwC1PJ" width="624" height="351"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edb501e91ecc63ecfbb409335c23bb93033afd8f.png" alt="Step4" data-base62-sha1="xUQXXUphjQ8ZoyMmomWNjIhN211" width="624" height="351"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d557600849493d1caeb6db4fd74c00781f82870d.jpeg" data-download-href="/uploads/short-url/uriTTyLPlGuKHax9RKgfcSFqOfz.jpeg?dl=1" title="Step5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d557600849493d1caeb6db4fd74c00781f82870d_2_690x423.jpeg" alt="Step5" data-base62-sha1="uriTTyLPlGuKHax9RKgfcSFqOfz" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d557600849493d1caeb6db4fd74c00781f82870d_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d557600849493d1caeb6db4fd74c00781f82870d_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d557600849493d1caeb6db4fd74c00781f82870d_2_1380x846.jpeg 2x" data-dominant-color="8E8F9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Step5</span><span class="informations">3900×2395 691 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5960384602a81361d8661aff01b73999bde7ffda.jpeg" data-download-href="/uploads/short-url/cKEDYUVxnauiU0rY26RDVSmYFvQ.jpeg?dl=1" title="Step6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5960384602a81361d8661aff01b73999bde7ffda_2_690x445.jpeg" alt="Step6" data-base62-sha1="cKEDYUVxnauiU0rY26RDVSmYFvQ" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5960384602a81361d8661aff01b73999bde7ffda_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5960384602a81361d8661aff01b73999bde7ffda_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5960384602a81361d8661aff01b73999bde7ffda_2_1380x890.jpeg 2x" data-dominant-color="787774"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Step6</span><span class="informations">3900×2517 1.13 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Fluvio_Lobo (2021-07-23 02:03 UTC)

<p><a class="mention" href="/u/rcapozza">@rcapozza</a>,</p>
<p>Unless you have a reason for using Tetgen, I would recommend using Cleaver as the tool for generating a volumetric mesh in 3D Slicer. My thinking for this is that you will likely want to scale to multiple compartments (or tissues) and Cleaver was designed for this task.</p>
<p>If you are only meshing a single tissue (as in your pictures) and you really want to use Tetgen, you can always run Tetgen separately or even through FEBio. You can take an .STL of this segmentation as the input to Tetgen.</p>
<p>Regarding the features and artifacts in the segmentation, which later affect the mesh, you may have to do some image pre-processing, filtering, and segmentation smoothing.</p>
<p>Let me know if this helps, this is not an easy process at all. If you need more help, feel free to send me your data (if you can). I can take a look.</p>

---

## Post #6 by @rcapozza (2021-07-23 17:03 UTC)

<p>Thank you very much <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a>  for your advice for the generation of volumetric mesh, I will proceed with your recommendations, we remain in contact, kind regards, Ricardo.</p>

---
