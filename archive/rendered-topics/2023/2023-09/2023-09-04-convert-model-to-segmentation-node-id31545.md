# Convert model to segmentation node

**Topic ID**: 31545
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/convert-model-to-segmentation-node/31545

---

## Post #1 by @hyncik (2023-09-04 12:45 UTC)

<p>Hi, I have a labeled surface model of a pelvic floor (47 labels in a single file, but labels separated):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e02e23c1abd1e4afa0053a722d7a8947f478bddb.jpeg" data-download-href="/uploads/short-url/vZbO2MF7t9DKABMMdDfLjfdtGNd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e02e23c1abd1e4afa0053a722d7a8947f478bddb_2_619x500.jpeg" alt="image" data-base62-sha1="vZbO2MF7t9DKABMMdDfLjfdtGNd" width="619" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e02e23c1abd1e4afa0053a722d7a8947f478bddb_2_619x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e02e23c1abd1e4afa0053a722d7a8947f478bddb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e02e23c1abd1e4afa0053a722d7a8947f478bddb.jpeg 2x" data-dominant-color="6D8A97"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">710×573 91.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
If I make a segmentation, all segmented labels have the same color:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95e1da3c090e1813e1de4ddfa19928e040ab05d3.png" alt="image" data-base62-sha1="lnV1QyjlgAYR442ryieXh0qMY03" width="306" height="194"><br>
The same output appear by reading VTK or STL or whatever. Any help, how can I make a segmentation having particular segments distinguished by colors (I mean segmentation labeled too)?</p>

---

## Post #2 by @pieper (2023-09-04 13:30 UTC)

<aside class="quote no-group" data-username="hyncik" data-post="1" data-topic="31545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hyncik/48/67418_2.png" class="avatar"> hyncik:</div>
<blockquote>
<p>labeled surface model</p>
</blockquote>
</aside>
<p>Please describe how the file was generated and how the labels are represented.</p>
<p>To make them into a Slicer segmentation you may need one file per segment and then merge them into a single segmentation with the Move/Copy option in the Segmentations module.  It may be easier to write a script for this, but it could be done with the GUI.</p>

---

## Post #3 by @hyncik (2023-09-04 13:40 UTC)

<p>I am writing it as a script (Slicer module). The file was converted by my script from a third-party software. I can convert to any format, currently I tested STL and VTK. I prefer VTK as I don’t loose the information on node numbering. In case of STL, it has the labels separated as solids, in case of VTK, it is an unstructured grid by labels distinguished by celldata. The same result appears with VTK polydata (labels distinguished by celldata).</p>
<p>The story behind is that I have a input file from a third-party software, I want to import the data into Slicer (that’s why I convert to VTK), make some corrections (morphing) and export it back for calculation.</p>
<p>I wanted to avoid multiple files, so is it necessary to have a file per label? Thank you.</p>

---

## Post #4 by @pieper (2023-09-04 17:28 UTC)

