# Model to Model Distance command line

**Topic ID**: 33384
**Date**: 2023-12-13
**URL**: https://discourse.slicer.org/t/model-to-model-distance-command-line/33384

---

## Post #1 by @jhernandezr (2023-12-13 21:37 UTC)

<p>Hello there!</p>
<p>Me and my teammates are trying to develop a project where we need to apply the model to model distance module with a command line and we were unable to do so.</p>
<p>Is there anyone that knows how to call that module from the terminal?</p>
<p>Thank you in advance!!</p>

---

## Post #2 by @rfenioux (2023-12-14 10:45 UTC)

<p>What issue are you encountering ?</p>
<p>This would be the command to run the cli from the terminal :</p>
<pre><code class="lang-auto">[path_to_the_cli]/ModelToModelDistance.exe -t TargetModel.vtk -s SourceModel.vtk -o OutputModel.vtk -d signed_closest_point
</code></pre>

---

## Post #3 by @RafaelPalomar (2023-12-14 11:04 UTC)

<p><a class="mention" href="/u/jhernandezr">@jhernandezr</a> the <code>ModelToModelDistance modle</code>  is a command-line module, which can be called from command line directly as <a class="mention" href="/u/rfenioux">@rfenioux</a> suggests. The module requires though the use of some other libraries that won’t be found unless some Slicer environment variables are set. For me, invoking the module through <code>Slicer --launch</code> worked fine:</p>
<pre data-code-wrap="sh"><code class="lang-sh">./Slicer --launch slicer.org/Extensions-32438/ModelToModelDistance/lib/Slicer-5.6/cli-modules/ModelToModelDistance -s /tmp/m1.vtk -t /tmp/m2.vtk -o /tmp/output.vtk
</code></pre>

---
