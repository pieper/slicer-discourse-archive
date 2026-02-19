---
topic_id: 1378
title: "How To Display 2 Volumes With Transparences"
date: 2017-11-04
url: https://discourse.slicer.org/t/1378
---

# How to display 2 volumes with transparences

**Topic ID**: 1378
**Date**: 2017-11-04
**URL**: https://discourse.slicer.org/t/how-to-display-2-volumes-with-transparences/1378

---

## Post #1 by @Anto (2017-11-04 10:30 UTC)

<p>As a title I’m curious to know how to display 2 or more volume in the same scene, with transparence effect, to show internal anatomic structures</p>
<p>thanks</p>

---

## Post #2 by @Frederic (2017-11-04 10:53 UTC)

<p>Hi,<br>
In python interface:<br>
Perhaps by:<br>
slicer.modules.models.logic().AddModel(myPolyData)<br>
or<br>
slicer.modules.models.logic().AddVolume(myPolyData)</p>

---

## Post #3 by @Anto (2017-11-04 11:50 UTC)

<p>Hello. Thank you for reply but I’m a beginner user and I’m able to use only a graphic interface… <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #4 by @AndFor (2017-11-04 11:55 UTC)

<p>do you mean a result like this?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a681a73a990c0483911dc670d7f66e4e2d562a6d.jpeg" alt="23" data-base62-sha1="nKZ2x7NvBsRZt54YsTLJsIKRrAh" width="426" height="471"></p>
<p>I’ve done with philips workstation, but i’m interest too to have a similar result with Slicer… I will try</p>

---

## Post #5 by @lassoan (2017-11-04 14:32 UTC)

<p>In general, anatomical images are complex enough that display them by simple blending has limited use. You can try it easily in slice views, select one volume as foreground, another one as background, and adjust the foreground visibility slider.</p>
<p>What works quite well (but of course somewhat more work) is to segment relevant structures from at least one of the volumes, and display those segments overlaid on the other volume. The non-segmented volume can be visualized using Volume rendering module. Segments can be made transparent in 3D views by adjusting display settings in Segmentations module.</p>

---

## Post #6 by @Anto (2017-11-04 15:36 UTC)

<p>I’ve 3 volume in volume rendering:</p>
<ul>
<li>the mail volume (dataset base)</li>
<li>volume 1 segmented from main volume using mask</li>
<li>volume 2 , similare to volume 1 but not sliglty different</li>
</ul>
<p>In volume rendering I can display correctly each of them but not all together ???!!</p>

---

## Post #7 by @lassoan (2017-11-04 16:19 UTC)

<p>Yes, you can show one volume using volume rendering at a time, all the others have to be segmented. By using Segment Editor module, you can often create high-quality Segmentations quite easily.</p>
<p>Multiple volume rendering may be added to VTK in the near future and then we’ll enable that in Slicer as well.</p>

---

## Post #8 by @AndFor (2017-11-04 18:57 UTC)

<p>but we can display multiple model as here?</p>
<p><a href="http://www.spl.harvard.edu/publications/bitstream/viewbiglogo/2037/BrainAtlas-Snapshot" class="onebox" target="_blank" rel="nofollow noopener">http://www.spl.harvard.edu/publications/bitstream/viewbiglogo/2037/BrainAtlas-Snapshot</a></p>
<p>I need to save segmentation as model?</p>

---

## Post #9 by @lassoan (2017-11-04 19:12 UTC)

<aside class="quote no-group" data-username="AndFor" data-post="8" data-topic="1378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andfor/48/822_2.png" class="avatar"> AndFor:</div>
<blockquote>
<p>display multiple model as here?</p>
</blockquote>
</aside>
<p>Yes, of course. You can adjust display parameters of all segments globally or individually for each segment - in Segmentations module Display section. If you prefer, you can also export all segments to model nodes using Export/Import section.</p>

---

## Post #10 by @AndFor (2017-11-04 20:55 UTC)

<p>Good, I’ve downloaded the pre-made model <a href="http://www.spl.harvard.edu/publications/item/view/2037" rel="nofollow noopener">http://www.spl.harvard.edu/publications/item/view/2037</a></p>
<p>I’ve see that we can use a different opacity for simultaneus 3D models</p>

---

## Post #11 by @lassoan (2017-11-04 22:06 UTC)

<p>Note that you can also access these anatomical atlases conveniently in Data Store module (Slicer automatically downloads and caches the selected atlas and other sample data sets).</p>

---

