# Slicer Issues with Displaying Certain DICOM Images

**Topic ID**: 17262
**Date**: 2021-04-23
**URL**: https://discourse.slicer.org/t/slicer-issues-with-displaying-certain-dicom-images/17262

---

## Post #1 by @spycolyf (2021-04-23 00:27 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Hello Slicer team, I’m wondering why Slicer has a problem displaying these images while other viewers display them correctly. Here are the images in my DropBox. They are test images, no worries…: <a href="https://www.dropbox.com/sh/hopthrktsxk096b/AACMArdeMeFo5aXxxfMkLN4Wa?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - TestImageVolume - Simplify your life</a></p>
<p>Here’s how they are displayed in Slicer…<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a8398bdf9c2315fb79eac5b00d83232de1847ba.png" alt="SlicerBadDisplay" data-base62-sha1="cUIUQprDQZ3iwO6rynNM2L8UAbw" width="406" height="386"></p>

---

## Post #2 by @issakomi (2021-04-23 02:07 UTC)

<p>This is related to <em>predictor6</em> bug in JPEG. In GDCM was a patch to workaround it, it is actually removed (some data set may work better without it, some with, AFAIK), so there is no problem with your data set in current Slicer version (tested with nightly).<br>
S. <a href="https://sourceforge.net/p/gdcm/gdcm/ci/37140257a286f109270bc415e207fc16d6d428c3/" class="inline-onebox" rel="noopener nofollow ugc">Grassroots DICOM / Gdcm / Commit [371402]</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/256d84d3e5596160c2deee13629f408df2a90554.jpeg" data-download-href="/uploads/short-url/5l6jbDlricsGblWgP0lQ7R1A0OE.jpeg?dl=1" title="Screenshot at 2021-04-23 04-07-03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/256d84d3e5596160c2deee13629f408df2a90554_2_655x500.jpeg" alt="Screenshot at 2021-04-23 04-07-03" data-base62-sha1="5l6jbDlricsGblWgP0lQ7R1A0OE" width="655" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/256d84d3e5596160c2deee13629f408df2a90554_2_655x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/256d84d3e5596160c2deee13629f408df2a90554_2_982x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/256d84d3e5596160c2deee13629f408df2a90554.jpeg 2x" data-dominant-color="929298"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2021-04-23 04-07-03</span><span class="informations">1130×862 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For reference (i left the option to enable/disable that patch)<br>
With patch<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a66615ee72b2fcd8f421b5b8ffd668c0063e88a4.png" alt="20210423-041133" data-base62-sha1="nK1YC1lnE5g7XsW34l5uUr9SLe4" width="183" height="218"></p>
<p>Without patch<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2abc30d0d44ddb3ff34302e119f6586c41992bed.png" alt="20210423-041127" data-base62-sha1="663fwI5kfvRCJUbrkGbZ05vSJFH" width="204" height="223"></p>

---

## Post #3 by @spycolyf (2021-04-23 15:30 UTC)

<p>Thanks <a class="mention" href="/u/issakomi">@issakomi</a>,</p>
<ol>
<li>Are you saying that in the most recent version of Slicer, my data will display fine because the patch is applied?</li>
<li>You stated “(some data set may work better without it, some with, AFAIK).” What is AFAIK and what types of images have it?</li>
<li>Can we dynamically turn the patch on or off? Perhaps we should add a button to our user interface to turn it on or off.</li>
</ol>
<p>Thanks.</p>

---

## Post #4 by @issakomi (2021-04-23 16:14 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="3" data-topic="17262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Are you saying that in the most recent version of Slicer, my data will display fine because the patch is applied?</p>
</blockquote>
</aside>
<p>Your data will display fine because the patch is removed.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="3" data-topic="17262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>You stated “(some data set may work better without it, some with, AFAIK).” What is AFAIK and what types of images have it?</p>
</blockquote>
</aside>
<p>I don’t have sample data set which works with the patch and doesn’t work without. The patch was ~10 years in GDCM, probably such data set exists.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="3" data-topic="17262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Can we dynamically turn the patch on or off? Perhaps we should add a button to our user interface to turn it on or off.</p>
</blockquote>
</aside>
<p>No, we can not turn it dynamically on/off in GDCM. S. DCMTK’s <a href="https://support.dcmtk.org/docs/dcmdjpeg.html" rel="noopener nofollow ugc">dcmdjpeg</a> and option <code>+w6</code></p>
<pre><code>  +w6   --workaround-pred6
          enable workaround for JPEG lossless images
          with overflow in predictor 6


  # DICOM images with 16 bits/pixel have been observed "in the wild"
  # that are compressed with lossless JPEG and need special handling
  # because the encoder produced an 16-bit integer overflow in predictor
  # 6, which needs to be compensated (reproduced) during decompression.
  # This flag enables a correct decompression of such faulty images, but
  # at the same time will cause an incorrect decompression of correctly
  # compressed images. Use with care.
</code></pre>

---

## Post #5 by @spycolyf (2021-04-24 00:01 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Was this a very recent gdcm fix removal?</p>
<p>Do Slicer fixes make it into SlicerQREADS builds?</p>
<p>Thanks.</p>

---

## Post #6 by @issakomi (2021-04-24 00:35 UTC)

<p>The change was <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/f2955fabd0a1e8b91f9d49f8c99be9b978dd4028" rel="noopener nofollow ugc">merged</a> into ITK <em>master</em> 10 months ago. Somewhere above is a link to GDCM’s initial commit (Sourceforge).</p>

---

## Post #7 by @issakomi (2021-04-24 00:44 UTC)

<p>Checked recent stable 4.11 release, there is the bug. Preview 4.13 is fine.</p>

