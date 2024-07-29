#!/usr/bin/env zsh
source .env
curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_GIST_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/gists/$GITHUB_GIST_ID \
  --data '@resume/resume.github.json' > /dev/null
