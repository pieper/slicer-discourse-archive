---
topic_id: 36798
title: "Loading Robot Into Slicer"
date: 2024-06-15
url: https://discourse.slicer.org/t/36798
---

# Loading Robot into Slicer

**Topic ID**: 36798
**Date**: 2024-06-15
**URL**: https://discourse.slicer.org/t/loading-robot-into-slicer/36798

---

## Post #1 by @Jeff_Boker (2024-06-15 03:37 UTC)

<p>I am trying to figure out how I load the Franka Robot into Slicer because I want to be able to send joint commands to it via OpenIGTLink and see it move in Slicer. It seems like I need to use Slicer_ROS2, but I was wondering if there is any easier way to just upload the URDF files of the robot because I do not need ROS and it seems like I need to use a specific version of ubuntu for Slicer_ROS2.</p>

---

## Post #2 by @lassoan (2024-06-15 03:55 UTC)

<p>Slicer_ROS2</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/rosmed/slicer_ros2_module">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/rosmed/slicer_ros2_module" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/c33af25eccdfb4e9eccb3224d43e1b8af5cecbf0c600e4273da9c2a23bc0525b/rosmed/slicer_ros2_module" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/rosmed/slicer_ros2_module" target="_blank" rel="noopener">GitHub - rosmed/slicer_ros2_module: Slicer module that can interface directly...</a></h3>

  <p>Slicer module that can interface directly with ROS 2 using ROS parameters, topics, tf... - rosmed/slicer_ros2_module</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If all you need is to visualize a robot and send joint commands then you can use the ROS OpenIGTLink bridge. You can extract surface meshes needed for rendering the robot from the urdf file and recreate them in Slicer - see an example here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yS3SKqNztJU" data-video-title="Medical robot visualization in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yS3SKqNztJU" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yS3SKqNztJU/maxresdefault.jpg" title="Medical robot visualization in 3D Slicer" width="690" height="388">
  </a>
</div>

<p>However, roboticists generally prefer to have full access to ROS from the Slicer module, and that is where the second option is useful: having a ROS node running in Slicer. This allows you to do a lot more, but it is harder to set up the build.</p>

---

## Post #3 by @Jeff_Boker (2024-06-21 00:11 UTC)

<p>Wow, thanks! That is what I am looking for as you show in the youtube video. Basically I want to just drag and drop a file and instead of using the mouse and sliders to adjust the joint values, I want to do this automatically using OpenIGTLink.</p>
<p>But I am a little confused about converting my urdf file into the mrb file where the joint values can be controlled with the sliders as you do in the video. So I can convert the urdf into surface meshes, but how will slicer know all the joints and how to set the sliders to actuate the joints?</p>

---

## Post #4 by @lassoan (2024-06-21 18:34 UTC)

<aside class="quote no-group" data-username="Jeff_Boker" data-post="3" data-topic="36798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_boker/48/67074_2.png" class="avatar"> Jeff_Boker:</div>
<blockquote>
<p>Basically I want to just drag and drop a file and instead of using the mouse and sliders to adjust the joint values, I want to do this automatically using OpenIGTLink.</p>
</blockquote>
</aside>
<p>Slicer can do exactly this. The file that you drag-and-drop is a Slicer scene file that contains models, transforms, and OpenIGTLink configuration.</p>
<aside class="quote no-group" data-username="Jeff_Boker" data-post="3" data-topic="36798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_boker/48/67074_2.png" class="avatar"> Jeff_Boker:</div>
<blockquote>
<p>I am a little confused about converting my urdf file into the mrb file where the joint values can be controlled with the sliders as you do in the video. So I can convert the urdf into surface meshes, but how will slicer know all the joints and how to set the sliders to actuate the joints?</p>
</blockquote>
</aside>
<p>You can build the transform tree from information in the urdf file. To make this very easy, I’ve implemented an automatic importer script. You can download it from here:</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/e174e853cd78ad93a1cd54b32debdac8">
  <header class="source">

      <a href="https://gist.github.com/lassoan/e174e853cd78ad93a1cd54b32debdac8" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/e174e853cd78ad93a1cd54b32debdac8" target="_blank" rel="noopener">https://gist.github.com/lassoan/e174e853cd78ad93a1cd54b32debdac8</a></h4>

  <h5>SlicerImportURDF.py</h5>
  <pre><code class="Python"># URDF importer for Slicer
#
# This script imports a universal robot description file (URDF) into 3D Slicer scene.
# This model can then be animated by updating the joint transforms by interactively modifying the transforms in 3D views
# or remotely via OpenIGTLink.
#
# Usage: Copy-paste this script into the Python console in 3D Slicer. The script automatically downloads an example URDF from github.
# You can use your own URDF file by setting `rootPath` and `urdfFilePath` to the path of your URDF file.

# Get URDF file.</code></pre>
   This file has been truncated. <a href="https://gist.github.com/lassoan/e174e853cd78ad93a1cd54b32debdac8" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The script does not support all possible features (e.g., I’ve only added “revolute” joint types), but can be easily extended as needed.</p>
<p>All you need is to copy-paste the script into Slicer’s Python console in a recent Slicer Preview Release (Slicer-5.7.x; Slicer Stable Release is not compatible, as it does not support selective display of transform rotation handles):</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb8a4c24db201bc3b989359123cc6f3d09b2caf3.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cce36310c40b5161715cbc92cb2a8ab536f27635.jpeg">
  </div><p></p>

---

## Post #5 by @Kyle_Hata25 (2024-08-04 21:46 UTC)

