# Can Slicer be used for splitting and reconstructing fragmented bone?

**Topic ID**: 4715
**Date**: 2018-11-10
**URL**: https://discourse.slicer.org/t/can-slicer-be-used-for-splitting-and-reconstructing-fragmented-bone/4715

---

## Post #1 by @Raymond (2018-11-10 23:16 UTC)

<p>I downloaded Slicer years ago but decided to postpone learning it for a while. The time has come.</p>
<p>My objective is to start with a pristine cranium, perhaps in the Slicer format (NRRD?), or in one of these:</p>
<p><a href="http://www.jfknumbers.org/ich-bin-ein-berliner/osseus-models/craniums/low-resolution/" rel="noopener nofollow ugc">Cranium in Common 3D Formats</a></p>
<p>then, based on 2 existent X-rays (A/P and Lateral), carve an injury as seen below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07e082520e9f265a2d4614f17077f233305e68e5.jpeg" data-download-href="/uploads/short-url/17GlKgvv5TEGU7msQDGmr8COqkl.jpeg?dl=1" title="Cummings-Perspective" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07e082520e9f265a2d4614f17077f233305e68e5_2_690x415.jpeg" alt="Cummings-Perspective" data-base62-sha1="17GlKgvv5TEGU7msQDGmr8COqkl" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07e082520e9f265a2d4614f17077f233305e68e5_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07e082520e9f265a2d4614f17077f233305e68e5_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07e082520e9f265a2d4614f17077f233305e68e5_2_1380x830.jpeg 2x" data-dominant-color="52504A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cummings-Perspective</span><span class="informations">1733×1044 377 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does Slicer provide such capability? A tutorial would be most appreciated.</p>
<p>Thanks,</p>
<p>-Raymond<br>
<strong>JFK Numbers</strong></p>

---

## Post #2 by @lassoan (2018-11-10 23:26 UTC)

