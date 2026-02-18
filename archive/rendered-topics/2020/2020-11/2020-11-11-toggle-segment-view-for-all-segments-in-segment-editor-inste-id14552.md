# Toggle segment view for all segments in segment editor instead of segmentations module

**Topic ID**: 14552
**Date**: 2020-11-11
**URL**: https://discourse.slicer.org/t/toggle-segment-view-for-all-segments-in-segment-editor-instead-of-segmentations-module/14552

---

## Post #1 by @pr4deepr (2020-11-11 22:55 UTC)

<p>HI<br>
Is it possible to toggle visibility of all segments in Segment Editor?<br>
In segment editor, I right click on a segment of interest and click  “Show only selected segments"to view my segment of interest and correct the annotation. Once I’m done, I would like to view all segmentations in Segment Editor module instead of going to segmentations module. If it was a few segments, then it wouldn’t matter, but when I’m annotating &gt;20-30 objects it does become quite cumbersome. Is there a way for this already?</p>
<p>Thanks a lot.</p>
<p>Cheers<br>
Pradeep</p>

---

## Post #2 by @lassoan (2020-11-12 00:41 UTC)

<p>I think the use case of bulk show/hide “all other segments” has not come up before. Can you tell why do you want to show only a single segment? Do all those segment overlap with your current segment and therefore it decreases its visibility? Or do you do this for performance reasons? (Is update is slower if you show more segments? It should not be)</p>

---

## Post #3 by @pr4deepr (2020-11-12 00:57 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks for your reply.</p>
<p>Its mostly because I use Fill between Slices option to create a segment and since that works on only the visible segment, I need to toggle visibility of all other segments off to use this option. After I am done, I want to see all other segments to figure out which ones I need to correct  or add. I need to switch between segmentation and segment editor modules to do this.</p>
<p>Example image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e86949eb03d5865db7be45ddb1b7b9f6d1d526e7.jpeg" data-download-href="/uploads/short-url/xa0lTPAWtaD9IDOJ7wuk8Jaqw0T.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86949eb03d5865db7be45ddb1b7b9f6d1d526e7_2_690x371.jpeg" alt="image" data-base62-sha1="xa0lTPAWtaD9IDOJ7wuk8Jaqw0T" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86949eb03d5865db7be45ddb1b7b9f6d1d526e7_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86949eb03d5865db7be45ddb1b7b9f6d1d526e7_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86949eb03d5865db7be45ddb1b7b9f6d1d526e7_2_1380x742.jpeg 2x" data-dominant-color="696969"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1901×1024 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14552">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do all those segment overlap with your current segment and therefore it decreases its visibility?</p>
</blockquote>
</aside>
<p>Yes,  this is another reason as well.</p>
<p>If you think there is a better approach than using Fill between slices, please do let me know.</p>
<p>Thanks</p>
<p>Pradeep</p>

---

## Post #4 by @lassoan (2020-11-12 01:11 UTC)

<p>I guess you mean “Grow from seeds” - the attached image contains small blobs, which are not well suited for “Fill between slices”. Anyway, both these effects can process any number of visible segments at once, so it should not be necessary to define segments one by one.</p>
<p>A simple way to segment images like this can be to generate seed points by Thresholding and Islands split. If sometimes blobs are fused together then you can use a higher threshold value (so high that blobs are not connected anymore), then run Grow from seeds on the result (to get the complete blob from the small seed).</p>

---

## Post #5 by @pr4deepr (2020-11-12 02:03 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks for the suggestion, this is really handy for images I label from scratch.</p>
<p>Apologies, I was not clear, but for most of the images I get label predictions from a different program and correct it in 3D Slicer, so Fill between slices is a quick way to add a few more labels or correct labels. Currently, I use paint or level tracing to create segments, and then use Fill between slices+Smoothing to complete it. So, if  the mask/label I imported already had 50 objects, I would like to hide all of them to activate Fill between slices to make a new segment and then re-display them after.</p>
<p>Hope it is clearer now.</p>
<p>Cheers<br>
Pradeep</p>

---

## Post #6 by @lassoan (2020-11-12 06:29 UTC)

