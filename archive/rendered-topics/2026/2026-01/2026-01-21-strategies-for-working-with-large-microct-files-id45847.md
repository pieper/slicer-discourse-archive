---
topic_id: 45847
title: "Strategies For Working With Large Microct Files"
date: 2026-01-21
url: https://discourse.slicer.org/t/45847
---

# Strategies for working with large microCT files

**Topic ID**: 45847
**Date**: 2026-01-21
**URL**: https://discourse.slicer.org/t/strategies-for-working-with-large-microct-files/45847

---

## Post #1 by @Antmaker (2026-01-21 01:23 UTC)

<p>Hi,</p>
<p>I am working with microCT tiff stacks and currently it is 75GB when read into the software at full resolution. Following the general guideline of using a hardware with RAM 6x-10x that of the file is not attainable especially with the current global memory shortage. I have been fortunate enough to get my hands on an HPC with 800GB of RAM and thus am able to do basic segmentation using the thresholding tool. However, it still takes a quite a while to convert the segments into 3D so that I can verify the segmentation.</p>
<h2><a name="p-131383-things-ive-tried-1" class="anchor" href="#p-131383-things-ive-tried-1" aria-label="Heading link"></a>Things I’ve tried:</h2>
<ul>
<li>Loading at half-resolution and remove the extra structures using ROI, then load the ROI in full-resolution. This reduces my file size, but not by much.</li>
<li>Reviewed posts such as:
<ul>
<li><a href="https://discourse.slicer.org/t/recommended-hardware-for-a-very-large-ct-segmentation/17482">Recommended hardware for a very large CT segmentation</a></li>
<li><a href="https://discourse.slicer.org/t/working-with-large-datasets/2469">Working with large datasets</a></li>
</ul>
</li>
</ul>
<h2><a name="p-131383-questions-2" class="anchor" href="#p-131383-questions-2" aria-label="Heading link"></a>Questions:</h2>
<ul>
<li>If I don’t use any semi-automated segmenting tools, could I subset the object using ROI into sections to do my segmentation and then combine the segmentation from each section together afterwards? This way I will only have to work with 1/4 of the data at a time.</li>
<li>What other strategies or recommendations are there for segmenting with very large files?</li>
</ul>
<p>Thanks,</p>

---

## Post #2 by @muratmaga (2026-01-21 04:26 UTC)

<aside class="quote no-group" data-username="Antmaker" data-post="1" data-topic="45847">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/antmaker/48/81424_2.png" class="avatar"> Antmaker:</div>
<blockquote>
<p>75GB when read into the software at full resolution.</p>
</blockquote>
</aside>
<p>That’s a very large dataset.</p>
<aside class="quote no-group" data-username="Antmaker" data-post="1" data-topic="45847">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/antmaker/48/81424_2.png" class="avatar"> Antmaker:</div>
<blockquote>
<p>Loading at half-resolution and remove the extra structures using ROI, then load the ROI in full-resolution. This reduces my file size, but not by much.</p>
</blockquote>
</aside>
<p>That’s interesting, so you can’t really trim much of the data then? When I use this methods, I often get my dataset less than 50% of the original size.</p>
<aside class="quote no-group" data-username="Antmaker" data-post="1" data-topic="45847">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/antmaker/48/81424_2.png" class="avatar"> Antmaker:</div>
<blockquote>
<p>could I subset the object using ROI into sections to do my segmentation and then combine the segmentation from each section together afterwards? This way I will only have to work with 1/4 of the data at a time.</p>
</blockquote>
</aside>
<p>If you need to work on the full dataset, yes, that’s the best solution. Maybe do more than 4. The important part is to make note of the threshold range you are using so that it remains consistent across the data.</p>
<p>But in the end, converting such segmentations into 3D models (if you are doing that) will be slow regardless. If you don’t need the 3D models, you might consider using Colorize Volume to color render the volume with your segmentations. However, at this point there are no commercial GPU out there that will fit your data, including those $40K ones (when you use RGBA rendering on full resolution 75GB dataset, you need a GPU with 300GB of RAM, which currently doesn’t exist).</p>
<aside class="quote no-group" data-username="Antmaker" data-post="1" data-topic="45847">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/antmaker/48/81424_2.png" class="avatar"> Antmaker:</div>
<blockquote>
<p>What other strategies or recommendations are there for segmenting with very large files</p>
</blockquote>
</aside>
<p>If you tell us what your dataset, what you are segmenting, and what your end goal is we might be able to suggest other things. But at this point, I think you already figured out your options.</p>

---

## Post #3 by @arumiat (2026-01-21 16:04 UTC)

