<template>
  <div class="home">
    <v-container>
      <v-row no-gutters>
        <v-col 
          cols="12" xs="12" sm="8" md="8" 
        >
          <v-card
            class="pa-2 mx-1 mt-2"
            outlined
            tile
          >
            <v-tabs
              v-model="tab"
            >
              <v-tab href="#tab-1">
                Calendar
              </v-tab>
              <v-tab href="#tab-2">
                Posts
              </v-tab>
              <v-tab href="#tab-3">
                Events
              </v-tab>
              <v-tabs-slider color="accent"></v-tabs-slider>
            </v-tabs>

            <v-tabs-items v-model="tab">
              <v-tab-item
                v-for="i in 3"
                :key="i"
                :value="'tab-' + i"
              >
                <v-card v-if="i == 1" flat>
                  <CalendarCom />
                </v-card>
                <v-card v-if="i == 2" flat>
                  <v-card-text>Posts</v-card-text>
                </v-card>
                <v-card v-if="i == 3" flat>
                  <v-card-text>Events</v-card-text>
                </v-card>
              </v-tab-item>
            </v-tabs-items>

          </v-card>
        </v-col>

        <v-col 
          cols="12" xs="12" sm="4" md="4"
        >
          <v-card
            class="pa-2 mx-1 mt-2"
            outlined
            tile
          >
            .col-6<br>Subsequent columns continue along the new line.
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import CalendarCom from '@/components/CalendarCom'

export default {
  name: 'HomepageView',
  components: { CalendarCom },
  data () {
    return {
      tab: null,
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }
  },
}
</script>