<p>Showing/hiding segments and using “Fill between slices” should not be necessary for this segmentation task. Most likely you can fix all these blobs at once, by keeping all of them displayed and adding a “background” segment, and applying “Grow from seeds” effect. You probably don’t need the label predictions from another program, because you can generate seeds by thresholding and island splitting. You may also try local thresholding (in SegmentEditorExtraEffects extension).</p>
<p>If you can share a volume (upload to dropbox/onedrive/google drive and post the link here) then you can get more specific advice.</p>

---

## Post #7 by @pr4deepr (2020-11-13 01:07 UTC)

<p>Thanks for that.<br>
Its a small image which can be found here:</p>
<p><a href="https://www.dropbox.com/s/mec1jegwx4ta31r/dapi_20-50.tif?dl=0" rel="noopener nofollow ugc">Image download link</a></p>
<p>To give more context and make sure I’m clear. I use 3D slicer to generate labelmaps which are then used as ground truth for training deep learning models to automate image segmentation tasks.<br>
The seed thresholding and island splitting is a really good idea. I am so used to ImageJ that I am still getting my head around workflows in 3D Slicer. Thanks, I have installed the SegmentEditorExtraEffects extension.<br>
Would you mind having a look at the dataset I uploaded and let me know if you have any other suggestions? I do appreciate that the image is quite small and noisy.</p>
<p>Thanks<br>
Pradeep</p>

---

## Post #8 by @lassoan (2020-11-13 16:11 UTC)

<p>Thank you for the sample image, it helped a lot in understanding the task and challenges. These images are different from usual 3D clinical images in that objects can overlap in the 3D space, so you will need some manual work to review and resolve these overlaps.</p>
<p>You can get a good starting point by automatically generating seeds and growing them:</p>
<ul>
<li>Add segment</li>
<li>Thresholding effect: select range 10000 to maximum, click Apply (these will be the basis of seed points)</li>
<li>Smoothing effect: Median, 3mm (removes small speckles, fill small holes)</li>
<li>Margin: Shrink, 1mm (splits connected seeds, but needs to be used carefully, as it can also remove small seeds)</li>
<li>Islands: Split islands to segments, Minimum size: 10 voxels</li>
<li>Grow from seeds effect: in Masking section, check “Editable intensity range”, set range 5000 to maximum, click initialize, then Apply</li>
<li>Smoothing: Joint smoothing method</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f16106673ba8ded9a4a68e2413f8b2c09d279431.jpeg" data-download-href="/uploads/short-url/yrkWCxkj2SJaqJ5ManWkiUyD7Ut.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f16106673ba8ded9a4a68e2413f8b2c09d279431_2_535x500.jpeg" alt="image" data-base62-sha1="yrkWCxkj2SJaqJ5ManWkiUyD7Ut" width="535" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f16106673ba8ded9a4a68e2413f8b2c09d279431_2_535x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f16106673ba8ded9a4a68e2413f8b2c09d279431_2_802x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f16106673ba8ded9a4a68e2413f8b2c09d279431_2_1070x1000.jpeg 2x" data-dominant-color="4B4C4F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1094×1021 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>These may seem like a lot of steps, but once you experimented with it manually and know what parameters work the best, you perform all the steps fully automatically by a Python script.</p>
<p>You might consider reducing noise in the image and use that as master volume, especially for the last “Grow from seeds” step. To do this noise filtering, first you need to cast the image to float using Cast scalar volume module, then use Simple Filters module - Gradient anisotropic smoothing filter. There are many other noise reduction filters in Simple Filters module that you might try.</p>
<p>Unfortunately, these automated processing needs manual fixing, mostly splitting of fused segments. If you can see fused blobs in the 3D view then you can separate them by using Scissors effect with Masking/Editable area → Inside all segments, Operation → Fill inside. After setting this up, you can add a new segment and in circle in a 3D view the part of a segment that you want separate out into a new segment.</p>
<p>You may also find Paint tool useful, you can enable sphere brush to paint in multiple slices at once and set Editable intensity range to restrict it to bright regions.</p>

---

