---
topic_id: 7840
title: "Updated Sample Code For Calling Cli Via C"
date: 2019-08-01
url: https://discourse.slicer.org/t/7840
---

# Updated sample code for calling CLI via C++

**Topic ID**: 7840
**Date**: 2019-08-01
**URL**: https://discourse.slicer.org/t/updated-sample-code-for-calling-cli-via-c/7840

---

## Post #1 by @rprueckl (2019-08-01 18:14 UTC)

<p>Hello,<br>
below is an updated example that shows how to call a CLI module from C++. I used the code from the link, but it seems to be quite old. So, i you want an update, please take my code (with any modification).</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel/Programmatic_Invocation" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel/Programmatic_Invocation</a></p>
<pre><code class="lang-auto">void MyWidget::generate3dModel()
{
    Q_D(MyWidget);
    vtkMRMLScene* scene = qSlicerCoreApplication::application()-&gt;mrmlScene();

    // get module and its widget
    qSlicerCLIModule* cliModule = static_cast&lt;qSlicerCLIModule*&gt;(qSlicerCoreApplication::application()-&gt;moduleManager()-&gt;module("GrayscaleModelMaker"));
    qSlicerCLIModuleWidget *cliWidget = static_cast&lt;qSlicerCLIModuleWidget*&gt;(cliModule-&gt;widgetRepresentation());
    vtkSlicerCLIModuleLogic* moduleLogic = vtkSlicerCLIModuleLogic::SafeDownCast(cliModule-&gt;logic());

    // get/create CLI module node
    vtkMRMLCommandLineModuleNode* cliNode = moduleLogic-&gt;CreateNodeInScene();

    // get/create output node
    QString outputNodeID(this-&gt;volumeNode()-&gt;GetID());
    outputNodeID += "Model";
    vtkMRMLModelNode* outputNode = vtkMRMLModelNode::SafeDownCast(scene-&gt;GetFirstNodeByName(outputNodeID.toStdString().c_str()));
    if (!outputNode)
    {
        outputNode = vtkMRMLModelNode::SafeDownCast(scene-&gt;CreateNodeByClass("vtkMRMLModelNode"));
        outputNode-&gt;SetName(outputNodeID.toStdString().c_str());
        
        // Add node to the scene
        scene-&gt;AddNode(outputNode);
        outputNode-&gt;Delete();
    }

    // extract threshold from volume display node
    vtkMRMLScalarVolumeDisplayNode* VolumeDisplayNode = vtkMRMLScalarVolumeDisplayNode::SafeDownCast(this-&gt;volumeNode()-&gt;GetDisplayNode());
    double threshold = VolumeDisplayNode-&gt;GetLowerThreshold();
    
    // set parameters
    cliNode-&gt;SetParameterAsNode("InputVolume", this-&gt;volumeNode());
    cliNode-&gt;SetParameterAsNode("OutputGeometry", outputNode);
    cliNode-&gt;SetParameterAsFloat("Threshold", threshold);
    cliNode-&gt;SetParameterAsString("Name", outputNodeID.toStdString().c_str());
    cliNode-&gt;SetParameterAsInt("Smooth", 15); // default
    cliNode-&gt;SetParameterAsFloat("Decimate", 0.25f); // default
    cliNode-&gt;SetParameterAsBool("SplitNormals", true); // default
    cliNode-&gt;SetParameterAsBool("PointNormals", true); // default

    // connect cli widget with cli module node
    cliWidget-&gt;setCurrentCommandLineModuleNode(cliNode);

    // Connect node modified event to the update the progress bar and to proceed to the next step
    this-&gt;qvtkConnect(cliNode, vtkCommand::ModifiedEvent, this, SLOT(on3dModelGenerationProgress(vtkObject*)));

    // start via logic
    moduleLogic-&gt;Apply(cliNode);
}

void MyWidget::on3dModelGenerationProgress(vtkObject* cliNode)
{
    Q_D(MyWidget);

    vtkMRMLCommandLineModuleNode * node = vtkMRMLCommandLineModuleNode::SafeDownCast(cliNode);
    if (node)
    {
        // Update Progress
        ModuleProcessInformation* info = node-&gt;GetModuleDescription().GetProcessInformation();
        switch (node-&gt;GetStatus())
        {
        case vtkMRMLCommandLineModuleNode::Cancelled:
            d-&gt;cliProgressBar-&gt;setMaximum(0);
            break;
        case vtkMRMLCommandLineModuleNode::Scheduled:
            d-&gt;cliProgressBar-&gt;setMaximum(0);
            break;
        case vtkMRMLCommandLineModuleNode::Running:
            d-&gt;cliProgressBar-&gt;setMaximum(info-&gt;Progress != 0.0 ? 100 : 0);
            d-&gt;cliProgressBar-&gt;setValue(info-&gt;Progress * 100.);
            break;
        case vtkMRMLCommandLineModuleNode::Completed:
        case vtkMRMLCommandLineModuleNode::CompletedWithErrors:
            d-&gt;cliProgressBar-&gt;reset();
            this-&gt;qvtkDisconnect(cliNode, vtkCommand::ModifiedEvent, this, SLOT(on3dModelGenerationProgress(vtkObject*)));
            break;
        default:
        case vtkMRMLCommandLineModuleNode::Idle:
            d-&gt;cliProgressBar-&gt;reset();
            break;
        }
    }
}
</code></pre>
<p>I have one question to this: where would be the right place to remove the vtkMRMLCommandLineModuleNode again after execution? I tried to remove it in the <code>case vtkMRMLCommandLineModuleNode::Completed:</code> case, but the program crashed…</p>

