---
topic_id: 7340
title: "Texturize 3D Model Ray Tracing"
date: 2019-06-27
url: https://discourse.slicer.org/t/7340
---

# Texturize 3D model (ray tracing)

**Topic ID**: 7340
**Date**: 2019-06-27
**URL**: https://discourse.slicer.org/t/texturize-3d-model-ray-tracing/7340

---

## Post #1 by @Michael_Ef (2019-06-27 12:44 UTC)

<p>Hi there,</p>
<p>I have created a 3D model from a stack of histological images. Now i would like to texturize/colorize this model by using the original rgb-images. Is there a way to project this “color” information on the model for example by ray casting (like it is done in volume rendering module)? Or any other way how I can achieve this? It should also work if i cut through the model.</p>
<p>I would appreciate any ideas or solutions. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thanks in advance<br>
Michael</p>

---

## Post #2 by @lassoan (2019-06-30 17:25 UTC)

<p>You can visualize a 3D color volume using ray casting as described in this post:</p>
<aside class="quote quote-modified" data-post="6" data-topic="6472">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/merge-colored-images-and-show-them-as-1-volume/6472/6">Merge colored images and show them as 1 volume</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If you have a full-color image then you can show a direct volume rendering of it by turning off “independent component” option in the volume renderer (it makes image components interpreted as RGBA). Type this in the Python console after enabling volume rendering: 
getNode('VolumeProperty').GetVolumeProperty().SetIndependentComponents(0)

Note that you need an RGBA image (not just RGB). The fourth (alpha) component controls opacity. If you only have an RGB image then you can create the “alpha” v…
  </blockquote>
</aside>


---

## Post #3 by @Michael_Ef (2019-07-27 13:33 UTC)

<p>Thanks a lot Andras. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">  That worked so far, except for the fact<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acebe60f7364df4877c6cd2416028291c51c4b52.png" data-download-href="/uploads/short-url/oFJxcr9PZ5XOyqzs0AA36yAJXV0.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acebe60f7364df4877c6cd2416028291c51c4b52_2_690x322.png" alt="Screenshot" data-base62-sha1="oFJxcr9PZ5XOyqzs0AA36yAJXV0" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acebe60f7364df4877c6cd2416028291c51c4b52_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acebe60f7364df4877c6cd2416028291c51c4b52.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acebe60f7364df4877c6cd2416028291c51c4b52.png 2x" data-dominant-color="807DA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">754×352 28.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> but that didnt help.</p>
<p>Do you know how to solve this problem?</p>
<p>Thanks and best regards,<br>
Michael</p>

---

## Post #4 by @lassoan (2019-07-27 13:58 UTC)

<p>As described in the linked post, you need an RGBA volume - the alpha channel containing transparency of voxels. If you want to make the background transparent then set alpha values of the background to 0.</p>

---

## Post #5 by @Michael_Ef (2019-07-28 12:25 UTC)

<p>Sorry to bother you again, but where do I have to set the alpha values? In the scalar volume or can I set this in the volume properties? Hope this question isn’t too stupid, but I’m still new to Slicer. Thanks!</p>

---

## Post #6 by @lassoan (2019-07-29 03:58 UTC)

<p>There is no GUI for manipulating voxel values, but you can retrieve voxel values in the Python console as a numpy array (using <code>slicer.util.arrayFromVolume</code>), adjust the values of the alpha channel using standard numpy array manipulations, then update the volume with the changes (<code>slicer.util.arrayFromVolumeModified</code>). See example <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" rel="nofollow noopener">here</a>.</p>

---

## Post #7 by @Michael_Ef (2019-08-09 09:20 UTC)

<p>Hello Andras,<br>
that worked well, thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Is there a way to keep these settings when I save the whole scene as a medical record bundle? Currently, when I reload the scene from the bundle my modifications are not displayed anymore. Display node is observing the volume properties and the volume node.<br>
How can I ensure to reload the scene in exactly the same state as I saved it?</p>

---

## Post #8 by @lassoan (2019-08-10 18:32 UTC)

<p>Probably <code>IndependentComponents</code> property is not saved in the file. Probably you would just need to add a couple of lines to <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/MRML/vtkMRMLVolumePropertyNode.cxx" rel="nofollow noopener">vtkMRMLVolumePropertyNode</a> to read/write the property to XML.</p>

---
