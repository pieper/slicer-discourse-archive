# How to use Python to achieve the thresholding effect of the ‘Volumes’ module? (synchronized with the volume rendering)

**Topic ID**: 20891
**Date**: 2021-12-02
**URL**: https://discourse.slicer.org/t/how-to-use-python-to-achieve-the-thresholding-effect-of-the-volumes-module-synchronized-with-the-volume-rendering/20891

---

## Post #1 by @CharlesChen (2021-12-02 22:13 UTC)

<p>Hi there,<br>
I’m new to 3D Slicer.<br>
Currently, I am trying to develop a python scripted module in 3D Slicer.<br>
One of the features is to control the threshold of the volume rendering image through a slider.<br>
In other words, I want to use python to achieve the same effect as the ‘Threshold’ slider in the ‘Volumes’ module.<br>
As shown in the picture is my goal:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfc7c9bf15d86c3e1a007ec0386eb7cb5bf9cea5.jpeg" data-download-href="/uploads/short-url/rmzeVJxYCJLS2kZTtFet3TOrm6N.jpeg?dl=1" title="Sample image1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfc7c9bf15d86c3e1a007ec0386eb7cb5bf9cea5_2_517x252.jpeg" alt="Sample image1" data-base62-sha1="rmzeVJxYCJLS2kZTtFet3TOrm6N" width="517" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfc7c9bf15d86c3e1a007ec0386eb7cb5bf9cea5_2_517x252.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfc7c9bf15d86c3e1a007ec0386eb7cb5bf9cea5_2_775x378.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfc7c9bf15d86c3e1a007ec0386eb7cb5bf9cea5_2_1034x504.jpeg 2x" data-dominant-color="BABBD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sample image1</span><span class="informations">1536×751 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53b4fb4f9b0749e2b33ff3212bf60357b2386559.jpeg" data-download-href="/uploads/short-url/bWvnExSL7CAXkiT97XZ9oU4gGCZ.jpeg?dl=1" title="sample image2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53b4fb4f9b0749e2b33ff3212bf60357b2386559_2_517x262.jpeg" alt="sample image2" data-base62-sha1="bWvnExSL7CAXkiT97XZ9oU4gGCZ" width="517" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53b4fb4f9b0749e2b33ff3212bf60357b2386559_2_517x262.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53b4fb4f9b0749e2b33ff3212bf60357b2386559_2_775x393.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53b4fb4f9b0749e2b33ff3212bf60357b2386559_2_1034x524.jpeg 2x" data-dominant-color="BEBEDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample image2</span><span class="informations">1559×793 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Under the premise that the value in the check box on the right is set to ‘Manual’ and the ‘Synchronize with Volumes module’ in the ‘Volume Rendering’ module is checked, <strong>the user can see the volume rendering image synchronized with the slider</strong>.</p>
<p>I found that the ‘Volumes’ module is a Loadable module written in C++. How can I achieve my target effect with python(Just for this single feature)?</p>
<p>I have found the corresponding method (C++) for ‘Threshold’ in the ‘Volumes’ module according to the prompts on this page: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a>.</p>
<pre><code class="lang-auto">void qMRMLVolumeThresholdWidget::setAutoThreshold(int autoThreshold)
{
  this-&gt;setAutoThreshold(static_cast&lt;ControlMode&gt;(autoThreshold));
}

// --------------------------------------------------------------------------
void qMRMLVolumeThresholdWidget::setAutoThreshold(ControlMode autoThreshold)
{
  Q_D(qMRMLVolumeThresholdWidget);

  if (!d-&gt;VolumeDisplayNode)
    {
    return;
    }
  int oldAuto = d-&gt;VolumeDisplayNode-&gt;GetAutoThreshold();
  int oldApply = d-&gt;VolumeDisplayNode-&gt;GetApplyThreshold();

  int disabledModify = d-&gt;VolumeDisplayNode-&gt;StartModify();
  if (autoThreshold == qMRMLVolumeThresholdWidget::Off)
    {
    d-&gt;VolumeDisplayNode-&gt;SetApplyThreshold(0);
    }
  else
    {
    d-&gt;VolumeDisplayNode-&gt;SetApplyThreshold(1);
    d-&gt;VolumeDisplayNode-&gt;SetAutoThreshold(
      autoThreshold == qMRMLVolumeThresholdWidget::Auto ? 1 : 0);
    }

  if (!oldApply &amp;&amp; autoThreshold == qMRMLVolumeThresholdWidget::Manual)
    {
    // Previously the threshold was turned off and now it is set to manual.
    // Since the default threshold range is VTK_SHORT_MIN to VTK_SHORT_MAX,
    // we don't want these values to appear on the GUI but instead set
    // the threshold range to the full scalar range of the volume (because
    // this corresponds to the previous state of the thresholding: having
    // the full scalar range of the volume in the threshold range).
    d-&gt;VolumeDisplayNode-&gt;SetThreshold(d-&gt;DisplayScalarRange[0], d-&gt;DisplayScalarRange[1]);
    }

  d-&gt;VolumeDisplayNode-&gt;EndModify(disabledModify);

  if (oldAuto != d-&gt;VolumeDisplayNode-&gt;GetAutoThreshold() ||
      oldApply != d-&gt;VolumeDisplayNode-&gt;GetApplyThreshold())
    {
    emit this-&gt;autoThresholdValueChanged(autoThreshold);
    }
}
</code></pre>
<p>However, I’m not sure if the above code(<a href="https://github.com/Slicer/Slicer/blob/c20e0a7849889e17224a5e605cc1df662b5ad977/Libs/MRML/Widgets/qMRMLVolumeThresholdWidget.cxx" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/c20e0a7849889e17224a5e605cc1df662b5ad977/Libs/MRML/Widgets/qMRMLVolumeThresholdWidget.cxx</a>) is accurate or not and I’m confused about how to convert it into Python code next.</p>
<p>In addition, I also found another method by searching online:<br>
<code>displayNode-&gt;SetFollowVolumeDisplayNode(follow ? 1 : 0);</code><br>
How can I integrate it into my code?</p>
<p>The following is the code of the slider I implemented in Python, FYI:</p>
<pre><code class="lang-auto">    #
    # thresholdRangeSlider
    #
    self.thresholdRangeSlider1 = ctk.ctkRangeWidget()
    self.thresholdRangeSlider1.minimum = 0.0
    self.thresholdRangeSlider1.maximum = 3522.0
    self.thresholdRangeSlider1.singleStep = 0.1

    self.thresholdRangeSlider1.minimumValue = 10.0
    self.thresholdRangeSlider1.maximumValue = 3522.0
    parametersFormLayout.addRow("Thresholds:", self.thresholdRangeSlider1)
    
    # connections
    self.thresholdRangeSlider1.connect('currentNodeChanged(vtkMRMLNode*)', self.onSlider)
    

    # Custom function
    def onSlider(self):
    
</code></pre>
<p>Should I implement my target feature in the custom ‘onSlider’ function? is that right? In addition, I am not sure whether the first parameter’currentNodeChanged(vtkMRMLNode*)’ in the ‘connect’ method is correct.</p>
<p>If possible, could you please give me some specific guidance to help me run in the right way, thank you very much for your help in advance!</p>
<p>Best regards,<br>
Charles</p>

---

## Post #2 by @mikebind (2021-12-02 23:34 UTC)

