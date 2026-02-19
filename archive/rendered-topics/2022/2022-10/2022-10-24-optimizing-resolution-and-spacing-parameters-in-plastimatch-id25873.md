---
topic_id: 25873
title: "Optimizing Resolution And Spacing Parameters In Plastimatch"
date: 2022-10-24
url: https://discourse.slicer.org/t/25873
---

# Optimizing resolution and spacing parameters in Plastimatch DRR

**Topic ID**: 25873
**Date**: 2022-10-24
**URL**: https://discourse.slicer.org/t/optimizing-resolution-and-spacing-parameters-in-plastimatch-drr/25873

---

## Post #1 by @fieldr4 (2022-10-24 19:45 UTC)

<p>Hi,</p>
<p>I am using Plastimatch DRR module within the SlicerRT extension to create synthetic lateral x-rays from a CT volume. I am trying to produce DRRs with the clearest vertebral margins (minimizing blur due to pixelation and banding artifacts) and I can’t find documentation of the “Spacing” parameter within the “Imager and Image” parameters in Plastmatch materials or 3D Slicer.</p>
<p>I have played around with the “Resolution” and “Spacing” parameters, but I don’t understand the relationship between them. At low values of both, the DRR doesn’t capture enough of the anatomy around the isocenter position and it is pixelated with significant banding artifacts.</p>
<p>Resolution = 120, 120; Spacing = 1, 1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8687338d6b4313c05201bf04ead20e86a2763a70.jpeg" data-download-href="/uploads/short-url/jc5EdqkESEWM2e5Yqmc69egooOQ.jpeg?dl=1" title="120, 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/8687338d6b4313c05201bf04ead20e86a2763a70_2_690x354.jpeg" alt="120, 1" data-base62-sha1="jc5EdqkESEWM2e5Yqmc69egooOQ" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/8687338d6b4313c05201bf04ead20e86a2763a70_2_690x354.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/8687338d6b4313c05201bf04ead20e86a2763a70_2_1035x531.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/8687338d6b4313c05201bf04ead20e86a2763a70_2_1380x708.jpeg 2x" data-dominant-color="ABADAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">120, 1</span><span class="informations">1920×987 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>At high values of both, the banding artifacts appear to be absent, but the image is very blurry.</p>
<p>Resolution = 400, 400; Spacing = 8,8<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c132b9fa92377b83e048cda293e5994cf3bc768.jpeg" data-download-href="/uploads/short-url/d8wZYMOTE2by6Qz9iJtYWtgVBUI.jpeg?dl=1" title="400, 8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c132b9fa92377b83e048cda293e5994cf3bc768_2_690x350.jpeg" alt="400, 8" data-base62-sha1="d8wZYMOTE2by6Qz9iJtYWtgVBUI" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c132b9fa92377b83e048cda293e5994cf3bc768_2_690x350.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c132b9fa92377b83e048cda293e5994cf3bc768_2_1035x525.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c132b9fa92377b83e048cda293e5994cf3bc768_2_1380x700.jpeg 2x" data-dominant-color="B0B2B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">400, 8</span><span class="informations">1920×974 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I find a balance between these two parameters to achieve the highest image quality?</p>

---

## Post #2 by @lassoan (2022-10-24 21:02 UTC)

<p><strong>Resolution</strong> is the number of rows and columns in the detector. You probably want to have it at about 2000 to be realistic.</p>
<p><strong>Spacing</strong> value refers to the detector pixel size. A realistic value is about 0.1-0.2 mm.</p>

---

## Post #3 by @fieldr4 (2022-10-25 02:20 UTC)

<p>Hi Andras,</p>
<p>Thank you for the prompt and informative response. I applied the settings that you recommended (Resolution = 2000, Spacing = 0.2mm) and the resulting DRR has some banding artifacts. See area around the navel.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c4f3534a32d062bb4be38719eb1b4260a68068a.jpeg" data-download-href="/uploads/short-url/fs9gFjdkwB3pb7OfRCcd74pfxG2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c4f3534a32d062bb4be38719eb1b4260a68068a_2_690x343.jpeg" alt="image" data-base62-sha1="fs9gFjdkwB3pb7OfRCcd74pfxG2" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c4f3534a32d062bb4be38719eb1b4260a68068a_2_690x343.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c4f3534a32d062bb4be38719eb1b4260a68068a_2_1035x514.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c4f3534a32d062bb4be38719eb1b4260a68068a_2_1380x686.jpeg 2x" data-dominant-color="AEB0B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×955 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there a combination of resolution/spacing that would result in the clearest margins of the vertebral bodies, not taking into account practicality?</p>
<p>I believe that I can achieve clearer visualization of the spine by cropping out the surrounding tissues and adjusting the SAD/SID. Before attempting those two avenues, I wanted to optimize resolution and spacing as much as possible.</p>
<p>Thanks,<br>
Andrew</p>

---

## Post #4 by @lassoan (2022-10-25 03:11 UTC)

<p>I always use the volume renderer for DRR generation. It is blazing fast (you can render 100+ images per second with a good GPU), by adjusting the cropping ROI and editing the transfer functions you can get very good contrast for the bones. Use the <code>CT-X-ray</code> volume rendering preset and set the view background to black. I find that the image appearance overall is quite to an X-ray or fluoroscopy image.</p>

---

## Post #5 by @fieldr4 (2022-10-25 03:32 UTC)

<p>Thank you for another quick reply.</p>
<p>I have used the CT-X-ray volume rendering for demonstrations, but I am not sure if it will meet my ultimate goal. I am trying to create a simulated XR (PNG, JPEG, or DICOM) in which the pixel coordinates of certain predetermined anatomic landmarks are known. To do this, I am marking the anatomic landmarks and the isocenter for the DRR on a CT or MHA in the Markup module. Then, I am calculating the distance between the isocenter and each of the coordinates in RAS and mapping those distances to the DRR using the center of the DRR as a reference.</p>
<p>Is there a better way of generating a simulated lateral x-ray in which the pixel coordinates of certain anatomic landmarks are known?</p>

---

## Post #6 by @lassoan (2022-10-25 03:45 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="5" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Is there a better way of generating a simulated lateral x-ray in which the pixel coordinates of certain anatomic landmarks are known?</p>
</blockquote>
</aside>
<p>Volume rendering is perfect for this. You know the pixel coordinates of anatomic landmarks from the camera parameters. You can even make the landmarks appear in the DRR by enabling <code>Occluded visibility</code> in Markup module (Display / Advanced / 3D Display).</p>

---

## Post #7 by @fieldr4 (2022-10-25 13:38 UTC)

