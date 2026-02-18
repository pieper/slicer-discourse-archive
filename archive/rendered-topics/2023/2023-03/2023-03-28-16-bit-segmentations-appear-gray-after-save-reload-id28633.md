# 16-bit segmentations appear gray after save + reload

**Topic ID**: 28633
**Date**: 2023-03-28
**URL**: https://discourse.slicer.org/t/16-bit-segmentations-appear-gray-after-save-reload/28633

---

## Post #1 by @K-Meech (2023-03-28 15:59 UTC)

<p>Hi!<br>
I’m having an issue with using 16-bit label images in 3D slicer (saved as nrrd). I make these files externally with python or ImageJ then load them into 3D slicer - this works fine, and I can edit with the Segment Editor with no problems. When I save the file, close it and re-open though, all my segments appear gray, rather than their usual random colour maps. Also, this often results in 3D slicer not closing properly - with ‘3D Slicer 5.2.2’ remaining in the task manager in windows, and not releasing the RAM space.</p>
<p>Any ideas on how I can fix this? Thanks so much!</p>

---

## Post #2 by @muratmaga (2023-03-28 18:17 UTC)

<p>When you edit these with the Segment Editor, how are you saving them? If you are saving them as _seg.nrrd, you shouldn’t have this problem, as Slicer will load them as segmentations.</p>
<p>What is the master volume you are using with the Segment Editor. Can you provide a screenshot of your scene?</p>

---

## Post #3 by @K-Meech (2023-03-29 16:58 UTC)

<p>Yes - I am saving the segmenation as .nrrd. They still open as segmentations, but all the colours reset to gray. The other volume in the scene is a 16-bit X-ray image. Unfortunately I can’t share these images, but I had the same result some small example 16-bit data.</p>
<p>Here, I load a small 16-bit X-ray image (one of the samples that come with ImageJ) as a volume, and a 16-bit label image as a segmentation. The label image is all zeros, with some small example blobs of the max value (65535). This gives the first image - displaying in green with one segment. Saving and re-loading, gives the second image where the same segments are present, but now all gray.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4771faa57215e472197ca9379c312facd1402da4.png" data-download-href="/uploads/short-url/ac26amnrwR68TSf26GHh587r5di.png?dl=1" title="Screenshot (15)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4771faa57215e472197ca9379c312facd1402da4_2_690x356.png" alt="Screenshot (15)" data-base62-sha1="ac26amnrwR68TSf26GHh587r5di" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4771faa57215e472197ca9379c312facd1402da4_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4771faa57215e472197ca9379c312facd1402da4_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4771faa57215e472197ca9379c312facd1402da4_2_1380x712.png 2x" data-dominant-color="797981"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (15)</span><span class="informations">1920×991 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/149dd8cc3c143a2daa3244f90dc8d74b187a4ca9.png" data-download-href="/uploads/short-url/2WnJypZVr8EChjknI9baUj5uRMR.png?dl=1" title="Screenshot (16)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/149dd8cc3c143a2daa3244f90dc8d74b187a4ca9_2_690x352.png" alt="Screenshot (16)" data-base62-sha1="2WnJypZVr8EChjknI9baUj5uRMR" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/149dd8cc3c143a2daa3244f90dc8d74b187a4ca9_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/149dd8cc3c143a2daa3244f90dc8d74b187a4ca9_2_1035x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/149dd8cc3c143a2daa3244f90dc8d74b187a4ca9_2_1380x704.png 2x" data-dominant-color="797981"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (16)</span><span class="informations">1920×982 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-03-30 13:25 UTC)

<p>A nrrd file can be interpreted many ways. You may want to use the values as grayscale values, or interpret the daata set as a transform (values specifiying displacements), as a segmentation (each discrete value referring to a segment), etc. If you use the default <code>.seg.nrrd</code> file extension then that gives a hint to Slicer to interpret the file as a segmentation. If you use a generic file extension (e.g., just <code>.nrrd</code>) then you need to give the hint in the “Add data” window by choosing “Segmentation” in the “Description” column (by default the file is interpreted as a grayscale image).</p>
<p>Note that ImageJ is a 2D image oriented software. It can handle stacks of 2D images, but that is very different from interpreting the data as one 3D volume. This not just limits what you can do with the images but it may also cause data corruption - as we can see on your screenshots, the z spacing is incorrect, because ImageJ did not store the distance between the frames of the image stack (but other corruptions are possible, too, for example the image maybe left-right flipped).</p>

---

## Post #5 by @K-Meech (2023-03-31 14:52 UTC)

<p>Thanks for the info <a class="mention" href="/u/lassoan">@lassoan</a> ! I tried using the .seg.nrrd extension, but it still resets to gray when I save and then open the scene .mrml file later. It’s still recognising it as a segmentation, and appearing properly in the segment editor, but the colour of all segments is set to a uniform gray. This doesn’t seem to happen with equivalent 8-bit data. It’s not a big issue though - for now I can just manually re-import the data and the segment colouring is fixed.</p>
<p>As for ImageJ, I only meant this as a quick example image, so I didn’t set the z spacing. (On my actual data this is set correctly!)</p>

