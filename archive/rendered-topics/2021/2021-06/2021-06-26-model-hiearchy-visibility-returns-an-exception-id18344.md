# Model hiearchy visibility returns an exception

**Topic ID**: 18344
**Date**: 2021-06-26
**URL**: https://discourse.slicer.org/t/model-hiearchy-visibility-returns-an-exception/18344

---

## Post #1 by @Amine (2021-06-26 02:45 UTC)

<p>HI, I made a script to find out which models are visible both individually and in the hiearchy ( hidden hierarchy is independent of individual model visibility so both have to be True for the model to be effectively visible on the 3d viewer).</p>
<p>here is the script:</p>
<pre><code class="lang-auto">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
sceneItemID = shNode.GetSceneItemID()
sceneitem_node = shNode.GetItemDataNode(sceneItemID)
for modelnode in slicer.util.getNodesByClass("vtkMRMLModelNode"):
    try:
        print("===========")
        print("model name: ", modelnode.GetName())
        print("model visibility: ", bool(modelnode.GetDisplayVisibility()))
        print("hiearchy visiblity: ", sceneitem_node.GetHierarchyVisibility(modelnode))
    except Exception as ex:
        print(ex)
</code></pre>
<p>My problem is that <code>sceneitem_node.GetHierarchyVisibility(modelnode)</code> returns an exception <code>'NoneType' object has no attribute 'GetHierarchyVisibility'</code> , the workaround is simply to drag and drop one of the models on the parent folder, the script does work fine then (for all models).</p>
<p>Reproducing this issue is consistent, i simply made segments and exported them to models, then entered that script, both on slicer 4.11 2019 and the last 2021 nightly.</p>
<p>PS: as an alternative, any other consistent way to find out if the model is visible on 3d (covering both individual visibility and hiearchy) would be welcome, thank you!</p>

---

## Post #2 by @Amine (2021-06-26 05:22 UTC)

<p>Update: I have been able to bypass that function by iterating through parent folders until one is not visible using <code> shNode.GetItemParent()</code>  and <code>shNode.GetItemDisplayVisibility()</code>, this does exactly what i expected from <code>GetHierarchyVisibility()</code></p>

---

## Post #3 by @cpinter (2021-06-28 14:27 UTC)

<p>For context, <code>sceneitem_node</code> is <code>None</code>, as there is no data node for the scene. It is always a good idea to check the output of each line of your Python script because then it will be obvious what each variable contains.</p>

---

## Post #4 by @Amine (2021-06-29 22:49 UTC)

<p>i see thanks, but why would it return None with an existing scene full of models but will return the correct data when a model is drag-dropped on a folder (hierarchy change I guess)  (this issue also happens after a scene is saved and re-opened)</p>

---

## Post #5 by @lassoan (2021-06-30 01:22 UTC)

<p><code>sceneitem_node = shNode.GetItemDataNode(sceneItemID)</code> is expected to set <code>sceneitem_node</code> to <code>None</code>, because the scene item is not associated with any data node.</p>
<p>In <a href="https://apidocs.slicer.org/master/classvtkMRMLFolderDisplayNode.html#a947a6549ec5be1e3f705bc9b76145a81">vtkMRMLFolderDisplayNode documentation</a> you can see that it is a static method, therefore the correct way to call it is this:</p>
<pre><code class="lang-python">slicer.vtkMRMLFolderDisplayNode.GetHierarchyVisibility(modelNode)
</code></pre>
<p>See how to use doxygen-generated documentation for Python in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#doxygen-style-documentation">developer manual</a>.</p>

---

## Post #6 by @Amine (2021-07-08 23:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>slicer.vtkMRMLFolderDisplayNode.GetHierarchyVisibility(modelNode)</code></p>
</blockquote>
</aside>
<p>This works great, thank you.</p>
<p>I’m a bit used to reading slicer documentation but sometimes finding the correct syntax to use can be tricky</p>

---

## Post #7 by @lassoan (2021-07-09 00:11 UTC)

<p>Happy to hear that it works. Let us know if you have any suggestions for improving the documentation.</p>

---

## Post #8 by @Amine (2021-07-09 02:51 UTC)

<p>There is a section in slicer’s documentation that has a lot of code examples for basic operations, that was the most helpful reference in the beginning.</p>
<p>I later started to use slicer’s github to search for implementation examples of classes or parameters if they didn’t work as intended, it would be nice if more modules were available to browse in python as opposed to c++ (in github)</p>
<p>Full slicer modules in python contain a lot of building blocks for various operations that were not featured in slicer’s documentation examples and were by far the most helpful ressource for module building (for example the first three lines in my code example are very hard if not impossible to find out from the generated documentation, i would look into the code of a module that uses folder hiearchy to find out how it’s done)</p>
<p>The doxygen generated documentation only provides the names of methods for each class or what type of argument is required for methods but finding out the sequence of code lines to actually obtain those arguments would require browsing into some related module’s code (especially when the arguments are “multi layered” to obtain like sceneItemID in my example)</p>

---

## Post #9 by @lassoan (2021-07-09 04:01 UTC)

