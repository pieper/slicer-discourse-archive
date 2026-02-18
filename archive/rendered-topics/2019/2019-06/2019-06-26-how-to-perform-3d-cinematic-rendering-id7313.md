# How to perform 3D-cinematic rendering?

**Topic ID**: 7313
**Date**: 2019-06-26
**URL**: https://discourse.slicer.org/t/how-to-perform-3d-cinematic-rendering/7313

---

## Post #1 by @Egor (2019-06-26 13:12 UTC)

<p>Is it possible to perform 3D-cinematic rendering from MDCT by 3D Slicer? Is there any modules to do that?</p>

---

## Post #2 by @pieper (2019-06-26 14:12 UTC)

<p>Hi -</p>
<p>We don’t have cinematic rendering functionality right now, but we’re going to be chatting about infrastructure improvements this afternoon so I added a note to talk about that.  Mostly for us it’s always a matter of either funded priorities or community contributions.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://projectweek.na-mic.org/PW31_2019_Boston/Breakouts/Infrastructure/" target="_blank" rel="nofollow noopener">ProjectWeek</a>
  </header>
  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW31_2019_Boston/Breakouts/Infrastructure/" target="_blank" rel="nofollow noopener">ProjectWeek</a></h3>

<p>Website for NA-MIC Project Weeks</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2019-06-26 14:55 UTC)

<p>Can you tell us a bit more about the application - patient education, understanding complex geometry, just playing around, …? Is there any particular clinical problem that you would like to solve?</p>
<p>Note that “cinematic rendering” is just a fancy name for adding more realistic lighting (most visible difference are shadows) to the volume rendering. For most applications, you could probably get functionally equivalent results (see the same clinically relevant details) with the current volume rendering if you spend some time with tuning transfer functions (in Advanced section of Volume rendering module).</p>

---

## Post #4 by @Chris_Rorden (2019-06-26 21:24 UTC)

<p>In my experience, it is much easier to apply enhanced rendering to CT modalities (e.g. MDCT) than MRI modalities. The image intensity of different tissues is calibrated for CT, while it is relative to MRI. These advanced renderings have a huge number of adjustable parameters, and this makes a generalized approach difficult. Therefore, while I certainly think one could develop a “cinematic” rendering module for Slicer (given substantial developer resources), it would only serve part of the user community.</p>
<p>A very simple but robust approach that can make both CT and MRI renderings look fancy is to use MatCaps. These are very easy to implement in a volume renderer and have very few parameters to adjust. This figure is generated with MRIcroGL using the MatCaps that come with Blender. I think these could be easily adapted to Slicer. While many MatCaps are a bit gaudy for my tastes, I do think they can help people visualize depth better than traditional volume rendering in some situations.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0b6aedc5e4b8f748f5594ef14fbada336087878.jpeg" data-download-href="/uploads/short-url/ruP4oKLAedvq9dZ6uoVmbwaLzFm.jpeg?dl=1" title="matcap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0b6aedc5e4b8f748f5594ef14fbada336087878_2_690x153.jpeg" alt="matcap" data-base62-sha1="ruP4oKLAedvq9dZ6uoVmbwaLzFm" width="690" height="153" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0b6aedc5e4b8f748f5594ef14fbada336087878_2_690x153.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0b6aedc5e4b8f748f5594ef14fbada336087878_2_1035x229.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0b6aedc5e4b8f748f5594ef14fbada336087878_2_1380x306.jpeg 2x" data-dominant-color="9D8184"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">matcap</span><span class="informations">3127×694 320 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2019-06-27 04:52 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="4" data-topic="7313">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>A very simple but robust approach that can make both CT and MRI renderings look fancy is to use MatCaps. These are very easy to implement</p>
</blockquote>
</aside>
<p>Implementation of surface mesh rendering is certainly easy and photorealistic rendering is widely available in various software applications. If creating of surface mesh (=model node) is not a problem then of course this approach may work well. Surface mesh files can be generated directly from segmentations using “Export to files” feature in Segment Editor.</p>
<p>However, most often creating a surface mesh requires significant effort and many cases (e.g., CT volumes) a number of structures can be displayed directly by volume rendering.</p>
<p>Anyway, if we decide to expose VTK’s photorealistic rendering engine (OSPray) in Slicer (see <a href="https://discourse.slicer.org/t/is-there-interest-in-higher-quality-rendering-for-slicer/6862/5">here</a>) then it will be usable for both surface rendering and volume rendering.</p>

