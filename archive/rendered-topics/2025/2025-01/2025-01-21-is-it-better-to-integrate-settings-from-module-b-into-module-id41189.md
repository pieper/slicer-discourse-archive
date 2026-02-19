---
topic_id: 41189
title: "Is It Better To Integrate Settings From Module B Into Module"
date: 2025-01-21
url: https://discourse.slicer.org/t/41189
---

# Is it better to integrate settings from Module B into Module A for improved user workflow (or user convenience)?

**Topic ID**: 41189
**Date**: 2025-01-21
**URL**: https://discourse.slicer.org/t/is-it-better-to-integrate-settings-from-module-b-into-module-a-for-improved-user-workflow-or-user-convenience/41189

---

## Post #1 by @shahrokh (2025-01-21 11:34 UTC)

<p>Hello Dear Developers and Users,</p>
<p>I wanted to get some advice on an issue.<br>
Suppose I am trying to develop a module named <strong>A</strong>, where one of the inputs of Module <strong>A</strong> is the output from another module, Module <strong>B</strong> which has already been developed. In this case, I could develop Module <strong>A</strong> completely independently. However, this would mean that the user would first need to go to Module <strong>B</strong> to generate its output, which is required as an input for Module <strong>A</strong>. Then, user would have to go to Module <strong>A</strong> and select the output from Module <strong>B</strong> as one of the inputs before running it.</p>
<p>My question is: for the sake of user convenience, would it be logical to integrate the settings/options of Module <strong>B</strong> directly into Module <strong>A</strong>, so that the user doesn’t need to first run Module <strong>B</strong> and then go to Module <strong>A</strong>?</p>
<p>Maybe it will be clearer if I explain with an example. In the implementation of Module <strong>A</strong>, I need the output from the <strong>Isodose</strong> module, specifically the <em><strong>Number of iso levels</strong></em> and <em><strong>Labels</strong></em> (which seem to be in terms of <strong>Dose (Gy)</strong> in <strong>Iso levels table</strong>) which need to be set or adjusted by the user. Can I add these two inputs from the <strong>Isodose</strong> panel (including <em><strong>number of iso levels</strong></em> and <em><strong>Label</strong></em> (in Gy)) as <em>Spin boxes</em> to the panel of Module <strong>A</strong> so that when Module <strong>A</strong> runs, the <strong>Isodose</strong> module will be executed in the background?</p>
<p>In this regard, I realized that it is possible to access the <strong>Isodose</strong> module in the <em>Python Interactor</em> using <code>slicer.util.getModule('Isodose')</code>. There is also a method called <code>setProperty</code>. Can I achieve my goal by specifying the arguments of this method?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29c3dabcf69a50491156e730d74110364ef754ac.png" data-download-href="/uploads/short-url/5XtbVYWSX4xCW488I86ZlcNE6TO.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c3dabcf69a50491156e730d74110364ef754ac_2_690x255.png" alt="1" data-base62-sha1="5XtbVYWSX4xCW488I86ZlcNE6TO" width="690" height="255" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c3dabcf69a50491156e730d74110364ef754ac_2_690x255.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c3dabcf69a50491156e730d74110364ef754ac_2_1035x382.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c3dabcf69a50491156e730d74110364ef754ac_2_1380x510.png 2x" data-dominant-color="AFAFA5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1854×686 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #2 by @shahrokh (2025-01-22 12:31 UTC)

