(function() {
  var $, load_repos, populate_repos, rewrite_repo;

  $ = jQuery;

  $(function() {
    return load_repos();
  });

  load_repos = function() {
    var jsonp;
    return $.getJSON('https://api.github.com/users/irskep/repos?callback=?', jsonp = populate_repos);
  };

  populate_repos = function(response) {
    var jsonp, repo, shown_repo_names, shown_repos, _i, _j, _k, _len, _len2, _len3, _ref, _results;
    $('#github-loading').remove();
    shown_repo_names = ['Space-Train', 'steveasleep', 'zhang-shasha', 'lizardwizard', 'kod', 'thesis_papers', 'ct', 'mrjob', 'boto', 'Tron', 'irskep_dotfiles', 'splatterboard', 'jist', 'rum', 'regex_compiler'];
    shown_repos = [];
    _ref = response.data;
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      repo = _ref[_i];
      if (shown_repo_names.indexOf(repo.name) !== -1) shown_repos.push(repo);
    }
    shown_repos.sort(function(a, b) {
      return b.updated_at.localeCompare(a.updated_at);
    });
    for (_j = 0, _len2 = shown_repos.length; _j < _len2; _j++) {
      repo = shown_repos[_j];
      $('.github').append("    <div class=\"github-item\" id=\"repo-" + repo.name + "\">      <h2><a href=\"" + repo.html_url + "\">" + repo.name + "</a></h2>      <p class=\"github-description\">" + repo.description + "</p>      <span class=\"github-forks\">" + repo.forks + " forks</span><br>      <span class=\"github-watchers\">" + repo.watchers + " watchers</span><br>    </div>");
    }
    _results = [];
    for (_k = 0, _len3 = shown_repos.length; _k < _len3; _k++) {
      repo = shown_repos[_k];
      if (repo.fork) {
        _results.push($.getJSON("https://api.github.com/repos/irskep/" + repo.name + "?callback=?", jsonp = rewrite_repo));
      } else {
        _results.push(void 0);
      }
    }
    return _results;
  };

  rewrite_repo = function(response) {
    var child, elem, repo, _i, _len, _ref;
    elem = $("#repo-" + response.data.name);
    _ref = elem.children();
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      child = _ref[_i];
      $(child).remove();
    }
    repo = response.data;
    return elem.append("    <h2><a href=\"" + repo.parent.html_url + "\">" + repo.parent.name + "</a></h2>    <p class=\"github-description\">" + repo.parent.description + "</p>    <span class=\"github-forks\">" + repo.parent.forks + " forks</span><br>    <span class=\"github-watchers\">" + repo.parent.watchers + " watchers</span><br>");
  };

}).call(this);