<p>That’s great. Using the “CT-X-ray” preset in the Volume Rendering module, I created a DRR in the blue window. Do you recommend using the “Screenshot” or “ScreenView” tools to create a PNG of the contents of the blue window?</p>
<p>Where can I view the camera parameters? I looked at documentation for the “Cameras” module, but that doesn’t appear to contain the information that I need.</p>

---

## Post #8 by @Mik (2022-10-26 07:19 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="3" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>I believe that I can achieve clearer visualization of the spine by cropping out the surrounding tissues and adjusting the SAD/SID. Before attempting those two avenues, I wanted to optimize resolution and spacing as much as possible.</p>
</blockquote>
</aside>
<p>You can try to increase “Threshold below” value (for example set this value to 150). Below that threshold the HU values of CT data will be set to -1000 (air), so some soft tissues can be replaced with air.</p>
<p>The DRR calculation process can be significantly upgraded, if use <a href="http://www.openrtk.org/" rel="noopener nofollow ugc">RTK</a> library for projection calculation.</p>

---

## Post #9 by @fieldr4 (2022-10-26 13:49 UTC)

<p>Thanks, Mikhail, for the suggestion. Two questions:</p>
<ol>
<li>Is there a 3D Slicer extension that offers the projection calculation capabilities that you are referencing from the RTK Library?</li>
<li>Are you aware of any RTK Library documentation that describes the process to create a DRR?</li>
</ol>

---

## Post #10 by @Mik (2022-10-26 14:43 UTC)

<ol>
<li>
<p>I don’t know, possibly not. 3D Slicer doesn’t compile ITK with RTK support.</p>
</li>
<li>
<p>Official documentation only describes classes and methods of the library in C++. I work in C++ most of the time as well. If you familiar with C++ you could look at <code>applications/rtkforwardprojections</code> directory in RTK source. CT data must be a single <code>mha</code> file and <a href="http://www.openrtk.org/Doxygen/DocGeo3D.html" rel="noopener nofollow ugc">projection geometry</a> must be setup for proper forward projection reconstruction. I can send you a C++ example, but it only for Linux.</p>
</li>
</ol>
<p>Here is some examples with python in itk:</p>
<ol>
<li><a href="https://itkpythonpackage.readthedocs.io/en/master/Quick_start_guide.html" class="inline-onebox" rel="noopener nofollow ugc">Quick start guide — ITKPythonPackage documentation</a></li>
<li><a href="https://www.mail-archive.com/rtk-users@public.kitware.com/msg00888.html" rel="noopener nofollow ugc">Creating DRR in RTK with python.</a></li>
</ol>
<p>You can also check RTK mailing-list discussions  <a href="https://www.mail-archive.com/search?l=rtk-users%40public.kitware.com&amp;q=DRR&amp;x=0&amp;y=0" rel="noopener nofollow ugc">DRR in RTK mailing-list</a></p>

---

## Post #11 by @Mik (2022-10-26 15:04 UTC)

<p>I forgot to mention that RTK can only increase calculation speed of DRR, any other features like projections of markups must be done (programmed) by the user.</p>

---

## Post #12 by @fieldr4 (2022-10-26 18:12 UTC)

<p>Thanks, Mikahil. I do not have experience working with C++ and have limited experience working in Python, so my options are constrained.</p>
<p>I will check out the Python documentation that you sent as it might be more in reach for me. I appreciate you linking the references!</p>

---

## Post #13 by @fieldr4 (2022-10-26 18:13 UTC)

<p>Hi Andras, do you have a suggestion for how to generate PNG of a DRR using the Volume Rendering module?</p>

---

## Post #14 by @lassoan (2022-10-26 19:35 UTC)

<p>You can right-click the 3D viewer, choose Copy image, then paste&amp;save it in Paint or other image viewer software. You can also do it by Python scripting as shown in these <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#screen-capture">examples</a> (hit Ctrl-3 to open the Python console and copy-paste the code snippet).</p>
<p>There are so many tools in 3D Slicer and related libraries that can generate DRRs, all with specific advantages and disadvantages. The right choice depends on what you would like to achieve. What is your end goal with the DRR generation? CT/fluoro registration? What is the target anatomy and clinical procedure?</p>

---

## Post #15 by @fieldr4 (2022-10-26 20:42 UTC)

<p>Thanks, copying the image manually makes sense.</p>
<p>The ultimate goal is to evaluate a novel method for measuring thoracolumbar endplate orientation in sagittal plane radiographs (DR, CR, and EOS). The method must be implemented in custom measurement software.</p>
<p>To accomplish this, the process that I envisioned was to create “ideal” reference points in a CT volume, then hide those points and generate a synthetic lateral XR of the spine. The synthetic lateral XR would then be imported into the custom software that I am using for making endplate measurements and my team would make measurements per the novel protocol. Finally, I would compare the known coordinates of the “ideal” reference points in the DRR to the manually-measured points placed by my team.</p>
<p>It is similar to a process described by <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9549721/" rel="noopener nofollow ugc">Hipp et al. 2022</a>  in a recent publication (pages 9 and 10). They used Plastimatch’s DRR functionality, so I thought that Plastimatch would work for my purposes. Unfortunately, the quality of the DRRs is not representative of normal lumbar x-ray. See image below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59934ecf066611e79e0caec5445f0e7bb6c55fc6.jpeg" data-download-href="/uploads/short-url/cMq6ee6HhigOnox5LKEUMMprZxs.jpeg?dl=1" title="Spine DRR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59934ecf066611e79e0caec5445f0e7bb6c55fc6_2_416x500.jpeg" alt="Spine DRR" data-base62-sha1="cMq6ee6HhigOnox5LKEUMMprZxs" width="416" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59934ecf066611e79e0caec5445f0e7bb6c55fc6_2_416x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59934ecf066611e79e0caec5445f0e7bb6c55fc6_2_624x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59934ecf066611e79e0caec5445f0e7bb6c55fc6.jpeg 2x" data-dominant-color="262626"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Spine DRR</span><span class="informations">766×920 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @lassoan (2022-10-27 02:31 UTC)

