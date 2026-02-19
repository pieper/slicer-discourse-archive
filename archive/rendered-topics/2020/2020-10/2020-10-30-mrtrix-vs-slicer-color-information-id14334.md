---
topic_id: 14334
title: "Mrtrix Vs Slicer Color Information"
date: 2020-10-30
url: https://discourse.slicer.org/t/14334
---

# MRTrix vs. Slicer color information

**Topic ID**: 14334
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/mrtrix-vs-slicer-color-information/14334

---

## Post #1 by @jaredsullivan (2020-10-30 16:20 UTC)

<p>Hello,</p>
<p>I am having trouble using Slicer to view a directionally-encoded color track density imaging (DEC-TDI) map created in MRtrix (documentation: <a href="https://mrtrix.readthedocs.io/en/latest/reference/commands/tckmap.html" rel="noopener nofollow ugc">https://mrtrix.readthedocs.io/en/latest/reference/commands/tckmap.html</a>). The volume displays in color in MRtrix, but displays in grayscale in Slicer. In order to compare to a DEC-FA map that correctly displays in color in Slicer, I am trying to determine how I can alter the MRtrix file to display in color in Slicer.</p>
<p>The two DEC files (FA and TDI maps) can be found in this Dropbox folder: <a href="https://www.dropbox.com/sh/5vw4bexypqyxr1r/AAATxL0pLsoU2jyLbTeGh3Pla?dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/sh/5vw4bexypqyxr1r/AAATxL0pLsoU2jyLbTeGh3Pla?dl=0</a><br>
“Subject1_FA_DEC.nii” is the file that displays in color in Slicer.<br>
“Subject1_TDI_DEC.nii.gz” is the MRtrix-generated file that displays in grayscale in Slicer (want color).</p>
<p>From the Volumes module, we see that,<br>
Subject1_FA_DEC.nii has:<br>
Scalars: 3<br>
Scalar type: unsigned char<br>
Volume type: vector<br>
Subject 1_TDI_DEC.nii.gz has:<br>
Scalars: 1<br>
Scalar type: float<br>
Volume type: scalar</p>
<p>From the NIFTI headers, we see that,<br>
Subject1_FA_DEC.nii has image dimensions: [112×112×60×3 uint8]<br>
Subject1_TDI_DEC.nii.gz has image dimensions:<br>
[448×448×240×3 single]</p>
<p>From this information, we believe that Slicer may only be reading one component of the three-component MRtrix data, thus resulting in grayscale, and not color, display.</p>
<p>If anyone else has encountered this problem, or something similar, please let me know.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2020-11-05 23:36 UTC)

<p>We followed up on this off-list, here’s a way to get it working:</p>
<p>One needs to <code>pip_install("nibabel")</code>. Then the key lines are:</p>
<pre><code class="lang-auto">b = "/home/pieper/Downloads/AG2003_CSD_TDI_5_dec_b0.nii.gz"
ii = nibabel.load(b)
slicer.util.addVolumeFromArray(ii.get_data(), nodeClassName="vtkMRMLVectorVolumeNode")
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/966731b66113d55943092dea9a95e2e74e45ed28.jpeg" data-download-href="/uploads/short-url/lswId9cncPGdsRHGHqoAmDk3Knm.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/966731b66113d55943092dea9a95e2e74e45ed28_2_690x474.jpeg" alt="image" data-base62-sha1="lswId9cncPGdsRHGHqoAmDk3Knm" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/966731b66113d55943092dea9a95e2e74e45ed28_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/966731b66113d55943092dea9a95e2e74e45ed28.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/966731b66113d55943092dea9a95e2e74e45ed28.jpeg 2x" data-dominant-color="2E2D34"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">819×563 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I also manually edited the space directions so the volume was roughly oriented correctly, but it may still be left-right flipped.</p>

---
