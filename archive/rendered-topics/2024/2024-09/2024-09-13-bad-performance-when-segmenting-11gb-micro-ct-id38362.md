# Bad performance when segmenting 11GB micro-CT

**Topic ID**: 38362
**Date**: 2024-09-13
**URL**: https://discourse.slicer.org/t/bad-performance-when-segmenting-11gb-micro-ct/38362

---

## Post #1 by @JaredAmudeo (2024-09-13 04:55 UTC)

<p>Hi!<br>
I am currently trying to segment some fossil material on a new desktop PC with the following specs:<br>
Lenovo ThinkStation<br>
Windows 11 Pro, Intel Xeon Silver 4208, 128 GB DDR4 (2400 MHz) RAM, Nvidia RTX A5000 24 GB, and a 512 GB NVMe SSD. The material in question is a stack of TIFF images obtained from micro-CT with a total resolution of almost 11 GB. I expected to work smoothly, but when navigating within segmentations, rendering volume, editing in 3D view, and most annoyingly when saving and exporting data, Slicer works slowly, gets stuck, and saving can take more than 10 minutes. Is there any way to improve performance, or could there be an issue with the hardware?</p>
<p>Thanks!.</p>

---

## Post #2 by @muratmaga (2024-09-13 05:43 UTC)

<p>There are many ways to improve the performance. But first you have to understand the memory usage during segmentation. If your volume is 11GB in size, during the segmentation (depending on the effect), Slicer may use 6-10 times more (so 60-100GB) transiently. That’s already at the limit of available memory on your computer. Adding another segment or five will increase even further. So while your computer is fairly powerful, your dataset is also quite big.</p>
<p>There are many ways to deal with that. For example, it is possible that while your full dataset is huge, perhaps you are only segmenting a portion of it (e.g., skull from a whole fish). Then all your operations will run faster, if you first crop your volume to the area you are going to segment (or only import that section).</p>
<p>As for the slowness during the save/exporting, that’s because Slicer by default compresses the data. Compression of 11GB file does take a while because it is a single threaded task. So to benefit from the fast NVMe disk, disable compression when saving/exporting (if you are using SlicerMorph you can enable the <strong>SlicerMorph customizations</strong>, which will disable the compression automatically for volume objects).</p>
<p>Your GPU is powerful enough that volume rendering should not be a problem. But volume rendering is not used during segmentation. Show3D button creates polydata (aka 3D model). That may take sometime for large dataset. To improve its performance, you can choose use new 3D model generation algorithm -Surface Nets, and the faster smoothing options).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a5870a00e12c431c82f2bb314efef16e5b5a4f5.png" data-download-href="/uploads/short-url/8k9aQEDLihhwQv8Bek8HnOrZTGB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a5870a00e12c431c82f2bb314efef16e5b5a4f5_2_690x203.png" alt="image" data-base62-sha1="8k9aQEDLihhwQv8Bek8HnOrZTGB" width="690" height="203" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a5870a00e12c431c82f2bb314efef16e5b5a4f5_2_690x203.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a5870a00e12c431c82f2bb314efef16e5b5a4f5_2_1035x304.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a5870a00e12c431c82f2bb314efef16e5b5a4f5_2_1380x406.png 2x" data-dominant-color="9AA3A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1410×416 77.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You should really check the SlicerMorph tutorials we have for segmentation to understand the types of issues you are facing and how to solve them:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation" target="_blank" rel="noopener nofollow ugc">Tutorials/Segmentation at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @JaredAmudeo (2024-09-13 06:08 UTC)

<p>Thank you very much for the prompt response! I will soon put into practice what you told me to adapt to the situation and be able to deal with the issue.</p>

---

## Post #4 by @lassoan (2024-09-13 12:36 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> this is an excellent summary. I’m wondering how to make this easier for new users.</p>
<p>I’ve submitted a <a href="https://github.com/SlicerMorph/SlicerMorph/pull/343">pull request</a> with a small change to ImageStacks extension to disable compression by default.</p>
<p>What is your experience with Surface Nets? I’ve only tried it a couple of times and it worked very nicely for me (with surface net smoothing). Should it be the default?</p>
<p>To advise the user on potential performance issues, we could display a message in the Segment Editor when the source image is very large (e.g., larger than 1GB or more than 10% of the available RAM). The message could contain a link that takes the user to a Slicer documentation page that explains the problem and potential solutions. Maybe it could have a button to change the segmentation geometry to be lower resolution than the source volume (e.g., make the resolution 1/2 … 1/4 along each axis to avoid having more than 512 voxels along that axis). If segmentation is only used for coloring or volume measurement then it would be no problem to have much lower resolution.</p>

