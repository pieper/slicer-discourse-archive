# Loading Tiff Stack

**Topic ID**: 15761
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/loading-tiff-stack/15761

---

## Post #1 by @mollyselba (2021-02-01 01:54 UTC)

<p>Issue 1:<br>
I am not sure why I keep having the same issue, but I was hoping you might be able to point me in the right direction. I am trying to load this file: [<a href="http://www.morphosource.org/Detail/MediaDetail/Show/media_id/18864" rel="noopener nofollow ugc">http://www.morphosource.org/Detail/MediaDetail/Show/media_id/18864</a>] <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09d7692254abbf0b54db3d6accbf7c08b443f56c.jpeg" data-download-href="/uploads/short-url/1p3OncyFEMU4d15uiMyHlcWFEtK.jpeg?dl=1" title="Question1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09d7692254abbf0b54db3d6accbf7c08b443f56c_2_690x349.jpeg" alt="Question1.PNG" data-base62-sha1="1p3OncyFEMU4d15uiMyHlcWFEtK" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09d7692254abbf0b54db3d6accbf7c08b443f56c_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09d7692254abbf0b54db3d6accbf7c08b443f56c_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09d7692254abbf0b54db3d6accbf7c08b443f56c.jpeg 2x" data-dominant-color="9192B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Question1.PNG</span><span class="informations">1288×653 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>. It is a .tiff stack. I load it in and then change the spacing to reflect the scan parameters. Every time I do, the skull ends up having these weird spaces… do you know what I am doing wrong? It looks fine as long as I don’t try to input the scan parameters. Morphosource is offline right now so it may not be possible to access the original file. Could it be I doing something wrong in the upload process? Or could it possibly be a greyscale issue?</p>
<p>Issue 2:<br>
For my files that are DICOM stacks, I was using the ROI function to clip the volume (so I could see endocranially). It isn’t working when I use a .tiff stack… is there a comparable function that I can use?</p>
<p>Operating system: Windows<br>
Slicer version: Slicer 4.13.0-2020-12-11<br>
Expected behavior: Volume loads without weird spaces<br>
Actual behavior: Volume loads with spaces in the volume</p>

---

## Post #2 by @muratmaga (2021-02-01 02:00 UTC)

<p>This looks like a rendering issue, in which shading is not working correctly. Can you provide a screenshot of your “Volume Rendering” panel?</p>
<p>Couple other things:<br>
Are you by any chance using “GPU MultiVolumeRendering”, which is an experimental feature? Can you try choosing “CPU Rendering”. It will be slow, but should render correctly.<br>
Also what’s the GPU (graphic card) in your computer and the driver version?</p>
<p>Since MorphoSource is currently offline, I can’t download and try the dataset.</p>

---

## Post #3 by @lassoan (2021-02-01 02:17 UTC)

<p>It looks like the volume renderer sampling is too sparse. You can try setting spacing to 0.1 in Volumes module (Volume Information section) and/or in Volume rendering module, use GPU volume rendering and change rendering quality to “Normal”. Splitting the volume to two smaller volumes that only contain one piece may also help.</p>

---

## Post #4 by @mollyselba (2021-02-01 23:03 UTC)

<p>It was on GPU MultiVolumeRendering on accident… I changed it back to GPU Rendering and now it is working again! (The ROI feature is now working again as well!). Thank you.</p>

---

## Post #5 by @muratmaga (2021-02-01 23:05 UTC)

<p>Great to hear that. But can you actually change the solution, so that it was tagged correctly? It wasn’t the spacing that Andras suggested (which is what you chose as the final solution).</p>

---

## Post #6 by @mollyselba (2021-02-02 00:17 UTC)

<p>Sorry… it should be fixed now.</p>

---
