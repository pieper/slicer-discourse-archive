---
topic_id: 3525
title: "Acpc Transform Question"
date: 2018-07-19
url: https://discourse.slicer.org/t/3525
---

# ACPC transform question

**Topic ID**: 3525
**Date**: 2018-07-19
**URL**: https://discourse.slicer.org/t/acpc-transform-question/3525

---

## Post #1 by @shebaelena (2018-07-19 14:50 UTC)

<p>Hello,</p>
<p>I have been trying to figure out how to transform a scan so that it aligns to the ACPC plane. I’ve tried using this module (<a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/ACPCTransform" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.8/Modules/ACPCTransform</a>) and placing fiducial points on different slices to transform the scan, but have been unsuccessful. Can anyone explain how I can do this? Also, is there a way to overlay a grid on the scan or in some way calculate just horizontal distance with the ruler?</p>
<p>Thank you!</p>

---

## Post #2 by @Fernando (2018-07-19 20:59 UTC)

<p>Hi Alexis,</p>
<p>You can try this code on the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np
import SampleData

def getSampleVolume():
    # Download MRHead
    sampleDataLogic = SampleData.SampleDataLogic()
    volumeNode = sampleDataLogic.downloadMRHead()
    return volumeNode


def getMatrixToACPC(ac, pc, ih):
    # Anteroposterior axis
    pcAc = ac - pc
    yAxis = pcAc / np.linalg.norm(pcAc)
    # Lateral axis
    acIhDir = ih - ac
    xAxis = np.cross(yAxis, acIhDir)
    xAxis /= np.linalg.norm(xAxis)
    # Rostrocaudal axis
    zAxis = np.cross(xAxis, yAxis)
    # Rotation matrix
    rotation = np.vstack([xAxis, yAxis, zAxis])
    # AC in rotated space
    translation = -np.dot(rotation, ac)
    # Build homogeneous matrix
    matrix = np.eye(4)
    matrix[:3, :3] = rotation
    matrix[:3, 3] = translation
    return matrix


def getTransformNodeFromNumpyMatrix(matrix, name=None):
    # Create VTK matrix object
    vtkMatrix = vtk.vtkMatrix4x4()
    for row in range(4):
        for col in range(4):
            vtkMatrix.SetElement(row, col, matrix[row, col])
    # Create MRML transform node
    transformNode = slicer.mrmlScene.AddNewNodeByClass(
        'vtkMRMLLinearTransformNode')
    if name is not None:
        transformNode.SetName(name)
    transformNode.SetAndObserveMatrixTransformToParent(vtkMatrix)
    return transformNode


# I defined these on MRHead
ac = np.array([-0.0641399910762672, 17.61291529545006, 5.009494772024041])
pc = np.array([-0.5843405105866637, -10.4779127581112, 3.044020167647495])
ih = np.array([-1.1045410300970602, 1.746799450383008, 45.04402016764749])

volumeNode = getSampleVolume()
matrix = getMatrixToACPC(ac, pc, ih)
transformNode = getTransformNodeFromNumpyMatrix(matrix, name='World to ACPC')

# Create markups node with AC, PC and an interhemispheric point
markupsNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode')
markupsNode.SetName('AC-PC-IH')
markupsNode.AddFiducialFromArray(ac, 'AC')
markupsNode.AddFiducialFromArray(pc, 'PC')
markupsNode.AddFiducialFromArray(ih, 'IH')

# Apply transform to volume node and markups node
volumeNode.SetAndObserveTransformNodeID(transformNode.GetID())
markupsNode.SetAndObserveTransformNodeID(transformNode.GetID())

# Fit image to slices
applicationLogic = slicer.app.applicationLogic()
applicationLogic.FitSliceToAll()

# Center views on AC
markupsLogic = slicer.modules.markups.logic()
acIndex = 0
markupsLogic.JumpSlicesToNthPointInMarkup(markupsNode.GetID(), acIndex)
</code></pre>
<p>By the way, looking forward to showing examples like these in a Jupyter Notebook <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<aside class="quote quote-modified" data-post="1" data-topic="3438">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/jupyter-notebooks-are-now-usable-in-3d-slicer/3438">Jupyter notebooks are now usable in 3D Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We worked hard with <a class="mention" href="/u/jcfr">@jcfr</a> during the during <a href="https://na-mic.github.io/ProjectWeek/PW28_2018_GranCanaria/" rel="noopener nofollow ugc">Slicer project week in Gran Canaria</a> and we are excited to share one of the newest developments: <a href="https://jupyter.org/" rel="noopener nofollow ugc">Jupyter notebook</a> support. 
You can create interactive Python notebooks to run Slicer code and show resulting text data or slicer/3D view content in the notebook. Great for experimenting and sharing code and results with others. 
[image] 
See an example notebook <a href="https://github.com/lassoan/SlicerNotebooks/blob/master/My%20second%20notebook.ipynb" rel="noopener nofollow ugc">here</a>, which shows loading of a sample data set, display of a slice view, creation and display of a…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2018-07-20 04:53 UTC)

<aside class="quote no-group" data-username="shebaelena" data-post="1" data-topic="3525">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shebaelena/48/9708_2.png" class="avatar"> shebaelena:</div>
<blockquote>
<p>have been unsuccessful</p>
</blockquote>
</aside>
<p>These may help (they are accurate for Slicer 3.6, but the behavior is not that much different on Slicer 4.9):</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation:Nightly:Registration:RegistrationLibrary:RegLib_C15" class="inline-onebox">Documentation:Nightly:Registration:RegistrationLibrary:RegLib C15 - Slicer Wiki</a></li>
<li><a href="https://www.slideserve.com/jacoba/slicer3-tutorial-registration-library-case-15-ac-pc-alignment" class="inline-onebox">PPT - Slicer3 Tutorial: Registration Library Case 15 AC-PC Alignment PowerPoint Presentation - ID:5393167</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ACPCTransform">https://www.slicer.org/wiki/Documentation/Nightly/Modules/ACPCTransform</a></li>
</ul>
<p>If you still have problems, then please describe what you did exactly, what you expected to happen, and what happened instead.</p>

---