<p>This is surprisingly hard to track down.  This documentation page has a lot of information on how to set up and customize volume rendering: <a href="https://slicer.readthedocs.io/en/v4.11/developer_guide/modules/volumerendering.html" class="inline-onebox">Volume rendering — 3D Slicer documentation</a></p>
<p>However, there do not appear to be simple convenience functions reproducing what the “Shift” slider in the Volume Rendering module does.  As far as I have been able to follow it, changing the slider value sends a signal to the <code>VolumePropertyNodeWidget</code>, calling <code>moveAllPoints(xOffset, yOffset, False)</code>.  <code>VolumePropertyNodeWidget</code> in turn calls <code>VolumePropertyWidget -&gt; moveAllPoints(xOffset, yOffset, False)</code>. At that point we move outside the Slicer github code base because <code>VolumePropertyWidget</code> is actually a <a href="http://www.commontk.org/docs/html/classctkVTKVolumePropertyWidget.html#ae1da08f4e593396997895f3732703e44">ctkVTKVolumePropertyWidget</a> (code <a href="https://github.com/commontk/CTK/blob/master/Libs/Visualization/VTK/Widgets/ctkVTKVolumePropertyWidget.cpp">here</a>).  <code>moveAllPoints</code> here calls a <code>moveAllPoints</code> function in a <code>ScalarOpacityWidget</code> and a <code>ScalarColorWidget</code>. I haven’t yet found the code which will be run by the <code>ScalarOpacityWidget</code> or the <code>ScalarColorWidget</code>, but I think it’s clear that the ultimate result will be moving all of the control points of the scalar opacity transfer function and the scalar color transfer function by an <code>xOffset</code> amount based on the location of the Shift scalar.  This is going to have to occur through changes in the <code>VolumeProperty</code> of the <code>VolumePropertyNode</code>. The volume property node is a MRML node that you can explore in the python interactor.  For example, set your rendering preset to <code>'MR-Default'</code> and then type <code>volPropNode=getNode('MR-Default')</code> in the python interactor.  <code>volProp = volPropNode.GetVolumeProperty()</code> gets the <code>vtkVolumeProperty</code>.  <code>volProp.GetScalarOpacity()</code> reveals that the scalar opacity is a <code>vtkPiecewiseFunction</code> (<a href="https://vtk.org/doc/nightly/html/classvtkPiecewiseFunction.html">documentation here</a>).  Again, there is no convenience function for shifting all the control points, but it looks like you can get the value at control point nodes using <code>GetNodeValue()</code>.  As an approach, you could collect all the current values at control point nodes, remove all the points, and then add them back in a shifted location.  So far, I’m not seeing any easier way to accomplish this.</p>

---

## Post #3 by @CharlesChen (2021-12-03 00:12 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="20891" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>This is surprisingly hard to track down. This documentation page has a lot of information on how to set up and customize volume rendering: <a href="https://slicer.readthedocs.io/en/v4.11/developer_guide/modules/volumerendering.html" rel="noopener nofollow ugc">Volume rendering — 3D Slicer documentation </a></p>
<p>However, there do not appear to be simple convenience functions reproducing what the “Shift” slider in the Volume Rendering module does. As far as I have been able to follow it, changing the slider value sends a signal to the <code>VolumePropertyNodeWidget</code> , calling <code>moveAllPoints(xOffset, yOffset, False)</code> . <code>VolumePropertyNodeWidget</code> in turn calls <code>VolumePropertyWidget -&gt; moveAllPoints(xOffset, yOffset, False)</code> . At that point we move outside the Slicer github code base because <code>VolumePropertyWidget</code> is actually a <a href="http://www.commontk.org/docs/html/classctkVTKVolumePropertyWidget.html#ae1da08f4e593396997895f3732703e44" rel="noopener nofollow ugc">ctkVTKVolumePropertyWidget</a> (code <a href="https://github.com/commontk/CTK/blob/master/Libs/Visualization/VTK/Widgets/ctkVTKVolumePropertyWidget.cpp" rel="noopener nofollow ugc">here</a>). <code>moveAllPoints</code> here calls a <code>moveAllPoints</code> function in a <code>ScalarOpacityWidget</code> and a <code>ScalarColorWidget</code> . I haven’t yet found the code which will be run by the <code>ScalarOpacityWidget</code> or the <code>ScalarColorWidget</code> , but I think it’s clear that the ultimate result will be moving all of the control points of the scalar opacity transfer function and the scalar color transfer function by an <code>xOffset</code> amount based on the location of the Shift scalar. This is going to have to occur through changes in the <code>VolumeProperty</code> of the <code>VolumePropertyNode</code> . The volume property node is a MRML node that you can explore in the python interactor. For example, set your rendering preset to <code>'MR-Default'</code> and then type <code>volPropNode=getNode('MR-Default')</code> in the python interactor. <code>volProp = volPropNode.GetVolumeProperty()</code> gets the <code>vtkVolumeProperty</code> . <code>volProp.GetScalarOpacity()</code> reveals that the scalar opacity is a <code>vtkPiecewiseFunction</code> (<a href="https://vtk.org/doc/nightly/html/classvtkPiecewiseFunction.html" rel="noopener nofollow ugc">documentation here</a>). Again, there is no convenience function for shifting all the control points, but it looks like you can get the value at control point nodes using <code>GetNodeValue()</code> . As an approach, you could collect all the current values at control point nodes, remove all the points, and then add them back in a shifted location. So far, I’m not seeing any easier way to accomplish this.</p>
</blockquote>
</aside>
<p>Hello Mike,<br>
Thank you very much for your quick and kindly reply. You mentioned a lot of knowledge points that I have not learned before, and I will refer to them. I realize that to implement this seemingly simple function seems to have to learn a lot…<br>
Hello <a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, do you have any comments on my issue? Or do I need to add an observer or something like that to do it? Could you please give me more guidance? Thank you so much!</p>

---

## Post #4 by @CharlesChen (2021-12-03 00:29 UTC)

<p>As a supplement:<br>
It seems that the slider in the ‘Volumes’ module affects the appearance of the volume rendering image actually by affecting the threshold range of the image data (as shown in the 3 slice windows).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da9b535ad7282bbbf09295aa88f8e4609e7173b3.png" data-download-href="/uploads/short-url/vbSS4tmC8w1ignIb5PVqRPIzOmf.png?dl=1" title="sample image3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9b535ad7282bbbf09295aa88f8e4609e7173b3_2_516x312.png" alt="sample image3" data-base62-sha1="vbSS4tmC8w1ignIb5PVqRPIzOmf" width="516" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9b535ad7282bbbf09295aa88f8e4609e7173b3_2_516x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9b535ad7282bbbf09295aa88f8e4609e7173b3_2_774x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9b535ad7282bbbf09295aa88f8e4609e7173b3_2_1032x624.png 2x" data-dominant-color="9C9B9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample image3</span><span class="informations">1207×728 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>From this perspective, the function of this slider is actually similar to the sliders above the 3 slice windows that can be used to adjust the positions of slices in real-time. However, what I want is to enable the volume rendering image can be updated in real-time.</p>

---

## Post #5 by @mikebind (2021-12-03 08:01 UTC)

