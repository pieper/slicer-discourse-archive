---
topic_id: 40037
title: "Delete Control Points Within A Roi"
date: 2024-11-05
url: https://discourse.slicer.org/t/40037
---

# Delete control points within a ROI

**Topic ID**: 40037
**Date**: 2024-11-05
**URL**: https://discourse.slicer.org/t/delete-control-points-within-a-roi/40037

---

## Post #1 by @bserrano (2024-11-05 14:16 UTC)

<p>Hi all,</p>
<p>I would like to develop a Python script that allows the deletion of multiple control points within a ROI. Specifically, it would be great to mimic the behavior of the Scissors tool from the Segment Editor module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb02dda2664e0338055bbd43b810f0eede6e21b0.png" data-download-href="/uploads/short-url/qGnqsKHPMSfPEBxp8vKLlT7nFa8.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb02dda2664e0338055bbd43b810f0eede6e21b0_2_545x500.png" alt="imagen" data-base62-sha1="qGnqsKHPMSfPEBxp8vKLlT7nFa8" width="545" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb02dda2664e0338055bbd43b810f0eede6e21b0_2_545x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb02dda2664e0338055bbd43b810f0eede6e21b0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb02dda2664e0338055bbd43b810f0eede6e21b0.png 2x" data-dominant-color="424869"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">704×645 29.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Example: I want to delete all the control points inside a selected circle on the image.</p>
<p>Any suggestions on how to approach this?</p>
<p>Many thanks,</p>

---

## Post #2 by @muratmaga (2024-11-05 14:40 UTC)

<p>This functionality already exists in SlicerMorph extension.  It is a plugin called MarkupEditor.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/MarkupsEditor#readme">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MarkupsEditor#readme" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/MarkupsEditor#readme" target="_blank" rel="noopener nofollow ugc">Tutorials/MarkupsEditor at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @bserrano (2024-11-05 15:12 UTC)

<p>Hi, thank you very much! I’m running some tests with this tool. However, the selection of points isn’t accurate when there’s overlap between points or with a curve. Additionally, sometimes points outside the ROI get selected.</p>
<p>The steps I’m following are:</p>
<p>Pick points with curve → Set selection → draw ROI → Edit selected points → Delete points</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29c610a25e6384464498521da1597ab2e41a0c72.png" data-download-href="/uploads/short-url/5XxVzkryb9AZkv8dfzlk4FZNr3A.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c610a25e6384464498521da1597ab2e41a0c72_2_394x500.png" alt="imagen" data-base62-sha1="5XxVzkryb9AZkv8dfzlk4FZNr3A" width="394" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c610a25e6384464498521da1597ab2e41a0c72_2_394x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29c610a25e6384464498521da1597ab2e41a0c72.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29c610a25e6384464498521da1597ab2e41a0c72.png 2x" data-dominant-color="3A415D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">567×718 60.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
See example here.</p>
<p>I also noticed that it only takes into account the points that are visible in the 3D view, which becomes a problem when the view is zoomed in on a specific region.</p>

---

## Post #4 by @muratmaga (2024-11-05 15:40 UTC)

<p>Yes, I observed similar issues occasionally as well. But often drawing another curve and choosing “Add to Selection” fixes it, so we didn’t spend too much debugging it.</p>
<p>You are welcome to take look and improve if you have the bandwidth.</p>

---

## Post #5 by @muratmaga (2024-11-05 15:41 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="3" data-topic="40037">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/60/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>I also noticed that it only takes into account the points that are visible in the 3D view</p>
</blockquote>
</aside>
<p>Yes, that’s a requirement for our use case, in which we often have points on a model. If you don’t restrict it to visible points only, it will select points on the back side of the model too.</p>

---

## Post #6 by @bserrano (2024-11-07 08:16 UTC)