---

## Post #2 by @lassoan (2019-08-01 21:26 UTC)

<p>The VTK object that invoked an event should not be deleted in the callback of that event. You can set a single-shot QTimer with 0 timeout to clean up the temporary nodes after the callback is completed.</p>

---

## Post #3 by @rprueckl (2019-08-02 12:45 UTC)

<p>I updated the code slightly (removed my own callback and used qSlicerCLIProgressBar):</p>
<pre><code class="lang-auto">Q_D(CxScalarVolumeDisplayWidget);
    vtkMRMLScene* scene = qSlicerCoreApplication::application()-&gt;mrmlScene();

    // get module and its widget
    qSlicerCLIModule* cliModule = static_cast&lt;qSlicerCLIModule*&gt;(qSlicerCoreApplication::application()-&gt;moduleManager()-&gt;module("GrayscaleModelMaker"));
    qSlicerCLIModuleWidget *cliWidget = static_cast&lt;qSlicerCLIModuleWidget*&gt;(cliModule-&gt;widgetRepresentation());
    vtkSlicerCLIModuleLogic* moduleLogic = vtkSlicerCLIModuleLogic::SafeDownCast(cliModule-&gt;logic());

    if (!d-&gt;cliNode)
    {
        // create CLI module node
        d-&gt;cliNode = moduleLogic-&gt;CreateNodeInScene();
        d-&gt;cliNode-&gt;Register(d);

        // get/create output node
        QString outputNodeID(this-&gt;volumeNode()-&gt;GetID());
        outputNodeID += "Model";
        vtkMRMLModelNode* outputNode = vtkMRMLModelNode::SafeDownCast(scene-&gt;GetFirstNodeByName(outputNodeID.toStdString().c_str()));
        if (!outputNode)
        {
            outputNode = vtkMRMLModelNode::SafeDownCast(scene-&gt;CreateNodeByClass("vtkMRMLModelNode"));
            outputNode-&gt;SetName(outputNodeID.toStdString().c_str());
        
            // Add node to the scene
            scene-&gt;AddNode(outputNode);
            outputNode-&gt;Delete();
        }

        // extract threshold from volume display node
        vtkMRMLScalarVolumeDisplayNode* VolumeDisplayNode = vtkMRMLScalarVolumeDisplayNode::SafeDownCast(this-&gt;volumeNode()-&gt;GetDisplayNode());
        double threshold = VolumeDisplayNode-&gt;GetLowerThreshold();
    
        // set parameters
        d-&gt;cliNode-&gt;SetParameterAsNode("InputVolume", this-&gt;volumeNode());
        d-&gt;cliNode-&gt;SetParameterAsNode("OutputGeometry", outputNode);
        d-&gt;cliNode-&gt;SetParameterAsFloat("Threshold", threshold);
        d-&gt;cliNode-&gt;SetParameterAsString("Name", outputNodeID.toStdString().c_str());
        d-&gt;cliNode-&gt;SetParameterAsInt("Smooth", 15); // default
        d-&gt;cliNode-&gt;SetParameterAsFloat("Decimate", 0.25f); // default
        d-&gt;cliNode-&gt;SetParameterAsBool("SplitNormals", true); // default
        d-&gt;cliNode-&gt;SetParameterAsBool("PointNormals", true); // default

        // connect cli widget with cli module node
        cliWidget-&gt;setCurrentCommandLineModuleNode(d-&gt;cliNode);

        // connect to qSlicerCLIProgressBar
        progressBar-&gt;setCommandLineModuleNode(d-&gt;cliNode);

        // start via logic
        moduleLogic-&gt;Apply(d-&gt;cliNode);
    }
</code></pre>

---

## Post #4 by @lassoan (2019-08-02 14:43 UTC)

