# Get volume being shown in qMRMLThreeDView or vtkMRMLViewNode from Python

**Topic ID**: 22655
**Date**: 2022-03-23
**URL**: https://discourse.slicer.org/t/get-volume-being-shown-in-qmrmlthreedview-or-vtkmrmlviewnode-from-python/22655

---

## Post #1 by @marcosrdac (2022-03-23 15:13 UTC)

<p>Supose I see a volume in a 3D view. Once I have that view instance in hands, how can I know which volume is being shown there? (instance = qMRMLThreeDView or vtkMRMLViewNode)</p>
<p>Thank you very much!</p>

---

## Post #2 by @mau_igna_06 (2022-03-23 16:29 UTC)

<p>I think you could use a function to send a ray in the camera direction and see with what volume it collides first.<br>
I think it could be possible but I don’t know how</p>

---

## Post #3 by @marcosrdac (2022-03-23 16:42 UTC)

<p>Thanks, Mauro. I believe your solution would give me some results, though I think it would not meet my needs well. I will try to make myself more clear:</p>
<p>If there is one or more volumes visible in the view, even if my camera is not pointing to them, I would like be able to list their IDs.</p>

---

## Post #4 by @mau_igna_06 (2022-03-23 16:59 UTC)

<p>Ok. Then you just need to traverse all displayNodes of those volumes and</p>
<pre><code class="lang-auto">volumeDisplayNode = volumeNode.GetDisplayNode()
viewNodesIDs = volumeDisplayNode.GetViewNodeIDs()
visibility = False
for i in range(len(viewNodesIDs))
  visibility = volumeDisplayNode.GetVisibility() and volumeDisplayNode.GetViewNodeIDs()[i] == 'myParticularViewID'
  if visibility:
    break

if visibility:
  myListOfVisibleVolumesIDs.append(volumeNode.GetID())
</code></pre>
<p>to get ‘myParticularViewID’ just use GetID() on the viewNodeThatYouHave.</p>
<p>I think that should work.</p>

---

## Post #5 by @marcosrdac (2022-03-23 17:34 UTC)

<p>I think you walk in a good way. The issue is that <code>volumeDisplayNode.GetViewNodeIDs()</code> gives me an empty tuple (<code>()</code>) (though in Slicer I definitely see the Red slice view showing my node). I saw in the documentation that it means “every view”. So I would advise people to list all 3D and slice views if they want to have control over the volume views of interest.</p>

---

## Post #6 by @marcosrdac (2022-03-24 14:46 UTC)

<p>Also, thank you very much, <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> !</p>

---

## Post #7 by @shai-ikko (2025-02-13 14:20 UTC)

<p>(almost three years later)</p>
<p>I was looking for this, and the answer given was insufficient for me (because <code>GetViewNodeIDs()</code> returns an empty tuple both for volumes displayed in all views, and for volumes displayed in no view).</p>
<p>I found a way to get from a <code>sliceWidget</code> to the displayed view – there is actually, potentially, more than one, because slice widgets can blend two volumes (background and foreground) and a label-map.</p>
<p>Anyway,</p>
<pre data-code-wrap="python"><code class="lang-python">node = sliceWidget.sliceLogic().GetBackgroundLayer().GetVolumeNode()
</code></pre>

---