<p>Use a tool like FijiJ (ImageJ) to resize the images. May also be able to crop them initially and then resize. Can bring down dataset size a lot</p>

---

## Post #4 by @muratmaga (2026-01-21 16:19 UTC)

<aside class="quote no-group" data-username="arumiat" data-post="3" data-topic="45847">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f05b48/48.png" class="avatar"> arumiat:</div>
<blockquote>
<p>FijiJ (ImageJ) to resize the images.</p>
</blockquote>
</aside>
<p>All of that can be done in Slicer with ImageStacks and CropVolume. Fiji doesn’t provide anything more, but causes more trouble (such as not recording the crop offset or correct image scale after resizing). I would not recommend using Fiji for this purpose.</p>

---

## Post #5 by @arumiat (2026-01-22 12:38 UTC)

<p>Been a while since Ive needed to do it but FijiJ made very large microCT datasets workable for me, in the situations where I couldn’t perform any manipulation in Slicer. I seem to remember their virtual stack function being very useful.</p>
<p>I found these notes, in case is helpful to OP:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1978b364e4cf8f9f3803fcf4d04fa8521504ce9.png" data-download-href="/uploads/short-url/tU8thX5CF9OeG1VYTa3XqhxkYQh.png?dl=1" title="notes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1978b364e4cf8f9f3803fcf4d04fa8521504ce9_2_690x397.png" alt="notes" data-base62-sha1="tU8thX5CF9OeG1VYTa3XqhxkYQh" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1978b364e4cf8f9f3803fcf4d04fa8521504ce9_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1978b364e4cf8f9f3803fcf4d04fa8521504ce9_2_1035x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1978b364e4cf8f9f3803fcf4d04fa8521504ce9_2_1380x794.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">notes</span><span class="informations">1457×840 99.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2026-01-22 16:33 UTC)

<p>The first part is the exactly the same functionality of ImageStacks, which provides many additional features not found in the Fiji, more convenient, and more importantly allows you to reimport the data correctly multiple times, without losing spatial relationship of the any subvolumes you might have created. You cannot do any of those in Fiji (not easily).</p>
<p>For workflow 2 if you want to load a dataset that’s beyond your computers memory size, you can increase the virtual memory of your own computer (which will be equivalent to using the virtual stack option) there.</p>

---

## Post #7 by @Antmaker (2026-02-10 00:18 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/arumiat">@arumiat</a>, thank you both for such great and detailed suggestions. I have made some progress in my workflow by incorporating suggestions you made here and other posts in combination with my trial-and-error.</p>
<p>I’m going to recap the discussion here for future readers.</p>
<h3><a name="p-131864-objective-use-case-1" class="anchor" href="#p-131864-objective-use-case-1" aria-label="Heading link"></a>Objective / Use case</h3>
<p>Segment medical device microCT scans that contain non-organic (plastic, metal, etc) and organic (blood clots) components/substances and quantify the statistics (esp. volume) of each segmented components.</p>
<h3><a name="p-131864-challenge-2" class="anchor" href="#p-131864-challenge-2" aria-label="Heading link"></a>Challenge</h3>
<p>The image stacks are large (approximately 70GB-80GB) and the segments are non-continuous (scattered like stars in the night sky). Because of how large the model size is, the computer takes a long time to do a simple segment by threshold and “Show 3D” feature will crash the application even when running with ~800GB of RAM.</p>
<h3><a name="p-131864-current-solutions-3" class="anchor" href="#p-131864-current-solutions-3" aria-label="Heading link"></a>Current solution(s)</h3>
<ul>
<li>
<p>Create pseudo-ROI using <a href="https://discourse.slicer.org/t/cropping-a-cylindrical-volume-jar-in-a-circular-roi/42750">“Draw tube” effect</a> and “Scissors” effect (add/remove shapes) to create the final segment for pseudo-ROI.</p>
</li>
<li>
<p>Use this pseudo-ROI as a mask by selecting it in the “Editable area” dropdown menu of the “Masking” tab when any of the “Segment Editor” effects is selected.</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05654e384890843b89ccdbb3e7daad228df00db0.png" data-download-href="/uploads/short-url/LJqSjqxX88YhqhEQ8Tu7YdgHTy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05654e384890843b89ccdbb3e7daad228df00db0.png" alt="image" data-base62-sha1="LJqSjqxX88YhqhEQ8Tu7YdgHTy" width="627" height="119"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">627×119 4.15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Utilizing <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254/7">“Colorize Volume” from the “Sandbox” module</a> instead of “Show 3D” of the “Segment Editor” module to view in 3D.</li>
</ul>

---
