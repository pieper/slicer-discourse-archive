# Generate digitally reconstructed radiograph from 3DCT

**Topic ID**: 2010
**Date**: 2018-02-02
**URL**: https://discourse.slicer.org/t/generate-digitally-reconstructed-radiograph-from-3dct/2010

---

## Post #1 by @mmtg (2018-02-02 14:56 UTC)

<p>Hello again,</p>
<p>I would like to create some digitally reconstructed radiographs (DRR) in slicer from come 3DCt data that I have to compare to actual radiograph images that I have acquired. I saw one thread here:</p>
<aside class="quote" data-post="1" data-topic="976">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/langderyos/48/599_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/generate-2d-x-ray-image-from-volume-just-like-drr/976">Generate 2D X-ray image from volume, just like DRR</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I’m finding a way to generate 2D X-ray image from volume data, just like what DRR does. 
Is there any extension which can do this?Or can I do it in a python way? 
thanks 
langderyos,
  </blockquote>
</aside>

<p>that talked about how to do it. At the end, Andras suggested installing the plastimatch module for more realistic DRR generation. I did install this extension (well I installed slicerRT which contains the plastimatch module) but I didn’t see the option anywhere to create a DRR.</p>
<p>Ideally I want to create a DRR at a specified angle and then export it out to matlab (or use the matlab bridge). Any help would be appreciated thanks. Sorry if I missed something obvious</p>

---

## Post #2 by @lassoan (2018-02-04 14:21 UTC)

<p>I think Plastimatch DRR generator is not bundled with SlicerRT, so you need to download &amp; install Plastimatch separately and run the tool from the command line. See details in <a href="http://www.plastimatch.org/drr.html">Plastimatch documentation</a>.</p>

---

## Post #3 by @Amir_Zolal (2021-01-05 17:43 UTC)

<p>To extend this question or make it more useful as reference, is there a possibility that I could get the plastimatch drr options normal vector,  vup vector and isocenter from the 3D view in Slicer? Meaning I have volume rendering and the desired projection set up in slicer, get these values and create a shot from my volume with command line drr?</p>
<p>That would be extraordinarily useful. I think the information has to be there (in the 3d view settings). Implementing a simple drr shot module based on the command line could be a child’s play. Can you give me a hint where to find the information? Python is no problem.</p>

---

## Post #4 by @Amir_Zolal (2021-01-05 18:54 UTC)

<p>After more research, I found this:</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/lancelevine/SlicerDRRGenerator" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/10343849?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/lancelevine/SlicerDRRGenerator" target="_blank" rel="noopener nofollow ugc">lancelevine/SlicerDRRGenerator</a></h3>


  <p><span class="label1">A 3D Slicer extension that generates Digitally Reconstructed Radiographs</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>so this is already possible.</p>

---

## Post #5 by @lassoan (2021-01-05 21:56 UTC)

<p>There was some discussion of this in SlicerRT. Maybe a DRR module was added to SlicerRT already.</p>
<p>What kind of DRR would you like to generate and for what purpose?</p>

---

## Post #6 by @Mik (2021-01-06 05:17 UTC)

<p>Greetings,</p>
<p>Platimatch single image mode DRR calculation has been added recently into SlicerRT. See modules  <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Docs/user_guide/modules/drr.md" rel="noopener nofollow ugc">description</a>. It is highly recommended to use loadable module “DRR Image Computation”, and create RTBeam in “External Beam Planning” module beforehand to use gantry and patient support rotation angles correctly. SlicerRT <a href="https://github.com/SlicerRt/SlicerRT/issues/11" rel="noopener nofollow ugc">issue</a>.</p>

---

## Post #7 by @Amir_Zolal (2021-01-16 16:42 UTC)

<p>Thanks, I will be trying to create DRRs of pelvic anatomy in various projections, hopefully I can get simulated screws in -&gt; convert to label and add to the base CT image, that way possibly I will have a screw like opacity in the DRR.</p>
<p>Thanks very much for the information about SlicerRT, I was not able to get the extension I linked above to work (some VTK error / mismatch with float volume being loaded where short was expected, did not look into it really).</p>

