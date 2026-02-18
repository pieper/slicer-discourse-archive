# Is there any api update in Slicer 5.7?

**Topic ID**: 35741
**Date**: 2024-04-26
**URL**: https://discourse.slicer.org/t/is-there-any-api-update-in-slicer-5-7/35741

---

## Post #1 by @derekcbr (2024-04-26 04:32 UTC)

<pre data-code-wrap="python"><code class="lang-python">args = [slicer_output_file, "--additional-module-paths", slice_installation_path, "--python-code", "print('Start Slicer from Blender!')", "--python-script", startup_slice_script_file]
process = subprocess.Popen([slicer_path] + args, shell=True)
</code></pre>
<p>When running this in Blender, can not install the Slicer addon properly. But it works in 5.6.</p>

---

## Post #2 by @derekcbr (2024-04-26 07:26 UTC)

<p>It works in Windows, but not in MacOS.</p>

---