<p>I’ve reviewed the code, and for our specific purpose, we need to ensure that points outside the view are not selected, and that the ROI restricts the selection similarly to how the scissors tool works in Segment Editor. To achieve this, I modified the logic class in the <code>MarkupEditor.py</code> file (look for comments marked “CHANGED”):</p>
<ol>
<li>Removed <code>if pointVisible:</code> in the selection option.</li>
<li>Added a check to determine if a point is outside the 3D view; if so, it is marked as unselected.</li>
</ol>
<pre><code class="lang-auto">class MarkupEditorLogic(ScriptedLoadableModuleLogic):
    def __init__(self):
        ScriptedLoadableModuleLogic.__init__(self)
        self.observerTags = {}

    def editMarkups(self, selectOption, fiducialsNode, curveNode, viewNode):
        layoutManager = slicer.app.layoutManager()
        threeDWidget = layoutManager.viewWidget(viewNode)
        threeDView = threeDWidget.threeDView()
        aspectRatio = threeDWidget.width / threeDWidget.height
        className = "vtkMRMLMarkupsDisplayableManager"
        markupsDisplayableManager = threeDView.displayableManagerByClassName(className)
        fiducialsWidget =  markupsDisplayableManager.GetWidget(fiducialsNode.GetDisplayNode())
        fiducialsRepresentation =  fiducialsWidget.GetRepresentation()

        cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(viewNode)
        camera = cameraNode.GetCamera()
        raswToXYZW = vtk.vtkMatrix4x4()
        modelView = camera.GetModelViewTransformMatrix()
        projection = camera.GetProjectionTransformMatrix(aspectRatio, 1, 100)  # near/far are arbitrary
        raswToXYZW.Multiply4x4(projection, modelView, raswToXYZW)

        def rasToColumnRow(ras):
            rasw = *ras, 1
            xyzw = raswToXYZW.MultiplyPoint(rasw)
            x, y = [xyzw[0], xyzw[1]]
            if viewNode.GetRenderMode() == viewNode.Perspective:
                x, y = [x / xyzw[3], y / xyzw[3]]
            column = (x + 1) / 2 * threeDWidget.width
            row = (1 - (y + 1) / 2) * threeDWidget.height
            return column, row

        selectionPolygon = qt.QPolygonF()
        for index in range(curveNode.GetNumberOfControlPoints()):
            ras = [0] * 3
            curveNode.GetNthControlPointPositionWorld(index, ras)
            column, row = rasToColumnRow(ras)
            point = qt.QPointF(column, row)
            selectionPolygon.push_back(point)

        pickImage = qt.QImage(threeDWidget.width, threeDWidget.height, qt.QImage().Format_ARGB32)
        backgroundColor = qt.QColor("#ffffffff")
        pickImage.fill(backgroundColor)

        painter = qt.QPainter()
        painter.begin(pickImage)
        painterPath = qt.QPainterPath()
        painterPath.addPolygon(selectionPolygon)
        brush = qt.QBrush(qt.Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawPath(painterPath)
        painter.end()

        debugging = False
        if debugging:
            pixmap = qt.QPixmap().fromImage(pickImage)
            slicer.modules.label = qt.QLabel()
            slicer.modules.label.setPixmap(pixmap)
            slicer.modules.label.show()

        visibleCount = 0
        pickedCount = 0
        for index in range(fiducialsNode.GetNumberOfControlPoints()):
            pointVisible = fiducialsRepresentation.GetNthControlPointViewVisibility(index)
            if pointVisible:
                visibleCount += 1

            ras = [0] * 3
            fiducialsNode.GetNthControlPointPositionWorld(index, ras)
            column, row = rasToColumnRow(ras)

            # CHANGED: check if the point is inside the 3D view
            if column &lt; 0 or column &gt;= pickImage.width() or row &lt; 0 or row &gt;= pickImage.height():
                fiducialsNode.SetNthControlPointSelected(index, False)
                continue  # we do not process this point

            # If the point is inside the 3D view, we check if it is inside
            # the polygon
            pickColor = pickImage.pixelColor(column, row)
            picked = (pickColor != backgroundColor)
            
            if picked:
                pickedCount += 1

            # CHANGED: we do not use pointVisible here, so overlapping points are selected
            if selectOption == "set":
                fiducialsNode.SetNthControlPointSelected(index, picked)
            elif selectOption == "add":
                if picked:
                    fiducialsNode.SetNthControlPointSelected(index, True)
            elif selectOption == "unset":
                if picked:
                    fiducialsNode.SetNthControlPointSelected(index, False)
            else:
                logging.error(f"Unknown selectOption {selectOption}")
    


</code></pre>

---
