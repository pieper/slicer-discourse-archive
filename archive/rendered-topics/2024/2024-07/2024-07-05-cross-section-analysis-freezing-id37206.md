---
topic_id: 37206
title: "Cross Section Analysis Freezing"
date: 2024-07-05
url: https://discourse.slicer.org/t/37206
---

# Cross Section Analysis Freezing

**Topic ID**: 37206
**Date**: 2024-07-05
**URL**: https://discourse.slicer.org/t/cross-section-analysis-freezing/37206

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-07-05 08:02 UTC)

<p>Hi all.</p>
<p>We automatizated the cross section analysis computation for our own centerlines.</p>
<p>The program runs  like this:</p>
<pre><code class="lang-auto">def obtainDataFromGeometry(segmentationNode, segmentID, branchID, G, centerlinesDict, tableNode, 
                 fileToSaveResults, createFile):

    """
    Runs CrossSectionAnalysis and genrates a file with
    - Centerline ID
    - Centerline branch ID
    - Node ID
    - Distance
    - Diameter
    - Area
    - Curvature
    - RAS coordinates 
    
    :segmentationNode: segmentation node where the geometry is
    :segmentID: the segment name we want to operate with
    :branchID: indicates the coronary branch ('left' or 'right')
    :centerlinesDict: a dictionary with key "centerline name" and value list of 
            nodeIDs of the centerline
    :tableNode: 'vtkMRMLTableNode' to save auxiliary results
    :fileToSaveResults: path to file where to save results
    :createFile: if True, generates a new file to save resutls. If False, appends results to file
    
    :return: creates a file in fileToSaveResults with the metadata
    """
    
    logic = CrossSectionAnalysis.CrossSectionAnalysisLogic()
    
    segmentNodeID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentID)
    
    # Set lumen surface
    logic.setLumenSurface(segmentationNode, segmentNodeID)
    
    # Set table node
    logic.setOutputTableNode(tableNode)
    
    # To obtain RAS coordinates in different cols
    logic.coordinateSystemColumnSingle = False
    
    # Set centerline node
    centerlineNames = list(centerlinesDict.keys()) # utils.getCurveNames(centerlinesPrefix)
    
    if(createFile): # We create a new file
        with open(fileToSaveResults, "w") as file:
            file.write("CenterlineID,branchID,nodeID,Distance,Diameter(CE),Cross-sectionArea,Curvature,R,A,S\n")
    
    
    for centerlineID in centerlineNames:
        print("Extracting metadata info from " + str(centerlineID) + "...")
        
        # Find nodes 
        # numberOfValues = tableNode.GetTable().GetColumn(0).GetNumberOfValues()
        numberOfValues = len(centerlinesDict[centerlineID])
        
        # If the curve has less than 3 points, cross section analysis crashes
        doCrossSection = False
        if(numberOfValues &gt; 2):
            doCrossSection = True
        
        if (doCrossSection):
            # avoids interpolating points
            slicer.util.getNode(centerlineID).SetNumberOfPointsPerInterpolatingSegment(1) 
            
            logic.setInputCenterlineNode(slicer.util.getNode(centerlineID))
            
            # Run CrossSectionAnalysis
            logic.run()
</code></pre>
<p>The issue we see few times is the following one:</p>
<ul>
<li>
<p>If the scene is created and saved and we use this routine in a new Slicer window where we open the saved scene, the function sometimes freezes extracting radius and other parameters. The function blocks the interface:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63eafafccf2ba463da45cbe09bec9499c73d1098.jpeg" data-download-href="/uploads/short-url/efUIc0Ow3FUX8FnkUw93FmqQqtG.jpeg?dl=1" title="Captura de pantalla 2024-07-05 095440" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63eafafccf2ba463da45cbe09bec9499c73d1098_2_690x415.jpeg" alt="Captura de pantalla 2024-07-05 095440" data-base62-sha1="efUIc0Ow3FUX8FnkUw93FmqQqtG" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63eafafccf2ba463da45cbe09bec9499c73d1098_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63eafafccf2ba463da45cbe09bec9499c73d1098_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63eafafccf2ba463da45cbe09bec9499c73d1098_2_1380x830.jpeg 2x" data-dominant-color="B3B4BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-07-05 095440</span><span class="informations">1913×1153 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>This problem is not seemed yet when we run the the function in the same Slicer window, but we do not rule out the possibility of happen here too.</p>
</li>
</ul>
<p>Thanks a lot for the help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> .</p>

