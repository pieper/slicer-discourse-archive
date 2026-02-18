# SlicerEditor improvement inquiry

**Topic ID**: 37244
**Date**: 2024-07-07
**URL**: https://discourse.slicer.org/t/slicereditor-improvement-inquiry/37244

---

## Post #1 by @muratmaga (2024-07-07 20:54 UTC)

<p>Following from the last PW, there is now a functional prototype of SlicerEditor based on open-source monaco editor. If you would like to give it a try, please use the “working” branch from:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerEditor/tree/working">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerEditor/tree/working" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerEditor/tree/working" target="_blank" rel="noopener">GitHub - SlicerMorph/SlicerEditor at working</a></h3>

  <p><a href="https://github.com/SlicerMorph/SlicerEditor/tree/working" target="_blank" rel="noopener">working</a></p>

  <p><span class="label1">a simple programming editor for Slicer based on monaco</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1a2ef51f60ca327b8d2ecd488abcd1e882e60f2.jpeg" data-download-href="/uploads/short-url/n3TXsxech06JctlzFnL0L5Nh7Wy.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1a2ef51f60ca327b8d2ecd488abcd1e882e60f2_2_669x500.jpeg" alt="image" data-base62-sha1="n3TXsxech06JctlzFnL0L5Nh7Wy" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1a2ef51f60ca327b8d2ecd488abcd1e882e60f2_2_669x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1a2ef51f60ca327b8d2ecd488abcd1e882e60f2_2_1003x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1a2ef51f60ca327b8d2ecd488abcd1e882e60f2.jpeg 2x" data-dominant-color="3D3B3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1189×888 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can use the provided code example, highlight and hit run to execute in the python console.</p>
<p>Currently the plan is write these files directly to disk, using a node selector/creator. However, I would like the scene to be aware of these files, and if possible become part of the scene tree (like the Texts node) and the I/O is handled like any other object in the scene tree through the regular save or export as options.</p>
<p>How can we achieve this? should we create a MRML object type called Scripts (similar to Text object)? Can we do this  through as an extension, or does it require changes to the core?</p>
<p>What would be the alternative to accomplish scene integration?</p>

---

## Post #2 by @pieper (2024-07-07 21:18 UTC)

<p>For reference:</p>
<p><a href="https://discourse.slicer.org/t/support-python-text-highlighting-in-text-module/34511">https://discourse.slicer.org/t/support-python-text-highlighting-in-text-module/34511</a></p>
<p>and</p>
<p><a href="https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SimpleEditorForPythonScripting/">https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SimpleEditorForPythonScripting/</a></p>
<p>Regarding integration with the scene, I suggest we start just by using Text nodes, since those are already exist.  I could make sense to have a subclass that does some “scripty” things, but I don’t think that’s needed now.  We could have a node attribute that flags script nodes as a kind of text node to be handled specially, e.g. to always save in a file rather than in the xml.</p>
<p>But I’m still not convinced that mixing code and data is a good architecture.  Usually we try to have scripts that are generic and can be applied to any data rather than having data-specific scripts.  Perhaps for demos or training though having everything in the scene can make sense so I suggest we play with it and maybe add more features before deciding about any changes to the core.</p>
<p>Also can we put this in the extension manager now so it’s easier for people to discover and try?</p>

---

## Post #3 by @pieper (2024-07-07 21:23 UTC)

<p>(Also, with the Text node the text data can already be in a dedicated file that’s pointed to by the mrml xml, so if we just make sure to set them up that way from the SlicerEditor code then we’ll get what I believe is the behavior you are looking for.)</p>

---

## Post #4 by @muratmaga (2024-07-07 21:38 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I suggest we start just by using Text nodes, since those are already exist.</p>
</blockquote>
</aside>
<p>Wouldn’t this conflict with the regular Texts module? Would be possible to distinguish nodes bearing python scripts vs regular text? I am concerned it will clash and the right-click “Edit Properties” would open the python script in the Texts module as opposed to SlicerEditor.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Usually we try to have scripts that are generic and can be applied to any data rather than having data-specific scripts.</p>
</blockquote>
</aside>
<p>I think that’s the function of the script repository, ie., to provide generic examples that applies to large number of people. Here I think the intention is exactly what you desribed, a script specific to the data the user is processing. I think for the reproducibility and retention it is important to keep these things together. But I suspect, you are right we have to experiemnt some…</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Also can we put this in the extension manager now so it’s easier for people to discover and try?</p>
</blockquote>
</aside>
<p>Once few remaining things are sorted out, yes, that’s the intention.</p>

---

