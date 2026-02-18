# How to add additional actions when using parameterNodeWrapper?

**Topic ID**: 42320
**Date**: 2025-03-26
**URL**: https://discourse.slicer.org/t/how-to-add-additional-actions-when-using-parameternodewrapper/42320

---

## Post #1 by @mikebind (2025-03-26 20:54 UTC)

<p>I like the newer parameterNodeWrapper architecture for modules, and it nicely simplifies keeping parameters and GUI elements in sync.  However, I run into problems whenever I want to add any other effects from changing a parameter value.  For example, I have a node selector widget for a sequence node.  When a sequence node is selected, I want to also automatically store the first associated sequence browser node as a different parameter in the parameter node and add an observer to that browser (so I can respond appropriately later when the user changes the current sequence index using the browser).  I have tried to achieve this by adding a connection from the node selector’s currentNodeChanged signal to a callback which handles setting the browser node parameter and browser observer creation.  However, this seems to interfere with the parameter node wrapper’s functionality, and I haven’t been able to figure out a solution which works.  It seems like what happens is my callback is triggered with the newly chosen node as input, but changing the parameter node within my callback triggers an update to the gui from the parameter node which ends up resetting the selector and the parameter node value to None and not my new selection.   Is there a suggested approach to handle this kind of situation?  The parameter node wrapper approach works for 95% of my needed parameters, so I would like to keep using it, but I don’t know how to handle the other 5%.  Should those elements just get their own separate callbacks independent of the wrapper?  Doesn’t that mean I will end up needing to write updateGUIFromParameterNode and updateParameterNodeFromGUI functions anyway, and won’t that also possibly cause conflicts with the wrapper functions?  I appreciate any suggestions people have.  I can also try to create a minimal module example illustrating the issue if someone is willing to take a look at that.</p>

---

## Post #2 by @pieper (2025-03-27 19:25 UTC)

<p>I think that yes, a small example module would help.  It would be good to document the best practices for working with and extending the parameter node wrappers in the context of more complex GUIs.</p>

---

## Post #3 by @mikebind (2025-03-28 15:57 UTC)

<p>Thanks for taking a look.  Here is a pretty minimal module which illustrates the issue <a href="https://drive.google.com/file/d/1f5S46cDQn719z96QqWSwzwg9l1i3j5Es/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">WrapperIssues.zip - Google Drive</a><br>
Unzip, add to module paths, and open WrapperIssues module.<br>
In the input selector, try to choose the loaded CTPCardioSeq sequence instead of None.</p>
<p>The intended result of this is that the sequence is selected in the selector, and, internally to the module, two additional actions occur:</p>
<ul>
<li>The first browser node associated with the selected sequence is stored in the module’s parameter node</li>
<li>That browser has an observer added to it which triggers a callback when the frame index changes.  Currently that callback just prints a line to the interactor</li>
</ul>
<p>Contrary to the expected result, the selector still shows None.  However, the browser node is, in fact observed, and is actually doubly observed (it prints two identical lines for every browser index change).</p>
<p>I assume the return to None selection comes somehow from there being two callbacks triggered when the GUI selection is made, and that the second one undoes the first. I’m even more confused by why two observations seem to be set.  My guess is that the second observation comes from a second round of callback calls triggered by the second change to the GUI selector (the one changing it back to None), but if the selected node is None, then no additional observation should end up being added. It’s also not clear to me what keeps the process from entering an infinite loop; that is, if the structure I have set up ends up results in a change in the GUI which triggers two callbacks, one of which triggers another change in the GUI, which maybe triggers two more callbacks, why did that loop stop there and not trigger two more callbacks?</p>
<p>I’m not wedded to this particular type of program flow; I am just interested in learning a best practice approach to add any kind of additional action on top of the parameterNodeWrapper linkage.  Especially an action which can make a different change to the parameter node within it. I realize that allowing arbitrary changes to a watched parameter node could easily lead to problems because nested changes could trigger infinite loops, but the particular type of case I am thinking of (just storing or updating a parameter value with no needed follow-on effects on the GUI side) doesn’t seem like it should be problematic at all.  If there were a way to easily make a direct change to a parameter without immediately triggering a Modified signal, that might be good enough.</p>
<p>Or, maybe I am thinking about this wrong, and the right approach is to have the parameterNodeWrapper parameters be ONLY the things which are directly linked to GUI elements, and any other parameters should be properties of the module widget or module logic objects.  I have generally tried to put all parameters into the parameter node because the parameter node is saved with the scene, whereas I don’t think things stored as widget or logic properties would be restored after a save/load cycle.</p>

---
