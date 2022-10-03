<h1>Python - Test-driven development</h1>
<h2>Background Context</h2>
<h3>Important notice on intranet checks for Python projects</h3>
<p>Starting from today:</p>
<ul>
<li>Based on the requirements of each task,&nbsp;<strong>you should always write the documentation (module(s) + function(s)) and tests first</strong>, before you actually code anything</li>
<li>The intranet checks for Python projects won&rsquo;t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case.&nbsp;<strong>But not in the implementation of them!</strong></li>
<li><strong>Don&rsquo;t trust the user</strong>, always think about all possible edge cases</li>
</ul>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="doctest &mdash; Test interactive Python examples" href="https://intranet.hbtn.io/rltoken/Hmd_LI8NZ-F2ymDxue5HCg" target="_blank" rel="noopener">doctest &mdash; Test interactive Python examples</a>&nbsp;(<em>until &ldquo;26.2.3.7. Warnings&rdquo; included</em>)</li>
<li><a title="doctest &ndash; Testing through documentation" href="https://intranet.hbtn.io/rltoken/fbFfGNFU07L2yD0D1uc-Xg" target="_blank" rel="noopener">doctest &ndash; Testing through documentation</a></li>
<li><a title="Unit Tests in Python" href="https://intranet.hbtn.io/rltoken/LhbdUZYzqiP7cjxjE3rG3w" target="_blank" rel="noopener">Unit Tests in Python</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/RMt2qsdC652WOJu2QyacaA" target="_blank" rel="noopener">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>Why Python programming is awesome</li>
<li>What&rsquo;s an interactive test</li>
<li>Why tests are important</li>
<li>How to write Docstrings to create tests</li>
<li>How to write documentation for each module and function</li>
<li>What are the basic option flags to create tests</li>
<li>How to find edge cases</li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
</ul>
<h3>Python Test Cases</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder&nbsp;<code>tests</code></li>
<li>All your test files should be text files (extension:&nbsp;<code>.txt</code>)</li>
<li>All your tests should be executed by using this command:&nbsp;<code>python3 -m doctest ./tests/*</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your functions should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case &ndash; The Checker is checking for tests!</li>