<p>I had a look at <code>DRR Generation</code> module and it creates reasonable image from the CTChest sample data set:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a8c6fe12a5870f51c29c6b825c500a8622d7b92.png" data-download-href="/uploads/short-url/64oWco8zoZXIfLccGBgp2VnVYl4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a8c6fe12a5870f51c29c6b825c500a8622d7b92_2_690x441.png" alt="image" data-base62-sha1="64oWco8zoZXIfLccGBgp2VnVYl4" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a8c6fe12a5870f51c29c6b825c500a8622d7b92_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a8c6fe12a5870f51c29c6b825c500a8622d7b92_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a8c6fe12a5870f51c29c6b825c500a8622d7b92_2_1380x882.png 2x" data-dominant-color="4F4F50"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 502 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The lateral view generated from CTChest was very soft due to the low resolution of the image. The result was nicer using CTLiver data set.</p>
<p>With “exact” exposure:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65fce129d6de5d7ebc5d0721cb2f2a125ecc71df.png" data-download-href="/uploads/short-url/eye11cn1y9MyIlEilPpxyRRrRWD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65fce129d6de5d7ebc5d0721cb2f2a125ecc71df_2_690x441.png" alt="image" data-base62-sha1="eye11cn1y9MyIlEilPpxyRRrRWD" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65fce129d6de5d7ebc5d0721cb2f2a125ecc71df_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65fce129d6de5d7ebc5d0721cb2f2a125ecc71df_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65fce129d6de5d7ebc5d0721cb2f2a125ecc71df_2_1380x882.png 2x" data-dominant-color="333334"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 423 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>With “uniform” exposure:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57806adf0112e56d4a7363007308728806f4761f.png" data-download-href="/uploads/short-url/cu4FJjH5HtdgnhUIq5eGrxmDznV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57806adf0112e56d4a7363007308728806f4761f_2_690x441.png" alt="image" data-base62-sha1="cu4FJjH5HtdgnhUIq5eGrxmDznV" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57806adf0112e56d4a7363007308728806f4761f_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57806adf0112e56d4a7363007308728806f4761f_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57806adf0112e56d4a7363007308728806f4761f_2_1380x882.png 2x" data-dominant-color="2E2D2E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 377 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @fieldr4 (2022-10-27 03:55 UTC)

<p>The “DRR Generation” module is the one that I was using in previous posts. I was able to generate a DRR of reasonable image quality by switching CT series to one with smaller “Image Spacing” (0.77, 0.77, 0.80. vs 0.85, 0.85, 1.0).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fd553a858394a831be84e7ec8316d78d8a7dd1a.jpeg" data-download-href="/uploads/short-url/mNWY2hvxFg4zkej0wU0JQPRqrcC.jpeg?dl=1" title="Spine DRR (new)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fd553a858394a831be84e7ec8316d78d8a7dd1a_2_524x500.jpeg" alt="Spine DRR (new)" data-base62-sha1="mNWY2hvxFg4zkej0wU0JQPRqrcC" width="524" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fd553a858394a831be84e7ec8316d78d8a7dd1a_2_524x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fd553a858394a831be84e7ec8316d78d8a7dd1a_2_786x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fd553a858394a831be84e7ec8316d78d8a7dd1a_2_1048x1000.jpeg 2x" data-dominant-color="D5D5D5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Spine DRR (new)</span><span class="informations">1492×1422 53.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Fortunately (or unfortunately) the lack of resolution of the CTs that I was using may have been causing my issues all along.</p>
<p>I have two questions regarding the DRR Generation module:</p>
<ol>
<li>
<p>How can I map the A and S components of the RAS coordinates of a point placed on the CT volume using the Markup module to the P,S or pixel coordinates of the DRR?</p>
<ul>
<li>The DRR isocenter is set to a known LPS coordinate in the CT (ex. approximate center of L3, [-3,-120,380])</li>
<li>Therefore the center of the resulting DRR is known in relation to the CT volume</li>
<li>If I have the A, S distance from the center of L3 in the CT volume to a landmark of interest, can I transform those values to find the coordinates of the landmark of interest in the DRR?</li>
</ul>
</li>
<li>
<p>Would you recommend exporting the DRR as a DICOM by right clicking the DRR volume in the “Data” module, selecting the “Export to DICOM” option, and checking the box for “Export to folder”? I am searching for the optimal method for exporting the DRR without compromising the relationship between the RAS coordinates of the CT volume and the pixel coordinates of the DRR.</p>
</li>
</ol>
<p>Thanks again for all of your help! The documentation and community support for 3D Slicer is exceptional.</p>

---

## Post #18 by @lassoan (2022-10-27 04:48 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="17" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>How can I map the A and S components of the RAS coordinates of a point placed on the CT volume using the Markup module to the P,S or pixel coordinates of the DRR?</p>
</blockquote>
</aside>
<p>It is a simple perspective projection. You can <a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/plastimatch/base/proj_matrix.cxx#L137">compute the projection matrix as it is done in Plastimatch</a>.</p>
<aside class="quote no-group" data-username="fieldr4" data-post="17" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Would you recommend exporting the DRR as a DICOM by right clicking the DRR volume in the “Data” module, selecting the “Export to DICOM” option, and checking the box for “Export to folder”? I am searching for the optimal method for exporting the DRR without compromising the relationship between the RAS coordinates of the CT volume and the pixel coordinates of the DRR.</p>
</blockquote>
</aside>
<p>We don’t have a DICOM exporter for DRR (or fluoro) images in Slicer. It would not be hard to add it, but it may be simpler to save the image in a research file format and the DRR parameters in custom fields or in a sidecar file. Spending time with writing a DICOM exporter script may worth it if you will process the data with software that takes advantage of all the DRR parameters stored in these DRR files or for long-term archival or sharing of the images outside your group.</p>

---

## Post #19 by @fieldr4 (2022-10-27 15:05 UTC)

<p>Great, I will dig into the Plastimatch documentation that you linked.</p>
<p>I am probably misunderstanding something, but it appears that I can create a DICOM export of the DRR using the “Data” module. This produces a .dcm file of ~8MB.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23fff513a40fdb197e595bd77c3ebcc392d6df7e.png" alt="Spine DRR export to DICOM" data-base62-sha1="58t62RiMQuVMn4NGYarhHkZvAhU" width="328" height="271"></p>
<p>Separately, how can I specify the filename for a DRR in the <code>DRR Generation</code> module when the output format is “pgm” or “pfm”? When “pgm” or “pfm” is selected, I receive the following error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f644ac75135a88a5b03007988fb14f0fa5c51355.png" data-download-href="/uploads/short-url/z8AABo3TdAlfZwQchoKqNFcowId.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f644ac75135a88a5b03007988fb14f0fa5c51355.png" alt="image" data-base62-sha1="z8AABo3TdAlfZwQchoKqNFcowId" width="690" height="131" data-dominant-color="F2E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">697×133 29.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>DRR generation standard error:</p>
<p>/Applications/Slicer.app/Contents/Extensions-30893/SlicerRT/lib/Slicer-5.0/cli-modules/plastimatch_slicer_drr: ITK exception caught !</p>
<p>itk::ExceptionObject (0x7fb01f1057c0)</p>
<p>Location: “unknown”</p>
<p>File: /Volumes/D/S/S-0-build/ITK/Modules/IO/ImageBase/include/itkImageFileWriter.hxx</p>
<p>Line: 96</p>
<p>Description: ITK ERROR: ImageFileWriter(0x7fb01f105cb0): No filename was specified</p>
</blockquote>

