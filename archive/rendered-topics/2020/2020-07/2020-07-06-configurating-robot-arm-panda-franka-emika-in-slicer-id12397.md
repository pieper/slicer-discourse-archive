# Configurating Robot arm (Panda - Franka Emika) In slicer

**Topic ID**: 12397
**Date**: 2020-07-06
**URL**: https://discourse.slicer.org/t/configurating-robot-arm-panda-franka-emika-in-slicer/12397

---

## Post #1 by @Cesar_Puga (2020-07-06 14:58 UTC)

<p>I went through the ROSMED tutorials where a robot arm is loaded to perform a needle insertion, my goal is to recreate this action but with another robot arm model, from what i can see in the tutorial, i would need to get the specific stl files from all the robot links AND the transformation matrices (h5 files in the tutorial) and integrate them into a .mrm scene lto be able to visualize and move the robot around in 3D slicer, i have mainly two questions:</p>
<ol>
<li>if i just load the stl files and issue commands via IGTLink for an arbitrarily planned path in rviz, then i would be able to visualize the correct movement in 3D slicer even if i did not construct the robot using a hierarchy of transforms in slicer, right? i would think that would be the case since rviz already has this information and 3D slicer would just work to visualize the movements that arise no issues in rviz-move it motion plannin</li>
</ol>
<p>in case thats not the case, is there any information on how to proceed in “assembling” the robot arm in 3D slicer? from the ROSMED tutorial a .mrlm scene is loaded so im wondering whats the required process for creating that scene with the mentioned robot arm, at the moment i just have the 3D model of the robot arm so maybe i would need to calculate the transformation matricesof the links but im unsure how</p>
<p>thanks for your support, i really appreciate it</p>

---

## Post #2 by @lassoan (2020-07-06 18:08 UTC)

<p>All of what you mentioned is possible and it is your decision how you want things to work. What would you send to Slicer from ROS?</p>
<ul>
<li>OpenIGTLink transform containing absolute position+orientation of each part of the robot arm (in Slicer there is no need for creating any transform tree, just apply the transform directly to the model nodes)</li>
<li>OpenIGTLink transform containing relative translation+rotation between joints (in Slicer you need to arrange the received transforms in a tree by drag-and-drop in the transform hierarchy)</li>
<li>OpenIGTLink transform containing relative rotation between joints (in Slicer you need to arrange the received transforms in a tree and add relative translations between them)</li>
<li>OpenIGTLink ndarray containing joint angles (in Slicer you need to add a small python script that computes relative transforms from the joint angles)</li>
</ul>

---

## Post #3 by @Cesar_Puga (2020-07-10 12:11 UTC)

<p>Hello Mr Laso, Thanks for your kind reply, in my case i would be sending information about the robot initial -&gt; target pose via MoveIt! (same as described in the RosMed tutorial) therefore i think the information sent would be the 1) absolute position+orientation of each joint (although i might be wrong, but based on MoveIt! RobotState Class i would assume this would be the case)</p>
<p>my current goal is to be able to visualize the same needle insertion technique from the RosMed tutorial but using a different robot arm, that is to be able to visualize robot arm movements/needle paths  in slicer, for this i have to assemble my own scene (with a patient model and the mentioned robot arm) but im unsure about how to load the robot parts in slicer as .stl files in slicer, i will try to assemble the robot arm in slicer as recommended in other posts, that is creating a transform hierarchy, to then create my own robot arm + patient scene and try to recreate the tutorial steps,</p>
<p>i apologize if my question is to naive or vague, im fairly new to this incredible tool, and doing my best to understand it properly</p>

---

## Post #4 by @lassoan (2020-07-10 17:39 UTC)

<p>To visualize the robot in Slicer, you need to have information about position+orientation of each robot part. You send this information from ROS to Slicer. What parameters do you send? Absolute position+orientation, relative transforms, … (see the list <a href="https://discourse.slicer.org/t/configurating-robot-arm-panda-franka-emika-in-slicer/12397/2">above</a>)?</p>

---

## Post #5 by @Cesar_Puga (2020-07-10 23:17 UTC)

<p>I think i understand it now, after analyzing the robot in the ROSMED slicer scene and the structure of the project in general, The Position+Orientation of the robot (Homogeneous matrix containing rotational+translational part of each link) is sent with the igtl_exporter.py via the IGTL_Bridge, therefore i would need to modify this script (igtl_exporter.py) according to my robot characteristics (links). That means i can “assemble” the robot in slicer applying a trasform directly in the model nodes as you suggest in your first option of your main reply, and send the position+orientation of each link via ROS whenever i want to achieve a new robot pose</p>
<p>Thank you very much for pointing me in the right direction</p>

---

## Post #6 by @CHRIS_HUYNH (2020-09-09 09:36 UTC)

