---
topic_id: 6962
title: "Using The Plus Remote Module From The Python Interactor"
date: 2019-05-29
url: https://discourse.slicer.org/t/6962
---

# Using the Plus Remote Module from the Python Interactor

**Topic ID**: 6962
**Date**: 2019-05-29
**URL**: https://discourse.slicer.org/t/using-the-plus-remote-module-from-the-python-interactor/6962

---

## Post #1 by @fergujm2 (2019-05-29 22:27 UTC)

<p>Hi,</p>
<p>I am trying to launch a PlusServer instance from the python interactor.  Specifically, I need to be able to start/stop the server, and each time I start, I would like to specify the config file.  The reason for this is because we will be updating parameters in the config file and then restarting PlusServer with new, calibrated parameters, and this will eventually need to be done in a scripted module.</p>
<p>I have had success interacting with the PlusServerLauncher from the Plus Remote GUI in slicer, but it would be great if I could do something like:</p>
<p>remote = slicer.modules.plusremote</p>
<p>remote.connect(‘localhost’, 18904)<br>
remote.SetConfigFile(‘SomeDefaultConfigFile’)<br>
remote.StartServer()</p>
<p>Then start an OpenIGTLinkConnector to stream data into slicer. When I want to change the config file, I would do something like:</p>
<p>remote.StopServer() # When I want to stop streaming data<br>
remote.SetConfigFile(‘SomeUpdatedConfigFile’)<br>
remote.StartServer()</p>
<p>I have tried to search for a good way to do the above from the python interactor, but I have had no luck.  Let me know if you have any insights on this.</p>
<p>Thanks,</p>
<p>James</p>

---

## Post #2 by @Sunderlandkyl (2019-05-30 03:24 UTC)

<p>What version of Slicer are you using?<br>
If you are using Slicer &gt;= 4.10.1 with an updated version of SlicerOpenIGTLink, then there are a couple of ways to do it:</p>
<pre><code class="lang-auto">launcherNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlusServerLauncherNode")
serverNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlusServerNode")

launcherNode.AddAndObserveServerNode(serverNode)
serverNode.SetAndObserveConfigNode(configFileNode)
serverNode.StartServer()
</code></pre>
<p>or</p>
<pre><code class="lang-auto">launcherNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlusServerLauncherNode")
serverNode = launcher.StartServer(configFileNode)
</code></pre>
<p>Note that the configFileNode is a vtkMRMLTextNode.</p>
<p>Relevant MRML nodes are here: <a href="https://github.com/openigtlink/SlicerOpenIGTLink/tree/master/PlusRemote/MRML" rel="nofollow noopener">https://github.com/openigtlink/SlicerOpenIGTLink/tree/master/PlusRemote/MRML</a></p>
<p>The vtkMRMLPlusServerNode controls the state of the server and can be changed using the StartServer() and StopServer() or SetState() methods.</p>

---

## Post #3 by @fergujm2 (2019-05-30 17:46 UTC)

<p>Thanks, Kyle.  This worked flawlessly.</p>
<p>For anyone else who needs the info, after starting PlusServerLauncher, the full way I got this working was by:</p>
<pre><code class="lang-python">fn = "C:/Full/Path/To/ConfigFile.xml"
with open(fn, 'r') as file:
  configText = file.read()

configNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTextNode')
configNode.SetText(configText) # Sets the text to the XML file contents

launcherNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlusServerLauncherNode")
serverNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlusServerNode")

launcherNode.AddAndObserveServerNode(serverNode)
serverNode.SetAndObserveConfigNode(configNode)

serverNode.StartServer()

# Do whatever with data streamed into Slicer... 
pass

# Also, you can change the configFile if/when desired
serverNode.StopServer()
configNode.SetText(SomeNewXmlText)
serverNode.StartServer()
</code></pre>

---
