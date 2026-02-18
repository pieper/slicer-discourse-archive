# Slicer crashes when I update a vtkDistancePolyDataFilter

**Topic ID**: 26559
**Date**: 2022-12-02
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-i-update-a-vtkdistancepolydatafilter/26559

---

## Post #1 by @Alpha_Jaeger (2022-12-02 20:32 UTC)

<p>Hi,</p>
<p>For my project, I need to compute the distance between 2 models (one loaded from a vtk file and the other one created by my own). To do that, I tried to use a vtkDistancePolyDataFilter. But when I’m updating this filter, Slicer crashes. So I can’t figure out the issue. If someone is able to help me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60fe0b3a66fa011574470e5d72204c0b087e9c72.png" data-download-href="/uploads/short-url/dQ27FcKOlFU0BqeZOTV2EDYxtxE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60fe0b3a66fa011574470e5d72204c0b087e9c72.png" alt="image" data-base62-sha1="dQ27FcKOlFU0BqeZOTV2EDYxtxE" width="690" height="303" data-dominant-color="272828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1186×522 43.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-12-02 20:35 UTC)

<p>The code looks fine, so most likely the input data is somehow invalid. Could you upload the scene and a script that we can run as is (after loading the scene) that reproduces the issue?</p>

---

## Post #3 by @Alpha_Jaeger (2022-12-02 20:47 UTC)

<p>I’m not allowed to upload the scene (format isn’t accepted).</p>
<p>Here is the script that I run :</p>
<pre><code class="lang-auto">import logging
import os
from math import dist
import vtk
import numpy as np

import slicer, vtk, qt, SampleData
from slicer.ScriptedLoadableModule import *
from slicer.util import *
from vtkmodules.vtkFiltersCore import vtkTubeFilter
from vtkmodules.vtkFiltersSources import vtkLineSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
from vtk.util.numpy_support import vtk_to_numpy


#%%
#
# Needle1
#

