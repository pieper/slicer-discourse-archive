# Hide a volume programmatically

**Topic ID**: 26654
**Date**: 2022-12-08
**URL**: https://discourse.slicer.org/t/hide-a-volume-programmatically/26654

---

## Post #1 by @rhodesdante (2022-12-08 20:14 UTC)

<p>I am writing a custom module in Python and I would like to:</p>
<ol>
<li>Replace the active volume in the slice viewer (similar to clicking on the “eye” icon of a different volume) with the next volume in the subject hierarchy</li>
<li>Shut the eye icon on the subject hierarchy of the volume I just turned off</li>
</ol>
<p>I was able to do the first bit with the following chunk of code, but I can’t seem to shut the eye in the subject hierarchy–both eyes stay on even though only one volume is present in the slice viewer. Is it possible to shut that eye icon programmatically? Thank you very much!</p>
<pre><code>#  self.shNode is a subjectHierarchy node
def viewNextVolume(self, reverse = False):
  # First, get all valid volume vtkIDs
  sceneID = self.shNode.GetSceneItemID()
  allChildren = []
  self.shNode.GetItemChildren(sceneID, allChildren)
  validChildren = [child for child in allChildren if self.shNode.GetItemDataNode(child).IsTypeOf("vtkMRMLScalarVolumeNode")]

  # Second, get the vtkID of the current volume
  layoutManager = slicer.app.layoutManager()
  redVolumeID=layoutManager.sliceWidget("Red").sliceLogic().GetSliceCompositeNode().GetBackgroundVolumeID()
  currentvtkID = self.shNode.GetItemByDataNode(slicer.mrmlScene.GetNodeByID(redVolumeID))

  # third, advance the slice viewer
  nextDex = (validChildren.index(currentvtkID) + 1* (-1)**reverse) % len(validChildren) 
  newNode = self.shNode.GetItemDataNode(validChildren[nextDex])
  for sliceViewName in layoutManager.sliceViewNames():
    compositeNode = layoutManager.sliceWidget(sliceViewName).sliceLogic().GetSliceCompositeNode()
    compositeNode.SetBackgroundVolumeID(newNode.GetID())
    layoutManager.sliceWidget(sliceViewName).fitSliceToBackground()

  # HOW TO SHUT OFF EYE OF PREVIOUS VOLUME?
</code></pre>

---

## Post #2 by @smrolfe (2022-12-08 22:23 UTC)

<p>For the MRHead example I can set the visibility in the subject hierarchy programmatically using:</p>
<pre><code class="lang-auto">volNode = getNode("MRHead")
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
volItem = shNode.GetItemByDataNode(volNode)
pluginHandler = slicer.qSlicerSubjectHierarchyPluginHandler().instance()
volPlugin = pluginHandler.getOwnerPluginForSubjectHierarchyItem(volItem)
volPlugin.setDisplayVisibility(volItem, 0)
</code></pre>

---

## Post #3 by @smrolfe (2022-12-08 22:26 UTC)

<p>I’m not sure why</p>
<pre><code class="lang-auto">volNode.GetDisplayNode().SetVisibility(0)
volNode.SetDisplayVisibility(0)
</code></pre>
<p>don’t work to hide the slice view of the volume, maybe someone else can weigh in? I also noticed if the volume is in a folder, hiding the folder does not hide the slice view of the volume.</p>

---

## Post #4 by @jamesobutler (2022-12-08 23:07 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="3" data-topic="26654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>I also noticed if the volume is in a folder, hiding the folder does not hide the slice view of the volume.</p>
</blockquote>
</aside>
<p>See the following and the insights liked from there:<br>
(ultimately it is due to turning the visibility on would only work for 2 volumes, since Slicer can’t show more than 2 volumes in a given slice view)</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6413">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6413" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6413" target="_blank" rel="noopener nofollow ugc">Folder visibility affects 3D rendering but not 2D</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-06-07" data-time="12:55:42" data-timezone="UTC">12:55PM - 07 Jun 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/fbordignon" target="_blank" rel="noopener nofollow ugc">
          <img alt="fbordignon" src="https://avatars.githubusercontent.com/u/4790289?v=4" class="onebox-avatar-inline" width="20" height="20">
          fbordignon
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As reported on https://discourse.slicer.org/t/folder-visibility-confusing/23753
<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">

The eye icon is both loved and hated by our users, but I believe there is a confusing behavior for the folder eye icon. When I close the folder’s eye and have both 2D and 3D renderings, only the 3D hides:

