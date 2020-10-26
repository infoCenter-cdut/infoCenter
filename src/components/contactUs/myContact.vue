<template>
  <div class="contact-container">
    <div class="contact-title centertxt">
      <h4>CONTACT ME</h4>
    </div>
    <div class="contact-form">
      <form>
        <p>请填写以下表格</p>
        <div class="contact-form-fullName">
          <span class="pre-input"><i class="icon icon-user"></i></span>
          <input type="text" name="fullName" v-model="fullName" placeholder="Full name" style="width: 80%;padding-left: 3rem">
        </div>
        <div class="contact-form-email">
          <span class="pre-input"><i class="icon icon-email"></i></span>
          <input type="text" name="email" v-model="email" placeholder="Emaill address" style="width: 80%;padding-left: 3rem">
        </div>
        <div class="contact-form-content">
          <textarea name="content" v-model="content" placeholder="Don't forget that kindness is all!" style="width: 80%;padding-left: 1rem;">

          </textarea>
        </div>
        <div class="contact-form-send">
          <el-button type="danger hidden-xs">SEND A MESSAGE</el-button>
          <el-button type="danger visible-xs" size="small">SEND A MESSAGE</el-button>
        </div>
      </form>
    </div>
    <div class="contact-aside">
      <h4>LOCATION</h4>
      <p>成都市成华区二仙桥东三路1号</p>
    </div>
  </div>
</template>
<style lang="less" scoped src="./../../assets/less/myContact.less">

</style>
<script>
export default {
  name: 'myContact',
  data() {
    return {
      fullName: '',
      email: '',
      content: '',
    }
  },
  methods: {

  },
}

</script>