---

## Post #2 by @chir.set (2024-07-05 08:13 UTC)

<p>Can you share an MRB file so as to reproduce and debug this over the weekend? Only reproducible execution pathways can be solved. What Slicer version are you using? Which OS?</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2024-07-05 08:34 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Only reproducible execution pathways can be solved</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/chir.set">@chir.set</a>, what is a MRB File? We usually work with mrml files… We are using 3D Slicer 5.6.2 version, in Windows 11.  I would try to send you the scene without the images and then I will try to reproduce the error. If the error occurs in the scene without images I can send you whatever you need.</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @chir.set (2024-07-05 09:31 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="3" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>what is a MRB File?</p>
</blockquote>
</aside>
<p>You can select an MRB file in the ‘Save dialog’, it’s a ZIP archive that includes anything in your scene that can be saved.</p>
<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="3" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>without the images</p>
</blockquote>
</aside>
<p>If you mean the volume node, it can be omitted. The segmentation and the centerlines must be included however. Your code is already online.</p>

---

## Post #5 by @SANTIAGO_PENDON_MING (2024-07-05 09:51 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="4" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>t an MRB file in the ‘Save dialog’, it’s a ZIP archive that includes anything in your scene that can be saved.</p>
</blockquote>
</aside>
<p>Okay, how can I share you this file?</p>
<p>Pd: We tried using the function without saving and opening the scene and it also freezes…</p>

---

## Post #6 by @chir.set (2024-07-05 10:38 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="5" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>Okay, how can I share you this file?</p>
</blockquote>
</aside>
<p>You can use any <a href="https://yandex.com/search/?text=online+file+sharing+services&amp;lr=112068" rel="noopener nofollow ugc">online</a> file sharing services like Yandex disk, Google drive…</p>

---

## Post #7 by @SANTIAGO_PENDON_MING (2024-07-05 10:47 UTC)

