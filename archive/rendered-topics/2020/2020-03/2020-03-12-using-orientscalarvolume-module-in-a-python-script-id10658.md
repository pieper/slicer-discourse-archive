---
topic_id: 10658
title: "Using Orientscalarvolume Module In A Python Script"
date: 2020-03-12
url: https://discourse.slicer.org/t/10658
---

# Using OrientScalarVolume module in a python script

**Topic ID**: 10658
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/using-orientscalarvolume-module-in-a-python-script/10658

---

## Post #1 by @Alex_Vergara (2020-03-12 12:47 UTC)

<p>Dear all<br>
Is there a way to avoid console calls in OrientScalarVolume such as</p>
<pre><code class="lang-auto">OrientImage
   --orientation Axial 
   ${MRML_DATA}/fixed.nrrd 
   ${TEMP}/OrientImageTestAxial.nrrd
</code></pre>
<p>as defined in the <a href="https://www.slicer.org/wiki/Documentation/4.0/Modules/OrientScalarVolume" rel="nofollow noopener">documentation</a>?</p>
<p>I want to use some kind of logic from it to generate a temporary node to be exported in the preferred coordinate system (in a python function). I know I can create a temporary directory, save the file there, execute the command line and copy the new file to the desired location, but thats awful. I would like more the “logic” way, generating a temporary node and save only one time.</p>
<p>My current script saves the nodes in RAS orientation, I like them in RAI which is the orientation <a href="http://opengatecollaboration.org/" rel="nofollow noopener">Gate</a> is expecting to perform the simulations.</p>

---

## Post #2 by @Alex_Vergara (2020-03-12 13:07 UTC)

<p>Ok I found the solution<br>
The OrientScalarVolume is a cli module, so the way is</p>
<pre><code class="lang-auto">def reorientNode(node, orientation):
    parameters = {'inputVolume1':node, 'outputVolume':node, 'orientation':orientation}
    slicer.cli.run(slicer.modules.orientscalarvolume, None, parameters, True)
</code></pre>
<p>This was pure luck as none of these parameters are documented. Just in case anyone need this.</p>

---

## Post #3 by @lassoan (2020-03-12 13:47 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="2" data-topic="10658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>This was pure luck as none of these parameters are documented</p>
</blockquote>
</aside>
<p>Documentation is the XML file. You can also find a convenience script <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">here</a> that lists all parameter names.</p>

---

## Post #4 by @Alex_Vergara (2020-03-12 13:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="10658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Documentation is the XML file.</p>
</blockquote>
</aside>
<p>This <a href="https://github.com/Slicer/SlicerGitSVNArchive/blob/master/Modules/CLI/OrientScalarVolume/OrientScalarVolume.xml" rel="noopener nofollow ugc">XML file</a>? So I assume for all cli modules is the same, right? OK that is a better way than try and test <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"> Thanks for the hint!</p>

---

## Post #5 by @lassoan (2020-03-12 14:08 UTC)

<p>Yes, that’s the XML file. Command-line arguments and GUI is documented in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/OrientScalarVolume">Slicer wiki</a>, too, but the parameter names are only described in the XML file (or you can list them using the script linked above).</p>

---

## Post #6 by @lassoan (2021-10-07 05:55 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-get-parameters-of-segment-editor-effects/20046">How to get parameters of Segment Editor effects</a></p>

---
