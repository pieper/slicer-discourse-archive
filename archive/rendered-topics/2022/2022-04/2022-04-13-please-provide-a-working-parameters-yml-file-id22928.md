# Please provide a working parameters.yml file

**Topic ID**: 22928
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/please-provide-a-working-parameters-yml-file/22928

---

## Post #1 by @harad (2022-04-13 06:45 UTC)

<p>Hi to everyone, I would like to produce a Parameters file for Slicerradiomics to customize the extraction of ALL image types and ALL feature classes.<br>
I found several examples of Parameter files in this forum and on GitHub, saved them as YAML through Visual Studio Code and checked each in YAML Lint.<br>
Without the file (manual customization) I do get a table with calculations. But with each of the Params.yml files, the calculation stops after about 10 seconds and the table remains empty.<br>
I am quite desperate and stuck and would greatly appreciate a working Params.yml file that instructs to generate all image transformations and calculations of all available features. I assume that just about anyone who used SlicerRadiomics should have a parameters file.<br>
Cheers,<br>
Marko</p>

---

## Post #2 by @JoostJM (2022-05-03 07:38 UTC)

<p>Did you open the python window in slicer? If the extraction fails, it should print an error as to why this happens in the python window.<br>
If you can find the error, but don’t understand it, please post it here, so we are better able to help you.</p>

---

## Post #4 by @harad (2022-06-22 09:54 UTC)

<p>Many thanks for your feedback, I was mainly interested in getting a functional Params file than troubleshooting, so miraculously I did manage to produce it with my non-existent coding skills - it leads to the calculation of 1340 features.<br>
This must be close to  all  available repertoire.<br>
I suggest putting this file in the manual, so who wants to skip some feature class or image type- it is easy to downsize even for non-coders.<br>
Here is the file:</p>
<pre><code class="lang-auto">    Original: {}
    LoG: {'sigma' : [1.0, 3.0]} 
    Wavelet:
        binWidth: 10

    Square: {}
    Logarithm: {}
    Exponential: {}


featureClass:
    glcm:
    firstorder:
    shape:
    glrlm:
    glszm:
    gldm:
    ngtdm:
</code></pre>

---
