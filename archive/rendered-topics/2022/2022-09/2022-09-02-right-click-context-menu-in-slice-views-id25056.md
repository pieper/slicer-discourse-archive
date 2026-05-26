---
topic_id: 25056
title: "Right-click context menu in slice views"
date: 2022-09-02
url: https://discourse.slicer.org/t/25056
last_bumped: 2026-03-18T13:10:03.413Z
---

# Right-click context menu in slice views

**Topic ID**: 25056
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/right-click-context-menu-in-slice-views/25056

---

## Post #1 by @giovform (2022-09-02 19:58 UTC)

<p>How can I programatically disable (and enable again) the right-click context menu in slice views?</p>

---

## Post #2 by @lassoan (2022-09-02 21:40 UTC)

<p>You can configure this at multiple levels. If you just want to disable all actions in all views then you can set an empty list for the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-allowlist-to-customize-view-menu">allowed context menu action names</a>. If you just want to disable right-click action in certain views then you can remove the right-click GUI event translation (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#custom-shortcut-for-moving-crosshair-in-a-slice-view">assign the right-click GUI event</a> to <code>vtk.vtkWidgetEvent.NoEvent</code> widget event).</p>

---

## Post #4 by @codeling (2026-03-17 15:22 UTC)

<p>I believe the input handling has been considerably reworked lately, I can’t figure out how disabling the context menu in current slicer(main branch) would work (3D view / slice views). I tried via displayable manager, but seems I can’t register vtkCommand::RightButtonPressEvent - my ProcessEvents is never called</p>

---

## Post #5 by @codeling (2026-03-18 12:29 UTC)

<p>I also tried via <code>qSlicerSubjectHierarchyPluginLogic::setAllowedViewContextMenuActionNames</code>, as suggested above, but setting the allowed actions to empty does not seem to work. When I look at the check in <code>buildMenuFromActions</code>, it looks like this:</p>
<pre><code class="lang-auto">if (!allowedActions.isEmpty() &amp;&amp; !allowedActions.contains(action-&gt;objectName()))
</code></pre>
<p>and thus considers an empty list as “all actions allowed”, right?</p>
<p>I have now a workaround based on eventFilter - I block the right button pressed/released event for the QVTKOpenGLNativeWidget of the respective 3D / slicer view; this is the best I could come up with so far which works, but maybe someone has a better solution?</p>

---

## Post #6 by @cpinter (2026-03-18 13:10 UTC)

<p>I recently had to customize this menu and after trying many things ended up doing this:</p>
<pre><code class="lang-auto">  @staticmethod
  def showSubjectHierarchyContextMenuActions(show) -&gt; None:
    """
    Show or hide subject hierarchy context menu actions that are not relevant in custom app mode.
    """
    pluginHandler = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    viewContextMenuPlugin = pluginHandler.pluginByName('ViewContextMenu')
    viewContextMenuActions = slicer.util.findChildren(viewContextMenuPlugin, className='QAction')
    actionTexts = ["Place", "Adjust window/level", "View transform", "Configure slice view annotations..."]
    for action in viewContextMenuActions:
      if action.text in actionTexts:
        # action.visible = show  #TODO: This does not have effect (shown at context menu building)
        action.enabled = show

</code></pre>
<p>Back then I didn’t want to spend time modifying the core, so had to do a workaround… It would make sense to make this possible from the API.</p>

---
