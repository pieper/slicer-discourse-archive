# Applying a SimpleFilter to a sequence

**Topic ID**: 16957
**Date**: 2021-04-06
**URL**: https://discourse.slicer.org/t/applying-a-simplefilter-to-a-sequence/16957

---

## Post #1 by @mc_barbour (2021-04-06 03:49 UTC)

<p>I’m trying to apply a LaplacianSharpeningImageFilter to a volume sequence (4DCT) using the python interpreter. I’m used to using loadable modules via python but I understand that SimpleFilters is a scripted module. I’m trying to loop through the sequence and execute the filter widget on every image in the sequence.</p>
<p>The function that I’ve written does not seem to work as I’d thought and only the first image in the sequence is filtered. Am I missing something about how to execute a scripted module in a loop or the functionality of the applyButton call? I thought the issue might be due to the MRML scene changing to the output volume after executing the widget (b.click()), but I’ve added a call to a function that sets the MRML display back to the original sequence. Any advice or examples of applying a scripted module to a sequence would be appreciated.</p>
<p>def laplace_sharp_seq(seq_name, n_start, n_vol):</p>
<pre><code># define widget
filter_widget = slicer.modules.SimpleFiltersWidget
filter_params = filter_widget.filterParameters
filter_widget.filterSelector.setCurrentIndex(142) # Laplacian Filter
b = filter_widget.applyButton

# load sequence and sequence browser
seq = slicer.util.getNode(seq_name)
seq_browser = slicer.util.getNode(seq_name + " browser")


for node_id in range(n_start, n_vol + n_start):
    print(node_id)
    update_display(seq). # make sure the MRML scene is showing the sequence
    seq_browser.SetSelectedItemNumber(node_id)
    outModel=slicer.vtkMRMLScalarVolumeNode()
    outModel.SetName("test_py_"+str(node_id))
    slicer.mrmlScene.AddNode(outModel)
    filter_params.outputSelector.setCurrentNode(outModel)
    b.click() 
return</code></pre>

---

## Post #2 by @lassoan (2021-04-06 13:42 UTC)

<p>Simple Filters module runs the processing in the background. You need to check if processing is completed and only then switch to the next frame.</p>
<p>Instead of simulating button clicks it would be more robust to use Simple Filters logic, or go one level lower and use SimpleITK filters.</p>

---

## Post #3 by @mc_barbour (2021-04-08 15:55 UTC)

<p>Great, thanks. I got the widget version to work and will try out a version using the logic.</p>

---
