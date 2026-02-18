# Segmenting vasculature from two-photon imaging

**Topic ID**: 8476
**Date**: 2019-09-18
**URL**: https://discourse.slicer.org/t/segmenting-vasculature-from-two-photon-imaging/8476

---

## Post #1 by @muratmaga (2019-09-18 01:29 UTC)

<p>This is on behalf of a colleague who is interested in using 3D Slicer to visualize and segment vasculature from mouse brains using two-photon imaging.</p>
<p>Specifically, they are interested in volume rendering of the data and do interactive segmentations and vessel tracing within the rendered volume with the aim of getting a 3D reconstructions of the vasculature and extracting data out of these reconstructions such as vessel diameter, length, tortuosity or straightness, branching order and branching angle etc.</p>
<p>He sent some examples of what they are trying to visualize and segment with Imaris currently. Any pointers would be much appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c99d05f6760539c6ebb8e648d5a29f4812f91355.jpeg" data-download-href="/uploads/short-url/sLyokqH7aqS9S8X6IMbmuk20tIp.jpeg?dl=1" title="Chronic%20window%201%20ZSeries%202%20map%20final_003%20(002)"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c99d05f6760539c6ebb8e648d5a29f4812f91355_2_690x290.jpeg" alt="Chronic%20window%201%20ZSeries%202%20map%20final_003%20(002)" data-base62-sha1="sLyokqH7aqS9S8X6IMbmuk20tIp" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c99d05f6760539c6ebb8e648d5a29f4812f91355_2_690x290.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c99d05f6760539c6ebb8e648d5a29f4812f91355_2_1035x435.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c99d05f6760539c6ebb8e648d5a29f4812f91355_2_1380x580.jpeg 2x" data-dominant-color="044A49"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Chronic%20window%201%20ZSeries%202%20map%20final_003%20(002)</span><span class="informations">2156×909 898 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sam_Horvath (2019-09-20 13:43 UTC)

<p>What would the interactive segmentation consist of?  Is this data suitable for thresholding, or would a more involved vessel segmentation algorithm (such as vmtk) be needed?</p>

---

## Post #3 by @muratmaga (2019-09-20 14:45 UTC)

<p>They trace the vessels in 3d rendering and then algorithm paints the branches, as I understand. In Imaris they don’t seem to use threshold, possibly due to change in intensities as they go deeper into the tissue.<br>
Ultimate goal is to get metrics from those branches, which I guess vmtk can do. But they first need a semi-automated way of extracting them.</p>

---

## Post #4 by @pieper (2019-09-21 21:20 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> can you provide a small sample?  It’s hard to tell from the image you posted how easy the task would be.  For example, is the pixel spacing isotropic?</p>

---

## Post #5 by @ylcnkzy (2023-01-31 14:01 UTC)

<p>What is the recent status if the topic? Any solution?</p>

---

## Post #6 by @muratmaga (2023-01-31 15:54 UTC)

<p>Not much, my colleague never gave me a sample dataset so that we can follow up.</p>

---

## Post #7 by @ylcnkzy (2023-01-31 16:09 UTC)

<p>I’m also investigating the possibility of using 3D slicer for segmentation, reconstruction and tracking of structures in 3D. I guess I can provide some data. Since 3D microscopy images are composed of channels (red, green, blue, etc) I believe that thresholding should be possible.</p>
<p>I will check my data I will provide a one if I can find it.</p>

---

## Post #8 by @ylcnkzy (2023-07-28 07:20 UTC)

<p>Well, I have now a data set can be used.</p>

---

## Post #9 by @pieper (2023-07-28 14:15 UTC)

<p>That’s great - if you can post a sample somewhere I’ll bet people would try some experiments and provide feedback.</p>

---

## Post #10 by @ylcnkzy (2023-08-24 11:41 UTC)

<p>Hi There,</p>
<p>Finally, I have managed to image some 3D stacks.</p>
<p>Properties:<br>
Nuclear staining for the kidney samples. There are two folders in the <a href="https://drive.google.com/drive/folders/1pQFT6bfeRi2GXW5R1Is2oqG9Ht91g-a1?usp=sharing" rel="noopener nofollow ugc">link</a>; the Kidney_nucleus_Series folder contains the tiff image series for nuclear staining and the Rendering folder contains some rendering videos that I have created with depth coding using the confocal microscope software.</p>
<p>I will update here with more complex data types (such as vasculature, and specific staining for specific cell types).</p>
<p>I believe a 3D slicer can create such a rendering view, but I could not figure out how.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ae2cd1c673f7cd405be130c4e5f40e06f798795.jpeg" data-download-href="/uploads/short-url/aGtfDmglNO59VOnGBi57rsp6BN3.jpeg?dl=1" title="3D_Z_stack_Nuclear staining" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4ae2cd1c673f7cd405be130c4e5f40e06f798795_2_690x474.jpeg" alt="3D_Z_stack_Nuclear staining" data-base62-sha1="aGtfDmglNO59VOnGBi57rsp6BN3" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4ae2cd1c673f7cd405be130c4e5f40e06f798795_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ae2cd1c673f7cd405be130c4e5f40e06f798795.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ae2cd1c673f7cd405be130c4e5f40e06f798795.jpeg 2x" data-dominant-color="2D441F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D_Z_stack_Nuclear staining</span><span class="informations">975×670 89.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please let me know if you have any questions regarding the data.</p>