<p>Okay, I think this should work:</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/14GGGxZf7JDOFPttMwpkifjvgTNLmrsY7/view">
  <header class="source">

      <a href="https://drive.google.com/file/d/14GGGxZf7JDOFPttMwpkifjvgTNLmrsY7/view" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/14GGGxZf7JDOFPttMwpkifjvgTNLmrsY7/view" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/14GGGxZf7JDOFPttMwpkifjvgTNLmrsY7/view" target="_blank" rel="noopener nofollow ugc">2_Slicer.mrb</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @chir.set (2024-07-05 10:48 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p><code>centerlineNames = list(centerlinesDict.keys()) # utils.getCurveNames(centerlinesPrefix)</code></p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p><code>numberOfValues = len(centerlinesDict[centerlineID])</code></p>
</blockquote>
</aside>
<p>How is <em>centerlinesDict</em> structured? What is pointed by <em>centerlinesDict[centerlineID]</em>?</p>

---

## Post #9 by @SANTIAGO_PENDON_MING (2024-07-05 11:18 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p><code>en(centerlinesDict[centerlineID])</code></p>
</blockquote>
</aside>
<p><em>centerlinesDict</em> is a dictionary which contains the centerline names as keys, and the list of nodes as values for each centerline.</p>
<p><code>numberOfValues = len(centerlinesDict[centerlineID])</code> is the number of nodes of the selected centerline.</p>

---

## Post #10 by @chir.set (2024-07-05 14:38 UTC)

<p>This code just works: first time, repeat run in same scene, in recreated scenes, after closing and restarting Slicer, i.e, always.</p>
<p>i</p>
<pre><code class="lang-auto">import CrossSectionAnalysis
logic = CrossSectionAnalysis.CrossSectionAnalysisLogic()

segmentation = getNode("Segmentacion")
segmentId = segmentation.GetSegmentation().GetSegmentIdBySegmentName("Paciente")
centerlines = slicer.util.getNodesByClass("vtkMRMLMarkupsCurveNode")

logic.setLumenSurface(segmentation, segmentId)
logic.coordinateSystemColumnSingle = False
# table = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
table = getNode("Table_4")
logic.setOutputTableNode(table)

for centerline in centerlines:
    centerline.SetNumberOfPointsPerInterpolatingSegment(1)
    logic.setInputCenterlineNode(centerline)
    logic.run()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05afa33e2f07edae6a1777aeb44f867295ba8282.png" data-download-href="/uploads/short-url/OiGJK9QBMRjtq7X4c0rzSwM7Pc.png?dl=1" title="csa_check" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05afa33e2f07edae6a1777aeb44f867295ba8282_2_690x384.png" alt="csa_check" data-base62-sha1="OiGJK9QBMRjtq7X4c0rzSwM7Pc" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05afa33e2f07edae6a1777aeb44f867295ba8282_2_690x384.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05afa33e2f07edae6a1777aeb44f867295ba8282_2_1035x576.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05afa33e2f07edae6a1777aeb44f867295ba8282_2_1380x768.png 2x" data-dominant-color="2A2A27"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">csa_check</span><span class="informations">2510×1400 480 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Looking at your code, there seem to be confusion between ‘number of points’ and ‘number of centerlines’:</p>
<pre><code class="lang-auto">numberOfValues = len(centerlinesDict[centerlineID])
...
# If the curve has less than 3 points, cross section analysis crashes
...
    if(numberOfValues &gt; 2):
</code></pre>
<p>because you precise:</p>
<p><code>centerlinesDict is a dictionary which contains the centerline names as keys, and the list of nodes as values for each centerline</code></p>
<p>This is confusing, it suggests that one key references a collection of centerline curves. Is it a simple</p>
<blockquote>
<p>dict[“centerlineName”] = centerlineNode</p>
</blockquote>
<p>mapping?</p>
<p>Regardless, if</p>
<blockquote>
<p>slicer.util.getNode(centerlineID)</p>
</blockquote>
<p>returns a curve node, it should not hang.</p>
<p>You seem to be getting the curves using a custom function in your project:</p>
<p><code># utils.getCurveNames(centerlinesPrefix)</code></p>
<p>Check whether all nodes in centerlinesDict for a given key is a curve; for example:</p>
<blockquote>
<p>print(centerlineID, slicer.util.getNode(centerlineID).GetClassName())</p>
</blockquote>
<p>It does not hang on my system (Linux) in any circumstances. In general, it’s user code, or some particulars of your system.</p>

---

## Post #11 by @SANTIAGO_PENDON_MING (2024-07-09 13:35 UTC)

<p>Hi <a class="mention" href="/u/chir.set">@chir.set</a> we have been testing the functions (your version and also our version). The behaviour seemed was:</p>
<p>· Both functions works when we execute it alone in Python’s terminal in Slicer.</p>
<p>· None of them works when we execute it in the whole routine. This routine contains the following steps:</p>
<p>With a button driven interface we generate the centerlines, smooth them and let the user modify it (with the same name per each centerline node). Then the centerlines are removed and re-generated using the modified points. Once this process is done, we call the  function you provide and Slicer hangs.</p>
<p>This routine sometimes works and sometimes hangs depending on the geometry and the centerlines. We also see that the message ‘Waiting for background jobs…’ is related with taking the geometry.</p>
<p>Do you spot any possible mistake here?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #12 by @chir.set (2024-07-09 14:41 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="11" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>any possible mistake</p>
</blockquote>
</aside>
<p>That’s hard to say without seeing the full routine that you can’t obviously disclose (no problem with this).</p>
<p>Since your code works in the Python console too, and not in your routine, the problem remains in the way your code is using CrossSectionAnalysis.</p>
<p>You are repurposing the centerline curves, namely smoothing the curve and recreating points. The initial points are associated with scalar arrays coming right from VMTK and ‘Extract centerline’. If you do not end up with the same number of points and/or if their coordinates change (they will change), the scalar arrays will be out-of-sync with the curve. Your curves miss the important ‘Radius’ array for example. They are being used as arbitrary curves, which is perfectly legitimate too.</p>
<p>Have the curves in your sample file online been repurposed already?</p>
<p>The perpetual ‘Waiting for background jobs…’ message indicates that execution instance is still in the C++ pathway, probably in an infinite loop (and probably with a high CPU load). It contains 2 ‘<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/5053cbf2bd0d60a733a4027324ef8b5f43496a1c/CrossSectionAnalysis/Logic/vtkCrossSectionCompute.cxx#L171" rel="noopener nofollow ugc">for</a>’ loops that you could debug so as to understand further. Please note that the scalar arrays of the centerline curves are not used by this C++ code.</p>

---

## Post #13 by @chir.set (2024-07-09 15:13 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="11" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>any possible mistake</p>
</blockquote>
</aside>
<p>I just noticed that your curves in the sample online file are of ‘Linear’  type. The curve is processed by vtkParallelTransportFrame in the C++ pathway to generate tangents along a spline, which is the default type for a markups curve. I don’t know how much this processing may be related with the hangs you are observing. Try with curves of ‘Spline’ type.</p>

---

## Post #14 by @SANTIAGO_PENDON_MING (2024-07-09 17:42 UTC)

<p>Hi <a class="mention" href="/u/chir.set">@chir.set</a> , by parts:</p>
<p>· We didn’t notice high CPU usage (by the way is very low)<br>
· Indeed, our centerlines in the online example were modified and processed.<br>
· We don’t use extract centerlines, so we create in each iteration the centerlines from arrays.<br>
· Our centerlines are Linear type, yes, and we use the command: <code>curve_node.SetCurveTypeToLinear()</code>. We don’t know how to create centerlines with ‘Spline’, cause is not an option in SetCurveType functions.</p>
<p>We thank a lot your help.</p>

---

## Post #15 by @SANTIAGO_PENDON_MING (2024-07-10 08:06 UTC)

<p>We were exploring and reading the problematic function <code>vtkCrossSectionCompute::UpdateTable </code> in <code>vtkCrossSectionCompute.cxx</code> and the only possibility we manage now is that the thread is never free to be selected, so the module waits indef for it or problems in synchronization between the main thread and the workers threads.</p>
<p>This could be weird because the only execution the big routine do different with execute directly the function in the terminal is keep in the slicer interface a qt dockInterfaceWidget (no subprocess are running during CSAnalysis) and the usage of CPU is quite low (less than 10% before start the CSAnalysis). The memory remains low too, around the 50% of the total memory available is used.</p>
<p>At this point we are concern with the problem and don’t know what to do.</p>

---

## Post #16 by @chir.set (2024-07-10 09:52 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="15" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>the thread is never free to be selected</p>
</blockquote>
</aside>
<p>I don’t really understand what it means. Joinable threads are spawn, the main thread will wait for their completion. Each thread will stop when there’s nothing more to process. The main thread cannot ‘select’ a running thread to release/free it AFAIU.</p>
<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="15" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>At this point we are concern with the problem and don’t know what to do.</p>
</blockquote>
</aside>
<p>Me too, me too… All I can say is that it’s an out-of-intent/design usage. If you can find a solution that can satisfy your specific requirements without breaking anything, it can be further considered.</p>

---

## Post #17 by @SANTIAGO_PENDON_MING (2024-07-10 11:03 UTC)

<p>We saw a completely arbitrary behavior in the well procedure or not in this function:</p>
<p>If we make some minimal changes in the geometry, like minimal smoothings or cut a little bit ends of some vessels, it looks to work again sometimes… A completely no sense…</p>
<p>Thank for your help in this process.</p>
<p>PD: could you tell us how to make our centerlines ‘Spline’?</p>

---

## Post #18 by @chir.set (2024-07-10 11:54 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="17" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>could you tell us how to make our centerlines ‘Spline’?</p>
</blockquote>
</aside>
<p>Since your centerlines are created outside of Slicer, I can’t really say how to draw them as spline.</p>
<p>In Slicer, the spline is the default curve type. As you know the coordinates of your centerline points, you just have to add points to a newly created curve:</p>
<pre><code class="lang-auto">mycurve = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
mycurve.AddControlPointWorld(0.0, 0.0, 0.0)
</code></pre>

---

## Post #19 by @SANTIAGO_PENDON_MING (2024-10-07 10:35 UTC)

<p>Hi, today I want to try again solve this topic.</p>
<p>I discovered something interesting: When CSA can’t intersect with the segment the module falls in a continuous ‘Waiting for background jobs’ and crash Slicer.</p>
<p>To avoid this I guess that check all the points are inside the segment before execute the CSA would be a solution, but the module shouldn’t crash for it also.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2bfb89126f784d2c7fe5534f297f73d1601f620.png" data-download-href="/uploads/short-url/ndK6QHNf9e0sHmdmyJV4tkAGby8.png?dl=1" title="Captura de pantalla 2024-10-07 123254" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2bfb89126f784d2c7fe5534f297f73d1601f620_2_627x500.png" alt="Captura de pantalla 2024-10-07 123254" data-base62-sha1="ndK6QHNf9e0sHmdmyJV4tkAGby8" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2bfb89126f784d2c7fe5534f297f73d1601f620_2_627x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2bfb89126f784d2c7fe5534f297f73d1601f620_2_940x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2bfb89126f784d2c7fe5534f297f73d1601f620_2_1254x1000.png 2x" data-dominant-color="B1B1B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-10-07 123254</span><span class="informations">1330×1059 35.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If anyone has more ideas to avoid crashes or some Slicer/VMTK developer reads this, it would be great if they share any opinions or solutions.</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #20 by @SANTIAGO_PENDON_MING (2024-10-07 11:48 UTC)

<p>Hi <a class="mention" href="/u/chir.set">@chir.set</a> , thanks for the quick answer <a href="https://discourse.slicer.org/t/run-cross-section-analysis-with-models/39561/2">here</a> .</p>
<p>The version is 3D Slicer 5.6.2 running on Window 11</p>
<p>The logs displayed in the slicers prompt I can’t share it because CSA blocks the interface.</p>
<p>The toy scene to show the questions and the problematic behaviour (for sure produced by a problematic input) is here: <a href="https://drive.google.com/drive/folders/1ABx1OPexRbRB878qazw2ymFmHqHPZYOD?usp=sharing" rel="noopener nofollow ugc">Scene</a>.</p>
<p>The ‘bad’ segment causes ‘Waiting for background jobs’ message, meanwhile the ‘good’ segment don’t. The ‘good’ segment takes sections in the lower zone instead.</p>
<p>In my complete project I use segments extracted from a bigger segment and their corresponding centerlines, but if some trash appears in the segmentation the centerlines fails and can produce curves as shown in the mrb file.</p>
<p>Now I see clear that one possibility to freeze the module comes from the fact that I gave some bad inputs as could be in the example scene…</p>
<p>Are other problematic inputs (as could be give a segment that not intersects with the centerline curve) documented?</p>
<p>Thanks again, we think we are close to the optimal solution <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #21 by @chir.set (2024-10-07 12:35 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="20" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>freeze</p>
</blockquote>
</aside>
<p>Thanks for the sample scene. No freezing was seen in Linux, and I don’t use Windows at all. It will be hard for me to go any further without tangible observations.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bf7185bf2b9b60fa88dcc259de71c2b313e06b7.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fab208442cf12ab5cb9485de12e7e8292790232.jpeg">
  </div><p></p>

---

## Post #22 by @chir.set (2024-10-07 12:49 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="20" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>freeze</p>
</blockquote>
</aside>
<p>It doesn’t freeze with Slicer 5.6.2 neither on Linux. Please try with Slicer Preview.</p>

---

## Post #23 by @SANTIAGO_PENDON_MING (2024-10-07 13:30 UTC)

<p>Hi again <a class="mention" href="/u/chir.set">@chir.set</a>, I’m sharing a video with the execution (sorry for not send it before, I didn’t think on it…)<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f74389f0e781c1471e7a3650483b80f07219ba93.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dd3ed682762927a54debab80865b442eedd70a8.jpeg">
  </div><p></p>
<p>I actually running in version 5.6.2 so i guess you suggest the newer (but not stable yet) version?</p>
<p>I think the real reason to crash or not is the OS, not executing it with code or clicks and also not a problem with the way we give the inputs to CSA…</p>
<p>Do you propose any specific  supervision on the input data to take care of this?</p>
<p>Thanks a lot.</p>

---

## Post #24 by @SANTIAGO_PENDON_MING (2024-10-07 14:02 UTC)

<p>Finally I found the solution:</p>
<p>Windows 11 with 3D Slicer 5.6.2 crashes when you try to execute CSA in zones where the centerline does not intersect the lumen surface.</p>
<p>BUT, in 5.7.0 version, the module does not crash and shows a similar behaviour as Linux/Mac in 5.6.2 version</p>
<p>I hope this could help someone and thanks to <a class="mention" href="/u/chir.set">@chir.set</a> for the amazing support during this months.</p>

---

## Post #25 by @SANTIAGO_PENDON_MING (2024-10-08 13:54 UTC)

<p>UPDATE:</p>
<p>The problem was not the version of Slicer or the OS version…</p>
<p>The problem is import Pyvista python module… This import crash the cross-section Analysis. We suppose that this come from Pyvista uses several VTK instances and some of them could enter into conflicts with the CSA Module…</p>
<p>To solve this issue I think we will need extra help <a class="mention" href="/u/chir.set">@chir.set</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddfc93dd0107929ebb5b143a4356d451d5a53ddc.png" data-download-href="/uploads/short-url/vFMFhXrHSkAFmBpUAwgoCIGEcyg.png?dl=1" title="Captura de pantalla 2024-10-08 155227" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddfc93dd0107929ebb5b143a4356d451d5a53ddc_2_690x405.png" alt="Captura de pantalla 2024-10-08 155227" data-base62-sha1="vFMFhXrHSkAFmBpUAwgoCIGEcyg" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddfc93dd0107929ebb5b143a4356d451d5a53ddc_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddfc93dd0107929ebb5b143a4356d451d5a53ddc_2_1035x607.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddfc93dd0107929ebb5b143a4356d451d5a53ddc_2_1380x810.png 2x" data-dominant-color="1F1E1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-10-08 155227</span><span class="informations">1654×971 42.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #26 by @chir.set (2024-10-08 14:09 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="25" data-topic="37206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>import Pyvista</p>
</blockquote>
</aside>
<p>A quick glance at its web page concludes that it is a competitor to Slicer’s approach to VTK via python. Expected conflicts have emerged in <em>your</em> project. This library is foreign to me and I can’t allocate resources in too many directions; I’m afraid not to be that helpful.</p>

---
