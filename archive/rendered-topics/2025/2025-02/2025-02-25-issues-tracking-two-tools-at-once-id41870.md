---
topic_id: 41870
title: "Issues Tracking Two Tools At Once"
date: 2025-02-25
url: https://discourse.slicer.org/t/41870
---

# Issues tracking two tools at once

**Topic ID**: 41870
**Date**: 2025-02-25
**URL**: https://discourse.slicer.org/t/issues-tracking-two-tools-at-once/41870

---

## Post #1 by @Arber_Demi (2025-02-25 11:40 UTC)

<p>Hello everyone.</p>
<p>I am working on developing a small tracking script to store specific tracking data, and in my specific case I need to track two tools at the same time. One of them is a pointer, and the other can be anything. Tracking works fine for both tools separately, and when they are both in view it also works fine, however, the first time the pointer tool enters in view it ruins the tracking for the other tool.</p>
<p>For some reason, the tracking from that moment onwards seems to be linked with the pointer tool. Anytime it is not in view, the other tool does not update its transform information anymore. The moment the pointer comes back into view, then everything works fine. I’m not sure if this behaviour is being caused by how the data is transmitted to slicer, or by the data handling from the module. Any tips or information on this would be really appreciated.</p>
<p>I am using Slicer 5.8 for this, however I get the same behaviour in 5.6.2</p>

---

## Post #2 by @Arber_Demi (2025-02-25 13:27 UTC)

<p>If there is anyway I can somehow get a trace of events that happen internally within the OpenIGTLinkIF module whenever handling tracking data, that would probably help to figure out the issue, is that possible without building from source?</p>

---

## Post #3 by @Arber_Demi (2025-02-25 14:29 UTC)

<p>A quick clarification, in the first part of the post I said “…the first time the pointer tool enters in view it ruins the tracking for the other tool.”, however I meant “the first time the pointer tool enters in view <strong>while the secondary is in view aswell</strong> it ruins the tracking for the other tool.”</p>
<p>After taking a closer look and printing out the contents of the query response (IGTLTrackingDataBundleNode) and the elements inside it (LinearTransformNode), there are no updates happening to the transform matrices of the secondary tool once the issue starts. If the secondary tool is in view on its own after the issue, the only thing that updates inside the LinearTransformNode is the MTime, which keeps going up as usual.</p>
<p>At first I thought this might be an issue with the device I am getting the tracking data from, however when trying to communicate to the device through a data recording script (the Example for Tracker Client Program in C++ provided by OpenIGTLink), I can see inside the TDATA that all of the transform data updates just fine.</p>
<p>This makes me think that there’s some issue with how the Slicer module is currently handling the data it receives, or maybe the checks it uses to update nodes. I haven’t been able to find anything in the C++ files that seems like it could cause this, but I am not as experienced in C++. Would really appreciate any help.</p>

---

## Post #4 by @Arber_Demi (2025-03-04 12:38 UTC)

<p>I have figured out the issue after building everything from source and doing some debugging.</p>
<p>To give a summary of everything once again, I was trying to track two tools, Tool1 and Tool2 using information obtained from OpenIGTLink. Separately they are both tracked fine, however the moment they both come into view at the same time, the tracking for Tool2 (when Tool1 is not in view) is broken. It does not update its transform data anymore (even though the MTime variable does). After some debugging, I figured out that the positioning of the data inside the <code>igtlioTrackingDataConverter::ContentData</code> object alongside how the transforms are updated to be the cause of this issue.</p>
<p>ContentData has a map which carries the information for each tracked tool.</p>
<pre><code class="lang-auto">struct ContentData
{
  std::map&lt;int, ContentEntry&gt; trackingDataElements;
};
</code></pre>
<p>However when multiple tools apear, the position of those tools in that map changes. They are seemingly sorted alphabetically, so if both tools appear at once, then the map updates to show Tool1 first then Tool2. However, if Tool1 goes out of view and Tool2 remains, the map still has a version of Tool2 at its old position. So if we loop through the map, we would get the new and updated Tool2 with the correct transform, then the old Tool2 with the old and wrong transform.</p>
<p>Due to how iterating and updating is currently handled in <code>void vtkMRMLIGTLConnectorNode::ProcessIncomingDeviceModifiedEvent</code> at the moment (coming from SlicerOpenIGTLink/OpenIGTLinkIF/MRML) , the correct version is handled first, the tool position is updated correctly, and then the old version is handled after and simply reverts the position back. This keeps happening until Tool1 comes back into view with Tool2, where now Tool2 updates normally again (as the maps only version of Tool2 is now correct).</p>
<p>At the moment I have remedied this by adding the following code:</p>
<pre><code class="lang-auto">for (int b = 0; b &lt; content.trackingDataElements.size()-1; b++) {
    if (content.trackingDataElements[b].deviceName.compare(content.trackingDataElements[b + 1].deviceName) == 0)
    {
        content.trackingDataElements.erase(b + 1);
    }
}   
</code></pre>
<p>This is placed between<br>
<code>igtlioTrackingDataConverter::ContentData content = tdataDevice-&gt;GetContent();</code> and<br>
<code>for (auto iter = content.trackingDataElements.begin(); iter != content.trackingDataElements.end(); iter++)</code> inside the else if case handling “TDATA” in the <code>void vtkMRMLIGTLConnectorNode::ProcessIncomingDeviceModifiedEvent</code> function.</p>
<p>I think the easiest way to solve this would be to have the map keys be something other than integers, since they have no guarantee that the same tool is not updated twice.</p>
<p>I would love to get some suggestions on this as I plan to make a pull request to hopefully fix this issue in a later version of Slicer.</p>

---

## Post #5 by @lassoan (2025-03-04 17:36 UTC)

<p>Thanks for the detective work, this is very useful. <code>TDATA</code> messages are not used very often, probably that’s why this error has not been noticed so far.</p>
<p>Why does <code>trackingDataElements</code> contain multiple entries for the same tool?</p>
<ul>
<li>A. the <code>TDATA</code> message contained multiple entries for the same tool</li>
<li>B. entries remain there from previous <code>TDATA</code> messages</li>
</ul>
<p>If A) then the sender of the message should be fixed (and maybe Slicer/OpenIGTLink/OpenIGTLinkIO could be made more robust).</p>
<p>If B) then probably we should clear out the <code>trackingDataElements</code> before starting to process a TDATA message.</p>

---

## Post #6 by @Arber_Demi (2025-03-04 18:55 UTC)

<p>I will clarify whether it is A) or B) tomorrow after taking another look at the data extracted through the “Example for Tracker Client Program” script.</p>

---

## Post #7 by @Arber_Demi (2025-03-05 09:20 UTC)

<p>I took a look at the <code>int igtlioTrackingDataConverter::fromIGTL()</code> function inside <code>OpenIGTLinkIO/Converter/igtlioTrackingDataConverter.cxx</code> and the data coming from <code>igtl::TrackingDataMessage::Pointer transMsg</code> (which is copying the information straight from the <code>igtl::MessageBase source</code> object). There are no duplicates inside, so I think the issue is somewhere within how <code>trackingDataElements</code> is updated.</p>
<p>I will have more time next week to investigate further and perhaps introduce a better solution than just deleting duplicate names from <code>trackingDataElements</code>.</p>

---
