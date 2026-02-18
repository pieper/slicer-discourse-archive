# Using DRRGeneratorModule in a Python script

**Topic ID**: 35022
**Date**: 2024-03-22
**URL**: https://discourse.slicer.org/t/using-drrgeneratormodule-in-a-python-script/35022

---

## Post #1 by @Yassin_Abdelrahman (2024-03-22 13:36 UTC)

<p>Hi all,</p>
<p>I would like to use the above module in a python script but am unsure how to do so. Below is something I have tried but I do not have that much experience in working in Slicer so I think I am misunderstanding the way modules are used correctly. If anyone can help me correct this It would be highly appreciated!</p>
<pre><code class="lang-auto">import slicer
import os

# Load CT volume
ct_volume = slicer.util.loadVolume(ct)

# Create DRR generator node
drr_generator = slicer.modules.drrgeneratormodule

# Set parameters
parameters = {}
parameters["InputVolume"] = ct_volume.GetID()
parameters["OutputResolution"] = [512, 512]

# Generate DRR
slicer.cli.runSync(drr_generator, None, parameters)

# Save DRR
output_path = os.path.join(output_folder, "drr.nii.gz")
slicer.util.saveNode(slicer.util.getNode('DRR'), output_path)
</code></pre>
<p>Thank you,<br>
Yassin</p>

---
