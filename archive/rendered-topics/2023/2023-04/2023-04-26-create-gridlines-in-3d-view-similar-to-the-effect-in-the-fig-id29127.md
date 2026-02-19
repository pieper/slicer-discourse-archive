---
topic_id: 29127
title: "Create Gridlines In 3D View Similar To The Effect In The Fig"
date: 2023-04-26
url: https://discourse.slicer.org/t/29127
---

# Create gridlines in 3D view, similar to the effect in the figure

**Topic ID**: 29127
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/create-gridlines-in-3d-view-similar-to-the-effect-in-the-figure/29127

---

## Post #1 by @q2577040659 (2023-04-26 02:35 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20d7a99cda47addfd7a196c9e87b2f6911004c97.png" data-download-href="/uploads/short-url/4GxkHEig6Ixy2T7FlEkJZsb9Rxt.png?dl=1" title="Snipaste_2023-04-26_10-33-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20d7a99cda47addfd7a196c9e87b2f6911004c97_2_690x451.png" alt="Snipaste_2023-04-26_10-33-11" data-base62-sha1="4GxkHEig6Ixy2T7FlEkJZsb9Rxt" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20d7a99cda47addfd7a196c9e87b2f6911004c97_2_690x451.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20d7a99cda47addfd7a196c9e87b2f6911004c97_2_1035x676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20d7a99cda47addfd7a196c9e87b2f6911004c97_2_1380x902.png 2x" data-dominant-color="0E0B09"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2023-04-26_10-33-11</span><span class="informations">1422×930 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2023-10-16 16:50 UTC)

<p>It would be quite straightforward to implement this, but we would need to understand what is the main motivation. We would not want to invest into implementing a tool if existing measurement tools would work just as well or better. 3D markups are generally more accurate, reliable, verifiable measurements than counting of gridlines. For approximate appreciation of size, you can enable view ruler.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30cb12abd21d0b39fff3e72cc9af564b08a28e41.jpeg" data-download-href="/uploads/short-url/6XE01ieHuegywqC2u7D6zlUlMeB.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30cb12abd21d0b39fff3e72cc9af564b08a28e41_2_667x500.jpeg" alt="image" data-base62-sha1="6XE01ieHuegywqC2u7D6zlUlMeB" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30cb12abd21d0b39fff3e72cc9af564b08a28e41_2_667x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30cb12abd21d0b39fff3e72cc9af564b08a28e41_2_1000x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30cb12abd21d0b39fff3e72cc9af564b08a28e41_2_1334x1000.jpeg 2x" data-dominant-color="6A5E59"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1438 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In certain fields, current practice may be to count grid points and it may take time to convince people to use proper 3D measurements instead. For this transition period (or to prove that 3D markups are superior), it could make sense to use a small Python script that displays the grid. For example, you can copy-paste this code snippet to the Python console to show a 10mm grid in the first 3D view:</p>
<pre data-code-wrap="python"><code class="lang-python">threeDViewIndex = 0
gridSizeMm = 10
renderers = slicer.app.layoutManager().threeDWidget(threeDViewIndex).threeDView().renderWindow().GetRenderers()
threeDRenderer = renderers.GetItemAsObject(0)
rulerRenderer = renderers.GetItemAsObject(1)

# Create a plane source
planeSource = vtk.vtkPlaneSource()
planeMapper = vtk.vtkPolyDataMapper()
planeMapper.SetInputConnection(planeSource.GetOutputPort())
planeActor = vtk.vtkActor()
planeActor.SetMapper(planeMapper)
planeActor.GetProperty().SetColor(0, 0, 0)
planeActor.GetProperty().SetOpacity(0.3)
planeActor.GetProperty().SetRepresentationToWireframe()
rulerRenderer.AddActor(planeActor)

camera = threeDRenderer.GetActiveCamera()

def updateScale(caller=None, eventId=None):
    if not camera.GetParallelProjection():
        print("Set view to parallel projection")
        return
    # View: xmin, ymin, xmax, ymax; range: -1 to +1; origin is bottom left
    # Determine the available renderer size in millimeters
    minWorld = [vtk.reference(-1), vtk.reference(-1), vtk.reference(-1)]
    rulerRenderer.ViewToWorld(*minWorld)
    maxWorld = [vtk.reference(1), vtk.reference(1), vtk.reference(1)]
    rulerRenderer.ViewToWorld(*maxWorld)
    rendererSizeInWorld = [maxWorld[0]-minWorld[0], maxWorld[1]-minWorld[1]]
    # Parallel scale: height of the half viewport in world-coordinate distances.
    scalingFactorMmPerWorld = camera.GetParallelScale() * 2.0 / rendererSizeInWorld[1]
    gridSizeWorld = gridSizeMm / scalingFactorMmPerWorld
    numberOfGrids = [int(rendererSizeInWorld[0] / gridSizeWorld / 4) * 2 + 2, int(rendererSizeInWorld[1]/gridSizeWorld/4) * 2 + 2]
    lowerLeft = [-numberOfGrids[0] * gridSizeWorld, -numberOfGrids[1] * gridSizeWorld]
    upperRight = [numberOfGrids[0] * gridSizeWorld, numberOfGrids[1] * gridSizeWorld]
    planeSource.SetOrigin(lowerLeft[0], lowerLeft[1], 0)
    planeSource.SetPoint1(upperRight[0], lowerLeft[1], 0)
    planeSource.SetPoint2(lowerLeft[0], upperRight[1], 0)
    planeSource.SetResolution(numberOfGrids[0] * 2, numberOfGrids[1] * 2)

cameraObservation = camera.AddObserver(vtk.vtkCommand.ModifiedEvent, updateScale)
updateScale()
slicer.util.forceRenderAllViews()

# Run these lines to hide the grid:
#
# camera.RemoveObserver(cameraObservation)
# rulerRenderer.RemoveActor(planeActor)
#
</code></pre>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7d042eb1f5b9fee5c88030219e4dfb1cfe2002a.mp4">
  </div><p></p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> If you find this useful then you may consider adding it to a module in SlicerMorph.</p>

---

## Post #4 by @muratmaga (2023-10-16 19:03 UTC)

<p>Thanks this might be useful option for people who want to have grid. We don’t use it but can be added as slicermorph customization.</p>

---