---

## Post #5 by @muratmaga (2024-09-13 15:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is your experience with Surface Nets? I’ve only tried it a couple of times and it worked very nicely for me (with surface net smoothing). Should it be the default?</p>
</blockquote>
</aside>
<p>Anything larger than toy data, I enable the surfacenets. I did not notice much of a difference in the models generated compared to the current default. So I have no objection making it the default.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To advise the user on potential performance issues, we could display a message in the Segment Editor when the source image is very large (e.g., larger than 1GB or more than 10% of the available RAM).</p>
</blockquote>
</aside>
<p>I think a warning like this probably would be useful. But I would not mess with the geometry. In my field, one reason to acquire such high-resolution dataset is to represent small structures in sufficient detail, which are often only 1-5 times thicker than image resolution. I think letting the user to know of the issues and offering some solutions (for them to decide which way to go) is probably the safest alternative.</p>

---

## Post #6 by @lassoan (2024-09-14 15:27 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="5" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is your experience with Surface Nets? I’ve only tried it a couple of times and it worked very nicely for me (with surface net smoothing). Should it be the default?</p>
</blockquote>
</aside>
<p>Anything larger than toy data, I enable the surfacenets. I did not notice much of a difference in the models generated compared to the current default. So I have no objection making it the default.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> What do you think about making surfacenets the default (maybe after releasing Slicer-5.8)?</p>
<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think a warning like this probably would be useful. But I would not mess with the geometry. In my field, one reason to acquire such high-resolution dataset is to represent small structures in sufficient detail, which are often only 1-5 times thicker than image resolution. I think letting the user to know of the issues and offering some solutions (for them to decide which way to go) is probably the safest alternative.</p>
</blockquote>
</aside>
<p>The popup could have buttons like “Ignore” (do nothing), “Reduce resolution” (change segmentation geometry), “More information” (open documentation page where the problem and solutions are explained in detail).</p>
<p>People may not realize that for most of the tasks, the segmentation does not have to be as accurate as the underlying data. For example, if the goal is visualization, or volume or surface measurement, then 1/4 resolution (64x less data) is probably perfectly fine.</p>
<p>Even for 3D printing, we could use segmentation for masking and then use “Grayscale model maker” (or maybe some new specialized module) to get smoother and more detailed models than from a full-resolution segmentation.</p>
<p>Maybe we should do a small study and write a paper on these? This could be very impactful, because it could prove that tasks that people thought would require a high-end workstation could be done on any laptop.</p>

---