---

## Post #8 by @Mik (2021-01-16 17:46 UTC)

<p>Module is expecting CT volume pixel type as Hounsfield Units aka short type. Can you recast your CT volume from float type into short type (for example using itk::CastImageFilter)?</p>
<p>You can use SlicerRtData for testing (<a href="https://github.com/SlicerRt/SlicerRtData/tree/master/eclipse-8.1.20-phantom-prostate" class="inline-onebox" rel="noopener nofollow ugc">SlicerRtData/eclipse-8.1.20-phantom-prostate at master · SlicerRt/SlicerRtData · GitHub</a>).</p>

---

## Post #9 by @lassoan (2021-01-16 18:46 UTC)

<aside class="quote no-group" data-username="Mik" data-post="8" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>Can you recast your CT volume from float type into short type (for example using itk::CastImageFilter)?</p>
</blockquote>
</aside>
<p>In Slicer it is available in “Cast scalar volume” module and in Simple Filters module.</p>

---

## Post #10 by @Amir_Zolal (2021-01-16 22:24 UTC)

<p>So just to clarify:<br>
The extension that did not work for me was this one: [lancelevine/SlicerDRRGenerator ]</p>
<p>I think it has nothing to do with SlicerRT DRR generation. And I did try to use a short image (ConvertImage from ANTs, but that did not work, now I see the file i generated is INT32 … weird). I gave up on that extension, and started experimenting with SlicerRT, now it has DRR.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a8b2681dad2bb4074adea9bf50f819ca0dade04.jpeg" data-download-href="/uploads/short-url/8lTOWydzZ51scp7Eq5PvbIcsJvK.jpeg?dl=1" title="Screenshot_8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a8b2681dad2bb4074adea9bf50f819ca0dade04_2_585x500.jpeg" alt="Screenshot_8" data-base62-sha1="8lTOWydzZ51scp7Eq5PvbIcsJvK" width="585" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a8b2681dad2bb4074adea9bf50f819ca0dade04_2_585x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a8b2681dad2bb4074adea9bf50f819ca0dade04.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a8b2681dad2bb4074adea9bf50f819ca0dade04.jpeg 2x" data-dominant-color="AEB8C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_8</span><span class="informations">739×631 70.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But I think I need help with that, see the attached screenshot. I try to align the beam with the screw (actually, with the line between posterior superior iliac spine and the anterior inferior iliac spine, to get the teardrop view, with the screw in the middle), but somehow the geometry of the DRR created is completely detached from the beam. Is the beam not the source for the vector for DRR generation?</p>
<p>And, I will repeat my question, I would actually like to get the vector from the 3D view only, without setting up the beam, to use on command line, can I get the vector somewhere using the python interactor?</p>

---

## Post #11 by @lassoan (2021-01-17 02:15 UTC)

<p>The volume renderer can directly generate DRR:</p>
<ul>
<li>Choose CT-X-Ray preset</li>
<li>Set 3D view background to black</li>
<li>Optional: tune Advanced / Volume properties / Scalar opacity mapping function as needed</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/288ac7d00673ee08bf611b65af7db77b4901e90b.jpeg" data-download-href="/uploads/short-url/5MEqX0HOj4hLfxAN8on8ruKY8or.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/288ac7d00673ee08bf611b65af7db77b4901e90b_2_451x499.jpeg" alt="image" data-base62-sha1="5MEqX0HOj4hLfxAN8on8ruKY8or" width="451" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/288ac7d00673ee08bf611b65af7db77b4901e90b_2_451x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/288ac7d00673ee08bf611b65af7db77b4901e90b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/288ac7d00673ee08bf611b65af7db77b4901e90b.jpeg 2x" data-dominant-color="555659"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">549×608 36.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The advantage of using the volume renderer for this is that the DRR generation is real-time (hundreds of frames per second if you use a good GPU; but even on an ultrabook without discrete GPU you get 8-10 images per second).</p>
<p>The most suitable method depends on what you are trying to achieve.<br>
What is your overall goal?<br>
What will you use the DRR for - generate image for 2D/3D image registration, training data for a volume reconstructor CNN, …?</p>

