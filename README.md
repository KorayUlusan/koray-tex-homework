# Koray's latex homework style package

This is the style I use in my homeworks. You can get a feel of this style [here](showcase.pdf).

I'm still learning and honestly have no idea what I'm doing. This repo probably doesn't follow any latex package convensions.

Feel free to open a pull request. 

## Usage

```latex
% You need to include this package in your latex file.
\usepackage{./koray-tex-homework/homework.sty}

% I'd really appricate if you give credit 
\KoraysHomeworkStyCredit % can be added before \end{document}
```

### `\question` commands

Since homeworks have a defined structure, it made more sense to write the question numbers by hand. It makes the latex document more readable. (and avoids `\section*{1}`)

```latex
\question{1}
\subquestion{(a)}
\subsubquestion{(i)}
```

You can overwrite colors

### text styles

```latex
\bdtexttt{text here}
\hltexttt{text here}
```

### comments

Its important to leave notes to your teampartners.

```latex
% first create a command per person
\newcommand{\noteKoray}[1]{\notePerson{red}{Note}{Koray}{#1}}

% then you can use it
\noteKoray{text here}
```

### decorations

TODO

```latex
\ornamento
\ornamentoL
\ornamentoR
```
