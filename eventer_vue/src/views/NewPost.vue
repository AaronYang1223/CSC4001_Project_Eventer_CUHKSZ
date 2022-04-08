<template>
  <div>
    <v-card>
      <v-row>
        <!-- 标题 -->
        <v-text-field
          type="text" 
          label="Topic"
          v-model="topic"
          id="inputTopic"
          :rules="[rules.required]"
        >
        </v-text-field>
      </v-row>
      <v-row>
        <!-- 摘要 -->
        <v-textarea
          counter
          type="text" 
          label="Abstract"
          v-model="abstract"
          id="inputAbstract"
          :rules="[rules.required, rules.max]"
        >
        </v-textarea>
      </v-row>
      <v-row>
      </v-row>
    </v-card>
    <v-textarea>
    </v-textarea>
  </div>
</template>

<script>
export default {
  data() {
    return {
      
    }
  },
  methods: {
    
  },
}
</script>

<style>

</style>