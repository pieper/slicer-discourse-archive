# Display different images and models in different views

**Topic ID**: 11442
**Date**: 2020-05-07
**URL**: https://discourse.slicer.org/t/display-different-images-and-models-in-different-views/11442

---

## Post #1 by @kristjanq (2020-05-07 10:03 UTC)

<p>Dear Slicer community,<br>
I am trying to build a training phantom for Interventional Cardiologists making use of tracked Ultrasound using PlusToolkit from <code>@lassoan et al</code>, as part of my master thesis. To give a big picture: The idea is to mimic a human torso, including a submerged 3D printed heart. The heart will be registered using PlusToolkit. The final goal is to provide a sample training phantom for students using tracked ICE catheters.</p>
<p>As a validation trial, I want to show to the students two windows: 1- containing only the US image, and 2- containing the US image plane (not necessarily containing US image data) oriented into the 3D model of the heart.</p>
<p>The idea is to be able to switch ON and OFF the second option while being able to show both windows on the same screen.<br>
Is it possible to achieve such a thing using Slicer?</p>

---

## Post #2 by @cpinter (2020-05-07 10:19 UTC)

<p>Just to be on the same page, when we Slicer developers talk about multi-volume rendering, we mean showing more than one volume in the same 3D view. Based on your description it seems that you want to show one volume in each view, but you want to show a different volume in the views. Maybe I misunderstand, in that case please clarify.</p>
<p>To show a different volume in the views, you can have different display nodes for each view, by assigning them to the corresponding view nodes. See these functions:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLDisplayNode.h#L505-L548" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLDisplayNode.h#L505-L548" target="_blank">Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLDisplayNode.h#L505-L548</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="505" style="counter-reset: li-counter 504 ;">
<li>/// Add View Node ID for the view to display this node in.</li>
<li>/// \sa ViewNodeIDs, RemoveViewNodeID(), RemoveAllViewNodeIDs()</li>
<li>void AddViewNodeID(const char* viewNodeID);</li>
<li>/// Remove View Node ID for the view to display this node in.</li>
<li>/// Note that if no view node IDs are specified then the displayable</li>
<li>/// node will be shown in every views. Therefore, to hide a displayable</li>
<li>/// node from a single view, it is not necessary to call RemoveViewNodeID</li>
<li>/// (unless it had been explicitly added before) but all the other</li>
<li>/// view node IDs must be added instead.</li>
<li>/// \sa ViewNodeIDs, AddViewNodeID(), RemoveAllViewNodeIDs()</li>
<li>void RemoveViewNodeID(char* viewNodeID);</li>
<li>/// Remove All View Node IDs for the views to display this node in.</li>
<li>/// \sa ViewNodeIDs, AddViewNodeID(), RemoveViewNodeID()</li>
<li>void RemoveAllViewNodeIDs();</li>
<li>/// Get number of View Node ID's for the view to display this node in.</li>
<li>/// If 0, display in all views</li>
<li>/// \sa ViewNodeIDs, GetViewNodeIDs(), AddViewNodeID()</li>
<li>inline int GetNumberOfViewNodeIDs()const;</li>
<li>/// Get View Node ID's for the view to display this node in.</li>
<li>/// If nullptr, display in all views</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLDisplayNode.h#L505-L548" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @kristjanq (2020-05-07 10:43 UTC)

<p>Thank you for your answer!</p>
<p>To be more concise: There is only one volume to render, 3D heart model, which could be a STL file. The ICE (Intra-cardiac echocardiography) catheter is tracked. The US image-plane should be visualized within heart volume.</p>
<p>Note that the catheter will be spatially calibrated and the heart model with be registered to a tracking system beforehand.</p>
<p>So my idea was: to be able to switch ON and OFF the US plane within the heart volume?!</p>

---

## Post #4 by @cpinter (2020-05-07 12:17 UTC)

<p>We need to clarify a few more things. An STL file is a model, and image data is called a volume in the Slicer nomenclature. Please consult the figure on the bottom of this page to get familiar with the data types:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>
<p>Once you know what Slicer objects you have, please describe again the views you want. A figure or mockup is welcome.</p>
<aside class="quote no-group" data-username="kristjanq" data-post="3" data-topic="11442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kristjanq/48/6534_2.png" class="avatar"> kristjanq:</div>
<blockquote>
<p>to be able to switch ON and OFF the US plane within the heart volume?</p>
</blockquote>
</aside>
<p>The answer to this question is yes. I’m not sure if you can have a live image slice in a 3D view without having a slice view as well, so you may need to have a slice view in addition to your 3D views. The layout can be set in any way you want. From the GUI, the slice an be shown/hidden by clicking an eye button on the slice view’s controller widget (accessible by moving mouse to top left corner of view).</p>

---

## Post #5 by @lassoan (2020-05-07 13:43 UTC)

<p>Yes, the title is misleading, as by volumes we mean 3D voxel array, while you work with 2D voxel array and surface meshes. I’ll update the title accordingly.</p>

---

## Post #6 by @kristjanq (2020-05-07 14:08 UTC)

<p>Thank you for the title update. Unfortunately, at the moment I can not express myself more clearly. I am a beginner in the matter! I hope I could somehow explain myself better with the  below diagram!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83a1ba9b5da86dab75b68adb593a64f5757564a1.jpeg" data-download-href="/uploads/short-url/iMt3b56QYSJP79quG9WJykj9zfb.jpeg?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83a1ba9b5da86dab75b68adb593a64f5757564a1_2_690x388.jpeg" alt="slicer" data-base62-sha1="iMt3b56QYSJP79quG9WJykj9zfb" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83a1ba9b5da86dab75b68adb593a64f5757564a1_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83a1ba9b5da86dab75b68adb593a64f5757564a1_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83a1ba9b5da86dab75b68adb593a64f5757564a1.jpeg 2x" data-dominant-color="E8E8E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">1280×720 50.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2020-05-07 22:14 UTC)

<p>Thank you, the image helps a lot. To get visualization like this, you need to do is load a 3D model (STL file), and set up real-time tracked ultrasound visualization as explained in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> (for example, U-32).</p>
<p>To create a layout where a slice view and a 3D view are shown side-by-side, use this example script:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout</a><br>
Probably you just need to change <code>type="vertical"</code> to <code>type="horizontal"</code> for a horizontal layout.</p>

---