<p>Thank you for sharing this.</p>
<p>It is an important design principle that all processing must be implemented in a module’s logic class, and not in the user interface. This decoupling of GUI from logic allows performing batch processing (without instantiating GUI) or using a module from another module. There are a few more similar principles - see development tutorial <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="nofollow noopener">here</a>.</p>
<p>Therefore, a few suggestions:</p>
<ul>
<li>Do not retreive or use cliWidget. A module’s widget should never be used from another module.</li>
<li>Node ID gets assigned automatically when a node is added to the scene and must not be get or set manually. To create an output model node, add it to the scene, and retrieve the object point, use <code>vtkMRMLNode* outputModelNode = scene-&gt;AddNewNodeByClass("vtkMRMLModelNode");</code> (this single line replaces 5-10 lines in your code)</li>
<li>All data processing should happen in your module logic, not in the GUI (widget) class, so move <code>Generate3dModel</code> method to your module logic and call that method from the GUI. See for example how it is done in <a href="https://github.com/Slicer/Slicer/blob/b0a932cc4b3a9d674c64f37a13a3b47144274b69/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.cxx#L415-L416" rel="nofollow noopener">Crop Volume module</a>. If you need progress bar or execution in the background then you can return the created CLI module node to the caller.</li>
</ul>
<p>Trivial: There is no “Name” parameter of Grayscale Model Maker module, so you can remove setting of that parameter.</p>

---

## Post #5 by @rprueckl (2019-08-06 11:31 UTC)

<p>Thanks for elaborating on this.</p>
<ul>
<li>I removed the cliWidget (it was a remainder from the initial sample code, which used a vtkCommandLineModuleGUI)</li>
<li>I replaced the code for creating the output node</li>
<li>I moved the code to the logic object</li>
<li>The Grayscale Model Maker lists a parameter called Name, therefore I tried to use it:</li>
</ul>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/079457fcce6ee3263210059d2a9bff66981fde2b/Modules/CLI/GrayscaleModelMaker/GrayscaleModelMaker.xml#L40-L47" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/079457fcce6ee3263210059d2a9bff66981fde2b/Modules/CLI/GrayscaleModelMaker/GrayscaleModelMaker.xml#L40-L47" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/079457fcce6ee3263210059d2a9bff66981fde2b/Modules/CLI/GrayscaleModelMaker/GrayscaleModelMaker.xml#L40-L47</a></h4>
<pre class="onebox"><code class="lang-xml"><ol class="start lines" start="40" style="counter-reset: li-counter 39 ;">
<li>&lt;string&gt;</li>
<li>  &lt;name&gt;Name&lt;/name&gt;</li>
<li>  &lt;label&gt;Model Name&lt;/label&gt;</li>
<li>  &lt;flag&gt;-n&lt;/flag&gt;</li>
<li>  &lt;longflag&gt;--name&lt;/longflag&gt;</li>
<li>  &lt;description&gt;&lt;![CDATA[Name to use for this model.]]&gt;&lt;/description&gt;</li>
<li>  &lt;default&gt;Model&lt;/default&gt;</li>
<li>&lt;/string&gt;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>A minimalistic example could look like this:</p>
<pre><code class="lang-auto">vtkMRMLScene* scene = qSlicerCoreApplication::application()-&gt;mrmlScene();

// get module and its logic
qSlicerCLIModule* cliModule = static_cast&lt;qSlicerCLIModule*&gt;(qSlicerCoreApplication::application()-&gt;moduleManager()-&gt;module("GrayscaleModelMaker"));
vtkSlicerCLIModuleLogic* moduleLogic = vtkSlicerCLIModuleLogic::SafeDownCast(cliModule-&gt;logic());

// create CLI module node
vtkMRMLCommandLineModuleNode* cliNode = moduleLogic-&gt;CreateNodeInScene();

// get/create output node
vtkMRMLModelNode* outputNode = vtkMRMLModelNode::SafeDownCast(scene-&gt;AddNewNodeByClass("vtkMRMLModelNode", "modelName"));

// extract threshold from volume display node
vtkMRMLScalarVolumeDisplayNode* VolumeDisplayNode = vtkMRMLScalarVolumeDisplayNode::SafeDownCast(volumeNode-&gt;GetDisplayNode());
double threshold = VolumeDisplayNode-&gt;GetLowerThreshold();

// set parameters
cliNode-&gt;SetParameterAsNode("InputVolume", volumeNode);
cliNode-&gt;SetParameterAsNode("OutputGeometry", outputNode);
cliNode-&gt;SetParameterAsFloat("Threshold", threshold);

// start via logic
moduleLogic-&gt;Apply(cliNode);
</code></pre>

---

## Post #6 by @lassoan (2019-08-06 15:04 UTC)

<p>Thank you, I’ve updated example in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel/Programmatic_Invocation#C.2B.2B_example" rel="nofollow noopener">Slicer wiki</a> (with some changes that show how processing should be implemented in the module logic).</p>

---
