---
topic_id: 13610
title: "Customize The Main Window"
date: 2020-09-22
url: https://discourse.slicer.org/t/13610
---

# Customize the Main Window

**Topic ID**: 13610
**Date**: 2020-09-22
**URL**: https://discourse.slicer.org/t/customize-the-main-window/13610

---

## Post #1 by @Hugo (2020-09-22 13:28 UTC)

<p>Is there a way to delete the effects case since I only need 4 of the buttons that I already made myself:<br>
I’ve already been able to delete the 3d slicer logo using: slicer.util.findChild(slicer.util.mainWindow(), ‘LogoLabel’).visible = False</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f71f63df91e03ebf358090846ed4b6f860c3aaa7.png" alt="image" data-base62-sha1="zg9bFBXxbkQmCXol92VLBJHAK59" width="466" height="160"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2effe9405831d8fbdaa237e5ab0d0da4800ac43.png" data-download-href="/uploads/short-url/nfpxea1IIi3JwulentGcG4sRNTl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2effe9405831d8fbdaa237e5ab0d0da4800ac43_2_690x28.png" alt="image" data-base62-sha1="nfpxea1IIi3JwulentGcG4sRNTl" width="690" height="28" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2effe9405831d8fbdaa237e5ab0d0da4800ac43_2_690x28.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2effe9405831d8fbdaa237e5ab0d0da4800ac43_2_1035x42.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2effe9405831d8fbdaa237e5ab0d0da4800ac43.png 2x" data-dominant-color="E9D5CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1370×56 4.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2020-09-22 13:33 UTC)

<p>Yes, you can do it like this:</p>
<pre><code class="lang-auto">segmentEditorWidget.unorderedEffectsVisible = False
segmentEditorWidget.setEffectNameOrder(['Paint', 'Draw', 'Erase', 'Smoothing'])
</code></pre>

---

## Post #3 by @Hugo (2020-09-22 13:43 UTC)

<p>Thanks a lot for responding that quick!<br>
In the future I might want the main window to not have the help&amp;Acknowledgment, Data Probe and Masking visible as well in order to make a very clear user’s interface. Is it possible?</p>

---

## Post #4 by @cpinter (2020-09-22 13:48 UTC)

<p>We call these kinds of customized Slicer applications Slicelets:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" target="_blank" rel="noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" target="_blank" rel="noopener">Documentation/Nightly/Developers/Slicelets - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Hugo (2020-09-22 13:56 UTC)

<p>I have been reading about these and it seems that can be a good alternative for my needs but I did not really understand how to make one, where to start, what’s needed. That is why I chose Jupyter Notebook book at first and also the fact that it can be accessible from any computer.</p>

---

## Post #6 by @cpinter (2020-09-22 14:06 UTC)

<p>The Slicelet page contains an example that you can change according to your needs:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/lassoan/SlicerSimpleWorkflows/tree/master/QuickSegment" target="_blank" rel="noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/307929?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/lassoan/SlicerSimpleWorkflows/tree/master/QuickSegment" target="_blank" rel="noopener">lassoan/SlicerSimpleWorkflows</a></h3>

<p>Examples of simple application-specific workflows implemented using 3D Slicer - lassoan/SlicerSimpleWorkflows</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>You can also create a Slicer custom application if you want something more complex:<br>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/2717525?s=400&amp;v=4" class="thumbnail onebox-avatar" width="59" height="59">

<h3><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="noopener">KitwareMedical/SlicerCustomAppTemplate</a></h3>

<p>Template to be used as a starting point for creating a custom 3D Slicer application - KitwareMedical/SlicerCustomAppTemplate</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #7 by @Hugo (2020-09-22 14:13 UTC)

<p>Thank you !<br>
I’m going to try launching the quick segment example to see how it looks</p>

---

## Post #8 by @Hugo (2020-09-23 12:22 UTC)

<p>Hello everyone,</p>
<p>I’ve managed to remove “Data Probe” from the main window using:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1ba0c22764d89d5a574e15593fbd9c74b050c061.png" data-download-href="/uploads/short-url/3WpjwUQDhqPCRNbcuFWkoVzAJYR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba0c22764d89d5a574e15593fbd9c74b050c061_2_517x18.png" alt="image" data-base62-sha1="3WpjwUQDhqPCRNbcuFWkoVzAJYR" width="517" height="18" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba0c22764d89d5a574e15593fbd9c74b050c061_2_517x18.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba0c22764d89d5a574e15593fbd9c74b050c061_2_775x27.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba0c22764d89d5a574e15593fbd9c74b050c061_2_1034x36.png 2x" data-dominant-color="E6E2E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1186×44 9.38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I have issue trying to remove help&amp;Acknowledgment:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/392abe47e461f6ecb37d30917102df552cb207f7.png" alt="image" data-base62-sha1="89IN9Pz7TXhXvmO7tPsrNyC2Ear" width="481" height="27"></p>
<p>And delete some of the module choices (example: to only keep segmentation, segment editor, models and  data visible in this column:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1f4ac7882eb5fc4f4f9c4aa4a5860b29a7420b1.png" alt="image" data-base62-sha1="ywrhrFIx4SaU2f0UJEIdm5nbggp" width="196" height="229"></p>
<p>Big thanks in advance your help has been very precious to me,</p>
<p>Hugo</p>

---

## Post #9 by @lassoan (2020-09-23 15:38 UTC)

<p>You can hide parts of the GUI using helper functions in slicer.util:</p>
<pre><code class="lang-python"># Hide data probe
slicer.util.setDataProbeVisible(False)
# hide Help &amp; Acknowledgement section
slicer.util.setModuleHelpSectionVisible(False)
</code></pre>
<p>To restrict what modules the user can select, you can hide the “Module selection” toolbar and set the modules you want to offer as “Favorite modules” in application settings (<code>Modules/FavoriteModules</code>).</p>

---
