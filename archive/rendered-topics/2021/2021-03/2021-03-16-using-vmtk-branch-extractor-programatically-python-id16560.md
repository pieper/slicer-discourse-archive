# Using VMTK Branch Extractor Programatically (Python)

**Topic ID**: 16560
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/using-vmtk-branch-extractor-programatically-python/16560

---

## Post #1 by @mjg (2021-03-16 03:16 UTC)

<p>How can I get a bifurcated centerline as two separate numpy arrays? I can view the two centerlines with the below code. How can I then get the red centerline as one numpy array, and the blue centerline as another numpy array?</p>
<p>Thank you!</p>
<pre><code>vmtkCommand = r'vmtkcenterlines -ifile ' + modelPath + r' --pipe vmtkbranchextractor -ofile ' + extractedPath + r' --pipe vmtkcenterlineviewer -cellarray CenterlineIds'
myPype = pypes.PypeRun(vmtkCommand)
</code></pre>
<p>Which returns:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71560e04df688776ec3814e33b5fb1306d2e5c08.png" data-download-href="/uploads/short-url/gaCkbKA1QQ0MzbUecQFGZjF0ndm.png?dl=1" title="Screen Shot 2021-03-15 at 11.10.37 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71560e04df688776ec3814e33b5fb1306d2e5c08_2_690x417.png" alt="Screen Shot 2021-03-15 at 11.10.37 PM" data-base62-sha1="gaCkbKA1QQ0MzbUecQFGZjF0ndm" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71560e04df688776ec3814e33b5fb1306d2e5c08_2_690x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71560e04df688776ec3814e33b5fb1306d2e5c08_2_1035x625.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71560e04df688776ec3814e33b5fb1306d2e5c08_2_1380x834.png 2x" data-dominant-color="191933"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-15 at 11.10.37 PM</span><span class="informations">1930×1168 99.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-03-26 03:34 UTC)

<p>You can see an example of how to extract a specific branch by thresholding based on group ID:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L938-L946" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L938-L946" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L938-L946</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="938" style="counter-reset: li-counter 937 ;">
<li>assignAttribute = vtk.vtkAssignAttribute()</li>
<li>assignAttribute.SetInputData(mergedCenterlines)</li>
<li>assignAttribute.Assign(self.groupIdsArrayName, vtk.vtkDataSetAttributes.SCALARS,</li>
<li>                       vtk.vtkAssignAttribute.CELL_DATA)</li>
<li>thresholder = vtk.vtkThreshold()</li>
<li>thresholder.SetInputConnection(assignAttribute.GetOutputPort())</li>
<li>groupId = mergedCenterlines.GetCellData().GetArray(self.groupIdsArrayName).GetValue(cellId)</li>
<li>thresholder.ThresholdBetween(groupId - 0.5, groupId + 0.5)</li>
<li>thresholder.Update()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
