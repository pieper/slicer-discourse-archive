# Scripted module version vs Slicer version

**Topic ID**: 22546
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/scripted-module-version-vs-slicer-version/22546

---

## Post #1 by @drouin-simon (2022-03-16 18:10 UTC)

<p>I have an extension that contains a scripted module (SlicerPRISMRendering) that I need to modify to work with the new markup system in Slicer 4.13. The modification will break the compatibility with the current stable version of Slicer (4.11). How can I support both versions?</p>
<p>Here’s what I deducted I should do (please confirm, I cannot find documentation on that):</p>
<ul>
<li>Create a slicer-4.11 branch in my extension repository</li>
<li>In the ExtensionsIndex repository, on the 4.11 branch, modify slicerPRISMRendering.s4ext to point to my extension’s slicer-4.11 branch</li>
<li>Modify the master branch of my extension to work with Slicer 4.13 (assuming that slicerPRISMRendering.s4ext in the master branch of the ExtensionsIndex is still pointing to the master branch of my extension’s repository)</li>
</ul>

---

## Post #2 by @jamesobutler (2022-03-16 18:54 UTC)

<p>Yes all that seems to match the content below:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extensions-index" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extensions-index</a></p>
<blockquote>
<p>Extension developers have to make sure that the extension description in each branch of the Extensions index is compatible with the corresponding Slicer version. Extension developers often create the same branches ( <code>master</code> , <code>4.11</code> , <code>4.13</code> , …) in their repository and they specify this branch name in the extensions descriptor file.</p>
</blockquote>

---

## Post #3 by @lassoan (2022-03-16 19:13 UTC)

<p>I would just add that if there are only a few minor differences then you can manage them by checking the Slicer or VTK version. For example:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/764184d5e4de1c0c0d60bf502e03da54b50a69f1/CardiacDeviceSimulator/CardiacDeviceSimulator.py#L1039-L1042">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/764184d5e4de1c0c0d60bf502e03da54b50a69f1/CardiacDeviceSimulator/CardiacDeviceSimulator.py#L1039-L1042" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/764184d5e4de1c0c0d60bf502e03da54b50a69f1/CardiacDeviceSimulator/CardiacDeviceSimulator.py#L1039-L1042" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/764184d5e4de1c0c0d60bf502e03da54b50a69f1/CardiacDeviceSimulator/CardiacDeviceSimulator.py#L1039-L1042</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="1039" style="counter-reset: li-counter 1038 ;">
            <li>if slicer.app.majorVersion*100+slicer.app.minorVersion &lt; 411:</li>
            <li>  displayNode.SetSliceIntersectionVisibility(True)</li>
            <li>else:</li>
            <li>  displayNode.SetVisibility2D(True)</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If there are too many such checks or you need to do things completely differently in different Slicer versions (or you simply don’t want to carry the baggage of backward-compatibility any further) then you can create the branches as described above - cutting off older versions from “automatic” updates from the latest versions.</p>

---
