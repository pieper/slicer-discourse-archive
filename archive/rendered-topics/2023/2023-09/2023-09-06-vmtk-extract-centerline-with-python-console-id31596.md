---
topic_id: 31596
title: "Vmtk Extract Centerline With Python Console"
date: 2023-09-06
url: https://discourse.slicer.org/t/31596
---

# VMTK Extract Centerline with python console

**Topic ID**: 31596
**Date**: 2023-09-06
**URL**: https://discourse.slicer.org/t/vmtk-extract-centerline-with-python-console/31596

---

## Post #1 by @wesselk (2023-09-06 19:17 UTC)

<p>Hello, I am looking to utilize the vmtk module for the ‘Extract Centerline’ and ‘Cross-section Analysis’ features with a purely scripted method, similar to <a href="https://discourse.slicer.org/t/automatic-centerline/14829/12">this issue</a> which had a lot of great information.</p>
<p>A brief summary of my workflow:</p>
<ul>
<li>I use other software to create an aorta segmentation, determine ideal endpoints for the centerline, convert those endpoint coordinates to RAS, and save them to a file ‘Endpoints.mrk.json’</li>
<li>I am running “Slicer --python-script extractCenter.py”, where the contents of extractCenter.py are:</li>
</ul>
<blockquote>
<p>CT_vol = slicer.util.loadVolume(‘CT.nii’)<br>
end_pts = slicer.util.loadMarkups(‘Endpoints.mrk.json’)<br>
aorta_seg = slicer.util.loadSegmentation(‘aorta.nii’)<br>
aorta_seg_1 = aorta_seg.GetAttribute(“Segment_1”)<br>
centerline = slicer.util.getModuleLogic(‘ExtractCenterline’).extractCenterline(aorta_seg_1, end_pts)</p>
</blockquote>
<p>My issue:</p>
<ul>
<li>I believe aorta_seg_1 is not what I think it is, how can I properly access the Segment_1 vtkDataObject, which is a child of the ‘aorta’ node?  Currently if I print out type(aorta_seg_1) I get ‘NoneType’</li>
<li>ExtractCenterline has a lot of output parameters which I would like to set, such as a network model or centerline curve.  How may I access these purely through python?</li>
</ul>
<p>Thanks in advance for any advice.  Below you can find the specific error I’m getting alongside a screenshot of my current scene.</p>
<blockquote>
<p>centerline = slicer.util.getModuleLogic(‘ExtractCenterline’).extractCenterline(aorta_seg_1, end_pts)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Users/me/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/qt-scripted-modules/ExtractCenterline.py”, line 724, in extractCenterline<br>
raise ValueError(“Failed to compute centerline (no Voronoi diagram was generated)”)<br>
ValueError: Failed to compute centerline (no Voronoi diagram was generated)<br>
[VTK] Input port 0 of algorithm vtkvmtkCapPolyData (000001ABAF8E1500) has 0 connections but is not optional.<br>
[VTK] No points to subdivide<br>
[VTK] No points to subdivide<br>
[VTK] No points to subdivide<br>
[VTK] Warning: In vtkDelaunay3D.cxx, line 455<br>
[VTK] vtkDelaunay3D (000001ABA8D6B480): Cannot triangulate; no input points<br>
[VTK] Centerline extraction failed: could not compute surface normals</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b51326460809714945cce92149a98f4751df534e.png" data-download-href="/uploads/short-url/pPRrSWTGfOPHaPlbqgcwEKIciqq.png?dl=1" title="Screenshot 2023-09-06 at 1.16.23 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b51326460809714945cce92149a98f4751df534e_2_690x207.png" alt="Screenshot 2023-09-06 at 1.16.23 PM" data-base62-sha1="pPRrSWTGfOPHaPlbqgcwEKIciqq" width="690" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b51326460809714945cce92149a98f4751df534e_2_690x207.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b51326460809714945cce92149a98f4751df534e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b51326460809714945cce92149a98f4751df534e.png 2x" data-dominant-color="E7EDF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-06 at 1.16.23 PM</span><span class="informations">751×226 28.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2023-09-06 19:30 UTC)