<p>I put together a working python function which allows shifting scalar opacity in a similar way to moving the “Shift” slider.</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c.js">
  <header class="source">

      <a href="https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c.js" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c.js" target="_blank" rel="noopener">https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c.js</a></h4>

  <h5>shiftVolumeRenderingGist.py</h5>
  <pre><code class="Python">def shiftVolumeRendering(volumePropertyNode, xOffset=0):
  """ Shift the scalar opacity control point values by an 
  offset value (similar to moving the "Shift" slider in the volume rendering module)
  """
  volProp = volumePropertyNode.GetVolumeProperty()
  scalarOpacity = volProp.GetScalarOpacity() # this is a vtkPiecewiseFunction
  pointIdx = 0
  opacityPointValues = [] # list to hold values
  # Gather Existing Values
  for pointIdx in range( scalarOpacity.GetSize() ):</code></pre>
    This file has been truncated. <a href="https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c.js" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hopefully this will be helpful.  I tried it out and it worked well for me.  It isn’t linked to a slider, but the basic functionality is there.</p>

---

## Post #6 by @CharlesChen (2021-12-03 15:00 UTC)

<p>Hello Mike,<br>
Thank you so much! I will take a reference <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #7 by @mikebind (2021-12-03 17:10 UTC)

<p>Sorry, it looks like I messed up the link to the gist above.  This was my first time trying that and it looks like I copied a javascript embedding link instead of just a link to the gist.  Try this one instead:</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c">
  <header class="source">

      <a href="https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c" target="_blank" rel="noopener">https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c</a></h4>

  <h5>shiftVolumeRenderingGist.py</h5>
  <pre><code class="Python">def shiftVolumeRendering(volumePropertyNode, xOffset=0):
  """ Shift the scalar opacity control point values by an 
  offset value (similar to moving the "Shift" slider in the volume rendering module)
  """
  volProp = volumePropertyNode.GetVolumeProperty()
  scalarOpacity = volProp.GetScalarOpacity() # this is a vtkPiecewiseFunction
  pointIdx = 0
  opacityPointValues = [] # list to hold values
  # Gather Existing Values
  for pointIdx in range( scalarOpacity.GetSize() ):</code></pre>
    This file has been truncated. <a href="https://gist.github.com/mikebind/88e19559c6b1c104d71f75083bcffb7c" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @rbumm (2021-12-03 18:04 UTC)

<p>You should be able to interact with the VolumeDisplayNode as easily as shown here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#turning-off-interpolation" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#turning-off-interpolation</a></p>
<p><a href="https://apidocs.slicer.org/master/classvtkMRMLScalarVolumeDisplayNode.html" rel="noopener nofollow ugc">vtkMRMLScalarVolumeDisplayNode</a> has several functions to set / change threshold and level.</p>

---

## Post #9 by @mikebind (2021-12-03 21:59 UTC)

<p>It looks like I also misread your initial question as pertaining to the volume rendering “Shift” slider when you wrote that you were interested in the threshold slider of the Volumes module.  My mistake!  As <a class="mention" href="/u/rbumm">@rbumm</a> pointed out, there <em>are</em> very easy ways to set those values. The only thing I would add is that you can get the display node for your volume of interest using <code>GetDisplayNode()</code>. For example:</p>
<pre><code class="lang-auto">volumeName =  "MR_Head" # replace with the name of your volume
volNode = getNode(volumeName)
dispNode = volNode.GetDisplayNode()
lowerThreshValue = 100 # for example
upperThreshValue = 500 # for example
dispNode.SetThreshold(lowerThreshValue, upperThreshValue)
</code></pre>

---

## Post #10 by @CharlesChen (2021-12-03 22:51 UTC)

<p>Dear Bumm, Mike<br>
Thank you for your guidance! Now I can change the threshold value of the displaynode(Volume rendering image) by running this piece of code in my Python console.</p>
<blockquote>
<p>volumeName =  “MR_Head” # replace with the name of your volume<br>
volNode = getNode(volumeName)<br>
dispNode = volNode.GetDisplayNode()<br>
lowerThreshValue = 100 # for example<br>
upperThreshValue = 500 # for example<br>
dispNode.SetThreshold(lowerThreshValue, upperThreshValue)</p>
</blockquote>
<p>I think the next thing I’m trying to do is to achieve that it(display node’s threshold) changes dynamically while adjusting the slider.</p>
<p>I will take a reference of the shiftVolumeRenderingGist.py you provided to do this.<br>
By the way, is this script( shiftVolumeRenderingGist.py) achieved the slider thing?<br>
Maybe I need an observer to do it? Cause I’m still not familiar with how to do this in python.<br>
So, If there are some other suggestions/useful scripts that can help me to do <strong>changing the parameters in real-time via the slider</strong> (In my case, the parameter is the threshold value of the display node) please let me know.  Thank you so much!!!</p>

---

## Post #11 by @mikebind (2021-12-04 00:02 UTC)

<p>This should work for you:</p>
<pre><code class="lang-auto">volumeName = 'MR_Head' # replace with the name of your volume
volNode = getNode(volumeName)

# Define function that will update the thresholds for a given volume
def updateThresholdOnVolume(volNode, lower, upper):
  displayNode = volNode.GetDisplayNode()
  displayNode.SetThreshold(lower, upper)

# Set up a version of the function where the volume node has already been suppled 
updateThreshold = lambda lower, upper: updateThresholdOnVolume(volNode, lower, upper)
# Create GUI widget to control thresholds
windowLevelWidget = slicer.qMRMLWindowLevelWidget()
# Connect it with the image volume (so auto thresholding and automatic ranges will work correctly)
windowLevelWidget.setMRMLVolumeNode(volNode)
# Connect the 'windowLevelValuesChanged' signal with the updateThreshold callback
windowLevelWidget.connect('windowLevelValuesChanged(double,double)', updateThreshold)
# Make the widget visible
windowLevelWidget.show()

</code></pre>
<p>Documentation: <a href="https://apidocs.slicer.org/master/classqMRMLWindowLevelWidget.html" class="inline-onebox">Slicer: qMRMLWindowLevelWidget Class Reference</a></p>

---

## Post #12 by @CharlesChen (2021-12-04 00:55 UTC)

<p>Hello Mike,<br>
Thank you for your reply!<br>
I tried the code you just provided in my python console.<br>
Now I can see a slider, and the slices in the other three slice views can be changed accordingly. That’s cool!<br>
However, the volume rendering image located in the upper right seems still hasn’t changed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9f4858fda625405892902077cbb8a816ce617d3.png" data-download-href="/uploads/short-url/zFcM578tzLsUnMEDAQFqQUC3hKz.png?dl=1" title="effect1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9f4858fda625405892902077cbb8a816ce617d3_2_344x375.png" alt="effect1" data-base62-sha1="zFcM578tzLsUnMEDAQFqQUC3hKz" width="344" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9f4858fda625405892902077cbb8a816ce617d3_2_344x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9f4858fda625405892902077cbb8a816ce617d3_2_516x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9f4858fda625405892902077cbb8a816ce617d3_2_688x750.png 2x" data-dominant-color="C8C8CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">effect1</span><span class="informations">967×1052 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd47a236f0780b45838b04692976984e2285d170.png" data-download-href="/uploads/short-url/vzwZI9KnLgaQqMvc06sRx05l9ok.png?dl=1" title="effect2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd47a236f0780b45838b04692976984e2285d170_2_339x375.png" alt="effect2" data-base62-sha1="vzwZI9KnLgaQqMvc06sRx05l9ok" width="339" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd47a236f0780b45838b04692976984e2285d170_2_339x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd47a236f0780b45838b04692976984e2285d170_2_508x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd47a236f0780b45838b04692976984e2285d170_2_678x750.png 2x" data-dominant-color="C5C4C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">effect2</span><span class="informations">977×1079 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know how to fix it? is the issue with the ‘displayNode’?<br>
Thank you very much!</p>

