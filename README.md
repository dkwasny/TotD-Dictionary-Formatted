Typing of the Dead: Overkill Dictionary Formatter
=================================================
The goal of this script is to make an attempt to format arbitrary english text such that it can be ingested into the Steam Workshop tool for The Typing of the Dead: Overkill.

My personal intention is to use a few public domain books from [Project Gutenberg](https://www.gutenberg.org/wiki/Main_Page).<br/>
This typically results in much longer phrases than what the game normally provides, which should help boost my typing skill.<br/>
You may want to manually remove the legal text in front of and after the book contents.

My limited testing has shown that TotD has a hard limit of 50 characters per line.<br/>
Any longer and the sentence will get cut off so I prevent any lines longer thant 50 characters from being written.

I added some sample input for my personal testing, but you can use it to verify the script is even working on your machine.

Please feel free to let me know of any issues via email or Github issues...or whatever.

How to Use
----------
Since TotD is not on OSX or Linux, the examples are going to be only for Windows.

To just see what the output will look like, you can run a command like this in your terminal.

        C:\path\to\python.exe totd-formatter.py -i INPUT_FILE [-m MIN_CHARACTERS_PER_LINE]

To write the output to a file just add an output redirect to the end of your command like so.

        C:\path\to\python.exe totd-formatter.py -i INPUT_FILE [-m MIN_CHARACTERS_PER_LINE] > output.txt

Using the ">" operator will overwrite the contents of the output file.<br/>
Using the ">>" operator will append to the end of the output file.<br/>
See the [Microsoft Documentation](https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/redirection.mspx?mfr=true) for more info on redirects.

You should then be able to load the file into the workshop tool.<br/>
Details on the tool itself can be found in [this](http://steamcommunity.com/sharedfiles/filedetails/?id=414808565) handy tutorial made by alex.marian.
