# How to automate sending of .stl file from cad software to 3D Slicer by scripting

**Topic ID**: 11198
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/how-to-automate-sending-of-stl-file-from-cad-software-to-3d-slicer-by-scripting/11198

---

## Post #1 by @rishikesh_hase (2020-04-20 06:33 UTC)

<p>How can I make a script in windows for transferring of .stl file from any folder or from CAD software to slicer automatically.</p>

---

## Post #2 by @Sam_Horvath (2020-04-20 13:28 UTC)

<p>To send from a script or application outside of Slicer, something like this would work:</p>
<pre><code class="lang-auto">Slicer.exe --python-code "slicer.util.loadModel( 'f/pth/to/model.stl' )" 
</code></pre>
<p>This will launch Slicer and load the requested stl model.  To load models into an already launched Slicer, something like <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Automatically_load_volumes_that_are_copied_into_a_folder" rel="nofollow noopener">this python snippet</a> would work within Slicer to have it monitor a folder to automatically load items saved there.</p>

---