## Post #9 by @pr4deepr (2020-11-13 18:16 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
This is super useful and I’m already getting some nice results… This has also given me an idea on the workflows and possibilities with 3D slicer.</p>
<p>I agree that it needs some manual fixing, but this is a great start. Restricting the editing area using Masking/Editable area is really handy. Didn’t realise I could use it here.</p>
<p>Just one question, I tried Gradient Anisotropic Diffusion filter under Filtering-&gt;Denoising and it worked without casting the image to float. Is this the same as using the same filter under Simple Filters module?</p>
<p>An unrelated question, in cases of using big images, are filters in 3D Slicer GPU-accelerated or does it use the CPU mainly?</p>
<p>Thanks a lot</p>
<p>Pradeep</p>

---

## Post #10 by @lassoan (2020-11-13 18:34 UTC)

<aside class="quote no-group" data-username="pr4deepr" data-post="9" data-topic="14552">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pr4deepr/48/8810_2.png" class="avatar"> pr4deepr:</div>
<blockquote>
<p>Just one question, I tried Gradient Anisotropic Diffusion filter under Filtering-&gt;Denoising and it worked without casting the image to float. Is this the same as using the same filter under Simple Filters module?</p>
</blockquote>
</aside>
<p>Probably the Gradient anisotropic diffusion filter module does the same as Simple Filters module’s filter. I recommended Simple Filters because it has many other noise filtering modules that you can experiment with, but if you end up using gradient anisotropic diffusion then it is simpler to use that module.</p>
<aside class="quote no-group" data-username="pr4deepr" data-post="9" data-topic="14552">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pr4deepr/48/8810_2.png" class="avatar"> pr4deepr:</div>
<blockquote>
<p>An unrelated question, in cases of using big images, are filters in 3D Slicer GPU-accelerated or does it use the CPU mainly?</p>
</blockquote>
</aside>
<p>With a very few exceptions, image processing filters run on the CPU. GPU is mainly used in Slicer for rendering.</p>

---

## Post #11 by @pr4deepr (2020-11-16 01:29 UTC)

<p>Thanks for that.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="14552">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>With a very few exceptions, image processing filters run on the CPU. GPU is mainly used in Slicer for rendering.</p>
</blockquote>
</aside>
<p>Is it of interest in 3D Slicer to use GPU-accelerated filters?<br>
If so, perhaps this may be of interest?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/clEsperanto/pyclesperanto_prototype">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/clEsperanto/pyclesperanto_prototype" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/210;"><img src="https://repository-images.githubusercontent.com/248206619/483b8ade-8bcb-4b03-b632-5d65c3d9a04d" class="thumbnail" width="690" height="210"></div>

<h3><a href="https://github.com/clEsperanto/pyclesperanto_prototype" target="_blank" rel="noopener nofollow ugc">GitHub - clEsperanto/pyclesperanto_prototype: GPU-accelerated bio-image...</a></h3>

  <p>GPU-accelerated bio-image analysis focusing on 3D+t microscopy image data - GitHub - clEsperanto/pyclesperanto_prototype: GPU-accelerated bio-image analysis focusing on 3D+t microscopy image data</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
This is a project where OpenCL kernels are being translated for use in Python.<br>
This is from a GPU accelerated image processing library in ImageJ/FIJI which uses OpenCL kernels: <a href="https://clij.github.io/" rel="noopener nofollow ugc">https://clij.github.io/</a><br>
The OpenCL implementations here are being ported for use in Python. There are quite  few ITK filters in there as well.</p>
<p>Cheers<br>
Pradeep</p>

---

## Post #12 by @lassoan (2020-11-16 06:54 UTC)

<p>We haven’t had have huge success stories with GPU-acceleration in image processing filters. Maybe it is because processing speed on CPU is a problem mainly on big data sets and with complex algorithms. However, big data is not very well suited for GPU processing either, as CPU/GPU transfer time can be very significant and available GPU memory may be limited. Complex algorithms get even more complex when you want to run them efficiently on the GPU and often you need to develop a new algorithm almost from scratch. Additional difficulty is that development, debugging, and maintenance of OpenCL code requires special skillset which only a small fraction of developers have.</p>
<p>Slicer is using more and more of the GPU as ITK (and various other packages) take advantage of the GPU. We may also look into improving speed of a few specific operations that are performed very frequently and noticeably slow. But I would expect that most of the image and mesh processing operations will remain mostly on the CPU in the near term.</p>

---

