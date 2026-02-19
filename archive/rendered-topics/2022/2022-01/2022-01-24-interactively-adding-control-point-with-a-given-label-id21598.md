---
topic_id: 21598
title: "Interactively Adding Control Point With A Given Label"
date: 2022-01-24
url: https://discourse.slicer.org/t/21598
---

# Interactively adding control point with a given label

**Topic ID**: 21598
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/interactively-adding-control-point-with-a-given-label/21598

---

## Post #1 by @CsatiZoltan (2022-01-24 15:26 UTC)

<p>I build a user interface in which the user will click on the 3D scene (or the scenes of the three anatomical planes) and a fiducial node control point with a predetermined label will be placed.<br>
The problem is that I cannot set the label in the <code>slicer.modules.markups.logic().StartPlaceMode</code> function (there is no argument for that). A workaround I thought of is to place the control point with the label 3D Slicer automatically gives, and rename it after the point placement. To do so:</p>
<pre><code class="lang-python">slicer.modules.markups.logic().StartPlaceMode(0)
last_point_index = self.markup_node.GetNumberOfControlPoints() - 1
self.markup_node.SetNthControlPointLabel(last_point_index, my_preferred_label)
</code></pre>
<p>However, the last two lines get executed before the user can click on the scene. How can I pause the execution of the code until <code>StartPlaceMode</code> returns? The best solution would be my initial intention, i.e. being able to provide the label of the control point <em>before</em> placing it on the scene.</p>

---

## Post #2 by @cpinter (2022-01-24 15:48 UTC)

<p>I assume you use an older version of Slicer. In the latest version it is possible to pre-define fiducials with names. I haven’t used that feature yet personally but I assume the way to do that is to create a fiducial node with the points you want and keep them undefined. Then when the user clicks, the next undefined point will be defined.</p>

---

## Post #3 by @jamesobutler (2022-01-24 15:49 UTC)

<p>You may want to consider using a Markups Point List template. See the following linked post below. You can add undefined points to the list where you have predefined the name. Then when going into placement mode for this Point List node it will be going through the list to define the point location so will use your already defined labels.</p>
<aside class="quote quote-modified" data-post="2" data-topic="20870">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-create-markups-point-list-template-with-gui/20870/2">How to create Markups Point List template with GUI</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Under the control points advanced options, there is a button to add an unplaced point. Previously, it was supposed to add a point at the origin, but it had been broken for a while. It’s not very easy to find, maybe it should be moved to the main control points menu? 
[image]
  </blockquote>
</aside>


---

## Post #4 by @CsatiZoltan (2022-01-24 18:37 UTC)

<p>I have version <em>4.11.20210226</em> installed.<br>
By fiducial, do you mean the Markups node object or the control points that are defined within the active node? In case of the former, I can set the name at construction time, for the control points I cannot. Could you please send me a link to the relevant API doc entry?</p>

---

## Post #5 by @CsatiZoltan (2022-01-24 19:02 UTC)

<p>Thank you for the tip, that could work for me. However, following the <a href="https://www.youtube.com/watch?v=m-z9vNRIhxg" rel="noopener nofollow ugc">referenced video</a>, the button at 0:21 does not add control points (I can still add normal control points, so I don’t know why unnamed control points cannot be defined).<br>
Assuming that the issue above is solved, here is a follow-up question. Can I select programmatically which unnamed control point to add? E.g. when the user clicks on the pushbutton <code>P1</code>, the control point with label <code>P-1</code> will be placed by the mouse, while if he clicks on another pushbutton <code>P7</code>, the control point with label <code>P-7</code> will be added to the scene. Note that the order may change, i.e. the user might first click on <code>P7</code> and then on <code>P1</code>.</p>

---

## Post #6 by @lassoan (2022-01-24 20:04 UTC)

<p>If you have a markup point list template, you can set the index of an unplaced point that will be placed on the next click using <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#a3fbca86f7ca3d28616d60b974cdf13c0">SetControlPointPlacementStartIndex() method</a>.</p>

---

## Post #7 by @CsatiZoltan (2022-01-24 22:09 UTC)

