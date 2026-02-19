---
topic_id: 5017
title: "Using Slicerelastix Binaries In The Terminal"
date: 2018-12-08
url: https://discourse.slicer.org/t/5017
---

# Using SlicerElastix binaries in the terminal

**Topic ID**: 5017
**Date**: 2018-12-08
**URL**: https://discourse.slicer.org/t/using-slicerelastix-binaries-in-the-terminal/5017

---

## Post #1 by @brhoom (2018-12-08 14:54 UTC)

<p>Operating system: Ubuntu<br>
Slicer version: 4.10<br>
Expected behavior: work<br>
Actual behavior: does not work</p>
<p>Based on <a href="https://discourse.slicer.org/t/extension-contribution-checklist/4975/2">this</a> and <a href="https://discourse.slicer.org/t/vissim-cochlea-tools-extension-is-now-public/4122/15">this</a> discussions, I tried to use:</p>
<pre><code>  .config/NA-MIC/Extensions-27501/SlicerElastix/lib/Slicer-4.10/elastix  
</code></pre>
<p>but I  got this error:</p>
<pre><code>  .config/NA-MIC/Extensions-27501/SlicerElastix/lib/Slicer-4.10/elastix: error while loading shared libraries: libi2d.so.13: cannot open shared object file: No such file or directory
</code></pre>
<p>I know I can just call some function but I will have to modify many things in my code. Is there another way to call it from the terminal?</p>

---

## Post #2 by @lassoan (2018-12-08 15:14 UTC)

<p>Can you start Elastix bundled with the latest nightly version? Does Elastix work with the latest nightly build when launched useing “General registration (Elastix)” module? Next steps depend on the answer to these questions.</p>

---

## Post #3 by @brhoom (2018-12-08 15:43 UTC)

<p>I got same error above using nightly build (just downloaded it) . Elastix works in Slicer but does not work from the terminal. It would be nice if it runs from the terminal even using Slicer --launch option.</p>

---

## Post #4 by @brhoom (2018-12-08 18:30 UTC)

<p>I did more testing, here is the result</p>
<p>Using nightly build:</p>
<ul>
<li>I can run elastix in the python interactor, I guess it should work also in the plugin.</li>
<li>I can not run elastix in Ubuntu terminal but I think this should not be a problem as the above work.</li>
</ul>
<p>Using 4.10:</p>
<ul>
<li>I can not run elastix in Ubuntu terminal</li>
<li>In Slicer, the plugin itself is not stable, sometimes the testing works and sometimes not.</li>
</ul>

---

## Post #5 by @brhoom (2018-12-08 18:44 UTC)

<p>I did more testing. SlicerElastix does not work after I run SliacerCochlea. If I restart Slicer and run SlicerElastix, it works.</p>
<p>What could be the problem in SlicerCochlea code???</p>

---

## Post #6 by @brhoom (2018-12-08 18:47 UTC)

<p>Problem solved! I disabled these lines</p>
<pre><code>#os.environ['LD_LIBRARY_PATH'] = self.vissimPath + "/sw/elastix-4.9.0/lib"
#os.environ['LD_LIBRARY_PATH'] = self.vissimPath + "/sw/elastix-4.9.0/lib"
</code></pre>
<p>Everything works now in Slicer. Only the terminal problem to be solved.</p>

---

## Post #7 by @brhoom (2018-12-08 18:52 UTC)

<p>Since some plugins affect other plugins negatively, something should be done to avoid this as this makes it difficult to find the source of the problem if it is from another extension.</p>

---

## Post #8 by @lassoan (2018-12-08 19:07 UTC)

<p>I don’t think there are any issues or limitations here, you just need to clearly distinguish between binaries built by Slicer factory machines (and included in extensions); and third-party binaries present on the system. Third-party binaries can be included in extensions, but this should be avoided.</p>
<p><strong>Running executables bundled in a Slicer extension:</strong></p>
<p>There is no interference between extensions if you let Slicer factory build all libraries (you must not bundle binaries created elsewhere). If there are libraries or executable used by multiple extensions (for example Elastix is used by several extensions) then you need to make sure that one extension builds the shared library and all other extensions depend on that. See how <a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/df60af069abb19397f8036c8d2d6d9c1816d8152/SequenceRegistration/SequenceRegistration.py#L557-L562" rel="nofollow noopener">SequenceRegistration extension uses SlicerElastix</a> for an example.</p>
<p>In the very rare case that different extensions use must incompatible versions of the same libraries, you can statically link the old version of the library to the extension that requires the old library version. We have 100+ extensions and I think this happened only once.</p>
<p><strong>Running third-party executables or scripts installed on the system (not bundled with Slicer):</strong></p>
<p>If you want to start third-party programs (executables, Python scripts, etc.) from Slicer, then you usually need to use startup environment as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_run_Python_script_using_a_non-Slicer_Python_environment" rel="nofollow noopener">here</a>.</p>

---

## Post #9 by @brhoom (2018-12-08 19:22 UTC)

<p>Thanks for the detailed info. I don’t understand the last part. Could you please provide an example of how to run the elastix binary in the terminal (not in python).</p>

---

## Post #10 by @thewtex (2018-12-08 20:01 UTC)

<p>Binaries to run elastix in the terminal can be <a href="https://github.com/SuperElastix/elastix/releases" rel="nofollow noopener">downloaded from the elastix GitHub release page</a>.</p>

---

## Post #11 by @lassoan (2018-12-08 20:15 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="9" data-topic="5017">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>run the elastix binary in the terminal (not in python)</p>
</blockquote>
</aside>
<p>Would you run it manually by typing commands on the terminal? Or using a bash script? Don’t you want to use it from your Python scripted module?</p>
<p>Anyway, you can use third-party libraries on your system as <a class="mention" href="/u/thewtex">@thewtex</a> suggested above (completely independently from Slicer), or run any Slicer executables using the launcher, for example:</p>
<pre><code>"c:\Program Files\Slicer 4.10.0\Slicer.exe" --launch c:\Users\andra\AppData\Roaming\NA-MIC\Extensions-27501\SlicerElastix\lib\Slicer-4.10\elastix.exe --help &gt;&gt;output.txt
</code></pre>

---

## Post #12 by @brhoom (2018-12-08 23:39 UTC)

<blockquote>
<p>Binaries to run elastix in the terminal can be</p>
</blockquote>
<p>I needed the one from Slicer to debug my module.</p>
<blockquote>
<p>or run any Slicer executables using the launcher<br>
Slicer --launch executable</p>
</blockquote>
<p>That is exactly what I needed, thanks a lot.</p>

---