---

## Post #8 by @Chris_Rorden (2021-04-24 11:55 UTC)

<p>As a historical note, once upon a time there was a popular DICOM tool named <code>Osiris</code> (I believe the modern <code>OsiriX</code> is an homage to this tool) that would save DICOM images using the compressed lossless JPEG transfer syntax <a href="https://www.dicomlibrary.com/dicom/transfer-syntax/" rel="noopener nofollow ugc">1.2. 840.10008.1.2.4.70</a>. This inefficient variant of JPEG is unique to medical imaging and is defined in <a href="https://www.w3.org/Graphics/JPEG/itu-t81.pdf" rel="noopener nofollow ugc">itu-t81</a>. Unfortunately, Osiris did not implement the format correctly, specifically Codec H.1.2.2: <code>No extra bits are appended after SSSS = 16 is encoded.</code> However, Osiris’ implementation was internally consistent (it could read and write its own images) and overwhelmingly popular. Since the format was so rare outside of medical imaging, many tools adopted the Osiris interpretation of the standard. Unfortunately, as far as I am aware there is no way to detect if this standard is implemented as described in the standard or as used by Osiris. For this reason, libraries must assume one method or another.</p>
<p>I would <em>strongly</em> discourage any DICOM users from using transfer syntax <a href="https://www.dicomlibrary.com/dicom/transfer-syntax/" rel="noopener nofollow ugc">1.2. 840.10008.1.2.4.70</a>. Due to the Osiris bug, it is handled differently by different tools. It is also very inefficient, and one will typically get much better compression using conventional file based compression (e.g. zstd, zip, gz). Since DICOM only requires DICOM compatible tools to handled uncompressed data, using compressed transfer syntaxes can cause unintended consequences. If you must use a compressed transfer syntax I would suggest the more efficient, modern and consistently implemented 1.2.840.10008.1.2.4.80 (JPEG-LS) or 1.2.840.10008.1.2.4.90 (JPEG 2000 Image Compression, Lossless Only).</p>

---

## Post #9 by @spycolyf (2021-04-24 14:52 UTC)

<p>Thanks <a class="mention" href="/u/issakomi">@issakomi</a> and <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a>.  I verified that Slicer 4.13 displays the images correctly. The timing on 4.13 availability perfect! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c36b99a922ee519d73af53f0c1ee8d06d95463f.png" alt="image" data-base62-sha1="8AFTyl8WSZlVILWNrZy2PuveQF1" width="461" height="385"></p>

---

## Post #10 by @issakomi (2021-04-25 17:00 UTC)

<blockquote>
<p>I don’t have sample data set which works with the patch and doesn’t work without.</p>
</blockquote>
<p>Here is such <a href="https://drive.google.com/file/d/1QO646Zl4tKvMeaOy1EuTFsxiDHIurMhi/view?usp=sharing" rel="noopener nofollow ugc">file</a>, from GDCM collection.</p>
<p>E.g. to test <code>dcmdjpeg +w6</code>.</p>

---

## Post #11 by @issakomi (2021-04-25 22:54 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="8" data-topic="17262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>As a historical note, once upon a time there was</p>
</blockquote>
</aside>
<p>May be this <a href="https://drive.google.com/file/d/1NUOlq7Ut57qiG8MTb3quXYlUajYnvGuj/view?usp=sharing" rel="noopener nofollow ugc">file</a> is an example of the bug you mentioned, <code>dcmdjpeg +wc</code> to fix.</p>

---

## Post #12 by @pieper (2021-04-26 15:15 UTC)

<aside class="quote no-group" data-username="issakomi" data-post="4" data-topic="17262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9e5f3/48.png" class="avatar"> issakomi:</div>
<blockquote>
<p>I don’t have sample data set which works with the patch and doesn’t work without.</p>
</blockquote>
</aside>
<p>I’m curious, shouldn’t this be a user option rather than a patch?  Maybe it’s not a common enough problem any more to be worth working on.</p>

---

## Post #13 by @issakomi (2021-04-26 15:31 UTC)

<p>In DCMTK <em>jpeg_decompress_struct</em> is extended, there is</p>
<pre><code>  /* Options that enable or disable various workarounds */
  unsigned int workaround_options;
</code></pre>
<p>and</p>
<pre><code>/* constants for workaround_options in struct jpeg_decompress_struct */
#define WORKAROUND_PREDICTOR6OVERFLOW 1
#define WORKAROUND_BUGGY_CORNELL_16BIT_JPEG_ENCODER 2
</code></pre>
<p>In GDCM it is not available, predictor patch is simply removed.</p>
<p>I don’t think the issue appears often. For “Predictor” bug - both, working and not-working files are 16 bit lossless JPEG <em>signed short</em>, AFAIK. Probably not very important, i hope, not 100% sure. Can be fixed with <code>dcmdjpeg</code> is someone has many files, IMHO.</p>

---

## Post #14 by @spycolyf (2021-04-27 22:17 UTC)

<p>Do you recommend that we use the latest nightly build (Slicer 4.13) if we have this problem? Or would  issues with other image types occur?</p>

---

## Post #15 by @jcfr (2021-04-27 22:21 UTC)

<p>For reference, this has been fixed integrating with the latest version of Slicer. See <a href="https://github.com/KitwareMedical/SlicerQReads/pull/93" class="inline-onebox">BUG: Update Slicer to include fix related to GDCM predictor6 bug in JPEG by jcfr · Pull Request #93 · KitwareMedical/SlicerQReads · GitHub</a></p>

---

## Post #16 by @spycolyf (2021-04-27 22:24 UTC)

<p>Oh ok. Thanks so much JC <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