<p>I cannot access that method from my <code>vtkMRMLMarkupsFiducialNode</code> object, which is strange as <code>SetControlPointPlacementStartIndex</code> is a public method of the <code>vtkMRMLMarkupsNode</code> class. Maybe it is not exposed to the Python interface? This is the traceback I get:</p>
<pre><code class="lang-python">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsFid' object has no attribute 'SetControlPointPlacementStartIndex'
</code></pre>
<p>My next try was looking into the source code to see what happens when I click on that button in the <em>Advanced</em> settings. Behind the scenes, <a href="https://github.com/Slicer/Slicer/blob/d36e96bd544db2489d624c85727194cde6da7484/Modules/Loadable/Markups/qSlicerMarkupsModuleWidget.cxx#L1528" rel="noopener nofollow ugc">that button</a> calls <a href="https://github.com/Slicer/Slicer/blob/d36e96bd544db2489d624c85727194cde6da7484/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.cxx#L686" rel="noopener nofollow ugc">this method</a> (again, not available through Python). But even that function seems to need the (R,A,S) triplet, so how can you instantiate an undefined control point?</p>

---

## Post #8 by @lassoan (2022-01-24 22:26 UTC)

<p>For all the features that we have been discussing here you need a recent Slicer Preview Release.</p>

---

## Post #9 by @CsatiZoltan (2022-01-24 22:42 UTC)

<p>Thank you, it works interactively with the latest preview release! I will try it tomorrow programmatically.</p>

---

## Post #10 by @CsatiZoltan (2022-01-25 11:08 UTC)

<p>I tried it, and it works just fine! All of you gave me very useful tips; since I can select only one solution, I accept the one from <a class="mention" href="/u/jamesobutler">@jamesobutler</a> as he pointed me to the GUI settings, which helped me find the corresponding implementation.</p>
<p>Here is an MWE so that others who stumble upon a similar problem can benefit from it.</p>
<ol>
<li>All the code enumerated below went into the <em>main.py</em> file, which was generated by the <em>Extension Wizard</em>.</li>
<li>Created a <strong>Markup</strong> node in the <code>setup</code> method of the class <code>mainWidget</code>. This is the node I will populate with the control points.<pre><code class="lang-python">node_id = slicer.modules.markups.logic().AddNewFiducialNode('your_label')
self.markup_node = slicer.mrmlScene.GetNodeByID(node_id)
</code></pre>
</li>
<li>Added the class variable <code>N_POINT = 9</code> into the class <code>mainWidget</code>, indicating the number of push buttons.</li>
<li>Initialized the control points by calling <code>self.initialize_points()</code> in the <code>setup method</code>. This function is defined as<pre><code class="lang-python">def initialize_points(self):
   slicer.modules.markups.logic().SetActiveListID(self.markup_node)
   self.markup_node.SetControlPointLabelFormat('P%d')
   for i in range(1, self.N_POINT + 1):
       self.markup_node.AddControlPoint([0, 0, 0])
   self.markup_node.UnsetAllControlPoints()
   self.markup_node.SetMaximumNumberOfControlPoints(self.N_POINT)
</code></pre>
</li>
<li>Created the nine push buttons in Qt Designer, and in the <code>setup</code> method I connected them with the function I want to execute. For instance, for button 4:<pre><code class="lang-python">self.ui.P4PushButton.connect('clicked(bool)', lambda: self.onPointPushButton('P4'))
</code></pre>
The function is defined as<pre><code class="lang-python">def onPointPushButton(self, button):
   slicer.modules.markups.logic().SetActiveListID(self.markup_node)
   n_point = self.markup_node.GetNumberOfControlPoints()
   index = None
   for i in range(n_point):
       label = self.markup_node.GetNthControlPointLabel(i)
       if label == button:
           index = i
           print('Index: ', index)
           break
   if not index:
       raise ValueError('Point {0} not found.'.format(button))
   self.markup_node.UnsetNthControlPointPosition(index)
   self.markup_node.SetControlPointPlacementStartIndex(index)
   self.markup_node.SetNthControlPointLabel(index, button)
   slicer.modules.markups.logic().StartPlaceMode(0)
