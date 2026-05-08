# Scientific Textbook Proofreading Skill

**语言 / Language:** [English](README.md) | [简体中文](README.zh-CN.md)

一个用于科学教材校对与候选勘误报告生成的可复用 AI skill。

本项目面向包含大量公式、推导、交叉引用、附录、习题和领域术语的长篇科学教材或讲义。它帮助 Codex、Claude Code 等本地 AI agent 按章节审查科学内容，重点关注公式错误、量纲一致性、物理假设、数值系数、惯例差异、过时科学表述和容易误导读者的科学语言。

本项目的目标用户包括教材作者、科学编辑、课程教师、研究生和技术审稿人。它的定位不是替代领域专家，而是为专家提供结构化、保守、可复核、基于证据的候选勘误工作流。

---

## 这个 skill 适合做什么？

- 科学教材校对。
- 课程讲义审查。
- 研究生课程材料检查。
- 公式和推导核验。
- 量纲一致性检查。
- 候选勘误报告生成。
- 与权威参考教材进行对照。
- 识别已经被后续研究或观测更新的过时表述。
- 使用 Codex 或 Claude Code 进行本地文件逐章审阅。
- 未来构建半自动教材校对 pipeline。

---

## 这个 skill 不适合做什么？

- 普通语法润色。
- 纯排版修正。
- 字体或版式清理。
- bibliography 格式整理。
- citation placeholder 自动补全。
- 替代专家人工审稿。
- 上传或重新分发受版权保护的教材。

---

## 仓库结构

~~~text
scientific-textbook-proofreading-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── SECURITY.md
├── .gitignore
├── skill/
│   ├── SKILL.md
│   ├── output_contract.md
│   ├── scientific_rubric.md
│   ├── citation_policy.md
│   └── refusal_and_uncertainty_policy.md
├── schemas/
│   └── errata_report.schema.json
├── examples/
│   ├── input/
│   │   ├── sample_page.md
│   │   └── sample_equations.tex
│   ├── expected_output/
│   │   ├── sample_errata_report.md
│   │   ├── synthetic_chapter_01_errata.md
│   │   └── synthetic_chapter_01_errata.json
│   ├── synthetic_textbook/
│   │   └── chapter_01.md
│   ├── prompt_templates/
│   │   ├── batch_chat_mode.md
│   │   ├── challenge_previous_judgement.md
│   │   ├── chapter_review_with_reference.md
│   │   ├── chapter_review_without_reference.md
│   │   ├── local_file_report_mode.md
│   │   └── single_equation_check.md
│   └── project_template/
│       ├── README.md
│       ├── input/
│       │   └── .gitkeep
│       └── reports/
│           └── .gitkeep
├── evals/
│   ├── cases.jsonl
│   └── golden/
│       ├── case_001.md
│       ├── case_002.md
│       ├── ...
│       └── case_012.md
├── scripts/
│   ├── install_local.sh
│   ├── make_project_template.py
│   ├── validate_schema.py
│   ├── lint_skill.py
│   ├── run_evals.py
│   ├── lint_markdown.py
│   └── validate_examples.py
├── templates/
│   └── processing_notes.template.md
└── .github/
    └── workflows/
        └── ci.yml
~~~

---

## 核心 skill 文件

主 skill 文件是：

~~~text
skill/SKILL.md
~~~

它包含 agent 的激活元数据、科学审查流程、输出格式、来源政策、不确定性处理、天体物理专项 checklist、batch mode 和 local file report mode。

配套文件包括：

~~~text
skill/output_contract.md
skill/scientific_rubric.md
skill/citation_policy.md
skill/refusal_and_uncertainty_policy.md
schemas/errata_report.schema.json
templates/processing_notes.template.md
~~~

这些文件共同定义了：什么问题应该报告、报告如何结构化、如何引用来源、如何处理不确定性，以及如何生成机器可读的 JSON 勘误报告。

---

## 推荐提示词：基础章节审查

~~~text
Please use the Scientific Textbook Proofreading Skill.

File roles:

- Manuscript under review: [draft_filename.pdf]
- Authoritative reference source: [reference_filename.pdf]
- Optional additional sources: [additional_sources_if_any]

Review the manuscript under review, starting from [chapter_or_section].

Focus on scientific correctness:

- formula errors,
- dimensional consistency,
- numerical coefficients,
- physical assumptions,
- approximation regimes,
- unit systems,
- notation consistency,
- consistency between formulae and prose,
- outdated scientific claims,
- misleading scientific prose.

Use the authoritative reference source to check standard derivations, conventions, terminology, and accepted formulae.

Ignore layout, typography, citation placeholders, missing references, bibliography formatting, and grammar-only issues.

Only report issues requiring correction or clarification.
~~~

如果用于中文教材，可以在提示词中补充：

~~~text
报告主体请使用中文。必要的英文术语、仪器名、合作组名和标准物理术语可以保留英文。若给出教材替换文字，请给出可直接粘贴回中文教材的中文表述。
~~~

---

## 文件角色命名规则

