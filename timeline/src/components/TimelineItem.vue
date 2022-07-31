<template>
  <div class="TimelineItem" :class="cls">
    <div class="TimelineItem_Line"></div>
    <div class="TimelineItem_Dot"></div>
    <div class="TimelineItem_ContentWrapper">
      <div class="TimelineItem_Content">
        <h2 v-html="title" class="TimelineItem_Title"></h2>
        <p v-html="text"></p>
      </div>
    </div>
    <div class="TimelineItem_Date">{{ date }}</div>
  </div>
</template>

<script>
export default {
  name: "TimelineItem",
  props: {
    cls: String,
    title: String,
    text: String,
    date: String,
  },
};
</script>

<style>
.TimelineItem {
  position: relative;
}

.TimelineItem_Line {
  position: absolute;
  top: 0;
  bottom: 0;
  left: calc(50% - 2px);
  width: 2px;
  background-color: lightgray;
}

.TimelineItem_Dot {
  position: absolute;
  top: 2rem;
  left: calc(50% - 12px);
  border-radius: 12px;
  width: 22px;
  height: 22px;
  background-color: red;
  border: 4px solid lightgray;
}
.m-right .TimelineItem_Dot {
  background-color: blue;
}

.TimelineItem_Date {
  position: absolute;
  top: 2rem;
  left: calc(50% + 12px + 1.5rem);
}
.m-right .TimelineItem_Date {
  left: auto;
  right: calc(50% + 12px + 1.5rem);
  text-align: right;
}

.TimelineItem_ContentWrapper {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: row-reverse;
  padding-top: 2rem;
  padding-left: calc(12px + 1rem);
  padding-right: calc(12px + 1rem);
}
.m-right .TimelineItem_ContentWrapper {
  flex-direction: row;
  margin-left: 50%;
}

.TimelineItem_Content {
  background-color: white;
  max-width: 20rem;
  padding: 0 0.5rem 0.5rem 0.5rem;
}

.TimelineItem_Content h2 {
  font-weight: bold;
  margin-bottom: 0.5rem;
}
</style>
