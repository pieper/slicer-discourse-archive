# Configuring vtkMRMLSliceNode

**Topic ID**: 2028
**Date**: 2018-02-05
**URL**: https://discourse.slicer.org/t/configuring-vtkmrmlslicenode/2028

---

## Post #1 by @asheu (2018-02-05 20:55 UTC)

<p>I’m currently trying to configure the vrkMRML slice node so that I can create a Slicer viewer (for example the coronal slice) that is able to be switched between two image datasets (say CT and MR images). I would like to develop a slider that helps move between these two files. However, since I have just started Slicer development, I am unsure how to approach this issue.</p>
<p>Should I write a separate Python script or would it be possible to configure the existing vrkMRML file to add new custom layouts?</p>
<p>Any insight would be helpful, thank you!</p>

---

## Post #2 by @pieper (2018-02-06 17:36 UTC)

<p>What you describe sounds like putting one image in the foreground and one in the background and crossfading?  if so you want to look at the vtkMRMLSliceCompositeNode and this example.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/CompareVolumes" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/CompareVolumes</a></p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L354-L416" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L354-L416" target="_blank" rel="nofollow noopener">pieper/CompareVolumes/blob/master/CompareVolumes.py#L354-L416</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="354" style="counter-reset: li-counter 353 ;">
<li>#</li>
<li># construct the XML for the layout</li>
<li># - one viewer per volume</li>
<li># - default orientation as specified</li>
<li>#</li>
<li>actualViewNames = []</li>
<li>index = 1</li>
<li>layoutDescription = ''</li>
<li>layoutDescription += '&lt;layout type="vertical"&gt;\n'</li>
<li>for row in range(int(rows)):</li>
<li>  layoutDescription += ' &lt;item&gt; &lt;layout type="horizontal"&gt;\n'</li>
<li>  for column in range(int(columns)):</li>
<li>    try:</li>
<li>      viewName = viewNames[index-1]</li>
<li>    except IndexError:</li>
<li>      viewName = '%d_%d' % (row,column)</li>
<li>    rgb = [int(round(v*255)) for v in self.lookupTable.GetTableValue(index)[:-1]]</li>
<li>    color = '#%0.2X%0.2X%0.2X' % tuple(rgb)</li>
<li>    layoutDescription += self.sliceViewItemPattern.format(viewName=viewName,orientation=orientation,color=color)</li>
<li>    actualViewNames.append(viewName)</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L354-L416" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
