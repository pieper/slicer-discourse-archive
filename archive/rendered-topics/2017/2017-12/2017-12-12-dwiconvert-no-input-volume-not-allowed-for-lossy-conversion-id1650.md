---
topic_id: 1650
title: "Dwiconvert No Input Volume Not Allowed For Lossy Conversion"
date: 2017-12-12
url: https://discourse.slicer.org/t/1650
---

# DWIConvert: no input volume not allowed for lossy conversion from NIFTI FSL to nrrd

**Topic ID**: 1650
**Date**: 2017-12-12
**URL**: https://discourse.slicer.org/t/dwiconvert-no-input-volume-not-allowed-for-lossy-conversion-from-nifti-fsl-to-nrrd/1650

---

## Post #1 by @vsivan (2017-12-12 14:47 UTC)

<p>Hello,</p>
<p>I am able to run DWI Convert for FSL to NRRD conversion with no input volume by selecting allow lossy conversion on DWIConvert 4.7.1. When I run DWI Convert with the same parameters in version 4.8.0, I get the following error:</p>
<pre><code class="lang-auto">Diffusion-weighted DICOM Import (DWIConvert) standard error:

W: DcmItem: Length of element (0300,d7ec) is odd
E: DcmElement: Unknown Tag &amp; Data (0300,d7ec) larger (3855987813) than remaining bytes in file
W: DcmItem: Dataset not in ascending tag order, at element (0300,d7ec)
W: DcmItem: Length of element (8b1f,0808) is odd
E: DcmElement: Unknown Tag &amp; Data (8b1f,0808) larger (1512397297) than remaining bytes in file
W: DcmItem: Length of element (8b1f,0808) is odd
E: DcmElement: Unknown Tag &amp; Data (8b1f,0808) larger (1512500603) than remaining bytes in file
W: DcmItem: Length of element (0300,d7ec) is odd
E: DcmElement: Unknown Tag &amp; Data (0300,d7ec) larger (3855987813) than remaining bytes in file
W: DcmItem: Dataset not in ascending tag order, at element (0300,d7ec)
W: DcmItem: Length of element (0300,d9ec) is odd
E: DcmElement: Unknown Tag &amp; Data (0300,d9ec) larger (3520476281) than remaining bytes in file
W: DcmItem: Dataset not in ascending tag order, at element (0300,d9ec)
W: DcmItem: Length of element (0300,d7ec) is odd
E: DcmElement: Unknown Tag &amp; Data (0300,d7ec) larger (1737862245) than remaining bytes in file
W: DcmItem: Dataset not in ascending tag order, at element (0300,d7ec)
W: DcmItem: Length of element (6600,c139) is odd
E: DcmElement: Unknown Tag &amp; Data (6600,c139) larger (63459087) than remaining bytes in file
Error: no DICOMfiles found in inputDirectory: .
Unable to create converter!
</code></pre>
<p>Is a workaround to carry out the conversion in the newer version?</p>
<p>Thanks.</p>

---

## Post #2 by @ihnorton (2017-12-12 15:08 UTC)

<p>It looks like the module is trying to run in DICOM-&gt;NRRD mode. Can you please send a screenshot of the options you selected? (please blank out any confidential information)</p>

---

## Post #3 by @vsivan (2017-12-12 15:47 UTC)

<p>Here’s the screenshot for the newer version (4.8.0):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7d9757930735af79c0fe8dc07df93cfb0ddc9e9.png" data-download-href="/uploads/short-url/uNuyHi4sUf3dCwiHlKpOoUP8umJ.png?dl=1" title="Screenshot from 2017-12-12 10-46-12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7d9757930735af79c0fe8dc07df93cfb0ddc9e9_2_439x500.png" alt="Screenshot from 2017-12-12 10-46-12" data-base62-sha1="uNuyHi4sUf3dCwiHlKpOoUP8umJ" width="439" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7d9757930735af79c0fe8dc07df93cfb0ddc9e9_2_439x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7d9757930735af79c0fe8dc07df93cfb0ddc9e9_2_658x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7d9757930735af79c0fe8dc07df93cfb0ddc9e9_2_878x1000.png 2x" data-dominant-color="B0ADB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2017-12-12 10-46-12</span><span class="informations">928×1056 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>EDIT: it is not apparent from the screenshot, but allowLossyConversion has been selected</p>

---

## Post #4 by @ihnorton (2017-12-12 20:11 UTC)