---

## Post #12 by @Mik (2021-01-17 07:00 UTC)

<aside class="quote no-group" data-username="Amir_Zolal" data-post="10" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amir_zolal/48/9423_2.png" class="avatar"> Amir_Zolal:</div>
<blockquote>
<p>but somehow the geometry of the DRR created is completely detached from the beam. Is the beam not the source for the vector for DRR generation?</p>
</blockquote>
</aside>
<p>Beam vector in SlicerRT defined by two points: isocenter and source-axis distance and beam transformation. You can set required isocenter position in “External Beam Planning” module.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9e20e87905b7b8a0189dec3503cfc6bce670c2f.png" alt="image" data-base62-sha1="v5tVZSMrlRQ0NUGO9s2N4uWtSR9" width="618" height="472">.</p>
<p>Beam transformation can be changed by clicking the “Edit” button on beam node<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8128ef002ef2c20b0b93d22a10a83cb2bd03c9c3.png" alt="image" data-base62-sha1="iqBicgCrWcOGqhrIy71aspXBYTp" width="622" height="467">.</p>
<blockquote>
<p>I would actually like to get the vector from the 3D view only, without setting up the beam</p>
</blockquote>
<p>There is no such feature (not yet) in DRR calculation in SlicerRT. May be later.</p>

---

## Post #13 by @Amir_Zolal (2021-01-17 07:16 UTC)

<p>Hi Mikhail, thanks for the answer. As you can see from the screenshot, the isocenter was set at the screw head and I edited the beam to come from the screw direction. The geometry of the DRR did not correspond to this direction.  Please look at the screenshots. You see that the image actually lands outside of the beam, and there is not so much IN the beam.  I do not know if it supposed to work like that. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa1d3d86d23d85909c02dfb39b6fd2e9bccef812.png" data-download-href="/uploads/short-url/zGC0UGYAqS8e2FrKGHZhHUG2DM6.png?dl=1" title="Screenshot_10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa1d3d86d23d85909c02dfb39b6fd2e9bccef812_2_690x386.png" alt="Screenshot_10" data-base62-sha1="zGC0UGYAqS8e2FrKGHZhHUG2DM6" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa1d3d86d23d85909c02dfb39b6fd2e9bccef812_2_690x386.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa1d3d86d23d85909c02dfb39b6fd2e9bccef812_2_1035x579.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa1d3d86d23d85909c02dfb39b6fd2e9bccef812_2_1380x772.png 2x" data-dominant-color="99A6C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_10</span><span class="informations">3695×2070 94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Andras&gt; thanks for the suggestion, this will probably be the easiest way to achieve what I want, which is just illustration of the screw trajectories in spinopelvic fixation.</p>
<p>Amir</p>

---

## Post #14 by @Mik (2021-01-17 09:08 UTC)

<aside class="quote no-group" data-username="Amir_Zolal" data-post="13" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amir_zolal/48/9423_2.png" class="avatar"> Amir_Zolal:</div>
<blockquote>
<p>The geometry of the DRR did not correspond to this direction. Please look at the screenshots. You see that the image actually lands outside of the beam, and there is not so much IN the beam. I do not know if it supposed to work like that.</p>
</blockquote>
</aside>
<p>Do you mean the image is just bigger than beam jaws, or there is misalignment between DRR image center and the projection of the screw head on the image?</p>
<p>If the latter then it’s a bug (because i have only tested module with DICOM CT data). Can you share your data and describe parameters of the beam with the position of isocenter?</p>

---

## Post #15 by @Moeka_Chan (2021-01-18 22:49 UTC)

<p>Hmmm… How to install it…? Using Extension Wizard?</p>

---

## Post #16 by @Moeka_Chan (2021-01-19 20:15 UTC)

