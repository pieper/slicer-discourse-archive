# How to set editable intensity range for individual segmentation components (each individual segment)

**Topic ID**: 9941
**Date**: 2020-01-25
**URL**: https://discourse.slicer.org/t/how-to-set-editable-intensity-range-for-individual-segmentation-components-each-individual-segment/9941

---

## Post #1 by @Vincent_C (2020-01-25 04:20 UTC)

<p>Hi all,</p>
<p>How can I set an editable intensity range for individual segmentation components separately under the Masking feature in Segment Editor? For example, I have 3 segments, A, B and C, of which each I want to limit to a unique editable intensity range to each. How can I do this without having to manually change the range for each segment?</p>
<p>Thanks</p>

---

## Post #2 by @Juicy (2020-01-25 07:34 UTC)

<p>Can you describe more about what you are trying to do? Are you trying to globally threshold different segments using the threshold effect, or are you manually painting using the masking function?</p>

---

## Post #3 by @Vincent_C (2020-01-25 17:50 UTC)

<p>Hi,</p>
<p>Thanks for the reply,</p>
<p>I am manually painting using the masking function over a CT image. For example:</p>
<p>Segment A: Editable intensity range = -50 to 10<br>
Segment B: Editable intensity range = 70 to 100<br>
Segment B: Editable intensity range = -30 to 150</p>
<p>It is a pain to manually adjust the range everytime for each segment!</p>
<p>Thanks</p>

---

## Post #4 by @manjula (2020-01-25 18:13 UTC)

<p>does this helps ?</p>
<p>segmentsFromHounsfieldUnits = [  [“fat”, -200, -50], [“muscle”, 25, 70],   [“bone”, 130, 3000] ]</p>
<p>from python script repository</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37#file-segmentbythresholding-py" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37#file-segmentbythresholding-py" target="_blank" rel="nofollow noopener">https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37#file-segmentbythresholding-py</a></h4>
<h5>SegmentByThresholding.py</h5>
<pre><code class="Python"># Download a sample data set (chest CT)
import SampleData
masterVolumeNode = SampleData.SampleDataLogic().downloadCTChest()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create temporary segment editor to get access to effects</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37#file-segmentbythresholding-py" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Vincent_C (2020-01-25 18:26 UTC)

<p>Hi Manjula,</p>
<p>Yes, this seems to be it! I am a novice user and not familiar with python - can you show me what the script will look like if I have an existing segment “Muscle” that I want to limit to  -29 (min) to 150(max)?</p>

---

## Post #6 by @Juicy (2020-01-25 21:30 UTC)

<p>The script will globally threshold 3 different segments to different threshold ranges which you can also do manually using the threshold effect.</p>
<p>I don’t know of a good way to set the mask for each segment so that when you change between them the mask threshold values will update. Have you looked into region growing methods for segmenting the different soft tissue components? It may save you a lot of time. Take a look at this video:</p>
<p><a href="https://www.youtube.com/watch?v=BJoIexIvtGo" rel="nofollow noopener">Whole heart segmentation from cardiac CT in 10 minutes</a></p>

---

## Post #7 by @lassoan (2020-01-26 02:11 UTC)

<p><a class="mention" href="/u/juicy">@Juicy</a> <a class="mention" href="/u/manjula">@manjula</a> thanks for the great suggestions. It is awesome to see that you’ve learnt so much about Slicer and now helping others, too! Well done.</p>
<p>I particularly like recommendatiom of “Grow from seeds” here, as it effectively learns the intensity range dynamically instead of trying to apply some predefined textbook values (which do not work very well, especially for soft tissues).</p>
<p>Pre-creating segments with fixed intensity ranges can be useful, too, at least to have a general idea about how well the different tissue types are separable with simple global thresholding.</p>

---
