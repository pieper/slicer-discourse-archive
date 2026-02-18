# pkModelling from bash and python console

**Topic ID**: 3633
**Date**: 2018-08-02
**URL**: https://discourse.slicer.org/t/pkmodelling-from-bash-and-python-console/3633

---

## Post #1 by @be2be (2018-08-02 06:54 UTC)

<p>dear experts,</p>
<p>it would be great to have an example command for (mac) bash as well as python for invoking pkModelling (and associated parameter set).</p>
<p>thank you so much!</p>

---

## Post #2 by @fedorov (2018-08-03 22:00 UTC)

<p>PkModeling module is a CLI (Command Line Interface) type of Slicer module. In this sense, the generic instructions for invoking it from command line or from python apply.</p>
<p>Can you please read the following FAQ entries, and let us know what is missing from those that you need to achieve your tasks?</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_call_a_CLI_module_from_command-line.3F">How to call a CLI module from command-line?</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_run_CLI_module_from_Python.3F">How to run CLI module from Python?</a></li>
</ul>

---

## Post #3 by @be2be (2018-08-04 13:42 UTC)

<p>Thanks. I’m struggling with the very basics. I can’t find a description of the command and the way to parse arguments. What I found is an example command posted back in 2015 <a href="http://slicer-users-archive.65878.n3.nabble.com/multivolumeimporter-PkModeling-td4029136.html" rel="nofollow noopener">here</a>. But parameter names seem to have changed.<br>
So I tried this without success ( Image Exception : <span class="hashtag">#22</span> :: ERROR: Could not open image Applications/Slicer.app/Contents/Extensions-26813/PkModeling/lib/Slicer-4.8/cli-modules/PkModeling Error in slicer input, exiting…):</p>
<p>Slicer --launch Applications/Slicer.app/Contents/Extensions-26813/PkModeling/lib/Slicer-4.8/cli-modules/PkModeling --T1PreBloodValue 1400 --T1PreTissueValue 911 --RelaxivityValue 0.0056 --Hematocrit 0.42 --UsePopulationAIF --InputFourDImageFileName DCE_input.nrrd --OutputKtransFileName Ktrans.nii.gz --ConstantBAT 3 --OutputFittedDataImageFileName outFit.nii.gz</p>
<p>Totally off the track?</p>

---

## Post #4 by @fedorov (2018-08-04 14:59 UTC)

<p>Did you try <code>--help</code>? It will show all of the parameters of the module.</p>

---

## Post #5 by @be2be (2018-08-04 19:21 UTC)

<p>Yes, I tried that, but got the same error… Seems that Slicer isn’t launching pkmodeling at all…</p>

---

## Post #6 by @fedorov (2018-08-04 22:50 UTC)

<p>Ah, sorry - I missed your error in the initial post.</p>
<p>I see you are on Mac - can you try running PkModeling directly? I don’t think you need the launcher. The command below works for me:</p>
<pre><code class="lang-bash">$ /Applications/Slicer.app/Contents/Extensions-27332/PkModeling/lib/Slicer-4.9/cli-modules/PkModeling --help

USAGE:

   /Applications/Slicer.app/Contents/Extensions-27332/PkModeling/lib/Slicer
                                        -4.9/cli-modules/PkModeling
                                        [--returnparameterfile
                                        &lt;std::string&gt;]
                                        [--processinformationaddress
                                        &lt;std::string&gt;] [--xml] [--echo]
                                        [--deserialize &lt;std::string&gt;]
                                        [--serialize &lt;std::string&gt;]
                                        [--outputDiagnostics &lt;std::string&gt;]
                                        [--fitted &lt;std::string&gt;]
                                        [--concentrations &lt;std::string&gt;]
                                        [--outputBAT &lt;std::string&gt;]
                                        [--outputRSquared &lt;std::string&gt;]

</code></pre>

---

## Post #7 by @lassoan (2023-03-21 03:00 UTC)



---