<p>Hello,<br>
I want to create DRR image from CT scan.<br>
I found <a href="https://github.com/lancelevine/SlicerDRRGenerator" rel="noopener nofollow ugc">SlicerDRRGenerator</a>, but I don’t know how to install it to Slicer…<br>
I used the Extension Wizard. The extension is not fully installed. The GUI differs from the one in the published paper by the developer.<br>
If the extension is not working, is there any method to create DRR?<br>
Thanks.</p>

---

## Post #17 by @lassoan (2021-01-19 20:33 UTC)

<aside class="quote no-group" data-username="Moeka_Chan" data-post="16" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moeka_chan/48/3388_2.png" class="avatar"> Moeka_Chan:</div>
<blockquote>
<p>I used the Extension Wizard</p>
</blockquote>
</aside>
<p>You can install extensions using Extensions Manager.</p>
<aside class="quote no-group" data-username="Moeka_Chan" data-post="16" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moeka_chan/48/3388_2.png" class="avatar"> Moeka_Chan:</div>
<blockquote>
<p>is there any method to create DRR?</p>
</blockquote>
</aside>
<p>There are several methods, they have all pros and cons, so you can choose the one that best fits your needs:</p>
<ul>
<li>Using volume rendering module: magnitudes faster than any other methods, projection is set up by the 3D view’s camera, you can control properties of the X-ray, materials, and processing in the imaging system using a transfer function</li>
<li>SlicerRT: new DRR module in SlicerRT, projection parameters are set up using beams, see above for details</li>
<li>Thick slab reformatting using “mean” slab mode: projection parameters uses slice position and normal, can only compute parallel projection, see <a href="https://discourse.slicer.org/t/generate-2d-x-ray-image-from-volume-just-like-drr/976">topic</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections">script</a> for details</li>
<li>SlicerDRR generator: I don’t know much about this one, you need to contact the author if you have any questions</li>
</ul>

---

## Post #19 by @Moeka_Chan (2021-01-19 21:11 UTC)

<p>I didn’t find the module in Extensions Manager at the beginning…<br>
I spent time learning how to install it via source code…<br>
I found it just now…<br>
Thank you.</p>

---

## Post #20 by @suzume (2022-09-27 09:25 UTC)

<p>Hi, I have tried the DRR Generator tool, but there is always showing the error. Do you know how to deal with it?<br>
The error message is below：<br>
" The message detail is:</p>
<p>Exception thrown in event: /Volumes/D/S/S-0-build/ITK/Modules/IO/NRRD/src/itkNrrdImageIO.cxx:1118:</p>
<p>ITK ERROR: NrrdImageIO(0x7f96ce8fbee0): Write: Error writing output_fixed.nrrd:</p>
<p>[nrrd] nrrdSave: couldn’t fopen(“output_fixed.nrrd”,“wb”): Read-only file system"</p>
<p>Wish for your reply!</p>

---

## Post #21 by @fieldr4 (2022-11-29 14:49 UTC)

