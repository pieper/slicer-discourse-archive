---
topic_id: 7247
title: "Ultrasound Slice Is Not Aligned With Reconstructed Volume"
date: 2019-06-19
url: https://discourse.slicer.org/t/7247
---

# Ultrasound slice is not aligned with reconstructed volume

**Topic ID**: 7247
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/ultrasound-slice-is-not-aligned-with-reconstructed-volume/7247

---

## Post #1 by @vgonzalezd (2019-06-19 16:27 UTC)

<p>Hello,<br>
I have 3 questions:</p>
<ol>
<li><strong>Does anyone have an idea why my ultrasound images don’t match over my reconstructed volume?</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1af833bb2f23f015fb771c2204a300ac313d252.png" alt="image" data-base62-sha1="wcvsPaR6dCNHiMedoJ4JLkfpcpI" width="589" height="254"><br>
I create my volume with PLUS, and the ImageToProbeTransform is included in the imageToReferenceTransform defined on the “prueba2.mha” file.</li>
</ol>
<p>PlusApp-2.6.0.20190221-Win64\bin\VolumeReconstructor.exe --config-file=" prueba2-VolRec.xml" --image-to-reference-transform=ImageToReference --source-seq-file=" prueba2.mha" --output-volume-file=" prueba2Volume.mha"<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e226ca9f712f685a15d930cf4fdedcf1c332f00.png" alt="image" data-base62-sha1="b9cZNCeRoZ5C7joYnxDga0iyGs0" width="375" height="237"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c799f4003833450876b1a9a2aefc212ff0c164c6.png" alt="image" data-base62-sha1="stKRiALYwQOwReJ0vcAvuh6IXFc" width="414" height="351"></p>
<ol start="2">
<li><strong>How I do to reconstruct my volume specifying the axes orientation:</strong><br>
Axes are inclined, I would like to Have the red view on the same orientation that the first ultrasound image.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cd2d05c392e4a0ad6baf3d9f4d8a5208ca5f4ab.jpeg" alt="image" data-base62-sha1="k5MvMldqbCiIfFRoBb1mMsUok4z" width="666" height="237"></li>
</ol>
<p>Because I would like to <em>extract SLICES</em> from the compounding volume of ultrasound images and MASKS from the compounding volume of contours images.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a03642d8a624e10de0b40724465bc4e6f8a8441.jpeg" data-download-href="/uploads/short-url/ayKB7kP93j4WoCoNMZm2FtTd2r7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a03642d8a624e10de0b40724465bc4e6f8a8441_2_690x313.jpeg" alt="image" data-base62-sha1="ayKB7kP93j4WoCoNMZm2FtTd2r7" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a03642d8a624e10de0b40724465bc4e6f8a8441_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a03642d8a624e10de0b40724465bc4e6f8a8441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a03642d8a624e10de0b40724465bc4e6f8a8441.jpeg 2x" data-dominant-color="9395B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">723×329 83.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce85bd35e6039023dc4ba50c76a4225963267900.png" alt="image" data-base62-sha1="tsYTp4OVmd7mRwVZN686trRn8Pe" width="558" height="224"></p>
<p>If I’m not mistaken, the reconstructed volume is saved as slices throw an axis. do not?<br>
If the reconstruction is done with the correct position and orientation of the axes, to recover the SLICES I should only read the mha format, similar to how it is done with a DICOM to obtain images. NOT?</p>
<ol start="3">
<li><strong>How I can plot the ultrasound probe like in this video</strong>:<br>
<a href="https://www.youtube.com/watch?v=2Oc_tCu_uzs" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=2Oc_tCu_uzs</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8df6b07492eaa2fffe42a35e4c4217a5bb10c515.png" alt="image" data-base62-sha1="kfRQRGskJ3HjLK84ZpyGTl9Hpul" width="325" height="272"></li>
</ol>
<p>I thanks you so much for your help<br>
Vanessa GONZALEZ</p>

---

## Post #2 by @lassoan (2019-06-19 16:54 UTC)

<p>Probably there is an RAS/LPS coordinate system difference. Configuration files are optimized for real-time reconstruction, when image is reconstructed in RAS coordinate system and sent to Slicer using OpenIGTLink.</p>
<p>If you reconstruct a volume using the VolumeReconstructor application then it reconstruct the image in RAS coordinate system and saves the image into a file. If you load an image file into Slicer then it is assumed to be in LPS coordinate system. To fix this inconsistency, either change the Plus configuration file to reconstruct in LPS coordinate system or apply this transformation matrix to the reconstructed image after you load it into Slicer:</p>
<pre><code>-1  0 0 0
0 -1 0 0
0 0 1 0
0 0 0 1
</code></pre>
<aside class="quote no-group" data-username="vgonzalezd" data-post="1" data-topic="7247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/b782af/48.png" class="avatar"> vgonzalezd:</div>
<blockquote>
<p>How I do to reconstruct my volume specifying the axes orientation:</p>
</blockquote>
</aside>
<p>You specify the coordinate system you want to reconstruct in by the <code>image-to-reference-transform</code> parameter.</p>
<aside class="quote no-group" data-username="vgonzalezd" data-post="1" data-topic="7247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/b782af/48.png" class="avatar"> vgonzalezd:</div>
<blockquote>
<p>How I can plot the ultrasound probe like in this video</p>
</blockquote>
</aside>
<p>You can find link to step-by-step instructions in the video comment. The .mrb scene file is included in Plus installation package.</p>

