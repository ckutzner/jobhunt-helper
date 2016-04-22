# jobhunt-helper
A set of bash and Python3 tools to help generate neat job applications in LaTeX, track them and generate reports. This is a rewrite/refactoring of my [application helper scripts](https://github.com/ckutzner/application-scripts), with a new approach and Python3.

Who likes hunting for jobs? I don't know - but I do know that I, personally, dislike it fiercely. So if I have to do it, I want to do it efficiently, e.g. by automating brainless work and copy-pasting, thus freeing mental capacity for the bits that actually benefit from the application of (a bit or lots) of brainpower. 

Here's what this toolset aims to do:

* generate a LaTeX coverletter, tailored to your needs (choose between different body text templates, e.g. conservative/edgy text, modify availability based on location of the job - e.g. if you could start a job in your city earlier than one that requires you to move - modify text for temp agencies or other intermediaries)
* generate a pdf from that letter and append your CV, testimonies, and work samples 
* if desired, open email client (so far: Thunderbird) with pre-populated fields and the right attachment already chosen
* track your applications in an sqlite3 database
* generate LaTeX reports for the German Jobcenters if necessary and desired

## Requirements
 * Python3
 * sqlite3
 * bash
 * LaTeX, pdflatex and detex

## Known limitations
Because this is a "scratch my own itch" project, I write it around my own application process. That means:

 * LaTeX-centric.
 * So far, the documents used in this toolset conform to German standards (re: letter class, addresses, etc.). Input for other countries is welcome.
 * so far, Linux/Unix-only. If you want to make a version for Windows or other OSs, go ahead and fork me!
 * I don't plan to make a GUI, because I tend to find GUIs distracting and prefer working in terminals, and making one doesn't pertain to "scratching my own itch". If you want to make one: fork me!
