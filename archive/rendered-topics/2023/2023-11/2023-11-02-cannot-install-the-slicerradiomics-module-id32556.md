# Cannot install the SlicerRadiomics Module 

**Topic ID**: 32556
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/cannot-install-the-slicerradiomics-module/32556

---

## Post #1 by @melisaocbe (2023-11-02 13:14 UTC)

<p>Hello, community!</p>
<p>I have been struggling with 3D Slicer, python, PyRadiomics for days… I’m an oral and maxillofacial radiologist so I’m a total stranger for these topics such as coding and computing. Although, I would like to apply Radiomics features for scientific reasons. But somehow I could not:</p>
<ol>
<li>Install SlicerRadiomics from extension manager on 3D Slicer</li>
<li>I tried to install by python but I could not do it either.</li>
<li>I tried to manually install Radiomics extension by editing applications → modules → additional module paths → add … etc.</li>
<li>I’ve installed both stable and nightly versions and tried all, but no success.</li>
</ol>
<p>I’m using Mac btw.<br>
Please guide me like instructing a child because I’m really insufficient in this area but I really like to improve.</p>
<p>Oh, in addition, I tried the BoneTexture module in 3D Slicer (both nightly and stable) but when I click compute texture feature set, nothing happens at all.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2023-11-02 16:04 UTC)

<p><a class="mention" href="/u/melisaocbe">@melisaocbe</a> Thanks for reporting this.  You should have been able to just install Radiomics from the Extension Manager of the stable application and would not need to touch python or the module paths at all, but due to the error described below that’s not currently working on the mac for radiomics.  If you have the option of working on a windows or linux machine it should all go smoothly.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> do you have any thoughts on this build error?  It may be that the factory mac is missing one of the platform package like <a href="https://discourse.slicer.org/t/building-on-mac-10-14-mojave/4554">we’ve seen in the past</a>.</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=3197265" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/viewBuildError.php?buildid=3197265</a></p>
<pre><code class="lang-auto">      radiomics/src/_cmatrices.c:3:10: fatal error: 'stdlib.h' file not found

      #include &lt;stdlib.h&gt;
               ^~~~~~~~~~
      1 error generated.
      error: command '/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/bin/clang' failed with exit code 1
      [end of output]
</code></pre>

---

## Post #3 by @melisaocbe (2023-11-02 16:57 UTC)

<p>I tried with a Windows device, its working. Thank you so much!</p>

---
