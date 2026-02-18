# Running Cross-section analysis via CLI Slicer Python Console

**Topic ID**: 38269
**Date**: 2024-09-08
**URL**: https://discourse.slicer.org/t/running-cross-section-analysis-via-cli-slicer-python-console/38269

---

## Post #1 by @klchtsk (2024-09-08 00:20 UTC)

<p>Dear community,</p>
<p>I’m building a code, which relies on cross-section analysis. The output I’m interested in is the standard output as in GUI: table and plot of diameters. I’m struggling to achieve the same via CLI.</p>
<pre><code class="lang-auto">
# Step 4: Cross-Sectional Analysis
def cross_sectional_analysis(centerline_model_node, segmentation_node):

    # Initialize the CrossSectionAnalysis logic
    logic = CrossSectionAnalysis.CrossSectionAnalysisLogic()

    # Set the inputs for the CrossSectionAnalysis logic
    logic.setInputCenterlineNode(centerline_model_node)
    logic.setLumenSurface(segmentation_node, 'Segment_1')
    
    # Run the cross-sectional analysis
    logic.run()

    # Create and set the output table node if it does not exist
    if not logic.outputTableNode:
        output_table_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
        logic.setOutputTableNode(output_table_node)
        print("Created and set new output table node.")

    # Create and set the output plot series node if it does not exist
    if not logic.outputPlotSeriesNode:
        output_plot_series_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode")
        logic.setOutputPlotSeriesNode(output_plot_series_node)
        print("Created and set new output plot series node.")

    # Determine the number of control points
    if centerline_model_node.IsTypeOf("vtkMRMLModelNode"):
        number_of_points = centerline_model_node.GetPolyData().GetNumberOfPoints()
    elif centerline_model_node.IsTypeOf("vtkMRMLMarkupsShapeNode"):
        trimmed_spline = vtk.vtkPolyData()
        if not centerline_model_node.GetTrimmedSplineWorld(trimmed_spline):
            number_of_points = centerline_model_node.GetSplineWorld().GetNumberOfPoints()
        else:
            number_of_points = trimmed_spline.GetNumberOfPoints()
    else:
        number_of_points = centerline_model_node.GetCurvePointsWorld().GetNumberOfPoints()

    print(f"Number of control points: {number_of_points}")

#GetArray?

#UpdateTable?
</code></pre>
<p>Thank you in advance!</p>
<p>Bohdan</p>

---

## Post #2 by @chir.set (2024-09-08 09:09 UTC)

<ol>
<li>You must import the module before creating an instance of the logic class.</li>
</ol>
<pre><code class="lang-auto">import CrossSectionAnalysis
logic = CrossSectionAnalysis.CrossSectionAnalysisLogic()
</code></pre>
<ol start="2">
<li>Create the output <em>table</em> and <em>plot</em> nodes <strong>before</strong> calling <em>logic.run()</em></li>
<li>You may also call <em>logic.getNumberOfPoints()</em>.</li>
</ol>

---

## Post #3 by @klchtsk (2024-09-08 09:57 UTC)

<p>It worked! I didn’t see that!</p>
<p>As for Import - I have listed all imports on top of the whole project, so that I wasn’t copied over. Sorry that was misleading from my side.</p>
<p>And for some reason, if I use GetNumberOfPoints directly without check for type, it ends un in error, so I looked up the source code and used it directly in mine. Probably not elegant solution, but it works.</p>
<p>Thank you!</p>

---