---

## Post #20 by @Mik (2022-10-27 15:35 UTC)

<blockquote>
<p>Separately, how can I specify the filename for a DRR in the <code>DRR Generation</code> module when the output  format is “pgm” or “pfm”</p>
</blockquote>
<p>Use only raw file format, other formats are only for internal plastimatch procedures!</p>

---

## Post #21 by @Mik (2022-10-27 15:42 UTC)

<p>Once the DRR image is generated, you can transform DRR image into UnsignedChar scalar volume, using “Cast Scalar Volume” module. Newly created casted volume can be saved as PNG, JPEG or any other format.</p>

---

## Post #22 by @fieldr4 (2022-10-27 15:42 UTC)

<p>Got it, thank you! I was asking because using DRR command in the “<a href="http://plastimatch.org/windows_installation.html#windows-installation" rel="noopener nofollow ugc">Plastimatch Command Prompt</a>” on a PC yields a .pfm and a .txt file that contains the projection matrix that Andras mentioned in his last post.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da728ee11521fb2a4ad1e4e9a6d7e90aa891f12e.png" data-download-href="/uploads/short-url/vatwKpoAQeFiNtBYKK1dei4EBZk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da728ee11521fb2a4ad1e4e9a6d7e90aa891f12e.png" alt="image" data-base62-sha1="vatwKpoAQeFiNtBYKK1dei4EBZk" width="690" height="329" data-dominant-color="E0E0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1050×502 51.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would like to figure out a workflow that is primarily within 3D Slicer, so I am trying to figure out the best way to obtain this projection matrix through 3D Slicer. I thought that outputting a .pfm or .pgm from the <code>DRR Generation</code> module might create a file on my local hard drive with the accompanying .txt.</p>

---

## Post #23 by @Mik (2022-10-27 15:48 UTC)

<p>Plastimatch <a href="http://plastimatch.org/proj_mat_file_format.html" rel="noopener nofollow ugc">projection matrix file format</a>. Projection matrix <a href="http://plastimatch.org/proj_geometry_15.html" rel="noopener nofollow ugc">description</a>.  DRR parameters <a href="http://plastimatch.org/drr.html" rel="noopener nofollow ugc">description</a>.</p>

---

## Post #24 by @fieldr4 (2022-10-27 15:52 UTC)

<p>Can I obtain the Plastimatch DRR projection matrix from the <code>DRR Generation</code> module in 3D Slicer?</p>

---

## Post #25 by @Mik (2022-10-27 16:03 UTC)

<p>It’s impossible in current version, but such feature can be added into DrrImageComputationLogic of the module, or a function can be added to calculate projection of a markup point on the DRR image plane.</p>

---

## Post #26 by @fieldr4 (2022-10-28 03:04 UTC)

<p>Can I access any of the Plastimatch command prompt capabilities through the Python terminal available in 3D Slicer? For example, “Plastimatch drr” or “Plastimatch convert”.</p>
<p>Right now I am alternating between 3D Slicer and the Plastimatch command prompt to label points on a CT and then create a DRR from the same CT. Just trying to figure out if there are any efficiencies to be had without getting in over my head coding.</p>
<p>Thanks again for your help on this!</p>

---

## Post #27 by @Mik (2022-10-28 14:44 UTC)

<p>No. You can’t. Plastimatch convert command doesn’t have implementation as a 3D Slicer module.</p>

---

## Post #28 by @Mik (2022-10-29 05:43 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="24" data-topic="25873" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Can I obtain the Plastimatch DRR projection matrix from the <code>DRR Generation</code> module in 3D Slicer?</p>
</blockquote>
</aside>
<p>If you need calculate the projection of point by ray casting. simple intersection between a line (Point-1 is a x-ray source. Point-2 is your point ) and imager plane, it can be added to DRR calculation logic within a several days. You can set a fiducial point within CT data, and calculate point “projection” on DRR image using 3D Slicer python console.</p>

---

## Post #29 by @fieldr4 (2022-10-29 12:09 UTC)

<p>Unfortunately, editing the DRR calculation logic is beyond my programming abilities. My workaround is to place points in 3D Slicer, then to create the DRR with the Plastimatch Command Prompt and pull the projection matrix from the .txt that is generated.</p>
<p>I have another question regarding the <code>DRR Generation</code> module: does the DRR calculation logic replicate the divergence of x-ray beams away from the source? I would like to simulate  the size and shape distortions that are characteristic of computed radiography and digital radiography (ex. femoral heads appear non-overlapping in a lateral DR because of the cone-shaped of the beam).</p>

---

## Post #30 by @Mik (2022-10-29 13:07 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="29" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Unfortunately, editing the DRR calculation logic is beyond my programming abilities. My workaround is to place points in 3D Slicer, then to create the DRR with the Plastimatch Command Prompt and pull the projection matrix from the .txt that is generated.</p>
</blockquote>
</aside>
<p>So you need only a projection matrix, not the coordinates of projected points? You don’t need to change anything in logic, but after update you can calculate projection of the points on image plane, either in GUI or in 3D Slicer python shell, using a simple script.</p>
<aside class="quote no-group" data-username="fieldr4" data-post="29" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>I have another question regarding the <code>DRR Generation</code> module: does the DRR calculation logic replicate the divergence of x-ray beams away from the source? I would like to simulate the size and shape distortions that are characteristic of computed radiography and digital radiography (ex. femoral heads appear non-overlapping in a lateral DR because of the cone-shaped of the beam).</p>
</blockquote>
</aside>
<p>Plastimatch simulates beam divergence (x-ray source to isocenter distance can be set in the  “Beams” module).  It’s not a parallel geometry, then x-ray comes from infinity.</p>

---

## Post #31 by @fieldr4 (2022-10-29 13:22 UTC)