<p>Here is how to get the segment you want:</p>
<pre><code class="lang-auto">segmentation = aorta_seg.GetSegmentation()
segmentID = segmentation.GetSegmentIDBySegmentName('Segment_1')
segment = segmentation.GetSegment(segmentID)
</code></pre>
<p>The VMTK inputs/outputs will take a bit more research and I just have time for this quick answer at the moment.</p>

---

## Post #3 by @wesselk (2023-09-06 19:43 UTC)

<p>Unfortunately the segment is not the right type:</p>
<blockquote>
<p>TypeError: SetInputData argument 1: method requires a vtkDataObject, a vtkSegment was provided.</p>
</blockquote>

---

## Post #4 by @mikebind (2023-09-06 22:48 UTC)

<p>OK, I looked a little deeper into the ExtractCenterline.py code, and I think what you need is the <code>vtkPolyData</code> for the closed surface representation of the segment.</p>
<pre><code class="lang-auto">segmentation = aorta_seg.GetSegmentation()
segmentID = segmentation.GetSegmentIDBySegmentName('Segment_1')
aorta_seg.CreateClosedSurfaceRepresentation() # just to ensure this representation exists
segmentVtkPolyData = vtk.vtkPolyData() # create empty vtkPolyData object
# Get vtkPolyData representation of segment surface into segmentVtkPolyData variable
aorta_seg.GetClosedSurfaceRepresentation(segmentID, segmentVtkPolyData)
</code></pre>
<p>For the rest of the details of how to use the VMTK centerline extraction from python inside Slicer, the best place to look is at the code from ExtractCenterline.py, available here: <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py" rel="noopener nofollow ugc">https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py</a></p>
<details>
<summary>
Some longer example code which might be helpful</summary>
<p>In some old code, I found a method from inside a custom scripted Slicer module I had developed which uses the ExtractCenterline module’s logic.</p>
<pre><code class="lang-auto">    def onGenerateCenterlineButtonClick(self):
        """Trying to mimic the implementation in ExtractCenterline.py from VMTK module"""
        qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)
        try:
            ## Gather inputs ##
            linkedAirwaySegmentationNode = self._parameterNode.GetNodeReference(
                "LinkedAirwaySegmentationNode"
            )
            linkedAirwaySegmentID = (
                self.ui.linkedAirwaySegmentSelectorWidget.currentSegmentID()
            )
            endPointsMarkupsNode = self._parameterNode.GetNodeReference(
                "EndpointsFiducialNode"
            )
            import ExtractCenterline

            extractLogic = ExtractCenterline.ExtractCenterlineLogic()
            ## Preprocess ##
            inputSurfacePolyData = extractLogic.polyDataFromNode(
                linkedAirwaySegmentationNode, linkedAirwaySegmentID
            )
            if (
                not inputSurfacePolyData
                or inputSurfacePolyData.GetNumberOfPoints() == 0
            ):
                raise ValueError("Valid input surface is required")
            # These are the default values in the VMTK module, which I have never had to change (until I ran into an error)
            # OK, now I've had to change decimationAggressiveness down to 3.5 from 4.0.  Preprocessed surface had inverted segments after decimation
            # which lead to failed centerline curve.  It is possible that we could detect failed curve if it has only two control points? (That was the
            # case in the single failure so far). If so, we could re-run with lower decimation aggressiveness.
            preprocessEnabled = True  # (self._parameterNode.GetParameter("PreprocessInputSurface") == "true")
            targetNumberOfPoints = 5000.0  # float(self._parameterNode.GetParameter("TargetNumberOfPoints"))
            decimationAggressiveness = 3.5  # 4.0 #float(self._parameterNode.GetParameter("DecimationAggressiveness"))
            subdivideInputSurface = False  # (self._parameterNode.GetParameter("SubdivideInputSurface") == "true")
            slicer.util.showStatusMessage(
                "Preprocessing surface before centerline extraction..."
            )
            slicer.app.processEvents()
            preprocessedPolyData = extractLogic.preprocess(
                inputSurfacePolyData,
                targetNumberOfPoints,
                decimationAggressiveness,
                subdivideInputSurface,
            )
            ## Extract centerline ##
            centerlineCurveNode = self._parameterNode.GetNodeReference(
                "CenterlineCurveNode"
            )
            if centerlineCurveNode is None:
                centerlineCurveNode = slicer.mrmlScene.AddNewNodeByClass(
                    "vtkMRMLMarkupsCurveNode", "Centerline curve"
                )
            slicer.util.showStatusMessage("Extracting centerline...")
            slicer.app.processEvents()  # force update
            centerlinePolyData, voronoiDiagramPolyData = extractLogic.extractCenterline(
                preprocessedPolyData, endPointsMarkupsNode
            )
            slicer.util.showStatusMessage(
                "Generating curves and quantification results table..."
            )
            slicer.app.processEvents()  # force update
            centerlinePropertiesTableNode = None
            extractLogic.createCurveTreeFromCenterline(
                centerlinePolyData, centerlineCurveNode, centerlinePropertiesTableNode
            )
            if centerlineCurveNode.GetNumberOfControlPoints() == 2:
                # Extraction had an error, likely due to too high decimation aggressiveness
                # Try again
                slicer.util.errorDisplay(
                    "Centerline generation failed, possibly due to decimationAggressiveness being too high."
                )
                # TODO TODO TODO: implement automatically trying again, with message to user about what's going on
        except Exception as e:
            slicer.util.errorDisplay("Failed to compute results: " + str(e))
            import traceback

            traceback.print_exc()
        qt.QApplication.restoreOverrideCursor()
        slicer.util.showStatusMessage("Centerline analysis complete.", 3000)
        self._parameterNode.SetNodeReferenceID(
            "CenterlineCurveNode", centerlineCurveNode.GetID()
        )
