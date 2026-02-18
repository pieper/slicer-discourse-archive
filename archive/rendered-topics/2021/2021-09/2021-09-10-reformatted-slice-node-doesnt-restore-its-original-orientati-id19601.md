# Reformatted slice node doesn't restore its original orientation

**Topic ID**: 19601
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/reformatted-slice-node-doesnt-restore-its-original-orientation/19601

---

## Post #1 by @keri (2021-09-10 01:40 UTC)

<p>Hi,</p>
<p>Slice node <code>vtkMRMLNode</code> has a method <code>GetOrientation()</code> wich returns string value: Axial, Coronal, Sagittal or Reformat.<br>
Also there is a button on the view that probably <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html?highlight=background%20layer#slice-view" rel="noopener nofollow ugc">restore the default state (on the picture)</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/924de4cbccb16bfcb18837c0457a6ee9ef3d2152.png" alt="image" data-base62-sha1="kSgB1NCIzdcogauws3tvozVq3qq" width="189" height="107"><br>
I tried to reformat the slice, restore it (by pressing on that button) and check the orientation (I expected that it should have been changed back to Axial):</p>
<pre data-code-wrap="python"><code class="lang-python">layoutManager = slicer.app.layoutManager()
view = layoutManager.sliceWidget('Red').sliceView()
sliceNode = view.mrmlSliceNode()
sliceNode.GetOrientation() # gives `Reformat`
</code></pre>
<p>but it returns <code>Reformat</code> orientation.</p>
<p>Is it expected behaviour?</p>

---

## Post #2 by @jamesobutler (2021-09-10 03:51 UTC)

<p>The button immediately to the left of the slice offset slider is the maximize/restore for the slice layout. This is a new button recently added. See the following for details on that feature</p>
<aside class="quote quote-modified" data-post="1" data-topic="19581">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-feature-maximize-view/19581">New feature: maximize view</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We added a new feature that allows quickly maximize a view (use the space of the entire view layout) without switching between layouts. 
The feature can be activated using 3 methods: 

double-click on a view to maximize/restore
click the maximize/restore button in the view control bar (at the top of each view)
right-click on the view and choose maximize/restore

 
    
   
When the view is restored then the original view layout is restored. The feature is available in latest Slicer Preview Relea…
  </blockquote>
</aside>

<p>There isn’t a button for resetting default orientation. You can change orientation in the slice view pop up widget that displays when hovering over the slice offset slider area. There is a combobox for selecting orientation.</p>
<p>You can also set orientation programmatically like so:</p>
<pre data-code-wrap="python"><code class="lang-python">orientation = slicer.app.layoutManager().sliceWidget("Red").sliceLogic().GetSliceNode().GetDefaultOrientation()
slicer.app.layoutManager().sliceWidget("Red").setSliceOrientation(orientation)
</code></pre>

---

## Post #3 by @lassoan (2021-09-10 04:32 UTC)

<p>If you use a recent Slicer Preview Release then you can enable “Reset view orientation on show” option (by right-clicking on the eye icon in Data module) and then hide and show the volume (by clicking on the eye icon).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4745550f26f52b4ffa7d97d8e6e325493355be41.png" data-download-href="/uploads/short-url/aaurx4RXKCJ3clHGnMhcDD8K7hn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4745550f26f52b4ffa7d97d8e6e325493355be41_2_690x495.png" alt="image" data-base62-sha1="aaurx4RXKCJ3clHGnMhcDD8K7hn" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4745550f26f52b4ffa7d97d8e6e325493355be41_2_690x495.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4745550f26f52b4ffa7d97d8e6e325493355be41_2_1035x742.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4745550f26f52b4ffa7d97d8e6e325493355be41.png 2x" data-dominant-color="C5C6BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1122×805 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @keri (2021-09-10 11:09 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="19601">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The button immediately to the left of the slice offset slider is the maximize/restore for the slice layout. This is a new button recently added.</p>
</blockquote>
</aside>
<p>I meant the button that is near to maximize button (in orange rectangle):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bde51ba80d78e32a6ed8b674dc96511466823c80.png" alt="image" data-base62-sha1="r5T6qhASanzXRn24OVECOM7KQSs" width="68" height="37"><br>
But still, as you said I can modify orientation in combobox, that is good.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> thank you for the help, I use SlicerCAT based on recent Slicer so I have tried your solution and it works.</p>

---