<aside class="quote no-group" data-username="Mik" data-post="30" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>So you need only a projection matrix, not the coordinates of projected points? You don’t need to change anything in logic, but after update you can calculate projection of the points on image plane, either in GUI or in 3D Slicer python shell, using a simple script.</p>
</blockquote>
</aside>
<p>That’s a fair point–my previous post didn’t capture my full workflow. I am actually just copying the projection matrix and RAS points into an Excel template that I created, which outputs the pixel coordinates. It’d be great to skip that altogether, but I am okay with the manual labor.</p>
<aside class="quote no-group" data-username="Mik" data-post="30" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>Plastimatch simulates beam divergence (x-ray source to isocenter distance can be set in the “Beams” module). It’s not a parallel geometry, then x-ray comes from infinity.</p>
</blockquote>
</aside>
<p>I see the controls for SAD/SID<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c94cb57a5efb75fbe55dd42455107be3993894e.png" data-download-href="/uploads/short-url/6mnNxtkpD94reby7nC1wbiSa7Ui.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c94cb57a5efb75fbe55dd42455107be3993894e_2_345x100.png" alt="image" data-base62-sha1="6mnNxtkpD94reby7nC1wbiSa7Ui" width="345" height="100" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c94cb57a5efb75fbe55dd42455107be3993894e_2_345x100.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c94cb57a5efb75fbe55dd42455107be3993894e_2_517x150.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c94cb57a5efb75fbe55dd42455107be3993894e_2_690x200.png 2x" data-dominant-color="E7E8E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1116×326 24.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Are there any process parameters that influence beam divergence?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c9b6f00e3924620495152055420a44bd867f0b1.png" data-download-href="/uploads/short-url/454nODpyJdvjhM0DWOpJ9m65Jw5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c9b6f00e3924620495152055420a44bd867f0b1_2_345x125.png" alt="image" data-base62-sha1="454nODpyJdvjhM0DWOpJ9m65Jw5" width="345" height="125" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c9b6f00e3924620495152055420a44bd867f0b1_2_345x125.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c9b6f00e3924620495152055420a44bd867f0b1_2_517x187.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c9b6f00e3924620495152055420a44bd867f0b1_2_690x250.png 2x" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1126×410 29.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any documentation of the beam divergence from Plastimatch?</p>
<p>Thanks again for all of your help. I appreciate the prompt replies on a Saturday.</p>

---

## Post #32 by @lassoan (2022-10-29 14:15 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="26" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Can I access any of the Plastimatch command prompt capabilities through the Python terminal available in 3D Slicer? For example, “Plastimatch drr” or “Plastimatch convert”.</p>
</blockquote>
</aside>
<p>Currently, only some platimatch features are exposed in SlicerRT, but with very little work you can make anything available. You can either:</p>
<ul>
<li>bundle an executable and call it with a Slicer Python scripted module (as it is done in SlicerElastix, SlicerANTs, SegmentMesher extension), or</li>
<li>you can add a Slicer CLI module to wrap library functions (as it is done already for 10 Plastimatch tools - <a href="https://github.com/SlicerRt/SlicerRT/tree/master/PlmDrr">PlmDrr</a>, PlmLandwarp, PlmRegister, …), or</li>
<li>you can expose Plastimatch library functions in <a href="https://github.com/SlicerRt/SlicerRT/tree/master/PlastimatchPy">PlastimatchPy</a></li>
</ul>
<aside class="quote no-group" data-username="fieldr4" data-post="31" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Is there any documentation of the beam divergence from Plastimatch?</p>
</blockquote>
</aside>
<p>You should be able to find lots of description of this basic projection geometry on the web, and probably even in the DICOM or other standards. Source to image distance specifies one side of the right-angled triangle, and half detector size (= number of pixels * size of one pixel / 2) is the other side.</p>

---

## Post #33 by @Mik (2022-10-31 10:31 UTC)

<p>Did you try the “DRR Image Computation” module from “Radiotherapy” category? You have to create a RtPlan and a RtBeam nodes beforehard in the “External Beam Planning” and “Beams” modules respectively.</p>
<p>The “DRR Image Computation” module has better GUI, shows size and orientation of your imager, and shows plastimatch drr command parameters in the “Plastimatch DRR command arguments” subwindow.</p>

---

## Post #34 by @fieldr4 (2022-11-07 18:24 UTC)

<p>Hi Mik,</p>
<p>The GUI for the <code>DRR Image Computation</code> module is fantastic. Would have saved me hours of fiddling with nrm and vup in the Plastimatch Command prompt and the <code>DRR generation</code> module.</p>
<p>That being said, I need a .png of the DRR and the pixel coordinates of reference points that I placed on the source CT. As far as I can tell, those are not available from any of the modules in 3D Slicer.</p>
<p>Does the 3D Slicer support team ever engage in paid consulting to enhance existing modules to meet unique user needs? Apologies if this is outside of the rules of the forum.</p>
<p>Andrew</p>

---

## Post #35 by @lassoan (2022-11-07 18:44 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="34" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Does the 3D Slicer support team ever engage in paid consulting to enhance existing modules to meet unique user needs? Apologies if this is outside of the rules of the forum.</p>
</blockquote>
</aside>
<p>Maybe someone will contact you in a private message offering paid help, and you can also post your asking for help in the <a href="https://discourse.slicer.org/c/announcements/jobs/22" class="inline-onebox">Jobs - 3D Slicer Community</a> category or contact any of the <a href="https://www.slicer.org/commercial-use.html#commercial-partners">Slicer Commercial Partners</a>.</p>

---

## Post #36 by @Mik (2022-11-08 08:09 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="34" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>That being said, I need a .png of the DRR and the pixel coordinates of reference points that I placed on the source CT. As far as I can tell, those are not available from any of the modules in 3D Slicer.</p>
</blockquote>
</aside>
<p>I can do the calculation of markups projections on a imager plane. I need such soft of functionality for myself. Do you need projection coordinates in World or in local imager system (offset from imager origin position (0,0) or column,row position)?</p>

---

## Post #37 by @fieldr4 (2022-11-09 02:31 UTC)

<p>That would be great! I would like to have the pixel coordinates relative to the top left corner of the PNG of the DRR. Right now, I am using an Excel template to calculate the coordinates relative to the isocenter selected in 3D Slicer. See workflow below. I am using GIMP to convert the .pfm produced by Plastimatch into a .png.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/191ad291f3a2c2bbd4f6786814497c862236f2c8.png" alt="Workflow" data-base62-sha1="3A5p29MSIhSNasoIr0rPDmDdZ5m" width="612" height="274"></p>
<p>As a side note, you can see that the contrast in the resulting DRR is suboptimal. I posted a question about this in a separate thread, but haven’t tried the “Plastimatch adjust” functionality yet.</p>

---

## Post #38 by @Mik (2022-11-11 16:27 UTC)

