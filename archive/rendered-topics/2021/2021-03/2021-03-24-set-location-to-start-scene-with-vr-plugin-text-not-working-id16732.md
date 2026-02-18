# Set location to start scene with VR plugin. Text not working in VR pluging

**Topic ID**: 16732
**Date**: 2021-03-24
**URL**: https://discourse.slicer.org/t/set-location-to-start-scene-with-vr-plugin-text-not-working-in-vr-pluging/16732

---

## Post #1 by @smallvalthoss (2021-03-24 01:26 UTC)

<p>Hello,</p>
<p>Firstly, I’m wondering if it is possible to set a starting location for the VR camera. I was hoping for something akin to unity’s camera object, where you can move it in the window. It then always starts from that location. If it were possible to move around with the headset, then it saves that location, that would work.</p>
<p>Second, text seems to not work in world space. The annotations seem to all appear clumped on the screen.</p>
<p>Any help would be appreciated <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:">, Thanks!</p>

---

## Post #2 by @cpinter (2021-03-24 13:32 UTC)

<blockquote>
<p>set a starting location for the VR camera</p>
</blockquote>
<p>This function sets the VR view to match that of an existing 3D view in Slicer:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/Widgets/qMRMLVirtualRealityView.cxx#L743">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/Widgets/qMRMLVirtualRealityView.cxx#L743" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/Widgets/qMRMLVirtualRealityView.cxx#L743" target="_blank" rel="noopener">KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/Widgets/qMRMLVirtualRealityView.cxx#L743</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="733" style="counter-reset: li-counter 732 ;">
          <li>  return d-&gt;MRMLVirtualRealityViewNode;</li>
          <li>}</li>
          <li></li>
          <li>//------------------------------------------------------------------------------</li>
          <li>void qMRMLVirtualRealityView::getDisplayableManagers(vtkCollection* displayableManagers)</li>
          <li>{</li>
          <li>  Q_D(qMRMLVirtualRealityView);</li>
          <li></li>
          <li>  if (!displayableManagers || !d-&gt;DisplayableManagerGroup)</li>
          <li>  {</li>
          <li class="selected">    return;</li>
          <li>  }</li>
          <li>  int num = d-&gt;DisplayableManagerGroup-&gt;GetDisplayableManagerCount();</li>
          <li>  for (int n = 0; n &lt; num; n++)</li>
          <li>  {</li>
          <li>    displayableManagers-&gt;AddItem(d-&gt;DisplayableManagerGroup-&gt;GetNthDisplayableManager(n));</li>
          <li>  }</li>
          <li>}</li>
          <li></li>
          <li>//------------------------------------------------------------------------------</li>
          <li>bool qMRMLVirtualRealityView::isHardwareConnected()const</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="smallvalthoss" data-post="1" data-topic="16732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/848f3c/48.png" class="avatar"> smallvalthoss:</div>
<blockquote>
<p>text seems to not work in world space</p>
</blockquote>
</aside>
<p>2D actors cannot be displayed well in stereoscopic vision. You need to use 3D text.</p>

---

## Post #3 by @lassoan (2021-03-24 15:10 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="2" data-topic="16732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<aside class="quote no-group" data-username="smallvalthoss" data-post="1" data-topic="16732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/848f3c/48.png" class="avatar"> smallvalthoss:</div>
<blockquote>
<p>text seems to not work in world space</p>
</blockquote>
</aside>
<p>2D actors cannot be displayed well in stereoscopic vision. You need to use 3D text.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/smallvalthoss">@smallvalthoss</a> it would be great if you could explore this further, maybe with getting advice from the <a href="https://discourse.vtk.org/">VTK forum</a>. It may be possible to render all the 2D actors at some fixed plane at a convenient reading distance. If needed, we could replace all 2D actors by 3D counterparts at application level, but it would add a lot of complexity.</p>

---

## Post #4 by @smallvalthoss (2021-03-26 17:26 UTC)

<p>Thank you for the reply! I’m new to 3D slicer as well as creating/modifying extensions, so I appreciate the patience.</p>
<p>Do you know of a way to have it as a 3D object in the scene? So I could position it to start at the same spot every time?</p>
<p>I noticed in the code it sets the magnification to the default of 10x. Would I go in to the code and change that hard-coded bit (line 792) to get the value from the scene window?</p>

---

## Post #5 by @smallvalthoss (2021-03-26 18:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I will take a look! Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @smallvalthoss (2021-04-16 23:25 UTC)

<p>Where in slicer is it possible to create 3D text?</p>

---

## Post #7 by @lassoan (2021-04-18 19:28 UTC)

<p>There are many ways to add 3D text, at various levels. The simplest solution is probably to create a custom markups type, where you change the 3D representation of point labels to use a 3D text actor (any of the classes that you see <a href="https://vtk.org/doc/nightly/html/classvtkProp3D.html">here</a>, for example vtkTextActor3D or vtkFlagpoleLabel). You can find a complete example of a custom markups node+widget+representation <a href="https://github.com/Slicer/Slicer/tree/master/Utilities/Templates/Modules/LoadableCustomMarkups">here</a>.</p>

---

## Post #8 by @smallvalthoss (2021-04-22 20:53 UTC)

<p>Thank you Andras, I will play around with this</p>

---

## Post #9 by @smallvalthoss (2021-04-22 20:53 UTC)

<p>I asked twice on the forum and no one has responded. But still thinking about it</p>

---

## Post #10 by @smallvalthoss (2021-04-22 20:55 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="2" data-topic="16732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<blockquote>
<p>set a starting location for the VR camera</p>
</blockquote>
<p>This function sets the VR view to match that of an existing 3D view in Slicer:</p>
</blockquote>
</aside>
<p>This function does set the same location, but the magnification is always set to 10x. Is there a way of making it the same magnification? Also, wondering about saving the start location when you save the mrml scene node?</p>

---