## Post #5 by @pieper (2024-07-08 14:08 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Would be possible to distinguish nodes bearing python scripts vs regular text?</p>
</blockquote>
</aside>
<p>Yes, these are doable with the existing infrastructure.  The qMRMLNodeComboBox can be configured to only show nodes with specific attributes, so if we used that to mark text nodes as scripts then only those would be selectable in the editor.  Similarly  we could have a subject hierarchy plugin that checks the node attribute and offers an ‘edit as script’ menu option.</p>
<p>The more I think about it, I do like the idea of capturing the script as a way of documenting what was done in processing the data in the scene.  Usually that information is ephemeral or lost in the log files.  Let’s see how it works out in a few specific cases.</p>

---

## Post #6 by @oothomas (2024-07-08 17:31 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>qMRMLNodeComboBox can be configured to only show nodes with specific attributes</p>
</blockquote>
</aside>
<p>Right now only vtkMRMLTextNode are displayed when you try to import a node from the scene, I’m guessing with qMRMLNodeComboBox only nodes with a python attribute would be displayed? That would be really nice. How do you create a subject hierarchy plugin?</p>

---

## Post #7 by @pieper (2024-07-08 18:12 UTC)

<p>You could provide a scripted file reader, something like <a href="https://github.com/Slicer/Slicer/blob/b05d25b1920bbf46e37ef45672630a7be6af28fc/Modules/Scripted/ImportItkSnapLabel/ImportItkSnapLabel.py#L14">this one</a> that registers the <code>.py</code> extension and loads it into a text node and then uses the <a href="https://github.com/Slicer/Slicer/blob/b05d25b1920bbf46e37ef45672630a7be6af28fc/Libs/MRML/Core/vtkMRMLNode.cxx#L789">SetAttribute</a> method to set <code>TextType</code> to be <code>PythonScript</code>.</p>
<p>Then in the Editor combo box you can use <a href="https://github.com/Slicer/Slicer/blob/b05d25b1920bbf46e37ef45672630a7be6af28fc/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L134-L146">addAttribute</a> to filter the nodes that appear.</p>
<p>Then it’s also possible to put in a subject hierarchy plugin that checks the <code>FileType</code> attribute and adds an option to use the SlicerEditor module.  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy-plugin-offering-view-context-menu-action">This documentation</a> should help, and you can see how it’s used in practice <a href="https://github.com/Slicer/Slicer/blob/b05d25b1920bbf46e37ef45672630a7be6af28fc/Modules/Scripted/SegmentStatistics/SubjectHierarchyPlugins/SegmentStatisticsSubjectHierarchyPlugin.py#L11">here</a>.</p>

---

## Post #8 by @muratmaga (2024-07-08 20:15 UTC)

<p>I actually want a slightly different behavior. I want the script object behave more like Volumes node. I.e., scene is aware of it, but data is written to / read from a file, instead of the scene.</p>
<p>So for script object, the Text node can keep its attributes (like it is modified etc), but the actual script is written to file.</p>

---

## Post #9 by @pieper (2024-07-08 20:19 UTC)

