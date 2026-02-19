---
topic_id: 27991
title: "Save Igtlink 3D Coordinates"
date: 2023-02-22
url: https://discourse.slicer.org/t/27991
---

# Save IGTLink 3D coordinates

**Topic ID**: 27991
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/save-igtlink-3d-coordinates/27991

---

## Post #1 by @Hugo_Angulo (2023-02-22 22:30 UTC)

<p>Hi there,</p>
<p>I am currently simulating that I receive some coordinates through the usage of the TrackerSim binary file that I found in an old page in the website. Now, I was able to mimic that this is a remote machine that is sending coordinates to another machine in which I have 3D Slicer running with IGTLink as a server. Initially I started the server in 3D Slicer, and after some time working on the TrackerSim, I was able to transmit some data. After that, I figured that there is a feature that allows you to ‘Collect Points’, so I assumed that this is what I wanted, and I was correct on that since I started to see that there were some ‘dots’ that got drawn into the 3D view. I was trying to download those streamed coordinates, but when I hit the SAVE button it only saves a txt file that has the following form:</p>
<p><span class="hashtag">#Insight</span> Transform File V1.0<br>
<span class="hashtag">#Transform</span> 0<br>
Transform: AffineTransform_double_3_3<br>
Parameters: -0.9974045864631055 0.04716505426897695 0.05439964112597738 -0.04716505426897695 0.14285717972280787 -0.9886188497583283 -0.05439964112597738 -0.9886188497583283 -0.1402618257905485 -49.41922555485868 -1.6675462033025057 -7.413424280973429<br>
FixedParameters: 0 0 0</p>
<p>How can I save all the coordinates that I have sent to the IGTLink Server in a CSV or TXT file? Or is there any other format that I can use to save ALL of the coordinates transmitted during a certain period of time?</p>
<p>Thanks and I do appreciate your help!</p>

---
