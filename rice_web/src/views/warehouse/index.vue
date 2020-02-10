<template>
  <div>
    <el-form class="btnForm">
      <el-form-item class="formItem">
        <el-button round class="btn" type="success" @click.native.prevent="deliver">发货</el-button>
      </el-form-item>
      <el-form-item class="formItem">
        <el-button round class="btn" type="primary" @click.native.prevent="statistics">统计</el-button>
      </el-form-item>
      <el-form-item class="formItem">
        <el-button round class="btn" type="danger" @click.native.prevent="collect">进货</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {

    }
  },
  methods: {
    deliver() {
      this.$router.push('/warehouse/deliver')
    },
    statistics() {
      this.$router.push('/warehouse/statistics')
    },
    collect() {
      this.$router.push('/warehouse/collect')
    }
  }
}
</script>

<style lang="scss" scoped>
.btnForm {
  position: relative;
  width: 420px;
  max-width: 100%;
  margin: 0 auto;
  overflow: hidden;
  .formItem {
    padding: 60px 35px 0 35px;
  }
}
.btn {
  margin: 0, auto;
  height: 150px;
  width: 100%;
  font-size: 52px;
  position: relative;
}

/* .btnRow{
 position:relative;
 background-color:#000;
 color:#fff;
 width:200px;
 height:200px;
}
.btnRow div {
  position: absolute;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
  background-color:red;
} */
</style>
