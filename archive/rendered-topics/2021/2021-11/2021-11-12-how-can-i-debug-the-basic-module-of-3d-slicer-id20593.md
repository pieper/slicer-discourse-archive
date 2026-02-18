# How can I debug the Basic Module of 3D Slicer?

**Topic ID**: 20593
**Date**: 2021-11-12
**URL**: https://discourse.slicer.org/t/how-can-i-debug-the-basic-module-of-3d-slicer/20593

---

## Post #1 by @kookoo9999 (2021-11-12 01:03 UTC)

<p>Hi,<br>
I am making my moudle via 3D Slicer. I want to save text file of HounsFiled Unit that I had segmented by using Segmentation , Segmentation Editor in 3D Slicer.<br>
but I don’t know segmentation algorithm well. so I tried to debug Segmentation module <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html" rel="noopener nofollow ugc">this way</a> .</p>
<p>but I can’t find AdditionalLauncherSettings.ini in C:\D\S4RS\Slicer-build\Modules\Loadable\Segmentations.</p>
<p>When I debug my moudle , there was a AdditionalLauncherSettings.ini in my moudle’s directory.</p>
<p>Thanks for reading, have a nice day!</p>
<p>I am working on Windows10,Visual Studio2019 , Slicer-master (Release).</p>

---

## Post #2 by @kookoo9999 (2021-11-12 04:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6850468b09bd4e8241460f7f7cf3d0526035c9cd.jpeg" data-download-href="/uploads/short-url/eSNE5dwtBuwwlTfN3ONnJg0bdtH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6850468b09bd4e8241460f7f7cf3d0526035c9cd_2_690x374.jpeg" alt="image" data-base62-sha1="eSNE5dwtBuwwlTfN3ONnJg0bdtH" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6850468b09bd4e8241460f7f7cf3d0526035c9cd_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6850468b09bd4e8241460f7f7cf3d0526035c9cd_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6850468b09bd4e8241460f7f7cf3d0526035c9cd_2_1380x748.jpeg 2x" data-dominant-color="8F9096"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1042 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I want hounsfield unit value of the blue part of the 3D View in the picture and save the text file.<br>
I’m also curious about the algorithm until the segmented image is displayed in the 3D View on the right. I’ve read the MRML node part, but I’m not sure how to debug it. If only the segmented video part is accessible in my module, I want to save only the HU value of the necessary area separately.</p>

---

## Post #3 by @lassoan (2021-11-12 06:15 UTC)

<p>Getting intensity values, computing histogram, etc. is the easiest to do in Python (it takes about 5 lines of code). See a full example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">script repository</a>.</p>
<aside class="quote no-group" data-username="kookoo9999" data-post="1" data-topic="20593">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kookoo9999/48/12394_2.png" class="avatar"> kookoo9999:</div>
<blockquote>
<p>When I debug my moudle , there was a AdditionalLauncherSettings.ini in my moudle’s directory.</p>
</blockquote>
</aside>
<p>No additional launcher settings are needed for core modules, such as Segmentations (they are included in the regular launcher settings).</p>

---

## Post #4 by @kookoo9999 (2021-11-12 06:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  Thank you for your kind reply every time. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I’ll try through the link you wrote.</p>
<p>I’m not familiar with other languages, platforms, andides other than c++ and Visual Studio, so I’m reading and studying the Slicer document part every day about the loadable module.Please understand that there are many questions.</p>
<p>How is it possible when I use the results I’ve processed in another module in My module? I’ve read the MRML node part, but I don’t know how to use it. Can you do Slicer Tutorial with Video or Picture?</p>

---

## Post #5 by @pieper (2021-11-12 14:57 UTC)

<p>Not to say there is anything bad or wrong with C++, but it will be very valuable to your understanding of 3D Slicer to learn the python interface.  It allows you to probe the structure of the program and understand the architecture in ways that are effectively impossible to do with C++.  Working through the python tutorials will help you even if you ultimately develop your cod in C++.</p>

---

## Post #6 by @kookoo9999 (2021-11-13 05:28 UTC)

<p>Thanks.<br>
I thought it was necessary to learn python by simply modifying the logic of storing HU as a txt file, referring to the place where Lasoan linked yesterday.</p>

---

## Post #7 by @kookoo9999 (2021-11-22 15:30 UTC)

<p>I tried to write the code <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" rel="noopener nofollow ugc">script repository</a> and checked the HU for test logic semented volume from import sampledata.<br>
how can I do for volume that I segmented by using segmented module and volume??</p>

---

## Post #8 by @kookoo9999 (2021-11-22 16:47 UTC)

<p>If I do make segmented volume and I want to get its HU,How do I write the code??<br>
When I use import SampleData , I get only SampleData’s HU…</p>

---

## Post #9 by @kookoo9999 (2021-11-23 01:06 UTC)

<p>Thanks for your reply.<br>
If I want to use Slicer’s scene or segmentation or volume etc…<br>
What can I use library or header or class and How can I use that (ex : <span class="hashtag">#include</span> &lt;opencv2/opencv.hpp&gt;  cv::Mat test …) or refer this??</p>

---

## Post #10 by @kookoo9999 (2021-11-23 01:08 UTC)

<aside class="quote no-group" data-username="kookoo9999" data-post="8" data-topic="20593">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kookoo9999/48/12394_2.png" class="avatar"> kookoo9999:</div>
<blockquote>
<p>I get only SampleData’s HU…</p>
</blockquote>
</aside>
<p>this mean I want segmented volume’s HU not sampleData’s HU like this picture (HU at x,y,z,HU)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15e780bd8c77b6ec21df2e2027f56262b9cb587e.png" alt="image" data-base62-sha1="37M1d6BIEi67zsH8r5nZgGDOp42" width="404" height="178"></p>

---
