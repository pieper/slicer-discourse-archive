---
topic_id: 12351
title: "Access An Object Between Modules Extensions In Python"
date: 2020-07-03
url: https://discourse.slicer.org/t/12351
---

# Access an object between modules/extensions in python

**Topic ID**: 12351
**Date**: 2020-07-03
**URL**: https://discourse.slicer.org/t/access-an-object-between-modules-extensions-in-python/12351

---

## Post #1 by @talmazov (2020-07-03 04:54 UTC)

<p>Hey all,<br>
If I have module_A that I have previously used and have some generic object within it, how can I access that object in module_A from module_B?<br>
I know I can use another module/extension’s logic but I need to access the instance of the object to check its state between 2 extensions.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-07-03 05:05 UTC)

<p>Except very rare cases, modules should share data with each other via MRML nodes stored in the scene. MRML nodes often wrap various generic data objects.</p>

---

## Post #3 by @talmazov (2020-07-03 05:47 UTC)

<p>Any examples you can point me to that create custom MRML nodes in python?</p>

---

## Post #4 by @talmazov (2020-07-03 14:19 UTC)

<p>Or at least how to store an instance of an object so it can be shared between two modules.</p>

---

## Post #5 by @lassoan (2020-07-03 14:25 UTC)

<p>You can only create new node types in C++. In Python but you can customize any existing nodes (add custom attributes, parameters, node references). If there is no specific node that you want the associate these additional information with then you can use a <a href="http://apidocs.slicer.org/master/classvtkMRMLScriptedModuleNode.html">vtkMRMLScriptedModuleNode</a>.</p>
<p>What kind of object do you want to share between modules? Is it Python-wrapped C++ object or a pure Python object? What does it store?</p>

---

## Post #6 by @talmazov (2020-07-03 15:02 UTC)

<p>The extension i am working on creates a TCP/IP socket connection with a server. this sock variable stores the instance which I use throughout the extension to handle events of incoming data. I would like to be able to access that instance from another extension.<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/dentsoft-foundation/linkSlicerBlender/blob/32141199088743155233998dc8deea31d4667b5f/slicer_module/BlenderMonitor.py#L438" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/dentsoft-foundation/linkSlicerBlender/blob/32141199088743155233998dc8deea31d4667b5f/slicer_module/BlenderMonitor.py#L438" target="_blank" rel="nofollow noopener">dentsoft-foundation/linkSlicerBlender/blob/32141199088743155233998dc8deea31d4667b5f/slicer_module/BlenderMonitor.py#L438</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="428" style="counter-reset: li-counter 427 ;">
<li>    modelNode.GetDisplayNode().SetSliceIntersectionVisibility(True)</li>
<li>    modelNode.GetDisplayNode().SetSliceIntersectionThickness(2)</li>
<li>
</li><li>    #update object location in scene</li>
<li>    self.update_scene(xml)</li>
<li>
</li><li>    #self.SlicerSelectedModelsList.append([modelNodeSelector.currentNode().GetName(), modelNodeSelector, ""])</li>
<li>
</li><li>    #TODO: apply the incoming xml matrix data to the newly imported object right away, dont wait for the event from blender</li>
<li>
</li><li class="selected">def onPlayButtonToggled(self, checked):</li>
<li>    if checked:</li>
<li>        self.watching = True</li>
<li>        self.playButton.text = "Stop"</li>
<li>        if self.sock == None:</li>
<li>            self.sock = asyncsock.SlicerComm.EchoClient(str(self.host_address.text), int(self.host_port.text), [("XML", self.update_scene), ("OBJ", self.import_obj_from_blender), ("OBJ_MULTIPLE", self.import_multiple), ("CHECK", self.obj_check_handle), ("DEL", self.delete_model)])</li>
<li>            #self.sock.send_data("TEST", 'bogus data from slicer!')</li>
<li>    else:</li>
<li>        self.watching = False</li>
<li>        self.playButton.text = "Start"</li>
<li>        self.sock.handle_close()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2020-07-03 15:18 UTC)

<p>If there is only a single instance of this object, you don’t need to observe it, and you don’t need to serialize its state to the scene, you can simply make it a member of the module logic. You can access any a module’s logic class from any other module. From one Python scripted module you can access another Python scripted module’s logic like this:</p>
<pre><code>slicer.modules.someothermodule.widgetRepresentation().self().logic
</code></pre>
<p>Instead of exposing the socket object directly, you may consider exposing methods that operate on it.</p>
<p>This Blender integration could enable some interesting applications. What Blender features do you plan to use in Slicer (or Slicer features to use in Blender)?</p>
<p>Note that you can use Blender features in Slicer by importing Blender’s Python library into Slicer.</p>
<p>For robust Boolean operations on meshes, you can try <a href="https://github.com/zippy84/vtkbool">vtkbool library</a>.</p>

---

## Post #8 by @talmazov (2020-07-04 02:59 UTC)

<p>thanks!<br>
I was able to access the object instance<br>
I didn’t know slicer extension instances, once launched, are saved and can be accessed via slicer.modules… i thought i can only access logic and routines not instanced objects<br>
so<br>
slicer.modules.BlenderMonitorWidget.sock = instance pointed<br>
it worked!</p>

---
