<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->

  <div>
    <v-card>
      <v-list-item-content
        class="justify-center py-6"
        style="background-color: #16cccc; height : 300px"
      >
        <v-list-item-title class="font-weight-black display-3 font-italic" align="center"></v-list-item-title>
        <v-list-item-title
          style="text-shadow: 0 0 2px #000;font-size: 3em;color:white"
          align="center"
        >
          <v-icon size="70" class="mr-2" color="white">mdi-magnify</v-icon>SEARCH PAGE
        </v-list-item-title>
        <v-list-item-title class="font-weight-bold" style="font-size:30px" align="center">
          <b style="color:white">{{this.$route.query.word}}</b> 을(를) 검색한 결과입니다.
          <v-icon color="white" x-large>mdi-clipboard-play-multiple-outline</v-icon>
        </v-list-item-title>
        <v-list-item-title
          v-if="searchFlag"
          class="font-weight-bold"
          style="font-size:30px; color:red"
          align="center"
        >한글자 이상 검색해주세요!</v-list-item-title>
      </v-list-item-content>
    </v-card>

    <v-container>
      <!--youtuber-->
      <v-container wrap style="background : white" border class="my-3">
        <v-row class="pt-0 pl-3">
          <v-col>
            <h1 class="font-weight-light mb-1">Youtuber</h1>
            <v-divider></v-divider>
          </v-col>
        </v-row>

        <v-container v-if="displayyoutuber.length == 0">
          <v-hover v-slot:default="{ hover }" open-delay="50">
            <v-card :elevation="hover ? 7 : 0" flat class="my-3 mx-3" shaped>
              <v-list-item-content
                class="justify-center py-6"
                style="background-color:#cdcdcd ; height : 250px"
              >
                <v-list-item-title class="font-weight-ligth" style="font-size:20px" align="center"></v-list-item-title>
                <v-list-item-title class="font-weight-black" align="center" style="font-size:25px">
                  <v-icon color="red" x-large>mdi-alert-circle</v-icon>검색어에 해당하는 유튜버가 없습니다.
                </v-list-item-title>
                <v-list-item-title
                  class="font-weight-ligth"
                  style="font-size:20px"
                  align="center"
                >유튜버를 추가하고 싶으신가요?</v-list-item-title>
                <v-row align="center">
                  <v-spacer></v-spacer>
                  <inputComponent position="search" v-if="$session.get('token') != undefined"></inputComponent>
                  <span
                    v-else
                    class="font-weight-bold"
                    style="font-size:20px; color:red"
                  >유튜버를 추가하고 싶으시다면 로그인을 해주세요.</span>
                  <v-spacer></v-spacer>
                </v-row>
              </v-list-item-content>
            </v-card>
          </v-hover>
        </v-container>
        <v-container v-else>
          <v-hover
            v-slot:default="{ hover }"
            open-delay="50"
            v-for="(item,i) in displayyoutuber"
            :key="i"
          >
            <v-card
              :elevation="hover ? 7 : 0"
              outlined
              flat
              @click="gotoYoutuberPage(item.yno)"
              class="my-3 mx-3"
              shaped
            >
              <v-row align="center">
                  <!-- thumbnail -->
                  <v-col class="ma-0 py-5 pr-0" cols="2" align="center">
                    <!-- <p class="title">{{ i + 1 }}위</p> -->
                    <!-- </v-col>
                    <v-col class="pr-0" cols="1" align="center">-->
                    <v-img
                      class="circle"
                      :src="item.thumbnails"
                      flat
                      :aspect-ratio="1 / 1"
                      width="110px"
                    />
                  </v-col>
                  <v-divider vertical class="pl-0 mr-2"></v-divider>
                  <!-- 유튜버 설명 -->
                  <v-col cols="7" class="pl-1 pr-0 pt-1 pb-0 ml-5 mr-0 mt-5">
                    <v-row align="center">
                      <v-col cols="12" class="pt-0 pb-1 pl-1">
                        <p
                          class="font-weight-black thin display-1 ma-0 text-truncate"
                        >{{ item.channelName }}</p>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col cols="12" class="pt-0 pb-0 pl-1">
                        <p
                          class="font-weight-light thin ma-0 pa-0"
                          style="font-size:13px"
                        >개설일 : {{ item.publishedDate }}</p>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col class="px-2 pl-1 py-0">
                        <table style="text-align: center; width: 100%; margin-top: 15px;">
                          <tr id="th1">
                            <td>구독자수</td>
                            <td>총 조회수</td>
                            <td>총 영상수</td>
                          </tr>
                          <tr>
                            <td>{{ tc(item.subscriber) }}</td>
                            <td>{{ tc(item.totalViewCount) }}</td>
                            <td>{{ item.totalVideoCount }}</td>
                          </tr>
                        </table>
                        <!-- <p id="subtitle" class="mt-1 mb-0"></p> -->
                      </v-col>
                      <v-col class="px-2 py-0">
                        <table style="text-align: center; width: 100%; margin-top: 15px;">
                          <tr id="th2">
                            <td>영향력</td>
                            <td>활동력</td>
                            <!-- <td>조회수력</td>
                            <td>구독자력</td>-->
                            <td>호감도</td>
                          </tr>
                          <tr>
                            <td>{{ item.influence }}점</td>
                            <td>{{ item.activity }}점</td>
                            <td>{{ item.charm }}점</td>
                          </tr>
                        </table>
                        <p
                          id="subtitle"
                          class="mt-1 mb-2 mb-0 ml-1"
                        >*위 3개 수치는 100점 만점으로 환산한 점수입니다.</p>
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-divider vertical class="pl-5 ml-3 mr-0 pl-2"></v-divider>
                  <!-- 등급 -->
                  <v-col cols="2" style="text-align: center">
                    <v-row align="center" class="ma-0 px-2">
                      <v-col class="px-0 pt-1 pb-0">
                        <p class="font-weight-bold">&nbsp;&nbsp;GRADE</p>
                      </v-col>
                    </v-row>
                    <v-divider class="ma-0 pa-0"></v-divider>
                    <v-row>
                      <v-col class>
                        <v-btn
                          class="ma-0"
                          fab
                          dark
                          large
                          :color="setGradeColor(item.grade)"
                          height="90px"
                          width="90px"
                        >
                          <v-icon large dark>{{ setGrade(item.grade) }}</v-icon>
                        </v-btn>
                      </v-col>
                    </v-row>
                  </v-col>
              </v-row>
            </v-card>
          </v-hover>
        </v-container>
        <v-row>
          <v-col align="center">
            <v-btn text color="black" @click="youtuberPageDown">
              <v-icon>mdi-menu-down</v-icon>더보기
            </v-btn>
          </v-col>
        </v-row>
      </v-container>

      <!-- video -->
      <!-- 최신동영상 -->
      <v-container wrap style="background : white" border class="my-3">
        <v-row class="pt-0 pl-3">
          <v-col>
            <h1 class="font-weight-light mb-1">Video</h1>
            <v-divider></v-divider>
          </v-col>
        </v-row>
        <v-row class="mx-3">
          <v-hover
            v-slot:default="{ hover }"
            open-delay="50"
            v-for="(item,i) in displayvideo"
            :key="i"
          >
            <v-col cols="4" class="px-1">
              <v-card height="480px">
                <v-container class="pa-2">
                  <v-row>
                    <v-col>
                      <v-list-item-content class="py-0">
                        <iframe
                          :src="String('https://www.youtube.com/embed/')+item.videoID"
                          frameborder="0"
                          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                          allowfullscreen
                        ></iframe>
                      </v-list-item-content>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="pt-0">
                      <p class="text-truncate title mb-0 pl-1"><b>{{item.videoName}}</b></p>
                      <!-- <v-row class="pa-0 ma-0"> -->
                      <p
                        style="font-size: 13px; float:left" class="mt-1 mb-5 pl-1"
                      >게시일 : {{item.regDate}} </p>
                      <p style="font-size: 13px; float:right" class="mt-1 mb-5 pl-1">조회수 : {{tc(item.videoViewCount)}} 회</p>
                      <!-- </v-row> -->
                      
                      <br>
                      <hr class="mb-3 px-2">
                      <p
                        v-html="item.videoDescription.substring(0,120).concat('...')"
                        class="font-weight-light pl-1 mb-0" style="font-size: 0.9em"
                      >
                      </p>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-btn
                        v-for="(tag,index) in item.tags"
                        :key="index"
                        rounded
                        color="#5edaef"
                        dark
                        class="ma-1"
                        @click="search(tag)"
                      >{{tag}}</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>
            </v-col>
          </v-hover>
        </v-row>

        <v-row>
          <v-col align="center">
            <v-btn text color="black" @click="videoPageDown">
              <v-icon>mdi-menu-down</v-icon>더보기
            </v-btn>
          </v-col>
        </v-row>
      </v-container>

      <!-- news -->
      <v-container wrap style="background : white" border class="my-3">
        <v-row class="pt-0 pl-3">
          <v-col>
            <h1 class="font-weight-light mb-1">News</h1>
            <v-divider></v-divider>
          </v-col>
        </v-row>
        <v-hover
          v-slot:default="{ hover }"
          open-delay="50"
          v-for="(item,i) in displaynews"
          :key="i"
        >
          <v-card :elevation="hover ? 7 : 0" outlined flat class="my-3 mx-3" shaped>
            <!-- 타이틀 -->
            <v-row>
              <v-col class="mx-5">
                <v-row>
                  <v-col cols="12" class="pb-0">
                    <a
                      target="_blank"
                      :href="item.newsLink"
                      v-html="item.newsTitle"
                      class="font-weight-black thin title ma-0 text-truncate"
                    ></a>
                  </v-col>
                </v-row>
                <!-- 게시 날짜 -->
                <v-row>
                  <v-col cols="12" class="py-0">
                    <p
                      class="font-weight-light thin ma-0"
                      style="font-size:13px"
                    >개설일 : {{item.newsDate}}</p>
                  </v-col>
                </v-row>
                <!-- 뉴스 설명 -->
                <v-row>
                  <v-col cols="12" class="py-1">
                    <span v-html="item.newsDescription"></span>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
        <v-row>
          <v-col align="center">
            <v-btn text color="black" @click="newsPageDown">
              <v-icon>mdi-menu-down</v-icon>더보기
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-container>
  </div>