---

## Post #13 by @koeglfryderyk (2021-12-05 09:20 UTC)

<p>Hi, thanks for this suggestion. However, it only works partially. Here’s what’s happening in my case:<br>
I added a shortcut that calls this code. When I press the shortcut-key, I see that in the GUI the threshold slider has moved to those values, however, the appearance in the Red, Green, and Yellow slices have not been updated. To make the views update I need to manually nudge the threshold slider in the GUI.</p>
<p>Any idea why this is happening?</p>

---

## Post #14 by @mikebind (2021-12-06 16:32 UTC)

<p>Providing a link to where a solution was provided for <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> 's issue.</p>
<aside class="quote" data-post="1" data-topic="20919">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/changing-threshold-in-python-does-not-update-in-any-views/20919">Changing threshold in python does not update in any views</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I want to use a shortcut to change the lower threshold of a foreground US volume to 1 (so that the black surrounding pixels disappear). 
I used the code from <a href="https://discourse.slicer.org/t/how-to-use-python-to-achieve-the-thresholding-effect-of-the-volumes-module-synchronized-with-the-volume-rendering/20891/9">here</a>, and this code changes the threshold in the GUI, however, it doesn’t ‘propagate’ to any of the views - nothing changes there. I still need to manually nudge the slider/value a bit for the view to be updated. 
Is there any command that needs to be executed for the view to be updated?
  </blockquote>
</aside>


---

## Post #15 by @CharlesChen (2021-12-06 17:07 UTC)

<p>Hello Mike <a class="mention" href="/u/mikebind">@mikebind</a> ,<br>
I tried the code above in my console, but there are still no changes with the volume rendering image, do you have any comments and guidance about this? how can I change the visible threshold of the volume rendering image on the upper right based on the code you provided? I think I’m close to it.<br>
Thank you so much!</p>

---

## Post #16 by @mikebind (2021-12-06 17:21 UTC)

<p>In the Volume Rendering module, make sure this box is checked</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/685fa16e67ae98df8897a81862aa8e8a21019fdc.png" alt="image" data-base62-sha1="eTkxL91lXH9NGfgVnSyevfhe5SQ" width="433" height="281"></p>
<p>You could do this in code by adding the line <code>displayNode.ApplyThresholdOn()</code> to the <code>updateThresholdOnVolume</code> function above.</p>

---

## Post #17 by @CharlesChen (2021-12-10 14:21 UTC)

<p>Hello Mike，<br>
It’s working! Thank you so much for your help!</p>
<p>Best regards，<br>
Charles</p>

---

## Post #18 by @WilliamDaniel (2022-01-06 18:40 UTC)

<p>Hello Mike,<br>
I also tried the code you mentioned above in the python console of slicer:</p>
<pre><code class="lang-auto">volumeName = 'MR_Head' # replace with the name of your volume
volNode = getNode(volumeName)

# Define function that will update the thresholds for a given volume
def updateThresholdOnVolume(volNode, lower, upper):
  displayNode = volNode.GetDisplayNode()
  displayNode.SetThreshold(lower, upper)

# Set up a version of the function where the volume node has already been suppled 
updateThreshold = lambda lower, upper: updateThresholdOnVolume(volNode, lower, upper)
# Create GUI widget to control thresholds
windowLevelWidget = slicer.qMRMLWindowLevelWidget()
# Connect it with the image volume (so auto thresholding and automatic ranges will work correctly)
windowLevelWidget.setMRMLVolumeNode(volNode)
# Connect the 'windowLevelValuesChanged' signal with the updateThreshold callback
windowLevelWidget.connect('windowLevelValuesChanged(double,double)', updateThreshold)
# Make the widget visible
windowLevelWidget.show()
</code></pre>
<p>But I found that the ‘windowLevelWidget’ in the code actually implements the first slider in the Volumes module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6315986d23fc837e1d3b8277e4db4b11a7bde0b6.png" data-download-href="/uploads/short-url/e8xxkisXHd6GRa96SAbXmyWYCDI.png?dl=1" title="slider-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6315986d23fc837e1d3b8277e4db4b11a7bde0b6_2_517x193.png" alt="slider-1" data-base62-sha1="e8xxkisXHd6GRa96SAbXmyWYCDI" width="517" height="193" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6315986d23fc837e1d3b8277e4db4b11a7bde0b6_2_517x193.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6315986d23fc837e1d3b8277e4db4b11a7bde0b6_2_775x289.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6315986d23fc837e1d3b8277e4db4b11a7bde0b6_2_1034x386.png 2x" data-dominant-color="757375"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slider-1</span><span class="informations">1762×659 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I think their requirement is to implement the ‘Threshold’ slider below(The second slider):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06a41a55a25e38de89a69311dba4ea6b754acb6a.png" data-download-href="/uploads/short-url/WKs7Dcf7A2ZGXsRiBT0ZyZbcIq.png?dl=1" title="slider-2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a41a55a25e38de89a69311dba4ea6b754acb6a_2_517x193.png" alt="slider-2" data-base62-sha1="WKs7Dcf7A2ZGXsRiBT0ZyZbcIq" width="517" height="193" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a41a55a25e38de89a69311dba4ea6b754acb6a_2_517x193.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a41a55a25e38de89a69311dba4ea6b754acb6a_2_775x289.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a41a55a25e38de89a69311dba4ea6b754acb6a_2_1034x386.png 2x" data-dominant-color="757375"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slider-2</span><span class="informations">1762×659 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To do this, does it mean we just need to change the GUI widget here? If so, what should be changed to the ‘windowLevelWidget’? and what should be the first parameter in the ‘connect’ method?</p>
<p>Could you please point out how to do this?<br>
Thank you very much!</p>
<p>Best regards,<br>
Daniel</p>

---

## Post #19 by @mikebind (2022-01-06 19:31 UTC)

<p>Good catch!  I could have sworn I tested this out before posting, but apparently not well enough.  The above snippet of code does indeed set the threshold values based on the slider values of the created widget (displayNode.SetThreshold() is the correct function for that), but it simultaneously also sets the window and level values (through some sort of automatic linkage between a qMRMLWindowLevelWidget and the volume node you associate with it, I presume). The resulting behavior is sub-optimal <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Luckily, it is easy to set right.  As you anticipated, we just need to change the widget we create.  The correct widget is <code>qMRMLVolumeThresholdWidget()</code>.  Because of the automatic linkage, once we associate the volume node we don’t need to connect the <code>updateThreshold()</code> function, the volume displays will already dynamically update with changes to the slider.</p>
<pre><code class="lang-auto">volumeName = 'MR_Head' # replace with the name of your volume
volNode = getNode(volumeName)
thresholdWidget = slicer.qMRMLVolumeThresholdWidget()
thresholdWidget.setMRMLVolumeNode(volNode)
thresholdWidget.show()
</code></pre>
<p>For completeness, the signal you would need to connect to if you wanted to have an additional callback run when the threshold slider values are changed is <code>'thresholdValuesChanged(double,double)'</code>, but this is not necessary because of the automatic linkage once you set the associated volume node. Documentation available at <a href="https://apidocs.slicer.org/master/classqMRMLVolumeThresholdWidget.html" class="inline-onebox">Slicer: qMRMLVolumeThresholdWidget Class Reference</a>.</p>
<p>Let me know if this doesn’t work for you or if there are further questions.</p>

---

## Post #20 by @CharlesChen (2022-01-06 20:03 UTC)

