# Standard way of running modules from the command line

**Topic ID**: 20552
**Date**: 2021-11-09
**URL**: https://discourse.slicer.org/t/standard-way-of-running-modules-from-the-command-line/20552

---

## Post #1 by @Connor-Bowley (2021-11-09 19:49 UTC)

<p>It would be nice to be able to run some modules from the command line, especially in cases of long running/computationally intensive modules that would be convenient to run on a server. My understanding is that there is not currently a nice or standard way to make a module run-able from the command line.</p>
<p>Proposition: Create a way to pass arbitrary arguments to a module for use as if it were a command line program running with all the features of 3DSlicer (or at least the non-GUI features).</p>
<p>Possible implementation:</p>
<ul>
<li>Add a new launch argument to the Slicer launcher similar to <code>-c</code>, but instead of running arbitrary code it runs a module. My suggestion would be to use <code>-m</code> as it is similar in concept to Python’s <code>-m</code> option.
<ul>
<li>Example: <code>./Slicer -m ShapeAnalysisModule --spharm-pdm-generator --number-of-iterations=1000 --input-directory=~/input --output-directory=~/output</code>
</li>
</ul>
</li>
<li>Add a new virtual method <code>int runModule(int argc, char** argv)</code> to qSlicerAbstractCoreModule(?) that is called by Slicer whenever the <code>-m</code> argument is used. Similar to Python’s <code>-m</code> I would propose that all arguments following the <code>-m</code> are passed as is to the <code>runModule</code> method of the module and not parsed by Slicer’s normal argument parsing.
<ul>
<li>Perhaps a different name for the function than <code>runModule</code>, but I am not sure what.</li>
<li>CLI modules would just be called when they are passed as a <code>-m</code>
</li>
<li>The default implementation in the base class would say something like “Module ‘name’ cannot be run from the command line” and then exit.</li>
<li>Module’s <code>runModule</code> method could use argparse in Python or something else to parse it’s own command line</li>
</ul>
</li>
<li>Possibly the <code>-m</code> method should also imply <code>--no-main-window</code>
</li>
</ul>
<p>Is this a feasible feature request?</p>

---

## Post #2 by @lassoan (2021-11-09 22:51 UTC)

<p>Putting together executables by running executables one after the other using shell script certainly used to be a popular approach. However, nowadays these workflows are implemented in Python scripts instead, because you can easily integrate many tools from different sources, the script runs on all platforms, there are great IDEs, and very importantly - you load your data once and you keep it in memory until the processing is completed. Are you sure that using a CLI interface is what you need? Is the hugely increased execution time by loading/saving all data to files acceptable?</p>
<p>Adding a <code>runModule(int argc, char** argv)</code> method would be easy, but the implementation, documentation, testing, and long-term maintenance would be very significant effort. If the same interface could be leveraged for the planned PySlicer, which would expose MRML and Slicer modules as pip-installable Python libraries then the effort would be better justified. Could you think about a design that would allow generation both CLI and Python function or class interface?</p>
<p>To reduce development and maintenance effort, it would be better to use existing C++ method definition and their documentation, with some extra decorators to mark a module logic method to be exposed as a <em>CLI module</em> and to indicate which parameters are input and which are output. Types should be possible to deduce the same way as the VTK Python wrapper does it. Maybe the CLI interface could use the Python interface, because it is much harder to retrieve method name, parameter names, types, documentation, etc. from a C++ header file than from a Python class.</p>

---

## Post #3 by @Connor-Bowley (2021-11-11 13:57 UTC)

<p>After giving it some thought, I think that the python script you recommended will probably meet my needs right now, although I do find the decorators for CLI commands interesting. Thanks.</p>

---