<p>Yes, you can do it with this parameter, which can be set in the custom reader for the scripts:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLTextNode.h#L69-L75">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLTextNode.h#L69-L75" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLTextNode.h#L69-L75" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLTextNode.h#L69-L75</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="69" style="counter-reset: li-counter 68 ;">
          <li>/// Force the use of a storage node, regardless of text length.</li>
          <li>/// By default, a storage node will only be used for nodes that have been read from file (drag and drop),</li>
          <li>/// or for nodes that have text longer than 250 characters.</li>
          <li>/// This option should be also be enabled for nodes with highly structured text (such as XML) that would</li>
          <li>/// not be good to have in the MRML.</li>
          <li>vtkSetClampMacro(ForceCreateStorageNode, int, CreateStorageNodeAuto, CreateStorageNodeNever);</li>
          <li>vtkGetMacro(ForceCreateStorageNode, int);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @oothomas (2024-07-17 15:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1b51371fedfd20ee07f63423be291e9e12e4727.jpeg" data-download-href="/uploads/short-url/pm4sSeh7vTQ4JATybM4h75Yxt5B.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1b51371fedfd20ee07f63423be291e9e12e4727_2_690x273.jpeg" alt="image" data-base62-sha1="pm4sSeh7vTQ4JATybM4h75Yxt5B" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1b51371fedfd20ee07f63423be291e9e12e4727_2_690x273.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1b51371fedfd20ee07f63423be291e9e12e4727_2_1035x409.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1b51371fedfd20ee07f63423be291e9e12e4727_2_1380x546.jpeg 2x" data-dominant-color="E6E5E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1400×554 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi everyone,</p>
<p>I wanted to share some progress and seek advice on a couple of issues I’m encountering with the SlicerEditor module.</p>
<p><strong>Current Progress:</strong></p>
<ol>
<li><strong>Subject Hierarchy Plugin</strong>: I’ve added a subject hierarchy plugin. When such a node is right-clicked, a new menu option for saving <code>.py</code> files is now available. This will be updated to override the existing “Export to file…” option, allowing <code>.py</code> files to be saved directly.</li>
<li><strong>Mime Type Attribute</strong>: I successfully added the <code>mimetype</code> attribute to <code>vtkMRMLText</code> nodes from <code>.py</code> files dropped into the Slicer window for import.</li>
<li><strong>PyFile Reader/Writer Module</strong>: I’ve added a module that reads and writes .py files to disk</li>
</ol>
<p><strong>Issues Encountered:</strong></p>
<ol>
<li><strong>Recording Executed Code</strong>: One of the core functions of the SlicerEditor module is currently lacking—the ability to record the code executed when the run button is clicked. Is there a way to programmatically “paste” the code from the editor into the interactor within the module? Or is there an alternative method to run the code that would allow users to use the up button (at the interactor) to see what has already been executed?</li>
<li><strong>Attribute Extraction for Imported .py Files</strong>: The <code>canOwnSubjectHierarchyItem</code> method isn’t extracting the set attributes of the imported <code>.py</code> file as expected. I’m trying to use this to override the default text node icon, but the attributes return <code>None</code>.</li>
</ol>
<p>Here’s a snippet of the relevant code:</p>
<pre><code class="lang-auto">def canOwnSubjectHierarchyItem(self, itemID):
    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    shNode = pluginHandlerSingleton.subjectHierarchyNode()
    node = shNode.GetItemDataNode(itemID)

    if node:
        print("Node found:", node.GetName())
        mimetype = node.GetAttribute("mimetype")
        fileType = node.GetAttribute("fileType")
        print("Node mimetype:", mimetype, "fileType:", fileType)
        if mimetype == "text/x-python" or fileType == "python":
            return 1.0
    else:
        print("No node found for itemID:", itemID)
    return 0.0

def icon(self, itemID):
    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    shNode = pluginHandlerSingleton.subjectHierarchyNode()
    node = shNode.GetItemDataNode(itemID)

    if node and (node.GetAttribute("mimetype") == "text/x-python" or node.GetAttribute("fileType") == "python"):
        return self.fileIcon

    # Check the file extension of the storage node
    storageNodeID = node.GetStorageNodeID()
    if storageNodeID:
        storageNode = slicer.mrmlScene.GetNodeByID(storageNodeID)
        if storageNode and storageNode.GetFileName().lower().endswith('.py'):
            return self.fileIcon

    return qt.QIcon()

</code></pre>
<p>To recreate this issue, you can install the <code>working version-2</code> branch of the SlicerEditor and drag and drop a <code>.py</code> file with some code into the Slicer data window to import the file.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/oothomas/SlicerEditor/tree/version-2">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/oothomas/SlicerEditor/tree/version-2" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/oothomas/SlicerEditor/tree/version-2" target="_blank" rel="noopener nofollow ugc">GitHub - oothomas/SlicerEditor at version-2</a></h3>

  <p><a href="https://github.com/oothomas/SlicerEditor/tree/version-2" target="_blank" rel="noopener nofollow ugc">version-2</a></p>

  <p><span class="label1">a simple programming editor for Slicer based on monaco</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I appreciate all the help so far and look forward to further developing this module with your assistance!</p>
<p>Best regards,<br>
Oshane</p>

---

## Post #11 by @muratmaga (2024-07-17 16:22 UTC)

<aside class="quote no-group" data-username="oothomas" data-post="10" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oothomas/48/68743_2.png" class="avatar"> oothomas:</div>
<blockquote>
<p>is currently lacking—the ability to record the code executed when the run button is clicked. Is there a way to programmatically “paste” the code from the editor into the interactor within the module?</p>
</blockquote>
</aside>
<p>Yeah, that’s a quite significant problem. While the code do get executed, and created python objects are accessible in the python console, not seeing the lines of code run, or history of them (with up arrow) is very confusing.</p>
<p>Given that you can paste code into Python console from outside, I thought maybe it is possible to do exactly that, stream the highlighted code as if it is copy/pasted? <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>I think this is the only remaining significant obstacle before we add it to the extension catalogue for people to try…</p>

---

## Post #12 by @lassoan (2024-07-17 19:03 UTC)

<aside class="quote no-group" data-username="oothomas" data-post="10" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oothomas/48/68743_2.png" class="avatar"> oothomas:</div>
<blockquote>
<p>is currently lacking—the ability to record the code executed when the run button is clicked</p>
</blockquote>
</aside>
<p>You can print anything to the console using <code>print...</code> methods, for example: <code>slicer.app.pythonConsole().printOutputMessage("something")</code></p>
<p>But maybe what we miss is that when multiple lines of code is copy-pasted then that does not get added to the command history (you cannot re-run by up-arrow and Enter). I think these multiline commands are not added to the history because there are some limitations in the console about running multi-line code and returning a value (the Python interpreter can either run single command and return a value that can be displayed; or run multiline commands but not return a value). You can see this limitation if you type multiple lines of code (using Shift+Enter to start a new line without executing the code) and only the first line of the code will be executed. It should be possible to improve the behavior and automatically switch to multiline execution. We could then keep very long code snippets in the command history.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>But I’m still not convinced that mixing code and data is a good architecture.</p>
</blockquote>
</aside>
<p>I agree, it may not be the best idea.</p>
<p>There is code, data, and documentation; and indded it is somewhat inconvenient to deal with all three separately. But instead of bundling data with code, I would rather bundle code with documentation (as they are much more similar) and make it very easy to run code snippets from documentation. For example, we could use custom URL protocol to run a code snippet that is shown in a tutorial document in the browser, by a single click.</p>
<p>But Jupyter does exactly this (bundling code and documentation), so it is not clear for me why we do not just use notebooks.</p>
<p>There is also VS Code. Step-by-step debugging is really useful. For that, you need to have your code in a .py file that is opened in VS Code. The only inconvenience there that you need to run the code by calling <a href="https://stackoverflow.com/a/41658338"><code>execfile('path/to/myscript.py')</code></a> in the debug console in VS Code instead of just pressing F5. But this can be addressed by adding a small custom VS Code extension (that registers a new command, which executes the currently edited file in the debug console).</p>

---

## Post #13 by @muratmaga (2024-07-17 19:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>But Jupyter does exactly this (bundling code and documentation), so it is not clear for me why we do not just use notebooks.</p>
</blockquote>
</aside>
<p>I agree, Jupyter notebooks are great. If people are comfortable with it, and know how to set it up correctly, they should use it. Nor, this editor is meant to be a replacement for IDEs.</p>
<p>The editor is there for recording things that cannot be recorded in Slicer easily. The typical example is a custom segmentation pipeline that involves thresholding and smoothing, parameters of which is get lost if all you save the data. You can of course do this through the  Jupyter notebooks, but the format is too verbose making it harder to find it by opening the notebook in a text editor.</p>
<p>So this is just another way of doing things, it is not so uncommon in Slicer to have tools with overlapping functionalities. So I am not sure why this has to be either/or situation.</p>

---

## Post #14 by @lassoan (2024-07-17 20:48 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>The editor is there for recording things that cannot be recorded in Slicer easily</p>
</blockquote>
</aside>
<p>OK, this may be important.</p>
<p>Would you like kind of “macro” functionality? To be able to easily specify (preferably record) a few processing steps and able to rerun it on various data?</p>
<p>Would users want to save their macros? Share macros with others? Then it really sounds like we would need to make it simpler to create, edit, run, and debug scripted modules and extensions.</p>
<p>We could also create a simple, Pythonic “SlicerMacros” library, which would allow using Slicer in a macro-like language without requiring anyone to know anything about Slicer, MRML, VTK, Qt, etc. SlicerMacros could be in an extension so that it could be continuously updated based on user requests. For example, the “macro” functions could work like this:</p>
<pre><code class="lang-auto">import SlicerMacros as sm
vol = sm.load_volume('path/to/volume.nrrd')
seg = sm.create_segmentation(vol)
seg1 = sm.create_segment(seg, "test")
sm.segment_threshold(seg1, vol, 200, 323)
sm.segment_smooth(seg1, 'joint', 0.3)
sm.save_segmentation(seg, 'path/to/segmentation.seg.nrrd')
</code></pre>

---

## Post #15 by @muratmaga (2024-07-17 21:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would you like kind of “macro” functionality? To be able to easily specify (preferably record) a few processing steps and able to rerun it on various data?</p>
</blockquote>
</aside>
<p>Yes, definitely! Once we have figured out the nuts and bolts of the editor, I was thinking on going a direction where people can import generic scripts for various tasks and customize if for their data. This sound very similar (if not better than that).</p>
<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could also create a simple, Pythonic “SlicerMacros” library,</p>
</blockquote>
</aside>
<p>This sounds very useful. But are you thinking of this as a package like slicerio which can be used without slicer. Or will this code  be executed inside the Slicer?</p>
<p>We do try to teach little bit of Python programming in our workshops, and an example like above will motivate people a lot more. The whole interacting with MRML/Qt objects business adds a significant complexity to even the simplest tasks, so abstraction like this would be great</p>

---

## Post #16 by @oothomas (2024-07-17 21:25 UTC)

<p>I’ve solved the issue with the icon, but I’m still having some trouble using the “Edit Properties” option when a python text node is clicked. The SlicerEditor opens, but the code does not appear in the editor. This only occurs if the SlicerEditor module has not been called i.e. after startup before the module is loaded. Here’s my code for edit properties where I’ve been trying to a few things to solve the problem:</p>
<pre><code class="lang-auto">    def editNodeInSlicerEditor(self, node):
        pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
        pluginHandlerSingleton.pluginByName("Default").switchToModule("SlicerEditor")

        # Allow some time for the module to fully load
        slicer.app.processEvents()
        time.sleep(0.5)  # Adjust the sleep time if necessary

        editorWidget = slicer.modules.slicereditor.widgetRepresentation().self()
        code = node.GetText().replace('\\', '\\\\').replace('`', '\\`').replace('"',
                                                                                '\\"')  # Escape backslashes, backticks, and double quotes

        # Define the JavaScript code as a string
        jsSetEditorContent = f"""
            function setEditorContent() {{
                if (window.editor) {{
                    window.editor.getModel().setValue(`{code}`);
                }} else {{
                    setTimeout(setEditorContent, 500);
                }}
            }}
            setEditorContent();
        """

        # Use evalJS to execute the JavaScript function
        editorWidget.editorView.evalJS(jsSetEditorContent)

    def editProperties(self, itemID):
        print("Edit Properties action triggered")
        node = self.subjectHierarchyNode.GetItemDataNode(itemID)
        if node:
            self.editNodeInSlicerEditor(node)
</code></pre>
<p>This runs perfectly fine if the module has already been selected manually and the user tries to “Edit Properties” of the python text node after.</p>
<p>I’ve updated the version-2 branch of the repo:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerEditor/tree/version-2">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerEditor/tree/version-2" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerEditor/tree/version-2" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerEditor at version-2</a></h3>

  <p><a href="https://github.com/SlicerMorph/SlicerEditor/tree/version-2" target="_blank" rel="noopener nofollow ugc">version-2</a></p>

  <p><span class="label1">a simple programming editor for Slicer based on monaco</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Simply install and drag and drop a python file from disk to slicer to test.</p>
<p>Oshane</p>
<p>**is this because we are using a slicer.qSlicerWebWidget() ?</p>

---

## Post #17 by @oothomas (2024-07-17 22:16 UTC)

<p>Nevermind…problem solved. I had to properly give the slicer.qSlicerWebWidget() and JS enough time to load:</p>
<pre><code class="lang-auto">    def editNodeInSlicerEditor(self, node):
        editorModule = slicer.modules.slicereditor
        slicer.util.selectModule(editorModule.name)

        editorWidget = slicer.modules.slicereditor.widgetRepresentation().self()
        code = node.GetText().replace('\\', '\\\\').replace('`', '\\`').replace('"',
                                                                                '\\"')  # Escape backslashes, backticks, and double quotes

        def setEditorContent():
            jsSetEditorContent = f"""
                (function setEditorContent() {{
                    if (window.editor &amp;&amp; window.editor.getModel()) {{
                        window.editor.getModel().setValue(`{code}`);
                    }} else {{
                        setTimeout(setEditorContent, 100);
                    }}
                }})();
            """
            editorWidget.editorView.evalJS(jsSetEditorContent)

        # Adding a slight delay to ensure the editor is initialized
        qt.QTimer.singleShot(500, setEditorContent)

    def editProperties(self, itemID):
        print("Edit Properties action triggered")
        node = self.subjectHierarchyNode.GetItemDataNode(itemID)
        if node:
            self.editNodeInSlicerEditor(node)
</code></pre>

---

## Post #18 by @pieper (2024-07-18 09:03 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="15" data-topic="37244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>import generic scripts for various tasks and customize if for their data</p>
</blockquote>
</aside>
<p>Yes, I think it would be great to be able to download and use (and share) handy scripts.  It would also be nice if we could integrate it with the UI a bit.  I.e. in the script repository we have some examples with hard-coded node names and text telling people to replace the string (a common source of confusion it seems).  Instead maybe <code>slicer.util.getNode</code> could prompt to select a node when run from the editor or console and doesn’t recognize the input string.</p>

---
