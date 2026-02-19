---
topic_id: 12647
title: "Stl File Model Not Displaying"
date: 2020-07-20
url: https://discourse.slicer.org/t/12647
---

# STL file model not displaying

**Topic ID**: 12647
**Date**: 2020-07-20
**URL**: https://discourse.slicer.org/t/stl-file-model-not-displaying/12647

---

## Post #1 by @Matt_B (2020-07-20 16:45 UTC)

<p>I have a stl file which seems to open in 3D slicer but does not appear to display in any of the views and I’m not sure why.<br>
It opens and displays in an online viewer: <a href="https://www.viewstl.com/" rel="nofollow noopener">https://www.viewstl.com/</a></p>
<p>The file is available here: <a href="https://1drv.ms/u/s!AqHhiLxi-jzyg_FTceE7gVj6hlY0fA?e=h0PlFe" rel="nofollow noopener">https://1drv.ms/u/s!AqHhiLxi-jzyg_FTceE7gVj6hlY0fA?e=h0PlFe</a></p>
<p>Any ideas what is wrong with the files? They are created with a script so must be something not quite right in the formatting I think.</p>

---

## Post #2 by @manjula (2020-07-20 17:01 UTC)

<p>Very interesting… I don’t know how to help but re exporting from blender works well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6590b19a4d059929456fdaff6f7fc2abbdc2551d.png" data-download-href="/uploads/short-url/euuee4D0p1NvSoV6uoYJspj4JsN.png?dl=1" title="Screenshot from 2020-07-20 19-00-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6590b19a4d059929456fdaff6f7fc2abbdc2551d_2_486x500.png" alt="Screenshot from 2020-07-20 19-00-16" data-base62-sha1="euuee4D0p1NvSoV6uoYJspj4JsN" width="486" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6590b19a4d059929456fdaff6f7fc2abbdc2551d_2_486x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6590b19a4d059929456fdaff6f7fc2abbdc2551d_2_729x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6590b19a4d059929456fdaff6f7fc2abbdc2551d.png 2x" data-dominant-color="5F5F74"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-07-20 19-00-16</span><span class="informations">885×909 52.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2020-07-20 17:07 UTC)

<aside class="quote no-group" data-username="Matt_B" data-post="1" data-topic="12647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt_b/48/6614_2.png" class="avatar"> Matt_B:</div>
<blockquote>
<p>Any ideas what is wrong with the files? They are created with a script so must be something not quite right in the formatting I think.</p>
</blockquote>
</aside>
<p>In the log file, there are these errors, which looks like incorrectly created STL. I am not sure why other viewers (like Paint3D in windows showing this).</p>
<blockquote>
<p>STLReader: error while reading file C:/Users/murat/Downloads/HEAD.stl at line 341195: Premature EOF while reading ‘facet’</p>
<p>Algorithm vtkSTLReader(0000028822EF0A20) returned failure for request: vtkInformation (00000288233853B0)<br>
Debug: Off<br>
Modified Time: 231260<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_DATA<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FROM_OUTPUT_PORT: 0</p>
<p>ReadDataInternal (vtkMRMLModelStorageNode1): File C:/Users/murat/Downloads/HEAD.stl does not contain coordinate system information. Assuming LPS.</p>
<p>No input data</p>
</blockquote>

---

## Post #4 by @Matt_B (2020-07-20 18:27 UTC)

<p>Thanks for your help.<br>
Based on both the replys I was able to determine the final line in the file was not correctly formatted</p>
<p>Strangely I had previously been using blender with these files for some tasks and so that’s why I hadn’t encountered the issue with the files previously.</p>

---

## Post #5 by @Chris_Rorden (2020-07-21 11:54 UTC)

<p>The final line is missing</p>
<pre><code class="lang-auto">endsolid
</code></pre>
<p>Other readers implicitly assume the STL file ends with this command.</p>
<p>I remain steadfast in my conviction that <a href="https://discourse.slicer.org/t/beware-of-the-stl-file-format/7642">STL should be considered harmful</a>. This same structure could be saved as binary PLY saving an order of magnitude in file size, even more benefit in read speed, and with none of the faceting or vertex unification required by the STL format. I contend the STL format should only be used as the format of last resort, and tools that do not support better formats should be improved. As STL does not reuse vertices, it is inherently a poor choice for applications such as this model.</p>

---
