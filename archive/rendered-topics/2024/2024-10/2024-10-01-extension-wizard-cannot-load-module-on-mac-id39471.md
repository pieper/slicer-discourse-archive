---
topic_id: 39471
title: "Extension Wizard Cannot Load Module On Mac"
date: 2024-10-01
url: https://discourse.slicer.org/t/39471
---

# Extension Wizard Cannot Load module on Mac

**Topic ID**: 39471
**Date**: 2024-10-01
**URL**: https://discourse.slicer.org/t/extension-wizard-cannot-load-module-on-mac/39471

---

## Post #1 by @alexjin (2024-10-01 12:50 UTC)

<p>Hi, I encountered a problem where if these lines are included in the code, the module cannot be loaded through extension wizard:</p>
<pre><code class="lang-auto">            # Check if binary labelmap is valid
            if binary_labelmap.GetNumberOfPoints() &gt; 0:
                # Count the non-zero voxels in the binary labelmap
                volume_pixels = 0
                data = vtk.util.numpy_support.vtk_to_numpy(binary_labelmap.GetPointData().GetScalars())
                volume_pixels = (data &gt; 0).sum()

                # Assuming you know the spacing of the labelmap to convert to volume in cm³
                spacing = binary_labelmap.GetSpacing()
                volume_cm3 = volume_pixels * spacing[0] * spacing[1] * spacing[2] / 1000.0  # Convert mm³ to cm³

                # Get the segment name
                segment_name = segmentation.GetSegment(segment_id).GetName()
                segment_volumes[segment_id] = (segment_name, volume_cm3)
                total_volume += volume_cm3

                print(f"{segment_name} volume = {volume_cm3:.3f} cm³, {volume_cm3}")
</code></pre>
<p>After I press select extension and select the correct folder, the extension editor shows the files in the directory, but I don’t get a popup for adding modules.</p>
<p>I have tested with ARM and Intel Macs and both had the same issues, however it worked fine on windows devices.</p>
<p>The only way I found to add the module is by deleting these lines, and the problem persists if they are only commented out.</p>
<p>Thanks in advance for any help!</p>

---

## Post #2 by @pieper (2024-10-01 12:52 UTC)

<aside class="quote no-group" data-username="alexjin" data-post="1" data-topic="39471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/5daacb/48.png" class="avatar"> alexjin:</div>
<blockquote>
<p><code># Convert mm³ to cm³</code></p>
</blockquote>
</aside>
<p>Hard to say for sure, but I’d get rid of these superscripts and use a convention like <code>mm^3</code> (i.e. all ascii).</p>

---

## Post #3 by @alexjin (2024-10-01 13:03 UTC)

<p>Unfortunately the problem is still there after I deleted all non-ASCII characters <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @pieper (2024-10-01 13:13 UTC)

<p>Maybe characters in the file path?</p>

---

## Post #5 by @alexjin (2024-10-01 13:17 UTC)

<p>That fixed it, thanks!</p>

---
