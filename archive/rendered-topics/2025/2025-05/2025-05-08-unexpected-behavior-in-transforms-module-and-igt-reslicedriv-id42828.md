# Unexpected behavior in Transforms Module and IGT ResliceDriver

**Topic ID**: 42828
**Date**: 2025-05-08
**URL**: https://discourse.slicer.org/t/unexpected-behavior-in-transforms-module-and-igt-reslicedriver/42828

---

## Post #1 by @sfrisken (2025-05-08 13:36 UTC)

<p>When tracking two instruments using the Brainlab system and OpenIGTLink:</p>
<ol>
<li>OpenIGT link transfers transforms for both instruments from BrainLab to Slicer as expected</li>
<li>As long as only one instrument is ever visible at a time, things work as expected<br>
a) Transform sliders and transforms change in real time in the Transform Module as expected<br>
b) Slice views are controlled by the transforms assigned in the ResliceDriver as expected</li>
<li>If at some point, both instruments become visible, the Transforms Module and ResliceDriver both behave in unexpected ways<br>
a) As long as both instruments are visible and until one of the instruments becomes not visible:
<ul>
<li>Transform sliders and transforms behave as expected in the Transforms Module</li>
<li>Slice views are controlled as expected by the ResliceDriver<br>
b) As soon as one of the two instruments becomes not visible and thereafter until Slicer is stopped and restarted:</li>
<li>The transform from one of the two instruments (always the same one, possibly determined by the order Brainlab sends transforms) no longer impacts the Transforms Module (sliders and transforms do not change when the instrument is moved) and the ResliceDriver (transform does not control the assigned slice view)<br>
c) Note that both transforms continue to be received via OpenIGTLink as expected and both emit move events. (We have an independent module that observes and records transform events. The behavior of the Transforms Module and ResliceDriver described here occurs whether or not our module is opened/activated.)</li>
</ul>
</li>
</ol>
<p>I think this may have something to do with how observers are attached/detached from transforms in the Transforms Module and ResliceDriver. However, the behavior is buried under multiple layers in vtk and MRML that I am having trouble tracing through the code.</p>
<p>Is there anyone familiar with these modules and/or the vtk observer model who might be able to help us with this issue? It is a blocking issue on software we used regularly during tumor resections.</p>
<p>Thanks!<br>
Sarah</p>

---

## Post #2 by @ungi (2025-05-08 18:38 UTC)

<p>Hi Sarah,</p>
<p>It sounds very strange that your custom module can successfully observe and record the transforms, but the Transforms module cannot.</p>
<p>Is the MRML transform node representing the problematic instrument updated in any way when the instrument is in view of the tracker? Is there maybe another MRML node in the scene created for some reason and that is being updated?</p>
<p>Each MRML node has an “MTime” property that you can watch using the Node info module. That is a timestamp for when it was last modified. Is that changing while you experience the problem? If that is not changing, then most modules would not get notified about the updates. (But it should change when new messages are received from the tracker.)</p>
<p>When IGTL transform messages arrive in Slicer, they are converted to MRML nodes, identified by the IGTL device name and the matching MRML node name. If there IGTL device name changes, then there may be no matching MRML node, so OpenIGTLinkIF creates one that is not associated with the reslice driver. Any chance the IGTL device names changes while the problem is happening?</p>
<p>These are just some ideas to start thinking along. Please let me know if you figure out more.</p>
<p>Tamas</p>

---

## Post #3 by @sfrisken (2025-05-08 19:33 UTC)

<p>Hi Tamas, thanks very much for your quick reply. I will do some more sleuthing based on your suggestions. In the meantime, here are some things we’ve observed:</p>
<p><em>It sounds very strange that your custom module can successfully observe and record the transforms, but the Transforms module cannot.</em></p>
<p>Yes, we agree it is odd. We checked this several times to make sure.</p>
<p><em>Is the MRML transform node representing the problematic instrument updated in any way when the instrument is in view of the tracker? Is there maybe another MRML node in the scene created for some reason and that is being updated?</em></p>
<p>This is possible. We checked that there is only one transform per instrument listed in the Data Module. I can check to see if there are some unnamed nodes that don’t appear there.</p>
<p><em>Each MRML node has an “MTime” property that you can watch using the Node info module. That is a timestamp for when it was last modified. Is that changing while you experience the problem? If that is not changing, then most modules would not get notified about the updates. (But it should change when new messages are received from the tracker.)</em></p>
<p>When I record transforms in my module (which sees both instruments changing even when Transforms and ResliceDriver do not), I also record the times of the transform matrix – these do change with each event. I can double check in the Transforms Module to see if they change there.</p>
<p><em>When IGTL transform messages arrive in Slicer, they are converted to MRML nodes, identified by the IGTL device name and the matching MRML node name. If there IGTL device name changes, then there may be no matching MRML node, so OpenIGTLinkIF creates one that is not associated with the reslice driver. Any chance the IGTL device names changes while the problem is happening?</em></p>
<p>I can dig deeper into this, possibly by printing out all the transform nodes to see if they change when the behavior occurs. Perhaps my module identifies the transform with a field that doesn’t change while the other Slicer modules use one that does? I will see what I can discover.</p>
<p>I will try these next time I have access to the equipment (probably next week). Let me know if you think of other things I should test.</p>
<p>Sarah</p>

---

## Post #4 by @cpinter (2025-05-14 11:30 UTC)

<p>Hi Sarah,</p>
<p>Did this configuration work correctly before? Or is this a new setup that you’d like to get working? If it used to work but stopped working, it could be useful to know if there was any update on any side after which this problem started.</p>
<p>Do you see any errors in the Python console? An obvious question but could help a lot, and I don’t see it mentioned that there are no apparent error messages.</p>
<p>I’m not familiar with how BrainLab is connected to Slicer, but is PLUS involved? If so, can you share the configuration XML file please?</p>

