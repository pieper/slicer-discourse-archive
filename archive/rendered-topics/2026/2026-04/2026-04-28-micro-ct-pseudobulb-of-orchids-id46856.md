---
topic_id: 46856
title: "Micro-CT Pseudobulb of Orchids: "
date: 2026-04-28
url: https://discourse.slicer.org/t/46856
last_bumped: 2026-05-08T04:14:14.406Z
---

# Micro-CT Pseudobulb of Orchids: 

**Topic ID**: 46856
**Date**: 2026-04-28
**URL**: https://discourse.slicer.org/t/micro-ct-pseudobulb-of-orchids/46856

---

## Post #1 by @Akhmad_Fauzan (2026-04-28 15:32 UTC)

<p>I’m having trouble with my 3D volume rendering. I am currently trying to render a 3D volume of a pseudobulb. The object appears as a thin, flattened disk rather than a full 3D structure. Could this be an issue with the ‘Image Spacing’ or ‘Voxel Size’ not being read correctly from the metadata, or is it simply because the Z-dimension is too low? Any advice on how to make it look more representative would be appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc.png" data-download-href="/uploads/short-url/86xcpKKwYNb3jW4RQUNMjPmHUny.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc_2_690x345.png" alt="image" data-base62-sha1="86xcpKKwYNb3jW4RQUNMjPmHUny" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc_2_1380x690.png 2x" data-dominant-color="3A3D3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×958 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-04-28 16:58 UTC)

<p>Do you know the actual z spacing?  If so you can type it in.  Otherwise it may be in the header in a format slicer doesn’t understand so you need to dig it out manually.</p>
<p>In general though this data is highly anisotropic (only 10 slices) so don’t expect a lot of 3D info. The segmentation you have is pretty meaningless, but you could try just volume rendering directly to see the internal structure in 3D.</p>

---

## Post #3 by @ThomasVanParys (2026-04-30 13:41 UTC)

<p>Hello. Have you inputted the parameters (spacing, especially the Z-axis) as per those from the mCT scan? Looks like you only have 10 slices too, is that correct?</p>

---

## Post #5 by @Akhmad_Fauzan (2026-05-01 15:43 UTC)

<p>Thank you for the detailed feedback regarding the anisotropic data! To clarify, the previous image was a partial subset. I actually have a full dataset of <strong>3,400 slices</strong> from this micro-CT.</p>
<p>With this in mind, do you recommend I proceed with <strong>Volume Rendering</strong> as the next step? Additionally, I am encountering performance issues when processing the full 3,400-slice stack, even on a high-spec PC. Do you have any suggestions for optimizing the workflow for a dataset of this size? Thanks for the help!</p>
<p>Below is the 3D for my 50 pictures (even for 50 images, it takes around 20-30 minutes for the 3D)</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/15_KDyhK0RqJT7CNzvLLLfBZy6Bww6mXc/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/15_KDyhK0RqJT7CNzvLLLfBZy6Bww6mXc/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/15_KDyhK0RqJT7CNzvLLLfBZy6Bww6mXc/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/15_KDyhK0RqJT7CNzvLLLfBZy6Bww6mXc/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">3D Slicer 5.10.0 2026-04-30 12-29-47.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Akhmad_Fauzan (2026-05-01 15:44 UTC)

<p>Hey, sorry for the late reply. I have updated the image spacing to <strong>0.009 mm</strong> for the X, Y, and Z axes to match the mCT scan parameters.</p>
<p>Regarding the slice count, the previous result was based on a subset of 10 images for initial testing. I actually have a full dataset of <strong>~3,400 slices</strong> from this micro-CT data. Any suggestions? I appreciate your guidance! Thank you.</p>

---

## Post #7 by @ThomasVanParys (2026-05-01 15:52 UTC)

<p>High-res mCT is computationally slow (depending on computer power), so I would suggest splitting the volume in half and then stitching them back together post-segmentation or lowering the resolution using the ImageStacks function (but you may want to keep the 0.009mm?)</p>

---

## Post #8 by @muratmaga (2026-05-01 18:03 UTC)

<p>Your XY pixels widths are about 2000. So you will have 2000x2000x3400 voxels, meaning you got about 13GB dataset (if they are 8 bit, twice if they are 16 bit, can’t tell from your screenshots). if you have big computer with a nice powerful GPU with at least 16GB of RAM, then you should be able to do the volume rendering of the full dataset.</p>
<p>You don’t need to use segmentation for that, only the Volume Rendering. If it turns out too large (and slow to interact with), as suggested, you can use the <code>ImageStacks</code> module. Given very large number of slices, I would suggest keeping the full resolution but skipping a slice.</p>

---

## Post #9 by @Akhmad_Fauzan (2026-05-07 01:47 UTC)