<p>Hi Cesar,</p>
<p>Did you manage to get the integration of your own robot with the ROSMED tutorials working? If so, could you provide me with some guidance on the steps you took to get it working.</p>

---

## Post #7 by @Cesar_Puga (2020-09-09 10:54 UTC)

<p>Hi Chris,</p>
<p>I was able to replace the UR5 robot in the ROSMED tutorials for the Franka-Emika Panda robot,</p>
<p>what you need to do first is to setup your robot in moveit, many robots models are available for motion planning in move it, the one i used was luckily one of them, but if you are using one not available, they provide guidance on how to configure it,</p>
<p>then you need to copy the igtl exporter py file from the ROSMED tutorial package, to your robot catkin_ws package (you can also create your own script), you need to modify this file according to your specific robot link names, if you want to visualize your robot in slicer you can import the robot stl model and assign the transforms that are communicated to slicer via this igtl_exporter python script, you apply this transforms directly to the individual robot links accordingly, if you dont have the stl model you can also visualize the transforms in slicer wich provide insight of the robot links positon+orientation</p>
<p>once this is covered you can visualize in slicer, robot trajectories planed with moveit, this is the stage of where im currently at in my project, still need to work on the segmentation, needle path planning, dont hesitate to ask if you have further questions</p>

---

## Post #8 by @CHRIS_HUYNH (2020-09-09 18:44 UTC)

