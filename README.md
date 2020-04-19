# doc
This repository hosts a lightweight markdown templating tool for command line. I mainly just use this for creating journal entries from a very simple template. Use it if you want...  
  
## Example Install and Usage  
Add to your ~/.bashrc (I didn't bother packaging this as anything but a python file...)
```
alias doc="python /path/to/this/repo/doc_from_template.py"
```
  
Navigate to where you want to create a document. Creating a default file is as easy as:
```
doc -d "Journal Entry" -t "journal, contemplation, programming, work"
```
  
Example output filename: 20200417-journalentry.md  
  
If you need to specify destination use the -c flag, and/or the filename with -f flag. Now you don't have to be in the same directory.
```
doc -d "To Do List" -t "errands, chores, general laborious tasks" -c /path/to/lists/ -f new_todo.md
```
This example creates `new_todo.md` at `path/to/lists/`. Generally, I just use the first example because I am usually in the directory I want to be in when I am writing a new document.