<p>Hello Daniel,<br>
As you mentioned, I had the same problem before.<br>
Like Mike just replied, based on the previous code, I changed <code>qMRMLWindowLevelWidget </code> to <code>qMRMLVolumeThresholdWidget</code>, and changed the first parameter of the connect method to <code>thresholdValuesChanged(double, double)</code>. Then it worked!</p>
<p>Mike just replied a simpler way and it is also effective! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"><br>
I hope this consultation can help you.</p>
<p>Best,<br>
Charles</p>

---

## Post #21 by @WilliamDaniel (2022-01-06 21:15 UTC)

<p>Hello Mike and Charles,<br>
Thank you very much for your kind and patient explanations. Now I can successfully run this code and achieve the purpose of thresholding the volume rendering image. I learned a lot from this exercise.<br>
Thanks again!</p>

---

## Post #22 by @WilliamDaniel (2022-01-25 23:06 UTC)

<p>Hello Mike <a class="mention" href="/u/mikebind">@mikebind</a> ,<br>
Following the advice and code in this post of yours, I’ve been able to successfully add this slider for adjusting the threshold of volume-rendered images to my module.<br>
As shown below: For this part of my module, users needs to set the input volume first to do the next Thresholding step.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eeeac3d2ffa333202b46c42427ff80d6bb9ec82.png" data-download-href="/uploads/short-url/bggB0d6Wcf2ddjMKJERv9y3rUMG.png?dl=1" title="figure1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eeeac3d2ffa333202b46c42427ff80d6bb9ec82_2_517x189.png" alt="figure1" data-base62-sha1="bggB0d6Wcf2ddjMKJERv9y3rUMG" width="517" height="189" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eeeac3d2ffa333202b46c42427ff80d6bb9ec82_2_517x189.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eeeac3d2ffa333202b46c42427ff80d6bb9ec82_2_775x283.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eeeac3d2ffa333202b46c42427ff80d6bb9ec82.png 2x" data-dominant-color="9F9EA7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure1</span><span class="informations">939×343 94.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However now I find that when I switch the input volume to the a new one(after I load one more volume as input here), the slider doesn’t work anymore:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15389ce73326f441a30ceb87f3f4e7225d7edc0f.png" data-download-href="/uploads/short-url/31JjO1iwey79OdwbzedfqMOPGR9.png?dl=1" title="figure2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15389ce73326f441a30ceb87f3f4e7225d7edc0f_2_517x193.png" alt="figure2" data-base62-sha1="31JjO1iwey79OdwbzedfqMOPGR9" width="517" height="193" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15389ce73326f441a30ceb87f3f4e7225d7edc0f_2_517x193.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15389ce73326f441a30ceb87f3f4e7225d7edc0f_2_775x289.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15389ce73326f441a30ceb87f3f4e7225d7edc0f.png 2x" data-dominant-color="B1B1B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure2</span><span class="informations">935×350 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It seems that it only works on the first individual input volume.<br>
I attached my code here, could you please give me some suggestions to solve this bug?<br>
When you test it, please make sure the checkbox of ‘Synchronize with Volumes module’ is checked.<br>
Thank you very much!!!</p>
<pre><code class="lang-auto">import logging
import os
import unittest
import vtk, qt, ctk, slicer
import SegmentStatistics
from slicer.ScriptedLoadableModule import *
from slicer.util import TESTING_DATA_URL
from slicer.util import VTKObservationMixin



class ScriptedLoadableModuleTemplate(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "My Test Module" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Test Extension 2"]
    self.parent.dependencies = []
    self.parent.contributors = ["John Doe (AnyWare Corp.)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
    The Help text for this scripted module.
"""
    self.parent.helpText += self.getDefaultModuleDocumentationLink()
    self.parent.acknowledgementText = """
   The acknowledgementText
"""
#
# ScriptedLoadableModuleTemplateWidget
#

class ScriptedLoadableModuleTemplateWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """



  def __init__(self, parent=None):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.__init__(self, parent)
    VTKObservationMixin.__init__(self)  # needed for parameter node observation
    self.logic = None
    self._parameterNode = None
    self._updatingGUIFromParameterNode = False

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Threshold"
    self.layout.addWidget(parametersCollapsibleButton)
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    #
    # input volume selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ["vtkMRMLScalarVolumeNode"]
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = False
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = False
    self.inputSelector.setMRMLScene(slicer.mrmlScene)
    self.inputSelector.setToolTip( "Pick the input." )
    parametersFormLayout.addRow("Input Volume: ", self.inputSelector)

    #
    # thresholdRangeSlider
    #
    self.thresholdRangeSlider1 = slicer.qMRMLVolumeThresholdWidget()
    parametersFormLayout.addRow(self.thresholdRangeSlider1)

    def updateThresholdOnVolume(volNode, lower, upper):
      displayNode = volNode.GetDisplayNode()
      displayNode.SetThreshold(lower, upper)
      displayNode.ApplyThresholdOn()

    updateThreshold = lambda lower, upper: updateThresholdOnVolume(volNode, lower, upper)

    volNode = slicer.util.getNode(self.inputSelector.currentNode().GetName())
    self.thresholdRangeSlider1.setMRMLVolumeNode(volNode)

    self.logic = ScriptedLoadableModuleTemplateLogic()
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.StartCloseEvent, self.onSceneStartClose)
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.EndCloseEvent, self.onSceneEndClose)

    # connections
    self.inputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)
    self.thresholdRangeSlider1.connect('thresholdValuesChanged(double, double)', updateThreshold)


    self.initializeParameterNode()

    # Add vertical spacer
    self.layout.addStretch(1)


  # def cleanup(self):
  #   pass
  def cleanup(self):
    """
    Called when the application closes and the module widget is destroyed.
    """
    self.removeObservers()

  def enter(self):
    """
    Called each time the user opens this module.
    """
    # Make sure parameter node exists and observed
    self.initializeParameterNode()


  def exit(self):
    """
    Called each time the user opens a different module.
    """
    # Do not react to parameter node changes (GUI wlil be updated when the user enters into the module)
    self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

  def onSceneStartClose(self, caller, event):
    """
    Called just before the scene is closed.
    """
    # Parameter node will be reset, do not use it anymore
    self.setParameterNode(None)

  def onSceneEndClose(self, caller, event):
    """
    Called just after the scene is closed.
    """
    # If this module is shown while the scene is closed then recreate a new parameter node immediately
    if self.parent.isEntered:
      self.initializeParameterNode()


  def initializeParameterNode(self):
    """
    Ensure parameter node exists and observed.
    """
    # Parameter node stores all user choices in parameter values, node selections, etc.
    # so that when the scene is saved and reloaded, these settings are restored.

    self.setParameterNode(self.logic.getParameterNode())

    # Select default input nodes if nothing is selected yet to save a few clicks for the user
    if not self._parameterNode.GetNodeReference("InputVolume"):
      firstVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
      if firstVolumeNode:
        self._parameterNode.SetNodeReferenceID("InputVolume", firstVolumeNode.GetID())


  def setParameterNode(self, inputParameterNode):
    """
    Set and observe parameter node.
    Observation is needed because when the parameter node is changed then the GUI must be updated immediately.
    """
    # Unobserve previously selected parameter node and add an observer to the newly selected.
    # Changes of parameter node are observed so that whenever parameters are changed by a script or any other module
    # those are reflected immediately in the GUI.
    if self._parameterNode is not None:
      self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
    self._parameterNode = inputParameterNode
    if self._parameterNode is not None:
      self.addObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

    # Initial GUI update
    self.updateGUIFromParameterNode()


  def updateGUIFromParameterNode(self, caller=None, event=None):
    """
    This method is called whenever parameter node is changed.
    The module GUI is updated to show the current state of the parameter node.
    """

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    # Make sure GUI changes do not call updateParameterNodeFromGUI (it could cause infinite loop)
    self._updatingGUIFromParameterNode = True

    # Update node selectors and sliders
    self.inputSelector.setCurrentNode(self._parameterNode.GetNodeReference("InputVolume"))
    # All the GUI updates are done
    self._updatingGUIFromParameterNode = False

  def updateParameterNodeFromGUI(self, caller=None, event=None):
    """
    This method is called when the user makes any change in the GUI.
    The changes are saved into the parameter node (so that they are restored when the scene is saved and loaded).
    """
    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    wasModified = self._parameterNode.StartModify()  # Modify all properties in a single batch

    self._parameterNode.SetNodeReferenceID("InputVolume", self.inputSelector.currentNodeID)

    self._parameterNode.EndModify(wasModified)