class Needle1(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Needle1"  # TODO: make this more human readable by adding spaces
        self.parent.categories = ["Examples"]  # TODO: set categories (folders where the module shows up in the module selector)
        self.parent.dependencies = []  # TODO: add here list of module names that this module requires
        self.parent.contributors = ["Caroline Essert (University of Strasbourg)"]  # TODO: replace with "Firstname Lastname (Organization)"
        # TODO: update with short description of the module and a link to online module documentation
        self.parent.helpText = """
            This is an example of scripted loadable module bundled in an extension.
            See more information in &lt;a href="https://github.com/organization/projectname#Needle1"&gt;module documentation&lt;/a&gt;.
            """
        # TODO: replace with organization, grant and thanks
        self.parent.acknowledgementText = """
            This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc., Andras Lasso, PerkLab,
            and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
            """

#%%
#
# Needle1Widget
#

class Needle1Widget(ScriptedLoadableModuleWidget, VTKObservationMixin):
    """Uses ScriptedLoadableModuleWidget base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent=None):
        """
        Called when the user opens the module the first time and the widget is initialized.
        """
        ScriptedLoadableModuleWidget.__init__(self, parent)
        VTKObservationMixin.__init__(self)  # needed for parameter node observation
        # store logic in a member variable
        self.logic = Needle1Logic()
       



    def setup(self):
        """
        Called when the user opens the module the first time and the widget is initialized.
        """
        # initialisation that needs to be here - don't remove
        ScriptedLoadableModuleWidget.setup(self)

        # Init button
        InitButton = qt.QPushButton("Init")
        self.layout.addWidget(InitButton)
        InitButton.connect('clicked(bool)', self.onInitButtonClicked)

        # Create Cylinder button
        CreateCyl = qt.QPushButton("Create Cylinder")
        self.layout.addWidget(CreateCyl)
        CreateCyl.connect('clicked(bool)', self.onCreateCylClicked)

        # Place Electrode button
        myButton = qt.QPushButton("Place Electrode")
        self.layout.addWidget(myButton)
        myButton.connect('clicked(bool)', self.onPlaceElectrodeButtonClicked)

        # Compute Distance button
        myButton = qt.QPushButton("Compute Distance")
        self.layout.addWidget(myButton)
        myButton.connect('clicked(bool)', self.onComputeDistanceButtonClicked)


    # Create Cylinder button callback function
    def onCreateCylClicked(self):
        # call logic function to print position of the first fiducial (requires a fiducial to be added beforehand to work properly)
        self.mySnode = self.logic.myCreateCylinder()



    def onPlaceElectrodeButtonClicked(self):
        self.logic.myPlacingfct()


    def onInitButtonClicked(self):
        self.logic.myInit()

    def onComputeDistanceButtonClicked(self):
        self.logic.myDistance()

#%%
#
# Needle1Logic
#

class Needle1Logic(ScriptedLoadableModuleLogic):
    """This class should implement all the actual
    computation done by your module.  The interface
    should be such that other python code can import
    this class and make use of the functionality without
    requiring an instance of the Widget.
    Uses ScriptedLoadableModuleLogic base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self):
        """
        Called when the logic class is instantiated. Can be used for initializing member variables.
        """
        ScriptedLoadableModuleLogic.__init__(self)
        print('in init logic')
        #myP1 = slicer.modules.markups.logic().AddControlPoint(0, 0, 0)
        #myP2 = slicer.modules.markups.logic().AddControlPoint(150.0, 0, 0)
        try:
            f = getNode('F')         
            obsTag=f.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, self.modifyMyCylinder)
            print('Observer instantiated')
        except slicer.util.MRMLNodeNotFoundException:
            print("Please create a fiducial first, no observer yet")
        
    def myInit(self):
        try:
            f = getNode('F')         
            obsTag=f.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, self.modifyMyCylinder)
            print('Observer instantiated')
        except slicer.util.MRMLNodeNotFoundException:
            print("Please create a fiducial first, no observer yet")

    def myCreateCylinder(self, caller=None, event=None): 
        #je dois gerer la creation des points si ils exisent pas encore, sinon creer sans cesse de nouveaux doublets de points
        
        try :
            f = getNode('F')
            print('f found in try')
            #print(dir(self))
            #update the position of the cylinder
            self.modifyMyCylinder()
            print(self.myLine)
            print(self.myCylinder)
            
        except slicer.util.MRMLNodeNotFoundException:
            print("I'll create 2 fiducials first")
            myP1 = slicer.modules.markups.logic().AddControlPoint(0, 0, 0)
            myP2 = slicer.modules.markups.logic().AddControlPoint(150.0, 0, 0)
            
            f = getNode('F')
            # initilize a position
            pos=[0,0,0]
            # get the first fiducial's position in pos (fiducial of index=0)
            f.GetNthFiducialPosition(0,pos)
            #print(pos)
            posF2=[0,0,0]
            f.GetNthFiducialPosition(1,posF2)
            #print(posF2)

            lineSource = vtkLineSource()
            lineSource.SetPoint1(pos)
            lineSource.SetPoint2(posF2)

            lineMapper = vtkPolyDataMapper()
            lineMapper.SetInputConnection(lineSource.GetOutputPort())

            lineActor = vtkActor()
            lineActor.SetMapper(lineMapper)

            # Create tube filter
            tubeFilter = vtkTubeFilter()
            tubeFilter.SetInputConnection(lineSource.GetOutputPort())
            tubeFilter.SetRadius(1)
            tubeFilter.SetNumberOfSides(50)
            tubeFilter.Update()

            self.myLine = lineSource
            self.myCylinder = tubeFilter

            sNode=slicer.modules.models.logic().AddModel(tubeFilter.GetOutputPort())
            sNode.SetAndObservePolyData(tubeFilter.GetOutput())
            sDisplayNode=sNode.GetDisplayNode()
            return sNode

    def myPlacingfct(self):
        right_snt = slicer.mrmlScene.GetFirstNodeByName('63_stn_right.vtk')
        pointCoordinates = slicer.util.arrayFromModelPoints(right_snt)
        pd = right_snt.GetPolyData().GetPoints().GetData() #right_snt.GetPolyData().GetCenter()
        centroid_right_snt = np.average(vtk_to_numpy(pd), axis=0)
        f = getNode('F')
        posF2 = [20,20,20]
        f.SetNthFiducialPositionFromArray(0,centroid_right_snt)
        f.GetNthFiducialPosition(1,posF2)
       
        self.myLine.SetPoint1(centroid_right_snt)
        self.myLine.SetPoint2(posF2)
        self.myLine.Update()
        self.myCylinder.Update()
        print('Electrode placed in the middle of the right STN')

    def modifyMyCylinder(self,caller=None, event=None):
        print('Position of one fiducial changed, adjusting the cylinder')
        f = getNode('F')
        pos=[0,0,0]
        f.GetNthFiducialPosition(0,pos)
        posF2=[0,0,0]
        f.GetNthFiducialPosition(1,posF2)
        self.myLine.SetPoint1(pos)
        self.myLine.SetPoint2(posF2)
        self.myLine.Update()
        self.myCylinder.Update()

    def myDistance(self,caller=None,event=None):
        right_sulci = slicer.mrmlScene.GetFirstNodeByName('63_sulci_right.vtk')
        left_sulci = slicer.mrmlScene.GetFirstNodeByName('63_sulci_left.vtk')
        
        fourth_ventricule = slicer.mrmlScene.GetFirstNodeByName('63_fourth_ventricle.vtk')
        third_ventricule = slicer.mrmlScene.GetFirstNodeByName('63_third_ventricle.vtk')
        lat_left_ventricule = slicer.mrmlScene.GetFirstNodeByName('63_lateral_ventricle_left.vtk')
        lat_right_ventricule = slicer.mrmlScene.GetFirstNodeByName('63_lateral_ventricle_right.vtk')

        tab_sulci = [right_sulci,left_sulci]
        tab_ventricule = [fourth_ventricule,third_ventricule,lat_left_ventricule,lat_right_ventricule]
        needle = self.myCylinder.GetOutputPort()
        print(type(self.myCylinder.GetOutputPort()))
        print(type(lat_left_ventricule.GetPolyDataConnection()))
        distanceFilter = vtk.vtkDistancePolyDataFilter()
        distanceFilter.SetInputConnection(0, needle)
        distanceFilter.SetInputConnection(1, lat_left_ventricule.GetPolyDataConnection()) #self.myCylinder.GetOutputPort()
        #distanceFilter.SignedDistanceOff()
        distanceFilter.Update()
        print(type(distanceFilter))
        #print(distanceFilter.GetOutput().GetPointData().GetScalars().GetRange()[0])