<p>Here is an upgrade for <code>DRR Image Compulation</code> i suggest to add to SlicerRT.</p>
<ol>
<li>Plastimatch DRR projection matrices. Self explanatory, matrices are the same as plastimatch output, for checking and debugging.</li>
<li>Markups projection intersection with an imager plane:<br>
Select markups node. Select control point. If point is within volume bounds and if there is a intersection with an imager plane you will get as a result: coordinates of perspective projection in RAS (World): offset from imager origin in mm within imager coordinate system, pixel position (Column, Row) of projected control point.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f47080b23a7cf696a1499ef97c06c0766fbdc69f.png" data-download-href="/uploads/short-url/ySpxoYioWO5lXmNgm5tP7fabTWf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f47080b23a7cf696a1499ef97c06c0766fbdc69f_2_276x500.png" alt="image" data-base62-sha1="ySpxoYioWO5lXmNgm5tP7fabTWf" width="276" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f47080b23a7cf696a1499ef97c06c0766fbdc69f_2_276x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f47080b23a7cf696a1499ef97c06c0766fbdc69f_2_414x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f47080b23a7cf696a1499ef97c06c0766fbdc69f.png 2x" data-dominant-color="E4E6E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">453×819 47.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #39 by @Mik (2022-11-12 16:56 UTC)

<p><a href="https://github.com/SlicerRt/SlicerRT/pull/221" rel="noopener nofollow ugc">PR</a> is on the way.</p>

---

## Post #40 by @Mik (2022-11-13 12:28 UTC)

<p>Can download the latest release, and install SlicerRT once again? The updated <code>DRR Image Computation</code> module with perspective projection of markups on imager plane has been compiled and ready for your testing.</p>
<p>How to test:</p>
<ol>
<li>Load a CT volume;</li>
<li>Create a RTPlan node with proper isocenter;</li>
<li>Create RTBeam node with proper orientation angles: gantry, couch;</li>
<li>Created a fiducial markups node within the CT volume, with a required number of control points;</li>
<li>Select volume and beam in <code>DRR Image Computiation</code>, select a created markups node in <code>Markups projection intersection</code> frame, and finally select a desired control point.</li>
<li>Check the calculated coordinates for correctness.</li>
</ol>

---

## Post #41 by @fieldr4 (2022-11-17 18:37 UTC)

<p>Hi Mik, thank you very much for adding this feature and sorry for the slow response. I am using version 477d3e3 of SlicerRT. I uninstalled, reinstalled, and checked for updates, but I am not sure that it is the right version because the date is 2022-09-10.</p>
<p>With v477d3e3, I don’t see a frame named<code> Markups projection intersection</code>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/414867b5221eb317bee330c35003f51b5ed0e31c.jpeg" data-download-href="/uploads/short-url/9jwa5PquIgr78EvsKg1QgabX9GQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/414867b5221eb317bee330c35003f51b5ed0e31c_2_690x435.jpeg" alt="image" data-base62-sha1="9jwa5PquIgr78EvsKg1QgabX9GQ" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/414867b5221eb317bee330c35003f51b5ed0e31c_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/414867b5221eb317bee330c35003f51b5ed0e31c_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/414867b5221eb317bee330c35003f51b5ed0e31c_2_1380x870.jpeg 2x" data-dominant-color="848383"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1659×1048 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #42 by @Mik (2022-11-17 18:57 UTC)

<p>Upgrade both Slicer and SlicerRT. The latest versions.</p>

---

## Post #43 by @fieldr4 (2022-11-18 03:23 UTC)

<p>That worked. I started checking the values produced in the <code>Markups projection intersection with an imager plane</code> and the values did not match ones that I generated using the Plastimatch command prompt and an Excel spreadsheet that I made. I am taking it as an indicator that my Excel calculations are off. I will trouble shoot tomorrow and follow up.</p>
<p>Is it possible to populate the “Column, Row:” or “Offset from origin in mm” values for all of the markup fiducials in the list rather than one at a time? In the current configuration of the <code>Markups projection intersection with an imager plane</code> UI, I am copying these values manually into a spreadsheet to have the pixel coordinates together.</p>
<p>The “Coordinates” table in the <code>Control Points</code> frame in the <code>Markups</code> module is great because all of the points can be selected together and copied into an Excel spreadsheet.</p>

---

## Post #44 by @Mik (2022-11-18 10:10 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="43" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>I started checking the values produced in the <code>Markups projection intersection with an imager plane</code> and the values did not match ones that I generated using the Plastimatch command prompt and an Excel spreadsheet that I made. I am taking it as an indicator that my Excel calculations are off. I will trouble shoot tomorrow and follow up.</p>
</blockquote>
</aside>
<p>That must be checked thoroughly. It could be my mistake in programming, or other kind of silly mistake!</p>
<aside class="quote no-group" data-username="fieldr4" data-post="43" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Is it possible to populate the “Column, Row:” or “Offset from origin in mm” values for all of the markup fiducials in the list rather than one at a time? In the current configuration of the <code>Markups projection intersection with an imager plane</code> UI, I am copying these values manually into a spreadsheet to have the pixel coordinates together.</p>
</blockquote>
</aside>
<p>Here is a <a href="https://disk.yandex.ru/d/F4fHaz71cXM1DA" rel="noopener nofollow ugc">test scene</a> with a CT volume, Isocenter markups node, and a ControlPoints markups node which you want to project on a imager plane.</p>
<p>Load the scene and use this python script into Slicer python console. It will setup your plan, beam and a drrParameters.  drrLogic calculates DRR image. Iterating along all original control point you will be able to calculate all the required projections and save the result into file. File names must be adopted for your system.</p>
<pre data-code-wrap="python"><code class="lang-python">
# Get isocenter, get control points
isocenterPoint = slicer.mrmlScene.GetFirstNodeByName('Isocenter')
controlPoints = slicer.mrmlScene.GetFirstNodeByName('ControlPoints')

# Get CT
ctVolume = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')

# Create RTPlan
rtImagePlan = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLRTPlanNode', 'rtImagePlan')
rtImagePlan.SetAndObserveReferenceVolumeNode(ctVolume)
rtImagePlan.SetIsocenterSpecification(slicer.vtkMRMLRTPlanNode.ArbitraryPoint)
rtImagePlan.SetAndObservePoisMarkupsFiducialNode(isocenterPoint)

# Create RTBeam, add beam to the plan, setup beam parameters
rtImageBeam = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLRTBeamNode', 'rtImageBeam')
rtImagePlan.AddBeam(rtImageBeam)
rtImageBeam.SetGantryAngle(90.)
rtImageBeam.SetSAD(1000.)