#
# ScriptedLoadableModuleTemplateLogic
#

class ScriptedLoadableModuleTemplateLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self):
    """
    Called when the logic class is instantiated. Can be used for initializing member variables.
    """
    ScriptedLoadableModuleLogic.__init__(self)





</code></pre>

---

## Post #23 by @mikebind (2022-01-26 01:28 UTC)

<p>The basic problem is that there is nothing which triggers an update of the volume node associated with  the volume threshold widget when the input volume is changed.  There are many possible ways to address this. Maybe the simplest is to do the following</p>
<pre><code class="lang-auto"># in your module widget's setup() function:
# Change the inputSelector connection callback to a new function
self.inputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onInputVolumeSelectorChange)
</code></pre>
<p>And then define that callback</p>
<pre><code class="lang-auto"># Add this function under the ScriptedLoadableModuleTemplateWidget class, the
# at the same indent level as setup(), updateParameterNodeFromGUI(), etc. 
def onInputVolumeSelectorChange(self, newInputVolumeNode):
    # Update the parameter node (so that your selection would be saved and restored with the scene)
    self._parameterNode.SetNodeReferenceID("InputVolume", newInputVolumeNode.currentNodeID)
    # Update the threshold slider's volume to the new selection
    self.thresholdRangeSlider1.setMRMLVolumeNode(newInputVolumeNode)
</code></pre>
<p>I haven’t had a chance to test this yet, but might be able to later.</p>

---

## Post #25 by @WilliamDaniel (2022-01-26 02:42 UTC)

<p>Dear Mike <a class="mention" href="/u/mikebind">@mikebind</a>,<br>
Thank you so much for your kind and fast reply!<br>
I’ve tried the code you just provided.<br>
However, some error logs pop up in the console：</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "E:/MySlicerExtensions/ScriptedLoadableExtensionTemplate/ScriptedLoadableModuleTemplate/ScriptedLoadableModuleTemplate.py", line 215, in onInputVolumeSelectorChange
    self._parameterNode.SetNodeReferenceID("InputVolume", newInputVolumeNode.currentNodeID)
AttributeError: 'NoneType' object has no attribute 'currentNodeID'
Traceback (most recent call last):
  File "E:/MySlicerExtensions/ScriptedLoadableExtensionTemplate/ScriptedLoadableModuleTemplate/ScriptedLoadableModuleTemplate.py", line 215, in onInputVolumeSelectorChange
    self._parameterNode.SetNodeReferenceID("InputVolume", newInputVolumeNode.currentNodeID)
AttributeError: 'MRMLCore.vtkMRMLScalarVolumeNode' object has no attribute 'currentNodeID'
</code></pre>
<p>In fact, this bug has been bothering me for several days, I have been collecting a lot of materials to learn to solve it, but it still doesn’t work…</p>
<p>If possible, could you please make some changes based on my code to fix this bug? Or could you please just to create a module that only contains this slider using the ‘extension wizard’？<br>
Your guidance is really like sunshine to me, thank you so much!!!</p>

---

## Post #26 by @CharlesChen (2022-01-26 19:47 UTC)

<p>Hello Mike <a class="mention" href="/u/mikebind">@mikebind</a> ,</p>
<p>Based on the error logs Daniel posted, does it mean that the ‘newInputVolumeNode’ is empty? How to make it store the new volume node?</p>
<p>Thank you so much!</p>

---

## Post #27 by @mikebind (2022-01-26 20:54 UTC)

<p>On testing, there are several problems.  I’ll try to get a version working later today if I get a chance.</p>

---

## Post #28 by @WilliamDaniel (2022-01-26 20:57 UTC)

<p>Hello Mike,<br>
Thank you very much! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #29 by @mikebind (2022-01-27 01:01 UTC)

<p>OK, this was harder than I expected <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:">  The following pretty much works…</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mikebind/f7cdd49f4dc5279d6c8fadf1c2d3b9b5">
  <header class="source">

      <a href="https://gist.github.com/mikebind/f7cdd49f4dc5279d6c8fadf1c2d3b9b5" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mikebind/f7cdd49f4dc5279d6c8fadf1c2d3b9b5" target="_blank" rel="noopener">https://gist.github.com/mikebind/f7cdd49f4dc5279d6c8fadf1c2d3b9b5</a></h4>

  <h5>TestDebug1.py</h5>
  <pre><code class="Python">import logging
import os
import unittest
import vtk, qt, ctk, slicer
import SegmentStatistics
from slicer.ScriptedLoadableModule import *
from slicer.util import TESTING_DATA_URL
from slicer.util import VTKObservationMixin

</code></pre>
    This file has been truncated. <a href="https://gist.github.com/mikebind/f7cdd49f4dc5279d6c8fadf1c2d3b9b5" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The remaining problem is that the slider seems to continue to affect the threshold values for input volumes which have been used before but switched away from.  I think this is a bug related to a Qt signal/slot issue, where a disconnect needs to happen in addition to adding a new connection when the <code>setMRMLVolumeNode()</code> function is used, but I’m not totally sure. I have to put this down at the moment, but hopefully it’s helpful.</p>

---

## Post #30 by @WilliamDaniel (2022-01-27 02:16 UTC)

<p>Dear Mike <a class="mention" href="/u/mikebind">@mikebind</a>,</p>
<p>Thank you so much for your hard work!<br>
I’ve test the scirpt you provided, but just as you mentioned, the remaining bug here is that the slider continue to affect the volume switched away from.<br>
Since I’m a beginner, I also realize that although this effect looks simple, it is difficult to implement… I have referenced the ‘updateGUIFromParameterNode’ method and ‘updateParameterNodeFromGUI’ method in <a href="https://github.com/Slicer/Slicer/blob/19d2cbe4cfb5cd3d651f7cdfee1958d1f159d941/Utilities/Templates/Modules/Scripted/TemplateKey.py" rel="noopener nofollow ugc">TemplateKey.py</a> and tried to make GUI elements like the slider update synchronously when the parameter node changes. But it still doesn’t work…<br>
If you can fix it in next few days that will be very great.<br>
Thank you very much!<br>
Dear <a class="mention" href="/u/lassoan">@lassoan</a>, or do you have any specific suggestions to address this based on the script <a href="https://gist.github.com/mikebind/f7cdd49f4dc5279d6c8fadf1c2d3b9b5" rel="noopener nofollow ugc">TestDebug1.py</a> <a class="mention" href="/u/mikebind">@mikebind</a> just provided?<br>
Thanks again! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #31 by @lassoan (2022-01-27 02:59 UTC)