当使用多个 PDF、TeX 源文件或参考资料时，请明确告诉 agent 每个文件的角色。

推荐文件名前缀：

~~~text
UNDER_REVIEW_textbook_draft.pdf
REFERENCE_Longair_High_Energy_Astrophysics.pdf
REFERENCE_Rybicki_Lightman_Radiative_Processes.pdf
ANSWER_KEY_chapter_12_reference_solution.pdf
IGNORE_old_notes.pdf
~~~

推荐角色说明：

~~~text
- Manuscript under review: UNDER_REVIEW_textbook_draft.pdf
- Authoritative reference source: REFERENCE_Longair_High_Energy_Astrophysics.pdf
- Optional additional source: REFERENCE_Rybicki_Lightman_Radiative_Processes.pdf
- Answer key, not automatically authoritative: ANSWER_KEY_chapter_12_reference_solution.pdf
~~~

不要假设 agent 一定能仅凭文件名准确判断文件角色。最好在提示词中显式说明。

---

## TeX 源文件与 PDF：哪个更适合？

对于科学教材，**TeX 源文件通常比 PDF 更适合科学内容审查**。

推荐优先级：

~~~text
TeX 源文件 > 编译后的 PDF > OCR/扫描版 PDF
~~~

原因：

- TeX 源文件保留公式结构、上下标、分式、符号和交叉引用。
- PDF 文本抽取可能破坏数学结构。
- PDF 更适合核对最终页码、图表、caption 和编译后显示效果。
- 最理想的输入方式是同时提供完整 LaTeX 工程和编译后的 PDF。

推荐结构：

~~~text
input/
├── UNDER_REVIEW_latex_project/
│   ├── main.tex
│   ├── chapRadiation.tex
│   ├── chapBinary.tex
│   ├── chapCompactObject.tex
│   ├── figures/
│   ├── tables/
│   └── references.bib
├── UNDER_REVIEW_compiled_book.pdf
├── REFERENCE_*.pdf
└── ANSWER_KEY_*.pdf
~~~

使用时可提示 agent：

~~~text
请优先读取 TeX 源文件进行正文、公式、符号、章节结构和交叉引用审查；使用 PDF 辅助确认页码、图表、caption 和最终显示效果。
~~~

---

## Batch Chat Mode

如果使用普通聊天界面，而不是本地 coding agent，可以使用 batch mode。

~~~text
Please use the Scientific Textbook Proofreading Skill in batch mode.

Review chapters in order. After finishing one chapter, continue to the next chapter automatically within the same response. Stop only when the response length is approaching the limit, file extraction quality is unreliable, source roles are ambiguous, or all requested chapters have been reviewed.

Only report scientifically meaningful issues requiring correction or clarification.
~~~

注意：普通聊天界面不能在一次回复结束后自动继续发送消息。这里的 batch mode 指在同一次回复中尽可能连续处理。

---

## Local File Report Mode

对于长篇教材，推荐使用 Local File Report Mode。

agent 不在聊天窗口中输出超长报告，而是为每章写一个 Markdown 文件：

~~~text
proofreading-project/
├── input/
│   ├── UNDER_REVIEW_textbook_draft.pdf
│   └── REFERENCE_authoritative_source.pdf
├── reports/
│   ├── chapter_01_errata.md
│   ├── chapter_02_errata.md
│   ├── processing_notes.md
│   └── summary.md
└── README.md
~~~

推荐提示词：

~~~text
Please use the scientific-textbook-proofreading skill in Local File Report Mode.

File roles:

- Manuscript under review: input/UNDER_REVIEW_textbook_draft.pdf
- Authoritative reference source: input/REFERENCE_authoritative_source.pdf

Review the manuscript chapter by chapter. Do not print the full report in chat. Write each chapter report to:

reports/chapter_01_errata.md
reports/chapter_02_errata.md
...

Each chapter report should contain only scientifically meaningful issues and a chapter-level summary. After processing multiple chapters, generate reports/summary.md. If PDF extraction, formula recognition, or chapter boundary detection is unreliable, write details to reports/processing_notes.md.
~~~

---

## 创建本地校对项目

使用辅助脚本：

~~~bash
python scripts/make_project_template.py ~/proofreading-projects/my-textbook-review
~~~

这会创建：

~~~text
~/proofreading-projects/my-textbook-review/
├── input/
├── reports/
└── README.md
~~~

然后将文件放入：

~~~text
~/proofreading-projects/my-textbook-review/input/
~~~

并使用以下前缀：

~~~text
UNDER_REVIEW_*.pdf
REFERENCE_*.pdf
ANSWER_KEY_*.pdf
IGNORE_*.pdf
~~~

---

## Codex 本地安装

Codex 的用户级 skills 可以安装到：

~~~text
~/.agents/skills
~~~

安装本 skill：

~~~bash
mkdir -p ~/ai-skills
cd ~/ai-skills

git clone https://github.com/ruoyuguan/scientific-textbook-proofreading-skill.git

cd scientific-textbook-proofreading-skill
bash scripts/install_local.sh
~~~

安装脚本会创建软链接：

