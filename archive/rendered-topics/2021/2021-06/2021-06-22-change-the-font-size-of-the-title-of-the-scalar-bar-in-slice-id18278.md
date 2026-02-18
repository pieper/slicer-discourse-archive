# Change the font size of the title of the scalar bar in SlicerRT Isodose module

**Topic ID**: 18278
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/change-the-font-size-of-the-title-of-the-scalar-bar-in-slicerrt-isodose-module/18278

---

## Post #1 by @Mik (2021-06-22 18:27 UTC)

<p>Isodose module in SlicerRT uses vtkScalarBar to show isodose palette and values.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e1dc4d4d8518ecb8ef353923d42c0a20863302.png" data-download-href="/uploads/short-url/8g37qAVIO00k6seuq74I8PA7k0a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39e1dc4d4d8518ecb8ef353923d42c0a20863302_2_690x439.png" alt="image" data-base62-sha1="8g37qAVIO00k6seuq74I8PA7k0a" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39e1dc4d4d8518ecb8ef353923d42c0a20863302_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e1dc4d4d8518ecb8ef353923d42c0a20863302.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e1dc4d4d8518ecb8ef353923d42c0a20863302.png 2x" data-dominant-color="1C1211"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">693×441 21.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have tried to change the title’s font size of the scalar bar actor, but it didn’t change anything.</p>
<p>For example</p>
<pre><code class="lang-auto">  // Update all scalar bar actors
  for (vtkScalarBarWidget* scalarBarWidget : d-&gt;ScalarBarWidgets)
  {
    vtkSlicerRTScalarBarActor* actor = vtkSlicerRTScalarBarActor::SafeDownCast( scalarBarWidget-&gt;GetScalarBarActor() );

    // Update actor
    actor-&gt;SetTitle(scalarBarTitle.c_str());

    if (vtkTextProperty* textProp = actor-&gt;GetTitleTextProperty())
    {
      textProp-&gt;SetFontSize(8);
    }
    scalarBarWidget-&gt;Render();
  }
</code></pre>
<p>How to do this correctly?</p>
<p><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/qSlicerIsodoseModuleWidget.cxx#L999-L1016" rel="noopener nofollow ugc">Update scalar bar actor original code</a></p>

---

## Post #2 by @lassoan (2021-06-22 23:00 UTC)

<p>The text is auto-scaled to the widget size. You can make the text larger by making the widget larger.</p>

---

## Post #3 by @Mik (2021-06-23 04:52 UTC)

<p>How can i make it more customized? Make it smaller, both title, labels and scalar bar itself, without modifying <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Widgets/vtkSlicerRTScalarBarActor.cxx" rel="noopener nofollow ugc">scalar bar actor</a> class.</p>

---

## Post #4 by @lassoan (2021-06-25 20:23 UTC)

<p>You can access some properties of the scalar bar, but maybe not all that you need. Unfortunately, the scalar bars are implemented very poorly. It would be awesome if you could help with implementing it properly. Most importantly, it would need to use a displayable manager class, which would display a scalar bar for each display node. Appearance of the scalar bar could be modified by changing the display node properties.</p>

---

## Post #5 by @Mik (2021-06-28 09:22 UTC)

<p>I can try to help.</p>
<p>I have checked the source code and have found <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLScalarBarDisplayableManager.h" rel="noopener nofollow ugc">ScalarBarDisplayableManager</a> class. Can it be used as a basis for the future implementation? I have also found that some modules (Colors, Isodose, DataProbe) use nearly identical versions of ScalarBarActor class. Is that the absent of universal solution of that problem?</p>

---

## Post #6 by @lassoan (2021-06-28 14:10 UTC)

<aside class="quote no-group" data-username="Mik" data-post="5" data-topic="18278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>I can try to help.</p>
</blockquote>
</aside>
<p>Awesome!</p>
<aside class="quote no-group" data-username="Mik" data-post="5" data-topic="18278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>I have checked the source code and have found <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLScalarBarDisplayableManager.h">ScalarBarDisplayableManager</a> class. Can it be used as a basis for the future implementation?</p>
</blockquote>
</aside>
<p>We should improve the scalar bar implementation in the Slicer core and then slightly modified versions in extensions will be no longer needed. You can modify the scalar bar any way you see fit. It is also very important to support multiple scalar bars and manage them (add them to the renderer) in a displayable manager.</p>

---