</code></pre>
When writing this function, I was inspired by what the GUI does. Hence, I searched for the <a href="https://github.com/Slicer/Slicer/blob/d36e96bd544db2489d624c85727194cde6da7484/Modules/Loadable/Markups/qSlicerMarkupsModuleWidget.cxx#L1528" rel="noopener nofollow ugc">corresponding GUI function</a>.</li>
</ol>
<hr>
<p>I will polish this code (e.g. moving the non-GUI related stuff into the <code>mainLogic</code> class), though the main functionality works.<br>
One issue with this approach is that the control points are identified by labels, so if the user changes the label (e.g. by clicking on the markup in the scene and choosing <em>Rename control point…</em>), the control point is no longer found by the loop in the <code>onPointPushButton</code> method. Is there a way to disable the renaming, or better yet: identifying the control points by a kind of persistent property ?</p>

---

## Post #11 by @jamesobutler (2022-01-25 13:08 UTC)

<p>You can whitelist certain right-click context menu actions. See the following:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-whitelist-to-customize-view-menu" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-whitelist-to-customize-view-menu</a></p>

---

## Post #12 by @Saima (2023-04-26 04:49 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="21598">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>your already defined labels.</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Would it be possible to select the point (x,y,z) location in a ply file, for all the ply files opening up one by one and closing once the point is selected.<br>
The point needed to be selected by the user on the model and then the next model file opens up automatically and the user selects a point on that model and will do until points in all the ply files are selected. can this process be automated.</p>
<p>Thank you</p>
<p>regards,<br>
Saima</p>

---

## Post #13 by @lassoan (2023-04-30 13:50 UTC)

<p>Yes, this can be very easily automated. Examples for all the necessary operations (loading a model, adding a markup point list, observing a markup node to get notified about changes) are available in the script repository but if you get stuck with automation of any specific step then let us know.</p>

---

## Post #14 by @Saima (2023-05-09 04:17 UTC)

<p>Hi Andras,<br>
I started working on the script. I loaded models from a given folder. used a for loop to load models one by one.</p>
<p>But i do not get the control point selection for each model.<br>
How can I stop for loop to get input from user first and then iterate the next one.<br>
The code is below:</p>
<p>import time<br>
startTime = time.time()<br>
logging.info(‘Processing started’)<br>
logging.info(‘Search for .ply files’)<br>
modelDir = inputDir<br>
modelFileExt = “ply”</p>
<pre><code>    import math
    import os
    
    modelFiles = list(f for f in os.listdir(modelDir) if f.endswith("."+modelFileExt))
    print(modelFiles)
    
    #load models and show in 3D view
    for modelIndex, modelFile in enumerate(modelFiles):
        name = os.path.basename(modelFile)
        modelNode = slicer.util.loadModel(modelDir + "/" + modelFile)
        placeModePersistence = 1
        slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)    
        markup_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
        placeModePersistence = 0
        slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)    
        #slicer.util.updateMarkupsControlPointsFromArray(markup_node, np.random.rand(10,3))
        #markup_node.GetDisplayNode().SetTextScale(0)    
        markup_node.GetDisplayNode().SetPointLabelsVisibility(False)
</code></pre>

---

## Post #15 by @lassoan (2023-05-09 04:22 UTC)

<p>You don’t need a loop. Instead, you can add an observer to the markup node. If an event invoked that indicates a new point is added then in your callback function you save the point and load the next model.</p>

---

## Post #16 by @Saima (2023-05-09 04:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="21598">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ed a loop. Instead, you can add an observer to the markup node.</p>
</blockquote>
</aside>
<p>could you please refer to the script for adding an observer.</p>
<p>Thanks alot.</p>
<p>regards,<br>
Saima</p>

---

## Post #17 by @Saima (2023-05-09 04:39 UTC)

<p>Do i need to keep the index for modelFiles[index] and pass it through the function in addObserver.</p>
<p>modelFiles = list(f for f in os.listdir(modelDir) if f.endswith(“.”+modelFileExt))<br>
print(modelFiles)</p>
<pre><code>    #load models and show in 3D view
    #for modelIndex, modelFile in enumerate(modelFiles):
    global index = 0
    name = os.path.basename(modelFile)
    modelNode = slicer.util.loadModel(modelDir + "/" + modelFiles[index])
    placeModePersistence = 1
    slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)    
    markup_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
    updateindex
    markup_node.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, onMarkupsAdded, index)
</code></pre>
<p>and in the function onMarkupsAdded I load the next model. right?</p>

---

