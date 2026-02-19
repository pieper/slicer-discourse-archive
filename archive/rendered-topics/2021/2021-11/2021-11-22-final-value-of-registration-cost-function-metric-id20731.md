---
topic_id: 20731
title: "Final Value Of Registration Cost Function Metric"
date: 2021-11-22
url: https://discourse.slicer.org/t/20731
---

# Final value of registration cost function metric

**Topic ID**: 20731
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/final-value-of-registration-cost-function-metric/20731

---

## Post #1 by @bz78 (2021-11-22 18:16 UTC)

<p>Hi Slicer Forum,</p>
<p>Is there a way to get the final value of the cost function (default being MattesMutualInformation, I believe) when registering volumes from Jupyter?</p>
<p>For a set of CTs, we are looping through a ton of MRIs to see which of those MRIs, when registered, best fits each CT. Obtaining the final value that the registration algorithm optimized for each combination would be the best solution.</p>
<p>Here is the core registration code:<br>
Is the final value of the cost function stored in any of the objects in this script?</p>
<pre><code class="lang-auto">    time_1_node = slicer.util.loadVolume(filename1)
    time_2_node = slicer.util.loadVolume(filename2)
    output_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
    transform_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode")
    
    parameters = {}
    parameters["fixedVolume"] = time_1_node
    parameters["movingVolume"] = time_2_node
    parameters['outputVolume'] = output_node
    parameters['outputTransform'] = transform_node
    parameters['initializeTransformMode'] = "useCenterOfHeadAlign"
    parameters['useRigid'] = True
        
    cliNode = slicer.cli.runSync(slicer.modules.brainsfit, None, parameters)
    
    myStorageNode2 = transform_node.CreateDefaultStorageNode()
    transform_filename = "output_transform.h5"
    myStorageNode2.SetFileName(transform_filename)
    myStorageNode2.WriteData(transform_node)
    
    myStorageNode = output_node.CreateDefaultStorageNode()
    output_filename = newFileString
    myStorageNode.SetFileName(output_filename)
    myStorageNode.WriteData(output_node)
</code></pre>

---

## Post #2 by @lassoan (2021-11-23 06:47 UTC)

<p>Similarity metric value is usually not be comparable between different images. Better metric value for the same image pair should indicate that the images are better aligned. However, metric value between two different image pairs, for example moving1&amp;fixed and moving2&amp;fixed, does not tell if fixed image is more similar (or better aligned) with moving1 or moving2 image.</p>
<p>Anyway, if you want to get the final metric value then you can specify a log file name for BRAINSfit, which will contain the final metric value:</p>
<pre><code class="lang-auto"># Specify a filename for the metric table
logFile = slicer.app.temporaryPath+"/brainsfitlog.csv"
cliNode.SetParameterAsString("logFileReport", logFile)

# ...run the registration

# Load the final metric value from the last row of the metric table
metricTable = slicer.util.loadTable(logFile)
finalMetricValue = float(metricTable.GetCellText(metricTable.GetNumberOfRows()-1, metricTable.GetColumnIndex('MetricValue')))
slicer.mrmlScene.RemoveNode(metricTable) # we don't need the metric table anymore
print(finalMetricValue)
</code></pre>
<p>However, BRAINSfit module always returns a hardcoded placeholder value (123.456789) - see implementation <a href="https://github.com/BRAINSia/BRAINSTools/blob/fdff2d1e3d11f929e81c83796d53ac761bd59923/BRAINSCommonLib/BRAINSFitHelper.h#L488-L501">here</a>.</p>
<p><a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> do you know why his feature got disabled? Could you re-enable it?</p>

---

## Post #3 by @bz78 (2021-11-23 10:30 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a>, thanks for educating us re: metrics! In that case, is there a better value/calculation to determine which of [<code>&lt;moving1&gt;, &lt;moving2&gt;, &lt;moving3&gt;, ..., &lt;movingN&gt;]</code> is best aligned with <code>&lt;fixed&gt;</code>?</p>
<p>Thanks as well for the sample code - we’ve implemented it and see what you mean by the hardcoded placeholder value. We can try to code a patch but let us know if there is a source update for that feature!</p>

---

## Post #4 by @lassoan (2021-11-23 14:22 UTC)

<aside class="quote no-group" data-username="bz78" data-post="3" data-topic="20731">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bz78/48/5964_2.png" class="avatar"> bz78:</div>
<blockquote>
<p>is there a better value/calculation to determine which of [ <code>&lt;moving1&gt;, &lt;moving2&gt;, &lt;moving3&gt;, ..., &lt;movingN&gt;]</code> is best aligned with <code>&lt;fixed&gt;</code> ?</p>
</blockquote>
</aside>
<p>There are some similarity metrics that are used for intensity based image registration that might be usable for this. You just need to be careful in which metric you choose, because both intensity difference and spatial misalignment may result in worse metric value. You may also want to use a smaller region than what was used for registration (for registration a larger region may help in making the method more robust at the expense of somewhat decreasing accuracy). Normalizing the intensity of the images in that region before computing the metric might help, too, with making evaluation more consistent across moving images.</p>
<p>If you want to evaluate best fit only in term of minimal residual error in spatial alignment then you may use metrics that are not commonly used for automatic intensity-based image registration (because they are hard to implement). For example, you could implement a method that detects landmarks and compute distance between correpsonding landmarks in the fixed and moving images. Or you can segment relevant structures and compute Hausdorff distance between them.</p>
<p>You may also ask advice from registration experts at the <a href="https://discourse.itk.org">ITK forum</a>.</p>

---