<p>Thank you for the info! Since I am working with this specific volume, could you guide me on the best way to see its internal structure? I want to ‘see through’ the outer surface to visualize the internal vascular networks. Do you have any advice on which Volume Rendering presets or opacity settings work best for this kind of plant tissue? Thanks a lot.</p>
<p>Below is my results. There are many noises and I just choose over presets that yield less noise.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/866814405f5d9992ea1c590283f464f77a1989bf.jpeg" data-download-href="/uploads/short-url/jb0Y6KLwP4LoKfEi4eekv1ve0aP.jpeg?dl=1" title="Screenshot 2026-05-05 141030" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/866814405f5d9992ea1c590283f464f77a1989bf_2_690x387.jpeg" alt="Screenshot 2026-05-05 141030" data-base62-sha1="jb0Y6KLwP4LoKfEi4eekv1ve0aP" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/866814405f5d9992ea1c590283f464f77a1989bf_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/866814405f5d9992ea1c590283f464f77a1989bf_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/866814405f5d9992ea1c590283f464f77a1989bf_2_1380x774.jpeg 2x" data-dominant-color="9A999F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-05 141030</span><span class="informations">1919×1079 456 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be6406004c8e58a2a7dca8c7220756cc06cee8fc.jpeg" data-download-href="/uploads/short-url/rah19A33FppI8AjH29kxNpWG2NC.jpeg?dl=1" title="Screenshot 2026-05-05 141407" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be6406004c8e58a2a7dca8c7220756cc06cee8fc_2_690x426.jpeg" alt="Screenshot 2026-05-05 141407" data-base62-sha1="rah19A33FppI8AjH29kxNpWG2NC" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be6406004c8e58a2a7dca8c7220756cc06cee8fc_2_690x426.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be6406004c8e58a2a7dca8c7220756cc06cee8fc_2_1035x639.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be6406004c8e58a2a7dca8c7220756cc06cee8fc_2_1380x852.jpeg 2x" data-dominant-color="9C9ED1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-05 141407</span><span class="informations">1427×883 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b5a79eddd405c4e6d39a500972b0f9067717588.jpeg" data-download-href="/uploads/short-url/6bwniujEEAmnRCgIcZK2bcOYUd2.jpeg?dl=1" title="Screenshot 2026-05-05 142518" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5a79eddd405c4e6d39a500972b0f9067717588_2_690x420.jpeg" alt="Screenshot 2026-05-05 142518" data-base62-sha1="6bwniujEEAmnRCgIcZK2bcOYUd2" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5a79eddd405c4e6d39a500972b0f9067717588_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5a79eddd405c4e6d39a500972b0f9067717588_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5a79eddd405c4e6d39a500972b0f9067717588_2_1380x840.jpeg 2x" data-dominant-color="9A9CD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-05 142518</span><span class="informations">1429×871 96.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Akhmad_Fauzan (2026-05-07 01:48 UTC)

<p>this one is the full scan:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5ec499aacf3e23a6c5d2cadb6962be08147e629.jpeg" data-download-href="/uploads/short-url/seUiVKSP2JHYgWLnB2EqWdx0tjH.jpeg?dl=1" title="pseudobulb-1_rec" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5ec499aacf3e23a6c5d2cadb6962be08147e629_2_690x490.jpeg" alt="pseudobulb-1_rec" data-base62-sha1="seUiVKSP2JHYgWLnB2EqWdx0tjH" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5ec499aacf3e23a6c5d2cadb6962be08147e629_2_690x490.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5ec499aacf3e23a6c5d2cadb6962be08147e629_2_1035x735.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5ec499aacf3e23a6c5d2cadb6962be08147e629.jpeg 2x" data-dominant-color="DDDDDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pseudobulb-1_rec</span><span class="informations">1312×933 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @muratmaga (2026-05-07 02:29 UTC)

<p>First do not use the VTK Multivolume Rendering, but the GPU Raycasting. Second, the presets are not going to be of any use, because microCTs are often not calibrated to a standard and intensity values are relative and specific to the reconstruction settings applied to your specific scan.</p>
<p>Is the Bruker rendering from the same dataset, if so, you should be able to render it like that in Slicer. Though the cross-sections seems like pure noise to me. So hard to tell what you will get out of that. If you can share your dataset, I can try to take a look.</p>

---

## Post #12 by @Akhmad_Fauzan (2026-05-07 03:26 UTC)

<p>thanks for the input. I will message you if it is okay for you.</p>

---

## Post #13 by @muratmaga (2026-05-07 04:19 UTC)

<p>If you don’t want to share the data publicly,  you can send the link to me privately. But otherwise we try to keep discussions public so everyone can benefit from it.</p>

---

## Post #15 by @muratmaga (2026-05-07 15:18 UTC)

<p>There is a lot of noise in your data. I did a median filter 2x2x2 kernel and then use the diceCT16 preset from SlicerMorph to render it like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b14fa39e3f8e34e636fe00bfbe4c48e17152099.jpeg" data-download-href="/uploads/short-url/697tsFp1TeEsYxcLyQT43HL5w81.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b14fa39e3f8e34e636fe00bfbe4c48e17152099_2_690x348.jpeg" alt="image" data-base62-sha1="697tsFp1TeEsYxcLyQT43HL5w81" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b14fa39e3f8e34e636fe00bfbe4c48e17152099_2_690x348.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b14fa39e3f8e34e636fe00bfbe4c48e17152099_2_1035x522.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b14fa39e3f8e34e636fe00bfbe4c48e17152099_2_1380x696.jpeg 2x" data-dominant-color="84888D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×971 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @Akhmad_Fauzan (2026-05-08 02:05 UTC)

<p>So, we use module SliceMorph to reduce the noise, right? Then, the 3D render is very clean, but it mostly shows the exterior surface. Could you show the internal morphology of that? Thanks for the big help.</p>

---

## Post #17 by @muratmaga (2026-05-08 04:14 UTC)

<p>Median filter is a core Slicer function. I used SlicerMorph to import the image stacks, and if you have it installed (which you need for imagestacks functionality), you also get the Dice16 preset I used.</p>
<p>Your scan does not show any internal detail that I can identify (except for little air pockets). You probably need to stain this with iodine or some other contrast agent to obtain some sort of contrast of tissues inside.</p>
<p>Likewise your bruker rendering does not show anything but the surface of the bulb.</p>

---
