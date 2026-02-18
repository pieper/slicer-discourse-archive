# Call an specifica class frome c++ in python

**Topic ID**: 13777
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/call-an-specifica-class-frome-c-in-python/13777

---

## Post #1 by @aldoSanchez (2020-09-30 16:25 UTC)

<p>hello<br>
I’m trying to access to this action:<br>
vtkMRMLLabelMapVolumeDisplayNode::vtkMRMLLabelMapVolumeDisplayNode()<br>
{<br>
this-&gt;MapToColors = vtkImageMapToColors::New();<br>
this-&gt;MapToColors-&gt;SetOutputFormatToRGBA();</p>
<pre><code> // set a thicker default slice intersection thickness for use when showing
 // the outline of the label map
 this-&gt;SliceIntersectionThickness = 3;
}
</code></pre>
<p>what I want is to call this instruction in python: SliceIntersectionThickness = 3;</p>

---

## Post #2 by @Andinet_Enquobahrie (2020-09-30 16:46 UTC)

<p>Hello <a class="mention" href="/u/aldosanchez">@aldoSanchez</a></p>
<aside class="quote no-group" data-username="aldoSanchez" data-post="1" data-topic="13777" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/5f9b8f/48.png" class="avatar"> aldoSanchez:</div>
<blockquote>
<p>hello<br>
I’m trying to access to this action:<br>
vtkMRMLLabelMapVolumeDisplayNode::vtkMRMLLabelMapVolumeDisplayNode()<br>
{<br>
this-&gt;MapToColors = vtkImageMapToColors::New();<br>
this-&gt;MapToColors-&gt;SetOutputFormatToRGBA();</p>
<pre><code> // set a thicker default slice intersection thickness for use when showing
 // the outline of the label map
 this-&gt;SliceIntersectionThickness = 3;
}
</code></pre>
<p>what I want is to call this instruction in python: SliceIntersectionThickness = 3;</p>
</blockquote>
</aside>
<p>You can do something like the following</p>
<pre><code>  labelMapNode.GetDisplayNode().SetSliceIntersectionThickness(3)
</code></pre>
<p>-Andinet</p>

---

## Post #3 by @aldoSanchez (2020-09-30 17:05 UTC)

<p>thanks, it works perfectly<br>
I leave the code here:</p>
<p>labelMapNode=getNode(‘nameOftheNode’)<br>
labelMapNode.GetDisplayNode().SetSliceIntersectionThickness(1)</p>

---