# Create vtkMRMLDrrImageComputationNode node, setup and update Normal and View-Up vectors
# Compute DRR using defined rtImageParameters and ctVolume
rtImageParameters = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLDrrImageComputationNode', 'rtImageBeamParams')
rtImageParameters.SetAndObserveBeamNode(rtImageBeam)
rtImageParameters.SetHUThresholdBelow(120)

drrLogic = slicer.modules.drrimagecomputation.logic()
drrLogic.UpdateMarkupsNodes(rtImageParameters)
drrLogic.UpdateNormalAndVupVectors(rtImageParameters) # REQUIRED
drrLogic.ComputePlastimatchDRR( rtImageParameters, ctVolume)

# Get Plastimatch matrices (for testing and control)
plastimatchIntrinsic = vtk.vtkMatrix4x4()
drrLogic.GetPlastimatchIntrinsicMatrix(rtImageParameters, plastimatchIntrinsic)

plastimatchExtrinsic = vtk.vtkMatrix4x4()
drrLogic.GetPlastimatchExtrinsicMatrix(rtImageParameters, plastimatchExtrinsic)

plastimatchProjection = vtk.vtkMatrix4x4()
drrLogic.GetPlastimatchProjectionMatrix(rtImageParameters, plastimatchProjection)

# Create markups nodes for the results
projPoints = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'ProjectedPoints')
whPoints = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'WidthHeightPoints')
crPoints = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'ColumnRowPoints')

# Get number of original control points
nofPoints = controlPoints.GetNumberOfControlPoints()

# Loop all original control points, calculate projection and offsets
for i in range(nofPoints):
    cpRAS = [0,0,0]
    projPAS = [0,0,0]
    offsetWidthHeight = [0,0]
    offsetColumnRow = [0,0]
    # Get control point coordinate
    controlPoints.GetNthControlPointPositionWorld(i, cpRAS)
    # Calculate projected point offsets
    if drrLogic.GetPointOffsetFromImagerOrigin(rtImageParameters, cpRAS, offsetWidthHeight, offsetColumnRow):
        whPoints.AddControlPoint(offsetWidthHeight[0], offsetWidthHeight[1], 0, controlPoints.GetNthControlPointLabel(i))
        crPoints.AddControlPoint(offsetColumnRow[0], offsetColumnRow[1], 0, controlPoints.GetNthControlPointLabel(i))
    # Calculate projected point world coordinates
    if drrLogic.GetRayIntersectWithImagerPlane(rtImageParameters, cpRAS, projPAS):
        projPoints.AddControlPoint(projPAS, controlPoints.GetNthControlPointLabel(i))

# Save the results into csv files
slicer.modules.markups.logic().ExportControlPointsToCSV(projPoints, "/tmp/ProjectedControlPoints.csv")
slicer.modules.markups.logic().ExportControlPointsToCSV(whPoints, "/tmp/WidthHeightPoints.csv")
slicer.modules.markups.logic().ExportControlPointsToCSV(crPoints, "/tmp/ColumnRowPoints.csv")

</code></pre>

---

## Post #45 by @Mik (2022-11-18 10:26 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="43" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>The “Coordinates” table in the <code>Control Points</code> frame in the <code>Markups</code> module is great because all of the points can be selected together and copied into an Excel spreadsheet.</p>
</blockquote>
</aside>
<p>Once calculated projections are OK. You can modify script as you wish. Calculated markups nodes are also available in Slicer as well.</p>

---

## Post #46 by @Mik (2022-11-19 11:54 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="43" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Is it possible to populate the “Column, Row:” or “Offset from origin in mm” values for all of the markup fiducials in the list rather than one at a time? In the current configuration of the <code>Markups projection intersection with an imager plane</code> UI, I am copying these values manually into a spreadsheet to have the pixel coordinates together.</p>
<p>The “Coordinates” table in the <code>Control Points</code> frame in the <code>Markups</code> module is great because all of the points can be selected together and copied into an Excel spreadsheet.</p>
</blockquote>
</aside>
<p>I will add table widget next week, it allows you to copy all the data easier. The scrip will be also valid though.</p>

---

## Post #47 by @fieldr4 (2022-11-28 19:55 UTC)

<p>That would be great, thank you! Sorry for the slow response.</p>
<p>Were you able to implement the table widget?</p>

---

## Post #48 by @fieldr4 (2022-11-29 03:17 UTC)

<p>I hate to ask for more, but is there any way for Slicer to output a file containing the DRR? I am using the Plastimatch command prompt to generate a .pfm file after I set the configurations in Slicer and I would love to avoid that step.</p>

---

## Post #49 by @Mik (2022-11-29 08:36 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="47" data-topic="25873" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>That would be great, thank you! Sorry for the slow response.</p>
<p>Were you able to implement the table widget?</p>
</blockquote>
</aside>
<p>Yes. A new <a href="https://github.com/SlicerRt/SlicerRT/pull/222" rel="noopener nofollow ugc">PR</a> is on the way, but on Linux i wasn’t able to copy/paste data from table widget into spreadsheet. I will add saving of projection data into vtkMRMLTableNode shortly.</p>

---

## Post #50 by @Mik (2022-11-29 08:40 UTC)

<p>What file format for DRR do you need? Are you trying to avoid using <code>plastimatch drr</code> command at all, and use only 3D Slicer?</p>

---

## Post #51 by @Mik (2022-11-29 09:25 UTC)

<aside class="quote no-group quote-modified" data-username="fieldr4" data-post="48" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>Is there any way for Slicer to output a file containing the DRR?</p>
</blockquote>
</aside>
<p>In subject hierarchy:</p>
<ol>
<li>Right click on DRR image node</li>
<li>Export to file…</li>
<li>Save as mha or raw format, you can open that file in ImageJ.</li>
</ol>

---

## Post #52 by @Mik (2022-11-29 13:47 UTC)

<p>Check box was added so you can save valid projected data into table node. That data can be copy/pasted into a spreadsheet (tested in LibreOffice Calc).</p>

---

## Post #53 by @Mik (2022-12-04 08:13 UTC)

<p><a class="mention" href="/u/fieldr4">@fieldr4</a><br>
Another upgrade in ready to test. You can try DRR cli module and select .pfm file format as output, the resulted pfm file will be in the 3D Slicer temporary directory. That feature is only work with “DRR Generation” module, not with “DRR Image Computation”.</p>
<p>Let me know the results.</p>

---

## Post #54 by @fieldr4 (2023-01-04 17:02 UTC)

<p>Thank you again for implementing this. It has really streamlined my workflow.</p>
<p>Is there a way to project multiple lines? I am using the <code>Line</code> tool to mark vertebral endplates and then copying the line endpoints into a <code>Point List</code> to be able to use the <code>Markups perspective projection on the imager plane</code> functionality.</p>