</code></pre>
</details>

---

## Post #5 by @wesselk (2023-09-13 22:41 UTC)

<p>Thank you Mike! Your input is very appreciated, with your help I was able to generate a centerline curve from command line.  I was hoping that understanding how to use one part of the vtmk module would make it easier for the next part, but I am stuck again for the cross section analysis tool.<br>
While referencing the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/CrossSectionAnalysis/CrossSectionAnalysis.py" rel="noopener nofollow ugc">CrossSectionAnalysis code</a> I found the functions process() and createMarksupCurve(), but neither of these are callable from CrossSectionAnalysisLogic() because of being NoneType.  I noticed the vital code for extractCenterlines was within an onApplyButton() function, but the CrossSectionAnalysis class does fancy stuff with widgets that has thrown me off.  Could you offer any more guidance around using these modules through code? Thanks again!</p>
<p>my code:</p>
<blockquote>
<p>logic = CrossSectionAnalysis.CrossSectionAnalysisLogic()<br>
input_surface_lumen_data = logic.lumenSurfaceNode(aorta_seg_node, aorta_seg_ID)<br>
slicer.app.processEvents()<br>
crosssection_curve = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsCurveNode”, “Cross-section curve”)<br>
crosssection_analysis_table_node = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTableNode”, “Centerline cross-sections”)</p>
</blockquote>

---

## Post #6 by @chir.set (2023-09-14 07:38 UTC)

<aside class="quote no-group" data-username="wesselk" data-post="5" data-topic="31596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/ac8455/48.png" class="avatar"> wesselk:</div>
<blockquote>
<p>While referencing the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/CrossSectionAnalysis/CrossSectionAnalysis.py" rel="noopener nofollow ugc">CrossSectionAnalysis code</a></p>
</blockquote>
</aside>
<p>You are pointing to a former module that <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/42" rel="noopener nofollow ugc">no longer exists</a> as such. Please consider the latest single module ‘Cross-section analysis’ in SlicerVMTK.</p>

