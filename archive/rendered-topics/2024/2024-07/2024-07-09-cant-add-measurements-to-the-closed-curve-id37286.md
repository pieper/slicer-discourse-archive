---
topic_id: 37286
title: "Cant Add Measurements To The Closed Curve"
date: 2024-07-09
url: https://discourse.slicer.org/t/37286
---

# Can't add measurements to the closed curve

**Topic ID**: 37286
**Date**: 2024-07-09
**URL**: https://discourse.slicer.org/t/cant-add-measurements-to-the-closed-curve/37286

---

## Post #1 by @Miguel_Nobre_Menezes (2024-07-09 15:09 UTC)

<p>I’m trying to add measurements to the closed curve markup:</p>
<pre><code class="lang-auto">&gt; # Create a new measurement instance
&gt; 
&gt; last_one = slicer.vtkMRMLMeasurementLength()
&gt; 
&gt; # Configure the new measurement
&gt; 
&gt; last_one.SetName("last_one")
&gt; 
&gt; last_one.SetUnits("mm")
&gt; 
&gt; last_one.SetValue(80.00) # Set the value
&gt; 
&gt; # Add the new measurement to the closed curve node
&gt; 
&gt; cc.AddMeasurement(last_one)
</code></pre>
<p>But every time I change the enabled status, by toggling or untoggling on the list, the value is gone. I believe the issue may lie with the observers, since they are different in existing measurements. But I cannot get them to change…</p>

---
