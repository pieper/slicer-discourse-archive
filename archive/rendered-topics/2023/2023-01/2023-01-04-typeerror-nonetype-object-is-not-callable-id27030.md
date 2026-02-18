# TypeError: 'NoneType' object is not callable

**Topic ID**: 27030
**Date**: 2023-01-04
**URL**: https://discourse.slicer.org/t/typeerror-nonetype-object-is-not-callable/27030

---

## Post #1 by @LuisaDantas (2023-01-04 14:26 UTC)

<p>Hey all,</p>
<p>I’m developing a module to Slicer and I’m facing some issues. One of the functionalities is to place a control point and get its coordinates through a button that calls a method. I put a <code>print</code> on the beggining of this method and it’s called right when I start the module, but when I place de control point and click the button it gives this error: <code>TypeError: 'NoneType' object is not callable</code></p>
<pre><code class="lang-auto">def setup(self):
      
        ScriptedLoadableModuleWidget.setup(self)

        uiWidget = slicer.util.loadUI(self.resourcePath('UI/Module.ui'))
        self.layout.addWidget(uiWidget)
        self.ui = slicer.util.childWidgetVariables(uiWidget)

        markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
        self.ui.PontoCentralButton.setCurrentNode(markupsNode)
        self.ui.PontoCentralButton.buttonsVisible=False
        self.ui.PontoCentralButton.placeButton().show()
        self.ui.PontoCentralButton.placeMultipleMarkups = slicer.qSlicerMarkupsPlaceWidget.ForcePlaceSingleMarkup

        uiWidget.setMRMLScene(slicer.mrmlScene)

# [...]

        # Buttons
        self.ui.CoordsButton.connect("clicked(bool)", self.logic.coordCentral(self.ui.MRMLNodeComboBox_frame.currentNode(),markupsNode))
</code></pre>
<pre><code class="lang-auto">def coordCentral(self, inputFrame, markupsNode):
        print("method called ")
</code></pre>

---

## Post #2 by @jamesobutler (2023-01-04 15:17 UTC)

<p>My guess is that <code>self.ui.MRMLNodeComboBox_frame</code> is the NoneType object. Make sure your UI file has this object with this exact objectName of MRMLNodeComboBox_frame and that you have saved this UI file (not unsaved changes).</p>

---

## Post #3 by @LuisaDantas (2023-01-04 16:17 UTC)

<p>Hi James, I checked that but it’s the exact same name. And the .ui file is saved too</p>

---

## Post #4 by @jamesobutler (2023-01-04 17:54 UTC)

<p>I would suggest you do some continued debugging to find the NoneType object. Adding a print statement for <code>self.ui.MRMLNodeComboBox_frame</code> will help confirm if it is indeed an object or a NoneType.</p>

---

## Post #5 by @LuisaDantas (2023-01-05 12:05 UTC)

<p>I printed the <code>inputFrame</code> on <code>coordCentral</code>, where <code>inputFrame = self.ui.MRMLNodeComboBox_frame</code> and it returned this:</p>
<pre><code class="lang-auto">vtkMRMLViewNode (000001CC95966B90)
  ID: vtkMRMLViewNode1
  ClassName: vtkMRMLViewNode
  Name: View1
  Debug: false
  MTime: 227115
  Description: (none)
  SingletonTag: 1
  HideFromEditors: false
  Selectable: true
  Selected: false
  UndoEnabled: false
  Attributes:
    MappedInLayout:1
  Node references:
    InteractionNodeRef: (none)
    ParentLayoutNodeRef: (none)
  LayoutLabel: 1
  ViewGroup: 0
  Active: 0
  Visibility: 1
  BackgroundColor: (0.756863, 0.764706, 0.909804)
  BackgroundColor2: (0.454902, 0.470588, 0.745098)
  LayoutColor: (0.454902, 0.513725, 0.913725)
  OrientationMarkerType: none
  OrientationMarkerSize: medium
  RulerType: none
  RulerColor: white
   AxisLabels: L;R;P;A;I;S
  FieldOfView: 200
  LetterSize: 0.05
  BoxVisible: true
  BoxColor: (1, 0, 1)
  FiducialsVisible: true
  FiducialLabelsVisible: true
  AxisLabelsVisible: true
  AxisLabelsCameraDependent: true
  AnimationMode: Off
  ViewAxisMode: LookFrom
  SpinDegrees: 2
  AnimationMs: 5
  SpinDirection: YawLeft
  RotateDegrees: 5
  RockLength: 200
  RockCount: 0
  StereoType: NoStereo
  RenderMode: Perspective
  UseDepthPeeling: 1
  GPUMemorySize: 0
  AutoReleaseGraphicsResources: false
  ExpectedFPS: 8
  VolumeRenderingQuality: 1
  RaycastTechnique: 0
  VolumeRenderingSurfaceSmoothing: 0
  VolumeRenderingOversamplingFactor: 2
  Interacting: 0
  LinkedControl: 0
</code></pre>
<p>From <code>Description: (none)</code> it seems to be a NoneType right? But again the method was called right when the module started, before selecting the input node and placing the control point. So I’m guessing that’s why it’s NoneType.</p>
<p>Don’t know why this is happening.</p>

---

## Post #6 by @cpinter (2023-01-05 12:20 UTC)

<p>Please copy-paste the whole error message you get. Without it it is only possible to keep guessing around.</p>

---

## Post #7 by @rbumm (2023-01-05 12:35 UTC)

<p>You seem to be using</p>
<pre><code class="lang-auto">self.ui.PontoCentralButton
</code></pre>
<p>and</p>
<pre><code class="lang-auto">self.ui.CoordsButton
</code></pre>
<p>in your example, which will probably not work …</p>

---

## Post #8 by @LuisaDantas (2023-01-05 12:37 UTC)

<p>I copied on the original qustion: <code>TypeError: 'NoneType' object is not callable</code></p>
<p>There’s nothing else.</p>

---

## Post #9 by @LuisaDantas (2023-01-05 12:47 UTC)

<p>They are different things actually. I don’t know if that’s the most effiecient way because I’m new to Slicer but the idea is: the user place a control point trought the Markups Control Point button (<code>PontoCentralButton</code>), and when it’s placed they click on the “Coordenadas” button (<code>CoordsButton</code>), wich should call the method and get the coordinates of that control point.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/236c59c254db88eb57b2cb4d0da63ae95fcb7102.png" alt="image" data-base62-sha1="53mQNywHCUa5TG7EBWHpbQS51kK" width="469" height="152"></p>
<p>Hope this helps to give more context to the problem.</p>

---

## Post #10 by @rbumm (2023-01-05 13:20 UTC)

<p>Please put your function into the YourExtensionWidget class, not into the YourExtensionLogic.</p>
<p>Connect it like:</p>
<pre><code class="lang-auto">      self.ui.toggleButton.connect('clicked(bool)', self.onToggleButton)
</code></pre>
<p>Hope that helps.</p>

---

## Post #11 by @LuisaDantas (2023-01-05 13:35 UTC)

<p>Unfortunately the same behavior happens <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"><br>
I made <code>onToggleButton</code> call the processing function on the Logic class too, but it didn’t work either.</p>

---

## Post #12 by @rbumm (2023-01-05 13:55 UTC)

<p>Maybe you can print the coordinates of your markup <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates">like described here</a> and avoid passing the view argument.</p>

---

## Post #13 by @LuisaDantas (2023-01-05 14:14 UTC)

<p>Great, I’ll try that and let you know if it works, thanks!</p>

---