---

## Post #7 by @mikebind (2023-09-14 14:26 UTC)

<p>This is the current code as referenced by <a class="mention" href="/u/chir.set">@chir.set</a> :  <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/CrossSectionAnalysis/CrossSectionAnalysis.py" rel="noopener nofollow ugc">https://github.com/vmtk/SlicerExtension-VMTK/blob/master/CrossSectionAnalysis/CrossSectionAnalysis.py</a><br>
Hopefully that will be helpful.  I have not ended up using the CrossSectionAnalysis module at all in my work so I don’t have any experience or outside code that uses it.  If you run into a specific problem, it’s fine to post back here and we’ll see if we can help.</p>

---

## Post #8 by @ruili (2024-01-29 17:58 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="31596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p><code>import ExtractCenterline</code></p>
</blockquote>
</aside>
<p>Hello,</p>
<p>I tried modifying your long code example to automatically extract centerline curves using python. However, I found that the extracted centerline curves are not labelled in the 3D view, but only in the slice views:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbefaaf4153bd0b81e39ad304803a2c6c2861f21.png" data-download-href="/uploads/short-url/vnE3dtHEIPvAvyZrImyXRHKDgfT.png?dl=1" title="Screenshot 2024-01-29 at 17.50.53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbefaaf4153bd0b81e39ad304803a2c6c2861f21_2_690x388.png" alt="Screenshot 2024-01-29 at 17.50.53" data-base62-sha1="vnE3dtHEIPvAvyZrImyXRHKDgfT" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbefaaf4153bd0b81e39ad304803a2c6c2861f21_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbefaaf4153bd0b81e39ad304803a2c6c2861f21_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbefaaf4153bd0b81e39ad304803a2c6c2861f21_2_1380x776.png 2x" data-dominant-color="575555"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-01-29 at 17.50.53</span><span class="informations">1920×1080 383 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is my code:</p>
<pre><code class="lang-auto">import vtk
import slicer
import ExtractCenterline

end_pts = slicer.util.loadMarkups("endpoints.json")

vessel_seg = slicer.util.loadSegmentation("segmentation.nii.gz")
segmentation = vessel_seg.GetSegmentation()
segmentation.SetConversionParameter("Smoothing factor", "0.1")

vessel_seg.CreateClosedSurfaceRepresentation() # This creates the 3D view
segmentID = segmentation.GetSegmentIdBySegmentName('Segment_1')
segmentVtkPolyData = vtk.vtkPolyData() # create empty vtkPolyData object
vessel_seg.GetClosedSurfaceRepresentation(segmentID, segmentVtkPolyData) # Get vtkPolyData representation of segment surface into segmentVtkPolyData variable


### Extract Centerline ###
extractLogic = ExtractCenterline.ExtractCenterlineLogic()

## Preprocess ##
inputSurfacePolyData = extractLogic.polyDataFromNode(vessel_seg, segmentID)

preprocessEnabled = True  # (self._parameterNode.GetParameter("PreprocessInputSurface") == "true")
targetNumberOfPoints = 15000.0  # float(self._parameterNode.GetParameter("TargetNumberOfPoints"))
decimationAggressiveness = 4.0 #float(self._parameterNode.GetParameter("DecimationAggressiveness"))
subdivideInputSurface = False  # (self._parameterNode.GetParameter("SubdivideInputSurface") == "true")
slicer.util.showStatusMessage(
    "Preprocessing surface before centerline extraction..."
)
slicer.app.processEvents()
preprocessedPolyData = extractLogic.preprocess(
    inputSurfacePolyData,
    targetNumberOfPoints,
    decimationAggressiveness,
    subdivideInputSurface,
)
## Extract centerline ##
centerlineCurveNode = None
if centerlineCurveNode is None:
    centerlineCurveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode", "Centerline curve")