<p>What you implemented should work, you just need to make sure that when you switch nodes you also switch which display nodes you modify.</p>
<p>By the way, I have never come across a use case when synchronization of the window/level between slice display and volume rendering was useful. The two visualization modes are just too different. Can you describe what is your overall goal?</p>
<p>If you just want to change the volume rendering settings then I would recommend to set the transfer function points directly. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-a-custom-volume-rendering-color-opacity-transfer-function">code snippet in the script repository</a> or a <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/521617989f08773d768e7c07ffcdaa795e245e62/LungCTAnalyzer/LungCTAnalyzer.py#L535-L561">complete example in LungCTAnalyzer module</a>.</p>

---

## Post #32 by @WilliamDaniel (2022-01-27 04:07 UTC)

<p>Hello Lassoan,</p>
<p>My goal is to implement the same ‘threshold’ slider as in the ‘Volumes’ module to control the threshold of the volume rendering image synchronously through a slider. I’m trying to extract this feature and transfer it to a python scripted module(This is one of step of the workflow of my module, next will be volume calculation etc.).</p>
<p>Currently, under <a class="mention" href="/u/mikebind">@mikebind</a> 's guidance, I can use the slider to modify the threshold of the volume rendering synchronously:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52145a165527196ddfdb64cdb13d758578b202f9.png" data-download-href="/uploads/short-url/bI6KTkfI1TgvFSJegI8051PuYjf.png?dl=1" title="picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52145a165527196ddfdb64cdb13d758578b202f9_2_517x158.png" alt="picture1" data-base62-sha1="bI6KTkfI1TgvFSJegI8051PuYjf" width="517" height="158" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52145a165527196ddfdb64cdb13d758578b202f9_2_517x158.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52145a165527196ddfdb64cdb13d758578b202f9_2_775x237.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52145a165527196ddfdb64cdb13d758578b202f9_2_1034x316.png 2x" data-dominant-color="C5C6D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture1</span><span class="informations">1316×403 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, when I switch the input volume to a new one(after I load one more volume as input here), the slider doesn’t work anymore, it only works on the first individual input volume’s volume rendering.</p>
<blockquote>
<p>you just need to make sure that when you switch nodes you also switch which display nodes you modify.</p>
</blockquote>
<blockquote>
<p>The basic problem is that there is nothing which triggers an update of the volume node associated with the volume threshold widget. when the input volume is changed.</p>
</blockquote>
<p>What you and Mike mentioned seems to be the reason. But I’m still confused how to do it.</p>
<p>Therefore, I hope to get more help from both of you. Or could you please give me some specific guidance based on the code Mike provided <a href="https://gist.github.com/mikebind/f7cdd49f4dc5279d6c8fadf1c2d3b9b5" rel="noopener nofollow ugc">TestDebug1</a>? Because what I need to modify is the volume rendering, here is the key function to do the modification:</p>
<pre><code class="lang-auto">  def updateThresholdOnVolume(self, volNode, lower, upper):
    displayNode = volNode.GetDisplayNode()
    displayNode.SetThreshold(lower, upper)
    displayNode.ApplyThresholdOn()
</code></pre>
<p>I hope that through my description, you can further understand my purpose.<br>
Thank you so much!</p>

---

## Post #33 by @lassoan (2022-01-27 05:23 UTC)

<p>I would recommend what I described above - do not try to shift the existing points of the transfer functions but explicitly set the transfer functions that you want.</p>
<p>Install the LungCTAnalysis extension and try how volume rendering works in the Lung CT Analysis module (how the slider moves the transfer functions).</p>
<p>Another simple example is Pedicle Screw Simulator extension (it just sets a fixed transfer function):</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/PedicleScrewSimulator/blob/7bf04fc00695115ac64742e692849a15e430f9dc/PedicleScrewSimulator/PedicleScrewSimulatorWizard/DefineROIStep.py#L347-L357">
  <header class="source">

      <a href="https://github.com/lassoan/PedicleScrewSimulator/blob/7bf04fc00695115ac64742e692849a15e430f9dc/PedicleScrewSimulator/PedicleScrewSimulatorWizard/DefineROIStep.py#L347-L357" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/PedicleScrewSimulator/blob/7bf04fc00695115ac64742e692849a15e430f9dc/PedicleScrewSimulator/PedicleScrewSimulatorWizard/DefineROIStep.py#L347-L357" target="_blank" rel="noopener">lassoan/PedicleScrewSimulator/blob/7bf04fc00695115ac64742e692849a15e430f9dc/PedicleScrewSimulator/PedicleScrewSimulatorWizard/DefineROIStep.py#L347-L357</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="347" style="counter-reset: li-counter 346 ;">
            <li>slicer.modules.volumerendering.logic().CopyDisplayToVolumeRenderingDisplayNode(self.__vrDisplayNode)</li>
            <li>
            </li>
<li>#update opacity and color map</li>
            <li>self.__vrOpacityMap = self.__vrDisplayNode.GetVolumePropertyNode().GetVolumeProperty().GetScalarOpacity()</li>
            <li>self.__vrColorMap = self.__vrDisplayNode.GetVolumePropertyNode().GetVolumeProperty().GetRGBTransferFunction()</li>
            <li>
            </li>
<li># setup color transfer function once</li>
            <li># two points at 0 and 500 force all voxels to be same color (any two points will work)</li>
            <li>self.__vrColorMap.RemoveAllPoints()</li>
            <li>self.__vrColorMap.AddRGBPoint(0, 0.95,0.84,0.57)</li>
            <li>self.__vrColorMap.AddRGBPoint(500, 0.95,0.84,0.57)</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It is just so much simpler to set the transfer functions than reimplementing the shift feature. Reimplementation is needed because the transfer function shift feature is inside a widget (qSlicerVolumeRenderingPresetComboBox.cxx) instead of a reusable logic class.</p>

---

## Post #34 by @mikebind (2022-01-27 17:11 UTC)

