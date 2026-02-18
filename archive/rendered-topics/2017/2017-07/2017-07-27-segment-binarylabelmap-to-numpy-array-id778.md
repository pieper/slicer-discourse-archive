# Segment / BinaryLabelMap to numpy array

**Topic ID**: 778
**Date**: 2017-07-27
**URL**: https://discourse.slicer.org/t/segment-binarylabelmap-to-numpy-array/778

---

## Post #1 by @Colin_McCurdy (2017-07-27 21:02 UTC)

<p>Operating system:Windows 10<br>
Slicer version: 4.7.0-2017-07-19</p>
<p>Hello All,</p>
<p>I’m trying to get a numpy array out of a segment or binarylabelmap and I can’t find a way to do that currently. I’m sure it’s right in front of me…</p>
<p>I’m just trying to use it to mask my grayscale data array so if there’s a better way to go about this I’m all ears!</p>
<p>What I hoped to do:<br>
grayDataArray = arrayFromVolume(grayscaleVolume)<br>
segmentArray = arrayFromVolume(segment) # this obviously doesn’t work <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
maskedData = grayDataArray * segmentArray</p>
<p>Thanks for any help and advice!</p>
<p>Colin</p>

---

## Post #2 by @lassoan (2017-07-28 00:50 UTC)

<p>Segmentation node -&gt; labelmap node: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node</a></p>
<p>Labelmap node -&gt; numpy array: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>

---

## Post #3 by @moselhy (2017-07-28 20:23 UTC)

<p>This works for me, if your Segmentation is named “Seg” and Volume is named “Vol”. If they are named differently, you would just change the parameters to ‘getNode’ in the first two lines</p>
<pre><code>volumeNode = slicer.util.getNode('Vol')  # Get the volume node
seg = slicer.util.getNode('Seg') # Get the segmentation node

# Create a binary label volume from segmentation
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
#To export specific segments instead, edit the following line with the one in the bottom
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, labelmapVolumeNode) 

# Export data as numpy arrays
dicomData = arrayFromVolume(volumeNode)
mask = arrayFromVolume(labelmapVolumeNode)
</code></pre>
<p><strong>Edit</strong>: to export specific segments instead of all of the segmentation, use the following code:</p>
<p><code>slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(seg,segmentsToExport, labelMapVolumeNode)</code></p>
<p>The <code>segmentsToExport</code> value has to be a <code>vtkStringArray</code> containing all the segment ID’s that you would like to be exported (note, I noticed that this overrides the label map), which is conceptually a fancy string array. To initialize it you have to run the following:</p>
<pre><code>#To get the segment ID of the first segment on the list (named Segment_1 below):
segmentId = seg.GetSegmentation().GetNthSegmentID(0)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/995b3aa6f5b9583114471fb465e601e9819a9a0c.png" alt="image" data-base62-sha1="lSEvE9uF603yk0PIvbflRcQCLVO" width="493" height="181"></p>
<pre><code>import vtk
segmentsToExport = vtk.vtkStringArray()
segmentsToExport.InsertNextValue(segmentId)
</code></pre>

---

## Post #4 by @Colin_McCurdy (2017-07-31 18:42 UTC)

<p>I’m assuming the following code converts all of the segments onto a single labelmap?</p>
<aside class="quote no-group" data-username="moselhy" data-post="3" data-topic="778">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moselhy/48/501_2.png" class="avatar"> moselhy:</div>
<blockquote>
<p>slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, labelmapVolumeNode)</p>
</blockquote>
</aside>
<p>So If I wanted this for one or multiple segments (but not all) I can just use:</p>
<blockquote>
<p>slicer.modules.segmentations.logic().ExportSegmentsToLabelMapNode(seg,segmentNameArray,labelMapVolumeNode)</p>
</blockquote>
<p>Now, I’m not entirely sure what I’m getting from this because now I have an error that the volume array (volumeNode) and the segmentation array (labelmapVolumeNode) have different sizes</p>

---

## Post #5 by @moselhy (2017-07-31 18:46 UTC)

<p>Try the edit that I made, does that still give you an error?</p>

---

## Post #6 by @fedorov (2017-07-31 20:58 UTC)

<aside class="quote no-group" data-username="Colin_McCurdy" data-post="4" data-topic="778">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/9d8465/48.png" class="avatar"> Colin_McCurdy:</div>
<blockquote>
<p>the volume array (volumeNode) and the segmentation array (labelmapVolumeNode) have different sizes</p>
</blockquote>
</aside>
<p>You can resample the label to match the volume geometry, for example as done here: <a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L365-L373" class="inline-onebox">SlicerRadiomics/SlicerRadiomics/SlicerRadiomics.py at master · AIM-Harvard/SlicerRadiomics · GitHub</a></p>
<p>The option of matching geometry is exposed in the <code>Segmentations</code> module GUI (specified by the “Reference volume” node), perhaps there is a corresponding API for that too, but I don’t have time to look for it now.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a08e4a75c2f5b894c532af834c6703512c43f30d.png" data-download-href="/uploads/short-url/mUlfCOjnv1U3pRvMi9kRk5c0Gfz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a08e4a75c2f5b894c532af834c6703512c43f30d_2_690x221.png" alt="image" data-base62-sha1="mUlfCOjnv1U3pRvMi9kRk5c0Gfz" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a08e4a75c2f5b894c532af834c6703512c43f30d_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a08e4a75c2f5b894c532af834c6703512c43f30d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a08e4a75c2f5b894c532af834c6703512c43f30d.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">708×227 17.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Colin_McCurdy (2017-08-09 20:11 UTC)

<p>Sorry I’m late to respond to this.<br>
I think your link is incorrect, it looks like the solution you’re speaking of is a bit further down. I think I found it though:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L383-L387" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L383-L387" target="_blank" rel="nofollow noopener">Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L383-L387</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="383" style="counter-reset: li-counter 382 ;">
<li>  return True</li>
<li>
</li>
<li>def prepareLabelsFromLabelmap(self, labelmapNode, grayscaleImage, labelsDict):</li>
<li>
</li>
<li>  combinedLabelImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(labelmapNode.GetName()))</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I appreciate the help!</p>

---

## Post #8 by @fedorov (2017-08-09 20:22 UTC)

<aside class="quote no-group" data-username="Colin_McCurdy" data-post="7" data-topic="778">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/9d8465/48.png" class="avatar"> Colin_McCurdy:</div>
<blockquote>
<p>it looks like the solution you’re speaking of is a bit further down</p>
</blockquote>
</aside>
<p>That’s probably because the code changed since I inserted the link, and I referred to the master instead of the specific commit.</p>
<p>Glad you found it anyway!</p>

---

## Post #9 by @jcfr (2017-08-09 20:44 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="778">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>because the code changed since I inserted the link</p>
</blockquote>
</aside>
<p>A neat GitHub trick is to press “y” to get a canonical link.<br>
See <a href="https://help.github.com/articles/getting-permanent-links-to-files/" class="inline-onebox">Getting permanent links to files - GitHub Docs</a></p>

---

## Post #10 by @fedorov (2017-08-09 20:57 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>!</p>
<p>Here comes the permalink: <a href="https://github.com/Radiomics/SlicerRadiomics/blob/97bdf52df6ba40b911b4e5d9783a017be2d2bfe4/SlicerRadiomics/SlicerRadiomics.py#L383-L386">https://github.com/Radiomics/SlicerRadiomics/blob/97bdf52df6ba40b911b4e5d9783a017be2d2bfe4/SlicerRadiomics/SlicerRadiomics.py#L383-L386</a></p>

---
