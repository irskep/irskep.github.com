$ = jQuery

$ ->
  load_repos()

load_repos = () ->
  $.getJSON(
    'https://api.github.com/users/irskep/repos?callback=?',
    jsonp=populate_repos)

populate_repos = (response) ->
  $('#github-loading').remove()
  shown_repo_names = [
    'Space-Train',
    'steveasleep',
    'zhang-shasha',
    'lizardwizard',
    'kod',
    'thesis_papers',
    'ct',
    'mrjob',
    'boto',
    'Tron',
    'irskep_dotfiles',
    'splatterboard',
    'jist',
    'rum',
    'regex_compiler'
  ]

  shown_repos = []
  for repo in response.data
    if shown_repo_names.indexOf(repo.name) != -1
      shown_repos.push(repo)

  shown_repos.sort((a, b) -> b.updated_at.localeCompare(a.updated_at))

  for repo in shown_repos
    $('.github').append("
    <div class=\"github-item\" id=\"repo-#{repo.name}\">
      <h2><a href=\"#{repo.html_url}\">#{repo.name}</a></h2>
      <p class=\"github-description\">#{repo.description}</p>
      <span class=\"github-forks\">#{repo.forks} forks</span><br>
      <span class=\"github-watchers\">#{repo.watchers} watchers</span><br>
    </div>")

  for repo in shown_repos
    if repo.fork
      $.getJSON(
        "https://api.github.com/repos/irskep/#{repo.name}?callback=?",
        jsonp=rewrite_repo
      )

rewrite_repo = (response) ->
  elem = $("#repo-#{response.data.name}")
  for child in elem.children()
    $(child).remove()

  repo = response.data

  elem.append("
    <h2><a href=\"#{repo.parent.html_url}\">#{repo.parent.name}</a></h2>
    <p class=\"github-description\">#{repo.parent.description}</p>
    <span class=\"github-forks\">#{repo.parent.forks} forks</span><br>
    <span class=\"github-watchers\">#{repo.parent.watchers} watchers</span><br>")
