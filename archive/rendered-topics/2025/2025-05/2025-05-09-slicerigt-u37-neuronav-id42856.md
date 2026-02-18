# SlicerIGT-U37_NeuroNav

**Topic ID**: 42856
**Date**: 2025-05-09
**URL**: https://discourse.slicer.org/t/slicerigt-u37-neuronav/42856

---

## Post #1 by @Ruida_Cheng (2025-05-09 20:12 UTC)

<p>I’m following the NeuroNav.ppt tutorial to try out an optical tracking probe setup, but I’m missing some critical configuration details. Specifically:</p>
<ol>
<li>Camera Setup in 3D Slicer:<br>
There are no instructions in NeuroNav.ppt on how to configure the camera in 3D Slicer.<br>
How do I connect and configure the OptiTrack V120:Trio camera for use with 3D Slicer?</li>
<li>Hardware Connections (SlicerIGT-U03_HardwareConnections):<br>
I have installed both Motive software (for the OptiTrack system) and the “Plus Toolkit” application.<br>
What are the required hardware connections and setup steps between the camera, Motive, and 3D Slicer?</li>
<li>PLUS Configuration File:<br>
How do I create a correct PLUS configuration file for the V120:Trio camera?<br>
The file mentioned in the U03 tutorial—<code>TrackSTAR_ReferenceStylus-Capture.xml</code>—is missing from the <code>SlicerIGT-Data</code> folder.</li>
</ol>
<p>Can you provide a step-by-step guide for configuring the OptiTrack system with 3D Slicer using PLUS?   Thanks much!!</p>

---

## Post #2 by @nagy.attila (2025-05-10 16:33 UTC)

<p>Hi!</p>
<p>Let’s first break down a little on what to do:<br>
You do not “configure the camera” in Slicer. Slicer will get the tracking data through SlicerOpenIGTLink module (extension), and the data will be fed into that module (and eventually into Slicer) through the Plus server. You’ll likely need the SlicerIGT extension as well too (later for sure).</p>
<p>So… if you use optical markers with your tools (reference, various objects that you want to track, and so on), you have to define so called “rigid bodies” in Motive, and then save the motive workspace.<br>
Slicer will get the bodies, and the associated tracking info through the above mentioned setup.</p>
<p>Next step is to create a config file for the Plus server, with the motive file, and some info of your setup, what you want to track, and so on. The Plus webpage has great tutorials on the topic.<br>
Here is the section about the Optitrack cameras:</p><aside class="onebox allowlistedgeneric" data-onebox-src="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOptiTrack.html">
  <header class="source">

      <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOptiTrack.html" target="_blank" rel="noopener nofollow ugc">perk-software.cs.queensu.ca</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOptiTrack.html" target="_blank" rel="noopener nofollow ugc">Plus applications user manual: OptiTrack</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
We have a Duo, and I do not have experiences with the Trio, but I would think that there are no big differences between them. Someone more experienced may give you more exact hints here.</p>
<p>If you have an Optitrack Trio, I don’t think you need the Trackstar config <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Depending on your use case (you mention a stylus), you may need to take additional actions, but first understand how connections - both hardware and software - work, and how to create an initial configuration.</p>
<p>Attila</p>

---