---

## Post #11 by @pieper (2023-08-24 15:34 UTC)

<p>Thanks for sharing the data.  It’s fairly easy to work with in Slicer.  Just drag and drop one file, then turn on the options and uncheck the Single File option.  Then use the Vector to Scalar Volume module to eliminate the redundant channels and then turn on Volume Rendering for the newly created volume.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yzIcBFcUgn8" data-video-title=" - YouTube" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yzIcBFcUgn8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="" title=" - YouTube" width="" height="">
  </a>
</div>


---

## Post #12 by @muratmaga (2023-08-24 15:55 UTC)

<p>Here is the default rendering of your data. I used ImageStacks from SlicerMorph, since it makes RGB-&gt;grayscale conversion easier as well as allows downsampling etc…</p>
<p>In Slicer opacity/color maps are determined by the intensity values inside each voxel. but as I understand you want to color them based on the relation in the stack. That’s dots higher in the stack will have a different color then ones in the lower in the stack. Is that what you mean by <strong>depth coding?</strong></p>
<p>It should be doable by scripting, but I don’t think it is exposed via UI.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b50a0f3e9c92f2b0577cd5c576e7339c6015005.jpeg" data-download-href="/uploads/short-url/fjlPNXB5OwukSCs8u3DurQEylcp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b50a0f3e9c92f2b0577cd5c576e7339c6015005_2_690x341.jpeg" alt="image" data-base62-sha1="fjlPNXB5OwukSCs8u3DurQEylcp" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b50a0f3e9c92f2b0577cd5c576e7339c6015005_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b50a0f3e9c92f2b0577cd5c576e7339c6015005_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b50a0f3e9c92f2b0577cd5c576e7339c6015005_2_1380x682.jpeg 2x" data-dominant-color="7B7871"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3176×1570 1.05 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @ylcnkzy (2023-08-29 09:40 UTC)

<p>Hi Steve,<br>
Thanks for quick update. It looks nice.<br>
I plan to have bigger data such (probably at 1-5 GB in size), do you think if 3DSlicer able to render such big data? Is it possible to segment (via tresholding) and quantify (size and co-localization)? the volume?</p>

---

## Post #14 by @ylcnkzy (2023-08-29 09:48 UTC)

<p>Hi Murat,</p>
<p>Data actually is not RGB (it is possibly 12-14 bit). The rendered video is RGB. I used colorcoding (as a depth coding) to demonstrate the <strong>thickness of the sample</strong>. It is good to know that downsampling is possible via SlicerMorph.</p>
<p>PS: I will update another data (contains vasculature together with nuclear staining) that may allow studying tracking better.</p>

---

## Post #15 by @pieper (2023-08-29 12:43 UTC)

<aside class="quote no-group" data-username="ylcnkzy" data-post="13" data-topic="8476">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ylcnkzy/48/12189_2.png" class="avatar"> ylcnkzy:</div>
<blockquote>
<p>bigger data such (probably at 1-5 GB in size), do you think if 3DSlicer able to render such big data?</p>
</blockquote>
</aside>
<p>That should be no problem if you have enough memory, although some steps, like decompressing, are single threaded and can be slow.  Cropping and downsampling can help a lot when exploring the data.</p>
<p>This example data was something like 180GB but can be explored at full res (not volume rendered).</p>
<aside class="quote quote-modified" data-post="7" data-topic="30648">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/imaging-data-commons-july-2023-release/30648/7">Imaging Data Commons July 2023 release</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    As far as I know the VHP Female data digitized from the 70mm film photos is the highest quality available.  It is very interactive to view if you have a big enough machine: 

  <a href="https://www.youtube.com/watch?v=ltNLT4jUX58" target="_blank" rel="noopener">
    [VHP F 70mm film]
  </a>


It would be great to hear if people know of higher quality data.  Or non-human data like this of high quality could also be interesting to look at.
  </blockquote>
</aside>


---
