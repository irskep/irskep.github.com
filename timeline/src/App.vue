<template>
  <main>
    <h1>My time at Asana so far</h1>
    <div class="timeline">
      <TimelineItem
        v-for="item in items"
        :key="item[1]"
        :cls="item[3]"
        :title="item[1]"
        :text="item[2]"
        :date="item[0]"
      />
    </div>
  </main>
</template>

<script>
import TimelineItem from "./components/TimelineItem.vue";

export default {
  name: "App",
  components: {
    TimelineItem,
  },
  data: function () {
    return {
      items: [
        [
          "April 2018",
          "Joined the company",
          `After 2.5 years at <a href='https://blog.steveasleep.com/my-time-at-hipmunk'>Hipmunk</a>,
          I joined Asana as the manager of the iOS team.`,
        ],
        [
          "August 2018",
          "<a href='https://asana.github.io/Drawsana/'>Drawsana</a>",
          `Before Apple released PencilKit, we needed a way to let users draw
          annotations on top of images. I wrote Drawsana, an extensible open
          source library for image annotation, drawing on my experience making
          <a href='http://literallycanvas.com'>Literally Canvas</a>.`,
          "m-right",
        ],
        [
          "December 2018",
          "Milestone feature",
          `I implemented Asana's <a href='https://asana.com/guide/help/premium/milestones'>Milestone</a>
          feature in the iOS app. A milestone is a task with special properties.
          It was the first time we added a second type of task.`,
          "m-right",
        ],
        [null, "2018", null, "m-yeardivider"],

        // 2019
        [
          "January 2019",
          "Started managing the Android team",
          `I filled in as manager for the Android team after some internal
          staffing changes. By the time we found a replacement, I was supporting
          twelve reports.`,
        ],
        [
          "January 2019",
          "Started helping with the intern program",
          `As part of Asana’s intern program, I helped facilitate interview huddles, match
          mentors and teams with individual interns, and work with our Talent Acquisition
          team on timelines and staffing.`,
        ],
        [
          "January 2019",
          "Took ownership of open source at Asana",
          `Drawing on my experience working on open source projects since college,
          I got the <a href='https://wavelength.asana.com/workstyle-aors/'>AOR</a>
          for producing open source software, helping other engineers polish their
          projects for release and promoting open source within the company.`,
        ],
        [
          "February 2019",
          "Took ownership of the engineering blog",
          `There was an internal search for someone to contribute to running the engineering
          blog. For the next couple of years, I collaborated with folks across Engineering,
          Employer Brand, and Talent Acquisition to make sure we consistently published articles
          to the blog that served the needs of various parts of Asana.`,
        ],
        [
          "February-November 2019",
          "Didn’t do anything technical",
          `Twelve reports is a lot, and I took on a lot of new responsibilities early
          in the year.`,
          "m-right",
        ],
        [
          "August 2019",
          "Stopped managing the Android team",
          `We internally promoted someone to manage the Android team, and he's still
          doing a great job.`,
        ],
        [
          "September 2019",
          "Started working on “Mobile Self-Serve”",
          `We were having a tough time hiring mobile engineers, so we experimented with
          training engineers on partner teams in how to make mobile changes on their own.
          I took this on because it didn’t have a clear owner, and worked hard on it for
          the next couple years, but ultimately it didn’t result in a good ROI.`,
        ],
        [null, "2019", null, "m-yeardivider"],

        // 2020
        [
          "January 2020",
          "Approvals feature",
          `I implemented Asana’s <a href='https://asana.com/guide/help/premium/approvals'>Approvals</a>
          feature in the iOS app. Like Milestones, an Approval is a special type of task.`,
          "m-right",
        ],
        [
          "February 2020",
          "Stopped working with the intern program",
          `I didn’t have enough bandwidth to keep working on the intern program, so
          I handed off my responsibilities to someone else.`,
        ],
        [
          "March 2020",
          "Transitioned to Staff Engineer",
          `Being a manager wasn’t what I wanted out of my career, so I asked to
          switch to an iOS-focused IC role. We were reorganizing from iOS/Android/Server
          mobile teams to cross-functional mobile teams, and I ended up with
          Mobile Foundations.`,
        ],
        [
          "March 2020",
          "Do Not Disturb feature",
          `I implemented a complex UI to let users choose time ranges to not receive
          notifications. As part of this project, I created a framework for building
          similar UIs that made implementing later features much easier for both myself
          and other engineers.`,
          "m-right",
        ],
        [
          "June 2020",
          "Invites feature",
          `Using the framework I developed for Do Not Disturb, I implemented another
          complex UI for inviting new users to individual tasks, projects, portfolios,
          and more.`,
          "m-right",
        ],
        [
          "August 2020",
          "Goals feature",
          `I built a new screen to display <a href='https://asana.com/guide/help/premium/goals'>Goals</a>,
          Asana’s goal-tracking system.`,
          "m-right",
        ],
        [null, "2020", null, "m-yeardivider"],

        // 2021
        [
          "January 2021",
          "Appreciations feature",
          `I implemented <a href='https://blog.asana.com/2020/06/appreciations/'>Appreciations</a>
          on iOS, including a custom picker that appears in the keyboard area.`,
          "m-right",
        ],
        [
          "February 2021",
          "Joined the Content Experience team",
          `In 2019, I learned that Asana was planning to rewrite its text editor, and I
          got involved in the design process to ensure there would continue to be a great
          mobile experience. By February 2021, this project was in full swing, and I
          joined to lay a strong foundation for the mobile component and help train
          engineers on the team in how to combine web and native mobile technology
          effectively.`,
        ],
        [
          "February-August 2021",
          "Prototyped a web-based mobile text editor",
          `Leveraging my experience at Graffiti Labs and Hipmunk, I designed
          and built an iOS and Android text editor that uses a web view but
          feels like a native control, to enable mixed media in task descriptions
          and enable fast iteration.`,
          "m-right",
        ],
        [
          "April 2021",
          "Sent Mobile Self-Serve to go live on a farm",
          `After two years of trying to train engineers around Asana on mobile
          and make our code friendly to them, we decided that the costs weren’t
          worth the investments and shut the program down.`,
        ],
        [
          "August 2021",
          "Switched back to the Mobile Foundations team",
          `My time on Content Experience was always intended to be temporary, and
          it came to an end in August. I switched back to Mobile Foundations to work on
          the overall mobile developer experience.`,
        ],
        [
          "August 2021",
          "Untangled service dependencies",
          `Like many iOS codebases, Asana’s contained many global singletons that
          depended on each other in hard-to-understand ways. I refactored a lot of
          code so we could use dependency injection throughout the app and have a
          clear initialization order among our dozens of services.`,
          "m-right",
        ],
        [
          "September 2021",
          "Locheck",
          `After a bad string translation caused a severe runtime crash, I realized it would
          be possible to write a linter for iOS and Android localization files. The
          result was the open source tool
          <a href='https://blog.asana.com/2021/09/locheck-open-source/'>Locheck</a>,
          which is now used by companies including GitHub.`,
          "m-right",
        ],
        [
          "November 2021",
          "Handed off responsibility for open source",
          `After almost two years, I had done everything I had set out to do with
          the open source program, and gave the responsibility to someone with
          more energy for it.`,
        ],
        [null, "2021", null, "m-yeardivider"],

        // 2022
        [
          "February 2022",
          "Mobilegen",
          `A recurring problem within the Asana mobile team has been the
          datastore schema differing between the iOS and Android apps. To
          enable a long-term solution to this problem, I wrote a code
          generator for iOS and Android code called Mobilegen. This is a big
          topic and I haven’t written about it publicly yet, so please ask me
          about it.`,
          "m-right",
        ],
        [
          "June 2022",
          "Handed off Mobilegen",
          `By June, I had ironed out most of the workflow issues with Mobilegen
          and helped two other engineers learn how to effectively update it. By
          this time, all mobile engineers were comfortable using Mobilegen to make
          data model changes.`,
          "m-right",
        ],
        [
          "June 2022",
          "Evolved how Asana’s engineering blog operated",
          `After owning the engineering blog for 3 years, some internal changes
          spurred me to think critically about how I was running it. As a result,
          I brought in three new people to help me manage and evolve it.`,
        ],
        [
          "July 2022",
          "Engineering-wide documentation improvements",
          `Asana’s engineering docs are mostly Markdown files in the GitHub
          monorepo. GitHub’s UI for browsing Markdown has some issues, so as
          a hackathon project, I experimented with rendering our internal docs
          using <a href='https://squidfunk.github.io/mkdocs-material/'>Material
          for Mkdocs</a>. It quickly became the canonical way for Asana
          engineers to browse internal documentation.`,
          "m-right",
        ],
        [
          "July 2022",
          "Tuist migration",
          `We wanted to start breaking the codebase into modules. The only way
          to effectively do this at scale is to add a lot of automation, which
          requires using an Xcode project generation tool like
          <a href='https://tuist.io'>Tuist</a>. Over the course of a week, I
          painstakingly converted our project file to a Tuist manifest.`,
          "m-right",
        ],
        [
          "August 2022",
          "Took back responsibility for open source",
          "The guy I handed it off to quit. Dang.",
          null,
        ],
        [
          "August 2022",
          "Migrated translation management backends",
          `Built a deep understanding of Xcode's translation tools and the
            XLIFF format in order to move from a decent translation management
            system to a crappy one to theoretically save the company money.`,
          "m-right",
        ],
        [
          "September-December 2022",
          "Cut build times by 80% using modules",
          `I led efforts by the Mobile Foundations team to leverage <a href="https://tuist.io">Tuist</a> to
          split our app into feature modules, by refactoring code, writing
          developer-facing tools, and helping educate the wider mobile team.
          As a result, most engineers wait 5 seconds instead of 45 seconds for
          rebuilds when making incremental changes, and make new feature
          modules on their own. I blogged about it—<a href="https://blog.asana.com/2023/02/scaling-a-mature-ios-codebase-with-tuist/">Read more here!</a>`,
          "m-right",
        ],
        [
          "February-July 2023",
          "Drove the redesign of the iOS Home tab",
          `I worked with a small team in a hackathon to present a new vision
          for how to use one of our top 3 most visited tabs in the mobile app.
          This kicked off a project to take the concept to production, which
          is still in progress.`,
          "m-right",
        ],
      ],
    };
  },
};
</script>

<style>
/*! minireset.css v0.0.6 | MIT License | github.com/jgthms/minireset.css */
html,
body,
p,
ol,
ul,
li,
dl,
dt,
dd,
blockquote,
figure,
fieldset,
legend,
textarea,
pre,
iframe,
hr,
h1,
h2,
h3,
h4,
h5,
h6 {
  margin: 0;
  padding: 0;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  font-size: 100%;
  font-weight: normal;
}
ul {
  list-style: none;
}
button,
input,
select {
  margin: 0;
}
html {
  box-sizing: border-box;
}
*,
*::before,
*::after {
  box-sizing: inherit;
}
img,
video {
  height: auto;
  max-width: 100%;
}
iframe {
  border: 0;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

h1 {
  font-size: 2rem;
  font-weight: bold;
  padding: 1rem;
  text-align: center;
}

.Timeline {
  width: 100%;
  min-height: 100vh;
  background-color: #eaeaec;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: fill;
}
</style>
