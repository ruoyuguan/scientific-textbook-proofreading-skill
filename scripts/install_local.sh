#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/ruoyuguan/scientific-textbook-proofreading-skill.git"
BASE_DIR="${HOME}/ai-skills"
REPO_DIR="${BASE_DIR}/scientific-textbook-proofreading-skill"
SKILL_NAME="scientific-textbook-proofreading"

mkdir -p "${BASE_DIR}"

if [ -d "${REPO_DIR}/.git" ]; then
  echo "Updating existing repository..."
  git -C "${REPO_DIR}" pull --ff-only
else
  echo "Cloning repository..."
  git clone "${REPO_URL}" "${REPO_DIR}"
fi

if [ ! -f "${REPO_DIR}/skill/SKILL.md" ]; then
  echo "Error: ${REPO_DIR}/skill/SKILL.md not found."
  exit 1
fi

mkdir -p "${HOME}/.agents/skills"
mkdir -p "${HOME}/.claude/skills"

ln -sfn "${REPO_DIR}/skill" "${HOME}/.agents/skills/${SKILL_NAME}"
ln -sfn "${REPO_DIR}/skill" "${HOME}/.claude/skills/${SKILL_NAME}"

echo "Installed skill for Codex:"
echo "  ${HOME}/.agents/skills/${SKILL_NAME}"

echo "Installed skill for Claude Code:"
echo "  ${HOME}/.claude/skills/${SKILL_NAME}"

echo "To update later, run:"
echo "  cd ${REPO_DIR} && git pull --ff-only"

echo "Done. Restart Codex or Claude Code if the skill does not appear immediately."