~~~text
~/.agents/skills/scientific-textbook-proofreading
~~~

后续更新：

~~~bash
cd ~/ai-skills/scientific-textbook-proofreading-skill
git pull --ff-only
~~~

因为安装的是软链接，所以拉取仓库最新版本后，本地 Codex skill 会自动同步更新。

如果 Codex 没有立即识别 skill，请重启 Codex。

---

## Claude Code 本地安装

Claude Code 的个人 skills 可以安装到：

~~~text
~/.claude/skills/<skill-name>/SKILL.md
~~~

同一个安装脚本也会为 Claude Code 安装本 skill：

~~~bash
cd ~/ai-skills/scientific-textbook-proofreading-skill
bash scripts/install_local.sh
~~~

安装脚本会创建软链接：

~~~text
~/.claude/skills/scientific-textbook-proofreading
~~~

后续更新：

~~~bash
cd ~/ai-skills/scientific-textbook-proofreading-skill
git pull --ff-only
~~~

如果 Claude Code 没有立即识别 skill，请重启 Claude Code。

---

## 推荐本地工作流

1. 本地安装 skill。
2. 创建一个本地 proofreading project。
3. 将待审教材和参考资料放入 `input/`。
4. 在项目目录中启动 Codex 或 Claude Code。
5. 要求 agent 使用 Local File Report Mode。
6. 查看 `reports/` 下生成的逐章报告。

示例：

~~~bash
python scripts/make_project_template.py ~/proofreading-projects/hea-review

cd ~/proofreading-projects/hea-review

# Put PDFs or TeX sources under input/
# input/UNDER_REVIEW_my_draft.pdf
# input/REFERENCE_Longair_High_Energy_Astrophysics.pdf

codex
~~~

然后提示：

~~~text
Please use the scientific-textbook-proofreading skill in Local File Report Mode.

File roles:

- Manuscript under review: input/UNDER_REVIEW_my_draft.pdf
- Authoritative reference source: input/REFERENCE_Longair_High_Energy_Astrophysics.pdf

Review Chapter 1. Do not print the full report in chat. Write the chapter report to reports/chapter_01_errata.md. If extraction quality is poor, write notes to reports/processing_notes.md.
~~~

---

## Evaluation Files

本仓库包含轻量级 eval 结构：

~~~text
evals/
├── cases.jsonl
└── golden/
    ├── case_001.md
    ├── case_002.md
    ├── ...
    └── case_012.md
~~~

`cases.jsonl` 包含正例和负例回归测试。`golden/` 目录包含每个 case 的参考输出。

这些不是完整自动科学评测，而是轻量级回归样例，用来在 skill 迭代时保持行为稳定，尤其是防止：

- 错误漏报；
- 正确内容误报；
- 输出格式漂移；
- 数学渲染污染；
- issue 类型失控。

运行基础检查：

~~~bash
python scripts/validate_schema.py
python scripts/lint_skill.py
python scripts/run_evals.py
python scripts/lint_markdown.py
python scripts/validate_examples.py
~~~

---

## Synthetic Example

本仓库包含一个可以公开测试的合成教材章节，不依赖任何受版权保护的 PDF：

~~~text
examples/synthetic_textbook/chapter_01.md
~~~

对应的期望输出包括 Markdown 和 JSON 两种格式：

~~~text
examples/expected_output/synthetic_chapter_01_errata.md
examples/expected_output/synthetic_chapter_01_errata.json
~~~

合成章节中故意包含若干科学问题：

- photon-energy formula 缺少 `c`；
- inverse-Compton/synchrotron ratio 缺少 Thomson-regime 限定；
- gamma-ray 观测表述过宽；
- 面积/体积量纲错误；
- 一个不应被报告为错误的 negative-control statement。

JSON 报告遵循：

~~~text
schemas/errata_report.schema.json
~~~

---

## Toward a Full Pipeline

本仓库目前提供 skill 和 local file workflow。未来完整 pipeline 可能包括：

1. PDF text extraction。
2. Formula extraction。
3. Chapter boundary detection。
4. Automatic chapter queue generation。
5. Per-chapter model calls。
6. Report validation against `schemas/errata_report.schema.json`。
7. Summary report aggregation。

推荐开发路径：

~~~text
Skill instructions
→ Local File Report Mode
→ Project template
→ Manual local-agent review
→ Semi-automated extraction scripts
→ Full pipeline
~~~

---

## 人工复核

输出结果应被视为供专家人工复核的候选勘误报告，而不是最终权威判断。

本 skill 旨在减少 false positives 和 false negatives，但不能保证完全正确。

特别需要人工复核：

- `confidence` 为 Medium / Low 的条目；
- `extraction_reliability` 为 medium / low 的条目；
- current-status claim；
- PDF 公式抽取不可靠的内容；
- 需要 visual inspection 的图表和公式。

---

## 版权说明

请不要将受版权保护的教材、私人手稿、未公开讲义或专有材料提交到本公开仓库。

用户应在运行时提供自己有合法访问权限的教材、参考资料和 PDF 文件。