</template>


<script>
import http from "../vuex/http-common";
import axios from "axios";
import tc from "thousands-counter";
import inputComponent from "../components/inputComponent";

export default {
  components: {
    inputComponent
  },
  name: "searchPage",

  methods: {
    setGradeColor(num) {
      if (typeof num == "undefined") {
        return "gray";
      }
      if (num >= 95) {
        return "red";
      } else if (num >= 90) {
        return "orange";
      } else if (num >= 80) {
        return "yellow";
      } else if (num >= 50) {
        return "green";
      } else if (num >= 20) {
        return "blue";
      } else {
        return "gray";
      }
    },
    gotoYoutuberPage: function(yno) {
      this.dialog = false;
      this.$vuetify.goTo(0);
      this.$router.push({ path: "/youtuberPage", query: { yno: yno } });
      this.$vuetify.goTo(0);
    },
    setGrade(num) {
      if (num >= 95) {
        return "SS";
      } else if (num >= 90) {
        return "S";
      } else if (num >= 80) {
        return "A";
      } else if (num >= 50) {
        return "B";
      } else if (num >= 20) {
        return "C";
      } else {
        return "D";
      }
    },
    tc(num) {
      return tc(num);
    },
    youtuberPageDown() {
      this.pageyoutuber++;
      if (this.searchedyoutuber.length + this.range > this.pageyoutuber * 3) {
        this.displayyoutuber = this.searchedyoutuber.slice(
          0,
          this.pageyoutuber * this.range
        );
      } else {
        alert("유튜버 검색 결과의 끝 페이지입니다.");
      }
    },
    newsPageDown() {
      this.pagenews++;
      if (this.searchednews.length + this.range > this.pagenews * 3) {
        this.displaynews = this.searchednews.slice(
          0,
          this.pagenews * this.range
        );
      } else {
        alert("뉴스 검색 결과의 끝 페이지입니다.");
      }
    },
    videoPageDown() {
      this.pagevideo++;
      console.log(this.pagevideo + " " + this.searchednews.length);
      if (this.searchedvideo.length + this.range > this.pagevideo * 3) {
        this.displayvideo = this.searchedvideo.slice(
          0,
          this.pagevideo * this.range
        );
      } else {
        alert("비디오 검색 결과의 끝 페이지입니다.");
      }
    },
    failCallback() {
      window.location.reload();
    },
    search: function(keyword) {
      this.$router.push(
        {
          path: "/searchPage",
          query: { word: keyword }
        },
        () => {}
      );
    }
  },
  mounted() {
    this.$vuetify.goTo(0);
    var keyword = this.$route.query.word
    var keywordIndex = keyword.indexOf('/')
    if(keywordIndex != -1){
      keyword = keyword.substring(0,keywordIndex)
    }
    const youtuberSearch = new Promise((resolve, reject) => {
      http
        .get("/youtuber/search/" + encodeURIComponent(keyword))
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });

    const newsSearch = new Promise((resolve, reject) => {
      http
        .get("/news/search/" + encodeURIComponent(keyword))
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });

    const videoSearch = new Promise((resolve, reject) => {
      http
        .get("/video/search/" + encodeURIComponent(keyword))
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });

    Promise.all([youtuberSearch, newsSearch, videoSearch]).then(
      axios.spread((...responses) => {
        if (this.$route.query.word == undefined) {
          this.displayyoutuber = [];
          this.displaynews = [];
          this.displayvideo = [];
          this.searchFlag = true;
          return;
        }
        for (let index = 0; index < responses.length; index++) {
          if (responses[index].data.state != "ok") {
            if (this.$route.query.word.split(" ").join("") != "") {
              this.failCallback();
              return;
            } else {
              this.displayyoutuber = [];
              this.displaynews = [];
              this.displayvideo = [];
              this.searchFlag = true;
              return;
            }
          }
        }

        this.searchedyoutuber = responses[0].data.data;
        this.displayyoutuber = this.searchedyoutuber.slice(0, 3);
        this.searchednews = responses[1].data.data;
        this.displaynews = this.searchednews.slice(0, 3);
        this.searchedvideo = responses[2].data.data;
        for (let index = 0; index < this.searchedvideo.length; index++) {
          var tags = [];
          var tagss = this.searchedvideo[index].tags.split(",");
          var count = 0;
          for (let i = 0; i < tagss.length; i++) {
            if (count >= 3) {
              break;
            }
            if (tagss[i].length > 20) {
              continue;
            } else {
              tags.push(tagss[i]);
              count++;
            }
          }
          this.searchedvideo[index].tags = tags;
        }
        this.displayvideo = this.searchedvideo.slice(0, 3);

      })
    );
  },
  computed: {},
  watch: {},
  data() {
    return {
      searchedyoutuber: [],
      searchednews: [],
      searchedvideo: [],
      displayyoutuber: [],
      displaynews: [],
      displayvideo: [],
      pageyoutuber: 1,
      pagenews: 1,
      pagevideo: 1,
      range: 6,
      searchFlag: false
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Do+Hyeon|Nanum+Gothic|Noto+Sans+KR&display=swap");
* {
  font-family: "Noto Sans KR", sans-serif;
}
#subtitle {
  float: right;
  color: gray;
  font-size: 12px;
}
.circle {
  border-radius: 50%;
}
td {
  border: 1px solid lightgray;
}
#th1 {
  background-color: #0d9090a3;
  color: white;
}
#th2 {
  background-color: #239494;
  color: white;
}
</style>