---

## Post #6 by @Chris_Rorden (2019-06-27 13:04 UTC)

<p>@ <a href="https://discourse.slicer.org/u/lassoan">lassoan</a> MRIcroGL is a volume renderer. MatCaps work for both voxel-based volume rendering (MRIcroGL) and mesh-based Surface Rendering (Surfice). MatCaps work for either method. The images above were from MRIcroGL. The image below shows MRIcroGL using MatCaps for a high quality volume rendering (left) and low quality rendering (right). The low quality ray casting does not jitter start position and has a thick step size (with correspondingly opaque opacity correction). One uses the voxel gradients to select the MatCap sampling. The use of gradients is described in Chapter 5 of Engel et al.'s (2006) Real-Time Volume Graphics as well as on my <a href="https://www.mccauslandcenter.sc.edu/mricrogl/gradients" rel="noopener nofollow ugc">web page</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f908f085b51df5bc19e51061c976925009b41736.jpeg" data-download-href="/uploads/short-url/zx42FmucF1GzlGRTJZMjlbEGZMi.jpeg?dl=1" title="good" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f908f085b51df5bc19e51061c976925009b41736_2_690x370.jpeg" alt="good" data-base62-sha1="zx42FmucF1GzlGRTJZMjlbEGZMi" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f908f085b51df5bc19e51061c976925009b41736_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f908f085b51df5bc19e51061c976925009b41736_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f908f085b51df5bc19e51061c976925009b41736_2_1380x740.jpeg 2x" data-dominant-color="A98B81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">good</span><span class="informations">1473×790 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @pieper (2019-06-28 11:18 UTC)

<p>Excellent images <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> - would love to see this technique in Slicer/OHIF-vtk/vtkjs</p>

---

## Post #8 by @Chris_Rorden (2019-06-29 02:36 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a> -<br>
Since MRIcroGL is a complicated program, I created a simple JavaScript web page to illustrate MatCap-based volume rendering. <a href="https://github.com/rordenlab/rordenlab.github.io" rel="noopener nofollow ugc">Click here for the Github project</a> and <a href="https://rordenlab.github.io/" rel="noopener nofollow ugc">click here for a live demo</a>. You can use the file menu to load NIfTI format images. The control of the transfer texture is pretty rudimentary - program like MRIcroGL and Slicer can provide better control. However, it does illustrate the principle.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ea4ff4bdf3075038033d37365554f40acbb32a9.jpeg" data-download-href="/uploads/short-url/i4lFj5Oydn94IynSQqhjYwJaXnH.jpeg?dl=1" title="matcap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ea4ff4bdf3075038033d37365554f40acbb32a9_2_689x290.jpeg" alt="matcap" data-base62-sha1="i4lFj5Oydn94IynSQqhjYwJaXnH" width="689" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ea4ff4bdf3075038033d37365554f40acbb32a9_2_689x290.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ea4ff4bdf3075038033d37365554f40acbb32a9_2_1033x435.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ea4ff4bdf3075038033d37365554f40acbb32a9.jpeg 2x" data-dominant-color="826466"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">matcap</span><span class="informations">1148×483 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2019-06-29 14:26 UTC)

<p>This is amazing, thanks a lot for sharing. This seems to be a very simple and efficient way of providing textured appearance without generating 3D textures or 2D texture coordinates. This could be particularly useful when different material is applied to each structure (using multi-volume rendering or a labelmap-based lookup of texture image).</p>

---

## Post #11 by @Egor (2019-07-03 06:57 UTC)

