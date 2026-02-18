# Install DentalSegmentator from behind restrictive firewall

**Topic ID**: 39474
**Date**: 2024-09-29
**URL**: https://discourse.slicer.org/t/install-dentalsegmentator-from-behind-restrictive-firewall/39474

---

## Post #1 by @xYanshui (2024-09-29 01:46 UTC)

<p>Thank you so much for developing the module. I came across with this error while applying segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d2839b0612b02ce5e6de5fb1c87054eed26e7f5.png" data-download-href="/uploads/short-url/6rtFs1jW5WNTgy1k4XyyCBw96SN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d2839b0612b02ce5e6de5fb1c87054eed26e7f5.png" alt="image" data-base62-sha1="6rtFs1jW5WNTgy1k4XyyCBw96SN" width="690" height="194" data-dominant-color="605E5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×279 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I tried to download the “.zip” file (“Dataset111_453CT_v100” I suppose?)  from the guided Github page, and created <code>DentalSegmentator\Resources\ML</code> folder as required since I didn’t find them. But the error remained. I wonder how can I solve this problem?</p>

---

## Post #2 by @lassoan (2024-10-01 13:57 UTC)

<p>You need to complete <a href="https://github.com/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#failed-to-download--find-weights">all the steps described in the module documentation</a>. There are further instructions below the first image (“Unzip the weight file…”).</p>

---

## Post #3 by @xYanshui (2024-10-02 06:03 UTC)

<p>I tried to put <code>checkpoint_final.pth</code> file from the downloaded zip and created <code>download_info.json</code> file, both in the mentioned folder <code>DentalSegmentator\Resources\ML</code>. The error remains.</p>

---

## Post #4 by @lassoan (2024-10-02 12:29 UTC)

<p>The problem must be something trivial, but it is hard to guess without any specific information. I would recommend to attach <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html">Visual Studio Code debugger</a> and put breakpoint into <a href="https://github.com/gaudot/SlicerDentalSegmentator/blob/7eaa69532e59d468cac6a28ecdd6c6218107eccd/DentalSegmentator/DentalSegmentatorLib/PythonDependencyChecker.py#L59">PythonDependencyChecker.py</a> and step through the code to see exactly what is happening. Setting up the debugger should not take more than 5-10 minutes and it will be obvious what is happening and what to do about it.</p>

---

## Post #5 by @xYanshui (2024-10-08 15:09 UTC)

<p>Sorry for replying late and I will try debugger these days. Maybe it’s a problem with the source of some python libraries. Thx for your timely help.</p>

---

## Post #6 by @RyderStevens (2024-10-22 13:38 UTC)

<p>Have you tried it? I also want to know it.</p>

---

## Post #7 by @xYanshui (2024-11-04 08:44 UTC)

<p>I found a post in local forum and it turned out to be a problem with access to online python libraries. I reset the environmental variables related to python libraries to change it for mirror url and it worked. The weight files should be downloaded manually and directly  unzipped in file mentioned in the instruction, which may require to be newly built.</p>

---

## Post #8 by @Jb-force (2025-03-05 16:43 UTC)

<p>I’d like to know how you solve this problem in the end, thanks</p>

---

## Post #9 by @lili-yu22 (2025-03-13 11:12 UTC)

<p>can you explain in more detail ?I have encountered the same problem  and tried  many methods.I urgently need your help.thank you</p>

---