<aside class="quote no-group" data-username="WilliamDaniel" data-post="32" data-topic="20891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/williamdaniel/48/13425_2.png" class="avatar"> WilliamDaniel:</div>
<blockquote>
<p>This is one of step of the workflow of my module, next will be volume calculation etc.</p>
</blockquote>
</aside>
<p>Looking ahead, volume calculation is not possible from a volume rendering. Volume rendering works by dynamically casting rays through an image volume from the perspective of the camera and displaying the result. To measure the volume of what is visible would require creating a segmentation and then measuring the segmentation.</p>
<aside class="quote no-group" data-username="WilliamDaniel" data-post="32" data-topic="20891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/williamdaniel/48/13425_2.png" class="avatar"> WilliamDaniel:</div>
<blockquote>
<p>However, when I switch the input volume to a new one(after I load one more volume as input here), the slider doesn’t work anymore, it only works on the first individual input volume’s volume rendering.</p>
</blockquote>
</aside>
<p>This problem is solved by the code in the gist above, which does switch the volume rendering display to the new volume.</p>
<aside class="quote no-group" data-username="WilliamDaniel" data-post="32" data-topic="20891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/williamdaniel/48/13425_2.png" class="avatar"> WilliamDaniel:</div>
<blockquote>
<p>The basic problem is that there is nothing which triggers an update of the volume node associated with the volume threshold widget. when the input volume is changed.</p>
</blockquote>
</aside>
<p>This is also addressed in the code in the gist.  This happens in the <code>onInputVolumeSelectorChange()</code> function, on line 111 of the gist.</p>
<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a> that it doesn’t seem very useful to have the visualization threshold in the slice view linked to the thresholds in the volume rendering, since the two views are quite different (it’s helpful to hide things in the rendering, but not usually helpful in the slice views). However, since that was what you had asked for, I was trying to help you see how to achieve that.</p>
<p>Andras, I think there may be a bug in the <code>setMRMLVolumeNode()</code> of the <code>qMRMLVolumeThresholdWidget</code>.  When a new volume is set, I think a link is maintained to the previous volume.  Possibly there is a missing disconnect of the signal and slot in Qt?  I’m not very good at debugging in C++, but if I can generate a minimal example I’ll post a bug report in the Slicer github issues page (that’s the correct place, right?).</p>
<p><a class="mention" href="/u/williamdaniel">@WilliamDaniel</a> , I think <a class="mention" href="/u/lassoan">@lassoan</a> 's suggestion to set the transfer function directly makes a lot of sense and would sidestep this bug.  Also, definitely consider the following steps of your workflow.  Do you even need volume rendering?  Or do you need to segment? I would recommend that you try out your complete workflow interactively (just figuring out the sequence of steps in the Slicer GUI) and make sure you can accomplish all the steps you want using the approach you are considering.</p>

---

## Post #36 by @WilliamDaniel (2022-01-27 18:11 UTC)

<p>Hello Mike,<br>
If possible, may I have a video chat with you for about 10-15 minutes to explain my workflow further to you? Any time when you are free is ok. Because I’m still confused about this point you mentioned:</p>
<blockquote>
<p>it doesn’t seem very useful to have the visualization threshold in the slice view linked to the thresholds in the volume rendering, since the two views are quite different.<br>
Just give me a chance to describe my workflow more clear.</p>
</blockquote>
<p>Here is my email: <a href="mailto:realdaniel021@gmail.com">realdaniel021@gmail.com</a><br>
Thank you so much for your kind help! <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #37 by @mikebind (2022-01-27 18:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> disregard my possible bug report here.  It was just a failure to update the parameter node appropriately. The threshold widget was controlling one volume’s display node, and the module code was controlling another (getting an outdated reference from the parameter node).</p>
<p><a class="mention" href="/u/williamdaniel">@WilliamDaniel</a>, I’ll follow up via email.</p>
<p>In the meantime, I’ve updated the gist which will now work without affecting the wrong image (the same gist link above will show the revised code).</p>

---

## Post #38 by @WilliamDaniel (2022-01-27 19:07 UTC)

<p>Hello Mike,</p>
<p>Thank you very much, now the gist can run successfully!<br>
But I found that there is still a small bug here, and that is the ‘crop’ function in ‘Volume rendering’ module seems to not work after I load this scripted module in slicer.</p>
<p>As you can see, I have the checked the checkbox of ‘Enable’ and ‘Display ROI’, but after I adjust the bounding box, the volume rendering image doesn’t change…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/603e3085b0112a6d56ce1e4656c859a4fbbd565d.jpeg" data-download-href="/uploads/short-url/dJp4OrhkgFx0beay1wXB9ljd8Xb.jpeg?dl=1" title="picture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/603e3085b0112a6d56ce1e4656c859a4fbbd565d_2_345x188.jpeg" alt="picture3" data-base62-sha1="dJp4OrhkgFx0beay1wXB9ljd8Xb" width="345" height="188" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/603e3085b0112a6d56ce1e4656c859a4fbbd565d_2_345x188.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/603e3085b0112a6d56ce1e4656c859a4fbbd565d_2_517x282.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/603e3085b0112a6d56ce1e4656c859a4fbbd565d_2_690x376.jpeg 2x" data-dominant-color="A8A9C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture3</span><span class="informations">1471×803 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Meanwhile, I’ll also continue to learn from the script you provided, it’s really helpful!<br>
Thank you!</p>

---

## Post #39 by @mikebind (2022-01-27 19:31 UTC)

<p>Try that without using the custom module.  I think the experimental MultiVolume renderer may not have the ROI crop functionality.  ROI cropping works for me in using GPU or CPU ray casting renderers.</p>

---

## Post #40 by @WilliamDaniel (2022-01-27 19:56 UTC)

<p>Hello Mike,<br>
All right, got you!<br>
The last thing is that whenever I close Slicer, there are always an error popup here:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcb4991bde4ccb08b4922096e8950cbf08795475.png" alt="FIGURE" data-base62-sha1="qVmH1VqJNUlPpRp3IajLgxwmXwp" width="300" height="204"><br>
I tried adding displayNode.UnRegister(slicer.mrmlScene) but it doesn’t work.<br>
Do you know how to avoid these errors?<br>
Thank you so much!</p>

---

## Post #41 by @mikebind (2022-01-27 21:19 UTC)

<p>You were on the right track.  This was caused by the use of <code>slicer.mrmlScene.GetNodesByClass()</code>.  See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement">here</a> for an explanation.</p>
<p>I updated the gist with the calls to properly unregister the extra references, so I don’t get the leak errors any more on closing Slicer.  When you’re testing, make sure you close and reopen Slicer after updating the code to see whether the fix works for you.</p>

---

## Post #42 by @WilliamDaniel (2022-01-27 21:54 UTC)

<p>Hello Mike,</p>
<p>Thank you very much for your guidance, now it totally working! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #43 by @dalv.silvermann (2022-08-02 09:56 UTC)

<p>Hi to all Discoursers here! I’v got a lot knowledge from this resource. Thank you very much ya all!</p>
<p>Plese, help me to find:</p>
<ol>
<li>How I can set the checkbox called “Synchronize with volumes module” in module called “Volume Rendering” from python code? How I can set it for a chosen volume (set only for special volume name with slicer.mrmlScene.GetFirstNodeByName())</li>
<li>How I can set it by default always “On” at start of the Slicer?</li>
</ol>
<p>Thank ya all!</p>

---

## Post #44 by @pieper (2022-08-02 15:07 UTC)

<p>The steps described here should work for you:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>

---

## Post #45 by @dalv.silvermann (2022-08-02 21:35 UTC)

<p>Thank you very much! Your advice helped me to find the way, it was definitely what I need to know in regard to all GUI elements in the Slicer. This code is work for me:</p>
<pre><code class="lang-auto">volumeRenderingWidgetRep.setMRMLVolumeNode(slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode11'))
volumeRenderingWidgetRep = slicer.modules.volumerendering.widgetRepresentation()
volumeRenderingWidgetRep.mrmlDisplayNode().GetFollowVolumeDisplayNode()
followGet = volumeRenderingWidgetRep.mrmlDisplayNode().GetFollowVolumeDisplayNode()
followSet = volumeRenderingWidgetRep.mrmlDisplayNode().SetFollowVolumeDisplayNode(1)
volumeName = "635166: AXIAL cropped_9"
volNode = getNode(volumeName)
dispNode = volNode.GetDisplayNode()
lowerThreshValue = 267
upperThreshValue = 32767
dispNode.SetThreshold(lowerThreshValue, upperThreshValue)
volNode.GetDisplayNode().ApplyThresholdOn()
</code></pre>
<p>Need to note, that <code>'vtkMRMLScalarVolumeNode11'</code> and <code>"635166: AXIAL cropped_9"</code> is the same node :0)</p>

---
