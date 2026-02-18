# Optimal way of filling `vtkFloatArray`

**Topic ID**: 19262
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/optimal-way-of-filling-vtkfloatarray/19262

---

## Post #1 by @keri (2021-08-18 22:30 UTC)

<p>Hi,</p>
<p>Ususally when we deal with containers it is recommended that we prepare size of the container before filling it. For example instead of <code>std::vector::push_back()</code> it is recommended to preliminary resize it and setting values using square brackets <code>std::vector&lt;float&gt; v[0] = 12</code>.</p>
<p>I assume that when we deal with <code>vtkFloatArray</code> we should stick to the same idea.<br>
I can see that there is a <code>vtkFloatArray::Resize()</code> method and <code>vtkFloatArray::SetValue(vtkIdType, ValueType)</code>. I thought that <code>vtkIdType</code> is something like an index of a value but I noticed that there is a difference between <code>vtkFloatArray::SetValue(vtkIdType, ValueType)</code> and <code>vtkFloatArray::InsertNextValue(ValueType)</code>. If the array is filled with <code>SetValue</code> method and I addd it to the <code>vtkImageData</code> then I get strange range of values something like max 1e308 and min -1e308 (that is why my Slicer app fails). Probably <code>vtkIdType</code> is not an index?<br>
But if I use <code>InsertNextValue(ValueType)</code> then everything is fine until I watch the size of an array:</p>
<pre><code class="lang-cpp">    vtkNew&lt;vtkFloatArray&gt; array;
    auto s = array-&gt;GetSize();  //gives 0

    for (size_t z = 0; z &lt; 10; z++){
      for (size_t x = 0; x &lt; 20; x++){
        for (size_t y = 0; y &lt; 30; y++){
          array-&gt;InsertNextValue(x+y+z);
          s = array-&gt;GetSize();  // gives 1, 3, 7 etc (why not 1, 2, 3, 4 ... ?)
        }
      }
    }
// PS here I kept the idea of my code but some little things may differ like x,y,z ranges and assignement value (x+y+z)
</code></pre>
<p>The size of array increase nonlinearly… Why?</p>
<p>How should I fill the array and not loose perfomance?</p>

---

## Post #2 by @lassoan (2021-08-20 17:55 UTC)

<p>You can have a look at VTK source code for best practices.</p>
<p>Non-linear increase of reserved memory is a good technique to reduce the number of reallocations, but if you know the array size in advance then you can call <code>Allocate</code> method to avoid all reallocations and extra memory usage.</p>

---

## Post #3 by @keri (2021-08-21 14:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Non-linear increase of reserved memory is a good technique to reduce the number of reallocations</p>
</blockquote>
</aside>
<p>Didn’t know about that</p>
<p>I have just took a look to the source code and more carefully at the documentation, now I see a much better how vtk arrays work</p>
<p>Thank you</p>

---