<p>Oh good, if you are writing a script it should be pretty straightforward.  The API of the segmentation infrastructure is very extensive and nicely documented.  You should just need to use <code>AddSegmentFromClosedSurfaceRepresentation</code> and similar methods.  If you do the whole process in Slicer you don’t need to use files at all.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/4a668bea6ebd183d9d0b70a510e87ea38164fd33/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L275">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/4a668bea6ebd183d9d0b70a510e87ea38164fd33/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L275" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4a668bea6ebd183d9d0b70a510e87ea38164fd33/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L275" target="_blank" rel="noopener">Slicer/Slicer/blob/4a668bea6ebd183d9d0b70a510e87ea38164fd33/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L275</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="265" style="counter-reset: li-counter 264 ;">
          <li>/// Get low-level access to the vtkPolyData object that stores a segment's closed surface representation.</li>
          <li>/// If representation does not exist yet then CreateClosedSurfaceRepresentation() must be called before this method.</li>
          <li>/// This function gives direct access to the internal data object, therefore modifications to this object will change the segmentation.</li>
          <li>/// Internal representation of the data object may change in the future (for example it may be possible that one vtkPolyData</li>
          <li>/// will be shared between multiple segments), therefore to get closed surface representation of a segment for read-only access,</li>
          <li>/// GetClosedSurfaceRepresentation() method is recommended.</li>
          <li>virtual vtkPolyData* GetClosedSurfaceInternalRepresentation(const std::string segmentId);</li>
          <li></li>
          <li>/// Add new segment from a closed surface.</li>
          <li>/// \return Segment ID of the new segment. Empty string if an error occurred.</li>
          <li class="selected">virtual std::string AddSegmentFromClosedSurfaceRepresentation(vtkPolyData* polyData,</li>
          <li>  std::string segmentName = "", double color[3] = nullptr, std::string segmentId = "");</li>
          <li></li>
          <li>/// Add new segment from a binary labelmap.</li>
          <li>/// \return Segment ID of the new segment. Empty string if an error occurred.</li>
          <li>std::string AddSegmentFromBinaryLabelmapRepresentation(vtkOrientedImageData* imageData,</li>
          <li>  std::string segmentName = "", double color[3] = nullptr, std::string segmentId = "");</li>
          <li></li>
          <li>/// Delete segment from segmentation.</li>
          <li>void RemoveSegment(const std::string&amp; segmentID);</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @hyncik (2023-09-05 03:12 UTC)

<p>Thank you, but still fumbling… Returning to your first answer, does it mean that Slicer doesn’t recognize segments in a single file and I need one file per each segment anyway, even by scripting approach? But it seems to me that Slicer must somehow recognize the segments from a single file, because it assigns colors to them upon reading…</p>

---

## Post #6 by @pieper (2023-09-05 11:51 UTC)

<aside class="quote no-group" data-username="hyncik" data-post="5" data-topic="31545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hyncik/48/67418_2.png" class="avatar"> hyncik:</div>
<blockquote>
<p>Slicer doesn’t recognize segments in a single</p>
</blockquote>
</aside>
<p>Since you are starting with a triangle mesh (a polydata in vtk terminology) you can associate values with points and display them using a lookup table (either continuous or discrete) when loading the data as a Model in Slicer.  But when loading the file as a Segmentation, these scalar value are not considered.  I don’t recall ever seeing files that used point scalars to indicate segments, so it’s probably not a standard approach or at least it’s not something we support currently.  But you can write a script to handle this case.</p>

---

## Post #7 by @cpinter (2023-09-05 14:36 UTC)

<p>I’d probably try this:</p>
<ol>
<li>Write a script that uses <a href="https://vtk.org/doc/nightly/html/classvtkSelectPolyData.html">vtkSelectPolyData</a> to create individual polydata objects for each label</li>
<li>Create a vtkMRMLModelNode for each per-segment polydata</li>
<li>In Data module create a folder and move all these models into it</li>
<li>Right-click folder and convert the models to a segmentation</li>
</ol>

---

## Post #8 by @lassoan (2023-09-05 15:02 UTC)

<p>If you don’t need to edit your colored mesh in Segment Editor then you can load it as model. Slicer can use the associated point or cell scalars for coloring the model. If you want to edit segments using Segment Editor then you can follow Csaba’s instructions above; or save the segments as a multiblock data set with <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmentations.html#segmentation-surface-file-format-seg-vtm">segmentation-specific metadata</a> that Slicer can directly load as segmentation.</p>
<p>Note that in the segmentations infrastructure of Slicer we chose to store closed surface representation of a segmentation as a multiblock dataset (and not as a simple polydata with cell scalars). This makes it is easier and less computationally expensive to extract each segment. This may matter when you work with atlases that have hundreds of segments.</p>

---

## Post #9 by @hyncik (2023-09-08 00:41 UTC)

<p>Thank you, all, I will try to proceed accordingly. Ludek</p>

---