<p>I’m going to try this method in peritoneal carcinomatosis assessing by MDCT (<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6158831/" rel="nofollow noopener">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6158831/</a>)</p>

---

## Post #12 by @Egor (2019-07-04 07:45 UTC)

<p>Thanks to all of you for your help.<br>
I understand that I can use Slicer to transfer CT data to NIfTI format then upload it to JavaScript web page. Am I right?</p>

---

## Post #13 by @Chris_Rorden (2019-07-04 11:43 UTC)

<p>Egor-<br>
CT scans have the advantage of having calibrated image intensity, but the disavantage that bone has extreme X-Ray attenuation relative to soft tissue. Therefore, nice CT rendering will require a nicely designed transfer texture. In brief, MRI scans often look nice without a transfer texture, but since CTs are calibrated one can design a transfer texture that works with most CTs. My javascript demo does not allow the user to specify a transfer texture, so while it is a proof of concept, it is not a great solution.</p>
<p>Would you be willing to share a nice modern CT dataset? One can get high quality CT scans at <a href="https://www.morphosource.org/" rel="nofollow noopener">morphosource</a>, but these do not include soft tissue. I do not have access to a modern CT dataset, so it is hard for me to design a CT transfer texture.</p>

---

## Post #14 by @pieper (2019-07-04 12:36 UTC)

<p>I was able to save the <a href="https://www.slicer.org/w/images/0/00/CTA-cardio.nrrd" rel="nofollow noopener">CTA-cardio.nrrd</a> volume from Slicer’s SampleData module in nii format and load it in Chris’s web page.  Looked really nice.  If you adjust the min/max range you can highlight different structures.</p>

---

## Post #15 by @Chris_Rorden (2019-07-06 11:36 UTC)

<p>Here is what the CTA-cardio image looks like with the MatCaps and a simple transfer texture. I suspect a trasnfer-texture specific pre-filter could improve this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd717e21c41f6aadee99f436297913390ea2975b.jpeg" data-download-href="/uploads/short-url/vAYG25Fa4vxaOZU25FLFmZSpEbp.jpeg?dl=1" title="ctx" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dd717e21c41f6aadee99f436297913390ea2975b_2_690x367.jpeg" alt="ctx" data-base62-sha1="vAYG25Fa4vxaOZU25FLFmZSpEbp" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dd717e21c41f6aadee99f436297913390ea2975b_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dd717e21c41f6aadee99f436297913390ea2975b_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dd717e21c41f6aadee99f436297913390ea2975b_2_1380x734.jpeg 2x" data-dominant-color="6C5D56"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ctx</span><span class="informations">1491×794 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @muratmaga (2019-07-07 16:59 UTC)

<p>This is really nice rendering. Would it with well with large datasets from morphosource?</p>
<p>Would it be possible to implement this technique in slicer?</p>

---

## Post #17 by @pieper (2019-07-07 21:27 UTC)

<p>Agreed - nice rendering <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p><a class="mention" href="/u/drouin-simon">@drouin-simon</a> and I discussed it a bit - VTK needs to have better support for sending down extra transfer function parameters (e.g. the extra 2D texture for the sphere map for the normal vector lookup).  Simon has a good idea what’s needed but it would also help of there’s anyone on the Kitware side with similar interests.</p>

---

## Post #18 by @lassoan (2019-07-07 23:05 UTC)

<p>This sounds like multi-volume rendering: multiple images used as inputs - some of them are 3D volumes as usual, some of them are 3-slice volumes that contain RGB components of the matcaps texture image. Could we use multi-volume renderer with special shaders to implement the matcaps lookup?</p>

---

## Post #19 by @finetjul (2019-07-08 07:28 UTC)

<p>For information, there is currently a <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/5584" rel="noopener nofollow ugc">PR</a> in VTK that adds Physically Based Rendering.<br>
Michael said:</p>
<blockquote>
<p>It is supported on the PolyDataMapper only.<br>
You can add any texture you want (vtkProperty::AddTexture) and sample it in the shader.<br>
Environment reflections (sphere map) and normal mapping will be supported natively by the shader in VTK 9.0 (shaders are only for PolyData mapper though) using multiple textures.</p>
</blockquote>
<p>I guess it could be extended to the Image mapper though…</p>

---

## Post #20 by @pieper (2019-07-08 13:06 UTC)

<p>Yes, it would be excellent to share the lighting maps and other infrastructure between polydata and volume rendering.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> it’s not so much mutli-volume (although it should apply there too) as managing extra 2D textures that store the normal maps etc.</p>

---

## Post #21 by @Chris_Rorden (2019-07-08 23:01 UTC)

<p><a href="https://discourse.slicer.org/u/muratmaga">muratmaga</a> Here are my thoughts with regards to the images from MorphoSource. The attached images below show <a href="https://www.morphosource.org/Detail/MediaDetail/Show/media_id/23861" rel="noopener nofollow ugc">a MorphoSource skull</a> with matcap-modulated volume rendering (left), pure-matcap volume rendering (center) and matcap-based surface rendering (right, Surfice)</p>
<ul>
<li>These are very high resolution images, but typically they only have a single hard surface boundary (e.g. bone vs air). This case seems ideally suited for using mesh-based surface rendering instead of volume rendering. For example, the Surfice function “Convert voxelwise volume to mesh” will convert a voxel-based image to an iso-surface mesh, alternatively you can use Slicer’s interactive Editor (I would suggest saving to any format except STL which is unable to share vertices). For large volumes, volume rendering will tend to be much slower than Surface rendering.</li>
<li>The quality of the DICOM headers varies for different images available on MorphoSource. Many convert with any tool without any problems. On the other hand, some lack instance numbers which will disrupt conversion. You can download and compile the developmental branch of dcm2niix from Github for a version that should salvage these images.</li>
<li>In my experience, most graphics cards are unable to handle any texture that exceeds 2Gb. So the resolution number of rows x columns x slices x 4  (XxYxZx4) must be less than 2Gb. Slicer’s “Crop Volume” or the “Resize Image (BRAINS)” functions are ideally suited to both crop and rescale volumes.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b103470e4bc09876eb1ec0a873543178ed788c7.jpeg" data-download-href="/uploads/short-url/3RpBQu5BfR7DTGikhRGSIKzLqqr.jpeg?dl=1" title="volumeRender_vs_surfaceRender" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b103470e4bc09876eb1ec0a873543178ed788c7_2_690x323.jpeg" alt="volumeRender_vs_surfaceRender" data-base62-sha1="3RpBQu5BfR7DTGikhRGSIKzLqqr" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b103470e4bc09876eb1ec0a873543178ed788c7_2_690x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b103470e4bc09876eb1ec0a873543178ed788c7_2_1035x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b103470e4bc09876eb1ec0a873543178ed788c7.jpeg 2x" data-dominant-color="B2ACAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volumeRender_vs_surfaceRender</span><span class="informations">1280×601 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #22 by @lassoan (2019-07-09 00:12 UTC)

<aside class="quote no-group" data-username="pieper" data-post="20" data-topic="7313">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> it’s not so much mutli-volume (although it should apply there too) as managing extra 2D textures that store the normal maps etc.</p>
</blockquote>
</aside>
<p>I just meant that the multi-volume GPU raycast mapper can already handle multiple image inputs, so that infrastructure may be usable for passing additional texture images to the volume renderer. I agree that it would be nicer to have a standard, dedicated interface in volume properties to store texture images.</p>

---

## Post #23 by @muratmaga (2019-07-09 12:36 UTC)

<p>Thanks for the pictures Chris. Yes, a lot of the images in MorphoSource comes from scans of specimens in osteological collection, and will not have any soft tissue to begin with. I also noticed the issues with DICOM headers. In my case,<br>
Slicer’s DICOM patcher worked fine fixing the issues, but dcm2niix definitely an option.</p>
<p>I have done some test to figure out HW limitations for GPU rendering in Slicer. I don’t know if that applies to the MatCaps/your software, but for VTK GPU raycasting the important parameter is the cards MAX_3D_TEXTURE_SIZE Opengl capability<br>
of the cards. Almost all ATI cards I have looked capped at 2K, whereas new NVIDIA geforces support 16K, and even up to 32K at new Quadro’s. The second requirement is to fit the entire volume in GPU’s memory.</p>
<p>But still these very good images.</p>

---

## Post #24 by @eewink (2019-09-02 13:06 UTC)

<p>Mevislab has excellent Cinematic Rendering. <a href="https://www.mevislab.de/download/" class="inline-onebox" rel="noopener nofollow ugc">MeVisLab: Download</a> Relatively easy to use as well. I have created a project file that does sculpting, and saving/loading of the cropped dataset and made crop box slider bars. Mevislab is visual network based programming - very easy to learn. I have made up a few colour transfer functions as well. Email me on <a href="mailto:derlang29@bigpond.com">derlang29@bigpond.com</a> if you are interested in getting my working project file. I don’t work for Mevislab.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e42c648422c00b6f43640ca58f77c9d7c69599a.jpeg" data-download-href="/uploads/short-url/bakj08vSPEe96djbCM43Awmfxjk.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e42c648422c00b6f43640ca58f77c9d7c69599a_2_441x500.jpeg" alt="1" data-base62-sha1="bakj08vSPEe96djbCM43Awmfxjk" width="441" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e42c648422c00b6f43640ca58f77c9d7c69599a_2_441x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e42c648422c00b6f43640ca58f77c9d7c69599a_2_661x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e42c648422c00b6f43640ca58f77c9d7c69599a_2_882x1000.jpeg 2x" data-dominant-color="614238"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1256×1423 450 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85336c54e666697e58d1b053ce3cd34d108450b4.jpeg" data-download-href="/uploads/short-url/j0lFZaKUN4lnwlFhj67M1EIG7oo.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85336c54e666697e58d1b053ce3cd34d108450b4_2_451x500.jpeg" alt="2" data-base62-sha1="j0lFZaKUN4lnwlFhj67M1EIG7oo" width="451" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85336c54e666697e58d1b053ce3cd34d108450b4_2_451x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85336c54e666697e58d1b053ce3cd34d108450b4_2_676x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85336c54e666697e58d1b053ce3cd34d108450b4_2_902x1000.jpeg 2x" data-dominant-color="44322C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1270×1406 320 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d2b162cc232bb0cf4d439410291f11db343fcef.jpeg" data-download-href="/uploads/short-url/dicItIYwN7z4wP7MIb7jAOmFSjB.jpeg?dl=1" title="brain1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d2b162cc232bb0cf4d439410291f11db343fcef_2_513x500.jpeg" alt="brain1" data-base62-sha1="dicItIYwN7z4wP7MIb7jAOmFSjB" width="513" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d2b162cc232bb0cf4d439410291f11db343fcef_2_513x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d2b162cc232bb0cf4d439410291f11db343fcef_2_769x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d2b162cc232bb0cf4d439410291f11db343fcef_2_1026x1000.jpeg 2x" data-dominant-color="564941"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">brain1</span><span class="informations">1263×1230 312 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #25 by @pieper (2019-09-02 13:32 UTC)

<aside class="quote no-group" data-username="eewink" data-post="24" data-topic="7313">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eewink/48/4612_2.png" class="avatar"> eewink:</div>
<blockquote>
<p>Mevislab has excellent Cinematic Rendering</p>
</blockquote>
</aside>
<p>Cool images!  Agreed, Mevislab is excellent.  For those who don’t know, Slicer’s python environment relies heavily on <a href="https://github.com/MeVisLab/pythonqt">PythonQt</a> from the Mevis team.</p>
<p>A few years ago when I was visiting Bremen we did an <a href="https://youtu.be/_FYDh0extbM">experiment hooking Slicer to Mevislab</a> (something like the MATLABBridge) so there’s a lot of interoperability potential if people want to go down that path.  People should of course be aware of the commercial licensing and regulatory considerations (Mevislab is free for non-commercial use, while the pro version (paid) is supported for medical device use).</p>

---

## Post #26 by @eewink (2019-09-02 13:37 UTC)

<p>I got a quote recently. The non commercial full version is $3000 euros and the commercial full version is $6000. The non commercial non full version is free. All my images were generated using the free non commercial non full version.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20e836fe4579d3aa490eed0bddbc7531c2ad9ca5.jpeg" data-download-href="/uploads/short-url/4H6NpGRoLYdE0RS72POdVOa9S3X.jpeg?dl=1" title="6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20e836fe4579d3aa490eed0bddbc7531c2ad9ca5_2_361x500.jpeg" alt="6" data-base62-sha1="4H6NpGRoLYdE0RS72POdVOa9S3X" width="361" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20e836fe4579d3aa490eed0bddbc7531c2ad9ca5_2_361x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20e836fe4579d3aa490eed0bddbc7531c2ad9ca5_2_541x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20e836fe4579d3aa490eed0bddbc7531c2ad9ca5_2_722x1000.jpeg 2x" data-dominant-color="46413D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6</span><span class="informations">1065×1473 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3de4f42972f7dfe9f4ffc2f0a2a81e475ff71171.jpeg" data-download-href="/uploads/short-url/8PxEIYeJqr5ki9cRBUwhVCai7SN.jpeg?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3de4f42972f7dfe9f4ffc2f0a2a81e475ff71171_2_439x500.jpeg" alt="5" data-base62-sha1="8PxEIYeJqr5ki9cRBUwhVCai7SN" width="439" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3de4f42972f7dfe9f4ffc2f0a2a81e475ff71171_2_439x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3de4f42972f7dfe9f4ffc2f0a2a81e475ff71171_2_658x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3de4f42972f7dfe9f4ffc2f0a2a81e475ff71171_2_878x1000.jpeg 2x" data-dominant-color="1E1C1A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">1328×1510 95.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df78204158500b5178e0d7047940903928903ab2.jpeg" data-download-href="/uploads/short-url/vSTQmUY7JBPz7f9R19toCv2fEAi.jpeg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df78204158500b5178e0d7047940903928903ab2_2_440x500.jpeg" alt="4" data-base62-sha1="vSTQmUY7JBPz7f9R19toCv2fEAi" width="440" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df78204158500b5178e0d7047940903928903ab2_2_440x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df78204158500b5178e0d7047940903928903ab2_2_660x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df78204158500b5178e0d7047940903928903ab2_2_880x1000.jpeg 2x" data-dominant-color="482E29"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1314×1490 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #27 by @lassoan (2019-09-02 22:20 UTC)

<p>I’m not sure how useful such artistic (plastic-looking) renderings are, but they definitely look nice.</p>
<p>How long does the rendering take?</p>
<p>Have you experimented with open-source photorealistic rendering engines, too?</p>
<p>Capabilities of MeVisLab are impressive but licensing fee is a nuisance and its restrictive license makes it impossible to use it in collaborative research (you cannot freely modify, enhance, and redistribute the library).</p>

---

## Post #28 by @pieper (2019-09-02 22:44 UTC)

<p>I did some experiments a few years ago with <a href="https://luxcorerender.org/">lux</a> and you can do some really nice things like the example below.  But most of the fancy renderers are surface-oriented and if they handle volumes at all it’s for like clouds or flame.</p>
<p>Also they are very slow even gpu accelerated.  They will basically run forever tracing light paths and you decide when the picture is good enough.</p>
<p>I think if we are going to invest time it’s better to try improving the existing volume rendering pipelines like we’ve been doing (although it would be great if there were more open source options).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a52bea1590099e62c75033d40818063300bace2b.jpeg" data-download-href="/uploads/short-url/nzaRRzaB0UtwJmgU0OoCVmGAaoP.jpeg?dl=1" title="someFibersEnhanced"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a52bea1590099e62c75033d40818063300bace2b_2_625x500.jpeg" alt="someFibersEnhanced" data-base62-sha1="nzaRRzaB0UtwJmgU0OoCVmGAaoP" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a52bea1590099e62c75033d40818063300bace2b_2_625x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a52bea1590099e62c75033d40818063300bace2b_2_937x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a52bea1590099e62c75033d40818063300bace2b_2_1250x1000.jpeg 2x" data-dominant-color="AEA8A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">someFibersEnhanced</span><span class="informations">1280×1024 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #29 by @eewink (2019-09-03 11:13 UTC)

<p>Each image progressively renders until it becomes high quality. You can set the number of iterations in the program. On average it takes 3-5 seconds to produce an image of good quality and 5-7 seconds for a very good image.</p>
<p>The images are better than regular volume rendering and ray casting in that it provides our hospital surgeons with better depth perception and it looks realistic just like a cadaver. It has been extremely useful in the hospital I work at. The feedback I have been given is that it is much easier to understand the 3D images performed with cinematic rendering. Interestingly I am also told that the images generated are less plastic looking and more life like.</p>
<p>The last rendering engine I used was VTK’s library. I also used Mitsubishi’s (now called Terarecon) VolumePro 1000 hardware accelerated ray casting chips. <a href="https://www.vision-systems.com/non-factory/security-surveillance-transportation/article/16744172/terarecon-launches-family-of-realtime-3d-visualization-products" rel="nofollow noopener">https://www.vision-systems.com/non-factory/security-surveillance-transportation/article/16744172/terarecon-launches-family-of-realtime-3d-visualization-products</a>.</p>

---

## Post #30 by @lassoan (2019-09-03 17:06 UTC)

<aside class="quote no-group" data-username="eewink" data-post="29" data-topic="7313">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eewink/48/4612_2.png" class="avatar"> eewink:</div>
<blockquote>
<p>The images are better than regular volume rendering and ray casting in that it provides our hospital surgeons with better depth perception and it looks realistic just like a cadaver. It has been extremely useful in the hospital I work at. The feedback I have been given is that it is much easier to understand the 3D images performed with cinematic rendering.</p>
</blockquote>
</aside>
<p>In most “cinematic rendering” images that I’ve seen, shadows are very strong. I guess it is probably because the main feature of this rendering mode is more realistic shadows. What I find very odd that normally surgeons don’t want this kind of dramatic lighting conditions (harsh shadows, <a href="https://oceanstudio.com/film-media-glossary/angle-incidence">contoured lighting</a>) in the operating room. They use flood lights and head lights to minimize shadows. So, why do they accept or even claim to be better to have shadows?</p>
<p>I understand that shadows can certainly improve depth perception, but casting shadows (decreasing visibility) in certain parts of the image has the risk of making potentially important details less clearly visible. There are cleaner, more direct ways of improving depth perception, such as virtual reality with its immersive stereo rendering, which provides more depth cues by disparity and motion parallax.</p>
<p>Long rendering time is an important problem, too. Several-second rendering time (which is about 100x slower than usual) makes “cinematic rendering” unsuitable for a wide range of applications, such as any interactive exploration of the volume, surgical guidance, virtual reality, etc.</p>
<p>It would be nice to be able to play with photorealistic rendering options to understand if shadows are good or bad after all, compare it to virtual reality, etc. Is there a sample application that you can share with us to play with (that does not require us to build anything or sign any license agreement)?</p>

---

## Post #32 by @eewink (2019-09-04 10:30 UTC)

<p>Just download the free noncommercial version of Mevislab. I can then email you my project file. Its only a rudimentary program with some minor bugs.</p>
<p>Yes you are right in that harsh shadows are not useful. The cinematic renderings I show to the surgeons (vascular and orthopaedic) don’t have strong shadows so nothing is missed.</p>
<p>Apparently Mevislab has a module for VR as well. But I think augmented reality is better so the surgeons can use it in the OR like the Microsoft Hololens and see a superimposed 3D image in the patient.</p>
<p>Current hardware for rendering is on a Nvidia 2080Ti.</p>

---

## Post #33 by @Chris_Rorden (2019-09-04 16:38 UTC)

<p>I created a new tomography’ shader that is included with the latest release of <a href="https://www.nitrc.org/projects/mricrogl/" rel="noopener nofollow ugc">MRIcroGL</a>. It is nice to have a selection of free tools for the job. Slicer provides a huge amount of flexibility. MRIcroGL generates reasonably interactive, reasonably pretty volume renderings on typical laptops for typically sized volumes. Mevislab can create stunning renderings but high quality is not interactive and requires high end hardware.</p>
<p>I do not have access to many CT images, nor have experience with CT color tables. If anyone wants to make suggestions or improvements I would like to hear about them.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9444b6a393cac9ddb6e17296b41b41cae040422c.jpeg" data-download-href="/uploads/short-url/l9DSM5IVfXRQpWmNxx56XAClm3y.jpeg?dl=1" title="GL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9444b6a393cac9ddb6e17296b41b41cae040422c_2_690x230.jpeg" alt="GL" data-base62-sha1="l9DSM5IVfXRQpWmNxx56XAClm3y" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9444b6a393cac9ddb6e17296b41b41cae040422c_2_690x230.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9444b6a393cac9ddb6e17296b41b41cae040422c_2_1035x345.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9444b6a393cac9ddb6e17296b41b41cae040422c_2_1380x460.jpeg 2x" data-dominant-color="574C4C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GL</span><span class="informations">1788×597 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