## Post #18 by @Saima (2023-05-09 06:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="21598">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ew point is added then in your callback function you save the point and load the</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Could you please refer to the code snippets or scripts of what you suggested?</p>
<p>thank you</p>

---

## Post #19 by @lassoan (2023-05-09 10:57 UTC)

<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>It is probably better to observe the new point definition event instead of any point modification.</p>
<p>This observation would immediately switch to the next case when you add the point, therefore you could not adjust the point after placement. So, maybe it is better to add a keyboard shortcut for going to the next case.</p>

---

## Post #20 by @Saima (2023-05-11 02:32 UTC)

<p>is new point definition event is PointAddedEvent?<br>
Also, I want to explore the model in the 3D view before placing a point on the model but because the mouse is in the fiducial placement mode I cant do that. whats the solution?</p>
<p>regards,<br>
Saima</p>

---

## Post #21 by @Saima (2023-05-11 04:59 UTC)

<p>not getting what I require. What is the problem in the code. doesnt load models one by one when ever the new event occurs (new event is the adding of a fiducial for a each model)</p>
<pre><code class="lang-auto">def onMarkupsAdded(self, caller, event):
        index=0
        print(index)
        index+=1
        modelFileExt = "ply"
        print(index)
        modelDir = "/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/Case1"
        modelFiles = list(f for f in os.listdir(modelDir) if f.endswith("."+modelFileExt))
        print(modelFiles)
        placeModePersistence = 0
        slicer.modules.markups.logic().StartPlaceMode(placeModePersistence) 
        modelNode = slicer.util.loadModel(modelDir + "/" + modelFiles[index])
def process(self, inputDir, inputVolume, outputVolume):
        """
        Run the processing algorithm.
        Can be used without GUI widget.
        :param inputVolume: volume to be thresholded
        :param outputVolume: thresholding result
        :param imageThreshold: values above/below this threshold will be set to 0
        :param invert: if True then values above the threshold will be set to 0, otherwise values below are set to 0
        :param showResult: show output volume in slice viewers
        """
        global index
        print(inputDir)
        if not inputVolume or not outputVolume:
            raise ValueError("Input or output volume is invalid")

        import time
        startTime = time.time()
        logging.info('Processing started')
        logging.info('Search for .ply files')
        modelDir = inputDir
        modelFileExt = "ply"
        
        import math
        import os
        
        modelFiles = list(f for f in os.listdir(modelDir) if f.endswith("."+modelFileExt))
        print(modelFiles)
        
        #load models and show in 3D view
        #for modelIndex, modelFile in enumerate(modelFiles):
        index = 0
        #name = os.path.basename(modelFiles)
        modelNode = slicer.util.loadModel(modelDir + "/" + modelFiles[index])
        placeModePersistence = 1
        slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)    
        markup_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
        
        markup_node.AddObserver(slicer.vtkMRMLMarkupsNode.PointAddedEvent, self.onMarkupsAdded)
</code></pre>

---

## Post #22 by @lassoan (2023-05-13 16:33 UTC)

<p>My first thought was that you would load the next model immediately when you placed the point, but actually you only want to switch to the next model when you confirmed that the markup was placed at the correct position (you rotate the view around and adjust the point position as needed). So, instead of observing the point added event, I would recommend to switch to the next model using a keyboard shortcut.</p>
<p>In the function that is executed by thr keyboard shortcut, you can check the number of points in the markup point list and from that you would know how many models are annotated already and load the next one.</p>

---

## Post #23 by @Saima (2023-05-15 02:41 UTC)

<p>Any examples of keyboard shortcut.</p>
<p>regards,<br>
Saima</p>

---

## Post #24 by @lassoan (2023-05-21 00:23 UTC)

<p>There are several examples for keyboard shortcuts in the script repository.</p>

---

## Post #25 by @Saima (2023-05-30 05:08 UTC)

<p>in the keyboard shortcut, is there a possibility to pass arguments to the called function.</p>
<p>shortcut = qt.QShortcut(slicer.util.mainWindow())<br>
shortcut.setKey(qt.QKeySequence(“s”))<br>
shortcut.connect( “activated()”, self.switchNextModel, like here can we pass arguments)</p>

---

## Post #26 by @Saima (2023-05-30 05:16 UTC)