<p>Hi Mik,</p>
<p>I am running into the same issue that Amir encountered. The DRR doesn’t match the rendering of the beam in the 3D view.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9187ba52dd4d9eb4830c0546300f27d28ee6233d.png" alt="Screenshot" data-base62-sha1="kLq1MuiemDAwcT04DQ1UOCWU16B" width="524" height="402"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18a6298aa9f7e6c68a3a62767d75a467f7058833.png" alt="Screenshot 2" data-base62-sha1="3w3sxsoS4OEcitC5cQu1H2e06SD" width="524" height="402"></p>
<p>I am using file 629 from the VerSe 2020 data set, which is accessible through this link. <a href="https://github.com/anjany/verse/blob/main/README.md" class="inline-onebox" rel="noopener nofollow ugc">verse/README.md at main · anjany/verse · GitHub</a></p>
<p>Here is a screenshot of an .mha export of the DRR in ImageJ.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d56c996bb8c8b37490b9b87b8cd7e634bdeb6d9e.jpeg" data-download-href="/uploads/short-url/us2ncaiQv4T3WBkbzRkhxEozuB8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d56c996bb8c8b37490b9b87b8cd7e634bdeb6d9e_2_473x499.jpeg" alt="image" data-base62-sha1="us2ncaiQv4T3WBkbzRkhxEozuB8" width="473" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d56c996bb8c8b37490b9b87b8cd7e634bdeb6d9e_2_473x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d56c996bb8c8b37490b9b87b8cd7e634bdeb6d9e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d56c996bb8c8b37490b9b87b8cd7e634bdeb6d9e.jpeg 2x" data-dominant-color="121212"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×710 22.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The isocenter of the beam is positioned at L3 and I verified that the coordinates are correct.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfb7efd782d566f6069f6c9dc746ccd8e070c45d.jpeg" alt="image" data-base62-sha1="tDyUZVoZsLrPpNsGJsRA4iq2kIl" width="561" height="449"></p>
<p>Here are the beam parameters<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fbea6025bf774658ecc297aa145b4b1a3b05999.png" alt="image" data-base62-sha1="bnsbk3iWPFgIhVJrmsXl2BgGPnH" width="560" height="399"></p>
<p>And here is the read only Plastimatch command arguments shown in the <code>DRR Image Computation</code> module<br>
plastimatch drr -A cpu <br>
–nrm “1 -3.44509e-16 -1.22465e-16” <br>
–vup “-3.44509e-16 -1 2.22045e-16” <br>
–sad 1120.71 --sid 1411.71 <br>
-r “2000 2000” <br>
-z “500 500” <br>
-c “999.5 999.5” <br>
-o “-2 -227 -1190” <br>
-e --autoscale --autoscale-range “0 255” <br>
-i uniform -P preprocess -O Out -t raw</p>

---

## Post #22 by @Mik (2022-11-29 15:03 UTC)

<p>Which dataset: training, validation, test?</p>

---

## Post #23 by @fieldr4 (2022-11-29 15:10 UTC)

<p>VerSe 2020 &gt; 03_test &gt; verse 563.nii</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36f544253c5cf91b1aeb8eee0b0552e0d1d00d38.jpeg" data-download-href="/uploads/short-url/7Qbgm2Q0zOQe6cKUx6n2yycMGRW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f544253c5cf91b1aeb8eee0b0552e0d1d00d38_2_573x500.jpeg" alt="image" data-base62-sha1="7Qbgm2Q0zOQe6cKUx6n2yycMGRW" width="573" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f544253c5cf91b1aeb8eee0b0552e0d1d00d38_2_573x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36f544253c5cf91b1aeb8eee0b0552e0d1d00d38.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36f544253c5cf91b1aeb8eee0b0552e0d1d00d38.jpeg 2x" data-dominant-color="E9EBEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">789×688 66.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I incorrectly said 629 in my last post. It is actually 563</p>

---

## Post #24 by @Mik (2022-11-30 03:57 UTC)

<p>Such misalignment is because of CT has internal matrix orientation.<br>
Quick fix is to set matrix transform manually, by python script in python console.<br>
The GUI fix will require a much more time.</p>
<pre><code class="lang-python">mat = vtk.vtkMatrix4x4()
mat.SetElement(0, 0, -1.)
mat.SetElement(1, 1, -1.)
ct = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
ct.SetIJKToRASMatrix(mat)
</code></pre>

---

## Post #25 by @fieldr4 (2022-11-30 04:34 UTC)

<p>Thanks! That worked like a charm. Is there any reason why I shouldn’t use this for all CT volumes that I import into Slicer?</p>
<p>Will manually setting the matrix transform have any impact on the coordinates of Control Points in the <code>Markup</code> module?</p>

---

## Post #26 by @Mik (2022-11-30 04:44 UTC)

<p>I must be fixed within DRR module. Points should be OK, since points coordinates are transformed into world coordinates, but it must be checked.</p>

---

## Post #27 by @Mik (2022-11-30 14:23 UTC)

