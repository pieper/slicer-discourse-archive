# Slicer Based GUI development/implementation c++

**Topic ID**: 11687
**Date**: 2020-05-25
**URL**: https://discourse.slicer.org/t/slicer-based-gui-development-implementation-c/11687

---

## Post #1 by @Cesar_Puga (2020-05-25 01:44 UTC)

<p>Hello Everyone, i have been researching through this forums during the past few weeks as i am currently working on my master thesis, my goal is to implement a GUI that achieves the following:</p>
<p>-display a volume based on a set of dicom files (slices),<br>
-functionality of selecting a specific point in the volume,<br>
-recognition of a corregistration marker in the volume in order to get the transformation matrix of the CT volume,<br>
-planning of a needle trajectory (located at the end efector of a robot arm) to reach the selected point (w/ specific set of constraints as avoiding organs and such), then highlight specific trajectory in volume<br>
-furthermore communicate with a robot via a ROS node to inform about the computed trajectory (this step is at the moment confusing for me as i would have to find a way to link my application to a ROS node, but i think i could save the instructions in a file that is latter read by another program (this step is not that important at the moment)</p>
<p>this last week i tried a lot of different things such as QT/VTK, MITK, NIFTK but ive been getting lot of errors at configuring/building/implementing examples to get me started (im working on linux, in which im also relatively new), this made me realize how much of a begginer i am and how hard would be to implement this GUI from scratch using those toolkits, plus the more i research the more i get to the conclusion that using/creating specific modules extensions in Slicer is the way to go, ive gathered a bunch of links to get me started at implementing what i need by using Slicer as a “framework” but i would just like to kindly ask if you can see the above mentioned functionalities being implemented with Slicer, thanks for your kind support</p>

---

## Post #2 by @lassoan (2020-05-25 04:39 UTC)

<p>These features are have been largely already implemented in Slicer. You can find tutorials how to implement a robot-assisted intervention planning and guidance system from readily available components:</p>
<ul>
<li>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Data_Loading_and_3D_Visualization">Slicer basic tutorials</a> - DICOM import, general visualization</li>
<li>
<a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> - patient registration, trajectory planning and visualization</li>
<li>
<a href="https://github.com/rosmed/rosmed.github.io/wiki/ISMR2019">ROS-MED tutorial</a> - robotics integration</li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Slicer programming tutorials</a></li>
</ul>
<p>What you need to do is first calibrate your system, develop a good hardware&amp;software system and clinical workflow based on phantom experiments, once you know exactly what you want to do (hardware components, registration methods, visualization modes, etc. to use) then implement a simplified user interface in a custom module (so that you don’t need to switch between several modules to complete your workflow), then do several iterations of phantom/animal tissue/cadaver experiments to refine your system. Probably it would not be realistic to plan for more in master’s thesis timeline, but if based on these experiments your system proves to be safe and useful then you can go on and apply for IRB approval for patient or animal trials.</p>

---

## Post #3 by @Cesar_Puga (2020-05-29 20:29 UTC)

<p>Thanks for your insightful answer i have been going through the user/developer tutorials and ive convinced myself this is the optimal path to take to generate a robust solution for the given problem, developing that kind of system/gui from 0 using qt/vtk/itk would be to much for me in the given timeframe,</p>
<p>i am still unsure why my supervisor suggested to take the route of implementing this from scratch in a purely c++ based program, could it be that he was thinking about speed/efficiency of the system? would the slicer based application have any setbacks? something like noisy/slow communication with the robot or something similar? sorry if my question is too vague, i would just like to be able to justify to him in a technical way why would this be a much more robust solution (other than my programming skills not being good enough to develop a software of this magnitude on my own)</p>

---

## Post #4 by @lassoan (2020-05-29 23:33 UTC)

<p>If you implement something from scratch, specifically for a single purpose, without allowing any flexibility, then you may get better performance, and of course if you don’t build on any existing tools and libraries then you will not depend on anyone else but yourself. However, these small advantages are far outweighed by the many other advantages of building from existing open-source components.</p>
<p>First of all, these advantages are not always advantages. 1. The performance advantage is just theoretical. If you need to spend a lot of time developing everything yourself then you may have less time to work on performance optimization, so your system may end up being slower. 2. Not relying on others also means that you cannot use other people’s money to keep your system up-to-date: you still rely on development tools, operating system, GUI toolkit, graphics library, etc. and if those change, then you are completely on your own with the work of updating your software, testing it, and fixing whatever is broken. If you work with toolkits then platform updates are provided for free by the maintainers and if you encounter any problems then you just file a bug report and wait for the fix.</p>
<p>If you work from existing components then you can very easily add features and reconfigure your system to do things differently. This flexibility is very important because in most projects (and in all research&amp;development projects) you don’t know at the beginning what exactly you will need to do and how.</p>
<p>I could add a lot of more reasons, but everything comes down to that if you don’t need to spend time with reimplementing things then you have more time to work on new things: things that matter and add value.</p>
<p>It is hard to guess why your supervisor suggested to implement everything from scratch. Probably the best is to ask him.</p>

---

## Post #5 by @Cesar_Puga (2020-06-03 16:09 UTC)

<p>Thanks again for your convincing answer, i recently spoke to my supervisor and he agreed on using slicer as it sounds like the optimal solution for the given task, he just made a remark regarding my contribution to the topic, since i would be mostly integrating modules from an already existing product, my intellectual contribution to the project would be small, but overall he agreed. i successfully was able to interact with the Slicer custom app template to generate the simplified user interface that you mention</p>
<p>to which i would like to ask if there is the possibility of creating that “intellectual contribution” by creating some sort of module/python script to find an optimal trajectory for the needle to follow (with its corresponding robot poses for achieving this trajectory (if possible due to robot kinematics)) as i understand from the ROS-MED tutorial an entry and target point are defined from the user, similarly the user specifies a certain path according to possible obstacles close to the target, right? would it be possible to create a module/script to calculate an optimal path based on this information so that the user only defines a entry and target point, and a path to follow is created from this?</p>
<p>Thank you very much for your answers, im certain that they have steered this project into the direction of the best possible output</p>

---

## Post #6 by @lassoan (2020-06-03 16:20 UTC)

<p>I agree that “intellectual contribution” is very important. Before Slicer, “contribution” of many biomedical imaging researchers was a slightly different reimplementation of the same basic features. Now, building on Slicer, you don’t need to waste time with reimplementing basic things so you can focus on creating new solutions for open problems. It is up to you which open problem you choose to solve.</p>

---
