---
topic_id: 45359
title: "Scene Views Modernization"
date: 2025-12-03
url: https://discourse.slicer.org/t/45359
---

# Scene Views Modernization

**Topic ID**: 45359
**Date**: 2025-12-03
**URL**: https://discourse.slicer.org/t/scene-views-modernization/45359

---

## Post #1 by @Sunderlandkyl (2025-12-03 20:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62ad1c9c0b8d608ca19fb5c616f5250ef81ba551.jpeg" data-download-href="/uploads/short-url/e4VGiSxIDYNZiFYZTVqBmdCDXwt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ad1c9c0b8d608ca19fb5c616f5250ef81ba551_2_690x370.jpeg" alt="image" data-base62-sha1="e4VGiSxIDYNZiFYZTVqBmdCDXwt" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ad1c9c0b8d608ca19fb5c616f5250ef81ba551_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ad1c9c0b8d608ca19fb5c616f5250ef81ba551_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ad1c9c0b8d608ca19fb5c616f5250ef81ba551_2_1380x740.jpeg 2x" data-dominant-color="747378"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 368 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-130365-what-are-scene-views-1" class="anchor" href="#p-130365-what-are-scene-views-1" aria-label="Heading link"></a>What are Scene Views?</h2>
<p>Scene Views store snapshots of visualization settings of the scene content. By default, the scene view stores the current view layout, camera viewpoint in 3D views, slice position in 2D views, and display settings of all nodes (visibility, color, transparency, etc.), along with a short description. They serve as visual bookmarks, which can be used to quickly review and share interesting details of the scene.</p>
<h2><a name="p-130365-whats-new-2" class="anchor" href="#p-130365-whats-new-2" aria-label="Heading link"></a>What’s New?</h2>
<p>In the latest stable and nightly releases, scene views have been reworked to internally use hidden “sequence” nodes (managed by Sequences module). This allows much faster and more robust storage compared to previous generations of this feature.</p>
<p>When the scene is saved, scene view data is automatically saved into a <code>Private</code> subfolder adjacent to the <code>.mrml</code> scene file, containing sequences for all the scene views. When loading an existing scene, scene views are automatically converted into the new format.</p>
<h2><a name="p-130365-for-users-3" class="anchor" href="#p-130365-for-users-3" aria-label="Heading link"></a>For Users</h2>
<p>Scene views can be created by enabling the “Capture/Restore” toolbar and selecting the middle “Capture and name a scene view” option.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbc2e4b1d322be6ab4fd94d1d07afe2561c22b23.png" alt="image" data-base62-sha1="qN0QkqXEIz98XQW6SIvQY9i2xUv" width="180" height="85"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b2f43f84b6974cec6f53f4e7222b0d2b1fd91dc.png" data-download-href="/uploads/short-url/m8PgYuJHKP9ES6t2dNvylwSjQx6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b2f43f84b6974cec6f53f4e7222b0d2b1fd91dc_2_522x500.png" alt="image" data-base62-sha1="m8PgYuJHKP9ES6t2dNvylwSjQx6" width="522" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b2f43f84b6974cec6f53f4e7222b0d2b1fd91dc_2_522x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b2f43f84b6974cec6f53f4e7222b0d2b1fd91dc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b2f43f84b6974cec6f53f4e7222b0d2b1fd91dc.png 2x" data-dominant-color="EAEAEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">646×618 43.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Scene views can be restored, deleted or edited within the scene views module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80d20638d9f8726645bde5809c1f45bd3b2d0521.png" data-download-href="/uploads/short-url/inB5EDf1fFqfbS6ngrRsnfVUo8x.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80d20638d9f8726645bde5809c1f45bd3b2d0521.png" alt="image" data-base62-sha1="inB5EDf1fFqfbS6ngrRsnfVUo8x" width="657" height="162"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">657×162 19.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-130365-for-developers-4" class="anchor" href="#p-130365-for-developers-4" aria-label="Heading link"></a>For Developers</h2>
<p>Scene views are controlled by one or more hidden sequence browser node, controlling sequences for each display node in the scene.</p>
<p>By default, only display/view/etc. nodes are stored in scene views, however it is possible to add any node type to a scene view. (See <a href="https://apidocs.slicer.org/main/classvtkSlicerSceneViewsModuleLogic.html#a3f2ab4e50f11cc9c94bb5d9d39d4100f" rel="noopener nofollow ugc">vtkSlicerSceneViewsModuleLogic::CreateSceneView()</a>).</p>
<h3><a name="p-130365-simplified-python-api-5" class="anchor" href="#p-130365-simplified-python-api-5" aria-label="Heading link"></a>Simplified Python API</h3>
<pre data-code-wrap="python"><code class="lang-python"># Create a scene view with optional screenshot
slicer.modules.sceneviews.logic().CreateSceneView(
    name="My Snapshot",
    description="Before surgery planning",
    screenshotType=0,
    screenshot=None)
# Restore by index or name
slicer.modules.sceneviews.logic().RestoreSceneView(0)
slicer.modules.sceneviews.logic().RestoreSceneView("My Snapshot")
</code></pre>
<h2><a name="p-130365-acknowledgements-6" class="anchor" href="#p-130365-acknowledgements-6" aria-label="Heading link"></a>Acknowledgements</h2>
<p>Development was funded in part by a Children’s Hospital of Philadelphia (CHOP) Cardiac Center Innovation Grant, a CHOP Cardiac Center Research Grant, a CHOP Frontier Grant, NIH R01 HL153166 and T32GM008562.</p>

---