<p>Ok, looks like an issue which I already fixed. So please try the <a href="http://download.slicer.org/">nightly</a> and let me know if it still doesn’t work. See here for details:</p>
<p><a href="https://issues.slicer.org/view.php?id=4463" class="onebox" target="_blank">https://issues.slicer.org/view.php?id=4463</a></p>

---

## Post #5 by @vsivan (2017-12-12 20:21 UTC)

<p>Hi Isaiah,</p>
<p>Thanks! I am currently working with a build of Slicer that needs this fix. Do you know if there is a way to get it onto the build of Slicer, without having to rebuild everything?</p>

---

## Post #6 by @ihnorton (2017-12-12 20:51 UTC)

<p>Your screenshot says 2017-10-11, but if you are indeed on 4.8 then I think <a href="https://github.com/Slicer/BRAINSTools/tree/slicer-2017-11-29-v4.7.1-42ac3c3">this branch</a> should build cleanly. So do something like:</p>
<ul>
<li><code>cd SuperBuild/BRAINSTools</code></li>
<li><code>git fetch origin</code></li>
<li><code>git checkout slicer-2017-11-29-v4.7.1-42ac3c3</code></li>
<li><code>cd SuperBuild/Slicer-build</code></li>
<li>
<code>make</code> (or ninja, MSBuild, etc.)</li>
</ul>
<p>(note that BRAINSTools is an “external module”, so it has a source tree under <code>SuperBuild/BRAINSTools</code>, but actually builds under <code>Slicer-build</code> – it does not have a <code>BRAINSTools-build</code> tree like most other external projects)</p>

---

## Post #7 by @vsivan (2017-12-12 21:27 UTC)

<p>Hi Isaiah,</p>
<p>Apologies, but I might have been unclear. I am working with a Slicer 4.7 build. When I said “4.8”, I was referring to the version that appeared in the DWIConvert XML file.</p>
<pre><code class="lang-auto">&lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;executable&gt; 
  &lt;category&gt;Diffusion.Import and Export&lt;/category&gt; 
  &lt;title&gt;Diffusion-weighted DICOM Import (DWIConvert)&lt;/title&gt; 
  &lt;description&gt;&lt;![CDATA[Converts diffusion weighted MR images in DICOM series into NRRD format for analysis in Slicer. This program has been tested on only a limited subset of DTI DICOM formats available from Siemens, GE, and Philips scanners. Work in progress to support DICOM multi-frame data. The program parses DICOM header to extract necessary information about measurement frame, diffusion weighting directions, b-values, etc, and write out a NRRD image. For non-diffusion weighted DICOM images, it loads in an entire DICOM series and writes out a single dicom volume in a .nhdr/.raw pair.]]&gt;&lt;/description&gt; 
  &lt;version&gt;4.8.0&lt;/version&gt; 
</code></pre>
<p>Given this, what would you suggest I do for getting the build to work on the Slicer version 4.7 build.</p>
<p>Thank you.</p>

---

## Post #8 by @ihnorton (2017-12-12 21:37 UTC)

<aside class="quote no-group" data-username="vsivan" data-post="7" data-topic="1650">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/edb3f5/48.png" class="avatar"> vsivan:</div>
<blockquote>
<p>what would you suggest I do for getting the build to work on the Slicer version 4.7 build.</p>
</blockquote>
</aside>
<p>Update to current trunk <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p>There was about one year worth of BRAINSTools updates pulled in to Slicer close to when 4.8 was released, so those changes I linked are not likely to apply cleanly. Plus there are probably ITK updates required as well. Figuring out inter-dependencies could easily take more than the two hours it will require to update Slicer+dependencies to current trunk (on any relatively recent 2+ core computer).</p>
<p>Between 2017-10-11 and current trunk I don’t there are any significant API changes affecting your own code, if that is the concern.</p>

---

## Post #9 by @ihnorton (2017-12-12 21:47 UTC)

<p>Hmm, actually the BRAINSTools update was in September, so you might be able to get away with pulling the changes as I indicated.</p>
<p><a href="https://github.com/Slicer/Slicer/commit/160cff9f8881f9c6f054abbc490e0d64057fcf09#diff-88b37dcc9267d819b6fabff68a8e5290" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/commit/160cff9f8881f9c6f054abbc490e0d64057fcf09#diff-88b37dcc9267d819b6fabff68a8e5290</a></p>

---

## Post #10 by @vsivan (2017-12-12 22:02 UTC)

<p>Okay, I will try that first. Otherwise, I’ll rebuild Slicer as you suggested. Thanks, Isaiah!</p>

---
