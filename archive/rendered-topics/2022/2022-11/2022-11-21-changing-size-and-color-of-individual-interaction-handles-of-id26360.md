# Changing Size and color of individual interaction handles of ROI

**Topic ID**: 26360
**Date**: 2022-11-21
**URL**: https://discourse.slicer.org/t/changing-size-and-color-of-individual-interaction-handles-of-roi/26360

---

## Post #1 by @maptekarev (2022-11-21 20:30 UTC)

<p>To implement ROI I am using vtkMRMLMarkupsROINode class. There is SetInteractionHandleScale() method in this class, but it is changing size of all interaction handles.<br>
Is it possible to change size and color of one individual interaction handle of ROI?</p>

---

## Post #2 by @pll_llq (2022-11-23 11:04 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> maybe you can give some insight here?</p>

---

## Post #3 by @cpinter (2022-11-23 12:08 UTC)

<p>The handle sizes and colors are hard-coded, see</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation.cxx#L1081-L1083">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation.cxx#L1081-L1083" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation.cxx#L1081-L1083" target="_blank" rel="noopener">Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation.cxx#L1081-L1083</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1081" style="counter-reset: li-counter 1080 ;">
          <li>this-&gt;AxisTranslationGlyphSource-&gt;SetTipRadius(INTERACTION_TRANSLATION_TIP_RADIUS);</li>
          <li>this-&gt;AxisTranslationGlyphSource-&gt;SetTipLength(INTERACTION_TRANSLATION_TIP_LENGTH / INTERACTION_WIDGET_RADIUS); // Scaled by INTERACTION_WIDGET_RADIUS later</li>
          <li>this-&gt;AxisTranslationGlyphSource-&gt;SetShaftRadius(INTERACTION_TRANSLATION_HANDLE_SHAFT_RADIUS);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation.cxx#L1322-L1331">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation.cxx#L1322-L1331" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation.cxx#L1322-L1331" target="_blank" rel="noopener">Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation.cxx#L1322-L1331</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1322" style="counter-reset: li-counter 1321 ;">
          <li>switch (index)</li>
          <li>  {</li>
          <li>  case 0:</li>
          <li>    currentColor = red;</li>
          <li>    break;</li>
          <li>  case 1:</li>
          <li>    currentColor = green;</li>
          <li>    break;</li>
          <li>  case 2:</li>
          <li>    currentColor = blue;</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @pll_llq (2022-11-23 16:09 UTC)

<p>Thanks for the insight <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #5 by @cpinter (2022-11-24 10:43 UTC)

<p><a class="mention" href="/u/maptekarev">@maptekarev</a> Can you tell us a bit about the motivation? I think the color can be made customizable relatively easily if you don’t need a GUI for that.</p>

---

## Post #6 by @maptekarev (2022-11-24 11:36 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Ii want the green and red handle on roi to correspond with feet color of the human model, and also change size or opacity of white corner handles.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f89a53d3f53f705a4cde8b1364b125d50805c990.png" data-download-href="/uploads/short-url/ztf3zQXXh9BmaUvv6XGM1ZS5LRC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f89a53d3f53f705a4cde8b1364b125d50805c990_2_690x428.png" alt="image" data-base62-sha1="ztf3zQXXh9BmaUvv6XGM1ZS5LRC" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f89a53d3f53f705a4cde8b1364b125d50805c990_2_690x428.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f89a53d3f53f705a4cde8b1364b125d50805c990_2_1035x642.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f89a53d3f53f705a4cde8b1364b125d50805c990_2_1380x856.png 2x" data-dominant-color="9C91C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1493×928 32.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @cpinter (2022-11-24 12:02 UTC)

<p>Ah OK, so it’s about ROIs. It is different from what I was investigating. FYI this is what interaction handle means without the special context you just mentioned:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bfc91ac3a504a1629dbd0b2b46da35157401c4c.png" alt="image" data-base62-sha1="d7KzJXccjsRzUvxHEq3JrT3BPNW" width="320" height="291"></p>
<p>The code is quite similar for ROIs though:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerROIRepresentation3D.cxx#L532-L552">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerROIRepresentation3D.cxx#L532-L552" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerROIRepresentation3D.cxx#L532-L552" target="_blank" rel="noopener">Slicer/Slicer/blob/3c592df27e3dccedbd8fcddf05979f59af484f2c/Modules/Loadable/Markups/VTKWidgets/vtkSlicerROIRepresentation3D.cxx#L532-L552</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="532" style="counter-reset: li-counter 531 ;">
          <li>double red[4]       = { 1.00, 0.00, 0.00, 1.00 };</li>
          <li>double green[4]     = { 0.00, 1.00, 0.00, 1.00 };</li>
          <li>double blue[4]      = { 0.00, 0.00, 1.00, 1.00 };</li>
          <li>double yellow[4]    = { 1.00, 1.00, 0.00, 1.00 };</li>
          <li>double lightGrey[4] = { 0.90, 0.90, 0.90, 1.00 };</li>
          <li></li>
          <li>double* currentColor = lightGrey;</li>
          <li>switch (index)</li>
          <li>  {</li>
          <li>  case 0: // L</li>
          <li>  case 1: // R</li>
          <li>    currentColor = red;</li>
          <li>    break;</li>
          <li>  case 2: // P</li>
          <li>  case 3: // A</li>
          <li>    currentColor = green;</li>
          <li>    break;</li>
          <li>  case 4: // I</li>
          <li>  case 5: // S</li>
          <li>    currentColor = blue;</li>
          <li>    break;</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I think customizing the color could be solved by adding members for the interaction handle colors to the markup display node (initialized with the hard-coded colors), and using these members in the two functions I have linked about colors. Note that in ROIs you have not three but six interaction colors, so this would need to be handled somehow if you want the left-right colors to be different (note the same red color setting for <code>L</code> and <code>R</code>). Maybe we could have <code>X</code>, <code>Y</code>, and <code>Z</code> interaction handle color getter/setters, with optional <code>AlternateX</code> or something similar for the inverse directions in the ROIs. <a class="mention" href="/u/lassoan">@lassoan</a> what do you think?</p>

---

## Post #8 by @lassoan (2022-11-25 05:41 UTC)

<p>ROI can be rotated, so there is no strict relationship between world coordinate system axis and ROI axis directions.</p>
<p>That said, the colors could be made customizable. If it is acceptable to provide only a low-level API (expose the color on the ROI representation class) then it is a very simple and small change. If we want to store it in MRML then it is a bigger change and I’m not sure if it is worth it (if it is an important use case or many users will ask for it then it is probaly worth the trouble implementing it).</p>

---