slicer.util.showStatusMessage("Extracting centerline...")
slicer.app.processEvents()  # force update
centerlinePolyData, voronoiDiagramPolyData = extractLogic.extractCenterline(
        preprocessedPolyData, end_pts, curveSamplingDistance=0.001)
slicer.util.showStatusMessage(
    "Generating curves and quantification results table..."
)
slicer.app.processEvents()  # force update

centerlinePropertiesTableNode = None


extractLogic.createCurveTreeFromCenterline(
    centerlinePolyData, centerlineCurveNode, centerlinePropertiesTableNode
)
if centerlineCurveNode.GetNumberOfControlPoints() == 2:
    # Extraction had an error, likely due to too high decimation aggressiveness
    # Try again
    slicer.util.errorDisplay(
        "Centerline generation failed, possibly due to decimationAggressiveness being too high."
    )
</code></pre>
<p>Do you have any insights on what might be causing this display error? Moreover, how can I also generate the ‘Centerline Model’ (the model including all the centerline branches and usually displayed in green in the output from the ExtractCenterline extension)?</p>
<p>Many thanks in advance!</p>
<p>Rui</p>

---

## Post #9 by @mikebind (2024-01-29 19:29 UTC)

<p>This section of ExtractCenterline.py shows how the centerline model is generated from the centerlinePolyData:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L288-L302">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L288-L302" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L288-L302" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L288-L302</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="288" style="counter-reset: li-counter 287 ;">
          <li>centerlineModelNode = self._parameterNode.GetNodeReference("CenterlineModel")</li>
          <li>centerlineCurveNode = self._parameterNode.GetNodeReference("CenterlineCurve")</li>
          <li>centerlinePropertiesTableNode = self._parameterNode.GetNodeReference("CenterlineProperties")</li>
          <li>voronoiDiagramModelNode = self._parameterNode.GetNodeReference("VoronoiDiagram")</li>
          <li>if centerlineModelNode or centerlineCurveNode or centerlinePropertiesTableNode or voronoiDiagramModelNode:</li>
          <li>    slicer.util.showStatusMessage("Extract centerline...")</li>
          <li>    slicer.app.processEvents()  # force update</li>
          <li>    centerlinePolyData, voronoiDiagramPolyData = self.logic.extractCenterline(preprocessedPolyData, endPointsMarkupsNode)</li>
          <li>if centerlineModelNode:</li>
          <li>    centerlineModelNode.SetAndObserveMesh(centerlinePolyData)</li>
          <li>    if not centerlineModelNode.GetDisplayNode():</li>
          <li>        centerlineModelNode.CreateDefaultDisplayNodes()</li>
          <li>        centerlineModelNode.GetDisplayNode().SetColor(0.0, 1.0, 0.0)</li>
          <li>        centerlineModelNode.GetDisplayNode().SetLineWidth(3)</li>
          <li>        inputSurfaceModelNode.GetDisplayNode().SetOpacity(0.4)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For the display of the names in the 3D view, I am guessing that something else is obscuring the markups curves (perhaps the voronoi diagram model, or a centerline curve tree model?).  It is possible to get the markups curve “Properties label”  to show only on the slice views and not in 3D, but it requires setting up multiple display nodes and tuning which views each display node applies to.  Since you haven’t done that, the most likely explanation is that something is hiding the markups curves in the 3D view.  Try hiding all other elements in the scene except for one of the markups curves (especially all models) and see if you can see the labels then.</p>

---

## Post #10 by @ruili (2024-02-03 16:00 UTC)

<p>Thanks! I tried hidding all the elements, but there is still no label of the branches in the 3D view. However, after running multiple experiments directly from the ExtractCenterline module on the 3D Slicer software, I found that whether a branch gets labelled in the 3D view seems to depend on whether it is visible in the 3D view at the moment when you are running the centerline extraction process (after you click “Apply”). If it was hidden, then there will be no label for it even after extracting the centerline and branches. Similarly, when I ran centerline extraction purely from my python script, technically no branch was visible in the 3D view, so in the end none of them was labelled.<br>
It seems that the display setting is just not updated after extracting the branches.</p>

