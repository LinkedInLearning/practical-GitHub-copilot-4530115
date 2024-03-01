# GitHub Copilot 实用教程

这是 LinkedIn Learning 课程 “GitHub Copilot实用教程” 的存储库。完整的课程可从[LinkedIn Learning][lil-course-url]获得。

![lil-thumbnail-url]

Github Copilot 正在彻底改变代码的编写方式。它可以提高开发人员的工作效率，将他们从重复性任务中解放出来。跟随讲师闫晓迪，学习如何用 Copilot 解决问题，成为一名更高效的开发人员。在课程中，他将展示如何使用 Copilot 找到代码问题的最佳解决方案， 让 Copilot 发挥最大效用。从设置到工具导航再到优化结果，带你亲身体验 Copilot 的强大功能。

## 使用说明

这个存储库为课程中的每个视频创建了相应的分支。您可以切换到特定分支，并查看该阶段的课程，或者将 `/tree/BRANCH_NAME` 添加到 URL 中以访问您要访问的分支。

## 分支

分支结构与课程中的视频相对应。命名约定遵循`CHAPTER#_MOVIE#`格式。例如，`02_03`分支对应第二章第三个视频。

有些分支会有一个起始状态和一个结束状态。这些状态用字母 `b` 表示“开始”，用字母 `e` 表示“结束”。`b` 分支包含视频开始时的代码。`e` 分支包含视频结束时的代码。`main` 分支保存课程最终状态的代码。

当做出文件更改后，从一个练习文件分支切换到下一个时，您可能会收到类似这样的消息：

```text
error: Your local changes to the following files would be overwritten by checkout:        [files]
Please commit your changes or stash them before you switch branches.
Aborting
```

要解决此问题：

1. 将更改添加到 git，可以使用这个命令：`git add`。
2. 提交更改，使用这个命令：`git commit -m "some message"`。

## 安装

1. 要使用这些练习文件，您必须安装以下内容：

    - [Visual Studio Code](https://code.visualstudio.com/)
    - [GitHub Copilot](https://copilot.github.com/)
    - [Python](https://www.python.org/downloads/)
    - [Git](https://git-scm.com/downloads)

2. 使用 terminal（Mac）、CMD（Windows）或 SourceTree 等 GUI 工具将此存储库克隆到本地机器上。

讲师

Xiaodi Yan

闫晓迪是微软 MVP、MCT 以及微软认证 Azure 解决方案架构师专家。自 2015 年起他就被授予微软 MVP 称号。他热衷于参与技术社区，组织线下和线上活动，并在各大会议和活动中做报告。他还撰写了许多关于 Azure、.NET 以及 DevOps 的博客和文章。


[lil-course-url]: https://www.linkedin.com/learning/practical-github-copilot-23083809
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D560DAQFl6dJmZ9ZAlw/learning-public-crop_675_1200/0/1709223121086?e=2147483647&v=beta&t=n_jIWoy4qW5Ao9N-dbKoAzg25yNZAslzdHdN3iwTK-c
