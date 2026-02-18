# Custom Color Map .txt file Implementation via code

**Topic ID**: 29761
**Date**: 2023-05-31
**URL**: https://discourse.slicer.org/t/custom-color-map-txt-file-implementation-via-code/29761

---

## Post #1 by @seanchoi0519 (2023-05-31 23:59 UTC)

<p>Hello,</p>
<p>I have a custom color map .txt file that I’d like to apply to a displayNode.<br>
I have the resourcePath to my .txt file as follows:</p>
<p>customColorMapPath = moduleDir +‘/Resources/CustomColorMaps/custom.txt’</p>
<p>It would be perfect if I could find a way to fit this into the code below to replace the ColdToHotRainbow.txt.</p>
<p>node.GetDisplayNode().SetAndObserveColorNodeID(‘vtkMRMLColorTableNodeFileColdToHotRainbow.txt’)</p>
<p>What would be the best way to do this?<br>
I’ve tried looking up the documentation however could not find anything related to a custom .txt file - <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/gui.html#create-custom-color-map-and-display-color-legend" class="inline-onebox" rel="noopener nofollow ugc">Install Slicer — 3D Slicer documentation</a></p>
<p>Please note that I’m looking to get this done all programmatically (no editing via the user interface or dragging the file in). Ideally the .txt file is imported by code on the backend.</p>
<p>I’m fairly new to 3DSlicer, so a simple, clear answer would be appreciated!</p>

---

## Post #2 by @jamesobutler (2023-06-01 00:31 UTC)

<p>If using python, there are a lot of common functions available in <code>slicer.util</code>. Take a look at the <code>loadColorTable</code> method below which will allow you to programmatically load the custom color table file. This method returns the node from which you can <code>GetID()</code> for use in the <code>SetAndObserveColorNodeID</code> method that you mentioned.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/f331600faffb462295cbe2775e10728b88dab13d/Base/Python/slicer/util.py#L735-L743">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/f331600faffb462295cbe2775e10728b88dab13d/Base/Python/slicer/util.py#L735-L743" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/f331600faffb462295cbe2775e10728b88dab13d/Base/Python/slicer/util.py#L735-L743" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/f331600faffb462295cbe2775e10728b88dab13d/Base/Python/slicer/util.py#L735-L743</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="735" style="counter-reset: li-counter 734 ;">
          <li>def loadColorTable(filename, returnNode=False):</li>
          <li>    """Load node from file.</li>
          <li>
          </li>
<li>    :param filename: full path of the file to load.</li>
          <li>    :param returnNode: Deprecated.</li>
          <li>    :return: loaded node (if multiple nodes are loaded then a list of nodes).</li>
          <li>      If returnNode is True then a status flag and loaded node are returned.</li>
          <li>    """</li>
          <li>    return loadNodeFromFile(filename, 'ColorTableFile', {}, returnNode)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Or if you want to create the color table programmatically rather than from file:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/gui.html#create-custom-color-table" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/gui.html#create-custom-color-table</a></p>
<p>Color Table file format:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html</a></p>

---

## Post #3 by @seanchoi0519 (2023-06-01 00:57 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="29761">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>SetAndObserveColorNodeID</p>
</blockquote>
</aside>
<p>Thanks so much, this worked great.</p>

---
