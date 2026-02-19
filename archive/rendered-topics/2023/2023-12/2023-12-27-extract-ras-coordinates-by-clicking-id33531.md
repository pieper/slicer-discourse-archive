---
topic_id: 33531
title: "Extract Ras Coordinates By Clicking"
date: 2023-12-27
url: https://discourse.slicer.org/t/33531
---

# Extract RAS coordinates by clicking

**Topic ID**: 33531
**Date**: 2023-12-27
**URL**: https://discourse.slicer.org/t/extract-ras-coordinates-by-clicking/33531

---

## Post #1 by @SANTIAGO_PENDON_MING (2023-12-27 11:42 UTC)

<p>Hi to everyone <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Today I want to extract RAS coordinates to 3d markups/curves to click.</p>
<p>My goal is interact with 3d view (if is not possible, interact with 2d views would great too). Processing the click I would like to know the ID of the selected point and RAS coordinates.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff66f340893da98cc156652262a75b2643a6c67b.jpeg" data-download-href="/uploads/short-url/Arok8mYNbhD7qmYBSi9RtEE4Irx.jpeg?dl=1" title="Captura de pantalla 2023-12-27 123747" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff66f340893da98cc156652262a75b2643a6c67b_2_690x271.jpeg" alt="Captura de pantalla 2023-12-27 123747" data-base62-sha1="Arok8mYNbhD7qmYBSi9RtEE4Irx" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff66f340893da98cc156652262a75b2643a6c67b_2_690x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff66f340893da98cc156652262a75b2643a6c67b_2_1035x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff66f340893da98cc156652262a75b2643a6c67b_2_1380x542.jpeg 2x" data-dominant-color="413F42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-12-27 123747</span><span class="informations">1913×754 236 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there a way to do it by python code → Run some lines which allows the user to select one point and then he can retrieve the coordinates?</p>
<p>I’m interested in obtain info from centerlines created by extractCenterlines module</p>

---

## Post #2 by @bserrano (2024-02-05 15:46 UTC)

<p>Also interested in having a callback function when clicking on a markups. Any solution for this?</p>
<p>Thanks</p>

---

## Post #3 by @cpinter (2024-02-07 11:53 UTC)

<p>This worked for me for adding new points:</p>
<pre><code class="lang-auto">@vtk.calldata_type(vtk.VTK_INT)
def onPointDefined(caller, eventid, callData):
    fiducialNode = caller
    fiducialIndex = callData
    print(f'Defined: {fiducialNode.GetName()}, Fiducial index: {fiducialIndex}')

fiducialsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent, onPointDefined)
</code></pre>
<p>For clicking this could be the solution:</p>
<pre><code class="lang-auto">@vtk.calldata_type(vtk.VTK_OBJECT)
def onPointClicked(caller, eventid):
    fiducialNode = caller
    fiducialIndex = int(fiducialNode.GetAttribute('Markups.MovingMarkupIndex'))
    print(f'Moved: {fiducialNode.GetName()}, Fiducial index: {fiducialIndex}')

fiducialsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointStartInteractionEvent, onPointClicked)
</code></pre>

---