"""         for vec in tab_sulci:
            print(type(vec))
            print('////////////////////\n')

        for vec in tab_ventricule:
            print(type(vec))
            print('////////////////////\n')
 """
""" 
        print('Distance to ventricules : ')
 """

#%%
#
# Needle1Test
#

class Needle1Test(ScriptedLoadableModuleTest):
    """
    This is the test case for your scripted module.
    Uses ScriptedLoadableModuleTest base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def setUp(self):
        """ Do whatever is needed to reset the state - typically a scene clear will be enough.
        """
        # open the MRBrainTumor1 sample dataset
        sampleDataLogic = SampleData.SampleDataLogic()
        masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

    def runTest(self):
        """Run as few or as many tests as needed here.
        """
        self.setUp()
        self.test_Needle11()

    def test_Needle11(self):
        """ Ideally you should have several levels of tests.  At the lowest level
        tests should exercise the functionality of the logic with different inputs
        (both valid and invalid).  At higher levels your tests should emulate the
        way the user would interact with your code and confirm that it still works
        the way you intended.
        One of the most important features of the tests is that it should alert other
        developers when their changes will have an impact on the behavior of your
        module.  For example, if a developer removes a feature that you depend on,
        your test should break so they know that the feature is needed.
        """

        # quick message box to inform that the test is starting
        self.delayDisplay("Starting the test")

        # create node to store fiducials
        markupsNodeID = slicer.modules.markups.logic().AddNewFiducialNode()
        markupsNode = getNode(markupsNodeID)
        markupsNode.SetName("F")
        # add one fiducial
        markupsNode.AddFiducial(6.4, 35.1, 0.7)

        # get the logic
        logic = Needle1Logic()
        # call function printPosF1 to test it on the previously added fiducial
        #logic.printPosF1()

        # quick message box to inform that the test has successfully ended
        self.delayDisplay('Test passed')


</code></pre>
<p>As an exemple, the scene looks like this :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5843e427b7fc7a0f16216c3e07d445aa987fd95.png" data-download-href="/uploads/short-url/sbjogFbz4pnpkfRN6tZz2PX0Kvb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5843e427b7fc7a0f16216c3e07d445aa987fd95_2_690x244.png" alt="image" data-base62-sha1="sbjogFbz4pnpkfRN6tZz2PX0Kvb" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5843e427b7fc7a0f16216c3e07d445aa987fd95_2_690x244.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5843e427b7fc7a0f16216c3e07d445aa987fd95_2_1035x366.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5843e427b7fc7a0f16216c3e07d445aa987fd95_2_1380x488.png 2x" data-dominant-color="A8AACD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×679 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My goal is to compute the distance between the cylinder ‘Model’ created with the function ‘myCreateCylinder’ and one of the ventricule.</p>

---

## Post #4 by @pieper (2022-12-02 21:55 UTC)

<aside class="quote no-group" data-username="Alpha_Jaeger" data-post="3" data-topic="26559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alpha_jaeger/48/17560_2.png" class="avatar"> Alpha_Jaeger:</div>
<blockquote>
<p>I’m not allowed to upload the scene (format isn’t accepted).</p>
</blockquote>
</aside>
<p>You can upload to dropbox, google drive, or similar and post the link here.</p>

---

## Post #5 by @Alpha_Jaeger (2022-12-02 21:58 UTC)

<p>Thanks for the tips.</p>
<p>Here is the link : <a href="https://drive.google.com/drive/folders/1GntBWCvMUKZ5qiQB1BbJT9HBQmwXyr_K?usp=share_link" class="inline-onebox" rel="noopener nofollow ugc">Slicer_project - Google Drive</a><br>
DBS contains the scene and test contains my module</p>

---

## Post #6 by @lassoan (2022-12-02 22:58 UTC)

<p>How can we reproduce the issue? Can you copy here a code snippet that we can copy-paste into thr Python console after we loaded the scene?</p>

---

## Post #7 by @Alpha_Jaeger (2022-12-03 08:53 UTC)

<p>Yes sure,<br>
So after loading the scene, here is the code :</p>
<pre><code class="lang-auto">myP1 = slicer.modules.markups.logic().AddControlPoint(0, 0, 0)
myP2 = slicer.modules.markups.logic().AddControlPoint(150.0, 0, 0)

lineSource = vtk.vtkLineSource()
lineSource.SetPoint1([0,0,0])
lineSource.SetPoint2([150,0,0])

tubeFilter = vtk.vtkTubeFilter()
tubeFilter.SetInputConnection(lineSource.GetOutputPort())
tubeFilter.SetRadius(1)
tubeFilter.SetNumberOfSides(50)
tubeFilter.Update()

sNode=slicer.modules.models.logic().AddModel(tubeFilter.GetOutputPort())
sNode.SetAndObservePolyData(tubeFilter.GetOutput())
sDisplayNode=sNode.GetDisplayNode()

right_sulci = slicer.mrmlScene.GetFirstNodeByName('63_sulci_right.vtk')

distanceFilter = vtk.vtkDistancePolyDataFilter()
distanceFilter.SetInputConnection(0, tubeFilter.GetOutputPort())
distanceFilter.SetInputConnection(1, right_sulci.GetPolyDataConnection())
distanceFilter.Update()
</code></pre>
<p>When you’ll execute the last line (“distanceFilter.Update()”), nothing will happen and Slicer will crash.</p>
<p>Thanks</p>

---

## Post #8 by @pieper (2022-12-03 16:12 UTC)

<p>Probably <code>right_sulci.GetPolyDataConnection()</code> is null because the model was read from a file.  Try using <code>distanceFilter.SetInputData(1, right_sulci.GetPolyData())</code> instead.</p>

---

## Post #9 by @lassoan (2022-12-03 16:40 UTC)

<p>I’ve debugged into this and <code>GetPolyDataConnection()</code> is all right.</p>
<p>The problem is a bug in VTK! vtkDistancePolyDataFilter crashes for any cell types that uses <code>subId</code> (such as <code>vtkTriangleStrip</code>) input because <code>subId</code> is an input argument of <code>EvaluateLocatio</code> and it is not initialized:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/VTK/blob/fa5c98ca6c587c655543ec37f6a2936475ffc2e0/Filters/General/vtkDistancePolyDataFilter.cxx#L129">
  <header class="source">

      <a href="https://github.com/Kitware/VTK/blob/fa5c98ca6c587c655543ec37f6a2936475ffc2e0/Filters/General/vtkDistancePolyDataFilter.cxx#L129" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/fa5c98ca6c587c655543ec37f6a2936475ffc2e0/Filters/General/vtkDistancePolyDataFilter.cxx#L129" target="_blank" rel="noopener">Kitware/VTK/blob/fa5c98ca6c587c655543ec37f6a2936475ffc2e0/Filters/General/vtkDistancePolyDataFilter.cxx#L129</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="119" style="counter-reset: li-counter 118 ;">
          <li>int numCells = mesh-&gt;GetNumberOfCells();</li>
          <li>
          </li>
<li>vtkDoubleArray* cellArray = vtkDoubleArray::New();</li>
          <li>cellArray-&gt;SetName("Distance");</li>
          <li>cellArray-&gt;SetNumberOfComponents(1);</li>
          <li>cellArray-&gt;SetNumberOfTuples(numCells);</li>
          <li>
          </li>
<li>for (vtkIdType cellId = 0; cellId &lt; numCells; cellId++)</li>
          <li>{</li>
          <li>  vtkCell* cell = mesh-&gt;GetCell(cellId);</li>
          <li class="selected">  int subId;</li>
          <li>  double pcoords[3], x[3], weights[VTK_MAXIMUM_NUMBER_OF_POINTS];</li>
          <li>
          </li>
<li>  cell-&gt;GetParametricCenter(pcoords);</li>
          <li>  cell-&gt;EvaluateLocation(subId, pcoords, x, weights);</li>
          <li>
          </li>
<li>  double val = imp-&gt;EvaluateFunction(x);</li>
          <li>  double dist = SignedDistance ? (NegateDistance ? -val : val) : fabs(val);</li>
          <li>  cellArray-&gt;SetValue(cellId, dist);</li>
          <li>}</li>
          <li>
      </li>
</ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please report this to the VTK forum or bugtracker and post the link here for future reference.</p>
<p>There is a simple workaround: apply a vtkTriangleFilter on the tube filter output.</p>

---