---

## Post #55 by @Mik (2023-01-05 07:15 UTC)

<p>Do you mean many markups line nodes or something else?</p>

---

## Post #56 by @fieldr4 (2023-01-05 14:52 UTC)

<p>I meant multiple markup lines simultaneously. I am measuring vertebral endplates in the lumbar spine, which necessitates at least 11 lines per CT. See example below.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5240c80ac7a7f9ed70cf50604a873adcd9e1559.png" alt="Lines" data-base62-sha1="pQrEHjYmqiCpoJYYYQRGpJU3m89" width="515" height="242"></p>
<p>I need to project the points from these lines into the DRR coordinate reference frame.</p>

---

## Post #57 by @Mik (2023-01-05 18:21 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="56" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>I need to project the points from these lines into the DRR coordinate reference frame.</p>
</blockquote>
</aside>
<p>Projected these lines as cloud of points (fiducials) or as line nodes?</p>

---

## Post #58 by @fieldr4 (2023-01-05 19:45 UTC)

<p>I believe as clouds of points. See example below with two points projected onto DRR:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16f132d2a063eb567fcd4c68ad517d44da6c6f37.png" alt="image" data-base62-sha1="3gXgJ98rPWCwQO0bKDRsBvk1g1x" width="397" height="359"></p>
<p>I would like to replicate this for all of the endpoints of the line segments.</p>

---

## Post #59 by @Mik (2023-01-06 07:43 UTC)

<p>If all required markups line nodes are visible, and DRR parameter node and DRR image were created successfully, then you can try to use the code below. It iterates along all visible line nodes and projects each first and second control point of each line on the DRR plane.</p>
<p>You must check the result carefully.</p>
<pre><code class="lang-python">
drrLogic.ShowMarkupsNodes(False)
lines = slicer.mrmlScene.GetNodesByClass('vtkMRMLMarkupsLineNode')
projPoints = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'ProjectedPoints')

for line in lines:
    cpRAS = [0,0,0]
    projPAS = [0,0,0]
    
    if line.GetMarkupsDisplayNode().GetVisibility() == 1:
      line.GetNthControlPointPositionWorld( 0, cpRAS)
      if drrLogic.GetRayIntersectWithImagerPlane(rtImageParameters, cpRAS, projPAS):
          projPoints.AddControlPoint(projPAS, line.GetNthControlPointLabel(0)  + '_Proj')
    
      line.GetNthControlPointPositionWorld( 1, cpRAS)
      if drrLogic.GetRayIntersectWithImagerPlane(rtImageParameters, cpRAS, projPAS):
          projPoints.AddControlPoint(projPAS, line.GetNthControlPointLabel(1)  + '_Proj')
    
    line.UnRegister(None)


</code></pre>

---

## Post #60 by @fieldr4 (2023-02-10 17:18 UTC)

<p>Hi Mik,</p>
<p>I have been using the “Markups perspective projection on the imager plane” in the <code>DRR Image Computation</code> module and realized that it may be producing erroneous results. My use case involves placing points on spinal anatomic landmarks, then observing their position in the resulting DRR. The projected points in the example below appear in a different location than I would expect:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f5c9c14e3f8a6cd4327e8252e9f2fc2deb90c49.jpeg" data-download-href="/uploads/short-url/bk48oW2sa2gNj5AZc95chkyoML7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f5c9c14e3f8a6cd4327e8252e9f2fc2deb90c49_2_690x316.jpeg" alt="image" data-base62-sha1="bk48oW2sa2gNj5AZc95chkyoML7" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f5c9c14e3f8a6cd4327e8252e9f2fc2deb90c49_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f5c9c14e3f8a6cd4327e8252e9f2fc2deb90c49_2_1035x474.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f5c9c14e3f8a6cd4327e8252e9f2fc2deb90c49_2_1380x632.jpeg 2x" data-dominant-color="9BAA93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1745×800 71.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The red projected points do not contact the anatomic structures on which the original points are positioned. What could be causing this?</p>

---

## Post #61 by @Mik (2023-02-11 07:02 UTC)

<p>Can you share a scene (CT, plan, beam, markups) so i can check?</p>

---

## Post #62 by @Mik (2023-02-11 07:54 UTC)

<p>Do you have examples of markups for which projections are accurate or miscalculated? For example <code>Markup_1</code> projection is correct, <code>Markup_2</code> projection is wrong.</p>

---

## Post #63 by @fieldr4 (2023-03-08 03:47 UTC)

<p>Fortunately, I can’t reproduce the error that I reported 25 days ago. I tried with two different beams on the same CT and the projected points appeared as expected on the DRR.</p>
<p>The only remaining peculiarity is that the beam’s isocenter appears outside of the input volume. How can I send the .mrml file with the markups, plan, and beams? The CT is file 629 from VerSe 2020.</p>

---

## Post #64 by @Mik (2023-03-09 10:12 UTC)

<aside class="quote no-group" data-username="fieldr4" data-post="63" data-topic="25873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/439d5e/48.png" class="avatar"> fieldr4:</div>
<blockquote>
<p>How can I send the .mrml file with the markups, plan, and beams?</p>
</blockquote>
</aside>
<p>File → Save Data → set the flag “Create a Medical Record Bungle containing the scene” so everything were in one file (.mbr).</p>
<p>You can send it to me by e-mail (see account info) if file isn’t large, or just share that file on onedrive or google drive.</p>

---

## Post #65 by @RIM_ZAMZAMI (2023-08-04 10:52 UTC)

<p>i’m trying ti convert some CT scans to DRR format but the DRR genaration module does not give me any output can you guys help ?</p>

---

## Post #66 by @Mik (2023-08-05 18:44 UTC)

<p>The DRR generation module doesn’t convert CT into DRR. It computes DRR images using predefined beam geometry parameters. If you need such sort of functionality it’s doable. See also:</p>
<aside class="quote" data-post="33" data-topic="25873">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/optimizing-resolution-and-spacing-parameters-in-plastimatch-drr/25873/33">Optimizing resolution and spacing parameters in Plastimatch DRR</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Did you try the “DRR Image Computation” module from “Radiotherapy” category? You have to create a RtPlan and a RtBeam nodes beforehard in the “External Beam Planning” and “Beams” modules respectively. 
The “DRR Image Computation” module has better GUI, shows size and orientation of your imager, and shows plastimatch drr command parameters in the “Plastimatch DRR command arguments” subwindow.
  </blockquote>
</aside>


---