<p>Also try to use that transform to the ct volume. You can check original volume transform in “Volumes” module, “Volume Information” subsection.</p>
<pre><code class="lang-python">mat = vtk.vtkMatrix4x4()
mat.SetElement(0, 0, -1.)
mat.SetElement(1, 1, -1.)
ct = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
ct.SetIJKToRASDirectionMatrix(ct)
</code></pre>

---

## Post #28 by @fieldr4 (2022-11-30 23:01 UTC)

<p>Is it possible to apply this to a new volume created from a CT? I created a smaller volume using the <code>Crop Volume</code> module on the transformed CT, but the DRR did not work on the cropped volume. The DRR was successful when I tried it on the transformed CT.</p>

---

## Post #29 by @lassoan (2022-12-01 01:35 UTC)

<p>The misalignment is due to that Plastimatch’s DRR generation tool assumes an “LPS oriented volume”, i.e., an image with an IJK to LPS direction matrix like this:</p>
<pre><code class="lang-auto">[ spacingX      0         0      0 ]
[     0      spacingY     0      0 ]
[     0         0     spacingZ   0 ]
[     0         0         0      1 ]
</code></pre>
<p>but of course it is often not the case - image coordinate system axes can be arbitrarily rotated in space.</p>
<p>It should be straightforward to support arbitrarily oriented images.  One simple solution is to compute a transform that transforms the image so that its IJK axes are oriented in LPS directions, then apply this transform both to the image and the camera position and orientation.</p>

---

## Post #30 by @Mik (2022-12-01 13:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="29" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It should be straightforward to support arbitrarily oriented images. One simple solution is to compute a transform that transforms the image so that its IJK axes are oriented in LPS directions, then apply this transform both to the image and the camera position and orientation.</p>
</blockquote>
</aside>
<p>I will add support of oriented volumes later.</p>

---

## Post #31 by @gcsharp (2022-12-01 18:25 UTC)

<p>Ideally this should be fixed upstream.  (As well as using IEC to specify gantry angle, etc…)</p>

---

## Post #32 by @Mik (2022-12-02 06:21 UTC)

<p>In that case the ct volume orientation must be taken into account by the beam node, because beam node already use IEC Logic and angles to calculate beam orientation.</p>

---

## Post #33 by @fieldr4 (2022-12-05 22:36 UTC)

<p>Hi Mik, Andras, and Greg,</p>
<p>I am still struggling with this. I can use the code that Mik shared:</p>
<aside class="quote no-group" data-username="Mik" data-post="24" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<pre><code class="lang-auto">mat = vtk.vtkMatrix4x4()
mat.SetElement(0, 0, -1.)
mat.SetElement(1, 1, -1.)
ct = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
ct.SetIJKToRASMatrix(mat)
</code></pre>
</blockquote>
</aside>
<p>to “correct” a CT volume such that the isocenter coordinates that I enter into the <code>External Beam Planning</code> module are in the center of a DRR created by the <code>DRR Image Computation</code> module. If I don’t apply the code snipped above, then the isocenter (and all patient anatomy) may be missing from the resulting DRR.</p>
<p>The reason that I still have a problem is that I need to create DRRs from cropped volumes created by the <code>Crop Volume</code> module. Cropping the original CT allows me to remove soft tissues that cause poor contrast in DRRs. The trouble is that the cropped volume isn’t “corrected” by the code snippet above. When I create a DRR from the cropped volume using isocenter coordinates that work on the un-cropped CT, there is no patient anatomy in the field of view.</p>
<p>Is there a quick fix that I could apply while this bug is sorted out?</p>
<p><a class="mention" href="/u/gcsharp">@gcsharp</a> I asked a question about this in the Plastimatch Google group last week. I have been alternating between Slicer and the Plastimatch Command prompt to figure out which is ideal for my use case.</p>

---

## Post #34 by @lassoan (2022-12-06 15:46 UTC)

