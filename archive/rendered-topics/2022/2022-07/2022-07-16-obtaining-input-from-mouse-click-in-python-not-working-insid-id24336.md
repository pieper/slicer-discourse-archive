---
topic_id: 24336
title: "Obtaining Input From Mouse Click In Python Not Working Insid"
date: 2022-07-16
url: https://discourse.slicer.org/t/24336
---

# Obtaining input from mouse click in python not working inside function: wait functionality?

**Topic ID**: 24336
**Date**: 2022-07-16
**URL**: https://discourse.slicer.org/t/obtaining-input-from-mouse-click-in-python-not-working-inside-function-wait-functionality/24336

---

## Post #1 by @KateDelb (2022-07-16 07:36 UTC)

<p>I am basing myself on this code <a href="https://discourse.slicer.org/t/how-to-get-input-value-from-mouse-click/5903">https://discourse.slicer.org/t/how-to-get-input-value-from-mouse-click/5903</a> to create a widget that allows you to select a point on the GUI.</p>
<p>The part of my code that selects the point is as follows:</p>
<pre><code class="lang-auto">#Volume is loaded into 3DSlicer

def placementModeChanged(active):
    print("Placement: " +("active" if active else "inactive"))
    # You can inspect what is in the markups node here, delete the temporary markup node, etc.

  # Temporary markups node
  markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")

  # Create and set up widget that contains a single "place markup" button. The widget can be placed in the module GUI.
  placeWidget = slicer.qSlicerMarkupsPlaceWidget()
  placeWidget.setMRMLScene(slicer.mrmlScene)
  placeWidget.setCurrentNode(markupsNode)
  placeWidget.buttonsVisible=True
  placeWidget.placeButton().show()
  placeWidget.connect('activeMarkupsFiducialPlaceModeChanged(bool)', placementModeChanged)
  placeWidget.show()
  
</code></pre>
<p>This works perfectly. It lets me choose a point on the previously loaded Volume.<br>
However, I’d like to store the selected point. For this reason I’ve incorporated it into a larger function that is supposed to take the stored point, convert it to ijk and save it.</p>
<pre><code class="lang-auto">def Register_Bg_point(fet,out_path,out_path_cv):
    #Display image
    volumeNode = su.PushVolumeToSlicer(fet)

    # Prevent automatic brightness/contrast update to make the processed images easier to compare
    # volumeNode.GetDisplayNode().SetAutoWindowLevel(False)

    # Set up view layout
    slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)
    # Set up slice views
    slicer.util.setSliceViewerLayers(background=volumeNode, fit=True)
    # Show volume rendering
    slicernb.showVolumeRendering(volumeNode, presetName='MR-Default')
    slicer.util.resetThreeDViews()

    # Display views
    slicernb.ViewDisplay()
    
    # Temporary markups node
    markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")

    # Create and set up widget that contains a single "place markup" button. The widget can be placed in the module GUI.
    placeWidget = slicer.qSlicerMarkupsPlaceWidget()
    placeWidget.setMRMLScene(slicer.mrmlScene)
    placeWidget.setCurrentNode(markupsNode)
    placeWidget.buttonsVisible=True
    placeWidget.placeButton().show()
    placeWidget.connect('activeMarkupsFiducialPlaceModeChanged(bool)', placementModeChanged)
    placeWidget.show()
    
    print("Select the center of the bg volume with the Widget")
    
    ## Get point coordinate in RAS
    point_ras = [0, 0, 0, 1]

    # Get number of markups
    num_fids = markupsNode.GetNumberOfFiducials()

    # Get coordinates of last markup (IN RAS)
    markupsNode.GetNthFiducialWorldCoordinates(num_fids - 1, point_ras)

    # Apply that transform to get volume's RAS coordinates
    transform_ras_to_volume_ras = vtk.vtkGeneralTransform()
    slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volumeNode.GetParentTransformNode(), transform_ras_to_volume_ras)
    point_volume_ras = transform_ras_to_volume_ras.TransformPoint(point_ras[0:3])

    # Get voxel coordinates from physical coordinates
    volume_ras_to_ijk = vtk.vtkMatrix4x4()
    volumeNode.GetRASToIJKMatrix(volume_ras_to_ijk)
    point_ijk = [0, 0, 0, 1]
    volume_ras_to_ijk.MultiplyPoint(np.append(point_volume_ras, 1.0), point_ijk)
    point_ijk = [ int(round(c)) for c in point_ijk[0:3] ]
    
    print(f"Chosen center of background VOI:{point_ijk}")    
    
    bg_mask_arr = spheremask(fet, point_ijk)

    bg_mask = sitk.GetImageFromArray(bg_mask_arr)

    #Allign with FET Image
    bg_mask.SetOrigin(fet.GetOrigin())
    bg_mask.SetDirection(fet.GetDirection())
    bg_mask.SetSpacing(fet.GetSpacing())
    
    #Add image to volume node 
    volumeNode = su.PushVolumeToSlicer(bg_mask)

    # Prevent automatic brightness/contrast update to make the processed images easier to compare
    # volumeNode.GetDisplayNode().SetAutoWindowLevel(False)

    # Set up view layout
    slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)
    # Set up slice views
    slicer.util.setSliceViewerLayers(background=volumeNode, fit=True)
    # Show volume rendering
    slicernb.showVolumeRendering(volumeNode, presetName='MR-Default')
    slicer.util.resetThreeDViews()

    # Display views
    slicernb.ViewDisplay()
    
    print("Background volume Showing in 3DSlicer extension")
    
    ## Save point IJK into csv file
    name = patient + pathname
    dict_point = [[name], [point_ijk]]
    print(dict_point)
    path_to_csv = os.path.join(out_path_csv,'points.csv')

    if os.path.exists(path_to_csv):
        with open(path_to_csv,'w') as f:
            out = csv.writer(f, delimiter=';',quoting=csv.QUOTE_ALL)
            out.writerows(dict_point)
    
    else:
        with open(path_to_csv,'a') as f:
            writer = csv.writer(f)
            writer.writerow(dict_point)

    ## Save bg as binary mask
    sitk.WriteImage(bg_mask, out_path)
    
    print('Saved!')
</code></pre>
<p>However, when running the larger function, I don’t get the time to actually select a point, as the function just continues running.</p>
<p>In the placementmode function, it takes the “active” parameter which is True when selecting a point and False when the point has been selected. I can’t figure out a straightforward way to put this into a variable however.</p>
<p>Ideally I’d like to do something like this:</p>
<pre><code class="lang-auto">placeWidget gets created + set up
if placementMode == inactive:
     Continue runnning code
</code></pre>
<p>Is there a way to do this?</p>

---

## Post #2 by @lassoan (2022-07-16 20:27 UTC)

<aside class="quote no-group" data-username="KateDelb" data-post="1" data-topic="24336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katedelb/48/14981_2.png" class="avatar"> KateDelb:</div>
<blockquote>
<p>However, I’d like to store the selected point.</p>
</blockquote>
</aside>
<p>GUI applications are event-driven, so you need to implement all functionalities in callback functions. If you want to store the selected points then store it in the callback function.</p>
<p>In a Jupyter notebook you can instruct the user to mark some points and when finished then then run the next cell. This would be the cleanest and simplest solution. If you really want to block the execution of a cell until all points are collected then you need to “pump the event loop” (process messages in the event loop) by calling <code>slicer.app.processEvents()</code> in your wait loop.</p>
<p>If you want to prevent a Jupyter notebook cell</p>

---
