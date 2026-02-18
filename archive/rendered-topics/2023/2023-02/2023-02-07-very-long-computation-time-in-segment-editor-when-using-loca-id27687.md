# Very long computation time in Segment Editor when using Local threshold or Smoothing

**Topic ID**: 27687
**Date**: 2023-02-07
**URL**: https://discourse.slicer.org/t/very-long-computation-time-in-segment-editor-when-using-local-threshold-or-smoothing/27687

---

## Post #1 by @Gening_Dong (2023-02-07 19:57 UTC)

<p>Hi all,</p>
<p>I’m using the latest release of Slicer (5.2.1) on a Windows 11 system. My laptop and the lab’s workstation crashed every single time when I trying to use Local Threshold to build a model AND when trying to smooth the model. My laptop is 32GB RAM and the workstation is 64GB RAM. The datasets I was using range from 600Mb to 1.3GB so I don’t think it’s a memory issue.</p>
<p>Does anyone know what may be the problem? Thanks in advance.</p>
<p>Best,<br>
Gening</p>

---

## Post #2 by @lassoan (2023-02-08 11:42 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> as you know the Local Threshold effect best, could you investigate this problem report?</p>
<p><a class="mention" href="/u/gening_dong">@Gening_Dong</a> Please provide exact list of steps you perform to reproduce the issue. Use any of the Slicer sample data sets as a starting point. If the issue is not reproducible with any of those then share the data set you are using.</p>

---

## Post #4 by @Gening_Dong (2023-02-08 15:16 UTC)

<p>Oh sorry there may be a format issue when I tried to reply by email.</p>
<p>The steps are as follow:</p>
<ol>
<li>Load NRRD files (3D images) as volumes</li>
<li>Create new sequence, add the sequence to the browser</li>
<li>Sequence registration - generic all (also weird, see the output volume below) <strong>(The issue can be reproducible without this step)</strong>
</li>
<li>Segment editor (Show 3D) – Local Threshold (default setting) – Ctrl + left click – <strong>CRASHED</strong><br>
OR Segment editor (Show 3D) – Threshold – not crashed</li>
<li>Smooth – Median or Close Hole - <strong>CRASHED</strong>
</li>
</ol>
<p>I tried to reproduce with the sample data CT Cardio Seq but the sample data worked well. So I share the dataset I was using as follow:<br>
<a href="https://drive.google.com/drive/folders/1otxcbxQYskwuoqg24a1a6LvpmpEO7teL?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1otxcbxQYskwuoqg24a1a6LvpmpEO7teL?usp=sharing</a></p>
<p>Thanks,<br>
Gening</p>

---

## Post #5 by @lassoan (2023-02-08 19:57 UTC)

<p>I’ve checked this on my computer and found that the application does not actually crash, just performs a lengthy computation. If you use the default 3mm kernel size that results in an incredibly large kernel (307x307x75 voxel). It is about 50000x larger than a usual 5x5x5 voxel kernel and accordingly it takes really long time to apply.</p>
<p>If your image scaling is correct (a voxel in your image is really just 10 micrometer) then you’ll need to adjust the default processing parameters to get reasonable results. For example, set your kernel size in Local threshold or Smoothing effect to around 0.08mm (9x9x3 voxel).</p>

---

## Post #6 by @Gening_Dong (2023-02-08 20:05 UTC)

<p>Thanks for the reply! My image scale is indeed pretty small so I think that’s the reason why the computation’s taking so long and generating weird results. Thanks for the advice, I’ll reduce the kernel size into a comparable value.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bda0d66cdc14313ec92fd7214eaa0c775ce1bd64.png" data-download-href="/uploads/short-url/r3wPLhpBcjp8HpmUX2PmHy5RacI.png?dl=1" title="D8900189AFDD4611AB52441F5C6B7741.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bda0d66cdc14313ec92fd7214eaa0c775ce1bd64.png" alt="D8900189AFDD4611AB52441F5C6B7741.png" data-base62-sha1="r3wPLhpBcjp8HpmUX2PmHy5RacI" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">D8900189AFDD4611AB52441F5C6B7741.png</span><span class="informations">709×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
