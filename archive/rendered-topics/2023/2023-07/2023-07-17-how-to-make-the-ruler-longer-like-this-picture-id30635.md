---
topic_id: 30635
title: "How To Make The Ruler Longer Like This Picture"
date: 2023-07-17
url: https://discourse.slicer.org/t/30635
---

# How to make the ruler longer like this picture

**Topic ID**: 30635
**Date**: 2023-07-17
**URL**: https://discourse.slicer.org/t/how-to-make-the-ruler-longer-like-this-picture/30635

---

## Post #1 by @slicer365 (2023-07-17 07:58 UTC)

<p>Any script will be helpful!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9722c75e84c84fc247cf13bf0da77eb00ff9c5ac.jpeg" data-download-href="/uploads/short-url/lz0BTCm1vCepqcY9UbzUBR3tbaI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9722c75e84c84fc247cf13bf0da77eb00ff9c5ac_2_500x375.jpeg" alt="image" data-base62-sha1="lz0BTCm1vCepqcY9UbzUBR3tbaI" width="500" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9722c75e84c84fc247cf13bf0da77eb00ff9c5ac_2_500x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9722c75e84c84fc247cf13bf0da77eb00ff9c5ac_2_750x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9722c75e84c84fc247cf13bf0da77eb00ff9c5ac_2_1000x750.jpeg 2x" data-dominant-color="555662"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1258×942 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-07-17 14:45 UTC)

<p>I don’t think that is exposed in python.  You can have a look at the C++ code to get an idea how the ruler is calculated and what parameters are available.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3acf6800e3578015ffd4d23404fcd1ff9bd1337d/Libs/MRML/DisplayableManager/vtkMRMLRulerDisplayableManager.cxx#L242">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3acf6800e3578015ffd4d23404fcd1ff9bd1337d/Libs/MRML/DisplayableManager/vtkMRMLRulerDisplayableManager.cxx#L242" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3acf6800e3578015ffd4d23404fcd1ff9bd1337d/Libs/MRML/DisplayableManager/vtkMRMLRulerDisplayableManager.cxx#L242" target="_blank" rel="noopener">Slicer/Slicer/blob/3acf6800e3578015ffd4d23404fcd1ff9bd1337d/Libs/MRML/DisplayableManager/vtkMRMLRulerDisplayableManager.cxx#L242</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="232" style="counter-reset: li-counter 231 ;">
          <li>  vtkTextProperty* textProperty = this-&gt;RulerTextActor-&gt;GetTextProperty();</li>
          <li>  textProperty-&gt;SetFontSize(RULER_BASE_FONT_SIZE);</li>
          <li>  textProperty-&gt;SetFontFamilyToArial();</li>
          <li>  if (this-&gt;External-&gt;GetMRMLApplicationLogic())</li>
          <li>    {</li>
          <li>    this-&gt;External-&gt;GetMRMLApplicationLogic()-&gt;UseCustomFontFile(textProperty);</li>
          <li>    }</li>
          <li>}</li>
          <li></li>
          <li>//---------------------------------------------------------------------------</li>
          <li class="selected">void vtkMRMLRulerDisplayableManager::vtkInternal::UpdateRuler()</li>
          <li>{</li>
          <li>  vtkMRMLAbstractViewNode* viewNode = vtkMRMLAbstractViewNode::SafeDownCast(this-&gt;External-&gt;GetMRMLDisplayableNode());</li>
          <li>  if (!viewNode || !viewNode-&gt;GetRulerEnabled())</li>
          <li>    {</li>
          <li>    vtkErrorWithObjectMacro(this-&gt;External, "vtkMRMLRulerDisplayableManager::UpdateMarkerOrientation() failed: view node is invalid");</li>
          <li>    this-&gt;ShowActors(false);</li>
          <li>    return;</li>
          <li>    }</li>
          <li></li>
          <li>  if (this-&gt;External-&gt;RulerScalePresets.empty())</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2023-07-17 17:40 UTC)

<p>The ruler is short to not interfere with corner annotations. The implementation should take the corner annotations into account (only make it wide if there is space; or shift things around the avoid overlap).</p>

---

## Post #4 by @jay1987 (2023-07-18 03:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ed8e648826627bfc21c58bb68ad6446ea51a63e.jpeg" data-download-href="/uploads/short-url/mFe919kg6Rgf3pIZEHZONeKaKHc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed8e648826627bfc21c58bb68ad6446ea51a63e_2_632x500.jpeg" alt="image" data-base62-sha1="mFe919kg6Rgf3pIZEHZONeKaKHc" width="632" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed8e648826627bfc21c58bb68ad6446ea51a63e_2_632x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed8e648826627bfc21c58bb68ad6446ea51a63e_2_948x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed8e648826627bfc21c58bb68ad6446ea51a63e_2_1264x1000.jpeg 2x" data-dominant-color="858585"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×1079 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
change to code</p>
<blockquote>
<p>double rulerPreferredLengthPixel = double(viewWidthPixel)/4.0;<br>
to<br>
double rulerPreferredLengthPixel = double(viewWidthPixel)/1.4;</p>
</blockquote>
<p>will make the ruler longer</p>

---