---

## Post #5 by @sfrisken (2025-05-14 19:27 UTC)

<p>Hi Csaba, thanks for thinking about this for us. The clinical team assures us that the configuration worked a few years ago. It is not clear exactly when it broke – the earliest I heard about it was about 1 year ago. I only started digging into it this month. It is possible that Brainlab updated their software during that period but we don’t have access to that information.</p>
<p>I don’t see any errors in the Python code. I have my Python logging level set to ‘info’. We also checked the log and didn’t see anything obvious.</p>
<p>We don’t use Plus, so there is no config file. We use OpenIGTLinkIF to connect to Brainlab and OpenIGTLinkRemote to access tracking data (using the Start/Stop buttons).</p>
<p>The strange thing is that my custom module gets the expected transform events but the Transforms Module and ResliceDriver do not seem to get them consistently (see below) This happens even when my module is not installed. I wonder if it has to do with event processing. In my module, I use AddObserver() in my tracked instrument class to observe and respond to transform changes, while the two Slicer modules use setAndObserveTransformNodeID(). I tried to see how these approaches are related, but got lost in the class layers.</p>
<p>I’m just speculating. However, what if Brainlab or OpenIGTLink changed from sending an event per transform to sending a bundle of transforms per event? It might cause unexpected behavior if more than one transform is sent and only the first transform is processed.</p>
<p>For a recap of the behavior: assuming we are tracking two instruments, i1 and i2 then</p>
<ol>
<li>
<p>If only one instrument (i1 or i2) is ever visible at a time, the Transforms Module and the Reslice Driver observe changes to both transforms.</p>
</li>
<li>
<p>If at any point, both i1 and i2 become visible at the same time, things chage. Thereafter<br>
a) if both are visible and both are moving, the two slicer modules respond to the transform of i1 but <strong>do not</strong> respond to the transform of i2 <strong>unless</strong> i1 is stationary<br>
b) if i2 is visible but i1 is not visible, the two slicer modules <strong>do not</strong> respond to the transform of i2</p>
</li>
</ol>
<p>I have access to the Brainlab system this Friday (we have limited access because it’s used clinically) so I’m going to make the tests Tomas suggested. Let me know if there is anything else you think I should try.</p>
<p>Many thanks!<br>
Sarah</p>

---

## Post #6 by @cpinter (2025-05-15 11:08 UTC)

<p>Thank you for the detailed answer! I have a very hard time imagining that OpenIGTLink has observation issues. It has been working (I’d guess) for at least a decade without any considerable changes to the base code, and it can handle more than two tracked devices without an issue. I see the probability of this being a bug in OpenIGTLink really low.</p>
<p>The only thing that keeps popping into my head (without knowing anything on how the BrainLab connection is set up, but surely there is some kind of configuration there) is that the name or ID of the two transforms are the same, or something of this sort, and one “overwrites” the other, and causes some kind of conflict.</p>
<p>Sorry I know this is very vague. If you can share more details about the connection to the hardware after your visit on Friday maybe we can try to diagnose the issue better.</p>

---

## Post #7 by @tokjun (2025-05-30 17:29 UTC)

<p>Hi All,</p>
<p>I had a chance to test this with <a class="mention" href="/u/sfrisken">@sfrisken</a> today, and we identified the root cause. It turns out that the server software (Brainlab) sends TDATA messages that containing two elements (transforms) with the same transform names under certain scenarios, which leads to the behavior described above.</p>
<p>Initially, when only one instrument (“i1”) is in the field, the TDATA message sent by Brainlab contains:</p>
<ul>
<li>Element 0: “Reference”</li>
<li>Element 1: “i1”</li>
</ul>
<p>When SlicerOpenIGTLink receives this message, it creates and updates vtkMRMLLinearTransformNodes with the same name (i.e., “Reference” and “i1”)</p>
<p>Once a second instrument is added, the TDATA message becomes:</p>
<ul>
<li>Element 0: “Reference”</li>
<li>Element 1: “i1”</li>
<li>Element 2: “i2”</li>
</ul>
<p>and SlicerOpenIGTLink creates a third vtkMRMLLinearTransformNode named “i2.”</p>
<p>When the first tool (i.e., “i1”) is removed from the field, Brainlab is supposed to send:</p>
<ul>
<li>Element 0: “Reference”</li>
<li>Element 1: “i2”</li>
</ul>
<p>Instead, it sends a TDATA message without removing the last element:</p>
<ul>
<li>Element 0: “Reference”</li>
<li>Element 1: “i2” (with the up-to-date transform)</li>
<li>Element 2: “i2” (with the last transform before removing “i1”)</li>
</ul>
<p>As a result, SlicerOpenIGTLink processes both elements 1 and 2 and overwrite the first transform (Element 1) with the second (Element 2).</p>
<p>So, I think SlicerOpenIGTLink behaves as expected, but Brainlab appears not to adjust the message size properly when the number of visible instruments changes, leading to this issue.</p>

---

## Post #8 by @tokjun (2025-05-30 17:36 UTC)

<p>A quick fix, which can be made without requiring any changes to Brainlab, could be to read the TDATA elements in reverse order, so that only the first occurrence of each transform name is used if duplicates are present.</p>
<p>We could potentially detect duplicates and warn the user, but I don’t know if it is a good idea from the performance perspective.</p>

---

## Post #9 by @sfrisken (2025-05-30 20:22 UTC)

<p>Many thanks to Junichi who helped me figure out and address this rather obscure issue!</p>

---