<p>Hi,</p>
<p>Thank you so much for making this converter available for us. I had some trouble with loading my own URDF into the python console of Slicer. The module and Slicer would crash when this portion of the code was pasted into the console:</p>
<pre><code class="lang-auto"># Add all links and joints to the scene
nodes = {}
for link in robot:
    name = link.get("name")
    if link.tag == "link":
        try:
            stlFilePath = rootPath + "/" + link.find('collision').find('geometry').find('mesh').attrib["filename"]
            # Use RAS coordinate system to avoid model conversion from LPS to RAS (we can transform the entire robot as a whole later if needed)
            modelNode = slicer.modules.models.logic().AddModel(stlFilePath, slicer.vtkMRMLStorageNode.CoordinateSystemRAS)
        except:
            # No mesh found, add a sphere
            sphere = vtk.vtkSphereSource()
            sphere.SetRadius(0.01)
            modelNode = slicer.modules.models.logic().AddModel(sphere.GetOutputPort())
        modelNode.SetName(name)
        nodes[name] = { "type": "link", "model": modelNode}
    
    elif link.tag == "joint":
        jointTransformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode", name)
        nodes[name] = { "type": "joint", "transform": jointTransformNode}
        if link.get("type") == "fixed":
            # do not create a display node, the transform does not have to be editable
            pass
        else:
            # make the transform interactively editable in 3D views
            jointTransformNode.CreateDefaultDisplayNodes()
            displayNode = jointTransformNode.GetDisplayNode()
            displayNode.SetEditorVisibility(True)
            displayNode.SetEditorSliceIntersectionVisibility(False)
            displayNode.SetEditorTranslationEnabled(False)
            if link.get("type") == "revolute":
                # &lt;axis xyz="0 0 1"/&gt;
                rotationAxis = [float(x) for x in link.find("axis").get("xyz").split()]
                if rotationAxis == [1, 0, 0]:
                    displayNode.SetRotationHandleComponentVisibility3D(True, False, False, False)
                elif rotationAxis == [0, 1, 0]:
                    displayNode.SetRotationHandleComponentVisibility3D(False, True, False, False)
                elif rotationAxis == [0, 0, 1]:
                    displayNode.SetRotationHandleComponentVisibility3D(False, False, True, False)
                else:
                    raise ValueError(f"Unsupported rotation axis {rotationAxis}")
            else:
                # TODO: implement translation and other joint types
                raise ValueError(f"Unsupported joint type {link.get('type')}")
</code></pre>
<p>I was wondering if I could get some help on this. Thank you</p>

---

## Post #6 by @pieper (2024-08-05 18:11 UTC)

<p><a class="mention" href="/u/kyle_hata25">@Kyle_Hata25</a> - It would be great if you could post an example robot file that isn’t working, along with a report of which specific error you are seeing.</p>

---

## Post #8 by @Kyle_Hata25 (2024-08-05 19:08 UTC)

<p>Hi! So I am not receiving an error message on the Slicer python console but rather Slicer is crashing and would shut down when pasting the code into the console.</p>

---

## Post #9 by @pieper (2024-08-05 19:55 UTC)

<p>To get help, be sure to post the data and the exact replication steps.  Maybe you need to put the robot file in google drive or similar and paste the link here.</p>

---

## Post #10 by @Kyle_Hata25 (2024-08-05 20:26 UTC)

<p>Hi,<br>
Thank you so much for the help. Here is the link to the drive with the information of the problem.<br>
<a href="https://drive.google.com/drive/folders/1mAaVVec7Cqw23gQi8qTbaYCFAJDbgrw6?usp=drive_link" rel="noopener nofollow ugc">Link</a></p>
<p>Once again, thank you so much!</p>

---

## Post #11 by @pieper (2024-08-05 22:56 UTC)

<p>Great, thanks for sharing the udf file - I can see now why it crashes.</p>
<p>If you look in your .urdf file you can see that the mesh lines are formatted like this:</p>
<pre><code class="lang-auto">&lt;mesh filename="package://quadruped_description/quadruped/body1.stl"/&gt;
</code></pre>
<p>Whereas in the <a href="https://github.com/justagist/franka_panda_description/tree/master">example that Andras used</a> this look like this:</p>
<pre><code class="lang-auto">        &lt;mesh filename="meshes/collision/link1.stl"/&gt;
</code></pre>
<p>That is, in the code that working the mesh files are in a location relative to the location of the .urdf file, while yours use a special syntax <code>package://</code></p>
<p>So you’ll need to investigate where to get those stl files and construct a layout like the one the code expects.  From a quick search I think this should help:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://answers.ros.org/question/370075/using-package-in-urdf-with-ros2/">
  <header class="source">
      <img src="https://answers.ros.org/m/ros/media/images/ros_favicon.gif?v=28" class="site-icon" width="32" height="32">

      <a href="https://answers.ros.org/question/370075/using-package-in-urdf-with-ros2/" target="_blank" rel="noopener">answers.ros.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://answers.ros.org/question/370075/using-package-in-urdf-with-ros2/" target="_blank" rel="noopener">Using `package://` in URDF with ROS2 - ROS Answers: Open Source Q&amp;A Forum</a></h3>

  <p>How is package:// in an URDF file resolved in ROS 2, i.e. what do I need to put there so that the files are found? Some context: With ROS 1 I was using package://package_name/meshes/file.stl in the URDF file with a directory "meshes" at the root of...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #12 by @lassoan (2024-08-15 16:32 UTC)

<p>It may be easier to update the code to strip <code>package://</code> and search for the STL files in the current folder and make sure that the STL files are in the correct subfolder relative to the .urdf file.</p>

---
