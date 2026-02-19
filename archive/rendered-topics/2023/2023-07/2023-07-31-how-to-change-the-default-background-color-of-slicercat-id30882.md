---
topic_id: 30882
title: "How To Change The Default Background Color Of Slicercat"
date: 2023-07-31
url: https://discourse.slicer.org/t/30882
---

# How to change the default background color of slicerCAT

**Topic ID**: 30882
**Date**: 2023-07-31
**URL**: https://discourse.slicer.org/t/how-to-change-the-default-background-color-of-slicercat/30882

---

## Post #1 by @slicer365 (2023-07-31 05:09 UTC)

<p>I know the python script can help change the background color.</p>
<p>Now I wan to change the color in the source code.</p>
<p>Which file should I edit?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/574dfaa92336e777f1cfbcb596e284e672d6eab7.png" data-download-href="/uploads/short-url/cskBMOvYekTLjs3lbtI92mad0Oz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/574dfaa92336e777f1cfbcb596e284e672d6eab7_2_517x135.png" alt="image" data-base62-sha1="cskBMOvYekTLjs3lbtI92mad0Oz" width="517" height="135" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/574dfaa92336e777f1cfbcb596e284e672d6eab7_2_517x135.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/574dfaa92336e777f1cfbcb596e284e672d6eab7_2_775x202.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/574dfaa92336e777f1cfbcb596e284e672d6eab7_2_1034x270.png 2x" data-dominant-color="F4F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1650×435 39.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75e9a2724afbe1999e946b32e6d8d9ea0bca65e9.png" data-download-href="/uploads/short-url/gP6qgYxY2KQV4m1TdqR2mQXZlZ7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75e9a2724afbe1999e946b32e6d8d9ea0bca65e9_2_517x266.png" alt="image" data-base62-sha1="gP6qgYxY2KQV4m1TdqR2mQXZlZ7" width="517" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75e9a2724afbe1999e946b32e6d8d9ea0bca65e9_2_517x266.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75e9a2724afbe1999e946b32e6d8d9ea0bca65e9_2_775x399.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75e9a2724afbe1999e946b32e6d8d9ea0bca65e9_2_1034x532.png 2x" data-dominant-color="61636C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×987 64.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sam_Horvath (2023-07-31 14:52 UTC)

<p>Is there a reason why you can’t continue to use a python script to change the background color of the 3D view?</p>
<p>We generally include a python scripted module (called ‘Home’ or similar) that can be used to apply python scripted changes to the application appearance (see this blog: <a href="https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/">https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/</a>)</p>

---

## Post #3 by @slicer365 (2023-07-31 15:40 UTC)

<p>If I click the ‘close scene’,I still hope the color is the sytle I preset.</p>
<p>If I write the script in the home.py, it just works for the first start of App.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4623de89794920d395568a95aec5705917b3d37e.png" data-download-href="/uploads/short-url/a0ugTzgENG10SQOyeo8FAVzn1j8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4623de89794920d395568a95aec5705917b3d37e_2_517x273.png" alt="image" data-base62-sha1="a0ugTzgENG10SQOyeo8FAVzn1j8" width="517" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4623de89794920d395568a95aec5705917b3d37e_2_517x273.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4623de89794920d395568a95aec5705917b3d37e_2_775x409.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4623de89794920d395568a95aec5705917b3d37e_2_1034x546.png 2x" data-dominant-color="55585D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1788×948 43.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jamesobutler (2023-07-31 15:51 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> should appearance customization of the Slice Views (3D View Background color, Orientation Marker, Ruler, etc), only be reset with the “Reset to default” action of the appearance menu? Currently all of these are reset with a scene clear.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ebb35e1cdcb9ed0afc88539b89b51838da5c188.png" alt="image" data-base62-sha1="i57fZgoyBU4btrcrsXeQqLr4hFC" width="567" height="219"></p>

---

## Post #5 by @Sam_Horvath (2023-07-31 15:55 UTC)

<p>I see!  Some properties of the views are stored as nodes, and so are cleared when the scene is closed.</p>
<p>You can</p>
<ul>
<li>detect the scene close and re-apply the changes or</li>
<li>apply the changes both to the existing node and to the default node that will be used to create new ones on the scene close</li>
</ul>
<p>Here is what you would add  to your existing code for option 2 (option 1 is a little verbose, so lets see if this one works for you):</p>
<pre><code class="lang-auto">defaultViewNode = slicer.vtkMRMLViewNode()
defaultViewNode.SetBackgroundColor(1,0,0)
slicer.mrmlScene.AddDefaultNode(defaultViewNode)

</code></pre>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Since these settings are stored in nodes, they are dumped with the scene clear.  It will be tricky to rework this behavior</p>

---