<p>Hi Cesar,</p>
<p>I’ve follow your steps but still have not managed to get it working, but I do think I’m on the right track. I’m just going to list the steps that I took on my behalf to give you a better understanding of the situation. This has all been done in my own workspace.</p>
<ol>
<li>
<p>I obtained my robot package from <a href="https://github.com/ros-industrial/abb_experimental" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ros-industrial/abb_experimental: Experimental packages for ABB manipulators within ROS-Industrial (http://wiki.ros.org/abb_experimental)</a> for the ABB IRB 120 robot. This package contains the support (contains the robot link urdf setup) and moveit packages (the moveit package was created already, but I made sure to edit the package to include ROS Controllers).</p>
</li>
<li>
<p>I have copied over the ros_igtl_bridge package from <a href="https://rosmed.github.io/ismr2019/ros_environment" class="inline-onebox" rel="noopener nofollow ugc">ISMR19 Workshop | ROS for Medical Robotics</a> and running the following command<br>
“catkin_make --cmake-args -DOpenIGTLink_DIR:PATH=~/igtl/OpenIGTLink-build” to build the packages for ros_igtl_bridge</p>
</li>
<li>
<p>I created a package transform_exporter in my workspace (following the same build dependencies as that of the ismr19_control package from the ROSMED tutorial) and created a ‘scripts’ folder in which i copied over the igtl_exporter.py script into.</p>
</li>
<li>
<p>In 3D slicer, I have obtained my robot link stl’s (converting them from units metres to mm for 3D slicer) and have applied <strong>LinearTransformations</strong> to each individual link (translating them using the translation sliders to set it up) image seen below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c765bf77586a1e2a4a6ccefb998e3110e6b01300.png" data-download-href="/uploads/short-url/srX0ErySOblxGlkxZYuPAEbhUac.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c765bf77586a1e2a4a6ccefb998e3110e6b01300_2_690x455.png" alt="image" data-base62-sha1="srX0ErySOblxGlkxZYuPAEbhUac" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c765bf77586a1e2a4a6ccefb998e3110e6b01300_2_690x455.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c765bf77586a1e2a4a6ccefb998e3110e6b01300_2_1035x682.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c765bf77586a1e2a4a6ccefb998e3110e6b01300_2_1380x910.png 2x" data-dominant-color="B0AECD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2407×1589 415 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>I have modified the igtl_exporter.py script to suit the links of my robot. The ABB IRB 120 robot has link_1, link_2, link_3, link_4, link_5, link_6 and tool0/flange. see image below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/117c59eda40ac8fe1d94f10f90f50214184a1c59.png" data-download-href="/uploads/short-url/2uGxnzJLWUKWW5rxMfB0X9hhqEp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/117c59eda40ac8fe1d94f10f90f50214184a1c59_2_368x500.png" alt="image" data-base62-sha1="2uGxnzJLWUKWW5rxMfB0X9hhqEp" width="368" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/117c59eda40ac8fe1d94f10f90f50214184a1c59_2_368x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/117c59eda40ac8fe1d94f10f90f50214184a1c59_2_552x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/117c59eda40ac8fe1d94f10f90f50214184a1c59_2_736x1000.png 2x" data-dominant-color="FAF9FA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1352×1835 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>To test my progress I ran the ros_igtl_bridge node (bridge.launch) and the igtl_exporter node. I then opened up 3D slicer and made sure that the connection status is ON for the OpenIGTLinkIF (port 18944) and then I proceeded to load up my ABB IRB 120 robot in Moveit and perform a plan and execute it.(see image below).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3346c22841b4807795716d65d92f756f6ccbdd4.png" data-download-href="/uploads/short-url/rQRq79mKdKPUZOzIUgru8aMzwUs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3346c22841b4807795716d65d92f756f6ccbdd4_2_667x500.png" alt="image" data-base62-sha1="rQRq79mKdKPUZOzIUgru8aMzwUs" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3346c22841b4807795716d65d92f756f6ccbdd4_2_667x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3346c22841b4807795716d65d92f756f6ccbdd4_2_1000x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3346c22841b4807795716d65d92f756f6ccbdd4_2_1334x1000.png 2x" data-dominant-color="969492"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1827×1368 364 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ol>
<p>I believe I’ve followed your steps, but maybe not to the exact detail (possibly elaborate on the exact steps you took) which is probably why my robot doesn’t work as intended.</p>
<p>Could it possibly be how I set up my linear transformations nodes in 3D slicer (I set mine up using the transformations module and manually translated each link into position to set up the robot)? or how I’ve copied over the ros_igtl_bridge package or igtl_exporter.py script (maybe I didn’t set up my transform_exporter package correctly) or is there something else on the ROS side of things that I need to edit/modify? Even though I got the moveit! packages from the github depository, maybe the planning group or ros controller isn’t set up properly?</p>
<p>I’m greatly appreciative for the guidance you have provided me thus far, and will be happy to hear from your response. I’d love to hear in detail how you set your own robot up to get it working with the ROSMED project, maybe I can mimic the exact steps you took to get mine up and running.</p>
<p>Thank you !!</p>

---

## Post #9 by @CHRIS_HUYNH (2020-09-10 07:37 UTC)

<p>Hi Cesar,</p>
<p>After a bit of tinkering I got it working !!! I’d like to thank you so much for your help. The next step for me is the same for you, getting the needle pathing and planning set up. I think that would just be adding an extra link to the end of the robot (end-effector) and setting it up the transformation for the link on 3D slicer, and adding the end-effector link to the existing moveit! package.</p>

---

## Post #10 by @lassoan (2020-09-10 13:39 UTC)

<aside class="quote no-group" data-username="CHRIS_HUYNH" data-post="9" data-topic="12397">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_huynh/48/6392_2.png" class="avatar"> CHRIS_HUYNH:</div>
<blockquote>
<p>After a bit of tinkering I got it working !!!</p>
</blockquote>
</aside>
<p>Awesome!</p>
<p><a class="mention" href="/u/cesar_puga">@Cesar_Puga</a> <a class="mention" href="/u/chris_huynh">@CHRIS_HUYNH</a> Could you post a nice screenshot (and acknowledgment text) of what you achieved that we could showcase it the image carousel in Slicer’s upcoming redesigned website? Thank you!</p>

---

## Post #11 by @CHRIS_HUYNH (2020-09-10 14:56 UTC)

<p>Hi Andras,</p>
<p>I’d be happy to provide anything you need <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Were there any specific screenshots you would like to have? A screenshot of both ROS Moveit! and 3D slicer on one window? maybe a video?</p>
<p>I’ll be working on my project again tomorrow at university so I can send them to you tomorrow if needed.</p>
<p>Regards,</p>
<p>Chris</p>

---

## Post #12 by @lassoan (2020-09-10 15:46 UTC)

<p>Thank you, all these sound good. Maybe you could upload all to a shared folder somewhere and post the link here.</p>

---

## Post #13 by @CHRIS_HUYNH (2020-09-14 08:51 UTC)

<p><a href="https://1drv.ms/u/s!AsyU2pv-0QIdjgmu64akSUQWlxlG?e=my780B" class="onebox" target="_blank" rel="noopener nofollow ugc">https://1drv.ms/u/s!AsyU2pv-0QIdjgmu64akSUQWlxlG?e=my780B</a></p>
<p>Hi Andras,</p>
<p>The shared document for the integration is in the above link. The mp4 file may be a bit laggy because having multiple programs open and nodes running in the background uses a lot of my laptop power.</p>
<p>I would like to acknowledge Junichi Tokuda for providing the project of the ROS and 3D Slicer Integration, along with all the associated files and scripts, Andras Lasso for being there to provide support for setting up my ABB IRB 120 robot in 3D slicer and applying transformations to each link of my robot in the 3d slicer software, and Cesar Puga for providing the guidance on how to set up my own ABB IRB 120 robot to replace the UR5 robot in the ROSMED ros-slicer-integration project.</p>

---

## Post #14 by @lassoan (2020-09-14 12:47 UTC)

<p>Perfect, thank you, very nice images.</p>

---
