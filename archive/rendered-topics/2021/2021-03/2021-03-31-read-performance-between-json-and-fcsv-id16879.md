---
topic_id: 16879
title: "Read Performance Between Json And Fcsv"
date: 2021-03-31
url: https://discourse.slicer.org/t/16879
---

# Read performance between json and fcsv

**Topic ID**: 16879
**Date**: 2021-03-31
**URL**: https://discourse.slicer.org/t/read-performance-between-json-and-fcsv/16879

---

## Post #1 by @muratmaga (2021-03-31 17:07 UTC)

<p>I have the same markups file with many points saved as fcsv and json. Reading the same file via JSON is instantenous, whereas fcsv takes minutes. This replicates all the time in the windows table. Files are here:</p>
<p><a href="https://app.box.com/s/chydl0iv3pvoq6o4x6cx1wme5n779789" class="onebox" target="_blank" rel="noopener">https://app.box.com/s/chydl0iv3pvoq6o4x6cx1wme5n779789</a></p>

---

## Post #2 by @lassoan (2021-04-01 13:55 UTC)

<p>We use a highly optimized json parser library (rapidjson) while fcsv files are just read by a custom parser, so such performance differences are expected.</p>
<p>We should not use fcsv files at all, but we should support importing/exporting csv files instead. For standard csv files we could use fast csv parsers, such as in pandas.</p>

---

## Post #3 by @muratmaga (2021-04-01 17:54 UTC)

<p>I don’t like the idea of exporting csv’s because it is even more lossy than fcsv. Given that fcsv are essentially csv with headers, can’t we find a middle ground where the specialized parser only reads the header and pandas is used to read the rest?</p>

---

## Post #4 by @lassoan (2021-04-02 12:34 UTC)

<p>You can store anything that you need in a csv file. Only those properties cause complications that are common the all control points, but you can store that in either a separate csv file or repeat the value for each control point.</p>
<p>Alternatively, you can parse the special fcsv header and after you determined the columns and the number of first lines that are skip, you can read the rest using pandas.</p>
<p>What is your use case? How did you end up with with a large fcsv file?</p>

---

## Post #5 by @muratmaga (2021-04-02 15:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="16879">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is your use case? How did you end up with with a large fcsv file?</p>
</blockquote>
</aside>
<p>We generate large number of landmarks via the tools in SlicerMorph (e.g., PseudoLMGenerator, or PlaceSemiLMPatches) for shape analysis. While we try to steer our users towards JSON pointing out to issues with fcsv, due to both community and paper reviewer requests we need to continue to support FCSV.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="16879">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Alternatively, you can parse the special fcsv header and after you determined the columns and the number of first lines that are skip, you can read the rest using pandas.</p>
</blockquote>
</aside>
<p>Yes, that’s exactly the solution. But I would like to see this done at the core Slicer level.</p>

---

## Post #6 by @lassoan (2021-04-03 01:16 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="16879">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Yes, that’s exactly the solution. But I would like to see this done at the core Slicer level.</p>
</blockquote>
</aside>
<p>It would be too much effort fixing and maintaining fcsv as a data saving/loading format (format that allows lossless storage). How would you save all display properties, measurement results, store multiple markups in a single file, etc. while maintaining backward compatibility? It would be practically impossible to use csv-based format for this.</p>
<p>CSV as export/import format can be very useful, but proper generic implementation (field chooser, etc.) would be a lot of time to implement and would never be as convenient as specialized exporters/importers (that allow loading markups to/from well-established standard csv-based file formats).</p>
<p>If you can get funding for developing a generic markup csv importer/exporter then it should be OK to keep it in the Slicer core, but it is more convenient for users and less work for developers if efforts are focused on implementing domain-specific csv importers/exporters in extensions.</p>

---

## Post #7 by @pieper (2021-04-03 15:12 UTC)