---

## Post #3 by @vgonzalezd (2019-07-01 16:05 UTC)

<p>Thank you Andras for your help, I tried to solve the problems in different ways before publish some stupid thing:</p>
<ol>
<li>
<p>I tried the matrix transformation solution to pass from RAS to LPS system, it worked really well. I tried also to: “<strong>change the Plus configuration file to reconstruct in LPS coordinate system</strong>”. But I thing, I am changing the wrong file.<br>
I suppose the plus configuration file, is the xml that I give as parameter of reconstruction. I define the transformation ReferenceToReference2. And I reconstruct the volume, but it does not to nothing.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bd65fd5110082890dce6d2f424b3a58c2302095.png" alt="image" data-base62-sha1="1GIxV10H4ocvP4wrsYaVLQLOCfX" width="362" height="232"></p>
</li>
<li>
<p>I changed ImageToReferenceTransformations in the .mha file, one by one, and it worked!!! Thanks for the idea.<br>
I couldn’t make work reconstruction changing the parameter “ `image-to-reference-transform="<strong>ReferenceToReference3</strong>”, Plus volumeReconstruction says:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f97b35c017a775db9e4f89c0459581bb7726df5f.png" alt="image" data-base62-sha1="zB0RHW5m96xcCNxCKCET6LuxxN5" width="589" height="110"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/eccb742790b1b5e12fd413adc7ff57e80d387d0a.png" alt="image" data-base62-sha1="xMMzZWfkfNaIowFcG1AqaL0k7c6" width="310" height="162"></p>
</li>
<li>
<p>I did not explain well. I did the step by step of the video, but I don’t find the way to print the probe.stl on realtime over my tracked images, I don’t need to simulate images, I have them already. If it is possible, could someone redirect me to the documentation, please? I’am sorry.</p>
</li>
<li>
<p><em>“NEW ISSUE”: Images from my MHA file are charged as LIFO:</em><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4bef3938a9e85579257bb9bc0371975546d2eb0.png" alt="image" data-base62-sha1="pMX3uuiPib2Fpt0Iuudr405CiIw" width="528" height="395"><br>
I extract the first image from my mha file, and I plot it with pyplot and they are good. Tracking Transforms matrices are created, taking as reference, the up-left corner.<br>
When I upload the images from my mha file in slicer I’m pretty sure they are charged as LIFO, so the bottom-rigth corner becomes the top-left corner.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dc6bc00c8b518a0b29335ecf90e04d6e32aa3b7.png" alt="image" data-base62-sha1="4fpDfEgkWdklaBsEfWwpByK4rt5" width="364" height="195"><br>
I do not just need to flip it in the slicer-view (I did it), because in the 3dspaceview they are not flipped soo tracking and reconstruction is not well done.<br>
4.a I try changing the .mha  parameter AnatomicalOrientation = RAI to RAS, TO LPS, etc. It didn’t work.<br>
I don’t want to save the images in the .mha as LIFO to be readed well, but if it is the only option I will do it.</p>
</li>
</ol>
<p>Thank you and nice day.</p>

---

## Post #4 by @lassoan (2019-07-01 18:08 UTC)

<aside class="quote no-group" data-username="vgonzalezd" data-post="3" data-topic="7247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/b782af/48.png" class="avatar"> vgonzalezd:</div>
<blockquote>
<p>I couldn’t make work reconstruction changing the parameter “ `image-to-reference-transform=" <strong>ReferenceToReference3</strong> ”, Plus volumeReconstruction says:</p>
</blockquote>
</aside>
<p>The error message “Unable to allocate … elements of size …” means that you have run out of memory. You need to decrease the image resolution (increase output voxel spacing) or reduce the region of interest sweeped by the probe. Since Plus computed that you would need 434GB of memory, it may indicate that not just the spacing is off but the region of interest is too big, potentially because of errors in how the coordinate systems are defined.</p>
<aside class="quote no-group" data-username="vgonzalezd" data-post="3" data-topic="7247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/b782af/48.png" class="avatar"> vgonzalezd:</div>
<blockquote>
<p>I did not explain well. I did the step by step of the video, but I don’t find the way to print the probe.stl on realtime over my tracked images, I don’t need to simulate images</p>
</blockquote>
</aside>
<p>Regardless you use real or simulated image source, you can use the exact same Slicer scene for visualization.</p>
<aside class="quote no-group" data-username="vgonzalezd" data-post="3" data-topic="7247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/b782af/48.png" class="avatar"> vgonzalezd:</div>
<blockquote>
<p>NEW ISSUE”: Images from my MHA file are charged as LIFO:</p>
</blockquote>
</aside>
<p>Make sure to set the <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceMicrosoftMediaFoundation.html">PortUsImageOrientation</a> tag correctly. See specification <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/UltrasoundImageOrientation.html">here</a>. If you don’t know what orientation your device provides images in then you can find the correct port US image orientation value by trial and error. Note that if you change the image orientation (or resolution, etc.) then you need to recompute ImageToProbe calibration matrix.</p>

