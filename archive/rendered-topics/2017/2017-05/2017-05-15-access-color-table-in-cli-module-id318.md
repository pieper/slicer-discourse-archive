---
topic_id: 318
title: "Access Color Table In Cli Module"
date: 2017-05-15
url: https://discourse.slicer.org/t/318
---

# Access color table in CLI module

**Topic ID**: 318
**Date**: 2017-05-15
**URL**: https://discourse.slicer.org/t/access-color-table-in-cli-module/318

---

## Post #1 by @mirclem (2017-05-15 21:56 UTC)

<p>One more question…</p>
<p>I noticed that the colormaps have an attribute “reference” in the tag “table” but I couldn’t find a way to access it.</p>
<blockquote>
<pre><code>&lt;table hidden="true" type="color" reference="InputVolume"&gt;
  &lt;name&gt;ColorTable&lt;/name&gt;
  &lt;channel&gt;input&lt;/channel&gt;
  &lt;longflag&gt;color&lt;/longflag&gt;
  &lt;description&gt;&lt;![CDATA[Color table to make labels to colors and objects]]&gt;&lt;/description&gt;
&lt;/table&gt;
</code></pre>
</blockquote>
<p>I thought we could use the same method than for the other attributes like the <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/CLI/vtkMRMLCommandLineModuleNode.cxx#L974" rel="noopener nofollow ugc">file extension</a>. But there is no GetParameterReference(int, int) function and the vtkMRMLCommandLineModuleNode.GetModuleDescription() is not available for python. The only thing I found is vtkMRMLCommandLineModuleNode.GetModuleDescriptionAsString() but it needs a way to structure the string to be parsed.</p>
<p>Any thoughts?</p>

---

## Post #2 by @lassoan (2017-05-15 23:54 UTC)

<p>Colormap is an input to the CLI module. It is used for passing colormap with labelmap volumes. This allows the CLI to get label name corresponding to a voxel value.</p>

---

## Post #3 by @mirclem (2017-05-16 13:15 UTC)

<p>Hi Andras, my question was more about how to get the labelmap node relative to a colormap given in a CLI command. I know it is possible in C++ but I could not find a way to do it in python.</p>

---

## Post #4 by @lassoan (2017-05-16 13:36 UTC)

<p>CLI infrastructure sets the labelmap node automatically from the colormap node that you set in the display node of the volume node (volumeNode-&gt;GetDisplayNode()-&gt;SetAndObserveColorNodeID(…)).</p>

---

## Post #5 by @mirclem (2017-05-16 14:05 UTC)

<p>Actually, this is why this post was in the previous post, because there is a context behind that. I am not trying to run the CLI from the regular CLI infrastructure but I am trying to create the command, send it to a database and run it remotely.</p>
<p>I was able to access the colormap knowing the labelmap node:<br>
<code>saveNode(getNode('MyLabelMap').GetDisplayNode().GetColorNode(), "myPath.txt")</code></p>
<p>But, in the <a href="https://discourse.slicer.org/t/access-color-table-in-cli-module/318?u=mirclem">example of Model Maker</a>, there is a <code>reference</code> attribute in the xml file. This attribute says which LabelMapNode looking for to get the colormap. And I can’t access the <code>reference</code> attribute.</p>

---

## Post #6 by @lassoan (2017-05-16 14:15 UTC)

<p>In the CLI you don’t get the reference attribute value, as MRML node IDs only make sense in a specific scene. Instead, you get the filename of the saved colormap node that is associated with the volume defined by reference attribute.</p>

---

## Post #7 by @mirclem (2017-05-16 15:44 UTC)

<p>I noticed two different behaviors:</p>
<ul>
<li>If you parse the CLI parameters without having run the CLI before, the colormap parameter has an empty value.</li>
<li>If you run the CLI and then try to parse the parameters, the colormap parameter has, as you said, the filename of the save colormap. (Which is enough for what I want)</li>
</ul>
<p>I don’t really want to have to previously run the CLI and then generate a right command.</p>

---

## Post #8 by @lassoan (2017-05-16 17:28 UTC)

<p>CLI node is for running CLIs. If you don’t want to run a CLI then you can get the information directly from the nodes in the scene.</p>
<p>If you need a better solution then please describe what exactly you would like to achieve as an end result, and then we can help better in figuring out how to get there.</p>

---

## Post #9 by @lassoan (2017-05-16 18:15 UTC)

<p>2 posts were split to a new topic: <a href="/t/running-cli-modules-on-a-remote-server/328">Running CLI modules on a remote server</a></p>

---