## Post #13 by @pr4deepr (2020-11-16 14:00 UTC)

<p>Thanks for the detailed reply.<br>
The transfer time isn’t too bad, but when we are using the GPU in an image processing workflow it is better to chain the GPU operations together so that the transfer time is reduced. Its usually a balance between if the image sits in the memory and if so, is the transfer time and processing quicker than using the CPU.<br>
I do agree that the development and maintenance can be a specialised skillset.<br>
There is a nice list of operations that are being translated into Python here, if its of interest to yoursel or anyone else who comes across this thread in the future:<br>
</p><aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/clEsperanto/pyclesperanto_prototype/issues/15" target="_blank" rel="noopener nofollow ugc">github.com/clEsperanto/pyclesperanto_prototype</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/clEsperanto/pyclesperanto_prototype/issues/15" target="_blank" rel="noopener nofollow ugc">todo list: operation translation</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-07-15" data-time="21:58:41" data-timezone="UTC">09:58PM - 15 Jul 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/haesleinhuepf" target="_blank" rel="noopener nofollow ugc">
          <img alt="haesleinhuepf" src="https://avatars1.githubusercontent.com/u/12660498?v=4" class="onebox-avatar-inline" width="20" height="20">
          haesleinhuepf
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">I'm just trying to get organized and split all CLIJ2 operations (which might be translated to clesperanto at some point) into...</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thanks for your help again <a class="mention" href="/u/lassoan">@lassoan</a><br>
Pradeep</p>

---

## Post #14 by @pieper (2020-11-16 14:48 UTC)

<p>I did some experiments with Slicer and OpenCL a while ago using PyOpenCL.  Generally it worked very well.  In addition to the issues Andras noted, at least when I was testing this I found a wide variety of performance and feature support across platforms (probably some drivers were buggy) so code that worked well on one machine was slow or just didn’t work on another.</p>
<p>That said, I agree with the overall goal of processing on the best hardware available and keeping the data in memory close to where it will be rendered.  The code linked below has example segmentation and volume rendering kernels.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="dfu2gugHLHs" data-video-title="growcutcl.mov" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=dfu2gugHLHs" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/dfu2gugHLHs/maxresdefault.jpg" title="growcutcl.mov" width="" height="">
  </a>
</div>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerCL">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerCL" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/600d93fffb1aba4874bb4d4526288281362da35be2c0561658dff712bc6e164d/pieper/SlicerCL" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerCL" target="_blank" rel="noopener">GitHub - pieper/SlicerCL: Extensions for Slicer that use OpenCL</a></h3>

  <p>Extensions for Slicer that use OpenCL. Contribute to pieper/SlicerCL development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>(yikes, was it really 9 years ago??)</p>

---

## Post #15 by @JohnMiles (2020-11-18 12:01 UTC)

<p>Useful topic for me, useful information to be applied in my laboratory, thanks to all! <a href="https://www.buyessayscheap.com/research-paper-writing-service.html" rel="noopener nofollow ugc"><img src="https://emoji.discourse-cdn.com/twitter/handshake.png?v=9" title=":handshake:" class="emoji only-emoji" alt=":handshake:"></a></p>

---

## Post #16 by @Bethrg (2022-01-22 23:40 UTC)

<p>Hello,</p>
<p>It looks like this thread theme changed a bit, so circling back, I also need to frequently turn off/toggle between many segments at a time. In my case it is because it is very busy/lots of overlap. Is there a quick way to do this without unclicking each one in the data section?</p>
<p>PS. Awesome program, and all these threads have been super helpful as I’ve been learning!</p>

---

## Post #17 by @lassoan (2022-01-25 15:21 UTC)

<p>There are lots of ways to achieve this. You can move group of segments temporarily into another segmentation so that you can show/hide them with a single click. You can also assign a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts">keyboard shortcut</a> to show/hide that separate segmentation or to show/hide a custom list of segments. For example, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-keyboard-shortcut-for-toggling-visibility-of-a-set-of-segments">this script toggles visibility of completed segments</a>.</p>

---

## Post #18 by @Bethrg (2022-01-26 04:36 UTC)

<p>Thanks so much! I’ve move to other segments before as a work around, but the other tips are very helpful.</p>

---