<p>Regarding this issue, I came across a question titled <a href="https://discourse.slicer.org/t/call-slicerrt-isodose-or-create-isodoses-from-python/4506">Call SlicerRT Isodose (or create isodoses) from python</a> which was asked in the 3DSlicer Community.</p>
<p>I realized that in the Python Interactor, in addition to the <code>slicer.util.getModule</code> method which I mentioned in my previous message, there is another method called <code>slicer.util.getModuleLogic</code> that seems to provide access to the settings (logic) of modules, including <strong>Isodose</strong> module. In other words, it seems that the <code>getModuleLogic</code> method in <code>slicer.util</code> is used for setting the settings of modules.</p>
<p>According to the help provided for the <code>SetNumberOfIsodoseLevels</code> method, it seems that this method takes two input arguments: a <code>vtkMRMLIsodoseNode</code> type and an <code>integer</code>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23aa647d0bda0ffa37784c7e0c8f851a7aebc1a7.png" data-download-href="/uploads/short-url/55vM674WSGt4mZIC4ECd16UVfQr.png?dl=1" title="Screenshot from 2025-01-22 15-45-45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23aa647d0bda0ffa37784c7e0c8f851a7aebc1a7_2_690x162.png" alt="Screenshot from 2025-01-22 15-45-45" data-base62-sha1="55vM674WSGt4mZIC4ECd16UVfQr" width="690" height="162" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23aa647d0bda0ffa37784c7e0c8f851a7aebc1a7_2_690x162.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23aa647d0bda0ffa37784c7e0c8f851a7aebc1a7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23aa647d0bda0ffa37784c7e0c8f851a7aebc1a7.png 2x" data-dominant-color="F8F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-01-22 15-45-45</span><span class="informations">829×195 26.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The following commands were executed.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; object_vtkMRMLIsodoseNode = slicer.vtkMRMLIsodoseNode().CreateNodeInstance()
&gt;&gt;&gt; type(object_vtkMRMLIsodoseNode)
&lt;class 'vtkSlicerIsodoseModuleLogic.vtkMRMLIsodoseNode'&gt;
&gt;&gt;&gt; numberOfColors = 1
&gt;&gt;&gt; myIsodose = slicer.util.getModuleLogic('Isodose').SetNumberOfIsodoseLevels(object_vtkMRMLIsodoseNode, numberOfColors)
&gt;&gt;&gt; type(myIsodose)
&lt;class 'NoneType'&gt;
&gt;&gt;&gt; myIsodose.__dir__()
['__repr__', '__bool__', '__new__', '__doc__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
&gt;&gt;&gt; 
</code></pre>
<p>It seems that there was no syntax error when executing the above commands, but since the output type is<code> NoneType</code>, it seems that a logical error must have occurred.</p>
<p>Please guide me on how to implement the settings of the <strong>Isodose</strong> module in Python so that I can generate the output of this module by taking the RTDose input.</p>
<p>Best regards.<br>
Shahrokh.</p>

---

## Post #3 by @pieper (2025-01-22 18:55 UTC)

<p>Looks like you are on the right track.  <code>SetNumberOfIsodoseLevels</code> returns <code>None</code> because it just sets the value.  You should be able to call <code>SetNumberOfIsodoseLevels</code> or something similar to confirm that it was set.</p>
<p>On the more general topic, yes, reusing the Logic classes from other modules is definitely the right way of doing things.  Also, several modules expose widgets that can be reused in other modules although not all do.  You can also include buttons that take you directly to another module, perhaps with some parameters pre-selected, which is sometimes useful.</p>

---

## Post #4 by @shahrokh (2025-02-16 11:56 UTC)

<p>Thank you for your helpful response! I appreciate the guidance you’ve provided.</p>
<p>Regarding my progress, I believe I have successfully set up the Isodose module settings through the Python Interactor with the following commands:</p>
<pre><code class="lang-auto">object_vtkMRMLIsodoseNode = slicer.vtkMRMLIsodoseNode().CreateNodeInstance()
object_vtkMRMLIsodoseNode.SetReferenceDoseValue(47)
object_vtkMRMLIsodoseNode.GetReferenceDoseValue()
object_vtkMRMLIsodoseNode = slicer.vtkMRMLIsodoseNode().CreateNodeInstance()
object_vtkMRMLIsodoseNode.SetDoseUnits(slicer.vtkMRMLIsodoseNode.Gy)
object_vtkMRMLIsodoseNode.SetShowDoseVolumesOnly(1)
</code></pre>
<p>Now, I want to apply the <code>object_vtkMRMLIsodoseNode</code> settings to a node of type <code>RTDose</code>. I am using the following command to retrieve the node:</p>
<pre><code class="lang-auto">doseNode = slicer.util.getFirstNodeByClassByName('vtkMRMLScalarVolumeNode', '2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1')
</code></pre>
<p>However, I have not been able to find a method within <code>object_vtkMRMLIsodoseNode</code> that can perform the “Generate Isodose” operation. Could you please help me on the method to use for this?</p>
<p>Best regards.<br>
Shahrokh.</p>

---

## Post #5 by @shahrokh (2025-02-17 12:43 UTC)

<p>I used the following commands to solve this problem:</p>
<pre><code class="lang-auto"># Get the dose node
doseVolmeNode = slicer.util.getFirstNodeByClassByName('vtkMRMLScalarVolumeNode', '2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1')

# Create the isodose node
object_vtkMRMLIsodoseNode = slicer.vtkMRMLIsodoseNode().CreateNodeInstance()

# Initial isodose settings (Similar to the settings of the Isodose module)
object_vtkMRMLIsodoseNode.SetReferenceDoseValue(47)
object_vtkMRMLIsodoseNode.SetDoseUnits(slicer.vtkMRMLIsodoseNode.Gy)
object_vtkMRMLIsodoseNode.SetShowDoseVolumesOnly(1)
object_vtkMRMLIsodoseNode.SetAndObserveDoseVolumeNode(doseVolmeNode)

# Create isodose surface
isodose_logic = slicer.modules.isodose.logic()
modelDose47 = isodose_logic.CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
</code></pre>
<p>However, I still cannot get the two results below:</p>
<ol>
<li>
<p>The model that is seen in the 3D window with the <code>Isodose</code> module, as shown in the image below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f670348710c8fbece24635f67661ef88c62cd457.png" data-download-href="/uploads/short-url/za5R5md36v7U8GI8MZY3GkfLMrl.png?dl=1" title="11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f670348710c8fbece24635f67661ef88c62cd457_2_690x380.png" alt="11" data-base62-sha1="za5R5md36v7U8GI8MZY3GkfLMrl" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f670348710c8fbece24635f67661ef88c62cd457_2_690x380.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f670348710c8fbece24635f67661ef88c62cd457_2_1035x570.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f670348710c8fbece24635f67661ef88c62cd457_2_1380x760.png 2x" data-dominant-color="C6C8C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">11</span><span class="informations">1847×1019 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>In the Data module, a node named IsodoseLevel_47Gy has been created. The image below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33abc29209f41d3b0931d4be8c31517d0ba22818.png" data-download-href="/uploads/short-url/7n6loSQy2ePOsXQ1aHdzxumbxiM.png?dl=1" title="12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33abc29209f41d3b0931d4be8c31517d0ba22818_2_690x380.png" alt="12" data-base62-sha1="7n6loSQy2ePOsXQ1aHdzxumbxiM" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33abc29209f41d3b0931d4be8c31517d0ba22818_2_690x380.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33abc29209f41d3b0931d4be8c31517d0ba22818_2_1035x570.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33abc29209f41d3b0931d4be8c31517d0ba22818_2_1380x760.png 2x" data-dominant-color="C9CBCA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">12</span><span class="informations">1847×1019 313 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #6 by @shahrokh (2025-02-18 06:09 UTC)

<p>Sorry… As I mentioned in the previous message, I first set the parameters of the Isodose module in the object named object_vtkMRMLIsodoseNode from the vtkMRMLIsodoseNode class. Then, I applied it to a dose volume node named doseVolumeNode. Today, I realized (in the error log display) that the issue seems to be in this last step. The image below shows this error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82004207a99d014cb51f15914968613e49aa6564.png" data-download-href="/uploads/short-url/iy2CFLLomobI3z25spKmnANnJxq.png?dl=1" title="Screenshot from 2025-02-18 09-12-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82004207a99d014cb51f15914968613e49aa6564_2_690x393.png" alt="Screenshot from 2025-02-18 09-12-11" data-base62-sha1="iy2CFLLomobI3z25spKmnANnJxq" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82004207a99d014cb51f15914968613e49aa6564_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82004207a99d014cb51f15914968613e49aa6564_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82004207a99d014cb51f15914968613e49aa6564_2_1380x786.png 2x" data-dominant-color="D7E1EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-02-18 09-12-11</span><span class="informations">1846×1053 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As can be seen, after running this command:<br>
<code>object_vtkMRMLIsodoseNode.SetAndObserveDoseVolumeNode(doseVolumeNode)</code><br>
I get this error message:</p>
<pre><code class="lang-auto">Python console user input: object_vtkMRMLIsodoseNode.SetAndObserveDoseVolumeNode(doseVolumeNode)
Cannot set reference: the referenced and referencing node are not in the same scene
</code></pre>
<p>Sorry, I don’t understand the meaning of the phrase <strong>Cannot set reference: the referenced and referencing node are not in the same scene.</strong>.</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #7 by @shahrokh (2025-02-18 11:10 UTC)

<p>Excuse me…<br>
I was able to move one more step forward. Instead of using the command</p>
<pre><code class="lang-auto">myIsodoseSurface = slicer.vtkSlicerIsodoseModuleLogic().CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
</code></pre>
<p>I executed the following command (as mentioned in the guidance provided in question of <a href="https://discourse.slicer.org/t/call-slicerrt-isodose-or-create-isodoses-from-python/4506/7">Call SlicerRT Isodose (or create isodoses) from python</a>):</p>
<pre><code class="lang-auto">myIsodoseSurface = slicer.modules.isodose.logic().CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
</code></pre>
<p>Therefore, the full commands executed are as follows:</p>
<pre><code class="lang-auto">doseVolumeNode = slicer.util.getFirstNodeByClassByName('vtkMRMLScalarVolumeNode', '2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1')
object_vtkMRMLIsodoseNode = slicer.vtkMRMLIsodoseNode().CreateNodeInstance()
object_vtkMRMLIsodoseNode.SetScene(doseVolumeNode.GetScene())
object_vtkMRMLIsodoseNode.SetReferenceDoseValue(47)
object_vtkMRMLIsodoseNode.SetDoseUnits(slicer.vtkMRMLIsodoseNode.Gy)
object_vtkMRMLIsodoseNode.SetAndObserveDoseVolumeNode(doseVolumeNode)
#myIsodoseSurface = slicer.vtkSlicerIsodoseModuleLogic().CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
myIsodoseSurface = slicer.modules.isodose.logic().CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
</code></pre>
<p>As you can see in the image below,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/453addf9589426cf63cc73ecc726d138afd0bb3e.png" data-download-href="/uploads/short-url/9Sr4bTAT41UQjhGisF4Gouc0wbk.png?dl=1" title="Screenshot from 2025-02-18 14-27-29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453addf9589426cf63cc73ecc726d138afd0bb3e_2_690x393.png" alt="Screenshot from 2025-02-18 14-27-29" data-base62-sha1="9Sr4bTAT41UQjhGisF4Gouc0wbk" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453addf9589426cf63cc73ecc726d138afd0bb3e_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453addf9589426cf63cc73ecc726d138afd0bb3e_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453addf9589426cf63cc73ecc726d138afd0bb3e_2_1380x786.png 2x" data-dominant-color="EFF0F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-02-18 14-27-29</span><span class="informations">1846×1053 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>similar to the <code>Isodose</code> module execution, which produces a model output placed in a folder, when running the command of:</p>
<pre><code class="lang-auto">myIsodoseSurface = slicer.modules.isodose.logic().CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
</code></pre>
<p>this folder is also created, but it is empty, and the 3DSlicer environment completely freezes, to the point where none of the icons in the red, yellow, or green windows are selectable. In the end, I have to close 3DSlicer.</p>
<p>I think I am getting closer to my answer.<br>
Please guide me.<br>
Best regards.<br>
Shahrokh.</p>

---

## Post #8 by @shahrokh (2025-02-19 12:06 UTC)

<p>I think I was mostly successful. The problem I mentioned in my previous message (the freezing of the 3DSlicer display environment, such as 3D view) was because I hadn’t set up its color table. Based on this, the commands became as follows.</p>
<pre><code class="lang-auto"># Get the dose volume node by class and name
doseVolumeNode = slicer.util.getFirstNodeByClassByName('vtkMRMLScalarVolumeNode', '2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1')

# Create a new Isodose node instance for displaying isodose surfaces
object_vtkMRMLIsodoseNode = slicer.vtkMRMLIsodoseNode().CreateNodeInstance()

# Set the scene for the isodose node to match the dose volume node's scene
object_vtkMRMLIsodoseNode.SetScene(doseVolumeNode.GetScene())

# Set the dose units to Gray (Gy)
object_vtkMRMLIsodoseNode.SetDoseUnits(slicer.vtkMRMLIsodoseNode.Gy)

# Set the reference dose value (in Gy) for isodose levels
object_vtkMRMLIsodoseNode.SetReferenceDoseValue(47.00)

# Observe the dose volume node to track its changes
object_vtkMRMLIsodoseNode.SetAndObserveDoseVolumeNode(doseVolumeNode)

# Setup the color table for the isodose node based on the dose volume
slicer.modules.isodose.logic().SetupColorTableNodeForDoseVolumeNode(doseVolumeNode)

# Create isodose surfaces based on the configured isodose node
slicer.modules.isodose.logic().CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
</code></pre>
<p>As can be seen in the commands above, I want the number of iso levels to be <strong>one</strong>, and the isodose surface to be generated for a dose of <strong>47.00 Gy</strong>. When I run these commands, the following result occurs.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaa61b2cafb975aa0b6d85ba8355f194e50043cb.png" data-download-href="/uploads/short-url/olD398aYtAJ3PPvwWHlJEzTUcMH.png?dl=1" title="Screenshot from 2025-02-19 15-29-40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaa61b2cafb975aa0b6d85ba8355f194e50043cb_2_690x391.png" alt="Screenshot from 2025-02-19 15-29-40" data-base62-sha1="olD398aYtAJ3PPvwWHlJEzTUcMH" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaa61b2cafb975aa0b6d85ba8355f194e50043cb_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaa61b2cafb975aa0b6d85ba8355f194e50043cb_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaa61b2cafb975aa0b6d85ba8355f194e50043cb_2_1380x782.png 2x" data-dominant-color="E8E8ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-02-19 15-29-40</span><span class="informations">1848×1049 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>as shown above, This result is exactly the same as the default settings of the Isodoses module, meaning the number of iso levels is 6, and the dose values are 5, 10, 15, 20, 25, and 30 Gy. In other words, the value I set with the above commands (47.00 Gy) has essentially had no effect here.</p>
<p>I don’t know where the problem is from. I hope you can guide me, and until then, I will continue with my efforts.<br>
Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---
