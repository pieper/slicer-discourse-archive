# What's wrong when trying to convert a model's coordinate points into a volume?

**Topic ID**: 33791
**Date**: 2024-01-16
**URL**: https://discourse.slicer.org/t/whats-wrong-when-trying-to-convert-a-models-coordinate-points-into-a-volume/33791

---

## Post #1 by @jumbojing (2024-01-16 05:36 UTC)

<ol>
<li>First, create a new volume and obtain the coordinates of the model based on it.</li>
<li>Convert the coordinates of the model (<code>RAS</code>) to <code>IJK</code> (from: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates" rel="noopener nofollow ugc"> (slicer.readthedocs.io)</a>)</li>
</ol>
<pre data-code-wrap="python"><code class="lang-python">def ras2IjkFor(ps, reVol):
  mat = vtk.vtkMatrix4x4()
  reVol.GetRASToIJKMatrix(mat)
  ijks= []
  for p in ps:
    ijk = [0, 0, 0, 1]
    mat.MultiplyPoint(np.append(p,1.0), ijk)
    ijk = [ int(round(c)) for c in ijk[0:3] ]
    ijks.append(ijk)
  return np.asarray(ijks)

</code></pre>
<ol start="3">
<li>Then, according to <code>IJK</code> staining</li>
</ol>
<pre data-code-wrap="python"><code class="lang-python">ps = slicer.util.array(mod)
reVol = slicer.util.getNode(reVol)
reArr = slicer.util.array(reVol)
ijk = ras2IjkFor(ps, reVol)
mArr = np.zeros_like(reArr)
z = ijk[:, 0].astype(int)
y = ijk[:, 1].astype(int)
x = ijk[:, 2].astype(int)
mArr[x, y, z] = lb
slicer.util.addVolumeFromArray(mArr)
</code></pre>
<p>but …</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/937f1245d9b7179aca3c9c4402eac0f4113af275.png" data-download-href="/uploads/short-url/l2Or75CIapm7nQ0rg3pFPdqgl1z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/937f1245d9b7179aca3c9c4402eac0f4113af275_2_688x500.png" alt="image" data-base62-sha1="l2Or75CIapm7nQ0rg3pFPdqgl1z" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/937f1245d9b7179aca3c9c4402eac0f4113af275_2_688x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/937f1245d9b7179aca3c9c4402eac0f4113af275_2_1032x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/937f1245d9b7179aca3c9c4402eac0f4113af275_2_1376x1000.png 2x" data-dominant-color="373849"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1806×1312 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The distance between the red vertebral model and the newly generated volume is so outrageous. what’s wrong???  <a class="mention" href="/u/lassoan">@lassoan</a>@pieper@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1_lRorqdx9SIxkj8DGV35d6pkGowa1GI8%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1_lRorqdx9SIxkj8DGV35d6pkGowa1GI8%2Fview%3Fusp%3Dsharing&amp;ifkv=ASKXGp3q-v3QSvNhPTtiI0vc5PCm5oIqwL8_dGDjzGKOHMbW2MV99146Gb_X7if881K1v2BLKAUj5Q&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1543613071%3A1705384969877507&amp;theme=glif">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1_lRorqdx9SIxkj8DGV35d6pkGowa1GI8%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1_lRorqdx9SIxkj8DGV35d6pkGowa1GI8%2Fview%3Fusp%3Dsharing&amp;ifkv=ASKXGp3q-v3QSvNhPTtiI0vc5PCm5oIqwL8_dGDjzGKOHMbW2MV99146Gb_X7if881K1v2BLKAUj5Q&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1543613071%3A1705384969877507&amp;theme=glif" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1_lRorqdx9SIxkj8DGV35d6pkGowa1GI8%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1_lRorqdx9SIxkj8DGV35d6pkGowa1GI8%2Fview%3Fusp%3Dsharing&amp;ifkv=ASKXGp3q-v3QSvNhPTtiI0vc5PCm5oIqwL8_dGDjzGKOHMbW2MV99146Gb_X7if881K1v2BLKAUj5Q&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1543613071%3A1705384969877507&amp;theme=glif" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @jumbojing (2024-01-17 21:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>@pieper@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #3 by @lassoan (2024-01-17 23:16 UTC)

<p>You have found the correct code snippet in the script repository. It works well, you can use it as is.</p>
<p>I cannot decypher what you intend to do from your code sample, but if you want to paint a small spheres in a volume at markup point positions then I would recommend to create a model that contains a small sphere at each markup position and then import that into a segmentation as it is shown here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-segmentation-from-a-model-node" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-segmentation-from-a-model-node</a></p>
<p>Another example where several spheres are added (it is more efficient to append all the spheres into a single polydata and add it as one segment if you have many points):</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b">
  <header class="source">

      <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="noopener">https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b</a></h4>

  <h5>SegmentGrowCutSimple.py</h5>
  <pre><code class="Python"># Generate input data
################################################

import SampleData

# Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation</code></pre>
    This file has been truncated. <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @jumbojing (2024-01-17 23:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I have also seen the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-segmentation-from-a-model-node" rel="noopener nofollow ugc">snippet</a> you provided and it was very successful, but I want to achieve the conversion from coordinate array to pixel array Because I want to convert <a href="https://drive.google.com/file/d/1WMobSpaHQpKQ39mgrt5kFknWVNIjpLB5/view?usp=drive_link" rel="noopener nofollow ugc">the model</a> or the array to a volume. Teacher, help me take a look Or perhaps there is something wrong with the code I wrote?</p>
<pre data-code-wrap="python"><code class="lang-python">def mod2Vol(mod, rVol=None, lbl = 1, mNam=''):
  mod = slicer.util.getNode(mod)
  if rVol is None:
    rVol = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
  else:
    rVol = slicer.util.getNode(rVol)
  seg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
  seg.SetReferenceImageGeometryParameterFromVolumeNode(rVol)
  slicer.modules.segmentations.logic().ImportModelToSegmentationNode(mod, seg)
  seg.CreateBinaryLabelmapRepresentation()
  vol = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", mNam)
  slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, vol, rVol)
  segArr = getArr(vol)
  Helper.nodsDel(seg)
  return sicer.util.updateVolumeFromArray(vol, segArr*lbl)

# vol = mod2Vol('pjMod')
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2635f30f25a5c284f85293b880cf4c1b1ffbd5a.png" data-download-href="/uploads/short-url/ps5TmpoNutCBbjup29n3WNcEzyO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2635f30f25a5c284f85293b880cf4c1b1ffbd5a_2_667x500.png" alt="image" data-base62-sha1="ps5TmpoNutCBbjup29n3WNcEzyO" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2635f30f25a5c284f85293b880cf4c1b1ffbd5a_2_667x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2635f30f25a5c284f85293b880cf4c1b1ffbd5a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2635f30f25a5c284f85293b880cf4c1b1ffbd5a.png 2x" data-dominant-color="9697C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">950×712 56.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20"> Um Yes, I used the <code>vtk.vtkProjectPointsToPlane()</code> method to press(or project) the vertebral body model into a plane along a certain direction…and then run <code>mod2Vol('pjMod')</code>, get <code>a none volume</code><img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20">.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81432514c65a7712c01936757bd5acea71a3f78c.png" data-download-href="/uploads/short-url/irvrX700FFvAv38EysBfWNN6qGU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81432514c65a7712c01936757bd5acea71a3f78c_2_690x268.png" alt="image" data-base62-sha1="irvrX700FFvAv38EysBfWNN6qGU" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81432514c65a7712c01936757bd5acea71a3f78c_2_690x268.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81432514c65a7712c01936757bd5acea71a3f78c_2_1035x402.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81432514c65a7712c01936757bd5acea71a3f78c_2_1380x536.png 2x" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1428×556 57.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2024-01-18 03:10 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="4" data-topic="33791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p>Because I want to convert <a href="https://drive.google.com/file/d/1WMobSpaHQpKQ39mgrt5kFknWVNIjpLB5/view?usp=drive_link">the model</a> or the array to a volume</p>
</blockquote>
</aside>
<p>You can export the segmentation to a labelmap volume.</p>

---

## Post #6 by @jumbojing (2024-01-18 06:27 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="4" data-topic="33791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p><code>egmentations.logic()</code></p>
</blockquote>
</aside>
<p><code>slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, vol, rVol)</code>, <img src="https://emoji.discourse-cdn.com/twitter/point_left/2.png?v=12" title=":point_left:t2:" class="emoji" alt=":point_left:t2:" loading="lazy" width="20" height="20">It seems that there is a problem with this sentence, Too thin to converted to? How to convert with code??<br>
<a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #8 by @jumbojing (2024-01-18 11:59 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c4a350a01153b865b73f7cd32f0d8c395570692.jpeg" data-download-href="/uploads/short-url/k13PHYAuopwLA1YkO3YRiT5kt9w.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c4a350a01153b865b73f7cd32f0d8c395570692_2_690x341.jpeg" alt="image" data-base62-sha1="k13PHYAuopwLA1YkO3YRiT5kt9w" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c4a350a01153b865b73f7cd32f0d8c395570692_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c4a350a01153b865b73f7cd32f0d8c395570692_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c4a350a01153b865b73f7cd32f0d8c395570692_2_1380x682.jpeg 2x" data-dominant-color="313A36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×950 77 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>可算对齐了!</p>

---