---

## Post #6 by @muratmaga (2023-03-31 18:22 UTC)

<aside class="quote no-group" data-username="K-Meech" data-post="5" data-topic="28633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/k-meech/48/65424_2.png" class="avatar"> K-Meech:</div>
<blockquote>
<p>It’s still recognising it as a segmentation, and appearing properly in the segment editor, but the colour of all segments is set to a uniform gray. This doesn’t seem to happen with equivalent 8-bit data.</p>
</blockquote>
</aside>
<p>Is there a reason why you are using 16bit data for labelmaps/segmentations? 8 bit would accommodate 255 classes and is sufficient for most usage.</p>

---

## Post #7 by @lassoan (2023-04-03 14:40 UTC)

<p>Slicer adjusts the scalar type automatically based on what values are in the segmentation, so I’m not sure how these 16-bit segmentations are created. <a class="mention" href="/u/k-meech">@K-Meech</a> can you clarify?</p>
<p>Please also share an example segmentation file (that you created of some publicly available data set) by uploading to somewhere (onedrive, dropbox, google drive, etc.) and posting the link here.</p>

---

## Post #8 by @K-Meech (2023-04-03 19:23 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> - I’m using 16-bit, as I have &gt; 255 classes. It’s an instance segmentation, and there are a lot of instances!<br>
<a class="mention" href="/u/lassoan">@lassoan</a> - I made these segmentations outside 3D slicer via some python scripts, so the segmentations are written via numpy + scikit-image. I’ll generate an example file next week when I’m back from vacation.</p>

---

## Post #9 by @K-Meech (2023-04-28 15:42 UTC)

<p>Sorry for the delay in getting back to you <a class="mention" href="/u/lassoan">@lassoan</a> - I’ve now made some example data which you should be able to download from dropbox: <a href="https://www.dropbox.com/sh/x6zlmgme9yvglb1/AABsYum8vmai1mgN7kUPKLBpa?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - slicer-example - Simplify your life</a></p>
<p>In this folder there is a small example x-ray stack (as nrrd), and a rough 16-bit segmentation with 2 segments (as nrrd). In 3D slicer, I load the stack as a volume, and the segmentation as a segmentation. The 2 segments display correctly in different colours. I then save the scene .mrml file and close. Double clicking the scene file to re-open, shows the correct image and segments - but the colour of all segments is now reset to gray.</p>
<p>Let me know if you need any more info - thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36c6429fe8119e95c89b774b69684b468d490f9f.jpeg" data-download-href="/uploads/short-url/7OyylIkxAwx7rMXU5iig3M1kyAL.jpeg?dl=1" title="Screenshot 2023-04-28 162457" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36c6429fe8119e95c89b774b69684b468d490f9f_2_610x499.jpeg" alt="Screenshot 2023-04-28 162457" data-base62-sha1="7OyylIkxAwx7rMXU5iig3M1kyAL" width="610" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36c6429fe8119e95c89b774b69684b468d490f9f_2_610x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36c6429fe8119e95c89b774b69684b468d490f9f_2_915x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36c6429fe8119e95c89b774b69684b468d490f9f.jpeg 2x" data-dominant-color="92928F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-28 162457</span><span class="informations">1214×994 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d8472155e9a0f4003ff65a1eb49f5b5b19ded67.jpeg" data-download-href="/uploads/short-url/6uFftCIfBKwpaGIJugIzLPmvMdV.jpeg?dl=1" title="Screenshot 2023-04-28 162646" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d8472155e9a0f4003ff65a1eb49f5b5b19ded67_2_611x500.jpeg" alt="Screenshot 2023-04-28 162646" data-base62-sha1="6uFftCIfBKwpaGIJugIzLPmvMdV" width="611" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d8472155e9a0f4003ff65a1eb49f5b5b19ded67_2_611x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d8472155e9a0f4003ff65a1eb49f5b5b19ded67_2_916x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d8472155e9a0f4003ff65a1eb49f5b5b19ded67.jpeg 2x" data-dominant-color="8E8E8E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-28 162646</span><span class="informations">1218×996 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2023-04-30 16:06 UTC)

<p>Thanks for the excellent instructions for reproducing this. The problem is that the segmentation file reader in Slicer generates segment colors automatically when the file is read from a non-segmentation NRRD file. However, it does not mark the segmentation node as modified, therefore by default saving the segmentation node is not offered by default when you save the scene.</p>
<p>All you need to do to fix this is to check the checkbox next to the segmentation node in the “Save data” window. An even better solution is to write the segment names, colors, and terminology in your segmentation file header.</p>
<p>I’ll fix the segmentation reader to automatically check this checkbox when colors are generated (and not stored in the segmentation file).</p>

---

## Post #11 by @K-Meech (2023-05-02 11:55 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> ! All working now.</p>

---