<p>Here are the steps needed int he module:</p>
<ol>
<li>search for the .ply files in the folder</li>
<li>load the first model from the list</li>
<li>rotate model and select the location<br>
turn the mouse pointer to fiducial placement mode (should I use keyboard shortcut here or what is best to use)</li>
<li>add a point to the selected location</li>
<li>save the location coordinated to the output .txt file</li>
<li>clear the view window</li>
<li>load the next model and repeat</li>
</ol>
<p>when using keyboard shortcut can I save the point in the file can i pass the argument.</p>
<p>I think I would need to clear the view before loading another model and selecting the point in that model.</p>

---

## Post #29 by @Saima (2023-05-31 03:38 UTC)

<p>Hi Andras,<br>
I am stuck at the following</p>
<p>I have the model loaded and the user can scroll to select the position to put the point.</p>
<p>adding markup and then adding the user defined number of control points for a given model.</p>
<p>how should i proceed with this scenario?</p>
<p>regards,<br>
Saima</p>

---

## Post #30 by @lassoan (2023-05-31 04:23 UTC)

<p>It is unclear for me what is that you already have and what is that you have trouble implementing.</p>

---

## Post #31 by @Saima (2023-05-31 04:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="21598">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>at you already have and what is that you have trouble implementing.</p>
</blockquote>
</aside>
<p>I am not understanding how the user will add the markup control points after locating the position on the model. I want to set the number of control points as well for a given model not just one control point for all models. For example in future user can adjust the number of control points to be added for a given model.</p>
<p>after adding the specified number of control points I will use keyboard shortcut to move to next model.</p>
<p>I am stuck with the adding of control points by the user. what is the best way to add the control points.<br>
Should there be a button to select for adding control points or a keyboard shortcut to add control points.<br>
and would be switching between node placement mode for control points.</p>
<p>Please let me know how to proceed.</p>
<p>Thank you</p>
<p>regards,<br>
Saima</p>

---

## Post #32 by @Saima (2023-06-01 04:11 UTC)

<p>Hi Andras,<br>
I have the following code but the keyboard shortcut not working. Could you please help.</p>
<p>modelNode = slicer.util.loadModel(modelDir + “/” + modelFiles[index])<br>
node_id = slicer.modules.markups.logic().AddNewFiducialNode(‘modelFileName’)<br>
self.markup_node = slicer.mrmlScene.GetNodeByID(node_id)<br>
self.initialize_points()</p>
<pre><code>import qt
shortcut1 = qt.QShortcut(qt.QKeySequence('p'), slicer.util.mainWindow())
shortcut1.connect("activated()", self.addNewNode)             
</code></pre>
<p>The initialize_points function is below:<br>
N_POINT = 3<br>
def initialize_points(self):<br>
slicer.modules.markups.logic().SetActiveListID(self.markup_node)<br>
self.markup_node.SetControlPointLabelFormat(‘P%d’)<br>
for i in range(1, self.N_POINT + 1):<br>
self.markup_node.AddControlPoint([0, 0, 0])<br>
self.markup_node.UnsetAllControlPoints()<br>
self.markup_node.SetMaximumNumberOfControlPoints(self.N_POINT)</p>
<p>The addNewNode function is below: I want this function to do the following 1) convert mouse cursor to control point placement mode and then add no more than N_POINT.</p>
<p>def addNewNode(self):<br>
slicer.modules.markups.logic().SetActiveListID(self.markup_node)<br>
n_point = self.markup_node.GetNumberOfControlPoints()<br>
placeModePersistence = 1<br>
slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)</p>
<pre><code>    for i in range(n_point):
        self.markup_node.UnsetNthControlPointPosition(i)
        self.markup_node.SetControlPointPlacementStartIndex(i)
        self.markup_node.SetNthControlPointLabel(index, "p"+i)
        
    slicer.modules.markups.logic().StartPlaceMode(0)
</code></pre>

---

## Post #33 by @lassoan (2023-07-02 11:38 UTC)

<p>This is too much code and to fragmented to copy-paste. If you send a link to your module source code on Github then I can have a look and give you some feedback.</p>

---

## Post #34 by @Saima (2023-07-10 03:32 UTC)

