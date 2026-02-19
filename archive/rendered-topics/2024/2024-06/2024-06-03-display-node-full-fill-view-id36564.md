---
topic_id: 36564
title: "Display Node Full Fill View"
date: 2024-06-03
url: https://discourse.slicer.org/t/36564
---

# Display node full fill view

**Topic ID**: 36564
**Date**: 2024-06-03
**URL**: https://discourse.slicer.org/t/display-node-full-fill-view/36564

---

## Post #1 by @fqzhice (2024-06-03 07:28 UTC)

<p>we create a new extension to load dicom image, code as below:</p>
<pre><code class="lang-auto">// add to volume node
 double dirs[3][3];
 for (int i = 0; i &lt; 3; i++)
 for (int j = 0; j &lt; 3; j++)
 dirs[i][j] = 0.0;
 dirs[0][0] = 1;
 dirs[1][1] = 1;
 dirs[2][2] = 1;
auto volumeNode = vtkMRMLScalarVolumeNode::SafeDownCast(
    this-&gt;logic()-&gt;GetMRMLScene()-&gt;AddNewNodeByClass("vtkMRMLScalarVolumeNode", "Source"));
volumeNode-&gt;SetAndObserveImageData(vtkImageDataPointer);
//volumeNode-&gt;SetOrigin(100,100,100);
//volumeNode-&gt;SetSpacing(1,1,1);
//volumeNode-&gt;SetIJKToRASDirections(dirs );
volumeNode-&gt;CreateDefaultDisplayNodes();
volumeNode-&gt;SetDisplayVisibility(true);
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23879fdbed1efd09c6c76b1508ee41743d026de8.jpeg" data-download-href="/uploads/short-url/54jhHuJHqifvMUtwEtD0AJrjukw.jpeg?dl=1" title="2024-06-03-15-23-44-image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23879fdbed1efd09c6c76b1508ee41743d026de8_2_690x344.jpeg" alt="2024-06-03-15-23-44-image" data-base62-sha1="54jhHuJHqifvMUtwEtD0AJrjukw" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23879fdbed1efd09c6c76b1508ee41743d026de8_2_690x344.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23879fdbed1efd09c6c76b1508ee41743d026de8_2_1035x516.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23879fdbed1efd09c6c76b1508ee41743d026de8_2_1380x688.jpeg 2x" data-dominant-color="504F50"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-06-03-15-23-44-image</span><span class="informations">1917×956 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the problem is that</p>
<ol>
<li>the image isn’t displayed without click “visible” button</li>
<li>it show nothing if drag slider to change slicer in “blue” rect range</li>
<li>image displayed on the right-down of view</li>
</ol>

---

## Post #2 by @fqzhice (2024-06-03 10:00 UTC)

<p>i think it maybe the origin , spacing and direction error, but i dont know how get from itk image</p>

---

## Post #3 by @lassoan (2024-06-03 14:14 UTC)

<p>The only supported method of loading DICOM images into Slicer is by <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom">using the DICOM module</a>. There are many different ways to deal with DICOM data, but if you do it your own way then we cannot help.</p>

---
