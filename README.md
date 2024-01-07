# GitHub Copilot 实用教程

This is the repository for the LinkedIn Learning course `GitHub Copilot 实用教程`. The full course is available from [LinkedIn Learning][lil-course-url].

这是 LinkedIn Learning 课程 “GitHub Copilot实用教程” 的存储库。完整的课程可从[LinkedIn Learning][lil-course-url]获得。

_请在 main 分支中查看 README 文件以获取最新信息。_

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

    - [GitHub Copilot](https://copilot.github.com/)
    - [Visual Studio Code](https://code.visualstudio.com/)
    - [Python](https://www.python.org/downloads/)
    - [Node.js](https://nodejs.org/en/download/)
    - [Git](https://git-scm.com/downloads)

2. 使用 terminal（Mac）、CMD（Windows）或 SourceTree 等 GUI 工具将此存储库克隆到本地机器上。
3. [Course-specific instructions]

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/
[lil-thumbnail-url]: http://