---

## Post #11 by @ruili (2024-02-07 14:43 UTC)

<p>Hi! I also found out that if I save the centerline curves in a mrml scene file, or just .mrk.json file, when I reload the files, the labels for the curves are not showing. I am struggling to figure out how I can let it show the label in 3D Slicer, and how I can perhaps change the saved .mrk.json file so that when it’s loaded the labels can show. Do you have any idea how to solve these problems?</p>

---

## Post #12 by @mikebind (2024-02-07 23:38 UTC)

<p>Hmm, that does seem like odd behavior.  If you want to chase this down further, I would try examining</p>
<ol>
<li>whether the curves end up with multiple display nodes associated with them (<code>myCurveNode.GetNumberOfDisplayNodes()</code>),</li>
<li>whether they are independently assigned to be visible only in certain views (check <code>myCurveNode.GetNthDisplayNode(0).GetViewNodeIDs()</code>, where an empty list means "show in all views), and</li>
<li>what the current visibility setting is for the curve label (<code>myDisplayNode.GetPropertiesLabelVisibility()</code>) . This setting should also be being saved in the .mrk.json file, so you can see if that seems like it is the case, and you can also try turning it off and back on and then save to see if that triggers an update which is then recorded in the saved file.</li>
</ol>

---

## Post #13 by @ruili (2024-02-15 18:03 UTC)

<p>Here are the outputs to your suggested commands:</p>
<blockquote>
<p><code>myCurveNode.GetNumberOfDisplayNodes()</code></p>
</blockquote>
<p><code>1</code></p>
<blockquote>
<p><code>myCurveNode.GetNthDisplayNode(0).GetViewNodeIDs()</code></p>
</blockquote>
<p><code>()</code></p>
<blockquote>
<p><code>myDisplayNode = myCurveNode.GetNthDisplayNode(0)</code><br>
<code>myDisplayNode.GetPropertiesLabelVisibility()</code></p>
</blockquote>
<p><code>True</code></p>
<p>It seems like all the outputs are as expected, but the centerline curve labels are still only showing in the slice views and not in the 3D view. Do you have any thoughts on this?</p>

---

## Post #14 by @mikebind (2024-02-15 21:54 UTC)

<p>I agree, those are the expected outputs.  It looks to me like you may have found a bug.  If you can generate and share a minimal example which reproduces the problematic behavior that would be very helpful to anyone who is trying to find the source of the problem.  As it is, we are now deeper in than I will likely be able to troubleshoot.  I would suggest starting a new topic (this one is marked solved so probably has less visibility) on this forum with a clean description and example of how to reproduce the issue, and also file a bug report, though it is not clear to me whether the bug is present in VMTK, Slicer, or possibly vtk.  You can link back to this discussion for details on things you’ve checked already.</p>

---

## Post #15 by @ruili (2024-02-16 14:39 UTC)

<p>Sure! I have posted this potential bug in a separate post <a href="https://discourse.slicer.org/t/slicer-3d-view-not-displaying-labels-of-markup-curves-properly/34364">here</a>.</p>

---

## Post #16 by @pc666nice (2024-12-27 08:49 UTC)

<p>Hi, have you solved this problem? Now I can generate centerline after reading the .stl files and using the python code, but only the Centerline Curve node appeared without the Centerline model node, how can I obtain the Centerline model node and save the model as .vtp file?</p>

---

## Post #17 by @ruili (2024-12-28 14:29 UTC)

<p>Hi! Sorry I’m not sure about this, as later on I found that I did not need the centerline model node for my work. Does this code here: <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L288-L302" class="inline-onebox" rel="noopener nofollow ugc">SlicerExtension-VMTK/ExtractCenterline/ExtractCenterline.py at 3787ea4a300da28ec5f0824f0715f2713b631155 · vmtk/SlicerExtension-VMTK · GitHub</a> as referenced by <a class="mention" href="/u/mikebind">@mikebind</a> help?</p>

---