<p>Thank you for taking the time to give feedback. It helps us a lot, because most documentation is written by experienced Slicer developers and for them it is not obvious what information a new developer may miss. It would be great if you could provide a bit more details by answering the questions below.</p>
<aside class="quote no-group" data-username="Amine" data-post="8" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>it would be nice if more modules were available to browse in python as opposed to c++ (in github)</p>
</blockquote>
</aside>
<p>There is a topic in github that makes it easy to find all the Slicer extensions: <a href="https://github.com/topics/3d-slicer-extension" class="inline-onebox">3d-slicer-extension · GitHub Topics · GitHub</a></p>
<p>Were you aware that this topic exist? Was it just too difficult to find the relevant repositories?</p>
<p>I find Github’s search quite poor (compared to global Google search or full-text search in a cloned repository on my computer). How do you usually use github search? Do you type complete class names there? How do you find the relevant class names?</p>
<aside class="quote no-group" data-username="Amine" data-post="8" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>for example the first three lines in my code example are very hard if not impossible to find out from the generated documentation, i would look into the code of a module that uses folder hiearchy to find out how it’s done</p>
</blockquote>
</aside>
<p>All the basics (how to get subject hierarchy node and how to use it) is demonstrated in several examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy">script repository</a>.</p>
<p>Were the examples in the script repository insufficient? What additional examples would have helped?</p>
<p>Was there any subject hierarchy related feature that you did not find in the <a href="http://apidocs.slicer.org/master/classvtkMRMLSubjectHierarchyNode.html">subject hierarchy node documentation</a>?</p>
<aside class="quote no-group" data-username="Amine" data-post="8" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>The doxygen generated documentation only provides the names of methods for each class or what type of argument is required for methods but finding out the sequence of code lines to actually obtain those arguments would require browsing into some related module’s code</p>
</blockquote>
</aside>
<p>This is indeed something to learn in all application frameworks, at all levels. The same applies at lower levels - for example for Qt. Although every Qt class is documented in detail, you need to look at Qt examples and search on forums to be able to accomplish anything. The same resources are available for Slicer (API reference, tutorials, forum, script repository, module template, and all the existing modules that serve as examples).</p>

---

## Post #10 by @Amine (2021-07-10 03:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Were you aware that this topic exist?</p>
</blockquote>
</aside>
<p>No I did not, it has indeed many python written modules that can be very helpful!, I used to look for those either in GitHub if the developer linked to that, in slicer’s git hub or in python’s install folder  (with no luck sometimes)</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Was it just too difficult to find the relevant repositories?</p>
</blockquote>
</aside>
<p>Yes it was often difficult, unless I found a link to the developer’s git. the slicer extension topic you sent is very rich and should definitely get more exposure!</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How do you usually use github search? Do you type complete class names there? How do you find the relevant class names?</p>
</blockquote>
</aside>
<p>It takes some trial and error, i sometimes search using the module’s name ( the modules self test provides some insight on how to access the methods of the core modules), and looking for class names across slicer’s GitHub is useful when i don’t know what module they were used in, as for obtaining class/method names i get a node in slicer’s console and use tab to browse through its methods, looking for what could be of use ( note on this: it’s tedious to look into those methods in the tiny scroll list that appears and oddly enough it doesn’t always correspond to the doxygen generated documentation!)</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>All the basics (how to get subject hierarchy node and how to use it) is demonstrated in several examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy" rel="noopener nofollow ugc">script repository</a>.</p>
<p>Were the examples in the script repository insufficient? What additional examples would have helped?</p>
</blockquote>
</aside>
<p>I wrote that code quite some time ago and i probably used the examples in the script repository you linked (my bad!) but there are still quite some code examples that are not present in the script repository ( and rightfully so, i guess it cannot contain everything needed for more complex needs)</p>
<p>In this case it would be this line that is not present in the script repo but i understand it’s a rather uncommon neeed <code>slicer.vtkMRMLFolderDisplayNode.GetHierarchyVisibility(modelNode)</code><br>
i used it in combination with the model’s visibility to know if it is effectively visible.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Was there any subject hierarchy related feature that you did not find in the <a href="http://apidocs.slicer.org/master/classvtkMRMLSubjectHierarchyNode.html" rel="noopener nofollow ugc">subject hierarchy node documentation</a>?</p>
</blockquote>
</aside>
<p>In a previous forum post (where I asked about a similar issue) I was linked to <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLFolderDisplayNode.h#L90" rel="noopener nofollow ugc">this function</a> which eventually led to using it as <code>sceneitem_node.GetHierarchyVisibility(modelnode)</code> and while I could find it under <a href="http://apidocs.slicer.org/master/classvtkMRMLFolderDisplayNode.html" rel="noopener nofollow ugc">vtkMRMLFolderDisplayNode</a> It’s not easy to figure out how to write the correct syntax (that you wrote in your reply).</p>
<p>As for for subject hierarchy node, the type of variables to use and how to get them is clear from the examples in the script repository, and additional methods are well listed in the doxygen documentation so basic usage is well covered.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="18344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The same resources are available for Slicer (API reference, tutorials, forum, script repository, module template, and all the existing modules that serve as examples).</p>
</blockquote>
</aside>
<p>Yes those are indeed a necessary reference to make anything in slicer, in fact, as a surgeon with no formal programming background, I was able to develop a fully working slicer module (segmentation related features mainly) only using that, qt documentation and help from this forum/stackoverflow. (some of those functions are quite innovative, I’ll describe what they do/link you the module if you’d like).</p>
<p>The GitHub topic with slicer extensions would be of enormous help to anyone and I think it should be linked very clearly on top of the script repository, as a more in depth and complete example stack completing the purpose of the script repo.</p>

---

## Post #11 by @pieper (2021-07-10 17:03 UTC)

<p>Very helpful discussion.  Here’s a PR to add some links.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5737">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5737" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5737" target="_blank" rel="noopener">DOC: Add links and comments to script repository</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>Slicer:repository-links</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-07-10" data-time="17:02:40" data-timezone="UTC">05:02PM - 10 Jul 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 9 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5737/files" target="_blank" rel="noopener">
          <span class="added">+9</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As suggested in this thread: https://discourse.slicer.org/t/model-hiearchy-visib<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5737" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ility-returns-an-exception/18344/10</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
