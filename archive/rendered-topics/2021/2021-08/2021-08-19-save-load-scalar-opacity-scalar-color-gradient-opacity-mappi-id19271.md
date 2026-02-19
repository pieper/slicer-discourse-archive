---
topic_id: 19271
title: "Save Load Scalar Opacity Scalar Color Gradient Opacity Mappi"
date: 2021-08-19
url: https://discourse.slicer.org/t/19271
---

# Save & load (scalar opacity | Scalar color | gradient opacity) mapping settings from volume rendering?

**Topic ID**: 19271
**Date**: 2021-08-19
**URL**: https://discourse.slicer.org/t/save-load-scalar-opacity-scalar-color-gradient-opacity-mapping-settings-from-volume-rendering/19271

---

## Post #1 by @hherhold (2021-08-19 12:55 UTC)

<p>Hey all,</p>
<p>Is there a way (python or otherwise) to save and load the “transfer curves”, meaning the scalar opacity mapping, scalar color mapping, and gradient opacity mapping settings to a file for reloading later? I do not use any of the presets, and it would be nice to be able to save mappings for later.</p>
<p>Totally fine if this is only doable from python with telling a node (or nodes) to write/read to/from disk.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @pieper (2021-08-19 14:35 UTC)

<p>These links should help:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Spr_2021/blob/cbd6e1d269fdb256d2ab0f42933a1422c8c8fff6/Day_2/VolumeRendering/VolumeRendering.md#saving-your-transfer-functions">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Spr_2021/blob/cbd6e1d269fdb256d2ab0f42933a1422c8c8fff6/Day_2/VolumeRendering/VolumeRendering.md#saving-your-transfer-functions" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Spr_2021/blob/cbd6e1d269fdb256d2ab0f42933a1422c8c8fff6/Day_2/VolumeRendering/VolumeRendering.md#saving-your-transfer-functions" target="_blank" rel="noopener">SlicerMorph/Spr_2021/blob/cbd6e1d269fdb256d2ab0f42933a1422c8c8fff6/Day_2/VolumeRendering/VolumeRendering.md#saving-your-transfer-functions</a></h4>


      <pre><code class="lang-md">## Visualization: Volume Rendering
The `Volume Rendering` module provides interactive visualization of 3D image data. For [**official documentation of the panel and functions, see here**](https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html).

* Only scalar volumes can be used for volume rendering. Vector volumes (eg jpg, png, bmp, or other classic 2D formats) can be converted to scalar volumes using the [VectorToScalarVolume module](https://www.slicer.org/wiki/Documentation/Nightly/Modules/VectorToScalarVolume). If you used SlicerMorph's `ImageStacks` module to import your data, vector to scalar conversion was done already at the time of import the data.

One quick way to render your volume is using the drag and drop function. In the `Data` module you can drag the mouse skull volume from the image stacks example directly into the 3D widow and Slicer will guess at the settings to render the volume. 

&lt;img src="./DragDropVR.png"&gt;

While this may be a good starting point, there are a lot of settings you can modify to improve the rendering of your volume in the `Volume Rendering` module. 

* 3D Slicer uses volume ray casting to computes 2D images from 3D volumetric data sets. Unlike surface reconstruction, there is no estimation of object surfaces or segmentation.
* The values displayed are calculated using a transfer function that incorporates voxel intensities, material properties, and illumination.
* The opacity and color of the image can be adjusted by modifying their transfer functions in the `Volume Rendering` module.

 &lt;img src="./volumeRenderTF.png"&gt;
 
* Slicer supports both CPU and GPU volume rendering. CPU based will always work, whether you are on a computer without a dedicated graphics card, or on a remote connection (which may not support hardware accelerated graphics), but it can be slow (unless you have dozens of cores in your cpu). GPU requires you have a dedicated graphics card with 1GB or more videoRAM and it is much faster, but it has its own limitations (see below).  
* If you have a dedicated graphics card, you may want to set the default visualization method to GPU rendering using the menu option in: Edit-&gt;Preferences 
* Always set the rendering quality to normal (this is enabled by defalt, if you opt-in for the SlicerMorph Preferences).
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Spr_2021/blob/cbd6e1d269fdb256d2ab0f42933a1422c8c8fff6/Day_2/VolumeRendering/VolumeRendering.md#saving-your-transfer-functions" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote quote-modified" data-post="8" data-topic="16383">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fishguy/48/7337_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/i-want-to-boot-up-with-my-very-own-color-map-and-a-black-background/16383/8">I want to boot up with my very own color map and a black background</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Ok…I have hit a roadblock. I am following the guidance here: 
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/volumerendering.html#how-to-register-custom-volume-rendering-presets" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/modules/volumerendering.html#how-to-register-custom-volume-rendering-presets</a> 
I have a new file called MyPresets.mrml in my Slicer Scene Location directory along with a PNG thumbnail. 
Now I come to this instruction… 
" Use the following code to read all the custom presets from MyPresets.mrml and load it into the scene:" 
I do not know how to ‘use’ the code. I pasted it in the Py…
  </blockquote>
</aside>


---

## Post #3 by @hherhold (2021-08-19 14:42 UTC)

<p>Most excellent! Thanks much.</p>
<p>-Hollister</p>

---

## Post #4 by @muratmaga (2021-08-19 18:57 UTC)

<p>Here is an example from SlicerMorph. A mrml file that defines the presets, and a short resource script that loads it into the scene (you only care the top couple lines, the rest are other SlicerMorph preferences).</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/MorphPreferences/Resources">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/MorphPreferences/Resources" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/MorphPreferences/Resources" target="_blank" rel="noopener nofollow ugc">SlicerMorph/MorphPreferences/Resources at master · SlicerMorph/SlicerMorph</a></h3>

  <p><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/MorphPreferences/Resources" target="_blank" rel="noopener nofollow ugc">master/MorphPreferences/Resources</a></p>

  <p><span class="label1">Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
