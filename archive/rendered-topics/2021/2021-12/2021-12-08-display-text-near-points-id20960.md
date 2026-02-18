# Display text near points

**Topic ID**: 20960
**Date**: 2021-12-08
**URL**: https://discourse.slicer.org/t/display-text-near-points/20960

---

## Post #1 by @keri (2021-12-08 02:49 UTC)

<p>Hi,</p>
<p>I’m looking for a way to display text at each point from point cloud. In the best scenario the text should have the constant size regardless of the distance between camera position and point and the text should be faced to the camera. Something similar to <a href="https://kitware.github.io/vtk-examples/site/Cxx/Visualization/LabeledDataMapper" rel="noopener nofollow ugc">LabeledDataMapper vtk example</a></p>
<p>Is <code>vtkLabeledDataMapper</code> the right choice? I guess in that case I would need to implement custom displayable manager right?</p>

---

## Post #2 by @keri (2021-12-14 02:34 UTC)

<p>Solved that with <code>vtkCaptionActor2D</code>. I’ve found it <a href="https://discourse.vtk.org/t/how-to-fix-the-font-actor-size-that-is-the-font-size-does-not-change-when-the-camera-distance-is-changed/2965" rel="noopener nofollow ugc">by the link</a>.<br>
<code>vtkCaptionActor2D</code> neither affected by zoom nor by inequal aspect ratio. Thus it is pretty good for me.</p>
<p>Adding observers to caption actor allows to react on events like <code>TransformModifiedEvent</code> (when the node is transformed/moved for example), or <code>DisplayModifiedEvent</code> (when visibility of node is changed).</p>
<p>This is implemented in displayable manager thus <code>::OnMRMLSceneNodeAdded()</code> and <code>::OnMRMLSceneNodeRemoved()</code> maybe used to create/delete caption actor when necessary.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fc6712fa58b9fed05d659f22dddd4b59266452c.png" alt="image" data-base62-sha1="6ODBhRqpHaMWQtOM1t3Pb0MfP6A" width="385" height="433"></p>
<p>Also there is a <code>vtkMRMLNode::IDChangedEvent</code> but no <code>NameChanged</code> am I right? Or there is something different that may be used when the node’s name is changed?</p>

---

## Post #3 by @pieper (2021-12-14 18:23 UTC)

<aside class="quote no-group" data-username="keri" data-post="2" data-topic="20960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>Also there is a <code>vtkMRMLNode::IDChangedEvent</code> but no <code>NameChanged</code> am I right? Or there is something different that may be used when the node’s name is changed?</p>
</blockquote>
</aside>
<p>When there’s no fine-grained event to observe you can typically just observe <code>ModifiedEvent</code>.  If you end up getting too many events from that you could propose to add a more specialized event.</p>

---
