# Can Python interpretor be used to call Slicer IGT "create models" ?

**Topic ID**: 20948
**Date**: 2021-12-07
**URL**: https://discourse.slicer.org/t/can-python-interpretor-be-used-to-call-slicer-igt-create-models/20948

---

## Post #1 by @clement_laplace (2021-12-07 13:44 UTC)

<p>Hello,</p>
<p>I am a fairly new user of 3D Slicer. I was wondering if it is possible to call the “CreateModels” functions of the Slicer IGT module from a python script.<br>
I need to create cylinder models in a more automated way, thus I wanted to combine python and Slicer IGT for this.</p>
<p>A more general questions: Can all the modules be called from python ?</p>
<p>Thank you</p>

---

## Post #2 by @mikebind (2021-12-08 23:11 UTC)

<p>The short answer is yes, all Slicer modules can be accessed from python.</p>
<p>Here’s a very long answer: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/index.html" class="inline-onebox">Developer Guide — 3D Slicer documentation</a></p>
<p>Self tests can be a good place to look to try to find examples of code in use.  Here’s one I found which seems to use the IGT create models functionality in a basic way:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/blob/983b9f08efa201df6f44a94d8f6b4a3d220bde86/BreachWarning/Testing/Python/BreachWarningSelfTest.py#L86">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/983b9f08efa201df6f44a94d8f6b4a3d220bde86/BreachWarning/Testing/Python/BreachWarningSelfTest.py#L86" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/983b9f08efa201df6f44a94d8f6b4a3d220bde86/BreachWarning/Testing/Python/BreachWarningSelfTest.py#L86" target="_blank" rel="noopener">SlicerIGT/SlicerIGT/blob/983b9f08efa201df6f44a94d8f6b4a3d220bde86/BreachWarning/Testing/Python/BreachWarningSelfTest.py#L86</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="76" style="counter-reset: li-counter 75 ;">
          <li>One of the most important features of the tests is that it should alert other</li>
          <li>developers when their changes will have an impact on the behavior of your</li>
          <li>module.  For example, if a developer removes a feature that you depend on,</li>
          <li>your test should break so they know that the feature is needed.</li>
          <li>"""</li>
          <li>
          </li>
<li>slicer.util.delayDisplay("Starting the test")</li>
          <li>
          </li>
<li>slicer.util.delayDisplay("Create models")</li>
          <li>modelNodes = []</li>
          <li class="selected">createModelsLogic = slicer.modules.createmodels.logic()</li>
          <li>sphereRadius = 10.0</li>
          <li>sphereModel = createModelsLogic.CreateSphere(sphereRadius) # watched model</li>
          <li>toolModel = createModelsLogic.CreateNeedle(50.0, 1.5, 0.0, False)</li>
          <li>
          </li>
<li>slicer.util.delayDisplay("Set up module GUI")</li>
          <li>mainWindow = slicer.util.mainWindow()</li>
          <li>mainWindow.moduleSelector().selectModule('BreachWarning')</li>
          <li>bwWidget = slicer.modules.breachwarning.widgetRepresentation()</li>
          <li>bwColorPickerButton = slicer.util.findChildren(widget=bwWidget, className='ctkColorPickerButton', name='WarningColorPickerButton')[0]</li>
          <li>bwModelNodeCombobox = slicer.util.findChildren(widget=bwWidget, name='ModelNodeComboBox')[0]</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Here is the C++ code for the Create Models module: <a href="https://github.com/SlicerIGT/SlicerIGT/blob/39dfcfa3c83e07981054b6e2164c5f26552b93bb/CreateModels/Logic/vtkSlicerCreateModelsLogic.cxx" class="inline-onebox">SlicerIGT/vtkSlicerCreateModelsLogic.cxx at 39dfcfa3c83e07981054b6e2164c5f26552b93bb · SlicerIGT/SlicerIGT · GitHub</a></p>
<p>Those C++ functions are wrapped and accessible via python.</p>

---
