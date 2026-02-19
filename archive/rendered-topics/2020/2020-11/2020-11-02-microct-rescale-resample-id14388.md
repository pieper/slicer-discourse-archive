---
topic_id: 14388
title: "Microct Rescale Resample"
date: 2020-11-02
url: https://discourse.slicer.org/t/14388
---

# MicroCT--Rescale, Resample

**Topic ID**: 14388
**Date**: 2020-11-02
**URL**: https://discourse.slicer.org/t/microct-rescale-resample/14388

---

## Post #1 by @tsehrhardt (2020-11-02 16:38 UTC)

<p>I was recording dimension and resolution data for a set of microCT scans I’ve been working on and I noticed some issues between 16-bit and 8-bit nrrd volumes, resampled 8-bit (to larger slice thickness for modeling), and between the way Fiji and Slicer reads the volumes.</p>
<ol>
<li>
<p><strong>Rescaling to 8-bits:</strong>  I have followed the protocol on the SlicerMorph site for rescaling my 16-bit nrrd to 8-bit (<a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab11_SlicerPlusPlus#rescalecast" class="inline-onebox" rel="noopener nofollow ugc">W_2020/Lab11_SlicerPlusPlus at master · SlicerMorph/W_2020 · GitHub</a>). There seems to be a difference between 4.10.2 and 4.11.  For a 4gb volume at 16bit, my 8bit volume (generated in 4.10.2) shows up as a 700mb file in my file explorer, but when I open it in Fiji, it shows it as 2.1gb. It also shows the dimensions in microns instead of mm, but the same volume shows the correct dimensions in Slicer.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ec52ed8efca441c7e6cffaa6f49faa64d1c94a2.jpeg" data-download-href="/uploads/short-url/fNUZ1VMEpd2N7hgYpqSsEwzd8UG.jpeg?dl=1" title="16bitto8bit" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ec52ed8efca441c7e6cffaa6f49faa64d1c94a2_2_630x500.jpeg" alt="16bitto8bit" data-base62-sha1="fNUZ1VMEpd2N7hgYpqSsEwzd8UG" width="630" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ec52ed8efca441c7e6cffaa6f49faa64d1c94a2_2_630x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ec52ed8efca441c7e6cffaa6f49faa64d1c94a2_2_945x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ec52ed8efca441c7e6cffaa6f49faa64d1c94a2.jpeg 2x" data-dominant-color="919191"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">16bitto8bit</span><span class="informations">1006×798 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I re-import the DICOM slices into Slicer 4.11 and re-save the volume and rescale, I’m getting the 8bit to show in my file explorer as 2.1gb, but the mm/micron issue with Fiji is the same.</p>
</li>
<li>
<p><strong>Resampling:</strong> Since I don’t need to generate a 3D model from an 82 micron scan, I resampled to 0.1637 mm using Resample Scalar Volume. The new volume shows the correct dimensions (still showing as microns though in Fiji), but shows the Scalar Range as 0 to 254 instead of 0 to 255. This happens in both Slicer 4.10.2 and 4.11.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06c07dcc9759bfc75043102dceefab286a218bd8.png" data-download-href="/uploads/short-url/XJh5ZmmX9S2SOFh6btdPOmhkQo.png?dl=1" title="8bit_resampled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06c07dcc9759bfc75043102dceefab286a218bd8_2_376x500.png" alt="8bit_resampled" data-base62-sha1="XJh5ZmmX9S2SOFh6btdPOmhkQo" width="376" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06c07dcc9759bfc75043102dceefab286a218bd8_2_376x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06c07dcc9759bfc75043102dceefab286a218bd8_2_564x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06c07dcc9759bfc75043102dceefab286a218bd8_2_752x1000.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">8bit_resampled</span><span class="informations">948×1260 38.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>Should I be doing something differently?<br>
Any ideas why there’s a difference between Fiji and Slicer after rescaling to 8bit or why a grayscale value is lost when resampling?</p>
<p>Sorry if it’s confusing! FYI the DICOMs were exported from a NorthStar.<br>
Terrie</p>

---

## Post #2 by @muratmaga (2020-11-02 16:58 UTC)

<p>In my experience FIJI doesn’t read the units correctly. So I am not surprised that you are seeing a mm to micron difference.</p>
<p>As for data size change, the default in Slicer is to compress the volumes. So 2.1GB stack may end up 700MB on disk (file explorer), because it is compressed. FIJI doesn’t compress the NRRD volumes, AFAIK. If you have installed SlicerMorph in 4.11, we disable compression for volume nodes to improve read/write times for large datasets. So that might explain while your datasets from 4.10.2 ended up being smaller on disk than what it needs to be. You can manually uncheck the compress option in v4.10.2 in the save as dialog box.</p>
<p>As for why you are not getting the max as 255 the highest intensity value, I am not sure…</p>

---

## Post #3 by @lassoan (2020-11-02 17:10 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="1" data-topic="14388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>shows up as a 700mb file in my file explorer, but when I open it in Fiji, it shows it as 2.1gb.</p>
</blockquote>
</aside>
<p>File size may be smaller due to image compression, but since it is exactly 3x more, it is also possible that Fiji chooses to store the image in 3 channels (RGB). You can try to change color mode to grayscale.</p>
<aside class="quote no-group" data-username="tsehrhardt" data-post="1" data-topic="14388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>When I re-import the DICOM slices into Slicer 4.11 and re-save the volume and rescale, I’m getting the 8bit to show in my file explorer as 2.1gb</p>
</blockquote>
</aside>
<p>Check Volume module / Volume information / Number of scalars. If you see 3 there then it confirms that Fiji converted the grayscale image to RGB, needlessly tripling the memory usage.</p>
<aside class="quote no-group" data-username="tsehrhardt" data-post="1" data-topic="14388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>Since I don’t need to generate a 3D model from an 82 micron scan, I resampled to 0.1637 mm using Resample Scalar Volume. The new volume shows the correct dimensions (still showing as microns though in Fiji), but shows the Scalar Range as 0 to 254 instead of 0 to 255. This happens in both Slicer 4.10.2 and 4.11.</p>
</blockquote>
</aside>
<p>When you resample your image to lower resolution then small details in the image are lost. For example, if you only had a few, isolated voxels that had the intensity value of 255 then it is very likely that you will not have a value of 255 in the downsampled output. You can slightly increase the quality by applying antialiasing filter (low-pass filter, such as Gaussian smoothing should suffice), but it rarely makes a practical difference (see <a href="https://discourse.slicer.org/t/downsampling-nrrds/14033/10">this discussion</a> for details).</p>

---

## Post #4 by @tsehrhardt (2020-11-02 17:11 UTC)

<p>That’s good to know about the compression–that makes sense. When I noticed the mm/micron issue, I worried that I was making tiny models!</p>

---

## Post #5 by @tsehrhardt (2020-11-02 17:24 UTC)

<p>Thank you Andras! This all makes sense. I don’t think losing 255 would affect my 3D models since they’re mostly dry bone, but I might try the antialiasing filter on some volumes to see if I notice a difference.</p>
<p>Would it make a difference if I resample the resolution first then convert to 8-bit? I normally just convert to 8-bit first to reduce the file size and depending on the complexity of the specimen and sometimes reduce the resolution if the volume is still difficult to work with.</p>

---
