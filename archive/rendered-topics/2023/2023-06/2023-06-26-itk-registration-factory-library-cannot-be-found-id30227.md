# ITK registration factory library cannot be found

**Topic ID**: 30227
**Date**: 2023-06-26
**URL**: https://discourse.slicer.org/t/itk-registration-factory-library-cannot-be-found/30227

---

## Post #1 by @jhlegarreta (2023-06-26 02:15 UTC)

<p>Hi,<br>
I am using 3D Slicer 5.2.2 r31382 / fb46bd1 on an Ubuntu 22.04 machine. I am trying to launch the <code>DWIConvert</code> process from the command line:</p>
<pre><code class="lang-auto">$DWIConvert --conversionMode FSLToNrrd --outputVolume $DWI --fslNIFTIFile $fslNIFTIFile --outputDirectory . --smallGradientThreshold 0.2 --transposeInputBVectors --inputBValues $inputBValues --inputBVectors $inputBVectors --outputDirectory . --smallGradientThreshold 0.2 --transposeInputBVectors --allowLossyConversion
</code></pre>
<p>where <code>$DWIConvert</code> points to <code>/opt/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2/cli-modules/DWIConvert</code> in my Slicer installation, and the rest of the parameters having some appropriate values.</p>
<p>The command exits with the following error:</p>
<pre><code class="lang-auto">/opt/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2/cli-modules/DWIConvert: error while loading shared libraries: libITKFactoryRegistration.so: cannot open shared object file: No such file or directory
</code></pre>
<p>A <code>find</code> command on the library shows that it is there:</p>
<pre><code class="lang-auto">$ find /opt/Slicer-5.2.2-linux-amd64 -name *libITKFactoryRegistration*
/opt/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2/libITKFactoryRegistration.so
</code></pre>
<p>Even when adding the Slicer root folder to the  PATH`  the library is not found.</p>
<p>How can this be fixed?</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-06-26 13:12 UTC)

<p>Try <code>Slicer --launch DWIConvert ..</code></p>

---

## Post #3 by @jhlegarreta (2023-06-26 13:52 UTC)

<p>That worked. Thanks for the support Steve.</p>

---