<p>With Slicer, you would normally start from a 3D CT scan of the injured cranium instead of just X-ray scans.</p>
<p>If that’s not feasible then you can certainly load a 3D model and edit using Segment Editor module (see for example this <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">craniotomy example</a>).</p>
<p>You can try to align a 3D X-ray-like volume rendering of the cranium with the X-ray projection to make the cut positions more accurate.</p>

---

## Post #3 by @Raymond (2018-11-11 03:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can try to align a 3D X-ray-like volume rendering of the cranium with the X-ray projection to make the cut positions more accurate.</p>
</blockquote>
</aside>
<p>That is a good start, but it would be terrific if it were computer-assisted. May I request that feature?</p>
<p>See here 24 frames from a PBS Nova program that displays the work that I am trying to replicate:</p>
<p><a href="http://www.jfknumbers.org/ich-bin-ein-berliner/project-freelancer-video/BU%20Cranium%20from%20PBS%20Nova/" rel="noopener nofollow ugc">Boston University Cranium Model as Shown in PBS Nova</a></p>
<p>The full video is here:</p>
<p><a href="https://www.youtube.com/watch?v=mhX1yiJ_8-0" rel="noopener nofollow ugc">PBS Nova Cold Case JFK 2013 Documentary</a></p>
<p>TIA<br>
-Raymond<br>
<strong>JFK Numbers</strong></p>

---

## Post #4 by @lassoan (2018-11-11 04:24 UTC)

<p>You can do all that is shown in the video quite easily in Slicer. You can split bone fragments using scissors tool in Segment Editor then export them to model nodes so that you can move each of them separately.</p>
<p>In the video they used a Phantom 6-DOF positioning arm to move around bone segments. Now you can buy a virtual reality headset for $300 that comes with two 6-DOF controllers to grab the bone segments and rearrange them and see all that in immersive 3D view. Similarly how you move around tools in this SlicerVirtualReality demo video: <a href="https://youtu.be/F_UBoE4FaoY">https://youtu.be/F_UBoE4FaoY</a></p>

---

## Post #5 by @Raymond (2018-11-11 05:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can do all that is shown in the video quite easily in Slicer. You can split bone fragments using scissors tool in Segment Editor then export them to model nodes so that you can move each of them separately.</p>
</blockquote>
</aside>
<p>Thanks so much, Andras. That YouTube video is impressive. Slicer has certainly made a lot of progress since I first tried it years ago.</p>
<p>I have more newbie questions. I have been using the provided data files, a filled cranium is there. However, at this point I am only interested in the cranium bone. I have models in the usual CAD formats, the documentation says that Slicer can read OBJ and STL models.</p>
<p>What is the procedure to display my models? In 3D apps, I simply select “Import”. I tried “Add Data” but nothing is displayed.</p>
<p>TIA</p>
<p>-Raymond<br>
<strong>JFK Numbers</strong></p>

---

## Post #6 by @lassoan (2018-11-11 12:53 UTC)

<aside class="quote no-group" data-username="Raymond" data-post="5" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c57346/48.png" class="avatar"> Raymond:</div>
<blockquote>
<p>I have been using the provided data files, a filled cranium is there. However, at this point I am only interested in the cranium bone.</p>
</blockquote>
</aside>
<p>You can segment the bone from CT images quite easily. See this example: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>
<aside class="quote no-group" data-username="Raymond" data-post="5" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c57346/48.png" class="avatar"> Raymond:</div>
<blockquote>
<p>I have models in the usual CAD formats, the documentation says that Slicer can read OBJ and STL models</p>
</blockquote>
</aside>
<p>You can load STL and OBJ files, for example by drag-and-dropping them to the application window. If you want to cut them then you can load it directly as segmentation by selecting “Segmentation” in the “Description” column before clicking “OK”.</p>

---

## Post #7 by @Raymond (2018-11-12 02:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can load STL and OBJ files, for example by drag-and-dropping them to the application window. If you want to cut them then you can load it directly as segmentation by selecting “Segmentation” in the “Description” column before clicking “OK”.</p>
</blockquote>
</aside>
<p>I am getting close, Andras, followed the provided example. However, I am facing two modes that seem mutually exclusive and incompatible.</p>
<p>(a) STL and OBJ files are nicely displayed, only in the 3D window. After I created a segment the scissor icon never becomes enabled.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb9f7503846c155e621da697031b54f471589366.png" data-download-href="/uploads/short-url/zTXtMjGNYCQbbEFbMMHaiufh6tw.png?dl=1" title="Slicer%20Post" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb9f7503846c155e621da697031b54f471589366_2_655x499.png" alt="Slicer%20Post" data-base62-sha1="zTXtMjGNYCQbbEFbMMHaiufh6tw" width="655" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb9f7503846c155e621da697031b54f471589366_2_655x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb9f7503846c155e621da697031b54f471589366_2_982x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb9f7503846c155e621da697031b54f471589366.png 2x" data-dominant-color="B4B6C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer%20Post</span><span class="informations">1286×981 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(b) Data downloaded and built-in. There is a cranium perfect for my purposes. The 3 orthogonal views are displayed but the most I can achieve in the 3D/perspective window is a flat surface that may be rotated. Other than drawing a line, the scissors don’t seem to cut anything.</p>
<p>TIA</p>
<p>-Raymond<br>
<strong>JFK Numbers</strong></p>

---

## Post #8 by @Raymond (2018-11-12 02:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can do all that is shown in the video quite easily in Slicer. You can split bone fragments using scissors tool in Segment Editor then export them to model nodes so that you can move each of them separately.</p>
</blockquote>
</aside>
<p>I will leave that for advanced practice. For now, I would like to encircle a region and press Delete. Hopefully the bone fragment will disappear? Or will I have to export and then remove?</p>
<p>Also, in which of the 4 windows will I be using the scissors tool?</p>
<p>TIA</p>
<p>-Ramon<br>
<strong>JFK  Numbers</strong></p>

---

## Post #9 by @lassoan (2018-11-12 03:06 UTC)

<aside class="quote no-group" data-username="Raymond" data-post="7" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c57346/48.png" class="avatar"> Raymond:</div>
<blockquote>
<p>STL and OBJ files are nicely displayed, only in the 3D window. After I created a segment the scissor icon never becomes enabled</p>
</blockquote>
</aside>
<p>You need to choose a master image. If you don’t have any image then you can generate one by exporting the segmentation node to a labelmap image (in Data module, right-click on the segmentation node and choose “Export visible segments to binary labelmap”). When you are in Segment Editor module, choose the created label volume as "Master volume.</p>

---

## Post #10 by @lassoan (2018-11-12 03:07 UTC)

<aside class="quote no-group" data-username="Raymond" data-post="8" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c57346/48.png" class="avatar"> Raymond:</div>
<blockquote>
<p>I will leave that for advanced practice. For now, I would like to encircle a region and press Delete. Hopefully the bone fragment will disappear? Or will I have to export and then remove?</p>
</blockquote>
</aside>
<p>Please follow the craniotomy example that I’ve linked above.</p>

---

## Post #11 by @Raymond (2018-11-12 03:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you don’t have any image then you can generate one by exporting the segmentation node to a labelmap image (in Data module, right-click on the segmentation node and choose “Export visible segments to binary labelmap”).</p>
</blockquote>
</aside>
<p>Prior to that, it seems that I need to “Convert Model to Segmentation Node”. I believe I found a bug. I have craniums from 2 vendors:</p>
<p>Very High Resolution: Behr Bros, Netherlands:<br>
<a href="https://behr-bros-shop.com/skull.html" rel="noopener nofollow ugc">Behr Bros. High Quality Cranium</a></p>
<p>Medium Resolution: CG Studio<br>
<a href="https://www.cgstudio.com/3d-model/human-skull-anatomy-38487" rel="noopener nofollow ugc">Human Skull - Anatomy 3D</a></p>
<p>From the first vendor I have high, med and low resolutions in OBJ and STL file formats. Using any of the 6 files, Slicer catches an exception:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a8fea932db8ec698074b2e3f3de094990c6e37.png" data-download-href="/uploads/short-url/v3vGcEqMgLpzragxgGQzNZSrXnh.png?dl=1" title="Model%20to%20Segmentation%20Fails" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a8fea932db8ec698074b2e3f3de094990c6e37_2_634x500.png" alt="Model%20to%20Segmentation%20Fails" data-base62-sha1="v3vGcEqMgLpzragxgGQzNZSrXnh" width="634" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a8fea932db8ec698074b2e3f3de094990c6e37_2_634x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a8fea932db8ec698074b2e3f3de094990c6e37_2_951x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a8fea932db8ec698074b2e3f3de094990c6e37.png 2x" data-dominant-color="B8BAC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Model%20to%20Segmentation%20Fails</span><span class="informations">1126×888 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/932ab38dce95cf0936575e91d7d5c8535db83d30.png" data-download-href="/uploads/short-url/kZTFSpJVxZ8fTquvlJcdVUmuTFS.png?dl=1" title="Bad%20Allocation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/932ab38dce95cf0936575e91d7d5c8535db83d30_2_600x500.png" alt="Bad%20Allocation" data-base62-sha1="kZTFSpJVxZ8fTquvlJcdVUmuTFS" width="600" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/932ab38dce95cf0936575e91d7d5c8535db83d30_2_600x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/932ab38dce95cf0936575e91d7d5c8535db83d30.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/932ab38dce95cf0936575e91d7d5c8535db83d30.png 2x" data-dominant-color="A7A8BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bad%20Allocation</span><span class="informations">810×674 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #12 by @Raymond (2018-11-12 04:07 UTC)

<p>All the cranium models from CG Studio are here:</p>
<p><a href="http://www.jfknumbers.org/ich-bin-ein-berliner/osseus-models/craniums/low-resolution/" rel="nofollow noopener">Cranium Models from CG Studio</a></p>
<p>I will upload the ones from Behr Bros. later.</p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #13 by @lassoan (2018-11-12 04:14 UTC)

<aside class="quote no-group" data-username="Raymond" data-post="11" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c57346/48.png" class="avatar"> Raymond:</div>
<blockquote>
<p>From the first vendor I have high, med and low resolutions in OBJ and STL file formats. Using any of the 6 files, Slicer catches an exception</p>
</blockquote>
</aside>
<p>“bad allocation” means that the operating system was not able to allocate the requested amount of memory. Increase virtual memory size in your system settings, it’ll use disk space instead of physical RAM to fulfill memory needs (of course, this is much slower than having more physical memory in your system, so if you find the software too slow then you may consider upgrading your computer with more RAM).</p>

---

## Post #14 by @Raymond (2018-11-12 04:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you may consider upgrading your computer with more RAM</p>
</blockquote>
</aside>
<p>I closed all my apps and am using the smallest of the 6 models from Behr Bros. See images:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dce48234d31b474ba92fe6a212a03cdd9a324b3b.png" data-download-href="/uploads/short-url/vw6CuXe4omHgSCfhafK3KUIbWVt.png?dl=1" title="Smallest%20Cranium%20Model%20is%20Used" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dce48234d31b474ba92fe6a212a03cdd9a324b3b.png" alt="Smallest%20Cranium%20Model%20is%20Used" data-base62-sha1="vw6CuXe4omHgSCfhafK3KUIbWVt" width="385" height="500" data-dominant-color="F0F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Smallest%20Cranium%20Model%20is%20Used</span><span class="informations">484×628 16.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72aacc7c97b44683e46f5af313f66023b18fd351.png" data-download-href="/uploads/short-url/gmomI8DPup5cGZfmxf6GEP0f3cR.png?dl=1" title="16%20GB%20RAM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72aacc7c97b44683e46f5af313f66023b18fd351_2_474x499.png" alt="16%20GB%20RAM" data-base62-sha1="gmomI8DPup5cGZfmxf6GEP0f3cR" width="474" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72aacc7c97b44683e46f5af313f66023b18fd351_2_474x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72aacc7c97b44683e46f5af313f66023b18fd351_2_711x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72aacc7c97b44683e46f5af313f66023b18fd351.png 2x" data-dominant-color="F8F8F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">16%20GB%20RAM</span><span class="informations">849×895 28.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Some of the models that succeed (from CG Studio) are bigger.</p>
<p>I will run tests tomorrow from the corporate computers at the office.</p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #15 by @lassoan (2018-11-12 04:54 UTC)

<p>16GB physical RAM should be OK, just adjust your settings to have 30GB virtual memory to make sure you don’t temporarily run out of memory in any case.</p>
<p>Size of the OBJ file does not matter, because only the only internal labelmap in the segmentation node consumes significant amount of memory. The larger the model’s physical extent and finer the resolution of the segmentation’s internal labelmap, the more memory you’ll need.</p>
<p>This should work for you:</p>
<ul>
<li>Load obj file as model (you can only load STL files directly as segmentation)</li>
<li>Import model to segmentation node in Segmentations module</li>
<li>Export segmentation to binary labelmap in Data module (by right-clicking on segmentation node)</li>
<li>Go to Segment Editor module, select the binary labelmap as master volume</li>
<li>Apply Hollow effect if you use a simplistic model (such as <a href="http://www.jfknumbers.org/ich-bin-ein-berliner/osseus-models/craniums/low-resolution/OBJ/">this</a>), where the cranium is modeled as a solid blob instead of a shell</li>
<li>Create a craniotomy as described in the page linked above (create a new segment, select Scissors effect, set masking editable area to “inside all segments”, scissors operation to “Fill inside”, draw in 3D view, etc.)</li>
</ul>

---

## Post #16 by @Raymond (2018-11-12 08:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This should work for you:</p>
<ul>
<li>Load obj file as model (you can only load STL files directly as segmentation)</li>
<li>Import model to segmentation node in Segmentations module</li>
</ul>
</blockquote>
</aside>
<p>Thanks for bearing with me, Andras. Please see below the 7 steps that I have taken, based on your first instructions above:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/908908dc2434fa1f39c20ff602345651e0dd34b1.png" data-download-href="/uploads/short-url/kCClLoNMZpHwrMRdL2IrgJMW7Lz.png?dl=1" title="1-%20Add%20Data" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/908908dc2434fa1f39c20ff602345651e0dd34b1.png" alt="1-%20Add%20Data" data-base62-sha1="kCClLoNMZpHwrMRdL2IrgJMW7Lz" width="631" height="500" data-dominant-color="F0F1F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1-%20Add%20Data</span><span class="informations">669×530 30.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will try similar variations, since the last step (Click on “Import” button) does not lead to expected outcome in the dialogs.</p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #17 by @lassoan (2018-11-12 14:21 UTC)

<p>You did well. Did you continue? What did you do? What did you expect  to happen? What happened instead?</p>

---

## Post #18 by @Raymond (2018-11-12 14:44 UTC)

<p>Being a clueless newbie, just wanted to double check.</p>
<p>BTW: I discovered a very useful module: as soon as I load my model, I select “Models”. I can see characteristics of the file, mesh type, the visibility and opacity may be adjusted. etc.</p>
<p>Will continue following your instructions.</p>
<p>Thanks,</p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1abfab4849180bf09ec97aa5cb89c7d8e26888ab.png" data-download-href="/uploads/short-url/3OD3VpSsRpFNyp6zMC3iwAS85B1.png?dl=1" title="Models%20Module" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1abfab4849180bf09ec97aa5cb89c7d8e26888ab_2_643x500.png" alt="Models%20Module" data-base62-sha1="3OD3VpSsRpFNyp6zMC3iwAS85B1" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1abfab4849180bf09ec97aa5cb89c7d8e26888ab_2_643x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1abfab4849180bf09ec97aa5cb89c7d8e26888ab_2_964x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1abfab4849180bf09ec97aa5cb89c7d8e26888ab.png 2x" data-dominant-color="CBCBDA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Models%20Module</span><span class="informations">1099×854 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @Raymond (2018-11-12 15:07 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="15" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Export segmentation to binary labelmap in Data module (by right-clicking on segmentation node)<br>
What did you do? What did you expect to happen? What happened instead?</p>
</blockquote>
</aside>
<p>After clicking on the “Import” button, I went to the “Data” module and selected the “Skull” model/node.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06a92e22aabbaed769e0ee11b7f943512606b2e7.png" data-download-href="/uploads/short-url/WVkziQlLHGh4mODGQoB5V2J8CX.png?dl=1" title="8%20-%20Cannot%20Export%20Segmentation%20to%20binary%20labelmap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a92e22aabbaed769e0ee11b7f943512606b2e7_2_690x491.png" alt="8%20-%20Cannot%20Export%20Segmentation%20to%20binary%20labelmap" data-base62-sha1="WVkziQlLHGh4mODGQoB5V2J8CX" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a92e22aabbaed769e0ee11b7f943512606b2e7_2_690x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a92e22aabbaed769e0ee11b7f943512606b2e7_2_1035x736.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06a92e22aabbaed769e0ee11b7f943512606b2e7.png 2x" data-dominant-color="C5C5D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">8%20-%20Cannot%20Export%20Segmentation%20to%20binary%20labelmap</span><span class="informations">1125×802 85.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks,</p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #20 by @Raymond (2018-11-12 15:30 UTC)

<p>I found the problem. Was missing a step:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b566b012b57daf69d2282920fed747903579cdf5.png" data-download-href="/uploads/short-url/pSKqDPAJ8IA9K0wmonQd8Sc0n4x.png?dl=1" title="9%20-%20Create%20New%20Segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b566b012b57daf69d2282920fed747903579cdf5_2_689x473.png" alt="9%20-%20Create%20New%20Segmentation" data-base62-sha1="pSKqDPAJ8IA9K0wmonQd8Sc0n4x" width="689" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b566b012b57daf69d2282920fed747903579cdf5_2_689x473.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b566b012b57daf69d2282920fed747903579cdf5_2_1033x709.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b566b012b57daf69d2282920fed747903579cdf5.png 2x" data-dominant-color="B9BACA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">9%20-%20Create%20New%20Segmentation</span><span class="informations">1196×821 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #21 by @cpinter (2018-11-12 15:40 UTC)

<p>You can go Model -&gt; Segmentation -&gt; Labelmap, all from within the Data module. In your screenshot two above, you see “Convert model to segmentation node”. It’s equivalent to creating a new segmentation and doing the import in the Segmentations module.</p>

---

## Post #23 by @Raymond (2018-11-12 18:30 UTC)

<p>Thank you so much for your kind assistance, Csaba. I will use the steps that you mentioned, but first I need to overcome what seems to be my last obstacle.</p>
<p>Could you please download the 2 files below, to replicate my work?</p>
<p><a href="http://www.jfknumbers.org/ich-bin-ein-berliner/osseus-models/craniums/low-resolution/OBJ/" rel="nofollow noopener">3D Cranium Model in OBJ Format</a></p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #24 by @cpinter (2018-11-12 18:35 UTC)

<p>I don’t see the problem. As you highlighted in the screenshot you need to select the master volume in order to do any editing. What I did:</p>
<ol>
<li>Drag&amp;drop obj into Slicer</li>
<li>In Data module right-click the model, choose ‘Convert model to segmentation node’</li>
<li>Right-click segmentation node, choose ‘Export visible segments to binary labelmap’</li>
<li>Go to Segment Editor</li>
<li>Select labelmap as master volume</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/338e818736b8fb8366a19d6c67f9ed5f8b166718.png" data-download-href="/uploads/short-url/7m5FsbTPlcy8FEsBQwrjr0oZHHG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/338e818736b8fb8366a19d6c67f9ed5f8b166718_2_689x465.png" alt="image" data-base62-sha1="7m5FsbTPlcy8FEsBQwrjr0oZHHG" width="689" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/338e818736b8fb8366a19d6c67f9ed5f8b166718_2_689x465.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/338e818736b8fb8366a19d6c67f9ed5f8b166718_2_1033x697.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/338e818736b8fb8366a19d6c67f9ed5f8b166718.png 2x" data-dominant-color="9AA69F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1283×866 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #25 by @Raymond (2018-11-12 19:31 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="24" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I don’t see the problem.</p>
</blockquote>
</aside>
<p>Great! I too overcame my last obstacle. Your 5-step method is very easy to follow and repeat.</p>
<p>In conclusion: that model that you used, from CG Studio, works fine. The scissors icon is enabled. The lack of accuracy implied by carving an injury based on 24 frames from a video remains a big issue for my particular purpose. I am considering contacting the author, Dr. Peter Cummings, to see whether he will share the 3D model shown in the PBS documentary.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123f758f853350154df2f99b67c43fecb1193cb5.jpeg" data-download-href="/uploads/short-url/2Bqyqh3uV73J9SdADgAGnePXEbj.jpeg?dl=1" title="BU%20Cranium%2006" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/123f758f853350154df2f99b67c43fecb1193cb5_2_597x500.jpeg" alt="BU%20Cranium%2006" data-base62-sha1="2Bqyqh3uV73J9SdADgAGnePXEbj" width="597" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/123f758f853350154df2f99b67c43fecb1193cb5_2_597x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/123f758f853350154df2f99b67c43fecb1193cb5_2_895x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123f758f853350154df2f99b67c43fecb1193cb5.jpeg 2x" data-dominant-color="88A0BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BU%20Cranium%2006</span><span class="informations">1086×909 66.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am currently downloading the real, high quality cranium model that I want for my project from the Behr Bros. website:</p>
<p><a href="https://behr-bros-shop.com/skull.html" rel="noopener nofollow ugc">Very High Definition 3D Cranium Model</a></p>
<p>That one is consistently crashing (a memory-related exception is being thrown). As soon as I have it in my server, I will ask for your help again. Please don’t go too far.  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #26 by @Raymond (2018-11-13 07:26 UTC)

<p>Hi Csaba:</p>
<p>I downloaded the latest versions of the Behr Bros. cranium. The OBJ files are here:</p>
<p><a href="http://www.jfknumbers.org/ich-bin-ein-berliner/osseus-models/craniums/high-resolution/OBJ/" rel="noopener nofollow ugc">High Resolution OBJ Models of a Cranium</a></p>
<p>in 3 qualities. Can you please check to see whether your PC has the same problem (a memory allocation exception is triggered) that my computer is having?</p>
<aside class="quote no-group" data-username="cpinter" data-post="24" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>In Data module right-click the model, choose ‘Convert model to segmentation node’</p>
</blockquote>
</aside>
<p>TIA,</p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8febb44cbdf7c4d41912b0c03d0f8f92da332115.png" data-download-href="/uploads/short-url/kxbgT6ozJmOe24fYTNZ3Xnv5D5r.png?dl=1" title="Bad%20Allocation%20Exception" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8febb44cbdf7c4d41912b0c03d0f8f92da332115_2_690x383.png" alt="Bad%20Allocation%20Exception" data-base62-sha1="kxbgT6ozJmOe24fYTNZ3Xnv5D5r" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8febb44cbdf7c4d41912b0c03d0f8f92da332115_2_690x383.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8febb44cbdf7c4d41912b0c03d0f8f92da332115_2_1035x574.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8febb44cbdf7c4d41912b0c03d0f8f92da332115.png 2x" data-dominant-color="C0C1D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bad%20Allocation%20Exception</span><span class="informations">1337×743 96.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #27 by @cpinter (2018-11-13 19:12 UTC)

<p>It seems that you’re running out of physical memory. You can increase the virtual memory, or you can adjust the resolution of the labelmap so that it fits. The formed is described many times in this forum and you can find it with a search. However, it may not be feasible due to the very long processing time in the case of such a large model (the high resolution model is specified to be physically larger so the default 1mm isotropic spacing is probably cannot be used).</p>
<p>The latter can be done in the Segmentations module.</p>
<ol>
<li>Create new segmentation node</li>
<li>Make Closed surface the master representation in the Representations section</li>
<li>Import skull model in Export/import section</li>
<li>In the Representations section long-click the Create button, then in the pop-up menu select Advanced create…</li>
<li>Click on the only offered conversion path, then in the bottom section click Specify geometry</li>
<li>In the pop-up window choose the skull model as source geometry, and secify a spacing that is large enough so that the labelmap fits into memory</li>
</ol>

---

## Post #28 by @lassoan (2018-11-13 21:11 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="27" data-topic="4715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>It seems that you’re running out of physical memory.</p>
</blockquote>
</aside>
<p>This happens because the model’s scale is off by a factor of 10x. Probably because the designer person used 0.1mm as unit, while Slicer (and most of the medical imaging world) uses 1mm as unit. If you apply a transform of 0.1x scaling to the model in Transforms module then memory usage should be OK. Use this transformation matrix:</p>
<pre><code class="lang-auto">0.1  0   0    0
0    0.1 0    0
0    0   0.1  0
0    0   0    1.0
</code></pre>

---

## Post #29 by @Raymond (2018-11-14 20:02 UTC)

<p>Please see table below, as a reference.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48def37e99de75445ba4e38590bbe9ac80a79619.png" alt="Parameters%20of%20Cranium%20OBJ%20Models" data-base62-sha1="aoE30t8oM67eJN90cQ2xxhv16Ln" width="682" height="244"></p>
<p>The OBJ files are here:</p>
<p><a href="http://www.jfknumbers.org/ich-bin-ein-berliner/osseus-models/craniums/high-resolution/OBJ/" rel="noopener nofollow ugc">High Quality 3D Cranium Models in OBJ Format</a></p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #30 by @cpinter (2018-11-14 20:47 UTC)

<p>Still, when you load them into Slicer, this is not what we see. In this screenshot the small red object is the low res skull and the gray one is the medium res skull. If you just open the two obj files in a text editor you see why, the magnitude of the point cooridnate values is quite different. For some reason also orientation is different, and I’m not sure why is this difference when they are supposed to describe the same object.</p>
<p>This is why I suggested scaling up the labelmap resolution, and <a class="mention" href="/u/lassoan">@lassoan</a> suggested scaling down the skull.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c746704f818d6f8a80b14956d650ca37530418b.jpeg" data-download-href="/uploads/short-url/k2weGD66jKq6QwoDmkBiW1iEIYj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c746704f818d6f8a80b14956d650ca37530418b_2_449x499.jpeg" alt="image" data-base62-sha1="k2weGD66jKq6QwoDmkBiW1iEIYj" width="449" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c746704f818d6f8a80b14956d650ca37530418b_2_449x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c746704f818d6f8a80b14956d650ca37530418b_2_673x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c746704f818d6f8a80b14956d650ca37530418b.jpeg 2x" data-dominant-color="717284"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">714×794 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #31 by @Raymond (2018-11-14 21:42 UTC)

<p>Hi Csaba:</p>
<p>I just sent an e-mail to Joerg Behr, one of the Behr Brothers:</p>
<p><a href="https://behr-bros-shop.com/anatomy.html" rel="nofollow noopener">Behr Brothers - Anatomy Section</a></p>
<p>In it I reported all these issues, since this should be solved at the source.</p>
<p>-Ramon<br>
<strong>JFK Numbers</strong></p>

---

## Post #32 by @lassoan (2018-11-14 23:12 UTC)

<p>Behr Brother models look nice aesthetically from the outside, but they miss most of the internals of the skull. If you cut it then you can see that the internal bone surface is completely missing (as if the whole cranium would be solid bone):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18f984996d813dd4c8fa9882edada8a804304cee.png" data-download-href="/uploads/short-url/3yW32CcH96Mtx4CW2AL8tCHxVbU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18f984996d813dd4c8fa9882edada8a804304cee_2_477x500.png" alt="image" data-base62-sha1="3yW32CcH96Mtx4CW2AL8tCHxVbU" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18f984996d813dd4c8fa9882edada8a804304cee_2_477x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18f984996d813dd4c8fa9882edada8a804304cee_2_715x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18f984996d813dd4c8fa9882edada8a804304cee.png 2x" data-dominant-color="7A7A94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">764×800 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can make this model somewhat usable by scaling it by 0.1x to anatomical size and applying shell operation (to create internal bone surface in the cranium).</p>
<p>To save you some time, I’ve done this and saved resulting files <a href="https://1drv.ms/f/s!Arm_AFxB9yqHtfVr6OhiKX1vLWRb2A">here</a>.</p>
<p>I’ve also tried playing with this in virtual reality:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="VzVjvnKuBAE" data-video-title="3D Slicer reconstruction of fragmented bones in virtual reality" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=VzVjvnKuBAE" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/VzVjvnKuBAE/maxresdefault.jpg" title="3D Slicer reconstruction of fragmented bones in virtual reality" width="" height="">
  </a>
</div>


---