<p>The performance differences when loading the two datasets is pretty striking and there’s clearly a bug in the fcsv loading code.  When I sample the process using the ActivityMonitor on macOS it shows that 95% of the time is in <code>vtkMRMLDisplayNode::UpdateScalarRange()</code> on each point insert, which leads to a parametric curve evaluation even though these are fiducials and not curves.  So the logic needs some work.</p>
<p>I filed an issue to track it.</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5564" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5564" target="_blank" rel="noopener">fcsv files are slow to load due to extra computation</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-04-03" data-time="15:11:45" data-timezone="UTC">03:11PM - 03 Apr 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">See: https://discourse.slicer.org/t/read-performance-between-json-and-fcsv
There is a lot of updating of display nodes (scalar range and parametric curves) each time a point is inserted.
Steps...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto">    +                                                                                       783 vtkSlicerMarkupsLogic::LoadMarkups(char const*, char const*)  (in libvtkSlicerMarkupsModuleLogic.dylib) + 1381  [0x15b7c3145]
    +                                                                                         783 vtkSlicerMarkupsLogic::LoadMarkupsFromFcsv(char const*, char const*)  (in libvtkSlicerMarkupsModuleLogic.dylib) + 1202  [0x15b7c3e32]
    +                                                                                           783 vtkMRMLStorageNode::ReadData(vtkMRMLNode*, bool)  (in libMRMLCore.dylib) + 253  [0x10ecf2f9d]
    +                                                                                             782 vtkMRMLMarkupsFiducialStorageNode::ReadDataInternal(vtkMRMLNode*)  (in libvtkSlicerMarkupsModuleMRML.dylib) + 3691  [0x15b026b0b]
    +                                                                                             ! 759 vtkMRMLMarkupsFiducialStorageNode::SetPointFromString(vtkMRMLMarkupsNode*, int, char const*)  (in libvtkSlicerMarkupsModuleMRML.dylib) + 3464  [0x15b024238]
    +                                                                                             ! : 747 vtkMRMLMarkupsNode::SetNthControlPointPosition(int, double, double, double, int)  (in libvtkSlicerMarkupsModuleMRML.dylib) + 371  [0x15b04c8c3]
    +                                                                                             ! : | 746 vtkMRMLDisplayNode::UpdateScalarRange()  (in libMRMLCore.dylib) + 23  [0x10ebb2fb7]
    +                                                                                             ! : | + 746 vtkMRMLMarkupsDisplayNode::GetScalarDataSet()  (in libvtkSlicerMarkupsModuleMRML.dylib) + 114  [0x15b020122]
    +                                                                                             ! : | +   746 vtkMRMLMarkupsNode::GetCurveWorld()  (in libvtkSlicerMarkupsModuleMRML.dylib) + 48  [0x15b04ecc0]
    +                                                                                             ! : | +     744 vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 283  [0x11de507ab]
    +                                                                                             ! : | +     ! 744 vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 706  [0x11de50242]
    +                                                                                             ! : | +     !   719 vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 792  [0x11de29758]
    +                                                                                             ! : | +     !   : 719 vtkCompositeDataPipeline::ForwardUpstream(vtkInformation*)  (in libvtkCommon-8.2.1.dylib) + 297  [0x11de25d59]
    +                                                                                             ! : | +     !   :   719 vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 706  [0x11de50242]
    +                                                                                             ! : | +     !   :     719 vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 1175  [0x11de298d7]
    +                                                                                             ! : | +     !   :       719 vtkCompositeDataPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 107  [0x11de24b1b]
    +                                                                                             ! : | +     !   :         718 vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 61  [0x11de2a13d]
    +                                                                                             ! : | +     !   :         | 718 vtkExecutive::CallAlgorithm(vtkInformation*, int, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 69  [0x11de2f515]
    +                                                                                             ! : | +     !   :         |   717 vtkCurveGenerator::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkSlicerMarkupsModuleMRML.dylib) + 289  [0x15b0601a1]
    +                                                                                             ! : | +     !   :         |   + 717 vtkCurveGenerator::GeneratePoints(vtkPoints*, vtkPolyData*, vtkPolyData*)  (in libvtkSlicerMarkupsModuleMRML.dylib) + 139  [0x15b06026b]
    +                                                                                             ! : | +     !   :         |   +   666 vtkCurveGenerator::GeneratePointsFromFunction(vtkPoints*, vtkPoints*, vtkDoubleArray*)  (in libvtkSlicerMarkupsModuleMRML.dylib) + 636  [0x15b06278c]
    +                                                                                             ! : | +     !   :         |   +   ! 635 vtkParametricSpline::Evaluate(double*, double*, double*)  (in libvtkCommon-8.2.1.dylib) + 53  [0x11de66ff5]
    +                                                                                             ! : | +     !   :         |   +   ! : 211 vtkParametricSpline::Initialize()  (in libvtkCommon-8.2.1.dylib) + 2504  [0x11de67ab8]
    +                                                                                             ! : | +     !   :         |   +   ! : | 138 vtkPiecewiseFunction::AddPoint(double, double, double, double)  (in libvtkCommon-8.2.1.dylib) + 780  [0x11dcf0a9c]
    +                                                                                             ! : | +     !   :         |   +   ! : | + 57 void std::__1::__sort&lt;vtkPiecewiseFunctionCompareNodes&amp;, vtkPiecewiseFunctionNode**&gt;(vtkPiecewiseFunctionNode**, vtkPiecewiseFunctionNode**, vtkPiecewiseFunctionCompareNodes&amp;)  (in libvtkCommon-8.2.1.dylib) + 524,556,...  [0x11dcf2fac,0x11dcf2fcc,...]
</code></pre>

---
