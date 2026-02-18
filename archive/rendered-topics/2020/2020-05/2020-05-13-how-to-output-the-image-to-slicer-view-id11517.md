# How to output the image to slicer view?

**Topic ID**: 11517
**Date**: 2020-05-13
**URL**: https://discourse.slicer.org/t/how-to-output-the-image-to-slicer-view/11517

---

## Post #1 by @sunshine_boycn (2020-05-13 10:51 UTC)

<p>Dear everybody:</p>
<p>I am following the tutorials on “Programming in Slicer4” implementing the demo “Implemen:ng the<br>
Laplace* Operator”. Everything is fine. The problems come out when I tried to modify the program using C++. Currently I have difficulties in converting the following lines into C++. I can’t find the corresponding class and method in C++.</p>
<pre><code># make the output volume appear in all the slice views
slicer.util.setSliceViewerLayers(background=self.outputSelector.currentNode())
</code></pre>
<p>Would any body help me out?</p>
<p>Thankyou very much</p>

---

## Post #2 by @pieper (2020-05-13 12:48 UTC)

<p>Hi - In general it can help to use the <code>git grep</code> command in the source directory to search for the definition and uses of methods.  Or you can search the repository at the github page.</p>
<p>In this case, the method is define here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L336-L377" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L336-L377" target="_blank">Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L336-L377</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="336" style="counter-reset: li-counter 335 ;">
<li>def setSliceViewerLayers(background='keep-current', foreground='keep-current', label='keep-current',</li>
<li>                         foregroundOpacity=None, labelOpacity=None, fit=False):</li>
<li>  """ Set the slice views with the given nodes.</li>
<li>
</li><li>  If node ID is not specified (or value is 'keep-current') then the layer will not be modified.</li>
<li>
</li><li>  :param background: node or node ID to be used for the background layer</li>
<li>  :param foreground: node or node ID to be used for the foreground layer</li>
<li>  :param label: node or node ID to be used for the label layer</li>
<li>  :param foregroundOpacity: opacity of the foreground layer</li>
<li>  :param labelOpacity: opacity of the label layer</li>
<li>  :param fit: fit slice views to their content (position&amp;zoom to show all visible layers)</li>
<li>  """</li>
<li>  import slicer</li>
<li>  def _nodeID(nodeOrID):</li>
<li>    nodeID = nodeOrID</li>
<li>    if isinstance(nodeOrID, slicer.vtkMRMLNode):</li>
<li>      nodeID = nodeOrID.GetID()</li>
<li>    return nodeID</li>
<li>
</li></ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L336-L377" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @sunshine_boycn (2020-05-13 13:20 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="11517">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>setSliceViewerLayers</p>
</blockquote>
</aside>
<p>Thank you very much!</p>
<p>I have solve this problem and have my C++ version of this “Implementing the Laplace* Operator” demo. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>You have introduced a good way of using “git grep”. That’s nice. Before your recommendation, I have tried to use grep in Ubuntu and “findstr” in Windows. I failed to get the correct answer because I searched in a wrong directory. I thought the function “setSliceViewerLayers” was a member function of some MRML classes.</p>
<p>Thank you. And I think it would be better to have the c++ version of this tutorial later on.</p>

---
