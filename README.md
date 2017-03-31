# HelloWorld
Learning GitHub

Learning branch

## git
Git can be downloaded from [here](http://git-scm.com/download/win)

#### Git commands
Following are some git commands:
* git init
* git add *file*
* git status
* git commit
* git log --oneline
* git push
* git pull
* git clone
* git checkout

#### A sample session:
* git init
* git config --global user.name 'user name'
* git config --global user.email 'email address'
* git add index.html
* git status
* git remote add origin *gitub address*
* git push origin master

#### Git version with office documents
**git diff can compare word documents, so we can use git to do version control of office documents.**

Four steps to accompany the goal.

1. install [pandoc](http://pandoc.org/installing.html)
1. in ~/.editconfig add
```
[diff "pandoc"]
  textconv=pandoc --to=markdown
  prompt = false
[alias]
  wdiff = diff --word-diff=color --unified=1
```
3. in .gitattributes of project add
```
*.docx diff=pandoc
```
4. git diff *file* or git wdiff *file*

[demo](https://github.com/hjy1210/gitwithword)

reference: 
* [integrate git diffs with word docx files](https://github.com/vigente/gerardus/wiki/Integrate-git-diffs-with-word-docx-files)
* [External Merge and Diff Tools](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
* [Adding an existing project to GitHub using the command line](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)

## cors
If restful service, which is an express server, use [cors](https://www.npmjs.com/package/cors) as middleware,
client websites in different domains can use restful service as back end.

## KaTeX vs MathJax
[KaTeX](https://github.com/Khan/KaTeX) is an alternative to [MathJax](http://docs.mathjax.org/).

[KaTeX and MathJax Comparison Demo](http://www.intmath.com/cg5/katex-mathjax-comparison.php) demostrate the pros and cons
between them. KaTeX is much faster, MathJax is much more flexible.

## React-Native
Reference [Getting started](https://facebook.github.io/react-native/docs/getting-started.html).

#### requirement
1. install node.js.
2. install python2 ?
3. use `npm install -g react-native-cli` to install globally module react-native-cli.
4. download and install [Android Studio](https://developer.android.com/studio/index.html).
5. use `set ANDROID_HOME=c:\users\username\appdata\local\android\sdk` to set environment variable ANDROID_HOME.
6. use `set JAVA_HOME=c:\program files\android\android studio\jre` to set environment variable JAVA_HOME.

#### react-native sample
[react-native sample](./React-Redux/react-redux-practice.md).

Choose appropriate directoy for doing work. For example *d:\work*.
1. In directory D:\work, execute `react-native init MyApp` to initial react-native project *MyApp* and install necessary components
  in subdirectory *MyApp*.
2. cd *MyApp*

Use Android Studio to start Android Virtual Device
1. Open Android Studio, open existing project *MyApp*.
2. Run > Edit Configuration > Defaults > Android App > Target > Emulator >
    Prefer Android Virtual Device ... > Shift+Enter > AVD manager >
    Creat Virtual Device(if your favorite cirtual device is not in list) >
    Select Virtual Device > Press Right Triangle to **lauch selected AVD**.

Note: `android avd` is no longer available.

Compile and bundle index.android.js into selected AVD
1. In subdirectory *MyApp*, execute `react-native run-android` to bundle index.android.js into selected AMD.
2. open selcted AMD, the *MyApp* is in work.
3. modify index.android.js and execute `react-native run-android` to rebundle index.android.js into selected AMD.

## textract
[Textract](https://www.npmjs.com/package/textract) is a node module, its source code is [here](https://github.com/dbashford/textract), which can extract text form .docx, .doc, .pdf, ...。

#### install
Use `npm install -g textract` to install globally.

#### usage
`textract file.docx`

## Markdown Reader
[Markdown Reader](./another.md) is a Chrome extension which can help displaying mathematics formula in any web page.

It can display some mathematics formula.
$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$
and $E=mc^2$.

But look at following matrix
$$ \begin{pmatrix} 1 & 0 \ 0 & 1 \end{pmatrix} $$

## Github with MathJax
[Github with MathJax](https://github.com/orsharir/github-mathjax) is a chrome extension which
 add support for LaTeX equations in GitHub repositories, rendering them with an open source [MathJax](https://mathjax.org) library. In example, if you had it install you would see the following lovely equation: $e^{iπ}+1=0$.

$$e^{iπ}+1=0$$

Check it with matrix
$$ \begin{pmatrix} 1 & 0 \ 0 & 1 \end{pmatrix} $$

## Detecting encoding
Detecting encoding of a text file is an important work. Please refer to [Encoding.md](./Encoding.md)