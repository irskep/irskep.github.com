#let data = yaml("resume.yaml");

// FUNCTIONS

// Jankyparse the tiniest subset of HTML so I can render the same data as HTML very easily.
// Just converts <a> to #link and <br> to \.
#let html2typst = (text) => {
  let text = text
    .replace(regex("<br>\s+"), s => "\\\n")
    .replace(
      regex("[<]a href=\"([^\"]+)\"[>](.*?)[<]/a[>]"),
      s => 
          "#link(\"" +
          s.at("captures").at(0) +
          "\", \"" +
          s.at("captures").at(1) +
          "\")"
        )
  return eval("[" + text + "]")
}

// If an item has the same startDate and endDate, return a range string. Otherwise just return startDate.
#let date_range = (obj) => {
  if obj.startDate == obj.endDate {
    return obj.startDate
  } else {
    return [#obj.startDate–#obj.endDate]
  }
}

// GLOBAL STYLES

#set par(justify: true, leading: 4pt)
#set text(font: "Charter", size: 10pt)

#show heading.where(
  level: 2
): it => block(width: 100%, below: 20pt)[
  #line(length: 100%)
  #text(font: "Fira Sans", size: 12pt, weight: "regular", it.body)
]

#show heading.where(
  level: 3
): it => block(width: 100%, below: 0pt)[
  #text(font: "Charter", size: 11pt, weight: "bold", it.body)
]

#show heading.where(
  level: 4
): it => block(width: 100%, above: 0pt, below: 11pt)[
  #set par(justify: false, leading: 4pt)
  #text(font: "Charter", size: 10pt, weight: "extralight", style: "italic", it.body)
]

// LAYOUT HELPERS

#let split(_l, _r) = block(
  width: 100%,
  below: 6pt,
  grid(columns: (1fr, auto), align(left, _l), align(bottom, _r)))
#let split_project(_l, _r) = grid(
  columns: (1fr, auto),
  align(left, _l),
  align(bottom, text(size: 11pt, _r)))

#grid(
  columns: (1fr, auto),
    align(left)[= #text(font: "Fira Sans", size: 22pt, weight: "regular")[#data.basics.name]],
  align(right)[
    #data.basics.location.city \
    #link("mailto:#data.basics.email", data.basics.email) \
    #link(data.basics.url, data.basics.url)
  ])

// CONTENT

== Role Fit <role-fit>
#html2typst(data.basics.summary)

== Work History <work-history>
#columns(2)[
  #for job in data.work [
    #split([=== #job.name], date_range(job))
    ==== #html2typst(job.position)
    #html2typst(job.summary)
    #if "breakAfter" in job and job.at("breakAfter") [#colbreak()]
  ]

  == Education
  #for ed in data.education [
    #split([=== #ed.institution], date_range(ed))
    #html2typst(ed.summary)
  ]
]

#pagebreak()

== Personal Projects
#for project in data.projects [
  #split_project([=== #project.name], emph[#project.url (#date_range(project))])
  #html2typst(project.description)
]

== Skills for the Keyword Filters
#show heading.where(
  level: 3
): it => block(width: 100%, below: 11pt)[
  #text(font: "Charter", size: 11pt, weight: "bold", it.body)
]

#grid(
  columns: (1fr, 1fr),
  gutter: 11pt,
  ..data.skills.map(skillset => [
    === #skillset.name
    
    #skillset.keywords.join(", ")
    
    #if "text" in skillset {
      [#html2typst(skillset.at("text"))]
    }
  ])
)

#for appendix in data.appendices [
  == #appendix.title
  
  #columns(2)[#html2typst(appendix.text)]
]