---
topic_id: 44685
title: "Question Planenode Normal"
date: 2025-10-07
url: https://discourse.slicer.org/t/44685
---

# Question PlaneNode Normal

**Topic ID**: 44685
**Date**: 2025-10-07
**URL**: https://discourse.slicer.org/t/question-planenode-normal/44685

---

## Post #1 by @evaherbst (2025-10-07 11:11 UTC)

<p>I am currently creating planes based on 3 control points as follows:</p>
<blockquote>
<p>planeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsPlaneNode”, “myPlaneNode")</p>
<p>planeNode.SetPlaneType(2)  # PlaneTypeThreePoints</p>
<p>planeNode.AddControlPoint(p1[0], p1[1], p1[2])</p>
<p>planeNode.AddControlPoint(p2[0], p2[1], p2[2])</p>
<p>planeNode.AddControlPoint(p3[0], p3[1], p3[2])</p>
</blockquote>
<p>However, sometimes the normal points correctly following right hand rule of order of points</p>
<p>i.e. it matches the normal that I can compute in python:</p>
<p>n1 = np.cross(p2 - p1, p3 - p1)  # Normal direction for the plane</p>
<p>but other times the normal is flipped.</p>
<p>I see I can also set the plane by normal as a solution, but I want to understand how the normal is assigned for the 3 point based plane method (does it follow the right hand rule based on order of control points or not?).</p>
<p>Thank you.</p>

---

## Post #2 by @mau_igna_06 (2025-10-07 12:12 UTC)

<p>The code is opensource so you can check out the implementation:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/4a1e4f8ddf25bd73198c81b8cb9c67d0bd88238f/Libs/MRML/Core/vtkMRMLMarkupsPlaneNode.cxx#L571-L583">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/4a1e4f8ddf25bd73198c81b8cb9c67d0bd88238f/Libs/MRML/Core/vtkMRMLMarkupsPlaneNode.cxx#L571-L583" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4a1e4f8ddf25bd73198c81b8cb9c67d0bd88238f/Libs/MRML/Core/vtkMRMLMarkupsPlaneNode.cxx#L571-L583" target="_blank" rel="noopener nofollow ugc">Libs/MRML/Core/vtkMRMLMarkupsPlaneNode.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/4a1e4f8ddf25bd73198c81b8cb9c67d0bd88238f/Libs/MRML/Core/vtkMRMLMarkupsPlaneNode.cxx#L571-L583" rel="noopener nofollow ugc"><code>4a1e4f8dd</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="571" style="counter-reset: li-counter 570 ;">
          <li>void vtkMRMLMarkupsPlaneNode::CalculateAxesFromPoints(const double point0[3], const double point1[3], const double point2[3], double x[3], double y[3], double z[3])</li>
          <li>{</li>
          <li>  vtkMath::Subtract(point1, point0, x);</li>
          <li>  vtkMath::Normalize(x);</li>
          <li></li>
          <li>  double tempVector[3] = { 0.0 };</li>
          <li>  vtkMath::Subtract(point2, point0, tempVector);</li>
          <li>  vtkMath::Cross(x, tempVector, z);</li>
          <li>  vtkMath::Normalize(z);</li>
          <li></li>
          <li>  vtkMath::Cross(z, x, y);</li>
          <li>  vtkMath::Normalize(y);</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>HIH</p>

---

## Post #3 by @evaherbst (2025-10-07 13:37 UTC)

<p>Thank you!</p>
<p>That answers my question, the bug must be somewhere else on my end.</p>
<p>Best,</p>
<p>Eva</p>

---