<p>You can apply a transform to the volume that preserves image spacing but rotates its axis to be aligned with LPS axes. You can find computation of a similar transform here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/gaoyi/SlicerBigImage/blob/08a898fe7a40338ed4e6f4566f27153e012ff1e9/NgffImageIO/NgffImageIO.py#L108-L113">
  <header class="source">

      <a href="https://github.com/gaoyi/SlicerBigImage/blob/08a898fe7a40338ed4e6f4566f27153e012ff1e9/NgffImageIO/NgffImageIO.py#L108-L113" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/gaoyi/SlicerBigImage/blob/08a898fe7a40338ed4e6f4566f27153e012ff1e9/NgffImageIO/NgffImageIO.py#L108-L113" target="_blank" rel="noopener">gaoyi/SlicerBigImage/blob/08a898fe7a40338ed4e6f4566f27153e012ff1e9/NgffImageIO/NgffImageIO.py#L108-L113</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="108" style="counter-reset: li-counter 107 ;">
          <li>ijkToRasMatrixVtk = vtk.vtkMatrix4x4()</li>
          <li>volumeNode.GetIJKToRASMatrix(ijkToRasMatrixVtk)</li>
          <li>ijkToRasMatrix = slicer.util.arrayFromVTKMatrix(ijkToRasMatrixVtk)</li>
          <li>ijkToLpsMatrix = np.dot(ijkToRasMatrix, np.diag([-1.0, -1.0, 1.0, 1.0]))</li>
          <li>xyzToIjkMatrix = np.diag([1.0/spacing[0], 1.0/spacing[1], 1.0/spacing[2], 1.0])</li>
          <li>xyzToLpsMatrix = np.dot(ijkToLpsMatrix, xyzToIjkMatrix)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #35 by @fieldr4 (2022-12-07 16:05 UTC)

<p>Thank you for sharing this. What is the syntax for selecting a DataNode for this transformation?</p>
<p>When I copy the code above into Slicer’s the Python terminal, I receive a NameError code that the volumeNode is not identified. I’m not sure if the way that volumeNode is defined in NgffImageIO is relevant (line 345) .</p>
<p>I would like to apply it to “563_cropped” in the scene shown below. Generally, I would like to know how to apply it to any volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8477f1a8ab2dba6f6a0c75169c273fb8586491c9.jpeg" data-download-href="/uploads/short-url/iTS0iNGxV9cqcTh0BA3rZ7PJZ4R.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8477f1a8ab2dba6f6a0c75169c273fb8586491c9_2_349x500.jpeg" alt="image" data-base62-sha1="iTS0iNGxV9cqcTh0BA3rZ7PJZ4R" width="349" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8477f1a8ab2dba6f6a0c75169c273fb8586491c9_2_349x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8477f1a8ab2dba6f6a0c75169c273fb8586491c9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8477f1a8ab2dba6f6a0c75169c273fb8586491c9.jpeg 2x" data-dominant-color="EAECEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">502×718 64.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #36 by @lassoan (2022-12-08 03:28 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="35" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>What is the syntax for selecting a DataNode for this transformation?</p>
</blockquote>
</aside>
<p>During debugging, you can get a node in the Python console like this:</p>
<pre><code>volumeNode = getNode('563_cropped')
</code></pre>
<p>In a Slicer module you would use a node selector widget to let the user choose a node.</p>

---

## Post #37 by @fieldr4 (2022-12-08 04:07 UTC)