---

## Post #5 by @vgonzalezd (2019-08-09 13:01 UTC)

<p>First of all, thank you Andras for your answer and help.<br>
<strong>I want to “Transfert images and tracking data from other software to slicer”.</strong><br>
I tried to reconstruct the volume with <strong>data of tracking</strong> and <strong>images</strong> obtained with other software. So I am building by myself the “.mha” file, because I am sure slicer is what I am looking for, but the reference systems are making me crazy.</p>
<p><strong>Problem with the reference axes LPS, RAS, IJK and MF- UF</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a6b61557960f925caa104d862b620f4598cbf78.png" alt="image" data-base62-sha1="jKvX1laQ92VnczsgbSIBXju1JkQ" width="362" height="284"></p>
<p>If PLUS algorithm works in <strong>RAS</strong> system, why it asks for an ‘UltrasoundImageOrientation = <strong>MF</strong> '? If I do not add this line on the mha file, it says during reconstruction with PLUS:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c8533801bb28558b2bf275a6eb8bb11a6df8ff3.png" data-download-href="/uploads/short-url/fu0WPYQvHqcG0glAXHV9uQaqkGD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c8533801bb28558b2bf275a6eb8bb11a6df8ff3_2_690x36.png" alt="image" data-base62-sha1="fu0WPYQvHqcG0glAXHV9uQaqkGD" width="690" height="36" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c8533801bb28558b2bf275a6eb8bb11a6df8ff3_2_690x36.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c8533801bb28558b2bf275a6eb8bb11a6df8ff3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c8533801bb28558b2bf275a6eb8bb11a6df8ff3.png 2x" data-dominant-color="2B1516"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">737×39 28.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li>So the question is: In the .mha file, should I see my image from the MF origin? Should I change trackingMatrices to my referenceSystem Mf? In this case I need to re-calculate calibration matrix also?, Not because it is just a relocation of the reference system, does not?</li>
</ol>
<p>Can I do it multiplying just: MatrixTracker*”MatrixReposition”*Image?</p>
<p>With MatrixReposition=[[-1,0,0, <strong>width/2</strong> ],[0,1,0,0],[0,0,1,0],[0,0,0,1]]?</p>
<ol start="2">
<li>When I have any <strong>TransformMatrix</strong> in the .xml file: where it is applied? In MF or in RAS origin?</li>
</ol>
<p>If I suppose that in PLUS the algorithm charge the image in RAS, so I have to write inversed each image in .mha file? And, with origin the bottom-Right, I applied ImageToIjkTransform=[[-1,0,0,width],[0,-1,0,height],[0,0,-1,0],[0,0,0,1]]  to change the origin.</p>
<p>MatrixTracker*” ImageToIjkTransform”*Image?</p>
<p>But I obtain images not ovelaped:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d2da12824853840506fb20ec0e46d9543b83e0f.png" alt="image" data-base62-sha1="b0KwC0K9Cc3y3kIMPwEvI14KpHh" width="525" height="222"></p>
<p>I tryed different configurations of Transforms and the best result that I have is with matrix ImageToIjkTransform=[[1,0,0,-width],[0,-1,0,-height],[0,0,1,0],[0,0,0,1]]. But it has no sense.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a0ce643a4b320d2a94976f88b536941febca07e.png" alt="image" data-base62-sha1="lYNanCybHUnALAM2hlBbTcpUQWi" width="333" height="191"></p>
<p>I thank you your help.</p>

---

## Post #6 by @Prashant_Pandey (2019-08-13 20:01 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="7247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To fix this inconsistency, either change the Plus configuration file to reconstruct in LPS coordinate system or apply this transformation matrix to the reconstructed image after you load it into Slicer:</p>
<pre><code class="lang-auto">-1 0 0 0
0 -1 0 0
0 0  -1 0
 0 0 0 1
</code></pre>
</blockquote>
</aside>
<p>Hi Andras,</p>
<p>I think the transform in Slicer for RAS to LPS would instead be</p>
<pre><code class="lang-auto">-1 0 0 0
0 -1 0 0
0 0  1 0
 0 0 0 1
</code></pre>
<p>Could you describe how to change the PLUS reconfig file to reconstruct in LPS instead of RAS? Just by including the above transform or is there an .xml property you can set?</p>

---

## Post #7 by @lassoan (2019-08-15 15:21 UTC)

<p>Yes, sorry, it was a typo (fixed it now), indeed, RAS&lt;-&gt;LPS conversion is done with a diag(-1,-1,1,1) matrix.</p>
<p>Plus can reconstruct a volume in any coordinate system you specify as the “To” coordinate system in <code>ImageToReference</code> transform (for example, if you specify <code>ImageToReference="ImageToTracker"</code> then the image will be reconstructed in <code>Tracker</code> coordinate system).</p>

---
