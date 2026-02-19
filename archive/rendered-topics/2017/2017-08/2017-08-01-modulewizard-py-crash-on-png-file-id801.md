---
topic_id: 801
title: "Modulewizard Py Crash On Png File"
date: 2017-08-01
url: https://discourse.slicer.org/t/801
---

# ModuleWizard.py crash on png file

**Topic ID**: 801
**Date**: 2017-08-01
**URL**: https://discourse.slicer.org/t/modulewizard-py-crash-on-png-file/801

---

## Post #1 by @JK_Kim (2017-08-01 15:23 UTC)

<ol>
<li>
<p>Following on the HelloCLI tutorial…</p>
</li>
<li>
<p>Ran the <code>ModuleWizard.py</code> as follows…</p>
</li>
</ol>
<pre><code class="lang-auto">/Utilities/Scripts/ModuleWizard.py --template ./Extensions/Testing/CLIExtensionTemplate --target ../My_Module 
My_Module
</code></pre>
<ol start="3">
<li>Then, it crashes with the following error message… It seems like the script cannot handle .png file properly…</li>
</ol>
<pre><code class="lang-auto">creating G:/Libs/slicer/My_Module/My_Module\My_Module.png
Traceback (most recent call last):
  File "g:\Libs\slicer\Slicer\Utilities\Scripts\ModuleWizard.py", line 121, in &lt;module&gt;
    main(sys.argv[1:])
  File "g:\Libs\slicer\Slicer\Utilities\Scripts\ModuleWizard.py", line 115, in main
    copyAndReplace(file, template, target, templateKey, moduleName)
  File "g:\Libs\slicer\Slicer\Utilities\Scripts\ModuleWizard.py", line 38, in copyAndReplace
    contents = fp.read()
  File "C:\Python36\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 154: character maps to &lt;undefined&gt;
</code></pre>

---

## Post #2 by @pieper (2017-08-01 15:53 UTC)

<p>Hi -</p>
<p>Thanks for reporting.</p>
<p>To confirm, you were using this tutorial?<br>
<a href="https://www.slicer.org/wiki/Documentation/4.6/Training#HelloCLI" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.6/Training#HelloCLI</a></p>
<p>It may be that the ModuleWizard script only works with python 2.7 (looks like you are using 3.6).  Maybe try that and let us know?</p>
<p>Also the ExtensionWizard is probably a better way now.  If you look at this “Developing and Contributing Extensions for 3D Slicer” tutorial you can see how it works.  The only difference is that you pick ‘cli’ instead of ‘scripted’ when adding the module to your extension.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.6/Training#Developing_and_Contributing_Extensions_for_3D_Slicer" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.6/Training#Developing_and_Contributing_Extensions_for_3D_Slicer</a></p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @JK_Kim (2017-08-02 00:41 UTC)

<p>Yes, I was using the HelloCLI tutorial of the link.</p>
<p>Just now, I removed python36 and installed python27. The ModuleWizard<br>
script finished without any error, but the png file got corrupted and I<br>
could not open it. I assume…, not 100% sure… me, a python newbie… it<br>
is because the file was open as text file, modified, and saved as text<br>
file…  If my assumption is right…, I guess the same is true for all<br>
other binary files (the image files in the Data sub-folder).</p>
<p>Thanks for the link regarding ExtentionWizard. I’ll try it.</p>
<p>Best regards,<br>
Jinkoo</p>

---

## Post #4 by @lassoan (2017-08-02 13:07 UTC)

<p>The included .png file is just a placeholder. Replace it with your own icon.</p>

---
