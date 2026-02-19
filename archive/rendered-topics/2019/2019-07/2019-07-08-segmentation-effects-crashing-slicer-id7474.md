---
topic_id: 7474
title: "Segmentation Effects Crashing Slicer"
date: 2019-07-08
url: https://discourse.slicer.org/t/7474
---

# Segmentation effects crashing Slicer

**Topic ID**: 7474
**Date**: 2019-07-08
**URL**: https://discourse.slicer.org/t/segmentation-effects-crashing-slicer/7474

---

## Post #1 by @smrolfe (2019-07-08 22:26 UTC)

<p>Hello,<br>
I’m using the preview version of Slicer to do a segmentation on a 2.6 GB micro-CT scan saved as a TIF. I can do a simple segmentation, but when I try to apply the mask or split volume effect, the Slicer application crashes. I’ve checked the error logs and there were no errors generated. I’m using a Windows machine with 32GB RAM and ~500GB free disk space.</p>
<p>I also generated the following warnings when trying to use the islands effect:</p>
<blockquote>
<p>Slicer has caught an internal error.<br>
You may be able to continue from this point, but results are undefined.<br>
Suggested action is to save your work and restart.<br>
If you have a repeatable sequence of steps that causes this message, please report the issue &gt; &gt; following instructions available at <a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a><br>
The message detail is:<br>
Exception thrown in event: d:\d\p\slicer-0-build\itk\modules\core\common\include\itkImportImageContainer.hxx:199:<br>
Failed to allocate memory for image.</p>
</blockquote>
<p>and</p>
<blockquote>
<p>Slicer has caught an internal error.<br>
You may be able to continue from this point, but results are undefined.<br>
Suggested action is to save your work and restart.<br>
If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a><br>
The message detail is:<br>
Exception thrown in event: bad allocation</p>
</blockquote>
<p>I expected the amount of memory to be sufficient, but could this be the problem? Thanks for your advice.</p>

---

## Post #2 by @lassoan (2019-07-09 03:34 UTC)

<p>It seems that you run out of memory. If you don’t expect this then maybe some extra memory allocations are performed or extents are computed incorrectly. You can add a breakpoint before itkImportImageContainer.hxx:199 and inspect variables to see if the memory that is attempted to be allocated have sensible size.</p>

---

## Post #3 by @smrolfe (2019-07-09 23:03 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, I’ll try this.</p>

---

## Post #4 by @jcfr (2019-07-30 22:27 UTC)

<p>After trying to load the dataset, I didn’t get a bad allocation. Instead I got a crash due to a lookup in scalar array using a negative index.</p>
<p>Code where the error occur is the following:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/VTK/blob/2cd7e84cb92a5bc091e2764bdfd35a01caafc47c/Imaging/Stencil/vtkImageToImageStencil.cxx#L146-L154" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/2cd7e84cb92a5bc091e2764bdfd35a01caafc47c/Imaging/Stencil/vtkImageToImageStencil.cxx#L146-L154" target="_blank" rel="nofollow noopener">Kitware/VTK/blob/2cd7e84cb92a5bc091e2764bdfd35a01caafc47c/Imaging/Stencil/vtkImageToImageStencil.cxx#L146-L154</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="146" style="counter-reset: li-counter 145 ;">
<li>// index into scalar array</li>
<li>int idS = ((extent[1] - extent[0] + 1)*</li>
<li>           ((extent[3] - extent[2] + 1)*(idZ - extent[4]) +</li>
<li>            (idY - extent[2])));</li>
<li>
</li>
<li>for (int idX = extent[0]; idX &lt;= extent[1]; idX++)</li>
<li>{</li>
<li>  int newstate = 1;</li>
<li>  double value = inScalars-&gt;GetComponent(idS++,0);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The crash occur when executing the line <code>inScalars-&gt;GetComponent(idS++,0);</code> with <code>idS = -2147482744</code></p>
<p>It turns out that the <code>idS</code> ivar is of type <code>int</code>, and the value overflow … it should be changed to <code>vtkIdType</code> along with all intermediate variables.</p>
<p>The following snippet allows to reproduce the incorrect index value:</p>
<pre><code class="lang-auto">  int extent_0 = 0;
  int extent_1 = 1207;
  int extent_2 = 0;
  int extent_3 = 1250;
  int extent_4 = 0;
  int idY = 47;
  int idZ = 1421;

  int idS_test = ((extent_1 - extent_0 + 1)*
                   ((extent_3 - extent_2 + 1)*(idZ - extent_4) +
                    (idY - extent_2)));
  std::cout &lt;&lt; "idS_test " &lt;&lt; idS_test &lt;&lt; std::endl;

  idY = 48;

  idS_test = ((extent_1 - extent_0 + 1)*
                     ((extent_3 - extent_2 + 1)*(idZ - extent_4) +
                      (idY - extent_2)));
  std::cout &lt;&lt; "idS_test " &lt;&lt; idS_test &lt;&lt; std::endl;
</code></pre>
<p>associated output is:</p>
<pre><code class="lang-auto">idS_test 2147483344
idS_test -2147482744
</code></pre>
<h3>Proposed path forward</h3>
<p>To move forward,</p>
<p>We need to change the type of all intermediate variable to <code>vtkIdType</code>. The following work as expected:</p>
<pre><code class="lang-auto">  vtkIdType extent_0 = 0;
  vtkIdType extent_1 = 1207;
  vtkIdType extent_2 = 0;
  vtkIdType extent_3 = 1250;
  vtkIdType extent_4 = 0;
  vtkIdType idY = 47;
  vtkIdType idZ = 1421;

  vtkIdType idS_test = ((extent_1 - extent_0 + 1)*
                   ((extent_3 - extent_2 + 1)*(idZ - extent_4) +
                    (idY - extent_2)));
  std::cout &lt;&lt; "idS_test " &lt;&lt; idS_test &lt;&lt; std::endl;

  idY = 48;

  idS_test = ((extent_1 - extent_0 + 1)*
                     ((extent_3 - extent_2 + 1)*(idZ - extent_4) +
                      (idY - extent_2)));
  std::cout &lt;&lt; "idS_test " &lt;&lt; idS_test &lt;&lt; std::endl;
</code></pre>
<p>Output</p>
<pre><code class="lang-auto">idS_test 2147483344
idS_test 2147484552
</code></pre>

---

## Post #5 by @jcfr (2019-08-01 17:51 UTC)

<p>Here is the corresponding VTK merge request: <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/5816" rel="nofollow noopener">https://gitlab.kitware.com/vtk/vtk/merge_requests/5816</a></p>

---

## Post #6 by @jcfr (2019-08-01 18:07 UTC)

<p>Corresponding change has been integrated in Slicer as <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28419" rel="nofollow noopener">r28419</a></p>

---

## Post #7 by @smrolfe (2019-08-02 15:58 UTC)

<p>The mask/split volume effects are working now for my &gt;2G images in the preview version.  Thanks <a class="mention" href="/u/jcfr">@jcfr</a>!</p>

---
