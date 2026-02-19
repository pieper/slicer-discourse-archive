---
topic_id: 7329
title: "Resolution Clarity"
date: 2019-06-27
url: https://discourse.slicer.org/t/7329
---

# Resolution clarity

**Topic ID**: 7329
**Date**: 2019-06-27
**URL**: https://discourse.slicer.org/t/resolution-clarity/7329

---

## Post #1 by @jackyhan (2019-06-27 03:28 UTC)

<p>I found that using 3D slicer to open DICOM image sequence, the resolution is very clear, but I use my own demo, ITK to read DICOM sequence, and then use VTK to display DICOM image, the resolution is very blurred, not 3D slicer clear. Why? Looking at the code, I found that 3dslicer uses vtkITK Archetype ImageSeries ScalarReader and vtkITK Archetype ImageSeries Reader to read and parse DICOM image sequences, and then I tried to use these two classes to read DICOM images, but the display is still not clear 3D slicer. Is 3D slicer optimized after that? Which class does the code use?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f25889947b7f2e3a7e83f0cc6b89d9c965c7d54f.jpeg" data-download-href="/uploads/short-url/yzTeMpsxxnc0osi2EXYkE3RRyPB.jpeg?dl=1" title="CCA5EA60-7B30-4a6a-AC10-9A904C9D258C" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f25889947b7f2e3a7e83f0cc6b89d9c965c7d54f_2_690x417.jpeg" alt="CCA5EA60-7B30-4a6a-AC10-9A904C9D258C" data-base62-sha1="yzTeMpsxxnc0osi2EXYkE3RRyPB" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f25889947b7f2e3a7e83f0cc6b89d9c965c7d54f_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f25889947b7f2e3a7e83f0cc6b89d9c965c7d54f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f25889947b7f2e3a7e83f0cc6b89d9c965c7d54f.jpeg 2x" data-dominant-color="A1A1A1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CCA5EA60-7B30-4a6a-AC10-9A904C9D258C</span><span class="informations">992×600 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jcfr (2019-06-27 03:31 UTC)

<p>To make sure we answer your question as thoroughly as possible,  would it be possible to summarize what you are trying to achieve ?</p>
<p>Alternatively, if you found an issue with the current modules, I suggest you provide a set of steps allowing to reproduce the problem.</p>

---

## Post #3 by @pieper (2019-06-27 11:44 UTC)

<p>Most likely the pixel data is identical but there is something different in the display pipeline.  You can control the way Slicer displays the data using the Volumes module and also see the pixel values with the Data Probe.  Probably there’s a way to do something similar in the ITK+VTK demo (or you can add something for debugging).</p>

---

## Post #4 by @jackyhan (2019-06-28 07:48 UTC)

<aside class="quote no-group quote-modified" data-username="jackyhan" data-post="1" data-topic="7329">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ad7895/48.png" class="avatar"> jackyhan:</div>
<blockquote>
<p>I found that using the 3D slicer to open the DICOM image sequence, the resolution is very clear, but I use my demo, ITK to read the DICOM sequence, and then use VTK to display the DICOM image, the resolution is very blurry, no 3D slicer is clear. why? Looking at the code, I found that 3dslicer uses vtkITK Archetype ImageSeries ScalarReader and vtkITK Archetype ImageSeries Reader to read and parse the DICOM image sequence, then I tried to use these two classes to read the DICOM image, but the display still does not clear the 3D slicer. Is the 3D slicer optimized? Which class does the code use?</p>
</blockquote>
</aside>
<details>
<summary>
Original in Chinese</summary>
<aside class="quote no-group quote-modified" data-username="jackyhan" data-post="1" data-topic="7329">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ad7895/48.png" class="avatar"> jackyhan:</div>
<blockquote>
<p>我发现使用3D切片器打开DICOM图像序列，分辨率非常清晰，但我用自己的demo，ITK读取DICOM序列，然后用VTK显示DICOM图像，分辨率非常模糊，没有3D切片器清晰。为什么？看看代码，我发现3dslicer使用vtkITK Archetype ImageSeries ScalarReader和vtkITK Archetype ImageSeries Reader来读取和解析DICOM图像序列，然后我尝试使用这两个类来读取DICOM图像，但显示仍然不清晰3D切片器。之后3D切片机是否经过优化？代码使用哪个类？</p>
</blockquote>
</aside>
</details>
<p>thank you for u answer! i have try to do it!</p>

---