<p>I was able to execute the code snippet with some modifications, but it did not solve my original problem.</p>
<p>Here is the code that ran:</p>
<pre><code class="lang-auto">import numpy as np
volumeNode = getNode('563_cropped')
spacing = volumeNode.GetSpacing()
ijkToRasMatrixVtk = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(ijkToRasMatrixVtk)
ijkToRasMatrix = slicer.util.arrayFromVTKMatrix(ijkToRasMatrixVtk)
ijkToLpsMatrix = np.dot(ijkToRasMatrix, np.diag([-1.0, -1.0, 1.0, 1.0]))
xyzToIjkMatrix = np.diag([1.0/spacing[0], 1.0/spacing[1], 1.0/spacing[2], 1.0])
xyzToLpsMatrix = np.dot(ijkToLpsMatrix, xyzToIjkMatrix)
</code></pre>
<p>However, the isocenter that I selected in the <code>External Beam Planning</code> module was absent from a DRR calculated in the <code>DRR Image Computation</code> module. Here is a screenshot of the full view. Note the mismatch between the 3D rendering and the DRR in the 3D View.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b43b517c987f6fb818f8a38c988bcbf98e3f9578.jpeg" data-download-href="/uploads/short-url/pIp252hvjvT4sErjhFxBQcbH4RW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b43b517c987f6fb818f8a38c988bcbf98e3f9578_2_690x380.jpeg" alt="image" data-base62-sha1="pIp252hvjvT4sErjhFxBQcbH4RW" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b43b517c987f6fb818f8a38c988bcbf98e3f9578_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b43b517c987f6fb818f8a38c988bcbf98e3f9578_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b43b517c987f6fb818f8a38c988bcbf98e3f9578_2_1380x760.jpeg 2x" data-dominant-color="8C8B8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1060 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here is a screenshot of the resulting DRR.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ea7d2355fadffdb500fc4adbdae14cf486116ec.jpeg" data-download-href="/uploads/short-url/25EeRnqk3Jn50IC1EIGrsyz2otC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ea7d2355fadffdb500fc4adbdae14cf486116ec_2_471x499.jpeg" alt="image" data-base62-sha1="25EeRnqk3Jn50IC1EIGrsyz2otC" width="471" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ea7d2355fadffdb500fc4adbdae14cf486116ec_2_471x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ea7d2355fadffdb500fc4adbdae14cf486116ec_2_706x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ea7d2355fadffdb500fc4adbdae14cf486116ec_2_942x998.jpeg 2x" data-dominant-color="2B2B2B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1340×1420 93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I check that the transform was applied to 563_cropped? Is there anything else that could be causing this misalignment?</p>
<p>Thank you for all of your help!</p>

---

## Post #38 by @fieldr4 (2022-12-08 18:54 UTC)

<p>Hi Mik, have you made any progress on adding support of oriented volumes?</p>
<p>Andras recommended a workaround that isn’t yet functional. See my last post.</p>

---

## Post #39 by @fieldr4 (2022-12-09 14:47 UTC)

<p>Hi Andras, do you have any recommendations for determining whether the LPS transformation was applied to the cropped volume? See my reply to your post on 12/7.</p>
<p>I am not sure if my problem is there or if it is in the <code>DRR Image Generation</code> module.</p>

---

## Post #40 by @Mik (2022-12-09 16:08 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="38" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Hi Mik, have you made any progress on adding support of oriented volumes?</p>
</blockquote>
</aside>
<p>Not yet.</p>
<p>In case of applying transform to cropped volume:</p>
<ul>
<li>Create a transform node RAS-&gt;LPS (matrix you know) in <code>Transforms</code> module;</li>
<li>Apply a newly created transform node to cropped volume and markups that within the cropped volume;</li>
<li>After that you must harder the transform for the cropped volume and markups.<br>
That gives you a cropped volume orientated as default DICOM volume.</li>
</ul>

---

## Post #41 by @fieldr4 (2022-12-09 16:43 UTC)

<p>That worked and solved all of my issues as far as I can tell! Thank you!</p>
<p>Minor question on <code>DRR Image Generation</code> module: How can I control the  Plastimatch parameters <code>vup</code> (panel orientation)? I need to rotate the resulting DRR by 90 degrees.</p>

---

## Post #42 by @Mik (2022-12-10 07:49 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="41" data-topic="2010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>How can I control the Plastimatch parameters <code>vup</code> (panel orientation)?</p>
</blockquote>
</aside>
<p>You can’t. The view-up vector is hard-coded. You can transpose image matrix in any external image editor.</p>

---

## Post #43 by @lassoan (2022-12-10 15:08 UTC)

<p>You can rotate the input volume by 90 degrees by applying a transform.</p>

---

## Post #44 by @fieldr4 (2022-12-11 15:26 UTC)

<p>Thank you, Mik and Andras.</p>

---