![image](https://user-images.githubusercontent.com/4790289/172384582-08113351-73e5-48a4-9e64-a5b77eabbc80.png)

![image](https://user-images.githubusercontent.com/4790289/172384604-57108b69-ab8d-4f87-af99-69d81c7be87b.png)


To confuse even more the users, the 2D slice is kept on the 3D view. I’ve personally spent 10 minutes fiddling with the volume rendering sliders only to discover that the folder eye was closed. I was seeing the 2D slice at the 3D view and at the slicewidgets but the 3D rendering was not showing, so I thought the visibility was fine.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4961#issuecomment-638710730">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4961#issuecomment-638710730" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4961#issuecomment-638710730" target="_blank" rel="noopener nofollow ugc">Controlling visibility of volume node children in subject hierarchy</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-06-03" data-time="18:38:40" data-timezone="UTC">06:38PM - 03 Jun 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/gregsharp" target="_blank" rel="noopener nofollow ugc">
          <img alt="gregsharp" src="https://avatars.githubusercontent.com/u/327896?v=4" class="onebox-avatar-inline" width="20" height="20">
          gregsharp
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The visibility toggle button (ie. the eyeball button) in the subject hierarchy c<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">an be used to show or hide the children of the hierarchy node.  However, visibility of children volume nodes is not affected in the 2D slice views.

## Steps to reproduce

See discourse post. 
https://discourse.slicer.org/t/hiding-patient-in-hierarchy/11850

## Expected behavior

Clicking the visibility button of a parent should allow user to control all children nodes in a uniform manner.

## Environment
- Slicer version: 4.11.0-2020-03-26 r28898 / f9eb7e9
- Operating system: Linux</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2022-12-09 06:00 UTC)

<p>You can show-hide volumes in slice views by using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.setSliceViewerLayers">slicer.util.setSliceViewerLayers()</a>.</p>
<p>You can hide volume rendering in 3D views like this (if you don’t want to use the subject hierarchy plugin based solution above):</p>
<pre><code class="lang-python">vrDisplayNode = slicer.modules.volumerendering.logic().GetFirstVolumeRenderingDisplayNode(volumeNode)
# hide volume rendering:
vrDisplayNode.SetVisibility(False)
# prevent showing volume rendering if eye icon is clicked in Subject Hierarchy:
vrDisplayNode.SetShowMode(slicer.vtkMRMLDisplayNode.ShowIgnore)
</code></pre>

---

## Post #6 by @rhodesdante (2022-12-12 17:51 UTC)

<p>slicer.util.setSliceViewerLayers() link worked very nicely for this purpose. Thanks!</p>

---

## Post #7 by @rohithck (2024-07-23 12:08 UTC)

<p>For a newly loaded volume, In the mentioned method</p>
<pre><code class="lang-auto">vrDisplayNode = slicer.modules.volumerendering.logic().GetFirstVolumeRenderingDisplayNode(volumeNode)
vrDisplayNode.SetVisibility(False)
</code></pre>
<p>it is only show or hide volume if I show volume in Volume Rendering plugin at first time. Otherwise getting error:<br>
<code>AttributeError: 'NoneType' object has no attribute 'SetVisibility'</code></p>

---

## Post #8 by @lassoan (2024-07-23 12:53 UTC)

<p>If the volume rendering display node (the data object that stores volume rendering settings) has not been created yet then you can create it by calling <code>CreateDefaultVolumeRenderingNodes</code>. There are several examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>.</p>

---

## Post #9 by @rohithck (2024-07-29 13:04 UTC)

<p>when I use <code>CreateDefaultVolumeRenderingNodes</code>, the volume property set to US-Fetal (Image 1). But if I show volume in Volume Rendering plugin at first time after loading the .mha file, it will automatically create a volume property with actual color of the image (Image 2). How can i solve this?</p>
<pre><code class="lang-auto">for file in mha_files:
    volume = slicer.util.loadVolume(file)
    vrDisplayNode = slicer.modules.volumerendering.logic().CreateDefaultVolumeRenderingNodes(volume)
    vrDisplayNode.SetVisibility(True)
</code></pre>
<p>Image 1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5390a01bd87bce587e49290098f1f5f5928082d.png" data-download-href="/uploads/short-url/uqfUe5mqFEhHNhwwrvpZLS1p01D.png?dl=1" title="Image 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5390a01bd87bce587e49290098f1f5f5928082d_2_338x500.png" alt="Image 1" data-base62-sha1="uqfUe5mqFEhHNhwwrvpZLS1p01D" width="338" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5390a01bd87bce587e49290098f1f5f5928082d_2_338x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5390a01bd87bce587e49290098f1f5f5928082d_2_507x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5390a01bd87bce587e49290098f1f5f5928082d.png 2x" data-dominant-color="E3DCD6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 1</span><span class="informations">535×790 52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image 2<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/727104f82801067346d9932cbbd988153b2c535a.png" data-download-href="/uploads/short-url/gkozCM9AhMMEPO9EEL1sra4euiS.png?dl=1" title="Image 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/727104f82801067346d9932cbbd988153b2c535a_2_338x500.png" alt="Image 2" data-base62-sha1="gkozCM9AhMMEPO9EEL1sra4euiS" width="338" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/727104f82801067346d9932cbbd988153b2c535a_2_338x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/727104f82801067346d9932cbbd988153b2c535a_2_507x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/727104f82801067346d9932cbbd988153b2c535a.png 2x" data-dominant-color="E4E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 2</span><span class="informations">535×790 59.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @cpinter (2024-08-02 13:03 UTC)

<p>You can get the existing display node like this:</p>
<pre><code class="lang-auto">volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.GetFirstVolumeRenderingDisplayNode(volume)
</code></pre>

---