<p>Hi Andras,<br>
I have added the code on github and added you in collaboration.<br>
can you see the code?</p>
<p>Please let me know.<br>
The switchnextmodel is not working with the shortcut key.<br>
how can I get access to the df variable created. it is a list of models and I am keeping track using this list for the next model to . be uploaded.<br>
How to lock the control points when the user move the model to locate the point</p>
<p>regards,<br>
Saima</p>

---

## Post #35 by @Saima (2023-07-10 03:33 UTC)

<p>Hi Andras,<br>
I have added the code on github and added you in collaboration.<br>
can you see the code?</p>
<p>Please let me know.<br>
The switchnextmodel is not working with the shortcut key.<br>
how can I get access to the df variable created. it is a list of models and I am keeping track using this list for the next model to . be uploaded.<br>
How to lock the control points when the user move the model to locate the point</p>
<p>regards,<br>
Saima</p>

---

## Post #36 by @Saima (2023-08-07 01:25 UTC)

<p>Hi Andras,<br>
I am putting the fiducials at each vertex for all the cells (triangles) in a surface model. I am using the following code. I need this for the next step where user needs to select a point in a surface model.</p>
<p>Problem: its very very time consuming to create a markup file for all the models (4000).</p>
<p>How can I improve the following code? or is there any way to highlight the vertices for all the cells in a model instead of looping through each cell and than creating a point at each vertex.</p>
<p>def process(self, dataDirectoryPath, showResult=True):<br>
“”"<br>
Run the processing algorithm.<br>
Can be used without GUI widget.<br>
:param dataDirectoryPath: path to the data directory containing .ply files</p>
<pre><code>    """

    if not dataDirectoryPath:
        raise ValueError("no Data folder selected")

    import time
    startTime = time.time()
    logging.info('Processing started')
    logging.info('Search for .ply files')
    modelDir = dataDirectoryPath
    modelFileExt = "ply"
    modelFiles = list(f for f in os.listdir(modelDir) if f.endswith("."+modelFileExt))
    print(modelFiles)
    import pandas as pd
    
    #dataframe to store all the ply files name along with index
    df = pd.DataFrame(modelFiles, columns =['FileNames'])
    filepath = dataDirectoryPath+'/models_ids.csv'
    df.to_csv(filepath, index=True)
    
    idFile = 0
    for idFile in range(idFile,len(df)):
        print(df.iloc[idFile].FileNames)
        markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
        markupsNode.CreateDefaultDisplayNodes()
        
        modelFileName =  df.iloc[idFile].FileNames
        modelNode = slicer.util.loadModel(dataDirectoryPath+ "/" + modelFileName)
        size = len(modelFileName)
        modelFileName = modelFileName[:size - 4]
        print(modelFileName)
        markupsNode.SetName(modelFileName)
        print(df.index.get_loc(idFile))
        
        meshModel = modelNode.GetMesh()
        points = meshModel.GetPoints()
        nPoints = points.GetNumberOfPoints()
        for i in range(nPoints):
            p = points.GetPoint(i)
            markupsNode.AddControlPoint(p[0],p[1],p[2])
            markupsNode.SetNthControlPointLocked(i, True)
            
            
        d = markupsNode.GetDisplayNode()
        d.PointLabelsVisibilityOff()
        #saving the markup point and cleaning the scene
        slicer.util.saveNode(markupsNode, os.path.join(dataDirectoryPath, modelFileName+".mrk.json"))
        slicer.mrmlScene.Clear(0)
   
    

    stopTime = time.time()
    logging.info(f'Processing completed in {stopTime-startTime:.2f} seconds')
</code></pre>
<p>regards,<br>
saima</p>

---

## Post #37 by @lassoan (2023-08-07 07:49 UTC)

<p>Your can draw a glyph, such as a small sphere at each point of a mesh using vtkGlyph3D filter.</p>

---

## Post #38 by @Saima (2023-08-08 05:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="37" data-topic="21598">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>our can draw a glyph, such as a small sphere at each point of a mesh using vtkGlyph3D filte</p>
</blockquote>
</aside>
<p>In the next step after creating all these points, there is another program where the user select the point and the respective point coordinates are saved in a file.</p>
<p>can i still retrieve the point coordinates with the glyph?<br>
Any example scripts?</p>
<p>regards,<br>
saima safdar</p>

---
