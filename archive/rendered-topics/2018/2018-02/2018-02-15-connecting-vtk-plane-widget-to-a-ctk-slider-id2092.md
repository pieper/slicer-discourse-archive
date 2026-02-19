---
topic_id: 2092
title: "Connecting Vtk Plane Widget To A Ctk Slider"
date: 2018-02-15
url: https://discourse.slicer.org/t/2092
---

# Connecting vtk plane widget to a ctk slider

**Topic ID**: 2092
**Date**: 2018-02-15
**URL**: https://discourse.slicer.org/t/connecting-vtk-plane-widget-to-a-ctk-slider/2092

---

## Post #1 by @asheu (2018-02-15 18:38 UTC)

<p>I’ve received a lot of feedback in regards to how widgets work and am now moving forward with the suggestions. However, I am curious as to whether there is a way to connect existing widget functionalities with slider widgets? For example in my case, the vtk implicit plane widget allows rotation of slices. Is it possible to make connections of this to a ctk slider, i.e, make it such that I can move the ctk slider to update the angle of the slice that the implicit plane widget controls?</p>
<p>Thank you very much for the help!</p>

---

## Post #2 by @Davide_Punzo (2018-02-15 19:39 UTC)

<p>Hi Asheu,</p>
<p>you may have a look here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L2821-L2873" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L2821-L2873" target="_blank" rel="nofollow noopener">Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L2821-L2873</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="2821" style="counter-reset: li-counter 2820 ;">
<li>//---------------------------------------------------------------------------</li>
<li>void qSlicerAstroModelingModuleWidget::onMRMLYellowSliceRotated()</li>
<li>{</li>
<li>Q_D(const qSlicerAstroModelingModuleWidget);</li>
<li>
</li>
<li>if (!d-&gt;parametersNode || !this-&gt;mrmlScene())</li>
<li>  {</li>
<li>  return;</li>
<li>  }</li>
<li>
</li>
<li>vtkMRMLSliceNode *yellowSliceNode = vtkMRMLSliceNode::SafeDownCast</li>
<li>  (this-&gt;mrmlScene()-&gt;GetNodeByID("vtkMRMLSliceNodeYellow"));</li>
<li>if (!yellowSliceNode)</li>
<li>  {</li>
<li>  return;</li>
<li>  }</li>
<li>
</li>
<li>vtkMatrix4x4* yellowSliceToRAS = yellowSliceNode-&gt;GetSliceToRAS();</li>
<li>if (!yellowSliceToRAS)</li>
<li>  {</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L2821-L2873" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Essentially I have a value from a slider in my module GUI and i use the value to rotate the a slice in the XY plane. You don’t need to set the center of the slice (i.e. 4 colomun of the slice matrix yellowSliceToRAS, <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L2848-L2855" rel="nofollow noopener">https://github.com/Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L2848-L2855</a>).</p>

---

## Post #3 by @Davide_Punzo (2018-02-15 19:43 UTC)

<p>actually you can have also a look at the module Reformat, it does what you need.</p>

---

## Post #4 by @asheu (2018-02-15 22:38 UTC)

<p>for the reformat module, i’m finding that its functionality is in moving the angle through dragging the cursor which is comparably more difficult to find the slice angle that I want. That is why I am thinking that I could have a ctk slider being implemented in conjunction with the implicit plane widget so that it moves through slight angles at a time.</p>
<p>In any case, thank you very much for the sample code! I was wondering however which of the widgets were being connected? Are the nodes simply being connected to the qSlicerAstro widget?</p>

---

## Post #5 by @Davide_Punzo (2018-02-16 14:34 UTC)

<p>sorry maybe we are not understanding each other:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e2faacfa82c5f22967866d52d96aa0432ed19f0.png" data-download-href="/uploads/short-url/21uOi5DHliJZx3JGEsLgxu1Sb3G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e2faacfa82c5f22967866d52d96aa0432ed19f0_2_690x392.png" alt="image" data-base62-sha1="21uOi5DHliJZx3JGEsLgxu1Sb3G" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e2faacfa82c5f22967866d52d96aa0432ed19f0_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e2faacfa82c5f22967866d52d96aa0432ed19f0_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e2faacfa82c5f22967866d52d96aa0432ed19f0_2_1380x784.png 2x" data-dominant-color="9394A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1854×1054 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>in the module GUI you have 3 slider widgets (LR, PA, IS) which enable to set the angle of the slice rotation (kind of Euler angles). Is this not what you need??</p>

---

## Post #6 by @Davide_Punzo (2018-02-16 14:38 UTC)

<p>in my sample code the value of the rotation is saved in a parameter node which is modified here when you interact with the ctkslider:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L4746-L4760" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L4746-L4760" target="_blank" rel="nofollow noopener">Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L4746-L4760</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="4746" style="counter-reset: li-counter 4745 ;">
<li>//--------------------------------------------------------------------------</li>
<li>void qSlicerAstroModelingModuleWidget::onYellowSliceRotated(double value)</li>
<li>{</li>
<li>Q_D(qSlicerAstroModelingModuleWidget);</li>
<li>
</li>
<li>if (!d-&gt;parametersNode)</li>
<li>  {</li>
<li>  return;</li>
<li>  }</li>
<li>
</li>
<li>int wasModifying = d-&gt;parametersNode-&gt;StartModify();</li>
<li>d-&gt;parametersNode-&gt;SetYellowRotOldValue(d-&gt;parametersNode-&gt;GetYellowRotValue());</li>
<li>d-&gt;parametersNode-&gt;SetYellowRotValue(value);</li>
<li>d-&gt;parametersNode-&gt;EndModify(wasModifying);</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>the slot onMRMLYellowSliceRotated is connected with the parameter node here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L2972-L2974" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L2972-L2974" target="_blank" rel="nofollow noopener">Punzo/SlicerAstro/blob/master/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L2972-L2974</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="2972" style="counter-reset: li-counter 2971 ;">
<li>this-&gt;qvtkReconnect(d-&gt;parametersNode, AstroModelingParaNode,</li>
<li>                    vtkMRMLAstroModelingParametersNode::YellowRotationModifiedEvent,</li>
<li>                    this, SLOT(onMRMLYellowSliceRotated()));</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @asheu (2018-02-16 21:01 UTC)

<p>My apologies, I’ve updated this response a few times. I think what I am trying to do is to fix both the LR and IS slider in the Reformat module widget, and instead, only allow the user to change the PA slider. In that sense, I am looking for parts of the reformat widget that would allow us to eliminate the 2 other sliders</p>

---

## Post #8 by @asheu (2018-02-16 21:36 UTC)

<p>i believe this should be easily achievable through the sample widget that you have created correct?</p>

---

## Post #9 by @Davide_Punzo (2018-02-17 16:28 UTC)

<p>Yes, you can take a look at the code of the reformat module regarding one slider or use my sample code (if I remember well the only difference between the two is that I store the value of the slider in a MRMLParameterNode).</p>

---

## Post #10 by @asheu (2018-02-19 22:44 UTC)

<p>been delving through the code in the last few days and still a bit in over my head. is the ctk slider something that was packaged into the MRML parameter node or was there a particular location in the code where you called it to throw it into the GUI?</p>
<p>also cannot seem to find the part of the code that might control the LR, PA and IS orientations that the sliders would seem to modulate (and can’t seem to locate the source code for the reformat module either…)</p>
<p>Lot of questions but thank you so much for your responses, I really appreciate it</p>

---

## Post #11 by @Davide_Punzo (2018-02-20 10:24 UTC)

<p>Hi Alex, no problem.</p>
<ol>
<li>
<p>the ctk widget in my code was created using the designer (./Slicer --designer). There you can find all the ctk widgets. If you don’t want use the designer or you are using python, here is some C++ code taken from my ui file:</p>
<p>ctkSliderWidget *GreenSliceSliderWidget;<br>
GreenSliceSliderWidget = new ctkSliderWidget(OutputCollapsibleButton_2);<br>
GreenSliceSliderWidget-&gt;setObjectName(QStringLiteral(“GreenSliceSliderWidget”));<br>
GreenSliceSliderWidget-&gt;setMinimum(-200);<br>
GreenSliceSliderWidget-&gt;setMaximum(200);<br>
GreenSliceSliderWidget-&gt;setValue(0);<br>
gridLayout_2-&gt;addWidget(GreenSliceSliderWidget, 1, 1, 1, 1);</p>
</li>
<li>
<p>and here are the main parts of the code related to the rotation in the reformat module:</p>
</li>
</ol>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L394-L401" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L394-L401" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L394-L401</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="394" style="counter-reset: li-counter 393 ;">
<li>// Connect Slice rotation sliders</li>
<li>this-&gt;connect(d-&gt;LRSlider, SIGNAL(valueChanged(double)),</li>
<li>              this, SLOT(onSliderRotationChanged(double)));</li>
<li>this-&gt;connect(d-&gt;PASlider, SIGNAL(valueChanged(double)),</li>
<li>              this, SLOT(onSliderRotationChanged(double)));</li>
<li>this-&gt;connect(d-&gt;ISSlider, SIGNAL(valueChanged(double)),</li>
<li>              this, SLOT(onSliderRotationChanged(double)));</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L659-L708" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L659-L708" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L659-L708</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="659" style="counter-reset: li-counter 658 ;">
<li>//------------------------------------------------------------------------------</li>
<li>void qSlicerReformatModuleWidget::</li>
<li>onSliderRotationChanged(double rotation)</li>
<li>{</li>
<li>Q_D(qSlicerReformatModuleWidget);</li>
<li>
</li>
<li>vtkNew&lt;vtkTransform&gt; transform;</li>
<li>transform-&gt;SetMatrix(d-&gt;MRMLSliceNode-&gt;GetSliceToRAS());</li>
<li>
</li>
<li>if (this-&gt;sender() == d-&gt;LRSlider)</li>
<li>  {</li>
<li>  // Reset PA &amp; IS sliders</li>
<li>  d-&gt;resetSlider(d-&gt;PASlider);</li>
<li>  d-&gt;resetSlider(d-&gt;ISSlider);</li>
<li>
</li>
<li>  // Rotate on LR given the angle with the last value reccorded</li>
<li>  transform-&gt;RotateX(rotation-d-&gt;LastRotationValues[axisX]);</li>
<li>
</li>
<li>  // Update last value and apply the transform</li>
<li>  d-&gt;LastRotationValues[axisX] = rotation;</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L659-L708" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I hope this help</p>
<p>NOTE: while in 3DSlicer is always very nice to use MRMLNode to store parameters regarding the data and the  GUI of a module, I advice you for the moment just to follow the implementation of the Reformat module.<br>
Later on, if you’d like to see how a proper module should be designed and implemented, you can have a look at the Crop module (<a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/CropVolume" rel="nofollow noopener">https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/CropVolume</a>).</p>

---

## Post #12 by @asheu (2018-02-20 15:47 UTC)

<p>thank you so much! this has been very helpful!</p>

---

## Post #13 by @asheu (2018-02-26 17:30 UTC)

<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> I hope this finds you well. I was wondering from your UI file, is the OutputCollapsibleButton something that you had defined? Or is it a parameter that the ctkSliderWidget object can take in.</p>
<p>Also if possible, I was wondering what the ‘d’ object in the rotational sliders are. I see that the Reformat ModuleWidget defines it as such:</p>
<p>Q_D(qSlicerReformatModuleWidget);<br>
d-&gt;setupUi(this);</p>
<p>Is d just a default set up of the UI?</p>

---

## Post #14 by @Davide_Punzo (2018-02-26 18:03 UTC)

<p>Hi Alex,</p>
<ol>
<li>
<p>the OutputCollapsibleButton  is a ctk widget.<br>
here the code generated by the designer:</p>
<pre><code> OutputCollapsibleButton = new ctkCollapsibleButton(qSlicerAstroModelingModuleWidget);
 OutputCollapsibleButton-&gt;setObjectName(QStringLiteral("OutputCollapsibleButton"));
 OutputCollapsibleButton-&gt;setEnabled(true);
 QSizePolicy sizePolicy8(QSizePolicy::Minimum, QSizePolicy::Expanding);
 sizePolicy8.setHorizontalStretch(0);
 sizePolicy8.setVerticalStretch(0);
 sizePolicy8.setHeightForWidth(OutputCollapsibleButton-&gt;sizePolicy().hasHeightForWidth());
 OutputCollapsibleButton-&gt;setSizePolicy(sizePolicy8);
 OutputCollapsibleButton-&gt;setChecked(true);
 OutputCollapsibleButton-&gt;setCollapsed(false);
</code></pre>
</li>
<li>
<p>for d pointers, here is a reference: <a href="https://wiki.qt.io/D-Pointer" rel="nofollow noopener">https://wiki.qt.io/D-Pointer</a></p>
</li>
</ol>
<p>The d pointers point to the Private class, i.e. to:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Punzo/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L48" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L48" target="_blank" rel="nofollow noopener">Punzo/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx#L48</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="38" style="counter-reset: li-counter 37 ;">
<li>#include "vtkMRMLSliceLogic.h"</li>
<li>#include "vtkMRMLVolumeNode.h"</li>
<li>
</li>
<li>// VTK includes</li>
<li>#include &lt;vtkCamera.h&gt;</li>
<li>#include &lt;vtkMath.h&gt;</li>
<li>#include &lt;vtkNew.h&gt;</li>
<li>#include &lt;vtkTransform.h&gt;</li>
<li>
</li>
<li>//------------------------------------------------------------------------------</li>
<li class="selected">class qSlicerReformatModuleWidgetPrivate :</li>
<li>public Ui_qSlicerReformatModuleWidget</li>
<li>{</li>
<li>Q_DECLARE_PUBLIC(qSlicerReformatModuleWidget);</li>
<li>protected:</li>
<li>qSlicerReformatModuleWidget* const q_ptr;</li>
<li>
</li>
<li>public:</li>
<li>qSlicerReformatModuleWidgetPrivate(</li>
<li>  qSlicerReformatModuleWidget&amp; object);</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
