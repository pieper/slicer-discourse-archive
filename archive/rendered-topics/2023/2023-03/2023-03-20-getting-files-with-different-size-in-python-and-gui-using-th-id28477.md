# Getting files with different size in Python and GUI using the same decimation method

**Topic ID**: 28477
**Date**: 2023-03-20
**URL**: https://discourse.slicer.org/t/getting-files-with-different-size-in-python-and-gui-using-the-same-decimation-method/28477

---

## Post #1 by @Contente (2023-03-20 14:16 UTC)

<p>Hello, everyone.</p>
<p>In order to use the decimation method, we call the method:</p>
<pre><code class="lang-auto">segmentation.SetConversionParameter("Decimation factor", "0.90")
</code></pre>
<p>My question is: by default, this method implements the DecimatePro algorithm or the new Quadric/FastQuadric ones? If not, then how can I call it using python to select which one I want to use (such as the “Boundary Deletion” checkbox in the GUI version).</p>
<p>For context purpouse, when I use the decimate by GUI I get an OBJ file with 200MB size and when I use python scripts with CLI I get an OBJ with 1GB with this decimate method from segmentation module. I’m trying to figure out why there is this difference.</p>

---

## Post #2 by @lassoan (2023-03-20 14:17 UTC)

<p>You can have a look at what the GUI does and do the same in your script:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/blob/3b556d10307c5c9ee9fd8da1ea873ddc1d48acf3/SurfaceToolbox/SurfaceToolbox.py#L419-L439">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/3b556d10307c5c9ee9fd8da1ea873ddc1d48acf3/SurfaceToolbox/SurfaceToolbox.py#L419-L439" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/3b556d10307c5c9ee9fd8da1ea873ddc1d48acf3/SurfaceToolbox/SurfaceToolbox.py#L419-L439" target="_blank" rel="noopener">Slicer/SlicerSurfaceToolbox/blob/3b556d10307c5c9ee9fd8da1ea873ddc1d48acf3/SurfaceToolbox/SurfaceToolbox.py#L419-L439</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="419" style="counter-reset: li-counter 418 ;">
          <li>def decimate(inputModel, outputModel, reductionFactor=0.8, decimateBoundary=True, lossless=False, aggressiveness=7.0):
</li>
          <li>  """Perform a topology-preserving reduction of surface triangles. FastMesh method uses Sven Forstmann's method
</li>
          <li>  (https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification).
</li>
          <li>
</li>
          <li>  :param reductionFactor: Target reduction factor during decimation. Ratio of triangles that are requested to
</li>
          <li>    be eliminated. 0.8 means that the mesh size is requested to be reduced by 80%.
</li>
          <li>  :param decimateBoundary: If enabled then 'FastQuadric' method is used (it provides more even element sizes but cannot
</li>
          <li>    be forced to preserve boundary), otherwise 'DecimatePro' method is used (that can preserve boundary edges but tend
</li>
          <li>    to create more ill-shaped triangles).
</li>
          <li>  :param lossless: Lossless remeshing for FastQuadric method. The flag has no effect if other method is used.
</li>
          <li>  :param aggressiveness: Balances between accuracy and computation time for FastQuadric method (default = 7.0). The flag has no effect if other method is used.
</li>
          <li>  """
</li>
          <li>  parameters = {
</li>
          <li>    "inputModel": inputModel,
</li>
          <li>    "outputModel": outputModel,
</li>
          <li>    "reductionFactor": reductionFactor,
</li>
          <li>    "method": "FastQuadric" if decimateBoundary else "DecimatePro",
</li>
          <li>    "boundaryDeletion": decimateBoundary
</li>
          <li>    }
</li>
          <li>  cliNode = slicer.cli.runSync(slicer.modules.decimation, None, parameters)
</li>
          <li>  slicer.mrmlScene.RemoveNode(cliNode)
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Contente (2023-03-20 19:31 UTC)

<p>Thank you very much. I’ve managed to finally decrease the size of the models using this approach.</p>

---