## Post #12 by @AndFor (2017-11-04 22:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9389e12790a4675922462cebfb66278c1d9810d0.png" data-download-href="/uploads/short-url/l3bANXUYmF5KOefIGRon5NyTmuI.png?dl=1" title="image_00022" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9389e12790a4675922462cebfb66278c1d9810d0_2_620x500.png" alt="image_00022" data-base62-sha1="l3bANXUYmF5KOefIGRon5NyTmuI" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9389e12790a4675922462cebfb66278c1d9810d0_2_620x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9389e12790a4675922462cebfb66278c1d9810d0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9389e12790a4675922462cebfb66278c1d9810d0.png 2x" data-dominant-color="0F0E08"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_00022</span><span class="informations">740×596 64.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>here my first segmentation <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
no possible to export in png with TRASPARENT background?</p>

---

## Post #13 by @lassoan (2017-11-04 23:49 UTC)

<p>Nice work!</p>
<p>We haven’t added GUI for exporting a screenshot in a PNG file with transparent background, but you can easily do it:</p>
<ol>
<li>Press Ctrl+3 to open Python console</li>
<li>Copy-paste “Capture 3D view into PNG file with transparent background” script from <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture">Script repository</a>
</li>
</ol>
<p>If you need animations with transparent background then you could add these few lines to the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ScreenCapture">ScreenCapture module</a> (and a checkbox that enables/disables transparent background mode). To edit a module, enable Developer mode in Application Settings and click on <code>Edit</code> button at the top of the module GUI. If you managed to implement this then send us a pull request and we’ll be happy to integrate it.</p>

---

## Post #14 by @fbordignon (2021-12-06 13:15 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a>, would it be possible to do this on the simpler Annotation Snap(Screen) Shot. I figure some logic like that would be necessary before and after the screenshot is called:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Annotations/GUI/qSlicerAnnotationModuleSnapShotDialog.cxx#L134">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Annotations/GUI/qSlicerAnnotationModuleSnapShotDialog.cxx#L134" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Annotations/GUI/qSlicerAnnotationModuleSnapShotDialog.cxx#L134" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Annotations/GUI/qSlicerAnnotationModuleSnapShotDialog.cxx#L134</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="124" style="counter-reset: li-counter 123 ;">
          <li>// description</li>
          <li>QString description = this-&gt;description();</li>
          <li>QByteArray descriptionBytes = description.toUtf8();</li>
          <li>
          </li>
<li>// we need to know of which type the screenshot is</li>
          <li>int screenshotType = static_cast&lt;int&gt;(this-&gt;widgetType());</li>
          <li>
          </li>
<li>if (this-&gt;data().toString().isEmpty())</li>
          <li>  {</li>
          <li>  // this is a new snapshot</li>
          <li class="selected">  this-&gt;m_Logic-&gt;CreateSnapShot(nameBytes.data(),</li>
          <li>                                descriptionBytes.data(),</li>
          <li>                                screenshotType,</li>
          <li>                                this-&gt;scaleFactor(),</li>
          <li>                                this-&gt;imageData());</li>
          <li>  }</li>
          <li>else</li>
          <li>  {</li>
          <li>  // this snapshot already exists</li>
          <li>  this-&gt;m_Logic-&gt;ModifySnapShot(vtkStdString(this-&gt;data().toString().toUtf8()),</li>
          <li>                                nameBytes.data(),</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Following the logic currently on the python module. Would that be desirable? Sometimes the user wants to grab a quick screenshot and the annotation screenshot is the quicker a cleaner option.<br>
Thanks</p>

---

## Post #15 by @jamesobutler (2021-12-06 13:38 UTC)

<p>Since the Annotations module is currently legacy and will be removed in the future, it would be better to modify the Screen Capture module to do what you want as modifying the annotations module is something not going to be supported.</p>

---

## Post #16 by @fbordignon (2021-12-06 13:56 UTC)

<p>Thanks. I will work on simplifying the Screen Capture.</p>

---

## Post #17 by @lassoan (2021-12-06 15:42 UTC)

<p>Currently, the fastest way of copying 3D view content is the context menu (right-click menu) in the view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f5616d754c81fe03f28560eef50b1ac31b8db85.png" data-download-href="/uploads/short-url/fSVryLUUTDSLoDcMwiODxVx81JH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f5616d754c81fe03f28560eef50b1ac31b8db85.png" alt="image" data-base62-sha1="fSVryLUUTDSLoDcMwiODxVx81JH" width="605" height="500" data-dominant-color="9E9B95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">696×575 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In addition to adding a “transparent background” option to the Screen Capture module, we could also add a “Copy image with transparent background” action to the view context menu.</p>

---

## Post #18 by @lassoan (2022-01-28 23:44 UTC)

<p>A post was split to a new topic: <a href="/t/segmentation-exported-to-model-file-and-imported-does-not-preserve-transparency/21684">Segmentation exported to model file and imported does not preserve transparency</a></p>

---