## Post #7 by @chir.set (2024-09-14 16:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>tasks that people thought would require a high-end workstation could be done on any laptop.</p>
</blockquote>
</aside>
<p>I wish to add a little note on this particular topic.</p>
<p>Working with segmentations on any modern laptop is fine and will be smooth, even without prior cropping. In my context, I use Slicer in 2 main situations at work: during consultation and in pre(/post)-operative assessment. In the latter case, I’m in no hurry. In the former case, things have to be fast, CPU and GPU power do count. Segmentation and discrete measurements rarely fit in the time frames. It’s volume rendering the main visualisation tool. The dimensions of a common CT study is 512x512x2048 <strong>+</strong>, it must be rendered in one click at best, which requires a good GPU card. A poor graphics card may (often) render a volume with less than 2048 slices as such, else it has to be cropped before (that’s why I wrote <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/TemplateROICrop?ref_type=heads" rel="noopener nofollow ugc">this</a> of old).</p>
<p>My point is: if people buy a new machine <em>for</em> Slicer, look for a high-end, they will definitely need it at some point, the more so if they are geeky and invest in Slicer. But they can still do a lot of wonderful things with a &lt;5 years old laptop, agreed.</p>

---

## Post #8 by @pieper (2024-09-14 17:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What do you think about making surfacenets the default (maybe after releasing Slicer-5.8)?</p>
</blockquote>
</aside>
<p>Yes, I think this is a good idea.</p>

---

## Post #9 by @muratmaga (2024-09-14 18:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The popup could have buttons like “Ignore” (do nothing), “Reduce resolution” (change segmentation geometry), “More information” (open documentation page where the problem and solutions are explained in detail).</p>
</blockquote>
</aside>
<p>This might work.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>People may not realize that for most of the tasks, the segmentation does not have to be as accurate as the underlying data. For example, if the goal is visualization, or volume or surface measurement, then 1/4 resolution (64x less data) is probably perfectly fine.</p>
</blockquote>
</aside>
<p>There is really no one use case here. For some people it is building a 3D model of a specific anatomical structure (without actually needing to measure it volume/SA), possibly to do shape analysis. For others, for example in cases of fossil, is to extract a bone fragment inside a matrix, or another bone. I will be more inclined to handle this via documentation. I am not sure about writing a paper, but I did long ago, demonstrate with some toy data how little volume estimate of a segment changes if it is full vs 1/2 vs 1/4 resolution. I can try to dig that up, and maybe include in the same documentation (i.e., for people whose goals is to get volumes).</p>
<aside class="quote no-group" data-username="chir.set" data-post="7" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>f people buy a new machine <em>for</em> Slicer, look for a high-end,</p>
</blockquote>
</aside>
<p>I think the current issue is the out-of-the-box default settings for Slicer does not work well with large dataset, giving an first-impression of Slicer not working well on a powerful computer, where one expects things to work fluidly. Number one culprit for this is the compression. We really need to go down the route of parallel compression/decompression if compression needs to be continued to be enabled by default.</p>

---

## Post #10 by @lassoan (2024-09-14 20:33 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>if compression needs to be continued to be enabled by default</p>
</blockquote>
</aside>
<p>Disabling compression by default for scalar volumes should be no problem. You only get about 50% compression anyway, which rarely matters.</p>
<p>For labelmap volumes and segmentations the compression can be easily 100000%, so that may worth some extra time.</p>
<p>The main issue is reading images from standard zip files. As far as I remember, unless the zip files are saved in multiple streams, parallel unzip implementations are not much faster and you dont have random access (need to uncompress everything up to the byte you want to access). If you use special “modern” compressed file formats then you lose compatibility with practically every other software. I hope that ome-ngff will help - as modern file format that many software supports - but we are not there yet.</p>

---

## Post #11 by @muratmaga (2024-09-16 17:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The main issue is reading images from standard zip files. As far as I remember, unless the zip files are saved in multiple streams, parallel unzip implementations are not much faster and you dont have random access (need to uncompress everything up to the byte you want to access). If you use special “modern” compressed file formats then you lose compatibility with practically every other software. I hope that ome-ngff will help - as modern file format that many software supports - but we are not there yet.</p>
</blockquote>
</aside>
<p>I thought all volumetric data compressed via gzip, and zip is only used during the MRB? Am I wrong?</p>
<p>If that’s indeed the case, one solution would be to compress the data inside the MRB via parallel compression prior to packing and create the MRB with minimal to no compression.</p>
<p>Hopefully ome-ngff will help as you said, but that appears it will take a while.</p>

---

## Post #12 by @pieper (2024-09-16 19:03 UTC)

<p>Yes, gzip is used for nrrd files and zip is used for MRB.</p>
<p>I understand there is work in progress to formalize representation of image geometry as part of ome-ngff, but it doesn’t seem to be a priority for that community.</p>
<p>If we wanted to add a new file type that uses zarr under the hood we could easily define our own conventions and probably hugely speed up load/save for large volumes with parallel codecs.</p>

---

## Post #13 by @lassoan (2024-09-16 23:02 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="11" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I thought all volumetric data compressed via gzip, and zip is only used during the MRB? Am I wrong?</p>
</blockquote>
</aside>
<p>One is using libarchive, the other uses zlib. I don’t think there is a significant difference between them in term of speed or compression rate.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="11" data-topic="38362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If that’s indeed the case, one solution would be to compress the data inside the MRB via parallel compression prior to packing and create the MRB with minimal to no compression.</p>
</blockquote>
</aside>
<p>Do you only have problems with saving speed if using MRB?</p>
<p>MRB zipping is already done without any compression, so it should be reasonably fast. What could be improved is to not recompress an image if the image has not been modified since it was read, but simply copy over the source file. However, this would be a bit risky, as it is hard to guarantee that the file the image was read from has not been modified on disk after reading was completed.</p>

---
