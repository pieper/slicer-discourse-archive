# How to programmatically set Terminology Name and Category for vtkMRMLSegmentationNode?

**Topic ID**: 41504
**Date**: 2025-02-05
**URL**: https://discourse.slicer.org/t/how-to-programmatically-set-terminology-name-and-category-for-vtkmrmlsegmentationnode/41504

---

## Post #1 by @baderstine (2025-02-05 02:18 UTC)

<p>Operating system: MacOS 15.3<br>
Slicer version: 5.6.2</p>
<p>In my slicer extension, I am loading image and label (segmentation) volumes from a database.  I have figured out how to load a custom terminology json file when the extension is loaded:</p>
<pre><code class="lang-auto"># Placed in extension's __init__ function
        path = self.resourcePath("Terminologies/terminologyfilename.json")
        tlogic = slicer.modules.terminologies.logic()
        terminologyName = tlogic.LoadTerminologyFromFile(path)
</code></pre>
<p>I also created color table files to use when loading in segmentations:</p>
<pre><code class="lang-auto">color_table_name = "some name"
script_path = os.path.dirname(os.path.abspath(__file__))  # returns path to this file (volume.py)
color_file = os.path.join(script_path,"..","&lt;module name&gt;","Resources","Terminologies",f"{color_table_name}.txt")
color_table_node = slicer.util.loadColorTable(color_file)

ref_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
&lt;load label data into ref_node&gt;
ref_node.CreateDefaultDisplayNodes()
ref_node.GetDisplayNode().SetAndObserveColorNodeID(color_table_node.GetID())
seg_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(ref_node, seg_node)
seg_node.GetDisplayNode().SetAndObserveColorNodeID(color_table_node.GetID())
seg_node.SetReferenceImageGeometryParameterFromVolumeNode(ref_node)
slicer.mrmlScene.RemoveNode(ref_node)
</code></pre>
<p>I’m wondering if there is some way for me to set the default terminology name and category for seg_node in the above code so that when a user opens the Segment Editor for this segmentation node, adds a new segment, then double clicks on the Segment Color box (which brings up the Terminology selection window), my preferred Terminology, and Category are pre-selected, and all the user needs to do is pick the correct Property Type to assign to this segment?</p>
<p>Is there something like:<br>
seg_node.SetDefaultTerminology()<br>
seg_node.SetDefaultTerminologyCategory(&lt;Category.CodeMeaning&gt;)<br>
?</p>
<p>It feels like I’m doing something wrong or inefficient by loading BOTH a custom terminology file AND custom colortables which essentially map the exact same IDs, Names, and RGB/opacity values to individual segments/labels in different ways… but from all I can read/find this is the way?</p>

---

## Post #2 by @pieper (2025-02-10 16:49 UTC)

<p>There was a lot of discussion of color tables and terminologies at the recent Project Week.  It would be great if you could review the pending pull request and see if that addresses your concerns.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/InfrastructureForCustomTerminologyAndColorTablesInSlicer/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/InfrastructureForCustomTerminologyAndColorTablesInSlicer/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/InfrastructureForCustomTerminologyAndColorTablesInSlicer/" target="_blank" rel="noopener">Project Description</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8112">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8112" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8112" target="_blank" rel="noopener">Store and edit terminologies in color table nodes</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>cpinter:terminology-editing-4</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-12-22" data-time="21:23:49" data-timezone="UTC">09:23PM - 22 Dec 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/cpinter" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
            cpinter
          </a>
        </div>

        <div class="lines" title="24 commits changed 123 files with 8290 additions and 3969 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8112/files" target="_blank" rel="noopener">
            <span class="added">+8290</span>
            <span class="removed">-3969</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">- Add CSV file format support for color tables
  - Refactoring of storing color<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8112" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> properties in color node
  - Save terminology columns into color table CSV file
  - Implement color table terminology CSV reading
- Terminology manual editing from Colors module
- Move Colors widget classes into Colors module
  - The Colors module related widget classes have been in Libs/MRML/Widgets, but that way they cannot possibly use Terminology features. They need to be moved to the Colors module to facilitate this
    - Classes in Testing and DesignerPlugins folders using the moved classes have also been moved to Colors module
  - Remove FileName member from vtkMRMLColorNode, as it was not used (moreover, there were comments explaining why it is not used)
- Create terminology editor widgets for editing from item delegate
- Add functions to color node for get/set terminology as/from string (also add GetColorNameAutoGenerated)
- Style fixes
- Select terminology Colors module from the Terminologies column
- Terminology contexts from color nodes are offered in terminology context selector
- Add new color table node and entry buttons to Colors module
- Add export to color table function to Segment Editor

Re #6975, #7593

@muratmaga


https://github.com/user-attachments/assets/43fc0943-0f9f-4d90-bccc-7d463e90b7bb


https://github.com/user-attachments/assets/40412bd2-e73e-46ca-bf30-fd49f382290f


https://github.com/user-attachments/assets/3c7b3d3f-b9bb-40f4-a78c-c8158345a9e2</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @baderstine (2025-02-10 17:13 UTC)

<p>That’s a very extensive pull request on a code base that I am not familiar with at all.  From what I’ve read in the comments, it is possible that it does address my concern but I cannot be sure until I’ve actually run my custom module code against it.</p>

---
