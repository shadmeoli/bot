<template>
  <!-- Filter -->
  <div style="{display: flex; align-items:center; position:relative; left: 11%;}" class="mt-15 ml-10">
    <v-btn dark icon @click="show = !show">
      <v-chip color="red magenta-3 " class="ml-10">
        <span>order</span>
        <v-icon color="black">{{ show ? 'mdi-food-fork-drink' : 'mdi-chat' }}</v-icon>
      </v-chip>
    </v-btn>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card max-width="70%">
          <v-card-title class="ml-2">
            Talk to me
          </v-card-title>
          <v-card-subtitle class="ml-2">
            FAQs ?
          </v-card-subtitle>


          <v-chip>{{ msg }}</v-chip>


          <v-card-actions>
            <v-text-field v-model="mine" @input="talkToMe()">
            </v-text-field>
            <v-btn v-on:click="talkToMe()" text>
              <v-icon slot="prepend" color="red">
                mdi-send-outline
              </v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>

      </div>
    </v-expand-transition>
  </div>

</template>

<script>

let msg;
export default {
  name: 'chat',

  data: () => ({
    show: false,
    msg: 'Hello there.',
    sent: false,
    mine: '',
  }),

  methods: {
    talkToMe() {
      this.mine = this.mine;
    }
  }
}
</script>
